# Introduction

Imagine that you have started a new job as a software developer at a firm that writes avionics software for commercial aircraft. Quality control is critical, and developers work in small teams using [Git](https://git-scm.com/) for version control. You have experience with other version-control systems, but to date, your experience with Git is minimal. To flourish in your new role and add value to the team, you need to get up to speed on Git — and quickly.

So you decide to build a Web site that lets you and your friends share pictures of your cats. The project will serve as a learning platform, and you will apply the lessons learned there at work. You enlist a couple of friends who are also software developers to help out. Together, you set out to build the site using Git to aid in collaboration, keep track of changes (and who makes them), make sure nothing bad happens when two people change the same file, and keep all the source-code files backed up in case the server goes down.

In this module, you accomplish all this and more with Git. Git can seem a little cryptic at first and even be frustrating at times, but if you learn it step by step, you will find that there's a reason it is quickly becoming the world's most popular version-control system — not just for software developers, but for teams who write documentation as well. 

## What is a version-control system?

A version-control system (VCS) is a program (or set of programs) that tracks changes for a collection of files. One goal is to easily recall earlier versions of individual files or the entire project. In a VCS, you can make branches so that people can work independently, and later merge the changes you want to keep.

Another name for version-control systems is software configuration management (SCM) systems. The two terms are often used interchangeably — in fact, Git's official documentation is located at [git-scm.com](https://git-scm.com/). Technically, however, version control is just one of the practices involved in SCM, while a VCS can be used for things other than software including books, Web sites, and tutorials.

With a version-control system:

- You can see all the changes made to your project, when the changes were made, and who made them.
- Every change has a message associated with it, explaining the reason for the change.
- You can retrieve every past version of the entire project or individual files.
- You can make branches, wherein changes can be made experimentally. This allows several different sets of changes (for example, features or bug fixes) to be worked on at the same time, possibly by different people, without impacting the master branch.
- You can attach a tag to a version, for example to mark a new release.

Git is a fast, versatile, highly scalable, free, open-source version-control system. Its primary author is [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), the creator of Linux. If you're interested, you can learn how Git came about by reading [A Short History of Git](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git).

## Distributed version control

Earlier VCSs, such as [CVS](http://www.nongnu.org/cvs/), [Subversion](https://subversion.apache.org/), and [Perforce](https://www.perforce.com/), used a centralized server to contain a project's history. This means that the server is a single source of truth about the history, but it's also a single point of failure. If a developer can't connect to the server, she can't record changes or compare her version with previous ones.

Git is _distributed_, which means that every copy of a project contains its complete history. You can do all of the usual version-control operations without a network connection. The result is that developers can work independently. Although team members can designate a single copy as the definitive version, they don't have to; there are many different ways for developers to collaborate. Changes can be passed around in email, or on removable media.

In addition to allowing independent development, a distributed VCS also gives you backups for free.

## Git terminology

As with any programming endeavor, there's unique nomenclature for the tool's elements. This is a short list of terms that Git users frequently use. We explore some of these concepts in later units.

- **Working Tree:** the set of nested directories and files that contains the version being worked on.

- **Repository (repo):** the directory, called `.git` and located at the top level of a working tree, where Git keeps all of the history and metadata for a project. "Repository" is almost always shortened to **repo**.

- A **bare repository** is a repository that is not part of a working tree; it is used for sharing or backup. A bare repo is usually a directory with a 	name ending in `.git`, e.g., `project.git`.

- **Object (blob, tree, commit, tag):** A Git repo contains four types of "objects," each of which is uniquely identified by an SHA-1 hash. A **blob** object contains an ordinary file. A **tree** object represents a directory; it contains the names, hashes, and permission bits of all of its contents. A **commit** object represents a version of the working tree. It contains the commit message, the name and email address of the person who made it, the date, and the hashes of the current tree and the previous commit (called the **parent**). A commit may also be signed. A **tag** is a name attached to a commit. Tags come in two types: a _lightweight_ tag is a named reference to a commit; an _annotated_ tag has essentially the same information in it as a commit.

- **Hash:** A hash is a large number that results from a process, called a [hash function](https://en.wikipedia.org/wiki/Hash_function), that reduces a file or other object to a fixed number of bits. Git identifies files and other objects by computing their SHA-1 hash, which is 160 bits long. It has the additional property that the hashes of two files that differ in a single bit are almost completely different.

- **Commit (verb):** When used as a verb, "commit" means to make a commit object; this takes its name from the corresponding database operation.

- **Branch:** a named series of linked commits. The most recent commit on a branch is called its **head**. The default branch, which is created when you initialize a repository, is called `master`. The head of the current branch is called `HEAD`.

- **Remote:** a named pointer to another Git repository. When you clone a repo, Git creates a remote called `origin` that is the default remote for push and pull operations.

- **Command** or **Subcommand:** All of Git's operations are performed by a command line starting with `git` -- the name of the program -- followed by the name of the operation. That name is properly called a _subcommand_, but _command_ is often used for either the subcommand or the Git command

- **Workflow:** a task or (more often) sequence of tasks, typically involving both human interactions and software automation. One goal in designing workflows is to automate processes as much as possible.

## About the examples

There are several different GUIs for Git. Examples include [GitKraken](https://www.gitkraken.com/) (which is cross-platform), [TortoiseGit](https://tortoisegit.org/) (Windows), and [git gui](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-gui.html) (Linux). Most text editors and IDEs also have an interface to Git. Unfortunately, they all work differently and have different limitations. None of them implement _all_ of Git's functionality.

This tutorial assumes that you are using the Bash command-line shell. Bash is the default on macOS and Linux, and is installed automatically by [Git for Windows](https://gitforwindows.org/). We use Bash for several reasons:

- Bash, and Git's command-line interface, work exactly the same no matter what operating system you're using. That's not true of the various graphical interfaces.
- You can simply copy the commands out of the examples and paste them into a terminal window. Mistyped commands are a common source of frustration.
- We can put command output under the commands, exactly as it will appear in your terminal window.  We don't need screen shots.
- We can use standard Unix commands, which you can also cut and paste, to create and modify files.
- You may occasionally need to use Git on a server (for example, a web host) where a GUI isn't available.

If you use Windows, you should be aware of a few peculiarities stemming from Git's Linux heritage:

- Commands are case-sensitive.
- Command options are preceded by hyphens (`-`). In Git and most other Unix utilities most options have both a short form (a single character) and a long form (a word preceded by `--`).
- Paths use forward slashes (`/`) to separate components.  The backslash (`\`) is an "escape" character for use in strings, and has the same meaning that it does in C.  Absolute paths start with a slash, so expect to see them start with `/c/` rather than `C:`.
- Command options start with `-`. A single hyphen marks a one-character option; in some cases you can combine several options behind a single hyphen (for example, `ls -la`, which gives a long listing of all files in a directory, including the "hidden" ones that start with a period.
- Options that start with `--` are full words; many have one-character equivalents, but not all of them do. Two hyphens by themselves (`--`) are sometimes used to separate different kinds of command-line arguments, such as branch names and file names in `git checkout`.

Commands in the examples are preceded by a dollar sign and a space (`$ `), which is the default prompt in Bash, and _not_ part of the command. The commands' output, if any, is indented. 

The `$ ` should not be typed. Commands are followed by their output, if any. For example, if you accidentally copy and paste the prompt character, you get:

```bash
$ $ git
  $: command not found
```

Bash treats almost any combination of characters at the start of a line as the name of a program to run; Unix is very permissive about file names.

In real life, we create and edit text files with a text editor; in our examples we try to accomplish the same changes with Unix commands such as `echo`, `mkdir`, and `sed`. Unix commands and Git subcommands are listed at the end of each unit that uses them.
