# Simplify histories and resolve merge conflicts

After Alice adds a picture of her cat and Bob pulls her change, Bob's history
becomes somewhat complicated.  What Alice does is:

```
$ cd ~/sandbox/Alice/Cats
$ git checkout -b add-cat
Switched to a new branch 'add-cat'
$ sed -i.bak -e '/Eventually/ c <img src="assets/bombay-cat-180x240.jpg">' index.html
$ sed -i.bak -e 's/<img /<img class=".cat" /' index.html
$ cp ../../bombay-cat-180x240.jpg assets
$ git add assets/
$ git commit -a -m "Add picture of Dinah"
[add-cat b83d930] Add picture of Dinah
 2 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 assets/bombay-cat-180x240.jpg
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
$ git merge --ff-only add-cat
Updating cddf95c..b83d930
Fast-forward
 assets/bombay-cat-180x240.jpg | Bin 0 -> 39760 bytes
 index.html                    |   2 +-
 2 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 assets/bombay-cat-180x240.jpg
$ git push
```

Now Bob pulls:

```
$ cd  ~/sandbox/Bob/BobCats
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
$ git pull
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (5/5), done.
From /home/steve/sandbox/Cats
 + b59ba72...b83d930 master     -> origin/master
Updating cddf95c..72c34d8
Fast-forward
 assets/bombay-cat-180x240.jpg | Bin 0 -> 39760 bytes
 index.html                    |   2 +-
 2 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 assets/bombay-cat-180x240.jpg
```

After this, Bob's history looks like:

```
Bob:    ...o---m---A---D
                    \
                     B---C
```

When he eventually merges this, there will be a conflict because he and Alice
have overlapping changes in `index.html`.  We will get to that later.

## Explore a complicated history

This is a good time to try some of the tools that let you visualize the
structure of Git's history graph.  The first one to try is

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

Gitk gives you a window with a view similar to `git log --graph` in the top
pane, and the details of each commit in the bottom pane.  Between them are
search and navigation tools, as well as a box containing the full ID of the
selected commit.  This is automatically selected, which makes it easy to copy
and paste into a command.

Bob has several different things he can do at this point, depending on what he
wants the resulting history to look like.  You've already seen two different
methods, `merge` and `rebase`.  They produce histories that look like:

``` 
# git checkout master; git merge --addCat
merge:  ...o---m---A---D---E
                    \     /
                     B---C

# git checkout addCat; git rebase master
rebase: ...o...m...A...D...B...C
```

Merge has the advantage of preserving all of the individual changes and
recording the merge metadata in a commit.  Rebase has the advantage of keeping
the history simple and easy to understand.  In both of these cases, if there's
a conflict Git will interrupt the process to let you try to resolve it.  There
are two ways to 


## Simplify history by squashing

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
than a series of simple ones made every day or so.  (Take a look at the man
page for `git bisect` to see to do that quickly.)

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

(We're using `#` instead of `$` to indicate that you shouldn't actually type
those commands -- Bash ignores everything from `#` to the end of the line.)
It isn't *quite* that simple, because Bob and Alice each changed the same line
in `index.html`, which created a merge conflict.

## Resolve merge conflicts

What *actually* happens when Bob makes his merge is that Git notices that the
branches being merged have changes that overlap, so it interrupts the merge
process so that you can figure out what the final result should be.

```
$ git merge --squash addCat
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Squash commit -- not updating HEAD
Automatic merge failed; fix conflicts and then commit the result.
$ git commit -m "Add  Bob's cat"
U	index.html
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
```

Notice that Bob tried to ignore the conflict and commit anyway; naturally, he
got an error message.

When Git detects a conflict, it inserts *both* conflicting versions into the
file, between lines starting with `<<<<<<<`, `=======`, and `>>>>>>>`.  The
part before the `=======` line is "your" side of the merge -- the branch
you were alreadt on -- and the part after is "their" side -- the branch you
specified in the `merge` command.  In this case it looks like this:

```
<h1>Our Furry Friends</h1>
<<<<<<< HEAD
<img class=".cat" src="assets/bombay-317x240.jpg">
=======
<img class=".cat" src="assets/bobcat2-317x240.jpg">
>>>>>>> addCat
<footer><hr></footer>
```

In this case, Bob wants to keep Alice's cat and add his own, so he simply
deletes the markers.

```
$ sed -i.bak -e '/<<<</d' -e '/====/d' -e '/>>>>/d' index.html
$ git add index.html
$ git commit -m "Add Bob's cat"
[master 39473bb] Add Bob's cat
 2 files changed, 1 insertion(+)
 create mode 100644 assets/bobcat2-317x240.jpg
$ git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 37.49 KiB | 7.50 MiB/s, done.
Total 5 (delta 1), reused 0 (delta 0)
To /home/steve/sandbox/Cats.git
   2868bbf..39473bb  master -> master
```

The `git add` tells Git that the conflict in `index.html` has been resolved,
and the `git merge --continue` finishes the merge.  Another option, if Bob had
decided that he shouldn't have made the merge after all, was `git merge
--abort`; that option only works if there are conflicts.

## Exploring merge alternatives

Bob could also use `git reset --hard` in both of the merged branches to get back
to what he had before a merge.  In this case, the `adCat` branch hasn't
actually been merged, so Bob only has to reset `master`.  It's worthwhile
playing around a little to see Bob's alternatives.

First, let's look at what happens if Bob does the squash but takes the default
merge message instead of replacing it.

```
$ git reset --hard HEAD^
$ git merge --squash addCat
$ sed -i.bak -e '/<<<</d' -e '/====/d' -e '/>>>>/d' index.html
$ git add index.html
$ git commit --no-edit
$ git log -n1
commit ffc8fde164f4cded11ed1f965a2602d894d059c7 (HEAD -> master)
Author: Bob <bob@example.com>
Date:   Fri May 17 14:28:33 2019 -0700

    Squashed commit of the following:
    
    commit f98a6e349309086088228feb8b284e12b72ee4de
    Author: Bob <bob@example.com>
    Date:   Wed May 15 22:06:11 2019 -0700
    
        Add style class to cat picture
    
    commit a6ed876ebc924d16f7589c221526d07220d64f33
    Author: Bob <bob@example.com>
    Date:   Wed May 15 21:50:35 2019 -0700
    
        Add picture of Bob's cat
    
    # Conflicts:
    #       index.html
```

As you can see, it's usually a good idea to edit the message down to something
that makes sense, but if Bob hadn't used the `--no-edit` option, Git would
have initialized the commit message with something that might be a good start.

## Backing out of a conflicted merge

Sometimes the best thing to do when there is a conflict is to back out of it.
This is particularly useful if you do a simple pull instead of `pull
--rebase`.  In that case you can use `git merge --abort` or `git rebase --abort`
to back out.  Unlike the case with squash, once you fix the conflict you can
go forward with `git merge --continue` or `git rebase --continue`.

### Exercise:

Try some of the following:

```
$ git reset --hard HEAD^
$ git merge addCat
$ git merge abort
```

and 

```
$ git merge addCat
$ sed -i.bak -e '/<<<</d' -e '/====/d' -e '/>>>>/d' index.html
$ git add index.html
$ git merge --continue
```

That will put you into the text editor looking at the default merge message,
which is just `Merge branch 'addCat'`.  If you delete the message, Git will
abort the commit just as it will with any commit.  That's a good way of
backing out of a pull that should have been a rebase.

Since Bob has already pushed the squashed merge, he can get it back with

```
$ git reset --hard origin/master
HEAD is now at 39473bb Add Bob's cat
```

It's often a good idea to keep a remote called "backup" that you can push
changes to every evening, or whenever you want to try something tricky.  If
you've done some rebasing, you can use `git push --force backup`.

## Merge tools

Some people prefer to have the versions being merged shown side-by-side so
that they can see what their choices are and select them interactively.  Some
version control systems already have a tool of this sort (e.g. `p4merge` from
Perforce), as do several text editors (e.g. `emerge` from Emacs and `vimdiff`
from Vim).  Git doesn't have a tool of its own; you can specify your favorite
on the `git mergetool` command line or with the `merge.tool` configuration
variable.  The `--tool-help` option shows the list of known tools:

```
$ git mergetool --tool-help
'git mergetool --tool=<tool>' may be set to one of the following:
		araxis
		emerge
		vimdiff
		vimdiff2
		vimdiff3

The following tools are valid, but not currently available:
		bc
		bc3
		codecompare
		deltawalker
		diffmerge
		diffuse
		ecmerge
		examdiff
		gvimdiff
		gvimdiff2
		gvimdiff3
		kdiff3
		meld
		opendiff
		p4merge
		tkdiff
		tortoisemerge
		winmerge
		xxdiff

Some of the tools listed above only work in a windowed
environment. If run in a terminal-only session, they will fail.
```

Naturally, if you run this command on your own computer you are likely to get
a different list.

## Summary

In this unit you learned how to deal with merge conflicts, using the
`--continue` and `--abort` options with `git merge`, and either a text editor
or a merge tool.  You can also use those options with `git rebase`, and
because `git pull` is a combination of `fetch` and `merge`, you can resolve
conflicts the same way.  You can use `git pull --rebase` to rebase instead of
merging after the fetch; it's particularly useful for keeping a branch up to
date if you want to continue working on it after your colleagues have pushed
changes to `master`.

In the next unit, you will learn how to use git to deploy a website using a
hook script, and how to use branches and tags to manage software releases.
