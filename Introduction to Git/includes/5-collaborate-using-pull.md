# Collaborate using pull requests

Your Web site for cat pictures is well underway and version control is being performed by Git. It's time to invite collaborators onto the project. During a pizza party at your house, your friend and fellow cat-lover [Alice](https://en.wikipedia.org/wiki/Alice_and_Bob) offers to help bring your vision to fruition, and you eagerly agree. Alice needs to make a copy of your project, and she will want to send her changes to you as she makes them.

This is where Git's _distributed_ nature comes in. It permits two or more people to work together on a project without fear of overwriting one another's work. Moreover, it allows you to check Alice's work before merging it with yours. Alice is talented, but no developer is perfect. Trust but verify.

In this lesson, you learn how to clone a repository to make it available to other people. You also learn to use one of Git's most important features: pull requests.

## Clone a repository

The proper way to copy a repo is to *clone* it with the [`git clone`](https://git-scm.com/docs/git-clone) command. To simulate Alice cloning your repo onto her computer, you'll create a directory named "Alice" on your computer and clone your project directory into there. In real life, you would accomplish this by setting up a network share or a remote reachable by URL. (More on this in a moment.)

1. Create a directory named "Alice" to clone the repo into. It must *not* be a subdirectory of your project directory, so `cd` up to the parent directory from your project directory to make "Alice" a sibling of the project directory. Then `cd` into the "Alice" directory:

	```bash
	cd ..
	mkdir Alice
	cd Alice
	```

1. Now use [`git clone`](https://git-scm.com/docs/git-clone) to clone the repo in your project directory into the "Alice" directory, and be sure to include the period at the end of the command:

	```bash
	git clone ../Cats .
	```

	`git clone` accepts a file-system path, an SSH path (for example, `git@example.com:alice/Cats` — you'll be familiar with this form if you've used `rsync` or `scp`); or a URL, typically starting with `file:`, `git:`, or `ssh`. The various types are described in the [documentation for `git clone`](https://git-scm.com/docs/git-clone). On Unix and Linux, the cloning operation uses hard links, which is fast and takes up very little space because only the directory entries need to be copied, not the files.

A clone of the repo in your project directory now lives in your "Alice" directory. Which means now is a great time to learn about remote repositories.

## Remote repositories

When Git clones a repository, it creates a reference to the original repo called a _remote_, with the name "origin," and sets it up so that it will pull from the remote repository. (Git can also "push"; you'll learn about that in the next lesson.) Origin is the default location for Git to pull changes from and push changes to. Pull, specifically, copies changes from the remote repository to the local one. It's very efficient because it only copies _new_ commits and objects, and then checks them into your working tree.

You pull from origin with the [`git pull`](https://git-scm.com/docs/git-pull) command. It's useful to compare `git pull` with other methods of copying files. The `scp` command (which is like the Unix `cp` command except that the files being copied don't have to be on the same computer) copies everything. If there are 10,000 files in the remote directory, `scp` copies them all. A more efficient program called `rsync` looks at every file in the local and remote directories, and only copies the ones that are different. It's often used for making backups, but `rsync` still has to hash every file unless they have different sizes or creation dates.

Git only has to look at commits. It already knows (because it saved the list) the last commit that it got from the remote repository. It then tells the computer from which it's copying to send everything that changed: the new commits and the objects they point to. Those get bundled up in a file called a _pack_ and sent over in one batch. Finally, Git updates the working tree by unpacking all the objects that changed, and merging them (if necessary) with the ones in the working tree.

Right now there's nothing for Alice to pull because you haven't made any changes since she cloned the repo. You can prove that with the following command, which responds "Already up-to-date:"

```bash
git pull
```

Git only pulls or pushes when you tell it to. That's different from, say, Dropbox, which has to ask the operating system to notify it of any changes you make in its folder, and occasionally ask the server whether anyone else has made changes.

## Make a change and submit a pull request

Alice starts working on the Web site. Her first decision is to change the site's background color. She experiments locally, and ultimately chooses her favorite shade of light blue.

1. Assume Alice's identity by executing the following commands:

	```bash
	git config user.name Alice
	git config user.email alice@contoso.com
	```

	These config settings are stored in the repo in **.git/config**, so you won't have to enter them again. Each time you `cd` into the "Alice" directory, you effectively assume Alice's identity.

1. Open **site.css** in the "Alice/assets" directory (not your project directory's "assets" directory) and replace the second line in the file with this one to change the background color of the page to light blue:

	```css
	body { font-family: serif; background-color: #F0FFF8; }
	```

1. Now commit the change:

	```bash
	git commit -a -m "Change background color to light blue"
	```

1. At this point, you (Alice) *could* attempt to push the changes to the original repo. But it would fail because Alice doesn't have permission to modify your repo. And that's as it should be. For now, you want to review Alice's changes before folding them into the master code base.

	For now, Alice has to submit a *pull request* asking you to pull her changes. She can do that with [`git request-pull`](https://git-scm.com/docs/git-request-pull). To that end, execute the following command, and once more be sure to include the period:

	```bash
	git request-pull -p origin/master .
	```

	`origin/master` is Alice's way of referring to the "master" branch on the "origin" remote.

This pull request is essentially the same thing as a pull request on [GitHub](https://github.com). It gives you a chance to review her changes before you incorporate her work into the Web site. Code reviews are an important part — some would say the most important part — of collaborative programming.

## Create a remote and complete the pull request

Because your project directory and the "Alice" directory are on the same computer, you can pull directly from the "Alice" directory. In real life, the "Alice" directory will be on Alice's computer. You solve this by setting up a *remote* using the [`git remote`](https://git-scm.com/docs/git-remote) command and using that remote for pulls and pull requests. Since it's not practical to set up two machines to do this, we'll set up a remote that uses a local path name. In reality, you would use a network path or URL instead.

1. `cd` back to the project directory and use a [`git remote`](https://git-scm.com/docs/git-remote) command to create a remote named "alice" that targets Alice's project directory:

	```bash
	cd ../Cats
	git remote add alice ../Alice
	```

1. Now execute a pull:

	```bash
	git pull alice master
	```

	Notice that you have to specify a branch, "master," in the pull command. You will learn in the next lesson how to fix that by setting an upstream URL.

1. Open the **index.html** file in your project directory in your browser. What color is the page background? What does this tell you about what `git pull` did? 

Behind the scenes, `git pull` is a combination of two simpler operations: `git fetch`, which gets the changes, and `git merge`, which merges those changes into your repository. In this case, the merge was _fast-forward_, meaning that Alice had your latest commit in her repository, so her commit could be added to the front of your history without any modification.

## Summary

In this lesson, you learned how to use pulls and pull requests to collaborate with another developer. You also became acquainted with the core Git commands used to support collaboration:

- [`git clone`](https://git-scm.com/docs/git-clone), which clones (copies) a repo
- [`git pull`](https://git-scm.com/docs/git-pull), which fetches commits from another repo and merges them into yours
- [`git request-pull`](https://git-scm.com/docs/git-request-pull), which creates a pull request
- [`git remote`](https://git-scm.com/docs/git-remote), which lists, creates, modifies, or deletes remotes

The fun is just beginning. In the next lesson, you learn how to set up and use a shared repository, which makes collaborating simpler and more convenient.
