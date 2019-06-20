# Collaborate using a shared repo

Directly pulling from someone else's repository works, provided you're both on the same network, but it's a clumsy process — and most collaborators are not on the same network. It's much better to set up a central repository to which everyone involved can push as well as pull from.

When you tell [Bob](https://en.wikipedia.org/wiki/Alice_and_Bob) about your project, and he asks to participate too, that's exactly what you decide to do.

## Create a bare repository

What you need is a repository that doesn't have a working tree. That's called a _bare repository_. A bare repo has several advantages:

- Without a working tree, everybody can push changes without having to worry about which branch is checked out.
- It's easy for Git to detect when somebody else has pushed changes that might conflict with yours (because your push wouldn't be fast-forward, and Git's default is to reject it so that you can merge the new files with your own).
- A shared repo scales to any number of developers. You only have to know about the shared repo rather than about all the other people from whom you might need to pull.
- By putting the shared repo on a server that you can all access, you don't have to worry about firewalls and permissions.
- You don't need separate accounts on the server, because Git keeps track of who made each commit. GitHub has millions of users all sharing the `git` account. (Everyone uses `ssh`, and users are distinguished by their public keys.) 

Creating a bare repo for sharing is easy.

1. Create a new directory named "Shared.git" on your hard disk to hold the bare repo. Once more, the directory name is not important, but we will refer to it as the "Shared.git" directory or simply the *shared* directory in these exercises.

	> Naming the directory "Shared.git" follows the longstanding tradition of assigning bare repositories a name ending with `.git` to distinguish them from working trees. It is a convention but not a requirement.

	Assuming you are currently in the project directory, use these commands to created the shared directory as a sibling of the project directory and `cd` into it:

	```bash
	cd ..
	mkdir Shared.git
	cd Shared.git
	```

1. Now use the following command to create a bare repo in the shared directory:

	```bash
	git init --bare
	```

1. The next step is to get the contents of _your_ repo into the shared repo. Use these commands to return to the project directory where your repo is stored, set up an "origin" remote, and perform an initial push:

	```
	cd ../Cats
	git remote add origin ../Shared.git
	git push origin master
	```

1. You want `push` and `pull` to use "origin's" master branch by default, just as if you had made your repo by cloning it in the first place. To do so, you need to tell Git which branch to track:

	```
	git branch --set-upstream-to origin/master
	```

Git would have complained if you had tried to do this before the initial push, because the new repository had no branches yet. Git can't track a branch that doesn't exist. All Git is doing under the hood is looking in ".git/refs/remotes" for a file named **origin/trunk**.

## Set up for collaborators

The next step is for Bob to clone the bare repository, and then for Alice to set the origin in her repo to target the shared repo for pushes and pulls.

1. Create a directory named "Bob" that's a sibling of the project directory and `cd` into the "Bob" directory:

	```bash
	cd ..
	mkdir Bob
	cd Bob
	```

2. Now clone the shared repo, and be sure to include the period at the end of the command:

	```Bash
	git clone ../Shared.git/ .
	```

1. Currently, Alice's repo is configured to push to and pull from her own repo. Use the following commands to `cd` to the "Alice" directory and change "origin" to point to the shared repo:

	```bash
	cd ../Alice
	git remote set-url origin ../Shared.git
	git push
	```

The push wasn't necessary, but it's a simple way of making sure the remote is set up with the correct defaults.

## Start collaborating

Now that Bob is set up to work on the Web site, he decides to add a footer to the bottom of the page. Let's take on Bob and Alice's persona for a few moments and learn the basics of collaboration.

1. Begin by navigating to the "Bob" directory and impersonating Bob:

	```bash
	cd ../Bob
	git config user.name Bob
	git config user.email bob@contoso.com
	```

1. Use your favorite text editor to open **index.html** and replace the `<hr>` element near the bottom of the page with this:

	```html
	<footer><hr>Copyright (c) 2019 Contoso Cats</footer>
	```

	Then save the file.

1. Commit the changes and push to the remote origin:

	```
	git commit -a -m "Put a footer at the bottom of the page"
	git push
	```

1. While Bob is editing the site, Alice is, too. She decides to add a nav bar to the page. This requires her to modify two files: **index.html** and **site.css**. `cd` to the "Alice" directory and configure Git to use Alice's credentials:

	```bash
	cd ../Alice
	git config user.name Alice
	git config user.email alice@contoso.com
	```

1. Now open **index.html** and insert the following line right after the `<body>` tag on line 8:

	```html
	<nav><a href="./index.html">home</a></nav>
	```

1. Open **site.css** in the "assets" subdirectory and add the following line at the bottom:

	```css
	nav { background-color: #C0D8DF; }
	```

1. Save both files. Now let's assume that Alice receives an e-mail from Bob saying he has made changes to the site. She decides to pull his changes before committing her own. (If she had already committed her changes, she would have a different problem which is discussed in the next unit.) Do a pull with `git pull`:

	```bash
	git pull
	```

	From the output, it looks as if Git has prevented a problem:

	```
	remote: Counting objects: 3, done.
	remote: Compressing objects: 100% (3/3), done.
	remote: Total 3 (delta 2), reused 0 (delta 0)
	Unpacking objects: 100% (3/3), done.
	From ../Shared
	   843d142..2cf6cbf  master     -> origin/master
	Updating 843d142..2cf6cbf
	error: Your local changes to the following files would be overwritten by merge:
	        index.html
	Please commit your changes or stash them before you can merge.
	Aborting
	```

	Git warns that the pull would overwrite Alice's version of **index.html** and lose her changes. That's because Bob modified **index.html**, too. If Alice hadn't changed **index.html**, Git would have gone ahead and committed the merge.

1. Use a `git diff` command to see what changes Bob made to **index.html**:

	```bash
	git diff origin -- index.html
	```

1. From the output, it is evident that Alice's changes and Bob's changes don't overlap. Now Alice can _stash_ her changes. [`git stash`](https://git-scm.com/docs/git-stash) saves the state of the working tree and index by making a couple of temporary commits. Think of the stash as a way to save your current work while you do something else, without making a "real" commit or affecting your repository history.

	> In reality, Alice should have stashed or committed her changes before she tried to pull. Pulling to a "dirty" working tree is risky, because it can do things from which you can't easily recover.

	Use the following command to stash Alice's changes:

	```bash
	git stash
	```

1. Now it's safe for Alice to pull, after which she can "pop" the stash, which is organized as a stack. (In fact, `git stash` is shorthand for `git stash push`. It's a lot like the stack where you put bills that you haven't gotten around to paying yet.) 

	```bash
	git pull
	git stash pop
	```

	Popping the stash merges the changes. If changes overlap, there may be a conflict. You will learn later how to resolve those situations.

1. At this point Alice can continue working, or simply commit and push her changes. Let's make another change as Alice by assigning footers the same style as nav bars. Open **site.css** and replace the third line — the one that styles `<nav>` elements — with this one, and as usual, save your changes:

	```html
	nav, footer { background-color: #C0D8DF; }
	``` 

1. Now commit the changes and push them to the shared repo:

	```bash
	git commit -a -m "Stylize the nav bar"
	git push
	```

1. The updated site is now in shared repo. Finish up returning to the project directory, assuming your own identity again, and doing a pull:

	```bash
	cd ../Cats
	git config user.name USER_NAME
	git config user.email USER_EMAIL
	git pull
	```

1. Confirm that the changes made by both Bob and Alice are present in your local repo by opening **index.html** (the one in the project directory) in your browser and verifying that it looks like this:

	![The updated home page](media/cats-home-page.png)

	_The updated home page_

Note that if Alice had committed her changes rather than stashing them a few moments ago, the situation would have been somewhat different. She would have had to make a branch and either merge or rebase her changes. (Branches, merging, and rebasing are covered in the next unit.)

Had Alice begun by working on a branch in the first place she would have saved herself quite a lot of trouble. You will learn how to do that in the next unit. For now it's worth pointing out that branching and rebasing is _exactly_ what `stash` accomplishes behind the scenes.

## Summary

In this unit, you learned how to set up a bare repository that can be shared among a group of developers, and about some new and very important Git commands:

- [`git init --bare`](https://git-scm.com/docs/git-commit), which sets up a repo that can be shared
- [`git branch --set-upstream-to`](https://git-scm.com/docs/git-branch), which specifies the default origin and branch for pushes and pulls
- [`git stash`](https://git-scm.com/docs/git-stash), which saves uncommitted changes so you can merge safely
- [`git push`](https://git-scm.com/docs/git-push), which merges changes with a remote repo

In the next unit, you take another big step by learning how to create and merge branches.