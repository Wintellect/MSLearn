# Branch, merge, and rebase

As your project progresses, the developers want to work on more than one task at a time, fixing bugs as they turn up while implementing new features. The contributors need a way to keep their work separate so what one person is doing doesn't affect another.

_Branches_ make this easy. The work done "on a branch" doesn't have to be shared, and it doesn't interfere with other branches, including "master." Branches let you keep the commits related to each topic together and in isolation, making changes easy to review and track. Modern software development is done almost entirely in branches. The goal is to keep "master" clean until the work is ready to check in. Then you submit a pull request to merge your branch into "master."

One of Git's advantages over older version control systems is that creating a branch is extremely fast; it amounts to writing a 40-character hash into a file under ".git/heads." Switching branches is also fast, because Git stores whole files and just unzips them rather than trying to reconstruct them from lists of changes. Merging in Git isn't _quite_ that simple, but it's straightforward and often completely automatic. Let's learn what branches are, how they're used, and how they work.

## Understanding branches

A _branch_ is simply a chain of commits "branching off" from the main line of development, like a branch on a tree.

If you are switching to Git from another version-control system, you may be accustomed to slightly different terminology. Subversion, for example, actually calls its main branch "trunk". Git calls it "master." You can rename "master," just as you can rename any other branch, and some teams do this when switching to Git from other version-control systems.

A branch usually starts with a commit on "master." It grows a separate history chain as commits are added. Eventually its changes can be merged back into "master." You will learn about two different ways of doing that — merging and rebasing — in a few moments.

Suppose you branch off of "master." Here's how to visualize what happens:

```
master:  A---B---C---D
              \
branch:        E---F---G
```

Each capital letter in the diagram represents a commit. Branches are given names such as "add-authentication" and "fix-css-bug," and branches can have branches of their own. The ultimate goal is to let developers do what they need to do without stepping on each other, and to wind up with a "master" branch representing the best efforts of everyone involved.

## Create a branch for Alice

Alice wants to add some CSS to style the cat pictures, so she creates a _topic branch_ (sometimes called a _feature branch_) and calls it "add-style." Let's assume the role of Alice, create the branch, and do some work in that branch.

1. Assuming you're in the project directory, navigate to the "Alice" directory and assume the role of Alice:

	```bash
	cd ../Alice
	git config user.name Alice
	git config user.email alice@contoso.com
	``` 

1. Now use the [`git branch`](https://git-scm.com/docs/git-branch) command to create a branch named "add-style," and the [`git checkout`](https://git-scm.com/docs/git-checkout) command to switch to that branch (make it the *current branch*):

	```bash
	git branch add-style
	git checkout add-style
	```

	You have already encountered `checkout` as a way of replacing files in the working tree by getting them from the index. With no paths in the argument list, `checkout` updates *everything* in the working tree and the index to match the specified commit — in this case the head of the branch.

1. Open **site.css** in the "Alice/assets" directory and add the following CSS class definition to the bottom of the file:

	```css
	.cat { max-width: 40%; padding: 5 }
	```

	Save the changes to the file.

1. Commit the change:

	```bash
	git commit -a -m "Add style for cat pictures"
	```

1. At this point, Alice wants to make her style available to everyone else, so she switches back to "master" and does a pull in case anyone else has made changes:

	```bash
	git checkout master
	git pull
	```

	The output looks something like this:

	```

	```

1. Seeing that no work has been done on "master," Alice merges the "add-style" branch into "master" using `git merge --ff-only` to perform a "fast-forward" merge. Then she pushes "master" from her repo to the shared repo:

	```bash
	git merge --ff-only add-style
	git push
	```

Performing a fast-forward merge because "master" has no changes wasn't strictly necessary in this case, but it's a good habit to get into.

# Create a branch for Bob

While Alice is working on the CSS, Bob is sitting in an apartment on the other side of town blissfully unaware of what Alice is doing (which is OK since they're both using branches). Bob decides to make some changes of his own.

1. Start by assuming the role of Bob:

	```bash
	cd ../Bob
	git config user.name Bob
	git config user.email bob@contoso.com
	```

1. Now use the following command to create a branch named "add-cat,", using the popular `-b` option to create the branch and switch to it in a single command:

	```
	git checkout -b add-cat
	```

1. Copy **bobcat2-317x240.jpg** from [insert location here] into Bob's "assets" directory:

	```bash
	cp bobcat2-317x240.jpg assets
	```

1. Now open **index.html** and replace tk with the following statement:

	```html
	<img src="assets/bobcat2-317x240.jpg">
	```

	Save the file.

1. You have now made two changes to Bob's "add-cat" branch. You have added a file and modified an existing file. Use the following commands to add the new file in the "assets" directory to the index and commit all changes: 

	```bash
	git add assets
	git commit -a -m "Add picture of Bob's cat"
	```

1. Bob now does as Alice did: he switches back to "master" and does a pull to see if anything has changed:

	```
	git checkout master
	git pull
	```

	Here's the output:

	```

	```

1. 









Right now, the two contributors are working in parallel. At this point, their two working trees look like this:

```
Alice:  ...o---m
                \
  add-style		 A		 

Bob:    ...o---m
                \
  addCat		 B				 
```

Note that the master branch, `m` in the diagram, has no commits following it.



## Merge without fast-forward

Alice could have forced Git to create a merge commit by using the `--no-ff` option. In that case, the history would have looked like:

```
        ...o---m---M        m: previous master
                \ /         M: new merge commit
				 A          A: Add style for cat pictures
```

Merge commits are used for additional metadata in some projects. In addition to recording the date and time of the merge, and the developer's name and email, you can use the `--signoff` option to include a "signed off by:"  line. The `-S` option adds a digital signature. Merge commits like this are often used in large distributed projects; the sign-off identifies the person who approved the change, and the signature backs that up by ensuring that _only_ that person could have made the commit.

Sometimes a non-fast-forward merge can't be avoided. Let's look at Bob's situation.

```
$ cd ~/sandbox/Bob/BobCats
$ git checkout master
Switched to branch 'master'
Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
$ git pull
Updating 88bed5a..cddf95c
Fast-forward
 assets/site.css | 1 +
 1 file changed, 1 insertion(+)
```

Now Bob's history looks like:

```
Bob:    ...o---m---A      A: Add style for cat pictures
                \
                 B        B: Add picture of Bob's cat
```

If Bob uses `git merge addCat` at this point, his history will look like:

```
Bob:    ...o---m---A---M
                \     /
                 B---/
```

Some projects prefer this kind of history. It keeps Bob's commits exactly the way he made them, so if any of them were signed the signatures would still be valid after the merge. Solo developers and many teams usually prefer something simpler. Fortunately Git lets Bob change his history so that he can use a fast-forward merge.

## Rebase instead of merge

_Rebasing_ a branch rewrites all of its commits so that it attaches to a different parent (base) commit. 

In order to simplify his history, Bob wants to rebase the `addCat` branch so that it is based on "A" rather than "m".  He uses:

```
$ git checkout addCat
Switched to branch 'addCat'
$ git rebase master
First, rewinding head to replay your work on top of it...
Applying: Add picture of Bob's cat
```

Now his history looks like:

```
Bob:    ...o---m---A
                    \
                     B       addCat
```

What Git did was to compute the difference between the commits `m` and `B`, and apply that difference as a patch to `A`.

Git lost track of the fact that Bob's change was originally made to commit `m`, but that's usually less important than making sure that Bob has taken all of his teammates' changes into account.

If Bob were to merge the `addCat` branch now, he could do it as a fast-forward merge. Instead, he decides that there's no reason to merge at this point, so he simply continues to work on his branch:

```
$ sed -i.bak -e 's/<img /<img class=".cat" /' index.html
$ git commit -a -m "Add style class to cat picture"
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Now Bob's history looks like:

```
Bob:    ...o---m---A
                    \
                     B---C   addCat
```

Bob can still do a fast-forward merge, but if he does it would be impossible for anyone looking at the log to see that commits B and C were made on the same branch, implementing parts of the same feature. Instead, Bob could have amended commit B rather than making a new commit on top of it; that would lead to a simpler-looking history, with a single commit combining all of his changes. That way anyone looking at the combined commit would see all of Bob's changes in one place rather than spread out over multiple commits. Many teams prefer simple histories, but as we'll see later there are other ways of combining commits that work better.

## Summary

In this unit, you learned how to create branches and several different ways to merge them. You learned about:

- [`git branch`](https://git-scm.com/docs/git-branch), which creates a branch
- [`git checkout`](https://git-scm.com/docs/git-checkout), which switches to a branch, and [`git checkout -b`](https://git-scm.com/docs/git-checkout) which creates a branch *and* switches to it,
- [`git rebase`](https://git-scm.com/docs/git-rebase), which revises commits to re-arrange branches
- [`git merge`](https://git-scm.com/docs/git-merge), which combines branches

It's up to each project to decide whether it's more important to use rebase and fast-forward merges to keep a simple linear history, or to use merge commits to preserve signoffs, signatures, metadata, and the exact sequence of changes. Small teams generally go for simplicity.

In the next unit, you learn how to simplify history using `merge --squash` or `rebase --interactive`, and how to resolve merge conflicts.
