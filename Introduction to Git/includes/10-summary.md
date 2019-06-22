# Summary

In this module, you learned the basics of using Git. Among the skills you learned were:
* installing Git
* creating, cloning, and exploring repositories
* tracking changes
* recovering from mistakes 
* collaborating with other developers
* creating, merging, and rebasing branches
* resolving merge conflicts, and some of the uses of hooks and tags

You also learned the basics of Git's terminology, how to read Git's documentation from the command line, and a few other useful commands. At this point you know enough about Git to perform everyday tasks, get yourself out of trouble if things get confusing, and understand the documentation.

## Digging deeper

There are many other good tutorials about Git. These include:

- On the command line, `git help tutorial` and `git help tutorial-2`
- [Everyday Git](https://git-scm.com/docs/everyday) (also available from the command line, as `git help everyday`)
- [Learn Enough Git to Be  Dangerous](https://www.learnenough.com/git-tutorial/getting_started)
- GitHub's [Git and GitHub learning resources](https://help.github.com/en/articles/git-and-github-learning-resources)
- [A Hacker's Guide to Git](https://wildlyinaccurate.com/a-hackers-guide-to-git/)

You can also learn more Git from the documentation section of [Git's official website, at git-scm.com/doc](https://git-scm.com/doc).

## Image credits

All of the cat pictures came from [commons.wikimedia.org](https://commons.wikimedia.org/). Here are the links and attributions:

- [Close up of a black domestic cat.jpg - Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Close_up_of_a_black_domestic_cat.jpg) (Dogbert420 [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en))
- [Bobcat2.jpg - Wikipedia](https://en.wikipedia.org/wiki/File:Bobcat2.jpg) (Calibas [public domain](https://en.wikipedia.org/wiki/en:public_domain))

## Check your knowledge

1. The command used to create a branch and switch to it in one step is:
	- `git branch BRANCH_NAME`
	- `git branch --switch BRANCH_NAME`
	- `git checkout -b BRANCH_NAME`
	- `git branch --checkout BRANCH_NAME`

1. A bare repository is one that:
	- Does not have a working tree
	- Is not reachable using a URL
	- Has had no commits
	- Has no branches

1. Which of the following commands clones a remote repository located at PATH_OR_URL?
	- `git add PATH_OR_URL`
	- `git copy PATH_OR_URL`
	- `git merge PATH_OR_URL`
	- `git clone PATH_OR_URL`

1. What is the purpose of a pull request?
	- To pull changes from a remote repo to a local repo
	- To sync a local repo with someone else's local repo
	- To give others a chance to review your changes before merging
	- To notify others that "master" has been updated

1. Following a pull, which of the following commands allows Alice to see the changes Bob made to **index.html**?
	- `git diff origin --index.html`
	- `git diff origin -- index.html`
	- `git diff --index.html`
	- `git origin -- index.html`