# Overview

## What does Kubeflow do?

Kubeflow runs your **workspaces**. You can have notebook servers (called Jupyter
Servers), and in them you can create analyses in R and Python with interactive
visuals. You can save and upload data, download it, and create shared workspaces
for your team.

![Kubeflow Manages the Jupyter Servers](../images/jupyter_visual.png)

**Let's get started!**

# Video Tutorial

[![Click here for the video](../images/KubeflowVideo.PNG)](https://www.youtube.com/watch?v=xaI6ExYdxc4&list=PL1zlA2D7AHugkDdiyeUHWOKGKUd3MB_nD&index=1 "Advanced Analytics Workspace - Kubeflow Getting Started")

# Setup

## Log into Kubeflow

<!-- prettier-ignore -->
??? warning "Log into the Azure Portal using your Cloud Credentials"
    You have to login to the azure portal **using your StatCan credentials**.
    `first.lastname@cloud.statcan.ca`. You can do that using
    [the Azure portal](https://portal.azure.com).
    ![Azure Portal: Choose the `@cloud.statcan.ca` address](../images/azure-login.png)

- Log into [Kubeflow](https://kubeflow.covid.cloud.statcan.ca)

- Navigate to the Notebook Servers tab

![Kubeflow Manages the Jupyter Servers](../images/readme/kubeflow_ui.png)

- Then click **+ New Server**

## Configuring your server

- You will get a template to create your notebook server. **Note:** the name of
  your server must be lowercase letters with hyphens. **No spaces, and no
  underscores.**

- You'll need to choose an image. Check the name of the images and choose one
  that matches what you want to do.

![Choose an Image](../images/kubeflow_choose_an_image.png)

- If you want to use a GPU, check if the image says `cpu` or `gpu`.

## CPU and Memory

- At the time of writing (April 21, 2020) there are two types of computers in
  the cluster

  - **CPU:** `D16s v3` (16 CPU cores, 64 GiB memory)
  - **GPU:** `NC6s_v3` (6 CPU cores, 112 GiB memory, 1 GPU)

  Because of this, if you request too much RAM or too many CPUs, it may be hard
  or impossible to satisfy your request.

  In the future (possibly when you read this) there may be larger machines made
  available, so you may have looser restrictions.

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
  take a few minutes to spin up depending on the resources you asked for. (GPUs
  take longer.)

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
