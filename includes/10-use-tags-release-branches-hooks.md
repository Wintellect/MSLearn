# Deploy and release software

Although Git is fundamentally a version-control system, it can also help with
other tasks (or sequences of tasks, usually called "workflows") related to
software configuration management.  In this unit you'll learn how to set up a
"web-focused" workflow for managing websites, and how to use branches and tags
to organize and track releases.

## Deploy your website using a hook

Now that your Cats project is almost ready to show off, the next things you
need are a web server to host it, and a way of getting the site deployed to
it.  This section is based on <a
href="http://joemaller.com/990/a-web-focused-git-workflow/" >"A web-focused
Git workflow" by Joe Maller</a>, a simple and popular way of automating
website deployment using hook scripts.

Hook scripts are small programs that Git runs when certain events occur, such
as commits or pushes.  Start by taking a look at `.git/hooks`:

```
$ ls .git/hooks
applypatch-msg.sample	   pre-applypatch.sample  pre-receive.sample
commit-msg.sample	       pre-commit.sample      prepare-commit-msg.sample
fsmonitor-watchman.sample  pre-push.sample	      update.sample
post-update.sample	       pre-rebase.sample
```

It's also worthwhile to look at the documentation, in `git help githooks`; not
all of the possible hooks have samples.  Any of the sample scripts can be
activated by simply renaming it to remove the `.sample` extension.

### Create a hook script

Get started by making a clone of your shared repo for the web server to serve:

```
$ git clone Cats.git Cats-on-the-web
```

And then set up the post-update hook in `Cats.git`.  The `<<EOF` construct
takes everything up to the next line starting with `EOF` and redirects it into
`cat`'s standard input.  The `chmod +x` command marks the hook as executable,
and the hook's name, `post-update`, tells Git that the hook should be run
whenever changes are pushed.

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

The line starting with `#!` is called the "shebang" line, and on a Unix system
it tells the operating system which program -- Shell, Bash, Python, etc. -- to
use to interpret the script.  In Git for Windows, the shell has additional
logic to make this happen, but depending on your installation you might have
to use a Windows file path rather than the expected Unix one.  It would look
like:

```
#!C:/Program\ Files/Git/usr/bin/sh.exe
```

(See [Git hooks, practical uses (yes, even on
Windows)](https://www.tygertec.com/git-hooks-practical-uses-windows/) by Ty
Walls for details, and more hook ideas.)

Now, whenever anybody pushes a change, the hook switches to the website
directory and pulls it.  This setup assumes that the shared bare repo and the
actual website are on the same server, which is almost always the case.  You
can use the same idea to automatically update backups on an external drive.

### Other uses for hooks

Joe Maller's article suggests using a `post-commit` hook in your web directory
to automatically update the shared repo when emergency changes are made on the
web server.  You can use a `post-update` hook there to do a production build
if the server has the necessary software, or to run tests on a staging server
and push to production if they pass.  Hooks are almost always an important
part of any Continuous Integration of Continuous Deployment workflow.

Many teams use a `pre-push` or `pre-commit` hook to run tests, to prevent bad
code from being pushed; other uses include checking for signatures.


## Manage software releases with tags and branches

Let's suppose that your cats on the web have become wildly popular, and you've
been getting requests for a more generic version of the site that can be used
as a base for a site focusing on other kinds of pets.  You'll want to make
occasional updates, so you need to keep track of which versions you've
released.  (Of course, this would make more sense if you'd switched to a site
generator like [Jekyll](https://jekyllrb.com/) or [Hugo](https://gohugo.io/),
which would let you release your templates as a theme.  Maybe in Version 2.0?)

There are many ways to organize a project at this stage.  GitFlow, originally
described in [A successful Git branching
model](https://nvie.com/posts/a-successful-git-branching-model/) by Vincent
Driessen, is a popular workflow for large projects.  It's especially useful
for software products that have many versions in the field at the same time.
There's even a Git subcommand, `flow`, for doing GitFlow-specific operations.
GitFlow uses the master branch for numbered releases, and a separate branch
for development.

Since this is a *small* project and you're already using `master` for
continuous integration into your main website, you decide to keep `master` as
it is and make a separate `release` branch:

```
$ git checkout -b release
$ git tag -a v0.1 -m "Start release branch"
$ git log --oneline -n2
$ git show v0.1
```

The `show` subcommand can be used to display the tag data along with the
commit it refers to; tags are also shown by `log` next to the commits they
refer to.

Git has two kinds of tags: "lightweight" and "annotated".  A lightweight tag
is just a file (`refs/tags/NAME`) containing the hash of the tagged commit.
Lightweight tags are primarily used as temporary labels; a typical use is to
tag the head of a branch before you rebase it, to make it easier to go back if
you ran into trouble.  Lightweight tags are almost always local to a
developer's copy of a repo.

Annotated tags, on the other hand, are objects that are very similar to
commits: they have a message, author, and optional signature.  Tags are not
normally pushed, but you can do it with the `--follow-tags` option:

```
$ git push --follow-tags
```

This option pushes all annotated tags that can be reached from the commits
being pushed.  If you always want this behavior, you can set the
`push.followTags` configuration option with

```
git config --global push.followTags true
```

There is an older option to `push`, `--tags`, which pushes *all* tags; this is
a bad idea because developers often pick the same names for their lightweight
tags. 


## Summary

In this unit, you have learned about Git hooks, which perform actions when
specific events occur, and the Git command

* `git tag`, which creates, deletes, or modifies tags.


