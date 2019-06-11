# Exercise: Find and eliminate unauthorized users

Users come, users go, and sometimes you get users you don't want at all. When an employee leaves to "pursue other opportunities," the sysadmin is called upon to ensure that the worker can no longer log into the company’s computer systems. Sysadmins are also expected to know who’s logged in — and who shouldn't be.

To find out who's on your servers, Linux provides the `who` (or `w`) command. This command displays information about the users currently on the computer system and those users' processes. By itself, `w` shows how many users are on the system, their user names, their IP addresses, how long they've been in the server, data about the time their processes are taking on the system, and the commands they're currently running.

```bash
$ w
```

Sure enough, in this case there are no other users. Let's say you find someone else though, under the name "bad_user" who is SSHing their way into another machine. Do you want them do that? Maybe yes, maybe no. If no, let's kick them out of your server. Your next step is to find their session's PID.

This shows all of bad_user's process PIDs:

```bash
$ ps -ef | grep bad_user
```

He's not SSHing anywhere that we can see, but we still don't want him on our server. Let's get rid of him.

Take the PID for "bad_user's" session and terminate it with extreme prejudice. Since the PID is 23308, we blow it away by running the `kill` command as the root user and pointing `kill` at 23308:

```bash
$ sudo kill -9 29412
```

And, as we can tell by running `ps -ef | grep bad_user` again, he's gone. 

Next, you should block "bad_user" from your server using other tools, but that's a much longer story for another day.