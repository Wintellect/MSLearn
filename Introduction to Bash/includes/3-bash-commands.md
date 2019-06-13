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

After the permissions comes the item's owner, the owner's group, the size in bytes, the last time the item was modified, and the file or directory name. 

`ls` also accepts a path name as an argument. To view the contents of the "/etc" subdirectory in long format, you could type:

```bash
$ ls -l /etc
```

The "/etc" directory is a special one in Linux. It contains system-configuration files. You don't want to delete any files from this directory unless you know what you are doing.

### The `cat` command

Suppose you want to see what's inside a file. You can use the `cat` command for that. The output won't make much sense unless the file is a text file. The following command shows the contents of the **os-release** file stored in the "/etc" directory:

```bash
cat /etc/os-release
```

This is a useful command because it tells you which Linux distribution you're running:

```
NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

### The `cd` command

`cd` stands for "change directory," and it does exactly what the name suggests: it changes the pwd to another directory. It enables you to move from one directory to another just as its counterpart in Windows does. 

The following command changes to a subdirectory of the current directory named "kitties:"

```bash
cd kitties
```

You can move up a directory by specifying ".." as the directory name:

```bash
cd ..
```

This one changes to your home directory — the one that you land in when you first log in:

```bash
cd ~
```

You can also use absolute path names. Let's say you want to inspect the contents of the "/usr/bin" directory where programs that come with your Linux distribution are stored. You could use an `ls /user/bin` command. Or you could change to that directory and execute an `ls` command:

```bash
cd /usr/bin
ls
```

Once more, "/usr/bin" is an important directory in Linux, so be careful poking around there.

### The `cp` command

The `cp` command copies — not just files, but entire directories (and their subdirectories) if you want. To make a copy of **cat.jpg** named **kitty.jpg**, use the command:

```bash
$ cp cat.jpg kitty.jpg
```

If **kitty.jpg** already exists, Bash silently replaces the older one with the copy. That's great if that's what you intended, but not so wonderful if you didn't realize you were about to overwrite the old version. 

Fortunately, if you use the `-i` (for "interactive") flag, Bash warns you before blowing away any existing file. This is much safer:

```bash
$ cp -i cat.jpg kitty.jpg
```

To copy a file to a different directory — for example, the home directory — include the path:

```bash
$ cp cat.jpg ~/kitty.jpg
```

To copy all the files in the current directory to a subdirectory named "kitties," do this:

```bash
cp * kitties
```

To copy all the files in a subdirectory named "cats" into a subdirectory named "kittens," you would do this:

```bash
cp cats kittens
```

This will copy the files in the "cats" directory, but not any files in subdirectories of "cats." To perform a deep copy that copies subdirectories and their contents, too, you can do this:

```bash
$ cp -r cats kittens
```

The `-r` stands for "recursive." In this context, it means the `cp` command works its way through a directory *and* its subdirectories before exiting.

### The `rm` command

The `rm` command is short for "remove." As you'd expect, `rm`, like its MS-DOS cousin `del`, deletes files. So this command puts an end to **cats.jpg**:

```bash
$ rm cats.jpg
```

And this command deletes all the files in the pwd:

```bash
$ rm *
```

Be wary of `rm`. It's a dangerous command.

Like `cp`, the `rm` command supports the `-i` flag. The following command lets you think before you delete:

```bash
$ rm -i cats.jpg
```

Making it a habit to include `-i` in every `rm` prevents you from falling prey to one of Linux's biggest blunders. The dreaded `rm -rf /` command deletes every file on an entire drive. It works by recursively all the subdirectories of root and their subdirectories. The `-f` flag adds insult to injury by deleting read-only files without confirmation. **Don't do this.**

If also pays to include a `-i` flag when using `rm` with any wildcard. The possibility always exists for you to delete the last file you ever wanted to get rid of. There is no easy way to undelete files in Linux.

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