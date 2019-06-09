# Start a project

Now it's time to get your website project off the ground!

The first step is to make a directory to hold your project, with a file in it (because git ignores empty
directories). "Cats" is a little unimaginative, but it's easy to type. (Feel
free to use something else -- nothing inside the working tree depends on the
directory it's in.) Since this will be a website, the first file you need to create is `index.html`.

There are actually two ways to get a git working tree on your computer; the
other one is to clone an existing git repository. In unit 6, we see how that works. At the moment, we take the simplest approach.

## Make yourself a sandbox

Eventually, you will make several different Git repositories. Some later examples require files, including a few images, that would
be tedious to create or download individually. You also need a "sandbox" in
which to play. Start by downloading [sandbox.zip](media/sandbox.zip). It's
easiest to use your browser for that download; it probably will be stored in your
`Downloads` directory by default. Unzip it.

```
cd ~
mkdir sandbox
cd sandbox
unzip Downloads/sandbox.zip
```

The `cd ~` makes sure you are in your home directory, which Bash abbreviates
as `~` (tilde).

## Create a repository and working tree

First, make the directory, `cd` into it, and initialize the repository.

```
$ mkdir Cats
$ cd Cats
$ git init
Initialized empty Git repository in /home/.../sandbox/Cats/.git/
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
$ ls -aF
./  ../  .git/
```

## Create and add (stage) a file

Create a file in the repository with `touch`, which updates the
"last-modified" time of a file, and creates itm if it doesn't exist.

```
$ touch index.html
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	index.html

nothing added to commit but untracked files present (use "git add" to track)
```

Notice that `git status` gives you hints about what you can do next. A config file option can make it less wordy if you prefer.

Now add your new file to Git's "index."

```
$ git add .
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   index.html
```

This isn't the only way to accomplish the task. Alternatively, you could have added just `index.html` with `git add
index.html`; adding the period (`.`) adds all changed or new files in the entire working
tree. The `touch` command updates the time at which the file was last modified, and
creates an empty file if it didn't exist before now.

Git's "index" is also called the _staging area_, so _staged_ is a shorter way of
saying "in the index." The index is a list of all the file
versions that are going to be part of the *next* commit you make.

For an examaple of a staging area, consider the way you go about cooking
dinner. To get organized, you pull out all the ingredients you need and at
least set them on the counter before you get underway making the meal. Once
you start cooking, you don't have to look in the fridge for an ingredient.
Similarly, Git doesn't have to look in the working tree (which might be
enormous) for a version.

There's no real need to start with an empty file. In fact, you can start with an entire project that you created before you learned how to use version control.

## Make your first commit

Now that `index.html` has been added to the index, you can commit it. Doing so requires that you understand what "commit" really means.

_Commit_ is both a verb and a noun. It has essentially the same meaning as when you commit to a plan, or commit a change to a database.

As a verb, committing changes means you put a copy (of the file, directory, or other "stuff") in the repository as a new version. As a noun, a commit is the small chunk of data that gives a unique identity to the changes you committed. It includes the author's name; the author's email address; the date; comments about what you did (and why); an optional digital signature; and the unique identifier of the previous commit.

```
$ git commit index.html -m "Create an empty index.html file"
[master (root-commit) 93dda01] Create an empty index.html file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 index.html
$ git status
On branch master
nothing to commit, working tree clean
$ git log
commit 93dda01e79f9f791c0fcba727ff18d1c7ccf76c8
Author: Steve Savitzky <steve@savitzky.net>
Date:   Tue May 14 14:23:39 2019 -0700

    Create an empty index.html file
$ git log --oneline
93dda01 Create an empty index.html file
```

When you try this on your own computer, expect different commit IDs. A commit includes the date and time it was made, and the name and email address of the person who made it.

If you don't provide a message on the command line, `git commit` invokes the default text editor so that you can create such a message.

A commit message can have multiple lines. The first line should have no more than 50 characters, and should be followed by a blank line. Subsequent lines should have no more than 72 characters. These aren't hard requirements, but they do make Git's
messaging look better.

For example, the format of `git log --oneline` adds 25 characters to the message, so a 50-character message still fits conveniently in an 80-column default terminal window.

Strictly speaking, everything up to the first blank line is a *paragraph*, and it can be any length. However, if the commit message is longer than 50 characters it may be truncated in some cases, and wrap in the middle of words in others. Lines of 72 characters and blank lines separating paragraphs were standard for text-based email. (Historically, the arbitrary-looking limits of 72 and 80 characters go back to the days when punched cards had 80 columns; the last eight columns were used to number the cards as a safety measure in case the deck was dropped.)

There are many different ways to phrase commit messages, but a good guideline is to
write the first line in the present imperative tense so that it says *what the
commit does to the tree*. It's also common to capitalize the first letter,
and to leave off the closing period to save space. Imagine that the first
line of the message completes the sentence starting with "When pushed, this
commit will...."  Some good articles to read about formatting commit messages
are "[The Art of the
Commit](https://alistapart.com/article/the-art-of-the-commit)" by David
Demaree and "[How to Write a Git Commit
Message](https://chris.beams.io/posts/git-commit/)" by Chris Beams.

## Add content

We need to put some kind of content onto our cat-centric website, and it makes sense to start with its home page. Here, you use the `echo` command to add a heading line to `index.html`.  Echo is a Unix command that echoes whatever you type on its command line.  The `>` on the command line redirects the command's output to a file.

```
$ echo '<h1>Our Feline Friends</h1>' > index.html

$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
$ git commit -a -m "add a heading to index.html"
[master 4c3b05d] add a heading to index.html
 1 file changed, 1 insertion(+)
```

The `-a` option to `git commit` adds all of the files you modified since the
last commit.  It won't add _new_ files -- for that you still need `git add`.

## Explore the Git repository

This is a good time to take a look inside the Git repository, while things are
still uncomplicated. We use `ls -RFC` to make a recursive directory
listing with flag characters (e.g., `/` flags directories, and `*` flags
executable files).

```
$ ls -FC .git
COMMIT_EDITMSG	HEAD  branches	config	description hooks  index  info  logs
objects	        refs
```

You can use `cat` to view the contents of `COMMIT_EDITMSG`, which contains the
most recent commit message, HEAD, which contains the filename of the branch
(`master`) that is currently checked out, and `config`, which contains the
local configuration for this working tree.

Using `ls -RF` you can drill down into `refs` and `objects`. (The following
listing has been edited; missing parts are indicated by Bash comments, which
start with `#`.)

```
$ ls -RFC .git/refs .git/objects
.git/objects:
0a/  41/  4c/  93/  e6/  info/	pack/
# 
.git/objects/0a:
5568b3eb72786b7d025f317905c26d9b2a59ce	a3ab0a00c949dd8acef42d64c720ad0677b345
# (other subdirectories of objects omitted)

# objects/info and objects/pack are currently empty

.git/refs:
heads/	tags/
.git/refs/heads:
master
.git/refs/tags:
$ cat .git/HEAD
ref: refs/heads/master
$ cat .git/refs/heads/master 
4c3b05d4c547a39118ff3381f003d259f016aabf
```

Every branch (`master` is the only one at the moment) has a corresponding file
in `refs/heads` that contains the hash of its head commit.

It's worth taking a moment to note the way Git stores objects: `objects` has a subdirectory
corresponding to the first byte (two hex digits) of the object's hash. The remaining 19 bytes are the name of the file in that directory that contains the object itself.

Objects are binary files (they're compressed with `gzip`), but you can examine their contents with `git show`. Try:

```
$ git show `cat .git/refs/heads/master`
commit 4c3b05d4c547a39118ff3381f003d259f016aabf
Author: Steve Savitzky <steve@savitzky.net>
Date:   Tue May 14 14:26:46 2019 -0700

    add a heading to index.html

diff --git a/index.html b/index.html
index e69de29..0aa3ab0 100644
--- a/index.html
+++ b/index.html
@@ -0,0 +1 @@
+<h1>Our Feline Friends</h1>
```

(Bash replaces a command enclosed in back-quotes with its output.) The diff
shown is computed from the changed files; you can see the actual contents of
the commit object using `git cat-file`:

```
$ git cat-file commit 4c3b05d4c547a39118ff3381f003d259f016aabf
tree 419d0dd7f1068e70e6b9e60b00f0235e0f5aa795
parent 93dda01e79f9f791c0fcba727ff18d1c7ccf76c8
author Steve Savitzky <steve@savitzky.net> 1557869206 -0700
committer Steve Savitzky <steve@savitzky.net> 1557869206 -0700

add a heading to index.html
```

You can use the `-t` option to get the object's type. The `cat-file` command
is one of the low-level commands that Git documentation refers to as
_plumbing_. The higher-level commands, such as `show`, are called _porcelain_.
Plumbing commands are designed to be used in scripts, and in fact many of the
less-commonly-used Git subcommands *are* scripts, as you can see from:

```
for f in /usr/bin/git-*; do file $f; done
```

One of the reasons why Git has so many sub-commands is that they're so easy to
create: Any executable file with a name starting with `git-` can be used as a
subcommand. 

## Summary

In this unit you learned how to create a project that is under Git's control
from the start. You learned about the following Git subcommands:

* [`git init`](https://git-scm.com/docs/git-init), which creates and
  initializes a Git repository in the current directory
* [`git add `](https://git-scm.com/docs/git-add), which adds files or
 directories to the index
* [`git commit`](https://git-scm.com/docs/git-commit),
 which records all of the files in the index in a commit
* [`git status`](https://git-scm.com/docs/git-status), which tells you the current state of the index and the working tree
* [`git log`](https://git-scm.com/docs/git-log), which lists commits, newest first 
* [`git show`](https://git-scm.com/docs/git-show), which prints the contents  of an object in human-readable form, and
* [`git cat-file`](https://git-scm.com/docs/git-cat-file), which outputs the contents of an object.

You also used the following Unix commands:

* [`mkdir`](https://linux.die.net/man/1/mkdir), which makes a directory
* [`touch`](https://linux.die.net/man/1/touch), which updates the "last-modified" time of a file (and creates it if it doesn't exist)
* [`echo`](https://linux.die.net/man/1/echo), which copies its command-line arguments to its output
* [`ls`](https://linux.die.net/man/1/ls), which lists the files in a directory
* [`cat`](https://linux.die.net/man/1/cat), which concatenates files and outputs the result, and
* [`for`](https://linux.die.net/man/1/for), which is one of several control-structure commands in Bash.

In the next unit, you start making and tracking changes. (We do get to cat photos, too.)

