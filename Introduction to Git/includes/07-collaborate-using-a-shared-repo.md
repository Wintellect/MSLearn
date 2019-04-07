# Collaborate using a shared repo

Directly pulling from someone else's repository works, provided you're both on
the same network, but it's clumsy.  It's much better to set up a central
repository that you can both push to as well as pull from.  When Bob decides
to join the project as well, that's exactly what you do.

## Set up a bare repository

What you need is a repository that doesn't have a working tree, to avoid the
problem Alice had trying to push.  That's called a "bare repository", and you
can set it up using:

```
$ cd ..
$ mkdir Website.git
$ cd Website.git
$ git init --bare
Initialized empty Git repository in .../sandbox/Website.git/
```

(The convention for bare repositories is to give them a name ending with
`.git` to distinguish them from working trees.)

Now you have to get the contents of _your_ repo into the new one.  You set up
an `origin` remote and push to it.

```
$ cd ../Website
$ git remote add origin ../Website.git
$ git push origin master
Counting objects: 40, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (28/28), done.
Writing objects: 100% (40/40), 3.80 KiB | 432.00 KiB/s, done.
Total 40 (delta 6), reused 0 (delta 0)
To ../Website.git
 * [new branch]      master -> master
```

Since you want push and pull to use `origin`'s master branch by default, the
way they do in a cloned repository, you need to tell Git which branch to
track:

```
$ git branch --set-upstream-to origin/master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Git would have complained if you had tried to do this before the initial push,
because there weren't any branches in the new repository yet and Git won't let
you track a branch that doesn't exist.

## Setup for collaborators

Now all Bob has to do is clone the bare repository:

```
$ mkdir Bob
$ cd Bob
$ git clone ../Website.git/
Cloning into 'Website'...
done.
$ cd Website
$ git config user.name Bob
$ git config user.email bob@example.com
```

Alice already has a remote called `origin`, so all she has to do is change
which repo it's pointing to:

```
$ cd ../../Alice/Website
$ git remote set-url origin ../../Website.git
$ git push
Everything up-to-date
```

## The basics of collaboration

Bob decides to change the page's title, currently "Sample Page", to match the
`h1` tag:

```
$ cd ../../Bob/Website
$ sed -i.bak -e 's/Sample page/Hello, everybody!/' index.html
$ git commit -a -m "make page title match heading"
$ git push
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 284 bytes | 284.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To /home/steve/vv/prj/ms-learn/sandbox/Bob/../Website.git/
   565748d..8af5fea  master -> master
```

He sends email to the rest of his team to let them know that he's made a
change.

Meanwhile, Alice decides to add a nav bar to the page, and adds a line to the
style sheet for it as well.

```
$ cd ../../Alice/Website
$ sed -i.bak -e '/<body>/a<nav> <a href="./">home<\/a> <\/nav>' index.html
$ echo 'nav { background-color: #C0D8DF; }' >> assets/site.css
```

Then she sees Bob's email, and decides to pull his changes before she commits
her own.  (If she had already committed her change, she would have a different
problem, which we'll discuss in the next unit.)

```
$ git pull
Updating 565748d..8af5fea
error: Your local changes to the following files would be overwritten by merge:
	index.html
Please commit your changes or stash them before you merge.
Aborting
```

It looks as though Git has prevented a problem.  Note that only `index.html`
would have been overwritten; Bob didn't make any changes in `site.css`.  Alice
uses `git diff` to see what Bob's changes were.

```
$  git diff origin -- index.html
diff --git a/index.html b/index.html
index a02a169..7692b01 100644
--- a/index.html
+++ b/index.html
@@ -2,10 +2,11 @@
 <html>
 <head>
 <meta charset='UTF-8'>
-<title>Hello, everybody!</title>
+<title>Sample page</title>
 <link rel="stylesheet" href="assets/site.css">
 </head>
 <body>
+<nav> <a href="./">home</a> </nav>
 <h1>Hello, everybody!</h1>
 <p> If this were a real website there would be content here.
 <hr>
```

She can see that, although she and Bob have both changed the same file, their
changes don't overlap.  She decides to stash her changes; `git stash` saves
the state of the working tree and index by making a couple of temporary
commits.  (She should have stashed or committed her changes _before_ trying to
pull.  Pulling to a "dirty" working tree is risky, because it can do things
you can't recover from.)

```
$ git stash
Saved working directory and index state WIP on master: 565748d change
background color to light blue
```

Now it's safe for Alice to pull, after which she can "pop" the stash, which is
organized as a stack.  (In fact, `git stash` is shorthand for `git stash
push`.) 

```
$ git pull
Updating 565748d..8af5fea
Fast-forward
 index.html | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git stash pop
Auto-merging index.html
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   assets/site.css
	modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (440daeff1849a5f6216fbb6960bfe63d8505a67d)
```

Popping the stash merges the changes; if changes overlap there may be a
conflict, which we will look at later.

At this point Alice can continue working, or commit and push her changes.

```
$ git commit -a -m 'add nav bar to page'
[master 33b6bc7] add nav bar to page
 2 files changed, 2 insertions(+)
$ git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 486 bytes | 486.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
To ../../Website.git
   8af5fea..33b6bc7  master -> master
```

If Alice had committed her changes rather than stashing them, the situation
would have been somewhat different -- she would have had to make a branch and
either merge or rebase her changes.  If she'd been working on a branch in the
first place she would have saved herself quite a lot of trouble.  We'll see
how to do that in the next unit; for now it's worth pointing out that
branching and rebasing is _exactly_ what the stash commands accomplish behind
the scenes.

## Commands in this unit

* `git push`
* `git stash`
