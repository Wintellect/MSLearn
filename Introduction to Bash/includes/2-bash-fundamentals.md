# Bash fundamentals

Before we get into the details of Bash commands, let's look at the way the shell interacts with the computer and the operating system. Bash is used both interactively — at the command line — and in shell scripts, which are files that contain Bash commands and whose names usually end with **.sh**. Thus, Bash bridges the gap between a simple shell language and a programming language. Mastering it is essential for day-in, day-out system-administration work.

When Bash starts, it first reads and executes commands from the file **/etc/profile**. This file — if it exists — contains the system's basic configuration data and any startup programs.

After reading this configuration file, Bash looks for **~/.bash_profile**, **~/.bash_login**, and **~/.profile** for the logged-on user configuration information. If none of these exist, Bash runs with the operating system defaults. The tilde (~) in the path names represents the user's home directory.

Once these startup chores are finished, Bash displays a prompt and awaits your command.

## Bash syntax

The full syntax for a Bash command is:

```
command [options] [arguments]
```

This syntax is very precise. Close to being right isn't good enough. If a shell argument doesn't use just the right combination of commands, options, and arguments — including spacing — it will fail. 

Usually, the Bash shell treats the first string it encounters as a command. Most of the time, that's what you intend: a command to do something. So, for example, to see what files are inside your pwd — shorthand for the current working directory — you would you invoke the Linux list command, `ls`: 

```bash
ls
```
 
As with other shell languages, Bash commands are often used with arguments. For example, creating a directory requires a directory name. So when you use `mkdir` to create a subdirectory named "orders" in the pwd, you type:

```bash
mkdir orders
```

Some Bash commands have options, which may or may not be required for a given task. Options, also called *flags*, give a command more specific instructions. To create a new subdirectory and a subdirectory inside it with one command under your pwd, you could run `mkdir` with a `--parents` flag:

```bash
mkdir --parents cats/pics
```

Many flags can be specified with an abbreviated alias. An alternate for `--parents` is `–p`, so the previous command could be entered as `mkdir -p cats/pics`.

## The `sudo` command

Some Bash commands can only be run by the root user — a system administrator or superuser. If you try one of these commands without these privileges, it fails. You can create directories in the VM you created in the previous unit because you are logged in as an admin. However, in Linux, ordinary users cannot create directories.

You don't want to run as root most of the time. It's too dangerous. So, to run commands that require admin privilege without logging in as an admin, you preface the commands with `sudo`:

```bash
sudo mkdir orders
```

`sudo` stands for "superuser do." When you use it, you're telling the shell that for this one command you are acting with the root-user level of permission.

## Getting help

Which options and arguments can be used, or must be used, varies from command to command. Fortunately, Bash documentation is built into the operating system. Help is never more than a command away. To learn about the options for a command, use the `man` (for "manual") command. For instance, to see all the options for the `mkdir` command, do this:

```bash
man mkdir
```

`man` will be your best friend as you learn Bash. `man` is how you find the information you need to understand how any command works.

Most Bash and Linux commands support the `--help` option. This shows a description of the command's syntax and options. To demonstrate, type `mkdir --help`. The output will look something like this:

```
Usage: mkdir [OPTION]... DIRECTORY...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
  -p, --parents     no error if existing, make parent directories as needed
  -v, --verbose     print a message for each created directory
  -Z                   set SELinux security context of each created directory
                         to the default type
      --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                         or SMACK security context to CTX
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Report mkdir translation bugs to <http://translationproject.org/team/>
Full documentation at: <http://www.gnu.org/software/coreutils/mkdir>
or available locally via: info '(coreutils) mkdir invocation'
```

Help obtained this way is typically more concise than help obtained with `man`. 

## Wildcards

Wildcards are symbols that represent one or more characters in Bash commands.  Bash supports several kinds of wildcards. The most frequently used is the *star* wildcard represented by an asterisk. It can represent zero characters or a sequence of characters. Suppose the pwd contains hundreds of image files, but you only want to see the PNG files — the ones whose file names end with **.png**. Here's the command to list only those files:

```bash
ls *.png
```

Now let's say the pwd also contains JEPG files, and some end in **.jpg** while others end in **.jpeg.** Here's one way to list all the JPEG files:

```bash
ls *.jpg *.jpeg
```

Another way is to use the ? wildcard, which represents a single character and also matches on no character at all:

```bash
ls *.jp?g
```

Yet another way to use wildcards to filter output is to use square brackets, which denote groups of characters. The following command lists all the files in the pwd whose names contain a period immediately followed the letter J or P:

```bash
ls *.[jp]*
```

This would list all the **.jpg**, **.jpeg**, and **.png** files, but not **.gif** files.


You can also use the logical NOT operator (!) in square brackets to exclude characters. The following command lists all the files in the pwd whose file names do *not* include a period followed by a J or a P:

```bash
ls *.[!jp]*
```

Expressions in square brackets can represent ranges of characters. For example, the following command lists all the files in the current directory whose names begin with a lowercase letter:

```bash
ls [a-z]*
```

This command, by contrast, lists all the files in the current directory whose names begin with an uppercase letter:

```bash
ls [A-Z]*
```

And this one lists all the files in the current directory whose names begin with a lowercase *or* uppercase letter:

```bash
ls [a-zA-Z]*
```

Based on this, can you guess what the following command would do?

```bash
ls [0-9]*
```

If you need to use one of the wildcard characters as an ordinary character, you make it literal or "escape it" by prefacing it with a backslash. So, if for some reason you had an * as part of a file name — something you should never do intentionally — you could search for it with a command such as:

```bash
$ ls *\**
```

## The Linux file system

Because many Bash commands deal with the Linux file system, you should be aware of some of the differences in how Linux and Windows treat files. Among the important things to know:

- In Linux, files and directories whose names begin with a period (.) are hidden. A common example is configuration files stored in your home directory. You may include hidden files and directories in directory listings by include a `-a` flag in `ls` commands, as in `ls -a`.

- File names are case sensitive. In Linux, the file names "Fluffy" and "fluffy" are entirely different.

- Linux has no concept of a file-name extension as other operating systems do. Many Linux programs, do, however, recognize file-name extensions, if only as a convention.

Armed with this information, you're ready to learn the first key Bash commands that every sysadmin should know.





