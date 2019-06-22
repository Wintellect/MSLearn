# Summary

In this module, you learned the basics of using Git. You learned how to install Git, how to create and clone repositories, how to track changes, how to collaborate with other team members using a shared repository, how to use branches to isolate your changes, how to merge branches, and more. You even learned one technique for recovering from merge conflicts — something that sooner or later, you will have to do.

At this point, you know enough about Git to perform everyday tasks, get yourself out of trouble if something goes awry, and understand the documentation. If you would like to dig deeper, here are some resources that you'll find helpful:

- On the command line, `git help tutorial` and `git help tutorial-2`
- [Everyday Git](https://git-scm.com/docs/everyday) (also available from the command line, as `git help everyday`)
- [Learn Enough Git to Be  Dangerous](https://www.learnenough.com/git-tutorial/getting_started)
- GitHub's [Git and GitHub learning resources](https://help.github.com/en/articles/git-and-github-learning-resources)
- [A Hacker's Guide to Git](https://wildlyinaccurate.com/a-hackers-guide-to-git/)

You can also learn more from the [documentation section](https://git-scm.com/doc) of [Git's official website](https://git-scm.com).

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
	- To merge changes made in a local branch into the local "master" branch
	- To give others a chance to review your changes before merging
	- To notify others that "master" has been updated

1. Following a pull, which of the following commands allows Alice to see the changes Bob made to **index.html**?
	- `git diff origin --index.html`
	- `git diff origin -- index.html`
	- `git diff --index.html`
	- `git origin -- index.html`