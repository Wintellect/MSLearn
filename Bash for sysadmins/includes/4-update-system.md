# Exercise: Update the system

In your new job, you just started running the pre-existing server Northwind. It almost certainly needs to have its base operating system updated. Fortunately, the operating system lets you know when new patches are available.

<INSERT: system needs update.png>

So, let's patch Northwind with a single Bash command line. You do this by combining two `apt` commands. `apt` is the default Ubuntu Linux command for installing and removing programs. 

```bash
$ sudo apt update && sudo apt upgrade -y
```

The first part of the command, `sudo apt update`, is run as the root user with the `update` flag. This tells the server to update the local database of available packages. Without the update, the local software database isn't updated. The second half, `sudo apt upgrade`, also runs as the root user. It is what actually updates the server. 

The `&&` instructs Bash to run the two commands that the second one only runs only the earlier command runs successfully. The `-y` in the end automatically enters an answer of "yes" when the command apt upgrade asks for confirmation before installing the updates.

Nothing says you have to do these in one line. You can also run these commands by themselves.

```bash
$ sudo apt update
$ sudo apt upgrade
```

Regardless of how you update the operating system, afterwards you may need to reboot the computer. (You can avoid the need to do this by installing Ubuntu LivePatch, but that's beyond what we're covering here.)

Before you restart your computer, first get rid of any old program packages hanging around. You do this with the `autoremove` command. This command, which again requires root-level access, removes obsolete packages.

```bash
$ sudo apt autoremove
```

That done, you're ready to reboot the server. There are several ways to do this. All require root-level access; each runs the shutdown command with the `-r` flag. The `-r` flag tells the system to shutdown and then reboot. To reboot immediately, use:

```bash
$ sudo shutdown now -r
```

To reboot later — after, say, 30 minutes — use the command:

```bash
$ sudo shutdown -r +30
```

What about at a given time? You can do that too.

```bash
$ sudo shutdown -r 15:00
```

The results should always be the same: a fully patched and ready- to-go server.