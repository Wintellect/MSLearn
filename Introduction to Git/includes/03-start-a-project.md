# Start a project

It's time to get your Web-site project off the ground. In the exercises that follow, you will create a directory to serve as your project directory and create a simple HTML file in it. Then you will place that directory under Git's control by turning it into a Git repo. Finally, you will tk. 

The first step is to make a directory to hold your project, with a file in it (because git ignores empty directories). "Cats" is a little unimaginative, but it's easy to type. (Feel free to use something else -- nothing inside the working tree depends on the directory it's in.) Since this will be a website, the first file you need to create is **index.html**.

There are actually two ways to create a Git working tree on your computer. One is to create a Git repo in an existing directory; the other is to clone an existing Git repository. You will see how the latter works in a subsequent unit. For now, you'll start from scratch with an existing directory.

## Create a repository and working tree

Let's start by creating an empty directory and initializing a Git working tree inside of it.

1. Create a directory named "cats" or something similar in the location of your choice. (The directory name is unimportant; Git is happy to work with it regardless.) This will be the *project directory* where your Web site is stored. Then `cd` into that directory in a Command Prompt window or terminal.

1. Execute a [git init](https://git-scm.com/docs/git-init) command in the project directory to initialize the repository:

	```bash
	git init
	```
1. Now use a [git status](https://git-scm.com/docs/git-status) command to show the status of the working tree:

	```bash
	git status
	```

	Git responds by saying "Nothing to commit." So far, so good.

1. Use an `ls` command to show the contents of the project directory:

	```bash
	ls -aF
	```

	Confirm that the directory contains a subdirectory named ".git." This is the directory in which Git stores metadata for the working tree.

You typically don't do anything with the ".git" directory yourself. Git updates the metadata there as the status of the working tree changes. This directory is hands-off for you, but it's incredibly important to Git.

## Create and add (stage) a file

Git doesn't do much with empty directories, so let's add a file to the project directory to serve as the home page for the Web site.

1. Use a [touch](https://linux.die.net/man/1/touch) command to create a file named **index.html**:

	```bash
	touch index.html
	```

	`touch` updates a file's last-modified time if the file exists, or creates an empty file if it does not.

1. Now use `git status` to get the status of the working tree:

	```bash
	git status
	```

	Git responds by informing you that nothing has been committed, but the directory does contain a new file:

	```
	No commits yet
	
	Untracked files:
	  (use "git add <file>..." to include in what will be committed)
	
		index.html
	
	nothing added to commit but untracked files present (use "git add" to track)
	```

	Notice that `git status` gives you hints about what you can do next. Git can be configured to be less wordy, but at this stage, more is better.

1. Now use [git add](https://git-scm.com/docs/git-status) to add the new file to Git's "index," followed by `git status` to check the status. Don't forget the period at the end of the first command. It tells Git to index all of the files in the current directory that have been added or modified:

	```bash
	git add .
	git status
	```

	Git's "index" is a staging area for commits, so _staged_ is a shorter way of saying "in the index." The index is a list of all the file versions that are going to be part of the *next* commit you make.

Rather than use `git add .`, you could have used `git add index.html` since **index.html** was the only new file in the directory. But had several files been added, `git add .` would have covered them all.

## Make your first commit

Now that **index.html** has been added to the index, the next step is to commit it. Doing so requires that you understand what "commit" really means.

_Commit_ is both a verb and a noun. It has essentially the same meaning as when you commit to a plan, or commit a change to a database. As a verb, committing changes means you put a copy (of the file, directory, or other "stuff") in the repository as a new version. As a noun, a commit is the small chunk of data that gives a unique identity to the changes you committed. It includes the author's name and e-mail address, the date, comments about what you did (and why), an optional digital signature, and the unique identifier of the previous commit.

1. Use the following command to create a commit:

	```bash
	git commit index.html -m "Create an empty index.html file"
	```

	There are many different ways to phrase commit messages, but a good guideline is to write the first line in the present imperative tense so that it says *what the commit does to the tree*. It's also common to capitalize the first letter, and to leave off the closing period to save space. Imagine that the first line of the message completes the sentence starting with "When pushed, this commit will...."  

1. Follow up with a `git status` command and confirm that the working tree is clean.

1. Now use a [git log](https://git-scm.com/docs/git-log) command to show information about the commit:

	```bash
	git log
	```

1. Use this command to see an abbreviated version of the commit:

	```bash
	git log --oneline
	```

A commit message can have multiple lines. The first line should have no more than 50 characters, and should be followed by a blank line. Subsequent lines should have no more than 72 characters. These aren't hard requirements, but they do make `git log` output look better.

## Add content

We need to put some kind of content onto our cat-centric website, and it makes sense to start with its home page. Here, you use the `echo` command to add a heading line to `index.html`. `echo` is a Unix command that echoes whatever you type. The `>` on the command line redirects the command's output to a file.

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

The `-a` option to `git commit` adds all of the files you modified since the last commit.  It won't add _new_ files -- for that you still need `git add`.

## Explore the Git repository

This is a good time to take a look inside the Git repository, while things are still uncomplicated. We use `ls -RFC` to make a recursive directory listing with flag characters (e.g., `/` flags directories, and `*` flags executable files).

```
$ ls -FC .git
COMMIT_EDITMSG	HEAD  branches	config	description hooks  index  info  logs
objects	        refs
```

You can use `cat` to view the contents of `COMMIT_EDITMSG`, which contains the most recent commit message, HEAD, which contains the filename of the branch (`master`) that is currently checked out, and `config`, which contains the local configuration for this working tree.

Using `ls -RF` you can drill down into `refs` and `objects`. (The following listing has been edited; missing parts are indicated by Bash comments, which start with `#`.)

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

Every branch (`master` is the only one at the moment) has a corresponding file in `refs/heads` that contains the hash of its head commit.

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

(Bash replaces a command enclosed in back-quotes with its output.) The diff shown is computed from the changed files; you can see the actual contents of the commit object using `git cat-file`:

```
$ git cat-file commit 4c3b05d4c547a39118ff3381f003d259f016aabf
tree 419d0dd7f1068e70e6b9e60b00f0235e0f5aa795
parent 93dda01e79f9f791c0fcba727ff18d1c7ccf76c8
author Steve Savitzky <steve@savitzky.net> 1557869206 -0700
committer Steve Savitzky <steve@savitzky.net> 1557869206 -0700

add a heading to index.html
```

You can use the `-t` option to get the object's type. The `cat-file` command is one of the low-level commands that Git documentation refers to as _plumbing_. The higher-level commands, such as `show`, are called _porcelain_. Plumbing commands are designed to be used in scripts, and in fact many of the less-commonly-used Git subcommands *are* scripts, as you can see from:

```
for f in /usr/bin/git-*; do file $f; done
```

One of the reasons why Git has so many sub-commands is that they're so easy to create: Any executable file with a name starting with `git-` can be used as a subcommand. 

## Summary

In this unit, you learned how to create a project that is under Git's control. You also learned about the following Git subcommands:

- [`git init`](https://git-scm.com/docs/git-init), which creates and initializes a Git repository in the current directory
- [`git add `](https://git-scm.com/docs/git-add), which adds files or directories to the index
- [`git commit`](https://git-scm.com/docs/git-commit), which records all of the files in the index in a commit
- [`git status`](https://git-scm.com/docs/git-status), which tells you the current state of the index and the working tree
- [`git log`](https://git-scm.com/docs/git-log), which lists commits, newest first 
- [`git show`](https://git-scm.com/docs/git-show), which prints the contents  of an object in human-readable form, and
- [`git cat-file`](https://git-scm.com/docs/git-cat-file), which outputs the contents of an object.

In the next unit, you start making and tracking changes. (You get to do cat photos, too.)