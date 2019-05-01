# Use tags, release branches, and hooks

FIXME: incomplete at this point.

You're finally ready to make your website available inside the company, and
you want to update it automatically whenever anyone pushes a change.  You need
a `post-update` hook.

* `git clone project website`
* install post-update hook to pull changes into the website when master is
  pushed.
* push a change

You can also use this technique to back up a software project on a file server
or even a thumb drive.

<a href="https://www.tygertec.com/git-hooks-practical-uses-windows/" 
>Git hooks, practical uses (yes, even on Windows) | tygertec</a>
shebang needs full windows path to shell: 

```
#!C:/Program\ Files/Git/usr/bin/sh.exe
```
