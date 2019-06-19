# Fix simple mistakes

Sometimes things go wrong. You might forget to add a new file, or add one by mistake. Perhaps you made a spelling error in your latest commit, or you committed something you didn't intend to. Perhaps you accidentally _deleted_ a file. You can even change Git's commit history as long as you only change commits that haven't been shared.

Git lets you make changes fearlessly, because it *always* offer a way to get back to where you were.

## Amend a commit

In the previous exercise, you modified the path to the style sheet in **index.html**. Suppose you discover that you made an error and rather than typing this:

```html
<link rel="stylesheet" href="assets/site.css">
```

You typed this:

```html
<link rel="stylesheet" href="assest/site.css">
```

When you refresh the page in your browser, you notice that your CSS style sheet isn't applied. After investigating, you see why.

So you update **index.html** with the correct path to the style sheet. At this point, you could simply commit the changed version of **index.html**, but instead, you prefer to put it in the same commit as the original. The `--amend` option to `git commit` lets you change history (and how often does one get the chance to change history?):

```bash
git commit --amend --no-edit
```

The `--no-edit` option tells Git to make the change without changing the commit message. You can also use `--amend` to edit a commit message, to add files accidentally left out of the commit, or to remove files that were added by mistake.

The ability to change history is one of Git's most powerful features. (You will learn later that there are other ways to accomplish this besides `--amend`.) As with most power tools, it has to be used carefully. In particular, it's a bad idea to change any commits that have been shared with another developer or were published in a shared repository such as GitHub.

## Retrieve an earlier version of a file

One thing that Git makes easy is retrieving an earlier version of a file. Perhaps you deleted more than you intended with a wildcard, or you damaged a file experimenting with `sed`, or you simply have made a series of changes that you
later regret.

Your friend in this situation is `git checkout`. For example,

```
$ rm index.html .bak
$ ls
assets	index.html.bak
```

This is a classic problem. You meant to delete the backup file, but your cat stepped on the keyboard and put in a space before the dot. If you notice the problem soon enough, it's particularly easy to fix:

```
$ git checkout -- index.html
$ ls
assets
index.html
index.html.bak
$ git status
On branch master
nothing to commit, working tree clean
```

(It is more difficult to fix the cat.)

You can also check out a file from another commit (typically the head of another branch), but the default is to get the file out of the index. The `--` in the argument list serves to separate the commit from the list of file paths. It's not strictly needed in this case, but if you had a branch called `index.html` (perhaps because that's the name of the file being worked on on that branch), the `--` would keep Git from getting confused.

In Unit 8 you'll learn that `checkout` is also used for switching branches.

This is another "Aha!" moment for some git users. Many earlier version-control systems make files read-only to ensure that only one person at a time can make changes; they use a completely unrelated "checkout" command to get a writable version. They also use "checkin" for an operation similar to what Git does with a combination of `add`, `commit`, and `push`. This occasionally causes confusion when people start using Git.

Things are a little more complicated if you used `git rm`:

```
error: pathspec 'index.html' did not match any file(s) known to git.
$ git rm index.html
rm 'index.html'
$ git checkout index.html
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	deleted:    index.html

$ git reset HEAD index.html
Unstaged changes after reset:
D	index.html
$ ls
assets
index.html.bak
$ git checkout index.html
$ ls
assets
index.html
index.html.bak
```

The `git reset` was needed because `git rm` did two things: It removed the file, and it recorded the deletion in the index. The `reset` unstaged the change, but the file was still deleted, so you had to use `checkout` to get it back.

## Revert a commit

As you work on the Web site design, you decide to make the background a little darker:

```
$ echo body '{ background-color:  #C0C0C0; }' > assets/site.css
$ git commit -a -m "Make the page background a little darker"
[master 6909e17] Make the page background a little darker
 1 file changed, 1 insertion(+), 2 deletions(-)
```

Oops! You meant to append to `site.css`, but used `>` instead of `>>`, which replaced the entire file. You already know how to fix this by amending the commit: Use `git checkout` to get the previous version of `site.css` back, make the change correctly, and `git commit --amend`. Or you could use `git reset --hard` to put everything back the way it was, and re-do both the change and the commit.

But suppose you didn't notice the problem until you'd already made another commit after the bad one, shared your repo with somebody (see the next unit), or made the commit public (see Unit 7). Changing history can be dangerous (see almost any dystopian science fiction story about time travel). Anyone with whom you collaborate has to do extra work to recover from your change.

In this situation the best thing to do is to _revert_ the change, by making another commit that cancels out the first one:

```
$ git revert --no-edit HEAD 
[master d31233f] Revert "Make the page background a little darker"
 Date: Wed May 15 12:23:32 2019 -0700
 1 file changed, 2 insertions(+), 1 deletion(-)
$ git log -n1
commit d31233fbe10ffe01eced101eb53214a7eccc96f4
Author: Steve Savitzky <steve@savitzky.net>
Date:   Wed May 15 12:23:32 2019 -0700

    Revert "Make the page background a little darker"
    
    This reverts commit 6909e17a67f6063d616f3863b3c04854fa4f5a9e.
```

Now you can make the change correctly.

```
$ echo body '{ background-color:  #C0C0C0; }' >> assets/site.css 
$ cat assets/site.css
h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
body { font-family: serif; }
body { background-color:  #C0C0C0; }
$ git commit -a -m "Make the page background a little darker" -m "correctly"
[master 2c01c05] Make the page background a little darker
 1 file changed, 1 insertion(+)
```

In addition to copying text from the terminal to a file, the `cat` command can be used going the other way for getting a quick look at a short file. For longer files, use `less`, which lets you go through a file a page at a time. As you might expect, it's an improved version of an older Unix command called `more`. (And it has nothing to do with the cat putting his paws on your keyboard.)

Revert isn't the only way to fix this; you could simply have edited `site.css` and committed the changed file. That's harder if the changes you committed were extensive, and in any case the `revert` is a good way to signal your intent.

You can also remove the most recent commit with 

```
git reset --hard HEAD^
```

There are several different resets. The default is `--mixed`, which resets the index but not the working tree; it also moves HEAD if you specify a different commit. The `--soft` option only moves HEAD, and leaves both the index and the working tree unchanged.  This leaves all your changed files "changes to be committed", as `git status` would put it. A `--hard` reset changes both the index and the working tree to match the specified commit; any changes you made to tracked files are simply discarded.

### Exercises

* Use `git reflog` to see all the changes you've made to `master` and `HEAD`, including the original version of the commit you amended.
* Use `gitk --all`, which shows you a GUI view of your history, to verify that the last few commits made the changes you expect.

## Summary

In this unit, you learned about

* [`git checkout`](https://git-scm.com/docs/git-checkout), which retrieves previous versions
* [`git reset`](https://git-scm.com/docs/git-reset), which sets the working tree and index back to an earlier state,
* [`git revert`](https://git-scm.com/docs/git-revert), which undoes the effect of a commit without affecting history
* [`git reflog`](https://git-scm.com/docs/git-reflog), which shows you previous values of `HEAD` and `master`, and 
* [`git commit --amend`](https://git-scm.com/docs/git-commit), which lets you change the most recent commit.

In the next unit you start collaborating with another developer. Because Git is distributed, you won't have to set up a server; you can share changes directly.
