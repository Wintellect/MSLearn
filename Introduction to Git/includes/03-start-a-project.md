# Start a project

Now it's time to get your website project off the ground.  You'll need to make
a directory to hold your project, with a file in it (because git ignores empty
directories).  "Cats" is a little unimaginativ, but it's easy to type.  (Feel
free to use something else -- nothing inside the working tree depends on the
directory it's in.) Since this will be a website, the first file will be
`index.html`.

There are actually two ways to get a git working tree on your computer; the
other one is to clone an existing git repository.  We'll see how that works
starting in Unit 6.

## Create a repository and working tree

First, make the directory, `cd` into it, and initialize the repository.

```
$ mkdir Cats
$ cd Cats
$ git init
Initialized empty Git repository in /home/you/Cats/.git/
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
$ ls -a
.  ..  .git
```

## Create and add (stage) a file

Create a file in the repository with `touch`, which updates the
"last-modified" time of a file, and creates itm if it doesn't exist.

FIXME:  do we need to use `.htm` on Windows?

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

Notice how `git status` gives you hints about what you can do next.  There's a
config file option to make it less wordy if you prefer.

Now add your new file to Git's "index".

```
$ git add .
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   index.html

```

Alternatively, you could have added just `index.html` with `git add
index.html`; adding `.` adds all changed or new files in the entire working
tree.  The `touch` command updates the time the file was last modified, and
it creates an empty file if it wasn't there before.

Git's "index" is also called the "staging area" -- it's a list of all the
file versions that are going to be part of the *next* commit you make.

There's no real need to start with an empty file; in fact you can start with
an entire project that you started before you learned how to use version
control.

## Make your first commit

Now that `index.html` has been added to the index, you can commit it.

```
$ git commit index.html -m "Create an empty index.html file"
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 index.html
$ git status
On branch master
nothing to commit, working tree clean
$ git log
[master (root-commit) 2f52bb5] create an empty index.html file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 index.html
$ git log --oneline
2f52bb5 (HEAD -> master) create an empty index.html file
```

When you try this on your own computer the commit IDs will be different,
because a commit includes the date and time it was made, and the name and
email address of the person who made it.

If you don't provide a message on the command line, `git commit` will invoke
your default text editor so that you can create it.  A commit message can have
multiple lines; the first line should have no more than 50 characters, and
there should be a blank line after it.  Subsequent lines should have no more
than 72 characters.  These aren't hard requirements, they just make Git's
messaging look better.  For example, the format of `git log --oneline` adds 25
characters to the message, so a 50-character message will still fit
conveniently in an 80-column default terminal window.

Strictly speaking, everything up to the first blank line is a *paragraph*, and
it can be any length, but if it's longer than 50 characters it will be
truncated in some cases, and wrap in the middle of words in others.  Lines of
72 characters and blank lines separating paragraphs were standard for
text-based email.  Historically, the arbitrary-looking limits of 72 and 80
characters go back to the days when punched cards had 80 columns, and the last
eight were used to number the cards as a safety measure in case the deck got
dropped.

There are many different ways to phrase commit messages, but a good one is to
write the first line in the present imperative tense so that it says what the
commit *does* to your tree.  It's also common to capitalize the first letter,
and to leave off the closing period to save space.  Imagine that the first
line of the message completes the sentence starting with "When pushed, this
commit will...".  Some good articles to read about formatting commit messages
are "[The Art of the
Commit](https://alistapart.com/article/the-art-of-the-commit)" by David
Demaree and "[How to Write a Git Commit
Message](https://chris.beams.io/posts/git-commit/)" by Chris Beams.

## Add content

Here, you use the `echo` command to add a heading line to `index.html`.  Echo
is a Unix command that echoes whatever you put on its command line.  The `>`
on the command line redirects the command's output to a file.

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
[master 0a3d184] add a heading to index.html
 1 file changed, 1 insertion(+)
```

The `-a` option to `git commit` adds all of the files you modified since the
last commit.  It won't add _new_ files -- for that you still need `git add`.

## Summary

In this unit you learned how to create a project that is under Git's control
from the start.  You learned about the following Git subcommands:

* `git init`, which initializes a Git repository in the current directory,
* `git add `, which adds files or directories to the index,
* `git commit`, which records all of the files in the index in a commit,
* `git status`, which tells you the current state of the index and the working
  tree, and
* `git log`, which lists commits, newest first.

You also used the following Unix commands:

* `mkdir`, which makes a directory,
* `touch`, which updates the "last-modified" time of a file, and creates itm
  if it doesn't exist, and
* `echo`, which copies its command-line arguments to its output.

In the next unit, you'll start making and tracking changes.

