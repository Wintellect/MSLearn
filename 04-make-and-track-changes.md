# Make and track changes

As you work on the site, `git` helps you keep track of the changes you make.
It also lets you undo any changes you make by mistake.

## Make some changes

Start by adding some HTML boilerplate to index.html.  You can do it with a
text editor; here we're using the `cat` (concatenate) command.  The `^D` at
the end is CTRL-D (EOT, the code for "End Of Transmission" back in the days of
teletypes and paper tape).  The leading circumflex is often used in Unix
documentation as shorthand for "control-", and should not be typed literally.

```
$ cat > index.html
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<title>Sample page</title>
</head>
<body>
<h1>Hello, world!</h1>
<p> If this were a real website there would be content here.
<hr>
</body>
</html>
^D
```

You can see what you changed by using `git diff`:

``` 
$ git diff
diff --git a/index.html b/index.html
index 9f735a6..3970c55 100644
--- a/index.html
+++ b/index.html
@@ -1 +1,12 @@
+<!DOCTYPE html>
+<html>
+<head>
+<meta charset='UTF-8'>
+<title>Sample page</title>
+</head>
+<body>
 <h1>Hello, world!</h1>
+<p> If this were a real website there would be content here.
+<hr>
+</body>
+</html>

```

The default is for `git diff` to compare the working tree with the index.  The
format is the same as the Unix `diff` command.

```
$ git commit -m "add HTML boilerplate to index.html" index.html
[master 4b360ff] add HTML boilerplate to index.html
 1 file changed, 11 insertions(+)
$ git diff
```

Notice that you can explicitly name a file to be committed.
You decide "everybody" would sound friendlier than "world".

```
	$ sed -i.bak s/world/everybody/ index.htm
$ ls
index.html  index.html.bak

```

Now you notice that you have a problem: there's a text editor backup file here
that you shouldn't commit.  (There may be more than one, depending on which
text editor you're using; Vim or Emacs will create one called `index.html~` by
default; you may have Emacs  configured to keep numbered backups, in which case
you would have `index.html.~1~`.)  You can tell Git to ignore these:

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

```

This example uses `HEAD^` to name the <em>previous</em> commit. 
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
* there are many ways to name commits; `master` and `HEAD` both refer to the
  latest commit on the master branch.

## Create a subdirectory

Most websites have CSS as well as HTML, and it's usually kept in a
subdirectory.

```
$ mkdir CSS
$ git status
On branch master
nothing to commit, working tree clean
```

People used to most other version-control systems may be surprised by the
fact that Git doesn't consider adding an empty directory to be a change.
That's because Git only tracks changes to <em>files</em>, not directories.

Sometimes, especially in the initial stages of development, you <em>want</em>
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
$ git commit -m "add a (mostly) empty directory for CSS"
[master c5a3013] add a (mostly) empty directory for CSS
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 CSS/.git-keep 
```

## Remove a file

You add a simple stylesheet to your website

```
$ echo 'h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }' > CSS/site.css
$ sed -i.bak -e '/title/a <link rel="stylesheet" href="CSS/site.css">' index.html
$ git add .
$ git commit -m "add a simple stylesheet"
```

Now that you have a file in `CSS`, you can remove the `.git-keep` file.

```
$ git rm CSS/.git-keep
rm CSS/.git-keep'
$ git commit -m "remove redundant .git-keep file"
[master 9ebf814] remove redundant .git-keep file
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 CSS/.git-keep
```

Notice, by the way, that we didn't need to use `git add` -- `git rm`
automatically updates the index as well as the working tree.

As with the Unix command `rm`, Git requires the `-r` option to recursively
remove a directory and its contents:

```
$ git rm CSS
fatal: not removing 'CSS' recursively without -r
```

### Exercise

* Open `index.html` in your browser.  Verify that the stylesheet has been
  applied. 


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

$ git commit -m "rename CSS -> assets for generality"
[master d0cd883] rename CSS -> assets for generality
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
Git is simply reporting the most efficient way of making the change; it
doesn't have any way to know your intention.


## Git log

Now that you have a reasonable number of changes recorded, you can use `git
log` to look at them.  As with most Git commands, there are plenty of options
to choose from; one of the most useful is `--oneline`.

```
$ git log --oneline
d0cd883 (HEAD -> master) rename CSS -> assets for generality
9ebf814 remove redundant .git-keep file
0fb33d0 add a simple stylesheet
c5a3013 add a (mostly) empty directory for CSS
c5c35ac make small wording change; ignore editor backups
4b360ff add HTML boilerplate to index.html
5d4f63b add a heading to index.html
2f52bb5 create an empty index.html file
```

### Exercise

Try the following log commands:

```
$ git log
$ git log -n2
$ git log -n2 --no-abbrev-commit

```

## Commands introduced in this unit

```
git diff
git mv
git rm
```
