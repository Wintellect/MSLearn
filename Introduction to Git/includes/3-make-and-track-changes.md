# Make and track changes

Most development projects are iterative. You write some code, then test it and make sure it works. Then you write more code, and invite other people to contribute their own. Thereafter ensues a multitude of changes: code additions, bug fixes, deletions, and replacements.

As you work on your project, Git helps keep track of the changes you make. It also lets you undo mistakes. In the exercises that follow, you continue building out the Web site you're working on and learn some important new commands such as [`git diff`](https://git-scm.com/docs/git-diff). You learn also learn how Git handles subdirectories. (Would you believe that it ignores them?)

## Modify index.html

The Web site's home page, **index.html** currently contains just one line of HTML. Let's update it to do more and commit the change to Git.

1. Open **index.html** in your favorite text editor and replace its contents with the following HTML:

	```html
	<!DOCTYPE html>
	<html>
	  <head>
	    <meta charset='UTF-8'>
	    <title>Our Feline Friends</title>
	  </head>
	  <body>
	    <h1>Our Feline Friends</h1>
	    <p>Eventually we will put cat pictures here.</p>
	    <hr>
	  </body>
	</html>
	```

	Then save your changes to the file.

1. Use a [`git diff`](https://git-scm.com/docs/git-diff) command to see what changed:

	``` bash
	git diff
	``` 

	The output format is the same as that of the Unix `diff` command, and it takes many of the same options. A plus sign appears in front of lines that were added, and a minus sign indicates lines that were deleted.

	The default is for `git diff` to compare the working tree to the index. In other words, it shows you all of the changes that haven't been staged (added to the index) yet. To compare the working tree to the last commit, you can use `git diff HEAD`.

1. Next, commit the change. You can explicitly name a file to be committed, provided Git already has the file in the index (which is all that `commit` looks at).

	```bash
	git commit -m "Add HTML boilerplate to index.html" index.html
	```

1. Use `git diff` again to compare the working tree to the index. This time, `git diff` produces no output because the working tree, index, and HEAD are all in agreement.

1. Let's say you decide "furry" sounds friendlier than "feline." Replace the two occurrences of "Feline" in **index.html** with "Furry." Then save the file.

1. Depending on which text editor you use, there could now be a problem. For example, if you use [sed](https://en.wikipedia.org/wiki/Sed) as your editor, it probably created an **index.html.bak** file that you don't want to commit. Other editors such as Vim and Emacs create backup files with names such as **index.html~** and **index.html.\~1\~**, depending on how they're configured. 

	Use the following command to create a file named **.gitgnore** that instructs Git to ignore files whose names end in **.bak** or **~**:

	```bash
	echo -e "*.bak\n*~" > .gitignore
	```

	**.gitignore** is a very important file in the Git world because it prevents extraneous files from being submitted to version control. Boilerplate **.gitignore** files are available for popular programming environments such as Microsoft's [Visual Studio](https://visualstudio.microsoft.com/).

1. Now use these commands to commit the changes:

	```bash
	git add -A
	git commit -m "Make small wording change; ignore editor backups"
	```

	This example uses the `-A` option with `git add` to add all untracked (and not ignored) files as well as ones that have changed to those already under Git control.

If you do a `git diff` right now, the output will be empty because the changes have been committed. However, you can always use a `git diff HEAD^` command to compare differences between the latest commit and previous commit. (Try it and see.)

## Add a subdirectory

Most Web sites use CSS style sheets as well as HTML, and the site you're building is no exception. Style sheets are typically stored in a subdirectory, so let's create a subdirectory named "CSS" and add it to the repo.

1. Begin by creating a subdirectory named "CSS" in the project directory:

	```bash
	mkdir CSS
	```

	Then do a `git status`. Why does it report that there is nothing to commit?

1. People used to other version-control systems are often surprised to learn that Git doesn't consider adding an empty directory to be a change. That's because Git only tracks changes to *files*, not directories.

	Sometimes, especially in the initial stages of development, you *want* to have empty directories as placeholders. A common convention is to create an empty file in them. It's often called **.git-keep**. Use the following commands to create an empty file with that name in the "CSS" subdirectory and add the contents of the subdirectory to the index:

	```bash
	touch CSS/.git-keep
	git add CSS
	```

Follow up by using `git status` again to check the status of the repo. Confirm that it reports one new file.

## Replace a file

Now let's replace **.git-keep** with a CSS file and update **index.html** to reference it.

1. Delete **.git-keep** from the "CSS" subdirectory:

	```bash
	rm CSS/.git-keep
	```

1. Use your favorite text editor to create a file named **site.css** in the "CSS" subdirectory and add the following CSS to it. Then save the file.

	```css
	h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
	body { font-family: serif; }
	```

1. Now add the following line to **index.html** after the `<title>` line, and save the modified file:

	```html
	<link rel="stylesheet" href="CSS/site.css">
	```

1. Use `git status` to see a summary of the files that have changed. Then use the following commands to submit untracked files to version control and commit your changes to **site.css** and **index.html**:

	```bash
	git add .
	git commit -m "Add a simple stylesheet"
	```

Finish up by opening **index.html** in your browser and seeing how it looks right now. It's not very fancy at the moment, but it's a start.

## Rename a subdirectory

After creating the "CSS" subdirectory, you decide to rename it "assets" since it will eventually hold files other than style sheets.

1. Use the following command to rename the subdirectory:

	```bash
	git mv CSS assets
	```

1. Next, modify the `<link>` element in **index.html** to reference the renamed subdirectory:

	```html
	<link rel="stylesheet" href="assets/site.css">
	```

1. Now commit the changes:

	```bash
	git commit -m "Rename CSS -> assets for generality"
	```

	The percentage reported by `git commit` on the last line is the degree of similarity between the new and old versions of **site.css**. In this case, you _just_ moved it, so they're 100% identical. If you change a file and don't commit before you move it, the percentage is lower, but in most situations Git correctly recognizes a change-and-move. It can guess wrong if you move more than half of one file into another; in that case, it will look as though the file was moved and then a new file was created in its place.

Unlike most version control systems, Git records the contents of your files rather than the deltas between them. That's a large part of what makes committing, branching, and switching between branches so fast in Git. Other VCSes have to apply a list of changes to get between one version of a file and another. Git just unzips the other version.

## List commits

Now that you have a reasonable number of changes recorded, you can use `git log` to look at them. As with most Git commands, there are plenty of options to choose from. One of the most useful is `--oneline`.

1. Use the following command to review all of your commits:

	```bash
	git log
	```

2. Now use this command to produce a more concise listing:

	```bash
	git log --oneline
	```

You can see why once you're hundreds (or thousands) of commits into a project, the `--online` option might be your best friend. Another useful option is `-nX`, where X is a commit number: 1 for the latest commit, 2 for the one before that, and so on. To see for yourself, try a `git log -n2` command.

## Summary

In this unit, you learned two new Git commands:

- [`git diff`](https://git-scm.com/docs/git-diff), which shows the differences between versions
- [`git mv`](https://git-scm.com/docs/git-mv), which moves (renames) a file or subdirectory

You also learned more about `git log`. Next up: learn how to use Git to recover from common mistakes.