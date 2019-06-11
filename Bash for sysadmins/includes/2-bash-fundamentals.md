# Bash fundamentals

Before we get into the details of Bash commands – we’ll do that shortly – let’s look at the way the shell interacts with the computer and the operating system.

To start Bash, you open a Azure Cloud terminal session and type in bash. When you do so, you see a shell prompt. Typically, the shell prompt contains your user name, the PC or server's name, then by a dollar sign. So, in the example below, the user name is sjvnbuddy, the server name is CheddarNorthwind, and the prompt is terminated by "$".

```
sjvnbuddy@CheddarNorthwind:~$
```

Bash is used both interactively — at the command line — and in shell scripts. Typing at the command line is used casually, such as when you are exploring what is going on with a system. However, when you perform a set of instructions regularly you want to store those commands in a text file — a script — that you or a program can invoke when needed.

Thus, Bash bridges the gap between a simple shell language and a programming language. Mastering it is essential for day-in and day-out system-administration work.

Any operating system and most programs need to read input, write output, and log errors. T, the Unix/Linux convention is to define three "file handles" for every process. These are:
- standard input, or `stdin` (0)
- standard output, or `stdout` (1)
- standard error, or `stderr` (2) 

When you use Bash interactively, `stdin` is typically the keyboard, `stdout` is your display (the screen, usually), and `stderr` is a log file. 

Traditionally, a Bash script file ends with ".sh", but that's not required.

For a Bash script to run, it must be made executable and it must be in the current print working directory, (pwd), be called for by its full path and script name; or be in a directory that is on the system PATH.

For a short review:
- A pwd is your current working directory 
- A system path defines the exact directory address
- A script is a shell program

## How Bash works

When you bring up a Bash shell, it first reads and executes commands from the file **/etc/profile**. This file — if it exists — contains the system's Bash's basic configuration data and any startup programs.

After reading this configuration file, Bash looks for **~/.bash_profile**, **~/.bash_login**, and **~/.profile** for the logged-on user configuration information. If none of these exist, Bash runs with the operating system defaults.

Bash configuration files are a subject all to themselves and we don't deal with them in this module. While you can accomplish quite a bit with custom configurations, they are beyond the basics.

Since Because many Bash commands deal with the Linux's file system, you should be aware of its differences from the Windows file system. Among the important things to know:

- File names that begin with a period (.) are hidden. These commonly include configuration files stored in your home directory that were created when the account was created. Other hidden files and directories may includebe application configuration and settings files.
- File names are case sensitive. Unlike the legacy Windows file systems, in Linux the file names "Fluffy" and "fluffy" are entirely different from one another.
- Linux has no concept of a "file extension, as do legacy operating systems. However, while Linux doesn't care about file extensions, many application programs do.

## Bash syntax

The full syntax for a Bash command is: command, options, argument. This syntax is very precise. Close to being right isn't good enough in Bash. If a shell argument doesn't use just the right combination of commands, options, and arguments — including spacing — it will fail. 

It works like this. Usually, the Bash shell treats the first string it encounters as a command. Most of the time, that’s what you intend: do this thing. So, for example, to see what files are inside your pwd you would you invoke the Linux directory command, `ls`: 

> The examples show the $ prompt to represent the command line where you type. Don’t type the $ or you will get an error message!

```bash
$ ls
```
 
<INSERT ls.png>

As with other shell languages, Bash commands are often used with an argument. For example, creating a directory requires a name. So when you use mkdir to create a subdirectory called KittyOrders off your current pwd, you use:

```bash
$ mkdir KittyOrders
```

<INSERT mkdir.png>

Some Bash commands have options, which may or may not be required for a given task. Options (also called flags) give a command more specific instructions. So to create a new directory with a new sub-directory under your pwd, you'd use the following command string with the `--parents` flag. 

```bash
$ mkdir --parents Felines/BlackCats
```

<INSERT: mkdir parents.png>
Many Bash options can also be invoked with an abbreviated alias. An alternate for --parents is –p. So, to   create the same directories in the same place, you could type:

```bash
$ mkdir -p Felines/BlackCats
```

Many Bash commands can only be run by the root user — the system administrator or superuser. If you try the command without those system priveleges, the command fails. For example, in Linux, ordinary users cannot create directories.

You don't, however, want to run as root most of the time. It's too dangerous. So, to run such commands without logging in as root, you preface the program with the sudo command.

Say, for example, if you try to create a directory in the system directory "/usr/games" you will fail.

```bash
$ mkdir KittyOrders
```

<INSERT: mkdir fail.png>

So, instead you must use `sudo` to run `mkdir`. When you run `sudo`, you're telling the shell that for this one command you are acting with the root user level of permission. Now, you've created the "KittyOrders" subdirectory in the "/usr/games" directory.

```bash
$ sudo mkdir KittyOrders
```

<INSERT: sudo mkdir.png>

Which options and arguments can be used, or must be used, varies from command to command. Fortunately, Bash and Linux documentation is built into the operating system. There's an always-available Help File. 

To learn about the options for a command – everyone forgets them sometimes – you run the man command. For instance, to know learn in exact detail how the mkdir command works, run:

```bash
$ man mkdir
```

<INSERT man mkdir.png>

Man is going to become your best friend. Man is where you find the information you need to understand how any individual command works.

Besides man, most Bash and Linux commands support the `--help` option. This shows you a description of the command's supported syntax and options. For example, to get a top-level view of the extremely useful regular expression search command grep (which we discuss in a later unit), type:

```bash
$ grep --help
```

<INSERT grep help.png>

Bash also comes with other useful documentation commands. For Bash's built-in commands, you can use the following syntax:

```bash
$ help <command>
```

For example, for in-depth information about the change directory command, cd, type:.

```bash
$ help cd
```

<INSERT help cd.png>

## Wildcards

Wild cards are symbols that used to replace or represent one or more characters. Bash supports several kinds of wildcards. These enable you to you to search on patterns and strings of characters. 
Bash supports several kinds of wild cards. The following trio are the most important ; expect to useof them. You'll be using these all the time.

### Bash wildcards

The most frequently used wild card is the star wild card, which you may know as an asterisk "*". It can represent zero characters, all single characters, or any string. Let's take this directory which contains the following files.

<INSERT ls kitties content.png>

When we use the * wildcard in the command below, it shows all files starting with the letter B.

```bash
$ ls B*
```

<INSERT ls wildcard B.png>

The question mark "?" wild card matches any single character. So, the following command on the same directory produces only a single file name.

```bash
$ ls B?ll
```

<INSERT ls ?.png>

You can use multiple kinds of wildcards in a single command. For instance, this command lists files with names containing the letter "e" in the second character.

<INSERT Double WildcardWildcard.png>

The sSquare brackets “[ ]” wildcard pair enables you to match a set of values. It They can contain alphanumeric, alphabetic, numeral, and upper-date case alphabetic characters. You can also set it the contents of the bracket pair to match any character that is not a member of the set.

For example, this command presents you with any file name containing the characters "B, e, and l."

```bash
$ ls [Bel]*
```

<INSERT: ls set of characters wildcard.png>

If you want to find files that don't contain any of those three letters, you'd preface the letters with the exclamation mark "!" character. In Bash, the "!" is a logical not construct. In this context, this means you want to match any character except B, e, or l. 

```bash
$ ls [!Bel]*
```

<INSERT ls Not wildcardwild card.png>

Now, say you want to find files that use a range of characters. Say, you need to lay your hands on only filenames with all lowercase names. For that job, use this command to find all the filenames that only have lowercase letters.

```bash
$ ls [a-z]*
```

<INSERT ls lowercase wildcard.png>

You can also use [A-Z] for all uppercase:

```bash
$ ls [A-Z]*
```

<INSERT ls uppercase wildcard.png>

If you need to use one of the wildcard characters as an ordinary character, you make it literal or "escape it" by prefacing it with a backslash ("\"). So, if for some reason you had an * or ? as part of a file — which you should never do intentionally — you could search for it with a command such as:

```bash
$ ls \*
```

Armed with this information, you're ready to learn the first key Bash commands that every sysadmin should know.