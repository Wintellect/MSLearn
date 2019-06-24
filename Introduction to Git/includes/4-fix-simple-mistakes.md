# Fix simple mistakes

Sometimes things go wrong. You might forget to add a new file, or add one by mistake. Perhaps you made a spelling error in your latest commit, or you committed something you didn't intend to. Perhaps you accidentally _deleted_ a file.

Git lets you make changes fearlessly, because it *always* offer a way to get back to where you were. You can even change Git's commit history as long as you only change commits that haven't been shared.

## Amend a commit

In the previous exercise, you modified the path to the style sheet in **index.html**. Suppose you discover that you made an error. Rather than type this:

```html
<link rel="stylesheet" href="assets/site.css">
```

You typed this:

```html
<link rel="stylesheet" href="assest/site.css">
```

When you refresh the page in your browser, you notice that your CSS style sheet isn't applied. After investigating, you see why.

So you update **index.html** with the correct path to the style sheet. At this point, you could simply commit the corrected version of **index.html**, but instead, you prefer to put it in the same commit as the original. The `--amend` option to `git commit` lets you change history (and how often does one get the chance to change history?):

```bash
git commit --amend --no-edit
```

The `--no-edit` option tells Git to make the change without changing the commit message. You can also use `--amend` to edit a commit message, to add files accidentally left out of the commit, or to remove files that were added by mistake.

The ability to change history is one of Git's most powerful features. As with most power tools, it has to be used carefully. In particular, it's a bad idea to change any commits that have been shared with another developer or were published in a shared repository such as GitHub.

## Recover a deleted file

Imagine you made a change to a source-code file that broke the entire project, so you want to revert to the previous version of that file. Or perhaps you accidentally deleted a file altogether. Git makes it easy to retrieve an earlier version, even if the current version no longer exists. Your best friend in this situation is the [`git checkout`](https://git-scm.com/docs/git-checkout) command.

1. To demonstrate, delete **index.html**:

	```bash
	rm index.html
	```

	This may seem like a bad idea, but remember: Git has your back.

1. Use an `ls` command to verify that **index.html** was deleted. Then follow it up with this command:

	```bash
	git checkout -- index.html
	```

1. Use `ls` again to check the contents of the current directory. Has **index.html** been restored?

	You can also check out a file from an earlier commit (typically the head of another branch), but the default is to get the file out of the index. The `--` in the argument list serves to separate the commit from the list of file paths. It's not strictly needed in this case, but if you had a branch named "index.html" (perhaps because that's the name of the file being worked on in that branch), `--` would prevent Git from getting confused.

	> Later, you will learn that `checkout` is also used for switching branches.

1. When it comes to recovering deleted files, things get a little more complicated if you delete them with [`git rm`](https://git-scm.com/docs/git-rm) rather than `rm`. To see for yourself, try this command:

	```bash
	git rm index.html
	```

1. Once more, **index.html** is gone. Try to recover it the same way you did last time:

	```bash
	git checkout -- index.html
	```

	This time, Git complains that it knows nothing about **index.html**. That's because Git not only deleted the file, it recorded the deletion in the index.

1. You can recover **index.html** with two commands:

	```bash
	git reset HEAD index.html
	git checkout -- index.html
	```

	`git reset` unstaged the change, but the file was still deleted, so you had to use `checkout` to get it back.

Here's another "Aha!" moment for new Git users. Many version-control systems make files read-only to ensure that only one person at a time can make changes; they use a completely unrelated `checkout` command to get a writable version. They also use `checkin` for an operation similar to what Git does with a combination of `add`, `commit`, and `push`. This occasionally causes confusion when people start using Git.

## Revert a commit

Now let's make things more complicated still. Suppose you accidentally overwrite one file with another, or make a change to a file that turns out to be a big mistake. You want to revert to the previous version of the file, but you had already committed the changes. This means that a simple `git checkout` won't do the trick.

One solution to this problem is to revert the previous commit.

1. Use your favorite text editor to replace the contents of **index.html** with this:

	```html
	<h1>That was a mistake!</h1>
	```

1. Now save the file, commit the changes, and show the latest commit:

	```bash
	git commit -m "Purposely overwrite the contents of index.html" index.html
	git log -n1
	```

1. Use the following commands to "restore" **index.html** and list its contents:

	```bash
	git checkout -- index.html
	cat index.html
	``` 

	Which version of **index.html** do you see? The old or the new?

1. In this situation, the best course of action is to _revert_ the change by making another commit that cancels out the first one. That's a job for [`git revert`](https://git-scm.com/docs/git-revert):

	```bash
	git revert --no-edit HEAD
	```

1. Follow up with a `git log` command to show the latest commit:

	```bash
	git log -n1
	```

1. Now use these commands to restore **index.html** and verify that the old version was indeed restored:

	```bash
	git checkout -- index.html
	cat index.html
	``` 

Reverting isn't the only way to remedy this situation; you could simply edit **index.html** and commit the corrected file. That's harder if the changes you committed were extensive, and in any case, `git revert` is a good way to signal your intent.

As an aside, you can also remove the most recent commit with:

```
git reset --hard HEAD^
```

There are several types of resets. The default is `--mixed`, which resets the index but not the working tree; it also moves HEAD if you specify a different commit. The `--soft` option only moves HEAD, and leaves both the index and the working tree unchanged. This leaves all your changes as "changes to be committed", as `git status` would put it. A `--hard` reset changes both the index and the working tree to match the specified commit; any changes you made to tracked files are simply discarded.

## Summary

In this unit, you learned several new Git commands:

- [`git checkout`](https://git-scm.com/docs/git-checkout), which retrieves previous versions
- [`git reset`](https://git-scm.com/docs/git-reset), which sets the working tree and index back to an earlier state
- [`git revert`](https://git-scm.com/docs/git-revert), which undoes the effect of a commit without affecting history
- [`git commit --amend`](https://git-scm.com/docs/git-commit), which changes the most recent commit

In the next unit, you start collaborating with another developer. Because Git is distributed, you won't have to set up a server; you can share changes directly.