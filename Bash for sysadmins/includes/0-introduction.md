# Introduction

Imagine that you just started a new job as a system administrator (sysadmin) at Northwind, a small chain of cat boutiques for chubby felines. While you know Windows Server like the back of your hand, in the new position you also need to manage Linux servers. It's time to skill up.

A vital tool you must learn is [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)). The name stands for "Bourne Again SHell." 

A shell is a program that instructs the operating system to perform actions. It's meant to operate directly with the computer as a system, such as its file organization and network settings. You type directly onto the command line, or use stored files (scripts) to emulate someone typing on the keyboard. That's different from the commonplace graphical interface. Shells such as PowerShell and Bash give system administrators the power and precision they need to give them fine-tuned control of the computers for which they are responsible. 

If you do any serious sysadmin work with Linux, you must get to know Bash. While there are other Linux shells— csh, Korn shell, and zsh—Bash has become Linux's default shell. That's because bash is compatible with Unix's first serious shell, sh; it incorporates the best features of its predecessors. Bash includes its own built-in commands and can invoke external programs.

One reason for its success is its simplicity. Bash, like the rest of Linux, is based on the Unix design philosophy. As Peter Salus summarized in his book, [A Quarter Century of Unix](https://www.amazon.com/Quarter-Century-UNIX-Peter-Salus/dp/0201547775/ref=sr_1_1), the three fundamental ideas are:
- Programs do one thing and do it well
- Programs work together
- Programs use text streams as the universal interface

That last part is key to understanding how Bash works. In Unix and Linux, everything is a file. That means you can use the same commands without worrying about whether the I/O stream — the stream of characters — is connected to a keyboard, a disk file, a socket, a pipe, or another I/O abstraction.

Whatever you think of it personally, Bash is the command shell of choice for Linux users. As [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-6) is to Windows Server, so Bash is to Linux. It behooves you to gain at least a modicum of expertise using the shell.

Bash has many features. Since we're just getting started, we focus on a few commands and how to use them together.

First, though, we need to do a little system configuration.