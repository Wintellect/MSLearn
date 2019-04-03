# Branching, merging, and rebasing

At this point it's become clear that you need a way for people to work more
independently.  Branches make this easy -- work "on a branch" doesn't have to
be shared.

## Introduction to refs and branches

A branch is simply a chain of commits "branching off" from the main line of
development like a branch on a tree.  (Some version control systems,
Subversion for example, actually call their main branch "trunk"; Git calls it
`master`.  You can rename `master`, just as you can rename any other branch,
and some teams do this when switching to Git from some other version control
system.)

Initially a branch starts with a commit on `master` and grows a separate
history chain as commits are added to it; eventually it can have its changes
merged back into `master`.  Branches can also be deleted (in which case any
work done on them will eventually disappear) or abandoned -- creating a branch
is a good way to try something out.



## Work on a branch



* discuss feature branches.
* git branch
* git checkout -b
* merge (fast-forward)
* `git stash`
* merge (non-fast-forward)
* we've already seen rebase in the form of `git pull --rebase`.  Time to show
  `git rebase` and `git rebase -i` as alternatives to merge.
* `git merge --abort`
