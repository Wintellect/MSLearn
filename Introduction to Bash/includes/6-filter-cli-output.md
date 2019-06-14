# Exercise: Use Bash and grep to filter Azure CLI output

Up until now, you have been running Bash commands in a Linux VM. That's a great way to practice Bash commands because you can't do any harm. If something goes terrible awry, you can delete the VM and start all over again.

You can also execute Bash commands in the Azure Cloud Shell. The drop-down list in the uper-left corner of the Cloud Shell lets you choose between two languages: PowerShell and Bash. The same Bash commands that make it easy to work with Linux can also be used with the Azure CLI (`az`) commands used to create and manage Azure resources. Let's demonstrate by disconnecting from the VM and returning to the Cloud Shell.

1. First, return to the Cloud Shell by running the following command in the VM: 

	```bash
	exit
	```

1. Make sure **Bash** is selected in the upper-left corner of the Cloud Shell. Let's say you want to see an up-to-date list of the VM images available in Azure. Do that with the command: 

	```bash
	az vm image list --all --output table
	```

	That's a lot of images.

1. While you can narrow the list using the `--publisher`, `--sku`, or `–-offer` options, you can also use `grep`, Linux's universal pattern matching program, to find what you're looking for. To find the images for CentOS, a popular Red Hat Enterprise Linux (RHEL) clone, use the following command:

	```bash
	az vm image list --all --output table | grep CentOS
	```

	This pipes output from the `az` command to `grep`, which filters out lines that lack the string "CentOS."

1. Now use the following command to list information about the VM that you created:

	```bash
	az vm show --resource-group bash-vm-rg --name bash-vm
	```

	Once more, that's a lot of output — this time in [JavaScript Object Notation](https://en.wikipedia.org/wiki/JSON) (JSON) format.

1. Perhaps what you really wanted to know was what operating system the VM is running. See if this makes it easier: 

	```bash
	az vm show --resource-group bash-vm-rg --name bash-vm | grep osType
	```

Applying what you know about Bash to the Azure Cloud Shell makes the latter easier to work with. And given that a sysadmin's work never ends, any tool that reduces the workload is a welcome tool indeed.