# Starting on the Advanced Analytics Workspace

The
**[Advanced Analytics Workspace portal](https://portal.covid.cloud.statcan.ca)**
is a great place to discover and connect to the available resources we'll be
talking about here.

## What are you looking for?

[![Getting Started](images/GettingStarted.PNG)](#get-started-with-aaw)

[![Analysis](images/Analysis.PNG)](#experiments)
[![Publishing](images/Publishing.PNG)](#publishing)
[![Pipelines](images/Pipelines.PNG)](#pipelines)
[![Collaboration](images/Collaboration.PNG)](#collaboration)
[![Storage](images/Storage.PNG)](#storage)

# Get Started with AAW

[![Set up Kubeflow](images/Kubeflow.PNG)](1-Experiments/Kubeflow/) Everything
starts with **[Kubeflow](1-Experiments/Kubeflow/)**! Start by setting it up.

[![Ask questions on Slack](images/Slack.PNG)](https://statcan-aaw.slack.com/)
You're going to have questions. Join our
**[Slack channel](https://statcan-aaw.slack.com/)** so we can get you answers!
<img src="images/SlackAAW.PNG" alt="A screenshot of the slack page. In the top right-hand corner is a link to create a new account" width="50%">

Click on the link, then choose "Create an account" in the upper right-hand
corner.
<img src="images/SlackAAW2.PNG" alt="A screenshot of the next page, with a box to use your @canada.ca email" width="50%">

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
