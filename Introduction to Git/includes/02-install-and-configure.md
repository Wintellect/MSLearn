# Install and Configure Git

## Install Git 

If you haven't already done so, it's time to install Git on the computer you
intend to work on.  Git is available for Windows, MacOs, and Linux.


### Install Git on Windows

The most recent official version of Git can be downloaded and installed from
[http://git-scm.com/download/win](http://git-scm.com/download/win) -- the
download starts automatically.  This is actually a separate project, called
Git for Windows -- you can get more information from
[https://git-for-windows.github.io/](https://git-for-windows.github.io/).  If
you have a preferred text editor, such as Atom or Emacs, you should set it as
the default while installing.  If you don't have one yet, select `nano` to
start with; the default is `vim`, which although extremely powerful is not at
all beginner-friendly.

> Hint:  if you get into Vim accidentally, typing `:q!` will get you out.

You can also get the git command-line tools by installing GitHub Desktop,
which you can get from
[https://desktop.github.com/](https://desktop.github.com/). 

Both Git for Windows and GitHub Desktop include a terminal window with the
Bash shell (command-line processor), the Vim and Nano text editors, and most
of the standard Linux command-line utilities.


### Install Git on MacOS

Git is included with the Xcode command line tools.  On 10.9 and above you
can simply try to run Git from the command line; if it's not already there you
will be prompted to install it:

```
$ git --version
```

The most recent version of Git for MacOS is also available for download from
[https://git-scm.com/download/mac](https://git-scm.com/download/mac).


### Install Git on Linux

All of the major Linux distributions have Git in their package archives,
which makes installation simple.  On Ubuntu and other Debian-based
distributions, the most common case, use `apt`:

```bash
sudo apt install git-all
```

If you're impatient or on a computer with limited disk space, you can install
just the packages you'll need for this tutorial (add `git.el` if you're using
Emacs as your text editor):

```bash
sudo apt install git git-doc gitk git-gui
```

On Fedora and other RPM-based distributions, use `dnf`:

```bash
sudo dnf install git-all
```

The Git website includes [installation instructions for other Linux
and Unix distributions](https://git-scm.com/download/linux).


## Configure Git

You query, set, replace, or delete configuration variables with the `git
config` command.  The default is to query or modify the "local" configuration
file, located in the current git repository (`.git/config`).  In addition there
is a "global" configuration in your home directory, and there may be a
"system" configuration file that applies to all users.  You can use 
`git help config` to see where the system and global files are on your system,
as well as the complete lists of options and configuration variables.

To start with, the only global configuration variables you need to set are
your name and email address, both of which are needed for commits.  (Git will
try to guess these based on your username and your computer's name and DNS
domain, but it will complain about it every time you make a commit.
Rightly so, because its guess will almost always be wrong.)  You set these
with:

```bash
git config --global user.name "Your Name"
git config --global user.email you@example.com
```

TODO: Windows/Mac config -- will require looking to see the default config.
TODO: Results of commands

At this point, you can use the following command to list all of Git's global
configuration variables.  The `--show-origin` option shows which file they are
defined in.

```bash
git config --show-origin --list
```

