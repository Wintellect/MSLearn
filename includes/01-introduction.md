# Introduction to Version Control and Git

Imagine that you want to set up a website to showcase the software your team
is producing.  It will start out as a side project, with you the only person
working on it, but you know that soon you'll be looking for contributions from
some of your coworkers.  You need to make it easy to collaborate, keep track
of changes (and who makes them), make sure that nothing bad happens if two
people want to change the same page, and eventually make it public. You need a
version-control system, and the obvious choice is Git, a fast, versatile,
highly-scalable, and very popular distributed version-control system.

## What is a Version Control System?

A Version Control System (VCS) is a program (or set of programs) that
tracks changes in a collection of files so that you can easily recall
earlier versions of individual files or the entire project.  You can make
branches so that people can work independently, and later merge the changes
you want to keep.

Another name for Version Control System is Software Configuration Management
(SCM) system.  The two terms are often used interchangeably -- in fact, Git's
official documentation is located on [git-scm.com](https://git-scm.com/) --
but technically version control is just one of the practices involved in SCM,
while a VCS can be used for things other than software including books,
websites, and tutorials.

With a version-control system,

  * You can see all the changes made to your project, when they were made, and
    who made them.
  * Every change has a message associated with it explaining why it was made.
  * You can retrieve every past version of either the whole project, or any
	file in it.
  * You can make branches, where changes can be made experimentally.  This
	allows several different sets of changes (e.g. features or bug fixes) to
	be worked on at the same time, possibly by different people.
  * You can attach a tag to a version, for example to mark a new release.	

## What is a _Distributed_ VCS?

Earlier VCSs like CVS, Subversion, and Perforce, use a centralized server to
contain a project's history.  That means that the server is a single source of
truth about the history, but it's also a single point of failure:  if a
developer can't connect to the server, they can't record changes or compare
their versions with previous ones.

Git is _distributed_, which means that every copy of a project contains its
complete history.  You can do all of the usual version-control operations
without a network connection.  Developers can work independently, and although
a group can designate a single copy as the definitive version, they don't have
to; there are many different ways for developers to collaborate.  Changes can
be passed around in email, or on removable media.  In addition to allowing
independent development, a distributed VCS also gives you backups for free.

## Some Git Terminology

  * *Working Tree:* the set of nested directories and files that contains the
	version being worked on.
  * *Repository (repo):* the directory, called `.git` and located at the top level of
	a working tree, where git keeps all of the history and metadata for a
	project.  "Repository" is almost always shortened to *repo*.  
    a *Bare Repository* is a repository that is not part of a working tree, used
	for sharing or backup.  A bare repo is usually a directory with a name
	ending in `.git`, e.g., `project.git`.
  * *Object (blob, tree, commit, tag):* A Git repo contains four types of
	"objects", each of which is uniquely identified by a SHA-1 hash. 
      * a *blob* object contains an ordinary file.
      * a *tree* object represents a directory; it contains the names, hashes,
		and permission bits of all of its contents.
      * a *commit* object represents a version of the working tree.  It
		contains the commit message, the name and email address of the person
		who made it, the date, and the hashes of the current tree and the
		previous commit (called the *parent*).  A commit may also be signed.
      * a *tag* is a name attached to a commit.  Tags come in two types: a
		lightweight tag is just named reference to a commit; an _annotated_
		tag has essentially the same information in it as a commit.
  * *Commit(v.):* "commit" used as a verb means to make a commit object; this
	takes its name from the corresponding database operation.
  * *Branch:* a named series of linked commits.  The most recent commit on a
	branch is called its *head*.  The default branch, which is created when
	you initialize a repository, is called `master`.  The head of the current
	branch is called `HEAD`.
  * *Remote:* a named pointer to another git repository.  When you clone a
	repo, a remote called `origin` is created that is the default remote for
	push and pull operations.

## About the Examples

This tutorial assumes that you are using the Bash command-line shell; it is
the default on MacOS and Linux, and installed automatically by Git for
Windows.  If you are used to Windows, there are a couple of peculiarities due
to Git's origin on Linux:

  * Command options are preceded by hyphens (`-`); in Git and most other Unix
	utilities most options have both a short form (a single character) and a
	long form (a word preceeded by `--`).
  * Options are case-sensitive.
  * Paths use forward slashes (`/`) to separate components.  The backslash
	(`\`) is an "escape" character for use in strings, and has the same
	meaning that it does in C.  Absolute paths start with a slash, so expect
	to see them start with `/c/` rather than `C:`.
	
Commands in the examples are preceeded by a dollar sign and a space (`$ `),
which is the default prompt in Bash, and _not_ part of the command.  It should
not be typed.  Commands are followed by their output, if any.  For example, if
you accidentally copy and paste the prompt character, you get:

```
$ $ git
$: command not found
```

