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
`add-style`: 

```
$ git branch add-style
$ git checkout add-style
Switched to branch 'add-style'
```

Throw-away branch names are 
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
  add-style		 A		 

Bob:    ...o---m
                \
  addCat		 B				 
```

Note that the master branch, `m` in the diagram, has no commits following it.

## Fast-forward merge

At this point Alice wants to make her style available to everyone else, so she
merges her branch and pushes it.  Because no work has been done on `master`,
she can do this as a "fast-forward" merge.

```
$ cd ../../Alice/Cats
$ git checkout master
$ git pull
$ git merge --ff-only add-style-for-cats
$ git push
```

Now Alice's working tree and the shared repo both look like:

```
        ...o---m---A        A: Add style for cat pictures
```

There are a few things worth noting here:  Alice pulled before merging, in
case somebody had pushed a change while she was working, and she used the
`--ff-only` option to make the merge fail if it *wasn't* fast-forward (which
wasn't strictly necessary in this case, but it's a good habit to get into).
If you have tests, you should run them after every merge to make sure that
what you're pushing to the shared repo passes them.  (Using hooks, it's
possible to run tests automatically and block the push if they fail.)

## Merge without fast-forward

Alice could have forced Git to create a merge commit by using the `--no-ff`
option.  In that case, the history would have looked like:

```
        ...o---m---M        m: previous master
                \ /         M: new merge commit
				 A          A: Add style for cat pictures
```

Merge commits are used for additional metadata in some projects.  In addition
to recording the date and time of the merge, and the name and email of the
developer who made it, you can use the `--signoff` option to include a "signed
off by:"  line.  The `-S` option adds a digital signature.  Merge commits like
this are often used in large distributed projects.

Sometimes a non-fast-forward merge can't be avoided.  Let's look at Bob's
situation.

```
$ cd ../../Bob/BobCats
$ git checkout master
$ git pull
```

Now Bob's history looks like:

```
Bob:    ...o---m---A
                \
                 B        B: Add picture of Bob's cat
```

If Bob uses `git merge addCat` at this point, his history will look like:

```
Bob:    ...o---m---A---M
                \     /
                 B---/
```

Some teams prefer this kind of history, but most prefer something simpler.
Fortunately Git lets Bob change his history so that he can use a fast-forward
merge. 

## Rebase instead of merge

In order to simplify his history, Bob uses

```
$ git checkout addCat
$ git rebase master
```

Now his history looks like:

```
Bob:    ...o---m---A
                    \
                     B       addCat
```

What Git did was to compute the difference between the commits `m` and `B`,
and apply that difference as a patch to A.

Bob decides that there's no reason to merge at this point, so he simply
continues to work on his branch:

```
$ sed FIXME
$ git commit -a -m "Add style class to cat picture"
```
Now his history looks like:

```
Bob:    ...o---m---A
                    \
                     B---C   addCat
```

Bob could have amended commit B rather than making a new commit on top of it;
that would lead to a simpler-looking history, with a single commit
representing all of his changes.  Many teams prefer this, but as we'll see
later there are other ways of getting there.

## Explore a complicated history

Meanwhile Alice adds a picture of *her* cat and pushes her change, and Bob
pulls it. 

```
$ cd ../../Alice/Cats
$ git checkout -b add-cat
$ sed FIXME
$ git commit -a -m "Add picture of Dinah"
$ git checkout master
$ git merge --ff-only add-cat
$ git push
# Bob pulls at this point
$ cd ../../Bob/BobCats
$ git checkout master
$ git pull
```

When Bob pulls this, his history looks like:

```
Bob:    ...o---m---A---D
                    \
                     B---C
```

It might be useful at this point to try some of the tools that let you
visualize the structure of Git's history graph.  The first one to try is 

```
git log --graph
```

It produces a graph similar to the ones used in this unit, only rotated
counter-clockwise so that it goes up the left-hand side of the log output.

The second is 

```
gitk --all &
```

Gitk is a GUI program for exploring Git histories; the `--all` option tells it
to show all of the branches.  The `&` at the end of the line tells Bash to run
the command in another process, so that you can continue working in the shell.

## Simplify history by squashing

Bob has several different things he can do at this point, depending on what he
wants the resulting history to look like.  You've already seen two different
methods, `merge` and `rebase`.  They produce histories that look like:

``` 
merge:  ...o---m---A---D---E
                    \     /
                     B---C

rebase: ...o...m...A...D...B...C
```

Merge has the advantage of preserving all of the individual changes and
recording the merge metadata in a commit.  Rebase has the advantage of keeping
the history simple and easy to understand.

The third possibility is to squash Bob's two commits into a single one, with a
message like "add Bob's cat" that summarizes everything that he did.  Most
developers prefer this -- it lets them make commits with messages like "Fix
off-by-one bug", "make backup", "Revert bad merge", or something even less
helpful (see [this xkcd cartoon](https://xkcd.com/1296/) for example).  Then
they can compose a good message, describing *what they did* rather than the
details of how they did it, and put that into the project's official history.

There are two different ways of doing this, plus a short-cut.  Many developers
take the short-cut and simply make a single commit that they keep amending.
It's not really a good idea, because it's much harder to find a problem in an
amended commit with a bug in it that was introduced sometime in the last week,
than a series of simple ones made every day or so.

The two ways are `git merge --squash` and `git rebase --interactive` (usually
shortened to `git rebase -i`).  Interactive rebase creates a temporary file
containing all of the commits and their one-line descriptions, preceeded by a
command.  Initially the command is `pick`; you can edit that to `drop`,
`squash`, `edit`, or `reword`.  (Edit lets you edit files, reword just lets
you edit the commit message.)  You can also change the order of the commits.

Squashing is simpler:  it simply performs all of the changes that would have
been made by a real merge, but stops just short of making the merge commit or
moving HEAD.  All of the changed files are left in the working tree and index,
ready to commit.  In a simpler world, Bob could just do:

```
# git merge --squash addCat
# git commit -m "Add Bob's cat"
```

It isn't *quite* that simple, because Bob and Alice each changed the same line
in `index.html`, which created a merge conflict.


## Resolving merge conflicts

What *actually* happens when Bob makes his merge is that Git notices that the
branches being merged have changes that overlap, so it interrupts the merge
process so that you can figure out what the final result should be.

```
$ git merge --squash addCat
# TODO conflict output
$ git commit -m "Add  Bob's cat"
# TODO commit attempt output
```

Notice that Bob tried to ignore the conflict and commit anyway; naturally, he
got an error message.

When Git detects a conflict, it inserts *both* conflicting versions into the
file, between lines starting with `<<<<<<<`, `=======`, and `>>>>>>>`.  The
part before the `=======` line is "your" side of the merge -- the branch
you were alreadt on -- and the part after is "their" side -- the branch you
specified in the `merge` command.

```
TODO: partial file listing of index.html
```

In this case, Bob wants to keep Alice's cat and add his own, so he simply
deletes the markers.

```
$ sed -i.bak -e '/<<<</d' -e '/====/d' -e '/>>>>/d' index.html
$ git add index.html
$ git merge --continue
$ git commit -m "Add Bob's cat"
$ git push
```

The `git add` tells Git that the conflict in `index.html` has been resolved,
and the `git merge --continue` finishes the merge.  Another option, if Bob had
decided that he shouldn't have made the merge after all, was `git merge
--abort`; that option only works if there are conflicts.

Bob could also use `git reset --hard` in both of the merged branches to get back
to what he had before a merge.

## Summary

In this unit you've learned how to create branches, and several different ways
of merging them.  You've learned about

* `git branch`, which creates a branch,
* `git checkout`, which switches to a branch, and
* `git checkout -b` which creates a branch *and* switches to it.

You've also learned how to use 

* `git rebase`, which revises commits to re-arrange branches, and
* `git merge`, which combines branches.

You've also learned how to deal with merge conflicts, using the `--continue`
and `--abort` options with `merge`; they also work with `rebase`.  And you 

It's worth noting that you can also use `--abort` and `--continue` with `git
rebase`, and  because `git pull` is a combination of `fetch` and `merge`, you
can resolve conflicts the same way.  You can use `git pull --rebase` to rebase
instead of merging after the fetch; it's particularly useful for keeping a
branch up to date if you want to continue working on it after your colleagues
have pushed changes to `master`.


In the next unit
