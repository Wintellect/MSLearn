# Exercise: Terminate a misbehaving process

Computers are imperfect. Sooner or later, it seems, a program goes bad. That's why you have a job as a sysadmin; it's up to you to troubleshoot and fix system problems.

The application may take up too much CPU time, it may freeze, or it may simply stop responding. In that case, you probably want to kill it off with extreme prejudice. To identify it and get rid of it you can use a simple pipe command with `ps` and `grep`. Then, to knock it on its virtual head, you use the `kill` command.

First, let's chase down the misbehaving program by using `ps` to track down a Python program gone bad. To refresh your memory, with `ps` and those flags you display all processes along with a great deal of information on each one. You pipe those results to grep, which then seeks out the pattern "python" within those results.

```bash
$ ps -ef | grep python
```

This presents you with all the programs currently invoking python and their process IDs (PIDs). Now, if you wanted to terminate one of those instances, you look for two pieces of information:
- Process name
- Process ID

There are two commands used to kill a process:
- `kill`: Kill a process by PID
- `killall`: Kill a process by name

Different signals can be sent to both `kill` commands. What signal you send is determined by the results you want. For instance, the hang up (HUP) signal kills and then restarts the process. This is always a wise choice when you need the process to immediately restart, such as with the case of a Linux daemon.

Like most Linux commands, there many possible flags. You can get a list of options for the `kill` command with `kill -l`. 

```bash
$ kill -l 
```

You have several choices to get rid of a specific process. For precision's sake, you should knock processes over the head using PIDs. So, to put an end to the unattended-upgrade process, use the command:

```bash
$ kill -9 1090
```

Let's say your Linux system has been running for a while and you suspect some dead processes are eating up resources. To find these processes, called zombies, use the `ps` command with the `-aux` flag. These show:

- All users' processes
- By user names
- Including all processes not attached to a terminal

These flags also show the status of each process. A zombie process shows up with, naturally, a Z. So to reveal these living dead processes, type:

```bash
$ ps -aux | grep Z
```

You can then kill them, as before, with the `kill` command. 

<INSERT Zombie Process.png>

In this example, we didn't find any zombies. That process with a "Z" in it? It's the `grep` process searching for a Z. Remember when you filter processes through grep, the `grep` search itself always shows up. 

It is a well known Linux oddity to have two similar but not identical set of flags that produce somewhat different results. It traces back to historical divergences between POSIX Unix systems, of which Linux is one, and BSD Unix systems, the most common of which today is macOS. In the beginning, POSIX used `-ef` while the BSD required `aux`. Today, both operating system families accept either format. 

This serves as an excellent reminder of why you should look closely at the manual for all Linux commands. Learning Bash is like learning English as a second language. There are many exceptions to the rules.