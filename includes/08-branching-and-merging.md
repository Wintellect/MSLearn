# Branch, merge, and rebase

At this point it's become clear that you need a way for people to work more
independently.  Branches make this easy -- work "on a branch" doesn't have to
be shared.

## Introduction to branches

A branch is simply a chain of commits "branching off" from the main line of
development like a branch on a tree.  (Some version control systems,
Subversion for example, actually call their main branch "trunk"; Git calls it
`master`.  You can rename `master`, just as you can rename any other branch,
and some teams do this when switching to Git from some other version control
system.)

Initially a branch starts with a commit on `master` and grows a separate
history chain as commits are added to it; eventually it can have its changes
merged back into `master` (we'll see two different ways of doing that --
merging and rebasing -- later on in this unit).

## Work on a branch

Alice decides to do some more work on the style sheet, so she starts a new
"topic branch" (sometimes called a "feature branch") called `style`:

```
$ git branch style
$  git checkout style
Switched to branch 'style'
```

The `git branch` command creates the branch, starting with the current HEAD.
The `git checkout` command switches to the new branch.  We've already
encountered `checkout` as a way of replacing files in the working tree by
getting it from the index.  You can also specify a commit to take the files
from, in which case both the index and the working tree will be updated.  With
no paths at the end of the argument list, `checkout` updates _everything_ in
the working tree and the index from the specified commit, in this case the
head of the branch.

You can combine creating a branch and switching to it by passing the `-b`
option to `checkout`.  That's by far the most common way of creating a branch.

Now that Alice is working on a private branch, she's free to make changes
without interfering with anyone else's work.

```

```

* discuss feature branches.
* git branch
* git checkout -b
* merge (fast-forward)
* `git stash`
* merge (non-fast-forward)
* we've already seen rebase in the form of `git pull --rebase`.  Time to show
  `git rebase` and `git rebase -i` as alternatives to merge.
* `git merge --abort`
