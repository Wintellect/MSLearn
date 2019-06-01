# Branch, merge, and rebase

At this point in your website project, it's become clear that contributors need to work more independently. [*NEEDS A SENTENCE SAYING WHY, PERHAPS MENTIONING THE DOWNSIDE OF THEM NOT DOING SO.--ES*]

_Branches_ make this easy. The work done "on a branch" doesn't have to be shared, and it can't interfere with work on other branches.

One of Git's advantages over older version control systems is that creating a branch is extremely fast; it amounts to writing a 40-character hash into a file under `.git/heads`.  Switching branches is also simple, because Git stores whole files rather than trying to reconstruct them from lists of changes. Merging in Git is also fast and comparatively simple. In this unit, we examine how each of these works.

## Introduction to branches

A _branch_ is simply a chain of commits "branching off" from the main line of development, like a branch on a tree.

If you are switching to Git from another version control system, you may be used to slightly different terminology. Subversion, for example, actually calls its main branch "trunk". Git calls it `master`. You can rename `master`, just as you can rename any other branch, and some teams do this when switching to Git from some other version control system.

Initially, a branch starts with a commit on `master` (or some other branch). It grows a separate history chain as commits are added; eventually it can have its changes merged back into `master`. (We'll see two different ways of doing that -- merging and rebasing -- later on in this unit.) 

It ends up looking like this:

```
master:  ...A---B---C---D
                \
branch:          E---F---G
```

## Create a branch

Alice wants to add some CSS to style the cat pictures, so she creates a _topic branch_ (sometimes called a _feature branch_) and calls it `add-style`: 

```
$ cd ~/sandbox/Alice/Cats
$ git branch add-style
$ git checkout add-style
Switched to branch 'add-style'
```

Throw-away branch names are  [*MISSING SOMETHING HERE? --ES*]
The `git branch` command creates the branch, starting with the current HEAD.
The `git checkout` command switches to the new branch.

We already encountered `checkout` as a way of replacing files in the working tree by
getting it from the index. You can also specify a commit to take the files from, in which case both the index and the working tree are updated. With no paths at the end of the argument list, `checkout` updates *everything* in the working tree and the index to match the specified commit, in this case the head of the branch.

While Alice is working on the CSS, Bob is busy creating a branch for adding a picture of his cat. He uses a popular shortcut. Passing the `-b` option to `checkout` creates a branch, then switches to it.

That's by far the most common way of creating a branch:

```
$ cd ~/sandbox/Bob/BobCats
$ git checkout -b addCat
Switched to a new branch 'addCat'
```

## Work on a branch

Now that Alice and Bob are working on private branches, they are free to make changes without interfering with one another. Bob starts by adding a picture of his cat:

```
$ sed -i.bak -e '/Eventually/ c <img src="assets/bobcat2-317x240.jpg">' index.html
$ cp ../../bobcat2-317x240.jpg assets
$ git add assets
$ git commit -a -m "Add picture of Bob's cat"
[addCat 61ad3ec] Add picture of Bob's cat
 2 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 assets/bobcat2-317x240.jpg
```

While Alice adds her style:

```
$ cd ~/sandbox/Alice/Cats
$ echo '.cat {max-width: 40%; padding: 5}' >> assets/site.css
$ git commit -a -m "Add style for cat pictures"
[add-style e9528be] Add style for cat pictures
 1 file changed, 1 insertion(+)
```

Right now, the two contributors are working on parallel. At this point, their two working trees look like this:

```
Alice:  ...o---m
                \
  add-style		 A		 

Bob:    ...o---m
                \
  addCat		 B				 
```

Note that the master branch, `m` in the diagram, has no commits following it.

## Fast-forward merge

At this point. Alice wants to make her style available to everyone else, so she merges her branch and pushes it. Because no work has been done on `master`, she can do this as a "fast-forward" merge.

```
$ git checkout master
$ git pull
$ git merge --ff-only add-style
Updating 88bed5a..e9528be
Fast-forward
 assets/site.css | 1 +
 1 file changed, 1 insertion(+)
$ git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 411 bytes | 205.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
To /home/steve/sandbox/Cats.git
   88bed5a..cddf95c  master -> master
```

Now Alice's working tree and the shared repo both look like:

```
        ...o---m---A        A: Add style for cat pictures
```

Note that Alice pulled before merging, in case somebody had pushed a change while she was working, and she used the `--ff-only` option to make the merge fail if it *wasn't* fast-forward. That wasn't strictly necessary in this case, but it's a good habit to get into.

If you have tests, you should run them after every merge to make sure that what you're pushing to the shared repo passes the test suite.  (Using hooks, it's possible to run tests automatically and block the push if they fail.)

## Merge without fast-forward

Alice could have forced Git to create a merge commit by using the `--no-ff` option. In that case, the history would have looked like:

```
        ...o---m---M        m: previous master
                \ /         M: new merge commit
				 A          A: Add style for cat pictures
```

Merge commits are used for additional metadata in some projects. In addition to recording the date and time of the merge, and the developer's name and email, you can use the `--signoff` option to include a "signed off by:" line. The `-S` option adds a digital signature. Merge commits like this are often used in large distributed projects. [*ADD A SENTENCE FOR A "FOR INSTANCE WHEN..." OR "...TO KEEP FROM [THIS PROBLEM]. OTHERWISE I'M NOT SURE OF THE VALUE. WELL, I CAN GUESS, BUT I SHOULDN'T HAVE TO GUESS.--ES*]

Sometimes a non-fast-forward merge can't be avoided. Let's look at Bob's situation.

```
$ cd ~/sandbox/Bob/BobCats
$ git checkout master
Switched to branch 'master'
Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
$ git pull
Updating 88bed5a..cddf95c
Fast-forward
 assets/site.css | 1 +
 1 file changed, 1 insertion(+)
```

Now Bob's history looks like:

```
Bob:    ...o---m---A      A: Add style for cat pictures
                \
                 B        B: Add picture of Bob's cat
```

If Bob uses `git merge addCat` at this point, his history will look like:

```
Bob:    ...o---m---A---M
                \     /
                 B---/
```

Some projects prefer this kind of history. It keeps Bob's commits exactly the way he made them, so if any of them were signed the signatures would still be valid after the merge. Solo developers and many teams usually prefer something simpler. Fortunately Git lets Bob change his history so that he can use a fast-forward merge.

## Rebase instead of merge

[*WE NEED AN INTRODUCTION TO REBASE AND A DIRECT DEFINITION--ES*]
In order to simplify his history, Bob uses:

```
$ git checkout addCat
Switched to branch 'addCat'
$ git rebase master
First, rewinding head to replay your work on top of it...
Applying: Add picture of Bob's cat
```

Now his history looks like:

```
Bob:    ...o---m---A
                    \
                     B       addCat
```

What Git did was to compute the difference between the commits `m` and `B`, and apply that difference as a patch to `A`.

Bob decides that there's no reason to merge at this point, so he simply continues to work on his branch:

```
$ sed -i.bak -e 's/<img /<img class=".cat" /' index.html
$ git commit -a -m "Add style class to cat picture"
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Now Bob's history looks like:

```
Bob:    ...o---m---A
                    \
                     B---C   addCat
```

Bob could have amended commit B rather than making a new commit on top of it; that would lead to a simpler-looking history, with a single commit representing all of his changes. Many teams prefer simple histories, but as we'll see later there are better ways of getting there.

[*THIS UNIT OOES A GOOD JOB OF SAYING HOW-TO, BUT AT THE END OF IT I'M NOT SURE IF I GROK WHEN-TO. I'M NOT SURE IF THAT MEANS I NEED A BETTER SCENARIO SET-UP (OH NO WHAT HAPPENED TO THE KITTY PICTURE?) OR A WRAP UP THAT GIVES ME EXCPLICIT ADVICE ABOUT WHEN EACH OPTION IS THE BEST CHOICE. YOUR THOUGHTS? --ES*]

## Summary

In this unit you learned how to create branches, and several different ways of merging them. You learned about creating branches using:

* [`git branch`](https://git-scm.com/docs/git-branch), which creates a branch
* [`git checkout`](https://git-scm.com/docs/git-checkout), which switches to a branch, and [`git checkout -b`](https://git-scm.com/docs/git-checkout) which creates a branch *and* switches to it
* [*MISSING SOMETHING HERE? I'M GUESSING REBASE--ES*]  which revises commits to re-arrange branches,  and
* [`git merge`](https://git-scm.com/docs/git-merge), which combines branches.

In the next unit you learn how to simplify history using `merge --squash` and `rebase --interactive`, and how to resolve merge conflicts.
