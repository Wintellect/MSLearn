# Collaborate using a shared repo

Directly pulling from someone else's repository works, provided you're both on the same network, but it's a clumsy process -- and most collaborators are not on the same network. It's much better to set up a central repository to which everyone involved can push as well as pull from.

When you tell Bob about your project, and he asks to participate too, that's exactly what you do.

## Create a bare repository

What you need is a repository that doesn't have a working tree, to avoid the problem Alice had trying to push. That's called a _bare repository_.

A bare repo has several advantages:

- Without a working tree, everybody can push changes without having to worry about which branch is checked out.
- It's easy for Git to detect when somebody else has pushed changes that might conflict with yours (because your push wouldn't be fast-forward, and Git' default is to reject it so that you can merge the new files with your own).
- A shared repo scales to any number of developers. You only have to know about the shared repo rather than about all the other people from whom you might need to pull.
- By putting the shared repo on a server that you can all access, you don't have to worry about firewalls and permissions.
- You don't need separate accounts on the server, because Git keeps track of who made each commit. GitHub has millions of users all sharing the `git` account. (Everyone uses `ssh`, and users are distinguished by their public keys.) 
  
You can set it up using:

```
$ cd ~/sandbox
$ mkdir Cats.git
$ cd Cats.git
$ git init --bare
Initialized empty Git repository in /home/steve/sandbox/Cats.git/
```

(The convention is to give bare repositories a name ending with `.git` to distinguish them from working trees.)

Now you have to get the contents of _your_ repo into the new one. You set up an `origin` remote and push to it.

```
$ cd ~/sandbox/Cats
$ git remote add origin ../Cats.git
$ git push origin master
Counting objects: 40, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (28/28), done.
Writing objects: 100% (40/40), 3.82 KiB | 559.00 KiB/s, done.
Total 40 (delta 6), reused 0 (delta 0)
To ../Cats.git
 * [new branch]      master -> master
```

You want push and pull to use `origin`'s master branch by default, just as if you'd made your repo by cloning in the first place. To do so, you need to tell Git which branch to track:

```
$ git branch --set-upstream-to origin/master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Git would have complained if you had tried to do this before the initial push, because there weren't any branches in the new repository yet. Git won't let you track a branch that doesn't exist.  (You get exactly the same error message, "the requested upstream branch [...] does not exist," if you get the name of either the branch (maybe you used "trunk" because you're used to Subversion) or the remote wrong.  That's not surprising because all Git is doing is looking in `.git/refs/remotes` for a file called `origin/trunk`.

## Setup for collaborators

Now all Bob has to do is clone the bare repository:

```
$ cd ~/sandbox
$ mkdir Bob
$ cd Bob
$ git clone ~/sandbox/Cats.git/ BobCats
Cloning into 'BobCats'...
done.
$ cd BobCats
$ git config user.name Bob
$ git config user.email bob@example.com
```

Notice that Bob specified a different directory to clone into. Git doesn't care what you call a working tree, because it never looks outside of it.

Alice already has a remote called `origin`, so all she has to do is change which repo it points to:

```
$ cd ~/sandbox/Alice/Cats
$ git remote set-url origin ~/sandbox/Cats.git
$ git push
Everything up-to-date
```

The push wasn't necessary, but it's a simple way of making sure the remote is set up with the correct defaults.

## The basics of collaboration

Now that Bob is set up to work on the website, he decides to wrap the horizontal rule at the bottom of the page with a footer.

```
$ cd ~/sandbox/Bob/BobCats
$ sed -i.bak -e 's/<hr>/<footer><hr><\/footer>/' index.html
$ git commit -a -m "Put a footer at the bottom of the page"
1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 315 bytes | 315.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To /home/steve/sandbox/Cats.git
   37903fd..99fbbca  master -> master
```

He sends email to you and Alice to let you know that he's made a change.

Meanwhile, Alice decides to add a nav bar to the page, and adds a line to the style sheet for it as well.

```
$ cd ~/sandbox/Alice/Cats
$ sed -i.bak -e '/<body>/a<nav> <a href="./index.html">home<\/a> <\/nav>' index.html
$ echo 'nav { background-color: #C0D8DF; }' >> assets/site.css
```

Then Alice sees Bob's email, and decides to pull his changes before she commits her own. (If she had already committed her change, she would have a different problem, which we discuss in the next unit.) She types:

```
$ git pull
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From /home/steve/sandbox/Cats
   37903fd..99fbbca  master     -> origin/master
Updating 37903fd..99fbbca
error: Your local changes to the following files would be overwritten by merge:
	index.html
Please commit your changes or stash them before you merge.
Aborting
```

It looks as though Git prevented a problem. Only `index.html` would have been overwritten; Bob didn't make any changes in `site.css`. If Alice hadn't changed `index.html`, Git would have gone ahead and committed the merge. If it did so, it could have caused trouble later on. (This is one reason why it's always a good idea to run tests after a merge.)

Alice uses `git diff` to see what Bob's changes were, specifying both the branch (`origin`) and the file (`index.html) to compare.


```
$  git diff origin -- index.html
diff --git a/index.html b/index.html
index 8ff78df..b8732b6 100644
--- a/index.html
+++ b/index.html
@@ -6,8 +6,9 @@
 <link rel="stylesheet" href="assets/site.css">
 </head>
 <body>
+<nav> <a href="./">home</a> </nav>
 <h1>Our Furry Friends</h1>
 <p> Eventually we will put cat pictures here.
-<footer><hr></footer>
+<hr>
 </body>
 </html>
```

Alice can see that, although she and Bob both changed the same file, their changes don't overlap. She decides to _stash_ her changes. `git stash` saves the state of the working tree and index by making a couple of temporary commits. Think of the stash as a way to save your current work while you do something else, without making a "real" commit or affecting your repository history.

In reality, Alice should have stashed or committed her changes before she
tried to pull. Pulling to a "dirty" working tree is risky, because it can do things from which you can't recover.

```
$ git stash
Saved working directory and index state WIP on master: 37903fd change background color to light blue
```

Now it's safe for Alice to pull, after which she can "pop" the stash, which is organized as a stack. (In fact, `git stash` is shorthand for `git stash push`.  It's a lot like the stack where you put bills that you haven't gotten around to paying yet.) 

```
$ git pull
Updating 37903fd..99fbbca
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
Dropped refs/stash@{0} (cad3c4cd27de5ca9b0a6e88b379fa8fda43246f5)
```

Popping the stash merges the changes. If changes overlap, there may be a conflict. We look later at how to resolve those situations.

At this point Alice can continue working, or simply commit and push her changes.

She gives footers the same style as nav bars.

```
$ sed -i.bak -e 's/nav/nav, footer/' assets/site.css
$ git commit -a -m 'add nav bar to page'
[master 88bed5a] add nav bar to page
 2 files changed, 2 insertions(+)
$ git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 495 bytes | 247.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
To /home/steve/sandbox/Cats.git
   99fbbca..88bed5a  master -> master
```

If Alice had committed her changes rather than stashing them, the situation
would have been somewhat different. She would have had to make a branch and
either merge or rebase her changes.  (Branches, merging, and rebasing are
covered in the next unit.)

Had Alice begun by working on a branch in the first place she would have saved herself quite a lot of trouble. We'll see
how to do that in the next unit; for now it's worth pointing out that branching and rebasing is _exactly_ what the stash commands accomplish behind the scenes.

## Summary

In this unit, you learned how to set up a bare repository that can be shared among a group of developers, and about the Git commands

* [`git commit --bare`](https://git-scm.com/docs/git-commit), which sets up a repo that can be shared
* [`git push`](https://git-scm.com/docs/git-push), which merges changes with a remote repo, and
* [`git stash`](https://git-scm.com/docs/git-stash), which saves un-committed changes so that you can merge safely.

In the next unit, you learn how to create and merge branches.
