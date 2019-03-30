# Collaborate using Pull

As work on the website progresses one of your coworkers, Alice, offers to help
you write the CSS stylesheet.  She will need to make a copy of your project,
and send her changes to you as she makes them.  This is where `git`'s
_distributed_ nature comes in.

## Cloning a repository

Instead of making an empty directory and running `git init` to initialize it,
Alice uses `git clone` to copy your repo.  In this section, we'll use a
directory to hold Alice's copy of the `Website` project.  You're probably in
the Website project directory, so you'll want to change to the parent
directory first.

```bash
$ cd ..
$ mkdir Alice
$ cd Alice
$ git clone ../Website
Cloning into 'Website'...
done.
$ cd Website
```

Usually `git clone` takes a URL (the various types are described in the
[documentation](https://git-scm.com/docs/git-clone)) that points to the
repository being cloned, but it can also use a file system path if the
repository is local; that's what Alice has done here.  On Unix and Linux, the
cloning operation uses hard links, which is fast and takes up very little
space because only the directory entries need to be copied, not the files.

Because Alice is working using your account (which is very bad from a security
point of view, but she can get away with it because she doesn't really exist)
she has to use local configuration variables:

```bash
$ git config user.name Alice
$ git config user.email alice@example.com
```

## Remote repositories

When Git clones a repository, it creates a reference to it called a "remote",
with the name "origin", and sets it up so that it will push and pull from the
remote repository.


```bash
$ git remote 
origin
$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```

Origin is the default location for git to pull changes from and push changes
to.  In this case, you haven't done anything new, so there's nothing for Alice
to pull.

```
$ git pull
Already up to date.
```

## Make a change and request a pull

Alice decides to start by changing the site's background color to her favorite
shade of light blue, and committing the change:

```bash
$ sed -i.bak -E '/background-color/s/#.+;/#F0F8FF;/' assets/site.css
$ git commit -a -m "change background color to light blue"
[master 565748d] change background color to light blue
 1 file changed, 1 insertion(+), 1 deletion(-)
$  git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Now she has to get the changes over to _your_ copy of the project.  Since Git
suggests using `git push`, she tries that first:

```bash
$  git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 403 bytes | 403.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: error: refusing to update checked out branch: refs/heads/master
remote: error: By default, updating the current branch in a non-bare repository
remote: is denied, because it will make the index and work tree inconsistent
remote: with what you pushed, and will require 'git reset --hard' to match
remote: the work tree to HEAD.
remote: 
remote: You can set the 'receive.denyCurrentBranch' configuration variable
remote: to 'ignore' or 'warn' in the remote repository to allow pushing into
remote: its current branch; however, this is not recommended unless you
remote: arranged to update its work tree to match what you pushed in some
remote: other way.
remote: 
remote: To squelch this message and still keep the default behaviour, set
remote: 'receive.denyCurrentBranch' configuration variable to 'refuse'.
To /home/steve/vv/prj/ms-learn/sandbox/Alice/../Website
 ! [remote rejected] master -> master (branch is currently checked out)
error: failed to push some refs to '/home/steve/vv/prj/ms-learn/sandbox/Alice/../Website'
```

Well, _that_ didn't work.  (It's worth noting that if Alice didn't have write
permission for your repository, the error message would have included "fatal:
Could not read from remote repository" -- see the next section for an
example.)  We'll see in the next unit how to set up a _shared_ repository that
both of you can push to, but for now Alice is going to have to ask you to
_pull_ her changes.  She can do that by running `git request-pull` and
emailing you the output:

```
$ git request-pull -p origin/master ../../Alice/Website
The following changes since commit a898ec56cf7f591cfa11a82d50b433e655572e75:

  make the page background a little darker (2019-03-24 08:07:47 -0700)

are available in the Git repository at:

  ../../Alice/Website

for you to fetch changes up to 565748d7955e6c9cf7e5829ac933dcc60627dbca:

  change background color to light blue (2019-03-29 08:42:23 -0700)

----------------------------------------------------------------
Alice (1):
      change background color to light blue

 assets/site.css | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
 
diff --git a/assets/site.css b/assets/site.css
index cd827ec..aa55481 100644
--- a/assets/site.css
+++ b/assets/site.css
@@ -1,2 +1,2 @@
 h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
-body { background-color:  #F0F0F0; }
+body { background-color:  #F0F8FF; }

```

A few things to notice:  `origin/master` is Alice's way of referring to the
`master` branch on the `origin` remote.  The path `../../Alice/Website` would
normally be relative to Alice's home directory or, better, the URL of a public
repository that Alice can push to (we'll see how to set that up in the next
unit) and you can pull from.

This pull request is essentially the same thing as a pull request on
[GitHub](https://github.com).  In addition to asking you to pull Alice's
changes, it is also asking you to _review_ those changes first.  Code reviews
are an important part of collaborative programming.

## An unsuccessful pull

Now, you can try to pull from Alice's repository:

```
$ cd ../../Website
$ git pull ../../Alice/Website
fatal: '../../Alice/Website' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

That didn't work because the path you took out of Alice's email was relative
to _her_ repository, not yours.  An absolute path or a public URL would have
worked in this case, but since you and Alice are going to be collaborating
more often it makes more sense to create a remote.

## Create a remote and pull from it

You create a remote using 

```
$ git remote add alice ../Alice/Website
$ git pull alice master
From ../Alice/Website
 * branch            HEAD       -> FETCH_HEAD
Updating a898ec5..565748d
Fast-forward
 assets/site.css | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Notice that you had to specify a branch.  We'll see in the next unit how to
fix that.

Behind the scenes, `git pull` is a combination of two simpler operations:
`git fetch`, which gets the changes, and `git merge`, which merges those
changes into your repository.  In this case, the merge was "fast-forward",
meaning that Alice had your latest commit in her repository, so her commit
could be added to the front of your history without any modification.

There's only one catch: this only works if Alice can access your computer, and
vice versa.  That's almost never true.

## Commands in this unit

* `git clone`
* `git pull`
* `git push`
* `git branch`
* `git remote`
