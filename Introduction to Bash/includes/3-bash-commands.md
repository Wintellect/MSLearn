# Bash commands


Every shell language has its most-used commands, just as every guitarist has a dozen songs she must be ready to play. ("Seven Nation Army," "Sweet Child O' Mine," and "Stairway to Heaven" come to mind, among others.) Let's start building your Bash repertoire by examining the most common Bash commands. 

### The `ls` command

You've met `ls` before. As you know, `ls` lists the contents of the pwd or the directory specified in an argument to the command. By itself, it shows you the files and directories in the current directory:

```bash
ls
```

Remember that files and directories whose names begin with a period are hidden by default. To include these items in a directory listing, include a `-a` flag in the `ls` command:

```bash
ls -a
```
To get even more information about the files and directories in the current directory, use a `-l` (for "long") flag:

```bash
ls -l
```

Here's some sample output from a directory that contains a handful of JPEGs and PNGs and a subdirectory named "gifs:"

```
-rw-rw-r-- 1 azureuser azureuser  473774 Jun 13 15:38 0001.png
-rw-rw-r-- 1 azureuser azureuser 1557965 Jun 13 14:43 0002.jpg
-rw-rw-r-- 1 azureuser azureuser  473774 Mar 26 09:21 0003.png
-rw-rw-r-- 1 azureuser azureuser 4193680 Jun 13 09:40 0004.jpg
-rw-rw-r-- 1 azureuser azureuser  423325 Jun 10 12:53 0005.jpg
-rw-rw-r-- 1 azureuser azureuser 2278001 Jun 12 04:21 0006.jpg
-rw-rw-r-- 1 azureuser azureuser 1220517 Jun 13 14:44 0007.jpg
drwxrwxr-x 2 azureuser azureuser    4096 Jun 13 20:16 gifs
```

Each line has an explicit structure that provides detailed information about the corresponding file or directory. The first nine characters specify:

- Whether the item is a file (-) or directory (d)
- The item's read (r), write (w), and execute (x) permissions, in that order
- The read, write, and execute permissions of the item's owner
- The read, write, and execute permissions of the group to which the item belongs

A file can't be executed unless the executable flag is set. Images aren't executable files. Consequently, none of the files in this example have an "x" in position 4.

So, in the example above, only the owner can write to the hidden **.bash_history** file. You can also see that anyone can read the hidden **.bashrc** file, which is the shell script Bash runs whenever it is started interactively.

After the permissions comes the item's owner, the owner's group, the size in bytes, the last time the item was modified, and the file or directory name. 

`ls` also accepts a path name as an argument. To view the contents of the "gifs" subdirectory in long format, you could type:

```bash
$ ls -l gifs
```

You'll notice that file and directory names are color-coded. That's a default Bash setting in Azure's Ubuntu 18.04 instances.

### The `cat` command

Now, it's time to do more than just look at Northwind's file directories. To look inside the files you use `cat`, which reads and concatenates files — that is, strings them together. Remember that in Linux, everything is treated as files so that's far more flexible than it might first appear.

There are three jobs for which `cat` is commonly used to display the contents of one or more text files, combine files by appending the contents of one file to the end of another file, and create new files. 

From the top, `cat` is often used to view files. Here, we use it to view the contents of the file **os-release**. This is also useful because it tells us a bit about which Linux distribution we're running.

```bash
$ cat /etc/os-release
```

To append one file to another and thus merge the contents of two files, use `cat`. Doing so lists the files to combine and then directs their contents using the the Bash I/O redirection operator `>` (more on redirection later) to a new file. The resulting file contains the contents of both files.

```bash
$ cat create new file.png
```

You can see the contents of the new file **NewCat** [You didn't say NewCat above?] by using `cat` in its first role:

```bash
$ cat NewCat
```

Finally, you can use `cat` to create new files by simply entering the command and redirecting your keyboard input into a new file. This command creates the file **Fuzzball**. To close and save the file, press **Ctrl-D**.

```bash
$ cat > Fuzzball
```

### The `cd` command

Now that we know a little bit about showing the contents of directories, we should learn a bit about navigating them. Change directory, `cd`, does exactly what the name suggests. It enables you to move from one directory to another just as its Windows cousin does. 

For example, to move from your primary directory to the subdirectory, use this command: 

```bash
$ cd kitties
```

Now, let's move back to your home directory. You can use several commands from this subdirectory, but the one below always gets you back to it; the `~` means home. 

```bash
$ cd ~
```

In this case, you could have also moved up a directory with the following command:

```bash
$ cd ..
```

You can also shift positions by using absolute directories. So the following command, no matter my location on the Northwind server, takes me back to my home directory.

```bash
$ cd /home/buddy
```

This works for any absolute address. So to jump from any directory to Linux's "/usr/bin" directory, which holds your Linux's distribution standard programs, type:

```bash
$ cd /usr/bin
```

### The `cp` command

Now, it's time to start working on Northwind's files and directories. Let's start with `cp`. This command copies both files and directories. In its most simple form, `cp` copies a single file. So, to make a copy of Selkirk use the command:

```bash
$ cp Selkirk JamesTKirk
```

If the file **JamesTKirk** already exists, Bash cheerfully and silently replaces the older **JamesTKirk** file with a new copy. Jim, he's dead.

That's great if that's what you intended, but not so wonderful if you didn't realize you just overwrote the old version of Northwind's customer records for **JamesTKirk**. 

Fortunately, if you use the `-i` (for "interactive") flag, Bash warns you before blowing away any existing file (in this case, **JamesTKirk**). This is much safer.

```bash
$ cp -i Selkirk JamesTKirk
```

If **JamesTKirk** already exists, Bash responds by asking if you really want to overwrite the file:

<INSERT cp -i.png>

To copy a file to a different directory, use the command:

```bash
$ cp Bobtail ~/kitties
```

To copy a directory, use:

```bash
$ cp -r kitties Cats
```

The `-r` flag stands for "recursive." In this context, it means the `cp` command works its way through a directory before exiting. So, when you change directories into Cats and look at its contents, you see a familiar set of files.

### The `rm` command

The `rm` command is short for "remove." As you'd expect, `rm`, like its MS-DOS cousin `del`, deletes files. So this command puts an end to Fuzzball:

```bash
$ rm Fuzzball
```

Be wary of `rm`. It's a dangerous command.

It's a good idea to always run `rm` with the `-i` flag. So, in another directory, where Fuzzball lives on, the following command lets you think before you delete:

```bash
$ rm -i Fuzzball
```

Otherwise, you might fall prey to one of the most infamous of Linux blunders: The dreaded `rm -rf /` would delete every file on an entire drive. It works by forcing recursive deletion through all subdirectories. The `-f` flag adds insult to injury by deleting read-only files without confirmation. Don't do this.

If also pays to be wary of `rm` when you use it with any wildcard. The possibility always exists for you to delete the last file you ever wanted to get rid of. There is no easy way to undelete files in Linux.

### The `ps` command

The `ps` command gives you a snapshot of all the currently-running processes on this Northwind server. By itself, with no arguments, it shows you all your current shell sessions processes. Not much is going on, as you see, on the top level of your shell.

```bash
$ ps
```

But, that's only at the surface. It's a different story when you take a deeper look of all your running processes with the `-e` flag

```bash
$ ps -e
```

For a more comprehensive view, use the `-f` flag. This shows the names of the running processes, their process identification number (pid), the pid of its parent program (ppid), the time the program began (STIME), what terminal, if any, to which a process is attached (TTY), how much CPU time has been spent on a process (TIME), and the processes' full path names.

```bash
$ ps -ef 
```

You'll use the data from `ps` and its related commands every day of your Linux sysadmin life.
In this unit, you've learned the some of the most used Linux Bash commands. Here's where to go to read the detailed information for each of them:

- `ls`: show directory contents 
- `cat`: concatenates files
- `cd`: change directory
- `cp`: copy files and directories
- `rm`: remove files and directories
- `ps`: display data on all currently running processes. 
- `sudo`: run a single command as the root user.

## Bash I/O operators

The commands you learned so far all give you helpful information. But you can really get work done at your new company only when you put them together using Bash's I/O operators.

By default, Bash commands direct their output to the display and they take their input from the keyboard. This does not have to be the case. By using I/O operators, you can redirect the output of many commands to files, devices, and to other commands.

The first element in using Bash's power is the pipe `|` operator. It redirects the output of the first command to the input of the second command. So, for instance, you might use `cat` to display the contents of a large file; the content scrolls too quickly for the human eye. But you can make it much more usable by piping the results to another program. 

For example, the 16K file named **Guide** contains an early version of this document. To view it with cat, it scrolls by too quickly to be read. All you see on your screen are the last lines.

```bash
$ cat Guide
```

But, if you pipe it to the command head, which displays the first lines of text in a file, you see the document's opening lines:

```bash
$ cat Guide | head
```

Or, say you want to know in detail about what processes are running. One way to do that is by piping the results of the `ps` command through `grep`. The `grep` command is a powerful utility for searching plain text for regular expressions. 

To do so, we pipe the output from `ps -ef` (for a full view of all running processes) through `grep` which searches for processes being run by the user sjvn:

```bash
$ ps -ef | grep sjvn
```

To redirect data from the standard output (your display) to a file you use `>`. So, for instance, this command sends the results of this directory command to new file **file.listing.txt**. If the file already exists, it overwrites it. 

```bash
$ ls -la > file.listing.txt
```

To append to an existing file, use `>>` to add data to it. This command adds more data to **file.listing.txt**:

```bash
$ ls -la >> file.listing.txt
```

In the screenshot above, we pipe `cat`'s output to another program, `more`. `more` lets you display the contents of a text stream in pages.

You can also use files as input. By default, standard input comes from the keyboard, but it too can be redirected. To redirect standard input from a file instead of the keyboard, use the `<` character. 
One simple sysadmin task is to sort the contents of a file. As the name suggests, `sort` sorts a text file's contents in alphabetical order. With Bash's `sort`, lines starting with a lowercase letter appear before lines starting with the same letter in uppercase.

```bash
$ sort < file.listing.txt
```

To save the results to a new file, you can redirect both a program's input and output with one command, which is far more efficient. To both sort **file.listing.txt** and send the result to the new file **sorted_file_listing.txt**, you would type:

```bash
$ sort < file.listing.txt > sorted_file_listing.txt
```

That's just the start. You can chain Linux commands together. For instance:

```bash
$ cat bad_format_report.txt | fmt | pr | lpr
```

Here, instead of showing you the file, `cat` pipes the contents to `fmt`'s standard input of `fmt`. The `fmt` formats the results into a tidy paragraph and passes it on to pr. This command transforms the text into pages. It then outputs it to `pr`'s standard output, which is piped into `lpr`'s standard input. Then `lpr` sends the tidied-up output to the system printer. All in a single line!

Let's take a look now at some practical examples of using Bash.