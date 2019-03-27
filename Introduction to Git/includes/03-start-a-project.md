# Start a project

Now it's time to get your website project off the ground.  You'll need to make
a directory to hold your project, with a file in it (because git ignores empty
directories).  Since this will be a website, the first file will be
`index.html`.  We'll call the working tree "Website".

There are actually two ways to get a git working tree on your computer; the
other one is to clone an existing git repository.  We'll see how that works
starting in Unit 6.

## Create a repository and working tree

First, make the directory, `cd` into it, and initialize the repository.

```
$ mkdir Website
$ cd Website
$ git init
Initialized empty Git repository in /home/you/Website/.git/
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
$ ls -a
.  ..  .git
```

## Creat and add (stage) a file


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
tree.  The `touch` command updates a file's "last modified" time, and it
creates an empty file if it wasn't there before.

There's no real need to start with an empty file; in fact you can start with
an entire project that you started before you learned how to use version
control.

## Make your first commit


```
$ git commit index.html -m "create an empty index.html file"
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
because a commit includes the date and time it was made.

If you don't provide a message on the command line, `git commit` will invoke
your default text editor so that you can create it.  A commit message can have
multiple lines; the first line should have no more than 50 characters, and
there should be a blank line after it.  Subsequent lines should have no more
than 72 characters.  These aren't hard requirements, they just make Git's
messaging look better.  For example, the format of `git log --oneline` adds
25 characters to the message, so a 50-character message will still fit
conveniently in an 80-column default terminal window.

There are many different ways to phrase commit messages, but a good one is to
imagine that the first line of the message completes the sentence starting
with "When pushed, this commit will...".  Different teams will have different
wording and formatting conventions.

## Add content

Here, we will use the `echo` command to add a heading line to `index.html`.


```
$ echo '<h1>Hello, world!</h1>' > index.html
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

## Commands introduced in this unit

```
git init
git add 
git commit
git status
git log
```
