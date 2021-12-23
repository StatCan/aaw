# Overview

## What does Kubeflow do?

Kubeflow runs your **workspaces**. You can have notebook servers (called Jupyter
Servers), and in them you can create analyses in R and Python with interactive
visuals. You can save and upload data, download it, and create shared workspaces
for your team.

![Kubeflow Manages the Jupyter Servers](../images/jupyter_visual.png)

**Let's get started!**

# Video Tutorial

<!-- prettier-ignore -->
!!! note ""
    This video is not up to date, some things have changed since.

[![Click here for the video](../images/KubeflowVideo.PNG)](https://www.youtube.com/watch?v=xaI6ExYdxc4&list=PL1zlA2D7AHugkDdiyeUHWOKGKUd3MB_nD&index=1 "Advanced Analytics Workspace - Kubeflow Getting Started")

# Setup

## Log into Kubeflow

<!-- prettier-ignore -->
??? warning "Log into the Azure Portal using your Cloud Credentials"
    You have to login to the Azure Portal **using your StatCan credentials**.
    `first.lastname@cloud.statcan.ca` or **StatCan credentials**
    `first.lastname@statcan.gc.ca`. You can do that using
    [the Azure Portal](https://portal.azure.com).
    ![Azure Portal: Choose the `@cloud.statcan.ca` address](../images/azure-login.png)

- Log into [Kubeflow](https://kubeflow.aaw.cloud.statcan.ca)

- Navigate to the Notebook Servers tab

![Kubeflow Manages the Jupyter Servers](../images/readme/kubeflow_ui.png)

- Then click **+ New Server**

## Configuring your server

- You will get a template to create your notebook server. **Note:** the name of
  your server must be lowercase letters with hyphens. **No spaces, and no
  underscores.**

- You'll need to choose an image. Check the name of the images and choose one
  that matches what you want to do. (Don't know which one to choose? Check out
  your options [here](./Selecting-an-Image.md).)

![Choose an Image](../images/kubeflow_choose_an_image.png)

- If you want to use a GPU, check if the image says `cpu` or `gpu`.

## CPU and Memory

- At the time of writing (December 23, 2021) there are two types of computers in
  the cluster

  - **CPU:** `D16s v3` (16 CPU cores, 64 GiB memory; for user use 15 CPU cores
    and 48 GiB memory are available; 1 CPU core and 16 GiB memory reserved for
    system use).
  - **GPU:** `NC6s_v3` (6 CPU cores, 112 GiB memory, 1 GPU; for user use 96 GiB
    memory are available; 16 GiB memory reserved for system use).

  When creating a notebook server, the system will limit you to the maximum
  specifications above. For CPU notebook servers, you can specify the exact
  amount of CPU and memory that you require. This allows you to meet your
  compute needs while minimising cost. For a GPU notebook server, you will
  always get the full server (6 CPU cores, 96 GiB accessible memory, and 1 GPU).

  In the future there may be larger machines available, so you may have looser
  restrictions.

<!-- prettier-ignore -->
!!! note "Use GPU machines responsibly"
    There are fewer GPU machines than CPU machines, so use them responsibly.

## Storing your data

- You'll want to create a data volume! You'll be able to save your work here,
  and if you shut down your server, you'll be able to just remount your old data
  by entering the name of your old disk. **It is important that you remember the
  volume's name.**

![Create a Data Volume](../images/kubeflow_volumes.png)

<!-- prettier-ignore -->
!!! tip "Check for old volumes by looking at the Existing option"
    When you create your server you have the option of reusing an old volume
    or creating a new one. You probably want to reuse your old volume.

## And... Create!!!

- If you're satisfied with the settings, you can now create the server! It may
  take a few minutes to spin up depending on the resources you asked for. GPUs
  take longer.

<!-- prettier-ignore -->
!!! note "Slow node creation bug."
    Due to a bug with the firewall, creating a new node may be very
    slow in some cases (up to a few hours). A fix for this issue is in the works.

<!-- prettier-ignore -->
!!! success "Your server is running"
    If all goes well, your server should be running!!! You will now have the
    option to connect, and [try out Jupyter!](/daaas/en/1-Experiments/Jupyter)

# Once you've got the basics ...

## Share your workspace

In Kubeflow every user has a **namespace** that contains their work (their
notebook servers, pipelines, disks, etc.). Your namespace belongs to you, but
can be shared if you want to collaborate with others. **For more details on
collaboration on the platform, see
[Collaboration](../4-Collaboration/Overview.md).**
