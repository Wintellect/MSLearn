# Start a project

It's time to get your Web-site project off the ground. In the exercises that follow, you will create a directory to serve as your project directory and create a simple HTML file in it. Then you will place that directory under Git's control by turning it into a Git repo. Finally, you will make some changes in the directory and learn to how commit the changes. 

There are actually two ways to create a Git working tree on your computer. One is to create a Git repo in an existing directory; the other is to clone an existing Git repository. You will see how the latter works in a subsequent unit. For now, let's start from scratch with an existing directory.

## Create a repository and working tree

Start by creating an empty directory and initializing a Git working tree inside it.

1. Create a directory named "cats" or something similar in the location of your choice. (The directory name is unimportant; Git is happy to work with it regardless.) This will be the *project directory* where your Web site is stored and the files that comprise it are subject to version control.

1. `cd` to the project directory in a Command Prompt window or terminal. Then execute a [git init](https://git-scm.com/docs/git-init) command to initialize the repository:

	```bash
	git init
	```
1. Now use a [git status](https://git-scm.com/docs/git-status) command to show the status of the working tree:

	```bash
	git status
	```

	Git responds by saying "Nothing to commit." It also says "On branch master" indicating that "master," which is presently the only branch, is the current branch. So far, so good.

1. Use an `ls` command to show the contents of the project directory:

	```bash
	ls -aF
	```

	Confirm that the directory contains a subdirectory named ".git." This is the directory in which Git stores metadata for the working tree.

You typically don't do anything with the ".git" directory directly. Git updates the metadata there as the status of the working tree changes. This directory is hands-off for you, but it's incredibly important to Git.

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

	A commit has now been staged. Git's "index" is a staging area for commits. It is a list of all the file versions that are going to be part of the *next* commit you make.

Rather than use `git add .`, you could have used `git add index.html` since **index.html** was the only new file in the directory. But had several files been added, `git add .` would have covered them all.

## Make your first commit

Now that **index.html** has been added to the index, the next step is to commit it. Doing so requires that you understand what "commit" really means.

_Commit_ is both a verb and a noun. It has essentially the same meaning as when you commit to a plan, or commit a change to a database. As a verb, committing changes means you put a copy (of the file, directory, or other "stuff") in the repository as a new version. As a noun, a commit is the small chunk of data that gives the changes you committed a unique identity. It includes the author's name and e-mail address, the date, comments about what you did (and why), an optional digital signature, and the unique identifier of the previous commit.

1. Use the following command to create a commit:

	```bash
	git commit index.html -m "Create an empty index.html file"
	```

	There are many different ways to phrase commit messages, but a good guideline is to write the first line in the present imperative tense so that it says *what the commit does to the tree*. It's also common to capitalize the first letter, and to leave off the closing period to save space. Imagine that the first line of the message completes the sentence starting with "When pushed, this commit will...."  

1. Follow up with a `git status` command and confirm that the working tree is clean — that is, the working tree contains no changes that haven't been committed.

1. Now use a [git log](https://git-scm.com/docs/git-log) command to show information about the commit:

	```bash
	git log
	```

1. Use this command to see an abbreviated version of the commit:

	```bash
	git log --oneline
	```

A commit message can have multiple lines. The first line should have no more than 50 characters and should be followed by a blank line. Subsequent lines should have no more than 72 characters. These aren't hard requirements, and they harken back to the days of punch cards and dumb terminals, but they do make `git log` output look better.

## Modify index.html and commit the change

**index.html** was created to serve as the Web site's home page, but it's currently empty. The next step is to pour some HTML into it. We'll start simple by using Unix's [echo](https://linux.die.net/man/1/echo) command to add a single line of HTML.

1. Execute the following command:

	```bash
	echo '<h1>Our Feline Friends</h1>' > index.html
	```

	The `>` operator redirects the command's output to a file — in this case, **index.html**.

1. Use a `git status` command to check the status of the working tree. What does it say about **index.html**?

1. Now commit the changes:

	```bash
	git commit -a -m "Add a heading to index.html"
	```

	The `-a` option adds all of the files you modified since the last commit.  It won't add _new_ files. For that, you still need `git add`.

The change to **index.html** has been committed. There are now two versions of the file in the repo, although you only see one of them (the current one). One of the benefits of using Git is that you can roll back the changes you have made, or go backwards in time and see previous versions. More on this important topic later.

## Explore the Git repository

This is a great time to take a look inside the repository and see what Git is doing while things are still relatively uncomplicated. The steps that follow aren't required, but they will help deepen your understanding of Git.

1. Use the following command to look inside the ".git" subdirectory:

	```bash
	ls -FC .git
	```

1. One of the files in the subdirectory is **COMMIT_EDITMSG**. It contains the most recent commit message. Use a [cat](https://linux.die.net/man/1/cat) command to list its contents to the screen:

	```bash
	cat .git/COMMIT_EDITMSG
	```

	Other files in the ".git" subdirectory include **HEAD**, which contains the file name of the branch that is currently checked out, and **config**, which contains the local configuration for the working tree.

1. Use `ls -RF` to drill down into the ".git/refs" directory:

	```bash
	ls -RFC .git/refs
	```

	Every branch has a corresponding file in ".git/refs/heads" that contains the hash of its head commit. Currently, there is just one branch, and therefore one file: **master**.

1. Now look inside the "/git/objects" directory:

	```bash
	ls -RFC .git/objects
	``` 

	It's worth taking a moment to note the way Git stores objects. The "objects" directory contains one subdirectory for each object in the working tree. The subdirectory name is the first two hex digits of the object's hash. Inside that subdirectory is another subdirectory containing a file whose name is a string of letters and numbers. Inside that file is the object itself.

1. Objects are stored in binary files (they're compressed with `gzip`), but you can examine their contents with [git show](https://git-scm.com/docs/git-show). To demonstrate, try this:

	```bash
	git show 'cat .git/refs/heads/master'
	```

	The diff shown is computed from the changed files; you can see the actual contents of the commit object using `git cat-file`:

	```bash
	git cat-file commit 4c3b05d4c547a39118ff3381f003d259f016aabf
	```

	And you can see the object's type with with the `-t` option:

	```bash
	git cat-file -t commit 4c3b05d4c547a39118ff3381f003d259f016aabf
	```

The `cat-file` subcommand is one of the low-level subcommands that the Git documentation refers to as _plumbing_. Higher-level subcommands, such as `show`, are called _porcelain_. Plumbing commands are designed to be used in scripts, and in fact many of the less-commonly-used Git subcommands *are* scripts, as you can see from:

```
for f in /usr/bin/git-*; do file $f; done
```

One of the reasons why Git has so many subcommands is that they're easy to create. Any executable file with a name starting with `git-` can be used as a subcommand. 

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