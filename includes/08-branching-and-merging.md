# Branch, merge, and rebase

At this point it's become clear that you need a way for people to work more
independently.  Branches make this easy -- work "on a branch" doesn't have to
be shared, and can't interfere with work on other branches.  One of Git's
advantages over older version control systems is that creating a branch is
extremely fast, and merging is comparatively simple.

## Introduction to branches

A branch is simply a chain of commits "branching off" from the main line of
development like a branch on a tree.  (Some version control systems,
Subversion for example, actually call their main branch "trunk"; Git calls it
`master`.  You can rename `master`, just as you can rename any other branch,
and some teams do this when switching to Git from some other version control
system.)

Initially a branch starts with a commit on `master` (or some other branch) and
grows a separate history chain as commits are added to it; eventually it can
have its changes merged back into `master` (we'll see two different ways of
doing that -- merging and rebasing -- later on in this unit).  It ends up
looking like this:

```
master:  ...A---B---C---D
                \
branch:          E---F---G
```

## Create a branch

Alice wants to add some CSS to style cat pictures, so she creates a
"topic branch" (sometimes called a "feature branch") called
`add-style-for-img`: 

```
$ git branch add-style-for-cats
$ git checkout add-style-for-cats
Switched to branch 'add-style-for-cats'
```

The `git branch` command created the branch, starting with the current HEAD.
The `git checkout` command switched to the new branch.  We've already
encountered `checkout` as a way of replacing files in the working tree by
getting it from the index.  You can also specify a commit to take the files
from, in which case both the index and the working tree will be updated.  With
no paths at the end of the argument list, `checkout` updates *everything* in
the working tree and the index to match the specified commit, in this case the
head of the branch.

Meanwhile Bob creates a branch for adding a picture of his cat, using a
popular shortcut:  passing the `-b` option to `checkout` first creates a
branch, then switches to it.  That's by far the most common way of creating a
branch:

```
$ cd ../../Bob/BobCats
$ git checkout -b addCat
```

## Work on a branch

Now that Alice and Bob are working on private branches, they are free to make
changes without interfering with one another.  Bob starts by adding a picture
of his cat:

```
$ sed 
$ git commit -a -m "Add picture of Bob's cat"
```

While Alice adds her style:

```
$ cd ../../Alice/Cats
$ echo 'img {width: 100%;}' >> assets/site.css TODO
$ echo 'div .catbox {width: 40%; }' >> assets/site.css
$ git commit -a -m "Add style for cat pictures"
```

At this point, their two working trees look like this:

```
Alice:  ...o---m
                \
				 A		 

Bob:    ...o---m
                \
				 B				 
```

Note that the master branch, `m` in the diagram, has no commits following it.

## Fast-forward merge

At this point Alice wants to make her style available to everyone else, so she
merges her branch and pushes it.  Because no work has been done on `master`,
she can do this as a "fast-forward" merge, and she uses the `--ff-only`
option, which will make the merge fail if it's not fast-forward.

```
$ cd ../../Alice/Cats
$ git checkout master
$ git merge --ff-only add-style-for-cats
$ git push
```

Now Alice's working tree and the shared tree both look like:

```
Alice:  ...o---m---A
```

Alice could have forced Git to create a merge commit by using the `--no-ff`
option.  If a team is using code reviews, they will often have the reviewer
perform the merge, using the merge commit to record their name and the date.
In large distributed projects the merge will also include a "signed off by:"
line, added with the `--signoff` option, and possibly a digital signature
(`-S` option).  In that case, the tree would have lookd like:

```
Alice:  ...o---m---M
                \ /
				 A		
```

* merge (non-fast-forward)
* we've already seen rebase in the form of `git pull --rebase`.  Time to show
  `git rebase` and `git rebase -i` as alternatives to merge.
* `git merge --abort`
