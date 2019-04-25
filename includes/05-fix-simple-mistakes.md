# Fix simple mistakes

Sometimes things go wrong.  You might forget to add a new file, or add one by
mistake.  Perhaps there was a spelling error in your latest commit, or you
committed something you didn't intend to.  Perhaps you accidentally _deleted_
a file.  Git lets you make changes fearlessly.

## Amend a commit

When you refresh the page in your browser, you notice that your stylesheet
isn't being applied.  After investigating, you see that `index.html` is still
referring to the stylesheet's old location in `CSS`.

```
$ sed -i.bak s/CSS/assets/ index.html
$ git add index.html
```

At this point you could simply commit the changed version of `index.html`, but
it makes more sense to put it in the same commit as the rename.  The `--amend`
option to `git commit` lets you change history.

```
$ git commit --amend --no-edit
[master e2e5bcd] rename CSS -> assets for generality
 Date: Sun Mar 24 06:24:01 2019 -0700
 2 files changed, 1 insertion(+), 1 deletion(-)
 rename {CSS => assets}/site.css (100%)
```

The ability to change history (we will see later that there are other ways
besides `--amend`) is one of Git's most powerful features.  Like most power
tools, it has to be used carefully -- in particular, it's a bad idea to change
any commits that have been published.

### Exercises:

* Run `git log -n1 --pretty=fuller`.  What do you notice about the AuthorDate
  and CommitDate fields?
* Compare that to the output of `git log -n1`.  Which date is reported by
  default?
* Can you think of cases where the author and committer would be different?

## Retrieve an earlier version of a file

One thing that git makes easy is retrieving an earlier version of a file.  You
may have deleted more than you intended with a wildcard, damaged a file
experimenting with `sed`, or simply have made a series of changes that you
later regret.  Your friend in this situation is `git checkout`.  For example,

```
$ rm index.html .bak
$ ls
assets	index.html.bak
```

This is a classic problem -- you meant to delete the backup file, but your cat
stepped on the keyboard and put in a space before the dot.  If you notice the
problem soon enough, it's particularly easy to fix:

```
$ git checkout -- index.html
$ ls
assets	index.html  index.html.bak
$ git status
On branch master
nothing to commit, working tree clean
```

You can also check out a file from another commit (typically the head of
another branch), but the default is to get the file out of the index.  The
`--` in the argument list is there to separate the commit from the list of
file paths.  It's not strictly needed in this case, but if there had been a
branch called `index.html` (perhaps because that's the name of the file being
worked on on that branch) or a file called `master`, it would be needed to
resolve the ambiguity.

Things are a little more complicated if you used `git rm`:

```
$ git rm index.html
rm 'index.html'
$ git checkout index.html
error: pathspec 'index.html' did not match any file(s) known to git.
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	deleted:    index.html

$ git reset HEAD index.html
Unstaged changes after reset:
D	index.html
$ ls
assets	index.html.bak
$ git checkout index.html
$ ls
assets	index.html  index.html.bak
```

The `git reset` was needed because `git rm` did two things:  it removed the file,
and it recorded the deletion in the index.  The `reset` unstaged the change,
but the file was still deleted, so you had to use `checkout` to get it back.

## Revert a commit

You decide to make the background a little darker:

```
echo body '{ background-color:  #E0E0E0; }' > assets/site.css
$ git commit -a -m "Make the page background a little darker"
[master 4a846bb] Make the page background a little darker
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Oops!  You meant to append to `site.css`, but used `>` instead of `>>`, which
replaced the entire file.  You already know how to fix this by amending
the commit -- use `git checkout` to get the previous version of `site.css`
back, make the change correctly, and `git commit --amend`.  Or you could use
`git reset --hard` to put everything back the way it was, and re-do both the
change and the commit.

But suppose you didn't notice the problem until you'd already made another
commit after the bad one, shared your repo with somebody (see the next unit)
or made the commit public (see Unit 7).  Changing history can be dangerous
(see almost any science fiction story about time travel).  It this situation
the best thing to do is to _revert_ the change, by making another commit that
cancels out the first one:

```
$ git revert --no-edit HEAD 
[master 3681d4a] Revert "make the page background a little darker"
 Date: Sun Mar 24 07:52:27 2019 -0700
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git log -n1
commit 3681d4ac99448818fba7714487206cc5426b1e79 (HEAD -> master)
Author: Steve Savitzky <steve@savitzky.net>
Date:   Sun Mar 24 07:52:27 2019 -0700

    Revert "Make the page background a little darker"
    
    This reverts commit 4a846bb58b8810bac9830780c9da2a33dc63c0c2.
```

Now you can make the change correctly.

```
$ echo body '{ background-color:  #E0E0E0; }' >> assets/site.css 
$ cat !$
cat assets/site.css
h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
body { background-color:  #E0E0E0; }
$ git commit -a -m "Make the page background a little darker" -m "correctly"
[master 9c139ee] make the page background a little darker
 1 file changed, 1 insertion(+)
```

In addition to copying text from the terminal to a file, the `cat` command is
possibly even more useful going the other way, for getting a quick look at a
short file.  For longer files, use `less`.

### Exercises

* Use `git reflog` to see all the changes you've made to `master` and `HEAD`,
  including the original version of the commit you amended.
* Use `gitk --all`, which shows you a GUI view of your history, to verify that
  the last few commits made the changes you expect.

## Summary

In this unit you've learned about

* `git checkout`, which retrieves previous versions,
* `git reset`, which sets the working tree and index back to an earlier state,
* `git revert`, which undoes the effect of a commit without affecting history,
* `git reflog`, which shows you previous values of `HEAD` and `master`,  and 
* `git commit --amend`, which lets you change the most recent commit.

You've also seen 

* `rm`, which removes a file, and
* `gitk`, which gives you a GUI for exploring your history.

In the next unit you'll start collaborating with another developer.  Since Git
is distributed, you won't have to set up a server; you can share directly.
