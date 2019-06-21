# Resolve merge conflicts

Sometimes, no matter how well you plan, things go wrong. Imagine that two developers are working on the same file at the same time and change the same line. When they push their changes, the second one will experience a *merge conflict*. Deveolopers using version control despise few things more than merge conflicts. But conflicts happen, and you best — no, *must* — know how to deal with them.

The good news is that Git provides solutions for dealing with merge conflicts. In this unit, you will learn about two of them. 

# Make a change as Alice

Let's started by taking on Alice's role again and making a change to the Web site's home page by replacing the picture of Bob's cat with a picture of Alice's.

1. Navigate to the "Alice" directory and configure Git to use Alice's credentials:

	```bash
	cd ../Alice
	git config user.name Alice
	git config user.email alice@contoso.com
	``` 

1. Create a branch named "add-cat" to work in:

	```bash
	git checkout -b add-cat
	```

1. Copy **bombay-cat-180x240.jpg** from [insert location here] into Alice's "assets" directory. Then open **index.html** and replace this line:

	```html
	<img src="assets/bobcat2-317x240.jpg">
	```

	With this one:

	```html
	<img class="cat" src="assets/bombay-cat-180x240.jpg">
	```

	Then save the file.

1. Now commit the changes, merge the "add-cat" branch into "master," and push the changes:

	```bash
	git commit -a -m "Add picture of Alice's cat"
	git merge --ff-only add-cat
	git push
	```

Finish up by confirming that the push succeeded.

# Make a change as Bob

Without knowing what Alice is doing, Bob notices that Alice's last push added a CSS style named `cats` to **site.css**. So he decides to apply that class to his cat picture.

1. Start by assuming the role of Bob:

	```bash
	cd ../Bob
	git config user.name Bob
	git config user.email bob@contoso.com
	```

1. Create a branch named "style-cat" to work in:

	```bash
	git checkout -b style-cat
	```

1. Open **index.html**, add a `class="cat"` attribute to the `<img>` element, and save the file:

	```html
	<img class="cat" src="assets/bobcat2-317x240.jpg">
	```

1. Now commit the change, merge the current branch into "master," and push:

	```bash
	git commit -a -m "Style Bob's cat"
	git merge --ff-only style-cat
	git push
	```

	The output should look something like this:

	```

	```

And there it is: the dreaded merge conflict. The same line in the same file was changed by two people. Git sees that and reports tk.










## Explore a complicated history

This is a good time to try some of the Git tools that let you visualize the structure of Git's history graph. The first one to try is:

```
git log --graph --all
* commit 2868bbfa4f1b6283d162f06b96f305a224d57bc2 (master)
| Author: Alice <alice@example.com>
| Date:   Wed May 15 23:00:20 2019 -0700
| 
|     Add picture of Dinah
|   
| * commit f98a6e349309086088228feb8b284e12b72ee4de (HEAD -> addCat)
| | Author: Bob <bob@example.com>
| | Date:   Wed May 15 22:06:11 2019 -0700
| | 
| |     Add style class to cat picture
| | 
| * commit a6ed876ebc924d16f7589c221526d07220d64f33
|/  Author: Bob <bob@example.com>
|   Date:   Wed May 15 21:50:35 2019 -0700
|   
|       Add picture of Bob's cat
|
```

The command produces a graph similar to the ones displayed in this unit, only rotated counter-clockwise so that it goes up the left-hand side of the log output. Because it uses vertical bars and slashes, it works perfectly in a terminal window; that's especially useful when you're running it on a remote server.

Of course, when you can run GUI programs, there are better options -- and quite a few are available! The one that is shipped as part of Git is `gitk`:


```
gitk --all &
```

Gitk is a GUI program for exploring Git histories; the `--all` option tells it to show all of the branches. The `&` at the end of the line tells Bash to run the command in another process, so that you can continue working in the shell.

![Screenshot of gitk --all.](media/gitk-screenshot.png)
Gitk gives you a window with a view similar to `git log --graph` in the top pane, and the details of each commit in the bottom pane. Between them are search and navigation tools, as well as a box containing the full ID of the selected commit. This is automatically selected, which makes it easy to copy and paste into a command.

Getting a picture of your history with one of these tools is especially useful after a pull to get an overview of the changes, or when you're about to do something you're not certain will work the way you expect. You can refresh Gitk with the `F5` key to see what actually happened.

## Bob's options

Bob has several things he can do at this point.

You've already seen two methods, `merge` and `rebase`. They produce histories that look like:

``` 
# git checkout master; git merge --addCat
merge:  ...o---m---A---D---E
                    \     /
                     B---C

# git checkout addCat; git rebase master
rebase: ...o...m...A...D...B...C
```

Merge has the advantage of preserving all of the individual changes and recording the merge metadata in a commit. Rebase has the advantage of keeping the history simple and easy to understand. In both cases, if there's a conflict, Git interrupts the process to let you try to resolve it.

## Simplify history by squashing

If there are more than one commit on a branch, both merging and rebasing make it hard to see the big picture. That's especially true if the commits have messages like "Fix off-by-one bug," "make backup," "Revert bad merge," or something even less helpful (see [this xkcd cartoon](https://xkcd.com/1296/) for an example). It's better to combine all of the commits on a branch into a single one. That lets you compose a new commit message that describes *what you did* rather than the details of how you did it, and store that information in the project's official history. The process of combining commits is called _squashing_.

There are two different ways to squash commits, plus a short-cut. Many developers take the short-cut mentioned in the last unit and simply make a single commit that they keep amending. It's not really a good idea, because it's much harder to find a problem in an amended commit with a bug in it that
was introduced sometime in the last week, than a series of simple ones made every day or so.  (Take a look at the man page for `git bisect` to see how to find bugs quickly in a long sequence of commits.)

The two (better) ways to package-up several changes into a single commit are `git merge --squash` and `git rebase --interactive` (usually shortened to `git rebase -i`). Interactive rebase creates a temporary file containing all of the commits and their one-line descriptions, preceeded by a command. Initially the command is `pick`; you can edit that to `drop`, `squash`, `edit`, or `reword`. (Edit lets you edit files; reword just lets you edit the commit message.) You can also change the order of the commits.

Squashing is simpler: It simply performs all of the changes that would have been made by a real merge, but it stops just short of making the merge commit or moving HEAD. All of the changed files are left in the working tree and index, ready to commit.

In a simpler world, Bob could just do:

```
# git merge --squash addCat
# git commit -m "Add Bob's cat"
```

(We use `#` instead of `$` to indicate that you shouldn't actually type those commands -- Bash ignores everything from `#` to the end of the line.)

It isn't *quite* that simple, because Bob and Alice each changed the same line in `index.html`, which created a merge conflict.

## Resolve merge conflicts

What *actually* happens when Bob makes his merge is that Git notices that the branches being merged have changes that overlap, so it interrupts the merge process to let him figure out what the final result should be.

```
$ git merge --squash addCat
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Squash commit -- not updating HEAD
Automatic merge failed; fix conflicts and then commit the result.
$ git commit -m "Add  Bob's cat"
U	index.html
error: Committing is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
```

Notice that Bob tried to ignore the conflict and commit anyway; naturally, he got an error message.

When Git detects a conflict, it inserts *both* conflicting versions into the file, between lines starting with `<<<<<<<`, `=======`, and `>>>>>>>`.  The part before the `=======` line is "your" side of the merge -- the branch you were already on -- and the part after is "their" side -- the branch you specified in the `merge` command.

In this case it looks like this:

```
<h1>Our Furry Friends</h1>
<<<<<<< HEAD
<img class=".cat" src="assets/bombay-317x240.jpg">
=======
<img class=".cat" src="assets/bobcat2-317x240.jpg">
>>>>>>> addCat
<footer><hr></footer>
```

In this case, Bob wants to keep Alice's cat photo and add his own, so he simply deletes the markers.

```
$ sed -i.bak -e '/<<<</d' -e '/====/d' -e '/>>>>/d' index.html
$ git add index.html
$ git commit -m "Add Bob's cat"
[master 39473bb] Add Bob's cat
 2 files changed, 1 insertion(+)
 create mode 100644 assets/bobcat2-317x240.jpg
$ git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 37.49 KiB | 7.50 MiB/s, done.
Total 5 (delta 1), reused 0 (delta 0)
To /home/steve/sandbox/Cats.git
   2868bbf..39473bb  master -> master
```

The `git add` tells Git that the conflict in `index.html` was resolved, and the `git merge --continue` finishes the merge.

Another option, if Bob had decided that he shouldn't have made the merge after all, was `git merge --abort`; that option only works if there are conflicts.

## Exploring merge alternatives

Bob could also use `git reset --hard` in both of the merged branches to get back to what he had before a merge. In this case, the `adCat` branch hasn't actually been merged, so Bob only has to reset `master`.

It's worthwhile playing around a little to see Bob's alternatives.

First, let's look at what happens if Bob does the squash but takes the default merge message instead of replacing it.

```
$ git reset --hard HEAD^
$ git merge --squash addCat
$ sed -i.bak -e '/<<<</d' -e '/====/d' -e '/>>>>/d' index.html
$ git add index.html
$ git commit --no-edit
$ git log -n1
commit ffc8fde164f4cded11ed1f965a2602d894d059c7 (HEAD -> master)
Author: Bob <bob@example.com>
Date:   Fri May 17 14:28:33 2019 -0700

    Squashed commit of the following:
    
    commit f98a6e349309086088228feb8b284e12b72ee4de
    Author: Bob <bob@example.com>
    Date:   Wed May 15 22:06:11 2019 -0700
    
        Add style class to cat picture
    
    commit a6ed876ebc924d16f7589c221526d07220d64f33
    Author: Bob <bob@example.com>
    Date:   Wed May 15 21:50:35 2019 -0700
    
        Add picture of Bob's cat
    
    # Conflicts:
    #       index.html
```

As you can see, it's usually a good idea to edit the message to something that makes sense, but if Bob hadn't used the `--no-edit` option, Git would have initialized the commit message with something that might be a good start.

## Backing out of a conflicted merge

Sometimes the best thing to do when there is a conflict is to back out of it. This is particularly useful if you do a simple pull instead of `pull --rebase`. In that case, you can use `git merge --abort` or `git rebase --abort` to back out. Unlike the case with squash, once you fix the conflict you can go forward with `git merge --continue` or `git rebase --continue`.

### Exercise:

Try the following:

```
$ git reset --hard HEAD^
$ git merge addCat
$ git merge abort
```

and 

```
$ git merge addCat
$ sed -i.bak -e '/<<<</d' -e '/====/d' -e '/>>>>/d' index.html
$ git add index.html
$ git merge --continue
```

That last exercise puts you into the text editor looking at the default merge message, which is just `Merge branch 'addCat'`. If you delete the message, Git aborts the commit just as it does with any commit. That's a good way of backing out of a pull that should have been a rebase.

Since Bob has already pushed the squashed merge, he can get it back with:

```
$ git reset --hard origin/master
HEAD is now at 39473bb Add Bob's cat
```

It's often a good idea to keep a remote called "backup" to which you push changes to every evening, or whenever you want to try something tricky. If you've done some rebasing, you can use `git push --force backup`.

## Merge tools

Some people prefer to see the versions being merged side-by-side so that they can see what their choices are and select them interactively. Some version control systems have a tool of this sort (e.g. `p4merge` from Perforce), as do several text editors (e.g. `emerge` in Emacs and `vimdiff` in Vim).

Git doesn't have a tool of its own for this purpose. You can specify your favorite on the `git mergetool` command line or with the `merge.tool` configuration variable.

The `--tool-help` option shows the list of known tools:

```
$ git mergetool --tool-help
'git mergetool --tool=<tool>' may be set to one of the following:
		araxis
		emerge
		vimdiff
		vimdiff2
		vimdiff3

The following tools are valid, but not currently available:
		bc
		bc3
		codecompare
		deltawalker
		diffmerge
		diffuse
		ecmerge
		examdiff
		gvimdiff
		gvimdiff2
		gvimdiff3
		kdiff3
		meld
		opendiff
		p4merge
		tkdiff
		tortoisemerge
		winmerge
		xxdiff

Some of the tools listed above only work in a windowed environment. If run in a terminal-only session, they fail.
```

Naturally, if you run this command on your own computer you are likely to get a different list.

## Summary

In this unit you learned how to deal with merge conflicts, using the `--continue` and `--abort` options with `git merge`, and either a text editor or a merge tool. You can also use those options with `git rebase`, and because `git pull` is a combination of `fetch` and `merge`, you can resolve conflicts the same way. You can use `git pull --rebase` to rebase instead of merging after the fetch; it's particularly useful for keeping a branch up to date if you want to continue working on it after your colleagues have pushed changes to `master`.

In the next unit, you will learn how to use git to deploy a website using a hook script, and how to use branches and tags to manage software releases.