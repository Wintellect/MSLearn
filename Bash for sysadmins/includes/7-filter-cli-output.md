# Exercise: Use Bash and grep to filter Azure CLI output

While Bash is powerful in its own right, you can also use it to work with the Azure Cloud Shell. First, leave the Bash shell behind with the command: 

```bash
$ exit
```

Let's explore how you can use Bash and Linux's tools to work with the Azure Command Shell, with sysadmin examples.

Say you want to look at an up-to-date list of the available VM images. You do that with the command: 

```bash
$ az vm image list --all --output table
```

That's a lot of images.

While you can narrow down the list by filtering it with the `--publisher`, `--sku`, or `–-offer` options, you can also use `grep`, Linux's universal pattern matching program, to find exactly what you're looking for.

So, to find the image for a CentOS, a popular Red Hat Enterprise Linux clone, use the following command.

```bash
$ az vm image list --all --output table | grep CentOS
```

This pipes the output from the Azure Command Shell to `grep`'s input. `grep` then looks for the string "CentOS" and lists just the CentOS images.

Another way to use these commands to explore the system to to discover detailed information about a specific virtual machine by name or ID. For this, you'd use the command:

```bash
$ az vm show --resource-group 'Northwind --name Northwind
```

That gives you a lot of information in JSON, the Azure Command Shell's default output format, which can be difficult to read.

But, perhaps all you really wanted to know was the VM's public key. For that, just run this command, which also pipes piping the output through grep. 

```bash
$ az vm show --resource-group 'Northwind --name Northwind | grep rsa
```

We see instead of a mass of JSON, a single line containing the SSH public key. Handy, eh?

Or let's say you want to know the names of all your VMs. We could run the `az` command with the `--query` flag to filter results and pick a subset of properties from the dataset. For instance, to see only the type and name of the resources in your subscriptions, you could use the command:

```bash
$ az resource list --query '[].{name:name, type:type}' -o tsv
```

That done, say you wanted to know the name of your VMs in your subscriptions. For that, just run the command and pipe it through `grep`:

```bash
$ az resource list --query '[].{name:name, type:type}' -o tsv | grep virtualMachine
```

And, there you have it. A list of your VMs. 

Of course, you can do much more by marrying the Azure Command Shell with Bash. But you've got your feet wet and are ready to start learning more. 