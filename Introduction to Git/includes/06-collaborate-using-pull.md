# Collaborate using Pull

You've been working on the cat website on your own for a while. After a pizza party at your house, your friend and fellow cat-lover
[Alice](https://en.wikipedia.org/wiki/Alice_and_Bob) offers to help, and you agree with delight. Alice needs to make a copy of your project, and she will want to send her changes to you as she makes them.

This is where `git`'s _distributed_ nature comes in. It permits two or more people to work together on a project without fear of overwriting one another's work.

## Clone a repository

Instead of making an empty directory and running `git init` to initialize it, Alice uses `git clone` to copy your repo. Since she's already on your household Wi-Fi network, she can mount the directory as a network share; for now (and the sake of simplicity) we make an ordinary directory called `Alice` to take the place of her home directory. You're probably in your working tree project directory, so you need to change to the parent directory first.

```
$ cd ~/sandbox
$ mkdir Alice
$ cd Alice
$ git clone ../Cats
Cloning into 'Cats'...
done.
$ cd Cats
```

You can give `git clone` a filesystem path as we did here; an SSH path (e.g. `git@example.com:alice/Cats` -- you'll be familiar with this form if you've used Rsync or Scp); or a URL (typically starting with `file:`, `git:`, or `ssh`). The various types are described in the [documentation for git clone](https://git-scm.com/docs/git-clone). On Unix and Linux, the cloning operation uses hard links, which is fast and takes up very little space because only the directory entries need to be copied, not the files.

Because Alice doesn't have her copy of Git properly configured yet (which is not surprising since she's a fictional character), she sets local configuration variables for her name and email:

```
$ git config user.name Alice
$ git config user.email alice@example.com
```

## Remote repositories

When Git clones a repository, it creates a reference to the repo called a _remote_, with the name `origin`, and sets it up so that it will push and pull from the remote repository.


```
$ git remote 
origin
$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```

Origin is the default location for Git to pull changes from and push changes to.
[*CAN WE GIVE AN ANALOGY HERE? I AM ENVISIONING THIS SOMETHING LIKE A DROPBOX DIRECTORY, OR PERHAPS THE PHOTOS STORED ON MY PHONE. I WORK LOCALLY, BUT -- AT THE TOUCH OF A BUTTON -- CAN SAY, "YO, UPDATE GIT, WHICH IS WHERE WE KEEP THE REAL COPY." BUT I AM UNSURE THAT IS AN ACCURATE VISUALIZATION. --ES*]

So far you haven't done anything new, so there's nothing for Alice to pull.

```
$ git pull
Already up to date.
```

## Alice makes a change and a pull request

Alice decides to start working on the cat website by changing the site's background color. She experiments locally on the right shade, and ultimately chooses her favorite shade of light blue. When she is ready, she commits the change:

```
$ sed -i.bak -E '/background-color/s/#.+;/#F0F8FF;/' assets/site.css
$ git commit -a -m "change background color to light blue"
[master 37903fd] change background color to light blue
 1 file changed, 1 insertion(+), 1 deletion(-)
$  git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Git gives Alice a hint about the next step, which is to get the changes over to _your_ copy of the project. Since Git suggests using `git push`, she tries that first:

```
$ git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 402 bytes | 201.00 KiB/s, done.
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
To /home/steve/sandbox/Alice/../Cats
 ! [remote rejected] master -> master (branch is currently checked out)
error: failed to push some refs to '/home/steve/sandbox/Alice/../Cats'
```

Well, _that_ didn't work. It would have worked if Alice had pushed to a different branch *and* had permission to write to your repo. (It's worth noting that if Alice *didn't* have write permission for your repository, she would have gotten a "fatal" error message instead.)

[*AGAIN, ESTHER THE BEGINNER! I THINK I WANT A LITTLE EXPLANATION ABOUT WHY THIS DOESN'T WORK. MY INITIAL EXPECTATION IS THAT ONCE I SHARE INFO WITH SOMEONE, I CAN UPLOAD AS WELL AS DOWNLOAD. I SUPPOSE THE ANALOGY IS THAT INITIALLY I HAVE READ-ONLY PERMISSIONS, AND UNTIL YOU GIVE ME WRITE-ONLY I MUST BEG YOU TO UPDATE THE FILES WITH MY CHANGES. BUT CAN YOU HELP ME GRASP THIS CONCEPT WITH A LITTLE MORE ASSURANCE THAT I'VE GOT IT RIGHT? PROBABLY ONLY A FEW SENTENCES OR AN ANALOGY. --ES*]

For now, Alice has to ask _you_ to _pull_ her changes. She can do that by running `git request-pull` and emailing you the output:

```
$ git request-pull -p origin/master ../../Alice/Cats
The following changes since commit 2c01c0503149e7c3bbcfdb90b54d576e7e4e177b:

  Make the page background a little darker (2019-05-15 12:25:20 -0700)

are available in the Git repository at:

  ../../Alice/Cats 

for you to fetch changes up to 37903fd0338e070bacb2a7baeb9ed83875252f37:

  change background color to light blue (2019-05-15 13:23:40 -0700)

----------------------------------------------------------------
Alice (1):
      change background color to light blue

 assets/site.css | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/assets/site.css b/assets/site.css
index 3866268..ceaebf9 100644
--- a/assets/site.css
+++ b/assets/site.css
@@ -1,3 +1,3 @@
 h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
 body { font-family: serif; }
-body { background-color:  #C0C0C0; }
+body { background-color:  #F0F8FF; }
```

Notice a few thingsabout this process:

 * `origin/master` is Alice's way to refer to the `master` branch on the `origin` remote.
 * Instead of the path `../../Alice/Cats`, Alice would normally be relative to Alice's network share. It would be better to use the URL of a public repository to which Alice can push (We'll see how to set that up in the next unit) and from which you can pull.
 *  Normally, Alice would redirect the pull request into a file, or pipe it directly into an email client.

This pull request is essentially the same thing as a pull request on [GitHub](https://github.com). In addition to the pull request asking you to pull Alice's changes, it also gives you a chance to review her changes before you incorporate her work into the website. Code reviews are an important part -- some would say the *most* important part -- of collaborative programming.

## An unsuccessful pull

Now, you can try to pull from Alice's repository:

```
$ cd ../../Cats
$ git pull ../../Alice/Cats
fatal: '../../Alice/Cats' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

That didn't work because the path you took out of Alice's email was relative to _her_ repository, not yours. An absolute path or a public URL would have worked in this case.

However, because you and Alice are going to collaborate regularly, it makes more sense to create a remote.

## Create a remote and pull from it

You create a remote using:

```
$ git remote add alice ../Alice/Cats
```

and pull from it with:

```
$ git pull alice master
From ../Alice/Cats
 * branch            HEAD       -> FETCH_HEAD
Updating 2c01c05..37903fd
Fast-forward
 assets/site.css | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Notice that you have to specify a branch, `master`, in the pull command. We'll see in the next unit how to fix that by setting an upstream URL.

Behind the scenes, `git pull` is a combination of two simpler operations: `git fetch`, which gets the changes, and `git merge`, which merges those changes into your repository. In this case, the merge was _fast-forward_, meaning that Alice had your latest commit in her repository, so her commit could be added to the front of your history without any modification.

[*WOULD IT MAKE SENSE TO SHOW WHAT IT'D LOOK LIKE IF IT WASN'T FAST FORWARD? SO I HAVE AN IDEA WHAT TO EXPECT? UP TO YOU ON THIS ONE.--ES*]

## Summary

In this unit you learned how to collaborate with another developer using nothing more than a thumb drive or a network share. You used:

* [`git clone`](https://git-scm.com/docs/git-clone),  which clones (copies) a repo
* [`git pull`](https://git-scm.com/docs/git-pull), which fetches commits from another repo and merges them into
  yours
* [`git request-pull`](https://git-scm.com/docs/git-request-pull), which creates a pull request
* [`git branch`](https://git-scm.com/docs/git-branch), which lists,  creates, modifies, or deletes branches
* [`git remote`](https://git-scm.com/docs/git-remote), which lists, creates, modifies, or deletes remotes.

There have been brief mentions of `git push`, `git fetch`, and `git merge`; you learn more about those in the next unit. There have been even briefer mentions of:

* [`ssh`](https://linux.die.net/man/1/ssh), the Secure SHell command, which lets you log in on another computer through the network
* [`scp`](https://linux.die.net/man/1/scp) (secure copy), which copies files using `ssh`, and
* [`rsync`](https://linux.die.net/man/1/rsync) (remote sync), which is similar to `scp` but faster and more versatile.

In the next unit, you learn how to set up and use a shared repository, which makes collaborating much simpler and more convenient.