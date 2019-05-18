# Make and track changes

As you work on the site, `git` helps you keep track of the changes you make.
It also lets you undo any changes you make by mistake.

## Make some changes

Start by adding some HTML boilerplate to `index.html`.  You can do it by
downloading [this file](media/unit-04-index.html), but it should already be in
your sandbox, so you can just copy it.  (If it isn't, you forgot to download
and unzip [sandbox.zip](media/sandbox.zip).)

```
$ cd ~/sandbox/Cats
$ cp ../unit-04-index.html index.html
```

You can see what you changed by using `git diff`:

``` 
$ git diff
diff --git a/index.html b/index.html
index 0aa3ab0..6f16b61 100644
--- a/index.html
+++ b/index.html
@@ -1 +1,12 @@
+<!DOCTYPE html>
+<html>
+<head>
+<meta charset='UTF-8'>
+<title>Our Feline Friends</title>
+</head>
+<body>
 <h1>Our Feline Friends</h1>
+<p> Eventually we will put cat pictures here.
+<hr>
+</body>
+</html>
``` 

The output format is the same as the Unix `diff` command, and it takes many of
the same options.  Here you can see a `+` in front of lines that have been
added; if any lines had been deleted you would see a `-` in front of them.
Notice that the `h1` line hasn't changed.

The default is for `git diff` to compare the working tree to the index; that
means that, it shows you all of the changes that haven't been staged yet.  To
compare the working tree to the last commit, use `git diff HEAD`.

```
$ git commit -m "Add HTML boilerplate to index.html" index.html
[master bc18ca7] Add HTML boilerplate to index.html
 1 file changed, 11 insertions(+)
$ git diff
```

Notice that you can explicitly name a file to be committed, provided Git
already has it in the index.

You decide "furry" would sound friendlier than "feline".  You can do this with
a text editor; here we're using `sed`, the "stream editor", which lets you
specify editing commands on the command line.  (See `man sed` for the details;
Sed's command set -- here we're using `s` to make a substitution -- is
essentially the same as Unix's original text-editor, `ed`.)

```
$ sed -i.bak s/Feline/Furry/ index.html
$ ls
index.html
index.html.bak
```

Now you may notice that you have a problem: if you used `sed` there's a text
editor backup file here that you shouldn't commit.  (There may not be one if
you used a text editor that's clever enough not to make backups of
version-controled files.  What the backups will look like will also depend on
which text editor you're using; Vim or Emacs will create one called
`index.html~` by default; you may have Emacs configured to keep numbered
backups, in which case you would have `index.html.~1~`.)  You can tell Git to
ignore these:

```
$ echo -e "*.bak\n*~" > .gitignore
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   index.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore

no changes added to commit (use "git add" and/or "git commit -a")
$ git add -A
$ git commit -m "make small wording change; ignore editor backups"
[master 569647a] make small wording change; ignore editor backups
 2 files changed, 4 insertions(+), 2 deletions(-)
 create mode 100644 .gitignore
```

This example uses `HEAD^` to name the *previous* commit.  It also uses
the `-A` option with `git add`, which adds the untracked (and not ignored)
files as well as changed ones that are already under Git control.

## Exercise: try the following commands

At this point, you can try a few different options to `git diff` to get a
feel for a few of its capabilities:

```
$ git diff
$ git diff HEAD^
$ git diff master HEAD^
$ git diff HEAD^ HEAD^^
$ git diff --word-diff HEAD^
$ git diff --name-only HEAD^
$ git diff HEAD^ -- index.html
$ git diff -- foo
$ git diff foo
```

Some things to notice:

* A circumflex after a commit name gets you to the previous commit.
* `--` can be used to separate commit references from filenames.  It's not
  needed in this case, but it will prevent problems if you ever make a file
  called `HEAD` or a branch that has the same name as a file.
* there are many ways to name commits; `master` always refers to the latest
  commit on the master branch, no matter which branch you're currently on.

## Create a subdirectory

Most websites have CSS as well as HTML, and it's usually kept in a
subdirectory, so you make a subdirectory for it:

```
$ mkdir CSS
$ git status
On branch master
nothing to commit, working tree clean
```

People used to most other version-control systems may be surprised by the
fact that Git doesn't consider adding an empty directory to be a change.
That's because Git only tracks changes to *files*, not directories.

Sometimes, especially in the initial stages of development, you *want*
to have empty directories.  A common convention is to create an empty file in
them -- it's often called `.git-keep`.

```
$ touch CSS/.git-keep
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	CSS/

nothing added to commit but untracked files present (use "git add" to track)
$  git add CSS
$  git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   CSS/.git-keep
```

This is also a good place to try `git diff --cached`, which compares the _index_
to the most recent commit.

```
$ git diff
$ git diff --cached
diff --git a/CSS/.git-keep b/CSS/.git-keep
new file mode 100644
index 0000000..e69de29
$ git commit -m "Add a (mostly) empty directory for CSS"
[master 9f9f355] Add a (mostly) empty directory for CSS
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 CSS/.git-keep
```

## Remove a file

Now you add a simple two-line stylesheet to your website (the `>>` on the
second `echo` command appends to the target file), and insert a link tag into
`index.html` that points to it.

```
$ echo 'h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }' > CSS/site.css
$ echo 'body { font-family: serif; }'                       >> CSS/site.css
$ sed -i.bak -e '/title/a <link rel="stylesheet" href="CSS/site.css">' index.html
$ git add .
$ git commit -m "Add a simple stylesheet"
[master 9555ac8] Add a simple stylesheet
 2 files changed, 3 insertions(+)
 create mode 100644 CSS/site.css
```

Now that you have a file in `CSS`, you can remove the `.git-keep` file.

```
$ git rm CSS/.git-keep
rm 'CSS/.git-keep'
$ git commit -m "Remove redundant .git-keep file"
[master b38d55f] Remove redundant .git-keep file
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 CSS/.git-keep
```

Notice, by the way, that you didn't need to use `git add` -- `git rm`
automatically updates the index as well as the working tree.

As with the Unix command `rm`, Git requires the `-r` option to recursively
remove a directory and its contents:

```
$ git rm CSS
fatal: not removing 'CSS' recursively without -r
```

(As we'll see in the next unit, if you accidentally added `-r` to your command
and removed the directory and its contents, it would have been easy to get it
back using `git checkout`.)

### Exercise

* Open `index.html` in your browser.  (The easy way is to open `file:///` and
  click your way down.  That works no matter what OS you're using.) Observe
  that the stylesheet has been applied.

## Rename files and directories

After creating CSS/site.css it occured to you that you might want to put other
assets on the site besides the stylesheet, so it would make sense to rename
the directory.  As you might expect, you do that with `git mv` -- `mv`, short
for "move", is the Unix command for renaming a file.

```
$ git mv CSS assets
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	renamed:    CSS/site.css -> assets/site.css

$ git commit -m "Rename CSS -> assets for generality"
[master 7f77894] Rename CSS -> assets for generality
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {CSS => assets}/site.css (100%)
```

Just as with `git rm`, `git mv` automatically updates the index, so it isn't
necessary to run `git add`.

The percentage reported by `commit` on the last line is the degree of
similarity between the file in its old and new locations.  In this case, of
course, you _just_ moved it, so they're 100% identical.  If you change a file
and don't commit before you move it, the percentage will be lower, but Git
correctly recognizes a change-and-move in most cases.  It can guess wrong if
you move more than half of one file into another -- in that case it will look
as though the file was moved and then a new file was created in its place.

Unlike most version control systems, Git records the contents of your files
rather than the changes you made between them.  That's a large part of what
makes committing, branching, and switching between branches so fast in Git:
other VCSs have to apply a list of changes to get between one version of a
file and another.  Git just unzips the other version.

By the way, if you reload the page in your browser you will notice that the
stylesheet has *not* been applied, because you moved it without changing the
reference in `index.html`.  We'll fix that in the next unit.

## List commits with Git log

Now that you have a reasonable number of changes recorded, you can use `git
log` to look at them.  As with most Git commands, there are plenty of options
to choose from; one of the most useful is `--oneline`.

```
$ git log --oneline
7f77894 Rename CSS -> assets for generality
b38d55f Remove redundant .git-keep file
9555ac8 Add a simple stylesheet
9f9f355 Add a (mostly) empty directory for CSS
569647a make small wording change; ignore editor backups
bc18ca7 Add HTML boilerplate to index.html
4c3b05d add a heading to index.html
93dda01 Create an empty index.html file
```

### Exercise

Try the following log commands:

```
$ git log
$ git log -n2
$ git log -n2 --no-abbrev-commit
```

## Summary

In this unit you learned about the following Git commands:

* [`git diff`](https://git-scm.com/docs/git-diff),
 which shows the differences between versions,
* [`git mv`](https://git-scm.com/docs/git-mv),
 which moves (renames) a file, and
* [`git rm`](https://git-scm.com/docs/git-rm),
 which removes (deletes) a file,

as well as a little more about `git log`.

You also used the Unix commands

* [`cat`](https://linux.die.net/man/1/cat), which concatenates files (including input from the terminal), and
* [`sed`](https://linux.die.net/man/1/sed), which applies text-editing commands non-interactively.

In the next unit you'll learn how to use Git to recover from several common
mistakes, including some of the mistakes that people often make using Git.
