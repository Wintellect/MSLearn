# Resolve merge conflicts

Sometimes, no matter how well you plan, things go wrong. Imagine that two developers are working on the same file at the same time and change the same line. When they push their changes, the second one will experience a *merge conflict*. Deveolopers using version control dread few things more than merge conflicts. But conflicts happen, and you best — no, *must* — know how to deal with them.

The good news is that Git provides solutions for dealing with merge conflicts. In this unit, you will learn about two of them. 

## Make a change as Alice

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

1. Now commit the changes, switch back to "master," do a pull to make sure nothing has changed, merge the "add-cat" branch into "master," and push:

	```bash
	git commit -a -m "Add picture of Alice's cat"
	git checkout master
	git pull
	git merge --ff-only add-cat
	git push
	```

Finish up by confirming that the push succeeded.

## Make a change as Bob

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

1. Now commit the change, switch back to "master," merge the "style-cat" branch into "master," and push:

	```bash
	git commit -a -m "Style Bob's cat"
	git checkout master
	git pull
	```

	And there it is: the dreaded merge conflict. The same line in the same file was changed by two people. Git sees that and reports "Updates were rejected because the remote contains work that you do not have locally." Git has no way of knowing whether the `src` attribute in the `<img>` element should reference **bobcat2-317x240.jpg** or **bombay-cat-180x240.jpg**:

	```
	remote: Counting objects: 3, done.
	remote: Compressing objects: 100% (3/3), done.
	remote: Total 3 (delta 2), reused 0 (delta 0)
	Unpacking objects: 100% (3/3), done.
	From D:/Labs/Git/Bob/../Shared
	   e02d9e3..0398d54  master     -> origin/master
	Auto-merging index.html
	CONFLICT (content): Merge conflict in index.html
	Automatic merge failed; fix conflicts and then commit the result.
	```

	If Bob tried to do a push right now, that would fail, too:

	```
	 ! [rejected]        master -> master (fetch first)
	error: failed to push some refs to 'D:/Labs/Git/Bob/../Shared.git'
	hint: Updates were rejected because the remote contains work that you do
	hint: not have locally. This is usually caused by another repository pushing
	hint: to the same ref. You may want to first integrate the remote changes
	hint: (e.g., 'git pull ...') before pushing again.
	hint: See the 'Note about fast-forwards' in 'git push --help' for details.
	```

The question now is: What's Bob to do?

## Resolve the merge conflict

Bob has a few options at this point. One is to use `git merge --abort` to restore "master" to what it was before the attempted merge. Bob could then create a new branch, make his changes, merge the branch into "master," and push his changes. Bob could also use `git reset --hard` to get back to where he was.

The preferred option in many cases is to resolve the conflict using information Git inserted into the affected files. When Git detects a conflict in a file, it inserts *both* conflicting versions into the file between lines starting with `<<<<<<<`, `=======`, and `>>>>>>>`.  The part before the `=======` line is "your" side of the merge — the branch you were already on — and the part after is "their" side -- the branch you specified in the `merge` command.

In this case, **index.html** in Bob's repo looks like this:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>Our Furry Friends</title>
    <link rel="stylesheet" href="assets/site.css">
  </head>
  <body>
    <nav><a href="./index.html">home</a></nav>
    <h1>Our Furry Friends</h1>
<<<<<<< HEAD
    <img class="cat" src="assets/bobcat2-317x240.jpg">
=======
    <img class="cat" src="assets/bombay-cat-180x240.jpg">
>>>>>>> 0398d54e51b77cc11d968e93cdf942acc698b75d
    <footer><hr>Copyright (c) 2019 Contoso Cats</footer>
  </body>
</html>
```

Knowing this, let's resolve the merge by editing **index.html**. Because this is a quick fix, you will make the change directly in the "master" branch.

1. Open **index.html**, delete these three lines, and then save the file:

	```html
	<<<<<<< HEAD
	=======
	>>>>>>> 0398d54e51b77cc11d968e93cdf942acc698b75d
	```

	**index.html** now has two `<img>` elements: one for Bob's cat and one for Alice's.

	As an aside, some text editors feature Git integration and offer to help when they see text representing merge conflicts. For example, if you open **index.html** in [Visual Studio Code](https://code.visualstudio.com/), you'll see this:

	![Resolving merge conflicts in Visual Studio Code](media/resolve-conflict.png)

	_Resolving merge conflicts in Visual Studio Code_

1. Now commit the change:

	```bash
	git add index.html
	git commit -a -m "Style Bob's cat"
	```

	The `git add` command tells Git that the conflict in **index.html** has been resolved.

1. Push the changes to "master" on the remote:

	```bash
	git push
	```

This time it should work, unless "master" on the remote changed again while Bob was working.

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

## Summary

In this unit you learned how to deal with merge conflicts, using the `--continue` and `--abort` options with `git merge`, and either a text editor or a merge tool. You can also use those options with `git rebase`, and because `git pull` is a combination of `fetch` and `merge`, you can resolve conflicts the same way. You can use `git pull --rebase` to rebase instead of merging after the fetch; it's particularly useful for keeping a branch up to date if you want to continue working on it after your colleagues have pushed changes to `master`.

In the next unit, you will learn how to use git to deploy a website using a hook script, and how to use branches and tags to manage software releases.