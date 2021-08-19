# Setting up your Cloud VM

This Guide is for creating a Windows VM. Then, installing WSL2 to run a Linux
environment and installing Xfce as a GUI for the Linux environment. **You will
need your work laptop for the following steps.**

## Getting your VM Created

You will need to create a Jira issue to get your VM created. Use
[this issue](https://jirab.statcan.ca/browse/CLOUD-9807)(open link on work laptop) as a template. Note that the WID Number in the JIRA issue stands for the Workload ID which you need to provide for billing of your project.

<!-- prettier-ignore -->
!!! Caution
    Double-check with your supervisor on the size of the VM

## Connecting to your VM

Once your VM is created, you will receive an email on how to connect to it;
follow those steps.

<!-- prettier-ignore -->
!!! Tip
    Consider saving your Remote Desktop Connection to your Desktop, using the Connection Settings > Save As...

## Using Multiple Monitors

### To display your VM on all your monitors

- Open the Remote Desktop Connection Application
- Go to the Display Tab
- Check _Use all my monitors for the remote session_ in Display configuration
- Go back to the General Tab and save the file to your Desktop
- If you open that new Remote Desktop Connection file, your VM should display on
  all your monitors

### To display your VM on specific monitors

- Run `mstsc /l` to see your monitors
  - run the command in your Command Prompt, paste it into Start > Search, or use
    the Run Desktop App
- Decide which monitors you want to display your VM on
  ![Placeholder](images/monitors.png)
- Open the Remote Desktop Connection file using NotePad
- Add the following line into the file, replacing the numbers with whatever
  monitors you decide to use

```
selectedmonitors:s:7,6
```

<img src="../images/specificmonitors.png" width="400"/>

## Installing your Linux Distribution

- Install [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
  - Complete the Manual Install
  - Be sure to run PowerShell as an Administrator
  - If you run into an error on wsl_update_x64.msi being unable to run try
    restarting your VM or follow some of the solutions
    [here](https://github.com/microsoft/WSL/issues/5035)

## Installing Xfce4

- Use
  [this guide](https://autoize.com/xfce4-desktop-environment-and-x-server-for-ubuntu-on-wsl-2/)
- Take a look at Step 3 of
  [this guide](https://github.com/StatCan/daaas/issues/540)
- Go to "Window Manager Tweaks" in XFCE and disable the compositor. The UI will be much faster.

## Setting up Your Dev Environment

- Install some common kubernetes tools with [this makefile](https://gist.github.com/blairdrummond/c147d67f78028f84f8b56a57dea337b5) (first do `sudo apt install jq make wget curl`)

- Setup Docker on Windows using
  [this guide](https://docs.docker.com/docker-for-windows/wsl/)
- Install VSCode
  - Get the
    [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
    extension
  - Get
    [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

<!-- prettier-ignore -->
!!! Tip
    Set your default formatter to Prettier, and consider turning on the setting for **format on save**
