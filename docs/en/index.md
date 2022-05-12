# Welcome to Advanced Analytics Workspace (AAW)

Please find below additional information, videos and links to help better
understand how to get started with Advanced Analytics Workspace (AAW).

Advanced Analytics Workspace (AAW) is our **_open source platform for data
science and machine learning (ML)_** for **advanced practitioners** to get their
work done in an **unrestricted environment** made by data scientists _for_ data
scientists. With AAW, you can customize your notebook deployments to suit your
data science needs. We also have a small number of expertly crafted images made
by our expert data science team.

![Getting Started](images/banner.png)

AAW is based on the Kubeflow project which is an open source comprehensive
solution for deploying and managing end-to-end ML workflows. Kubeflow is
designed to make deployments of ML workflows on **Kubernetes** simple, portable
and scalable.

🔔 **Important!** Users external to Statistics Canada will require a cloud
account granted access by the business sponsor.

🔔 **Important!** Users internal to Statistics Canada can get started right away
without any additional sign up procedures, just head to
[https://kubeflow.aaw.cloud.statcan.ca/](https://kubeflow.aaw.cloud.statcan.ca/).

## AAW Services

The Advanced Analytics Workspaces' services can be accessed from one of two portals.

<div class="grid" markdown>

- [![Analysis](images/portal-external.png)](https://analytics-platform.statcan.gc.ca/covid19) <br> [**External**](https://analytics-platform.statcan.gc.ca/covid19){ .md-button .md-button--primary }
- [![Getting Started](images/portal-internal.png)](https://www.statcan.gc.ca/data-analytics-service/aaw) <br> [**Internal**](https://www.statcan.gc.ca/data-analytics-service/aaw){ .md-button }

</div>


## Getting Help

https://statcan.github.io/daaas/
https://statcan-aaw.slack.com


<div class="grid cards" markdown>

  - __HTML__ for content and structure
  - __JavaScript__ for interactivity
  - __CSS__ for text running out of boxes
  - __Internet Explorer__ ... huh?

</div>

## Getting Started

In order to access the AAW services, you will need to:

1. Login to [Kubeflow](https://kubeflow.aaw.cloud.statcan.ca/) with your StatCan
   guest cloud account. You will be prompted to authenticate the account.
2. Select Notebook Servers.
3. Click the "➕ New Server" button.

## Tools Offered

AAW is a flexible platform for data analysis and machine learning, featuring:

- Languages: Python, R, Julia, SAS
- Development environments: VS Code, R Studio, Jupyter Notebooks
- Linux virtual desktops for additional tools: OpenM++, QGIS

## Demos

If you would like a quick Onboarding Demo session or require any help or have
any questions, please do not hesitate to reach out through our
[Slack Support Channel](https://statcan-aaw.slack.com).

## FAQ

- Frequently Asked Questions are located
  [here](https://github.com/StatCan/daaas/blob/master/README.md).

Thank you!


# Starting on the Advanced Analytics Workspace

The
**[Advanced Analytics Workspace portal](https://analytics-platform.statcan.gc.ca/)**
is a great place to discover and connect to the available resources we'll be
talking about here.

## What are you looking for?

<center>

| Tools and Services | | |
|---|---|---|
| <center><h3> [![Getting Started](images/GettingStarted.PNG)](#gettingstarted) <br> [Getting Started](#gettingstarted) </h3></center> | <center><h3> [![Analysis](images/Analysis.PNG)](#experiments) <br> [Data Analysis](#experiments) </h3></center> | <center><h3> [![Publishing](images/Publishing.PNG)](#publishing) <br> [Data Publishing](#publishing) </h3></center> |
| <center><h3> [![Pipelines](images/Pipelines.PNG)](#pipelines) <br> [Kubeflow Pipelines](#pipelines) </h3></center> | <center><h3> [![Collaboration](images/Collaboration.PNG)](#collaboration) <br> [Collaboration](#collaboration) </h3></center> | <center><h3> [![Storage](images/Storage.PNG)](#storage) <br> [Storage](#storage) </h3></center> |

</center>

# Get Started with AAW

[![Set up Kubeflow](images/Kubeflow.PNG)](1-Experiments/Kubeflow/)

Everything starts with **[Kubeflow](1-Experiments/Kubeflow/)**! Start by setting it up.

[![Ask questions on Slack](images/Slack.PNG)](https://statcan-aaw.slack.com/)

You're going to have questions. Join our **[Slack channel](https://statcan-aaw.slack.com/)** so we can get you answers!
[![A screenshot of the slack page. In the top right-hand corner is a link to create a new account](images/SlackAAW.PNG)](https://statcan-aaw.slack.com/)

Click on the link, then choose "Create an account" in the upper right-hand corner.

[![A screenshot of the next page, with a box to use your @canada.ca email](images/SlackAAW2.PNG)](https://statcan-aaw.slack.com/)

Use your @canada.ca email address so that you will be automatically approved.

# Experiments

## Process data using `R`, `Python`, or `Julia`

[![R, Python, or Julia in Jupyter notebooks](images/Jupyter.PNG)](1-Experiments/Jupyter.md)
Once you have Kubeflow set up, use
**[Jupyter Notebooks](1-Experiments/Jupyter.md)** to create and share documents
that contain live code, equations, or visualizations.
![Jupyter Notebooks](images/jupyter_in_action.png)

## Process data using 'R' or 'Python'

[![R or Python in R Studio](images/RStudio.PNG)](1-Experiments/RStudio.md)
**[R Studio](1-Experiments/RStudio.md)** gives you an integrated development
environment for R and Python. Use the r-studio-cpu image to get an R Studio
environment.

## Run a virtual desktop

[![Virtual Desktop](images/VirtualDesktop.PNG)](1-Experiments/Remote-Desktop.md)
You can run a full Ubuntu desktop, with typical applications, right inside your
browser, using [**ML Workspaces**](1-Experiments/Remote-Desktop.md)

# Publishing

## Build and publish an interactive dashboard

[![InteractiveDashboard](images/InteractiveDashboard.PNG)](/2-Publishing/R-Shiny/)
Use **[R-Shiny](/2-Publishing/R-Shiny/)** to build interactive web apps straight
from R. You can deploy your R-Shiny dashboard by submitting a pull request to
our [R-Dashboards GitHub repository](https://github.com/StatCan/R-dashboards).
![R Shiny Server](images/readme/shiny_ui.png)

**[Dash](/2-Publishing/Dash/)** is a data visualization tool that lets you build
an interactive GUI around your data analysis code.

## Explore your data

[![Explore your data](images/ExploreData.PNG)](/2-Publishing/Datasette/) Use
**[Datasette](/2-Publishing/Datasette/)** , an instant JSON API for your SQLite
databases. Run SQL queries in a more interactive way!

# Pipelines

## Build and schedule data/analysis pipelines

[![Build Piplines](images/BuildPipelines.PNG)](/3-Pipelines/Kubeflow-Pipelines/)
**[Kubeflow Pipelines](/3-Pipelines/Kubeflow-Pipelines/)** allows you to set up
pipelines. Each pipeline encapsulates analytical workflows, and can be shared,
reused, and scheduled.
![Kubeflow Pipelines](images/readme/kubeflow_pipeline.png)

[![Integrate with PaaS](images/IntegratePaaS.PNG)]()

## Integrate with Platform as a Service (PaaS) offerings

We can integrate with many Platform as a Service (PaaS) offerings, like
Databricks or AzureML.

# Collaboration

There are many ways collaborate on the platform. Which is best for your
situation depends on what you're sharing and how many people you want to share
with. See the [Collaboration Overview](4-Collaboration/Overview.md) for details.

Content to be shared breaks roughly into **Data**, **Code**, or **Compute
Environments** (e.g.: sharing the same virtual machines) and who you want to
share it with (**No one**, **My Team**, or **Everyone**). This leads to the
following table of options

|             |           **Private**            |                  **Team**                  |  **StatCan**  |
| :---------: | :------------------------------: | :----------------------------------------: | :-----------: |
|  **Code**   | GitLab/GitHub or personal folder |        GitLab/GitHub or team folder        | GitLab/GitHub |
|  **Data**   |    Personal folder or bucket     | Team folder or bucket, or shared namespace | Shared Bucket |
| **Compute** |        Personal namespace        |              Shared namespace              |      N/A      |

<!-- prettier-ignore -->
??? question "What is the difference between a bucket and a folder?"
    Buckets are like Network Storage. See the [Storage section](#storage) section for more discussion of the differences between these two ideas.

Sharing code, disks, and workspaces (e.g.: two people sharing the same virtual
machine) is described in more detail in the
[Collaboration](4-Collaboration/Overview.md) section. Sharing data through
buckets is described in more detail in the **[MinIO](./5-Storage/MinIO.md)**
section.

# Storage

The platform provides several types of storage:

- Disk (also called Volumes on the Notebook Server creation screen)
- Bucket ("Blob" or S3 storage, provided through MinIO)
- Data Lakes (coming soon)

Depending on your use case, either disk or bucket may be most suitable. Our
[storage overview](./5-Storage/Overview.md) will help you compare them.

## Disks

[![Disks](images/Disks.PNG)](Storage.md/) **[Disks](./5-Storage/Disks.md)** are
added to your notebook server by adding Data Volumes.

## Buckets

[![MinIO](images/Buckets.PNG)](MinIO.md/) **[MinIO](./5-Storage/MinIO.md)** is a
cloud-native scalable object store. We use it for buckets (blob or S3 storage).
