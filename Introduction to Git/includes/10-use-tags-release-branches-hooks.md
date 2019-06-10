# Deploy and release software

Although Git is fundamentally a version-control system, it can also help with other tasks (or sequences of tasks, usually called "workflows") related to software configuration management. In this unit you learn how to set up a "web-focused" workflow for managing websites, and how to use branches and tags to organize and track releases.

## Deploy your website using a hook

Now that your Cats project is almost ready to show off, you need are a web server to host it, and a way to get the site deployed to
it. This section is based on <a href="http://joemaller.com/990/a-web-focused-git-workflow/">"A web-focused
Git workflow"</a> by Joe Maller, a simple and popular way of automating website deployment using hook scripts.

Hook scripts are small programs that Git runs when certain events occur, such as commits or pushes. Start by looking at `.git/hooks`:

```
$ ls .git/hooks
applypatch-msg.sample	   pre-applypatch.sample  pre-receive.sample
commit-msg.sample	       pre-commit.sample      prepare-commit-msg.sample
fsmonitor-watchman.sample  pre-push.sample	      update.sample
post-update.sample	       pre-rebase.sample
```

It's also worthwhile to look at the documentation, in `git help githooks`; not all of the possible hooks have samples. Any of the sample scripts can be activated by simply renaming it to remove the `.sample` extension.

### Create a hook script

Get started by making a clone of your shared repo for the web server to serve:

```
$ cd ~/sandbox
$ git clone Cats.git Cats-on-the-web
```

Then set up the post-update hook in `Cats.git`. The `<<EOF` construct takes everything up to the next line starting with `EOF` and redirects it into `cat`'s standard input. The `chmod +x` command marks the hook as executable, and the hook's name, `post-update`, tells Git that the hook should be run whenever changes are pushed.

```sh
$ cat > Cats.git/hooks/post-update <<EOF
#!/bin/sh
unset GIT_DIR; export GIT_DIR
cd ../Cats-on-the-web
git pull --ff-only origin master
git update-server-info
EOF
$ chmod +x Cats.git/hooks/post-update
```

The line starting with `#!` is called the "shebang" line. On a Unix system it tells the operating system which program to use to interpret the script: Shell, Bash, Python, etc.

In Git for Windows, the shell has additional logic to make this happen, but depending on your installation you might have to use a Windows file path rather than the expected Unix one. It would look like:

```
#!C:/Program\ Files/Git/usr/bin/sh.exe
```

(See [Git hooks, practical uses (yes, even on
Windows)](https://www.tygertec.com/git-hooks-practical-uses-windows/) by Ty
Walls for details, and more hook ideas.)

Now, whenever anybody pushes a change, the hook switches to the website directory and pulls it. This setup assumes that the shared bare repo and the actual website are on the same server, which is almost always the case.

You can use the same idea to automatically update backups on an external drive. 

For example, you return from a well-deserved vacation and want to catch up with what Bob and Alice have done:

```
$ git fetch
remote: Counting objects: 22, done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 22 (delta 6), reused 0 (delta 0)
Unpacking objects: 100% (22/22), done.
From ../Cats
   37903fd..39473bb  master     -> origin/master
$ git status
On branch master
Your branch is behind 'origin/master' by 5 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
$ git pull
Updating 37903fd..39473bb
Fast-forward
 assets/bobcat2-317x240.jpg    | Bin 0 -> 38514 bytes
 assets/bombay-cat-180x240.jpg | Bin 0 -> 39760 bytes
 assets/site.css               |   2 ++
 index.html                    |   6 ++++--
 4 files changed, 6 insertions(+), 2 deletions(-)
 create mode 100644 assets/bobcat2-317x240.jpg
 create mode 100644 assets/bombay-cat-180x240.jpg
```

Doing a fetch first rather than a pull can be useful. It shows you how far behind you are, and gives you a chance to look at the changes (with `git diff`) before you pull them.

Now you can fix that annoying footer, which is almost invisible because its only content is a horizontal rule.

```
$ sed -i.bak -e 's|<hr>|<a href="index.html">home</a>|' index.html
$ git commit -a -m 'Add a link to the footer'
[master d0346f6] Add a link to the footer
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 341 bytes | 341.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: From /home/steve/sandbox/Cats
remote:  * branch            master     -> FETCH_HEAD
remote:    39473bb..d0346f6  master     -> origin/master
remote: Updating 39473bb..d0346f6
remote: Fast-forward
remote:  index.html | 2 +-
remote:  1 file changed, 1 insertion(+), 1 deletion(-)
To ../Cats.git
   39473bb..d0346f6  master -> master
```

The lines prefixed with `remote:` came from the hook. Typically, both the shared repo and the website would be on the same remote web server and `origin` would have a URL like `git@server.example.org:Cats.git` -- that's the same format that you would use with `ssh`.

### Make changes on the server

You realize that you haven't added your own cat to the site. She would be very unhappy if she found out.

Since you happen to be logged in on the server, you can make your changes there.

```
$ cd ~/sandbox/Cats-on-the-web/
$ cp ../tortoiseshell-cat-180x240.jpg assets/
$ sed -i.bak -i '/bobcat/a <img class=".cat" src="assets/tortoiseshell-cat-180x240.jpg">' index.html
$ git add .
$ git commit -m "Make a last-minute addition."
[master d1b49d2] Make a last-minute addition.
 2 files changed, 1 insertion(+)
 create mode 100644 assets/tortoiseshell-cat-180x240.jpg
$  git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 20.50 KiB | 6.83 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: From /home/steve/sandbox/Cats
remote:  * branch            master     -> FETCH_HEAD
remote:    d0346f6..d1b49d2  master     -> origin/master
remote: Already up to date.
To /home/steve/sandbox/Cats.git
   d0346f6..d1b49d2  master -> master
```

Notice that the hook pulled the changes you just made, but of course it was already up to date. 

### Other uses for hooks

Joe Maller's article suggests using a `post-commit` hook in your web directory to automatically update the shared repo when emergency changes are made on the web server. You can use a `post-update` hook there to do a production build if the server has the necessary software, or to run tests on a staging server and push to production if they pass. Hooks are almost always an important
part of any Continuous Integration of Continuous Deployment workflow.

Many teams use a `pre-push` or `pre-commit` hook to run tests, to prevent bad code from being pushed; other uses include checking for signatures.


## Manage software releases with tags and branches

Let's suppose that your cats on the web have become wildly popular. As a result, you get requests for a more generic version of the site that can be used as a base for a site focusing on other kinds of pets. You'll want to make occasional updates, so you need to keep track of which versions you released. (Of course, this would make more sense if you'd switched to a site generator like [Jekyll](https://jekyllrb.com/) or [Hugo](https://gohugo.io/), which would let you release your templates as a theme. Maybe in Version 2.0?)

There are many ways to organize a project at this stage. GitFlow, originally described in [A successful Git branching
model](https://nvie.com/posts/a-successful-git-branching-model/) by Vincent Driessen, is a popular workflow for large projects.  It's especially useful for software products that have many versions in the field at the same time. There's even a Git subcommand, `flow`, for doing GitFlow-specific operations. GitFlow uses the master branch for numbered releases, and a separate branch
for development.

Since this is a *small* project and you're already using `master` for continuous integration into your main website, you could also keep `master` as it is and make a separate `release` branch. But since it's a *very* small project, the simplest thing is just to tag releases on `master`.

```
$ cd ~/sandbox/Cats
$ git pull
$ git tag -a v0.1 -m "Release version 0.1"
$ git log --oneline -n1
d1b49d2 (HEAD -> master, tag: v0.1, origin/master) Make a last-minute addition.
$ git show v0.1
```

Notice how tags are shown by `log` next to the commits they refer to. The `show` subcommand can be used to display the tag data along with the commit to which it refers.

Git has two kinds of tags: _lightweight_ and _annotated_. A lightweight tag is just a file (`refs/tags/NAME`) containing the hash of the tagged commit. Lightweight tags are primarily used as temporary labels; a typical use is to tag the head of a branch before you rebase it, to make it easier to go back if you ran into trouble. Lightweight tags are almost always local to a developer's copy of a repo.

Annotated tags, on the other hand, are objects that are very similar to commits. They have a message, author, and optional signature. Tags are not normally pushed, but you can do it with the `--follow-tags` option:

```
$ git push --follow-tags
Counting objects: 1, done.
Writing objects: 100% (1/1), 167 bytes | 167.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0)
remote: From /home/steve/sandbox/Cats
remote:  * branch            master     -> FETCH_HEAD
remote: Already up to date.
To ../Cats.git
 * [new tag]         v0.1 -> v0.1
```

This option pushes all annotated tags that can be reached from the commits being pushed. If you always want this behavior, you can set the `push.followTags` configuration option with:

```
git config --global push.followTags true
```

There is an older option to `push`, `--tags`, which pushes *all* tags. Using it is a bad idea, because developers often pick the same names for their lightweight tags. 

Before you can consider the website ready for public release, though, you need to make sure that all of the images are properly credited. They all came from Wikimedia, which makes it easy; for example go to [File:Short-haired tortoiseshell cat.jpg - Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Short-haired_tortoiseshell_cat.jpg) and click on "Use this file on the web."

Since you downloaded the images you want to use, you want to edit the `img` tags so that they point to your server and not Wikimedia's. We've already done that for you:

```
$ sed -i.bak -E 's/^<img[^>]*>//' index.html
$ for f in bombay bobcat tort; do
>     sed -i.bak -e "/<foot/e cat ../$f*.txt" index.html;
> done
$ git commit -a -m "Link images to their source pages" \
> -m "Put attributions in the link titles (tooltips)"
```

(You don't type the `>` characters; they're the prompt Bash gives you when a command continues on the next line. Bash knows that there's more coming after `do`, but you can continue any command by ending the line with a backslash.)

At this point, this looks good enough for you to call it version 1.0.

```
$ git tag -a v1.0 -m "Release 1.0!"
$ git push --follow-tags
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 790 bytes | 395.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: From /home/steve/sandbox/Cats
remote:  * branch            master     -> FETCH_HEAD
remote:    d1b49d2..8c97793  master     -> origin/master
remote: Updating d1b49d2..8c97793
remote: Fast-forward
remote:  index.html | 9 ++++++---
remote:  1 file changed, 6 insertions(+), 3 deletions(-)
To ../Cats.git
   d1b49d2..8c97793  master -> master
```

Congratulations! You, Bob, and Alice create a simple cat photo website, and you collaborated on the project using Git.

## Summary

In this unit, you learned about Git hooks, which perform actions when specific events occur. You also learned how to use the Git command

* [`git tag`](https://git-scm.com/docs/git-tag), which creates, deletes, or modifies tags.

In addition, you also encountered Bash `for` loops and learned how to break a long command by escaping the end of line with a backslash.

