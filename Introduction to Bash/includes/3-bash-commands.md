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
cp cat.jpg kitty.jpg
```

If **kitty.jpg** already exists, Bash silently replaces the older one with the copy. That's great if that's what you intended, but not so wonderful if you didn't realize you were about to overwrite the old version. 

Fortunately, if you use the `-i` (for "interactive") flag, Bash warns you before blowing away any existing file. This is much safer:

```bash
cp -i cat.jpg kitty.jpg
```

To copy a file to a different directory — for example, the home directory — include the path:

```bash
cp cat.jpg ~/kitty.jpg
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
cp -r cats kittens
```

The `-r` stands for "recursive." In this context, it means the `cp` command works its way through a directory *and* its subdirectories before exiting.

### The `rm` command

The `rm` command is short for "remove." As you'd expect, `rm`, like its MS-DOS cousin `del`, deletes files. So this command puts an end to **cats.jpg**:

```bash
rm cats.jpg
```

And this command deletes all the files in the pwd:

```bash
rm *
```

Be wary of `rm`. It's a dangerous command.

Like `cp`, the `rm` command supports the `-i` flag. The following command lets you think before you delete:

```bash
rm -i *
```

Make it a habit to include `-i` in every `rm` command and you might not fall prey to one of Linux's biggest blunders. The dreaded `rm -rf /` command deletes every file on an entire drive. It works by recursively deleting all the subdirectories of root and their subdirectories. The `-f` (for "force") flag adds insult to injury by suppressing prompts. **Don't do this.**

### The `ps` command

The `ps` command gives you a snapshot of all the currently running processes. By itself, with no arguments, it shows all your shell processes — in other words, not much. But it's a different story when you include a `-e` flag:

```bash
ps -e
```

`-e` lists *all* running processes, and there are typically many of them.

For an even more comprehensive look at what processes are running in the system, use the `-ef` flag:

```bash
ps -ef 
```

This shows the names of all the running processes, their process identification numbers (PIDs), the PIDs of their parents (PPIDs), when they began (STIME), what terminal, if any, they're attached to (TTY), how much CPU time they have racked up (TIME), and their full path names. Here is an abbreviated example:

```
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0 13:35 ?        00:00:03 /sbin/init
root          2      0  0 13:35 ?        00:00:00 [kthreadd]
root          3      2  0 13:35 ?        00:00:00 [rcu_gp]
root          4      2  0 13:35 ?        00:00:00 [rcu_par_gp]
root          5      2  0 13:35 ?        00:00:00 [kworker/0:0-cgr]
root          6      2  0 13:35 ?        00:00:00 [kworker/0:0H-kb]
root          8      2  0 13:35 ?        00:00:00 [mm_percpu_wq]
root          9      2  0 13:35 ?        00:00:01 [ksoftirqd/0]
root         10      2  0 13:35 ?        00:00:02 [rcu_sched]
```


You'll use `ps` virtually every day in your life as a Linux sysadmin. One common use for it is to retrieve process IDs for processes that you want to kill. More on this important topic later.

## Bash I/O operators

You can do a lot in Linux just by exercising Bash commands and their many options. But you can really get work done when you combine commands using I/O operators:

- `<` for redirecting input to a source other than the keyboard
- `>` for redirecting output to destination other than the screen
- `>>` for doing the same, but appending rather than overwriting
- `|` for piping output from one command to the input of another

Suppose you want to list everything in the pwd but capture the output in a file named **listing.txt**. The following command does just that:

```bash
ls > listing.txt
```

If **listing.txt** already exists, it gets overwritten. If you use the `>>` operator instead, the output from `ls` is appended to what's already in **listing.txt**:

```bash
ls >> listing.txt
```

The piping operator is extremely powerful (and often used). It redirects the output of the first command to the input of the second command. Let's say you use `cat` to display the contents of a large file, but the content scrolls by too quickly for you to read. You can make the output more readable by piping the results to another command such as `more`. The following commands lists all the currently running processes. But once the screen is dull, you press **Enter** to display subsequent lines:

```bash
ps -ef | more
```

You can also pipe output to `head` to see just the first several lines:

```bash
ps -ef | head
```

Or suppose you want to filter the output to include only those lines containing the word "daemon." One way to do that is by piping the output from `ps` to `grep`:

```bash
ps -ef | grep daemon
```

The output might look like this:

```
azureus+  52463  50702  0 23:28 pts/0    00:00:00 grep --color=auto deamon
azureuser@bash-vm:~$ ps -ef | grep daemon
root        449      1  0 13:35 ?        00:00:17 /usr/lib/linux-tools/4.18.0-1018-azure/hv_kvp_daemon -n
root        988      1  0 13:35 ?        00:00:00 /usr/lib/accountsservice/accounts-daemon
message+   1002      1  0 13:35 ?        00:00:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
daemon     1035      1  0 13:35 ?        00:00:00 /usr/sbin/atd -f
root       1037      1  0 13:35 ?        00:00:00 /usr/bin/python3 -u /usr/sbin/waagent -daemon
root       1039      1  0 13:35 ?        00:00:00 /usr/lib/linux-tools/4.18.0-1018-azure/hv_vss_daemon -n
azureus+  52477  50702  0 23:28 pts/0    00:00:00 grep --color=auto daemon
```

The `grep` command is a powerful tool for searching plain text using regular expressions. 

You can also use files as input. By default, standard input comes from the keyboard, but it too can be redirected. To get input from a file instead of the keyboard, use the `<` operator. One common sysadmin task is to sort the contents of a file. As the name suggests, `sort` sorts text in alphabetical order.

```bash
sort < file.txt
```

Note that with Bash's `sort`, lines starting with a lowercase letter appear before lines starting with the same letter in uppercase.

To save the sorted results to a new file, you can redirect input *and* output:

```bash
sort < file.txt > sorted_file.txt
```

You can use I/O operators to chain Linux commands endlessly. For instance:

```bash
cat file.txt | fmt | pr | lpr
```

Here, the output from `cat` goes as input to `fmt`, the output from `fmt` goes as input to `pr`, and s on. `fmt` formats the results into a tidy paragraph. '`'pr` paginates the results. And `lpr` sends the paginated output to the system printer. All in a single line!