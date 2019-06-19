# Make and track changes

Most development projects are iterative. You write some code, then test it and make sure it works. Then you write more code, and invite other people to contribute their own. Thereafter ensues a lot of changes: code additions, bug fixes, deletions, and replacements.

As you work on your project, Git helps keep track of the changes you make. It also lets you undo mistakes. In the exercises that follow, you will continue building out the Web site you're working on make changes to the project as you do. You will learn tk.

## Modify index.html

The Web site's home page, **index.html** currently contains just one line of HTML. Let's update it to present a prettier face to the public and commit the change to Git.

1. Open **index.html** in your favorite text editor and replace its contents with the following HTML:

	```html
	<!DOCTYPE html>
	<html>
	  <head>
	    <meta charset='UTF-8'>
	    <title>Our Feline Friends</title>
	  </head>
	  <body>
	    <h1>Our Feline Friends</h1>
	    <p> Eventually we will put cat pictures here.
	    <hr>
	  </body>
	</html>
	```

	Then save your changes to the file.

1. Use a [git diff](https://git-scm.com/docs/git-diff) command to see what changed:

	``` bash
	git diff
	``` 

	The output format is the same as that of the Unix `diff` command, and it takes many of the same options. A plus sign appears in front of lines that were added, and a minus sign indicates lines that were deleted. Notice that the `h1` line hasn't changed.

	The default is for `git diff` to compare the working tree to the index. In other words, it shows you all of the changes that haven't been staged (added to the index) yet. To compare the working tree to the last commit, you can use `git diff HEAD`.

1. Next, commit the change. Notice that you can explicitly name a file to be committed, provided Git already has the file in the index (which is all that `commit` looks at).

	```bash
	git commit -m "Add HTML boilerplate to index.html" index.html
	```

1. Use `git diff` again to compare the working tree to the index. This time, `git diff` produces no output because the working tree, index, and HEAD are all in agreement.

1. Let's say you decide "furry" would sound friendlier than "feline." Replace the two occurrences of "Furry" in **index.html** wuth "Feline." Then save the file.

1. Depending on which text editor you use, there could now be a problem. For example, if you use [sed](https://en.wikipedia.org/wiki/Sed) as your editor, it creates an **index.html.bak** file that you don't want to commit. Other editors such as Vim and Emacs create backup files named **index.html~** or **index.html.~1~**, depending on how they're configured. 

	Use the following command to create a file named **.gitgnore** that instructs Git to ignore files whose names end in **.bak** or **~**:

	```bash
	$ echo -e "*.bak\n*~" > .gitignore
	```

	**.gitignore** is a very important file in the Git world because it prevents extraneous files from being submitted to version control. Boilerplate **.gitignore** files are available for commonly used programming tools such as Microsoft's [Visual Studio](https://visualstudio.microsoft.com/).

1. Now use these commands to commit the changes:

	```bash
	git add -A
	git commit -m "Make small wording change; ignore editor backups"
	```

This example uses the `-A` option with `git add` to add all untracked (and not ignored) files as well as ones that have changed to those already under Git control.

## Exercise: try the following commands

At this point, you can try a few different options to `git diff` to get a feel for a few of its capabilities:

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

- A circumflex after a commit name gets you to the previous commit.
- Use `--` to separate commit references from filenames. It's not needed in this case, but the '--' prevents problems if you ever make a file called `HEAD` or a branch that has the same name as a file.
- There are many ways to name commits; `master` always refers to the latest commit on the master branch, no matter which branch you're currently on.

## Create a subdirectory

Most websites use CSS as well as HTML. It's usually kept in a subdirectory, so you make a subdirectory for it:

```
$ mkdir CSS
$ git status
On branch master
nothing to commit, working tree clean
```

People used to most other version-control systems may be surprised to learn that Git doesn't consider adding an empty directory to be a change. That's because Git only tracks changes to *files*, not directories.

Sometimes, especially in the initial stages of development, you *want* to have empty directories as placeholders. A common convention is to create an empty file in them -- it's often called `.git-keep`.

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

This is also a good place to try `git diff --cached`, which compares the _index_ to the most recent commit.

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

Now, to create the simple CSS file that accompanies the cat project website, add a simple two-line stylesheet to your website (the `>>` on the second `echo` command appends to the target file), and insert a link tag into `index.html` that points to it.

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

Notice, by the way, that you didn't need to use `git add` -- `git rm` automatically updates the index as well as the working tree.

As with the Unix command `rm`, Git requires the `-r` option to recursively remove a directory and its contents:

```
$ git rm CSS
fatal: not removing 'CSS' recursively without -r
```

(As we'll see in the next unit, if you accidentally added `-r` to your command and removed the directory and its contents, it would have been easy to get it back using `git checkout`.)

### Exercise

* Open `index.html` in your browser. (The easy way is to open `file:///` and click your way down. That works no matter which OS you use.) Observe that the stylesheet is applied.

## Rename files and directories

The cat website may be sparse, so far, but it's functional. However, after you create CSS/site.css you may decide to put other
assets on the site besides the stylesheet. It makes sense to rename the directory.

As you might expect, you do that with `git mv`. Again, the command reflects common Unix commands; `mv`, short for "move," is the Unix command for renaming a file.

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

Just as with `git rm`, `git mv` automatically updates the index, so it isn't necessary to run `git add`.

The percentage reported by `commit` on the last line is the degree of similarity between the file in its old and new locations. In this case, of course, you _just_ moved it, so they're 100% identical. If you change a file and don't commit before you move it, the percentage is lower, but in most situations Git correctly recognizes a change-and-move. It can guess wrong if you move more than half of one file into another; in that case, it will look as though the file was moved and then a new file was created in its place.

Unlike most version control systems, Git records the contents of your files rather than the changes you made between them. That's a large part of what makes committing, branching, and switching between branches so fast in Git. Other VCSs have to apply a list of changes to get between one version of a file and another. Git just unzips the other version.

By the way, if you reload the page in your browser you will notice that the stylesheet has *not* been applied, because you moved it without changing the reference in `index.html`. We fix that in the next unit.

## List commits with Git log

Now that you have a reasonable number of changes recorded, you can use `git log` to look at them. As with most Git commands, there are plenty of options to choose from; one of the most useful is `--oneline`.

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

* [`git diff`](https://git-scm.com/docs/git-diff), which shows the differences between versions
* [`git mv`](https://git-scm.com/docs/git-mv),  which moves (renames) a file
* [`git rm`](https://git-scm.com/docs/git-rm),  which removes (deletes) a file
* ...and a little more about `git log`.



In the next unit you learn how to use Git to recover from several common mistakes.
