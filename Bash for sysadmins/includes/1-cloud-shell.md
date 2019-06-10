# Set up a Linux VM and Bash on Azure Cloud Shell

On your own Linux computer, you just start Bash from the command line. But nobody wants to experiment on a live production system — particularly on your first day at Northwind!

For this module, we use an Azure-based Linux virtual machine (VM) as a sandbox. That lets you see what happens when you type in each command.

## Launch Azure Cloud Shell

The Azure Cloud Shell is a free interactive shell that you can use to run the steps in this module. It has common Azure tools pre-installed and configured to use with your account. 

To set up your Linux VM, use the instructions in [Create and Manage Linux VMs with the Azure CLI](https://docs.microsoft.com/azure/virtual-machines/linux/tutorial-manage-vm). Note that from within this Bash shell you can also work with the Azure CLI commands, by prefacing them with `az`. This lets you use the power of both interfaces. As you'll see later, this empowers you to use both Bash and Azure from the interface.

Once you create the Ubuntu Linux VM, the next step is to arrange things so you can securely log into it with an ssh client or from within the Azure Cloud Shell.

To do this, you use `ssh`, also known as "Secure Shell" or "Secure Socket Shell." It is the default network security protocol, and it enables you to securely into a system over an unsecured network. The name `ssh` also refers to the programs you run that permit you to use SSH to make these secure connections.

To connect safely and securely with a Linux-based VM, you need an SSH client client such as [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/), the popular free Windows-based SSH client.

TODO: Mention Windows Subsystem for Linux.

To securely work with your Azure VM, start here: 
- In the VM blade of the Azure portal, select the VM to which you want to connect.
- Start the VM, if it is not already running.
- Click on the VM’s name to open its overview page.
- Note the VM’s public IP address and DNS name. (If these values are not set, then you must create a network interface.)
- Open PuTTY.
- In the PuTTY configuration dialog, enter your VM's IP address or DNS name.
- Click open to start a terminal session.
- When prompted, enter your VM account name and password.

You can also login to your VM using ssh from within the Azure Cloud Shell by using its built-in ssh functionality by taking the following steps: 
- In the Azure portal search bar, search for your VM name.
- When you find it, click on the VM. This shows an overview of its settings.
- Click Connect to get your VM login name and public IP address.
- Copy the command listed under the “Login using VM local account” label to your clipboard. 
- In the Azure Cloud Shell Bash command line, paste and enter this command. 

This securely logs you into your Ubuntu shell.

For this purpose, you don't need a password, because you generated an ssh key pair when you created the VM. The key pair does two things: It logs you into the system and it secures your connection to the VM. When you first use ssh, the client prompts about the host's authenticity. Answering “yes” saves the IP address as a valid host for an ssh connection and completes the connection.

<INSERT: Azure Command Shell ssh Login.png>

Once you're in the Ubuntu shell, you can no longer access the Azure Command Shell, but you are free to start working with your Linux VM. To tell the difference between the two shells, look to their prompts:

- The Azure Command Shell reads `<user name>@Azure:~$` 
- The Linux prompt shows as `<user name>@<your Ubuntu VM name>:~$`

For example: 

```
buddy@Azure:~$
buddy@Northwind:~$
```

Now that everything is set up, in the next unit, you learn the concepts underlying the Bash shell and how to get started using it.