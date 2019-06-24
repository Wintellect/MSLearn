## Explore the Git repository

*This section originally appeared at the end of the unit entitled "Start a project."* 

This is a great time to take a look inside the repository and see what Git is doing while things are still relatively uncomplicated. The steps that follow aren't required, but they will help deepen your understanding of Git.

1. Use the following command to look inside the repository (the ".git" subdirectory):

	```bash
	ls -FC .git
	```

1. One of the files in the subdirectory is **COMMIT_EDITMSG**. It contains the most recent commit message. Use a [`cat`](https://linux.die.net/man/1/cat) command to list its contents to the screen:

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

	It's worth taking a moment to note the way Git stores objects. The "objects" directory contains one subdirectory for each object in the working tree. The subdirectory name is the first two hex digits of the object's hash. Inside that subdirectory is a file whose name is a string of letters and numbers containing the object itself.

1. Objects are stored in binary files (they're compressed with `gzip`), but you can examine their contents with [`git show`](https://git-scm.com/docs/git-show). To demonstrate, try this:

	```bash
	git show `cat .git/refs/heads/master`
	```

	The output shows the diff between the changed files. You can see the actual contents of the commit object by using [`git cat-file`] and providing the commit ID:

	```bash
	git cat-file commit COMMIT_ID
	```

The `cat-file` subcommand is one of the low-level subcommands that the Git documentation refers to as _plumbing_. Higher-level subcommands, such as `show`, are called _porcelain_. Plumbing commands are designed to be used in scripts, and in fact many of the less-commonly-used Git subcommands *are* scripts. One of the reasons why Git has so many subcommands is that they're easy to create. Any executable file with a name starting with `git-` can be used as a subcommand. 