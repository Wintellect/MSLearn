# Collaborate using pull

Your Web site for cat pictures is well underway and version control is being performed by Git. It's time to invite collaborators onto the project. After a pizza party at your house, your friend and fellow cat-lover [Alice](https://en.wikipedia.org/wiki/Alice_and_Bob) offers to help bring your vision to fruition, and you eagerly agree. Alice needs to make a copy of your project, and she will want to send her changes to you as she makes them.

This is where Git's _distributed_ nature comes in. It permits two or more people to work together on a project without fear of overwriting one another's work. Moreover, it allows you to check Alice's work before merging it with yours. Alice is talented, but no developer is perfect. Trust but verify.

In this unit, you learn how to clone a repository to make it available to other people. You also learn to use one of Git's most important features: pulls.

## Clone a repository

Instead of making an empty directory and running `git init` to initialize it, Alice uses [`git clone`](https://git-scm.com/docs/git-clone) to copy your repo. Since she's already on your household Wi-Fi network, she can mount the directory as a network share; for now (and for the sake of simplicity) we make an ordinary directory named "Alice" to take the place of her home directory. You're probably in your working tree project directory, so you need to change to the parent directory first.

1. Create a directory named "Alice" to clone the repo into. It must *not* be a subdirectory of your project directory, so `cd` up to the parent directory first so "Alice" is a sibling of "Cats." Then `cd` into the "Alice" directory:

	```bash
	cd ..
	mkdir Alice
	cd Alice
	```

	In real life, Alice would be cloning this onto her machine. For training purposes, since you probably don't have a programmer friend named Alice, both your repo and hers will reside on your computer.

1. Now use [`git clone`](https://git-scm.com/docs/git-clone) to clone the repo in your project directory into the "Alice" directory, and be sure to include the period at the end of the command:

	```bash
	git clone ../Cats .
	```

	`git clone` accepts a file-system path, an SSH path (e.g. `git@example.com:alice/Cats` — you'll be familiar with this form if you've used `rsync` or `scp`); or a URL, typically starting with `file:`, `git:`, or `ssh`. The various types are described in the [documentation for `git clone`](https://git-scm.com/docs/git-clone). On Unix and Linux, the cloning operation uses hard links, which is fast and takes up very little space because only the directory entries need to be copied, not the files.

A clone of the repo in your project directory now lives in your "Alice" directory. Which means now is a great time to learn about remote repositories.

## Remote repositories

When Git clones a repository, it creates a reference to the original repo called a _remote_, with the name "origin," and sets it up so that it will pull from the remote repository. (Git can also "push"; we'll get to that in the next unit.) Origin is the default location for Git to pull changes from and push changes to. Pull, specifically, copies changes from the remote repository to the local one. It's very efficient because it only copies _new_ commits and objects, and then checks them into your working tree.

You pull from origin with the [`git pull`](https://git-scm.com/docs/git-pull) command. It's useful to compare `git pull` with other methods of copying files. The `scp` command (which is like the Unix `cp` command except that the files being copied don't have to be on the same computer) copies everything. If there are 10,000 files in the remote directory, `scp` copies them all. A more efficient program called `rsync` looks at every file in the local and remote directories, and only copies the ones that are different. It's often used for making backups, but `rsync` still has to hash every file unless they have different sizes or creation dates.

Git only has to look at commits. It already knows (because it saved the list) the last commit that it got from the remote repository. It then tells the computer from which it's copying to send everything that changed: the new commits and the objects they point to. Those get bundled up in a file called a _pack_ and sent over in one batch. Finally, Git updates the working tree by unpacking all the objects that changed, and merging them (if necessary) with the ones in the working tree.

Right now there's nothing for Alice to pull because you haven't made any changes since she cloned the repo. You can prove that with the following command, which responds "Already up-to-date:"

```bash
git pull
```

Git only pulls or pushes (which is copying in the other direction) when you tell it to. That's different from, say, Dropbox, which has to ask the operating system to notify it of any changes you make in its folder, and occasionally ask the server whether anyone else has made changes. A program named [SparkleShare](https://www.sparkleshare.org/) does something similar using Git. SparkleShare still has to keep track of changes on both ends, but it keeps all of your history, and if you own the server it uses you don't have to pay for space.

## Make a change and submit a pull request

Alice starts working on the Web site. Her first decision is to change the site's background color. She experiments locally, and ultimately chooses her favorite shade of light blue.

1. Temporarily assume Alice's identity by executing the following commands:

	```bash
	git config user.name Alice
	git config user.email alice@contoso.com
	```

1. Open **site.css** in the "Alice/assets" directory (not your project directory's "assets" directory) and replace the second line in the file with this one:

	```css
	body { font-family: serif; background-color: #F0FFF8; }	
	```

1. Now commit the change:

	```bash
	git commit -a -m "Change background color to light blue"
	```

1. At this point, you (Alice) *could* attempt to push the changes to the original repo. But it would fail because Alice doesn't have permission to modify your repo. And that's as it should be. For now, you want to review Alice's changes before folding them into the master code base.

	For now, Alice has to submit a *pull request* asking you to pull her changes. She can do that with [`git request-pull`](https://git-scm.com/docs/git-request-pull). To that end, execute the following command:

	```bash
	$ git request-pull -p origin/master .
	```

	`origin/master` is Alice's way of referring to the "master" branch on the "origin" remote.

This pull request is essentially the same thing as a pull request on [GitHub](https://github.com). It gives you a chance to review her changes before you incorporate her work into the Web site. Code reviews are an important part — some would say the most important part — of collaborative programming.

## An unsuccessful pull

Now, you can try to pull from Alice's repository:

```
$ cd ../../Cats
$ git pull ../../Alice/Cats
fatal: '../../Alice/Cats' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

That didn't work because the path you took out of Alice's email was relative to _her_ repository, not yours. An absolute path or a public URL would have worked in this case.

However, because you and Alice are going to collaborate regularly, it makes more sense to create a remote.

## Create a remote and pull from it

You create a remote using:

```
$ git remote add alice ../Alice/Cats
```

and pull from it with:

```
$ git pull alice master
From ../Alice/Cats
 * branch            HEAD       -> FETCH_HEAD
Updating 2c01c05..37903fd
Fast-forward
 assets/site.css | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Notice that you have to specify a branch, `master`, in the pull command. We'll see in the next unit how to fix that by setting an upstream URL.

Behind the scenes, `git pull` is a combination of two simpler operations: `git fetch`, which gets the changes, and `git merge`, which merges those changes into your repository. In this case, the merge was _fast-forward_, meaning that Alice had your latest commit in her repository, so her commit could be added to the front of your history without any modification.

(We'll see non-fast-forward merges in unit 8.  Merging can cause enough complications to make it worth its own unit.)

## Summary

In this unit, you learned how to collaborate with another developer using nothing more than a thumb drive or a network share. You also became acquainted with the core Git commands used to support collaboration:

- [`git clone`](https://git-scm.com/docs/git-clone), which clones (copies) a repo
- [`git pull`](https://git-scm.com/docs/git-pull), which fetches commits from another repo and merges them into yours
- [`git request-pull`](https://git-scm.com/docs/git-request-pull), which creates a pull request
- [`git branch`](https://git-scm.com/docs/git-branch), which lists,  creates, modifies, or deletes branches
- [`git remote`](https://git-scm.com/docs/git-remote), which lists, creates, modifies, or deletes remotes

But you're not finished yet. In the next unit, you learn how to set up and use a shared repository, which makes collaborating much simpler and more convenient.
