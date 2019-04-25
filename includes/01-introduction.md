# Introduction to Version Control and Git

Imagine that you want to set up a website where you and your friends can show
off pictures of your cats.  You start out working by yourself, but you're
hoping that some of your friends will join in the fun.  You need to make it
easy to collaborate, keep track of changes (and who makes them), make sure
that nothing bad happens if two people want to change the same page, and keep
it backed up in case the server goes down. You need a version-control system,
and the obvious choice is Git, a fast, versatile, highly-scalable, and very
popular distributed version-control system.

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

  * **Working Tree:** the set of nested directories and files that contains the
	version being worked on.
  * **Repository (repo):** the directory, called `.git` and located at the top
	level of a working tree, where git keeps all of the history and metadata
	for a project.  "Repository" is almost always shortened to **repo**.
  * A **bare repository** is a repository that is not part of a working tree,
	used for sharing or backup.  A bare repo is usually a directory with a
	name ending in `.git`, e.g., `project.git`.
  * **Object (blob, tree, commit, tag):** A Git repo contains four types of
	"objects", each of which is uniquely identified by a SHA-1 hash. 
      * A **blob** object contains an ordinary file.
      * A **tree** object represents a directory; it contains the names, hashes,
		and permission bits of all of its contents.
      * A **commit** object represents a version of the working tree.  It
		contains the commit message, the name and email address of the person
		who made it, the date, and the hashes of the current tree and the
		previous commit (called the **parent**).  A commit may also be signed.
      * A **tag** is a name attached to a commit.  Tags come in two types: a
		lightweight tag is just named reference to a commit; an _annotated_
		tag has essentially the same information in it as a commit.
  * **Hash:** A hash is a large number that results from a process, called a
	"[hash function](https://en.wikipedia.org/wiki/Hash_function)", that
	reduces a file or other object down to a fixed number of bits.  Git
	identifies files and other objects by computing their SHA-1 hash, which is
	160 bits long and has the additional property that the hashes of two files
	that differ in a single bit will be almost completely different.
  * **Commit(v.):** "commit" used as a verb means to make a commit object; this
	takes its name from the corresponding database operation.
  * **Branch:** a named series of linked commits.  The most recent commit on a
	branch is called its **head**.  The default branch, which is created when
	you initialize a repository, is called `master`.  The head of the current
	branch is called `HEAD`.
  * **Remote:** a named pointer to another git repository.  When you clone a
	repo, a remote called `origin` is created that is the default remote for
	push and pull operations.
  * **Command or Subcommand:** all of Git's operations are performed by a
	command line starting with `git` -- the name of the program -- followed by
	the name of the operation.  That name is properly called a "subcommand",
	but "command" is often used for either the subcommand or the Git command
	that contains it.

## About the Examples

This tutorial assumes that you are using the Bash command-line shell; it is
the default on MacOS and Linux, and installed automatically by Git for
Windows.  If you are used to Windows, there are a couple of peculiarities due
to Git's origin on Linux:

  * Commands, options, and so on are case-sensitive.
  * Command options are preceded by hyphens (`-`); in Git and most other Unix
	utilities most options have both a short form (a single character) and a
	long form (a word preceeded by `--`).
  * Paths use forward slashes (`/`) to separate components.  The backslash
	(`\`) is an "escape" character for use in strings, and has the same
	meaning that it does in C.  Absolute paths start with a slash, so expect
	to see them start with `/c/` rather than `C:`.
  * Command options start with `-`.  A single hyphen marks a one-character
	option; in some cases you can combine several options behind a single
	hyphen (for example, `ls -la`, which gives a long listing of all files in
	a directory, including the "hidden" ones that start with a period.
  * Options that start with `--` are full words; many have one-character
	equivalents, but not all of them.  Two hyphens by themselves (`--`) are
	sometimes used to separate different kinds of command-line arguments, for
	example, branch names and filenames in `git checkout`.
	
Commands in the examples are preceeded by a dollar sign and a space (`$ `),
which is the default prompt in Bash, and _not_ part of the command.  It should
not be typed.  Commands are followed by their output, if any.  For example, if
you accidentally copy and paste the prompt character, you get:

```
$ $ git
$: command not found
```

Bash treats almost any combination of characters at the start of a line as the
name of a program to run; Unix is very permissive about file names.

In real life we create and edit text files with a text editor; in our examples
we try to accomplish the same changes with Unix commands such as `echo`,
`mkdir`, and `sed`.  Unix commands and Git subcommands are listed at the end
of each unit that uses them.

