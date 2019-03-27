# Collaborate using a shared repo

When Bob decides to join the project as well, you realize that it would help
if there was an "official" copy of the project that you can all share.  This
will also come in handy when the website goes live, because the server will be
able to pull from it too.

* `git clone --bare project project.git`
* `git clone project.git Bob` (briefly mention ssh at this point; we don't
  need that complication right now, but we'll be using it in the next module.)
* You and Alice want to be able to pull from the shared repo instead of from
  each other.  Alice's repo already has an origin, so she can use
  `git remote --set-url origin ../project.git`
* It's a little more complicated for you. `git remote origin ../project.git`
  When you try to push, git asks which branch.  reply with "master"
  You eliminate that question for future uploads with
  `git branch --set-upstream-to origin` -- doesn't work before the
  master branch is actually pushed.
* pull before push.  (Alice and Bob both make changes.  Alice pushes first,
  so Bob has to `git pull --rebase; git push`  (more about rebase later)
