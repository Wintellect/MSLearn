# Collaborate using pull

As work on the website progresses one of your coworkers, Alice, offers to help
you write some of the content.  She will need to make a copy of your project,
and send her changes to you as she makes them.  This is where `git`'s
_distributed_ nature comes in.

## Alice clones your project

Instead of making an empty directory and running `git init` to initialize it,
Alice uses `git clone` copy your repo.  In this section, we'll use a directory
to hold Alice's copy of the `Website` project.  You're probably in the Website
project directory, so you'll want to change to the parent directory first.

```
$ cd ..
$ mkdir Alice
$ cd Alice
$ git clone ../Website
$ cd Website
```

Alice will need to configure Git with her name and email address.  Since she's
working using your account (which is very bad from a security point of view,
but she can get away with it because she doesn't really exist) she will have
to use local configuration variables for this:

```
$ git config user.name Alice
$ git config user.email alice@example.com
```

* commit some changes in Alice's directory.
* pull from Alice. `git pull ../Alice`
* Make changes in both your tree and Alice's.
* Alice: `git pull` -- she has an origin remote; you don't.
  alice blue: 	#F0F8FF body { background-color:  #F0F8FF; } 
