# Install and Configure Git

If you haven't already done so, it's time to install Git on the computer on which you
intend to work. Git is available for Windows, MacOs, and Linux.

If Git is already installed, skip ahead to the next section, which is about
configuring the VCS, or, if git is already configured with your user name and email ID,
jump to the next unit.

You can tell whether Git is installed and properly configured with the
command:

```
$ git config --get user.name
```

If it doesn't print your name, skip to the next section:  Git is installed but
not configured.  If it prints `Command git not found`, read on!

## Install Git 

Unless you're curious -- or use more than one operating system -- you can just
read the subsection for the computer you're sitting in front of. We start
with Windows because it's the most common and the most complicated.

### Install Git on Windows

You can download the most recent official version of Git for Windows from
[http://git-scm.com/download/win](http://git-scm.com/download/win); the
download starts automatically. Git for Windows is a separate project from
Git; you can get more information from
[https://git-for-windows.github.io/](https://git-for-windows.github.io/). If
you have a preferred text editor, such as Atom or Emacs, you should set it as
the default while installing. If you don't have one yet, select `nano` to
start with; the default is `vim`, which although extremely powerful is not at
all beginner-friendly.

> Hint: If you get into Vim accidentally, typing `:q!` gets you out.

You can also get the git command-line tools by installing GitHub Desktop,
which you can get from
[https://desktop.github.com/](https://desktop.github.com/). 

Both Git for Windows and GitHub Desktop include a terminal window with the
Bash shell (command-line processor), the Vim and Nano text editors, and most
of the standard Linux command-line utilities.


### Install Git on MacOS

Git is included with the Xcode command line tools. If you use MacOS 10.9 and above, simply try to run Git from the command line; if it's not already installed, the operating system prompts you to do so:

```
$ git --version
```

The most recent version of Git for MacOS is also available for download from
[https://git-scm.com/download/mac](https://git-scm.com/download/mac).


### Install Git on Linux

All of the major Linux distributions have Git in their package archives,
which makes installation simple. On Ubuntu and other Debian-based
distributions, the most common case, use `apt`:

```bash
$ sudo apt install git-all
```

If you're impatient or on a computer with limited disk space, you can install
just the packages you need for this tutorial (and add `git.el` if you're using
Emacs as your text editor):

```bash
$ sudo apt install git git-doc gitk git-gui curl
```

On Fedora and other RPM-based distributions, use `dnf`:

```bash
$ sudo dnf install git-all curl
```

The Git website includes [installation instructions for other Linux
and Unix distributions](https://git-scm.com/download/linux).


## Configure Git

Great. Git is installed. Now let's set it up so you can get to work with it.

You query, set, replace, or delete configuration variables with the 
`git config` command. The default is to query or modify the "local"
configuration file, located in the current git repository (`.git/config`). In
addition, there is a "global" configuration in your home directory. Depending on operating system, a "system" configuration file that applies to all users may also be found in that home directory. Use
`git help config` to see where the system and global files are on your system,
as well as the complete lists of options and configuration variables.

To start with, the only global configuration variables you absolutely need to set are
your name and email address, both of which are needed for commits. (Git tries to guess these based on your username and your computer's name and DNS domain, but then it complains every time you make a commit.
Rightly so, because its guess is almost always wrong. You may as well set it straight once and for all.)

You set these values with:

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com
```

If you're using Windows, you have a little more work to do. Windows
uses the character combination "CR,LF" (Carriage Return, Line Feed) to end
lines in text files, but Unix-based operating systems (Linux and MacOS) use
just "LF". Git uses the Unix convention by default, so if you collaborate
with people who use a different operating system, you need to tell Git to
convert line endings.

```
$ git config --global core.autocrlf true
$ git config --global core.safecrlf true
```

There's a good discussion of this problem in "[Mind the End of Your Line](https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/)" by [Tim Clem](https://adaptivepatchwork.com/about/). There are some additional subtleties that Windows users may need to watch out for later, but the defaults are all you need for this tutorial. 

## Check your configuration

At this point, you can use the following command to list all of Git's global
configuration variables. The `--show-origin` option shows in which file each is defined.

```bash
$ git config --show-origin --list
```

The values you just set will be in your home directory (under `/home` on Linux,
`/Users` on MacOS, or `C:\Users` on Windows). MacOS and Windows users also probably
have some system variables defined.

## Summary

In this unit you installed and configured Git, and learned about

 * `[`git config`](https://git-scm.com/docs/git-config)`, which gets, sets,
   replaces, or deletes configuration variables.

You've also seen brief mentions of

 * [`vim`](https://linux.die.net/man/1/vim), an advanced text editor favored
   by many Unix and Linux developers, with a well-deserved reputation for
   user-unfriendliness
 * [`nano`](https://linux.die.net/man/1/nano), a basic but very easy-to-use text editor, and
 * [`sudo`](https://linux.die.net/man/1/sudo), a Unix command that lets you
   run a single command as the system administrator (`root`) without having to
   log in as root.

> (It may look a little odd not to start each bullet point with a capital
> letter, but Git and the Bash shell have built-in commands that are
> case-sensitive, even on Windows and MacOS.)

In the next unit, you learn how to set up a project so that you can use
Git to track changes.
