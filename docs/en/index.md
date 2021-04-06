# Starting on the Advanced Analytics Workspace (AAW)

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

# Get Started with AAW

[![Set up Kubeflow](images/Kubeflow.PNG)](1-Experiments/Kubeflow/)
Everything starts with
**[Kubeflow](1-Experiments/Kubeflow/)**!
Start by setting it up. 

[![Ask questions on Slack](images/Slack.PNG)](https://statcan-aaw.slack.com/)
You're going to have questions. Join our 
**[Slack channel](https://statcan-aaw.slack.com/)** 
so we can get you answers! 
<img src="images/SlackAAW.PNG" alt="A screenshot of the slack page. In the top right-hand corner is a link to create a new account" width="50%">

Click on the link, then choose "Create an account" in the upper right-hand corner. 
<img src="images/SlackAAW2.PNG" alt="A screenshot of the next page, with a box to use your @canada.ca email" width="50%">

Use your @canada.ca email address so that you will be automatically approved. 


# Experiments

## Process data using Notebook Servers

Within [Kubeflow](1-Experiments/Kubeflow/), **[Notebook Servers](1-Experiments/Jupyter/)** are how you get an interactive compute environment to process data.  All Notebook Servers have access to up to 15CPU/48GB RAM and GB/TB scale storage, but have a different user interface depending on the flavor you choose.

* Python, Julia, and R through **Jupyter Notebooks**
* R through **RStudio**

### Jupyter Notebooks for `Python`, `Julia`, or `R`

Use (Jupyter Notebooks)[https://jupyter.org/] to create and share interactive documents that contain a mix of live code, visualizations, and text.  These can be written in `Python`, `Julia`, or `R`.  

![Jupyter Notebooks](images/jupyter_in_action.png)

To start a Notebook Server with the Jupyter Notebook interface, choose any `jupyterlab` image when creating your Notebook Server.  The `jupyterlab` image also comes pre-loaded with VS Code in the browser if you prefer a full IDE experience.

### RStudio for `R` and `Shiny`

**[RStudio](1-Experiments/RStudio/)**
gives you an integrated development environment specifically for R. If you're coding in R, this is typically the Notebook Server to use.  Use the `rstudio` image to get an RStudio environment.

**TODO: Add image showing RStudio?  Take from the 1-Experiments/RStudio/ page?**

### Virtual Desktop for General Computing Needs

For a full Ubuntu desktop experience, use any [remote-desktop](1-Experiments/ML-Workspaces) Notebook Server.  These come pre-loaded with Python and R, but are delivered in a typical desktop experience that also comes with Firefox, VS Code, and open office tools.  If you need Geomatics tooling for R, choose the `remote-desktop-geomatics` flavor of this image.

**TODO: Add image showing Virtual Desktop?  Take from the 1-Experiments/ML-Workspaces/ page?**

# Publishing

## Build and publish an interactive dashboard

[![InteractiveDashboard](images/InteractiveDashboard.PNG)](/2-Publishing/R-Shiny/)
Use 
**[R-Shiny](/2-Publishing/R-Shiny/)** 
to build interactive web apps straight from R. You can deploy your R-Shiny dashboard by submitting a pull request to our
[R-Dashboards GitHub repository](https://github.com/StatCan/R-dashboards).
![R Shiny Server](images/readme/shiny_ui.png)

**[Dash](/2-Publishing/Dash/)** is a data visualization tool that lets you build an interactive GUI around your data analysis code.

## Explore your data


[![Explore your data](images/ExploreData.PNG)](/2-Publishing/Datasette/)
Use 
**[Datasette](/2-Publishing/Datasette/)**
, an instant JSON API for your SQLite databases. Run SQL queries in a more interactive way!

# Pipelines

## Build and schedule data/analysis pipelines
[![Build Piplines](images/BuildPipelines.PNG)](/3-Pipelines/Kubeflow-Pipelines/)
**[Kubeflow Pipelines](/3-Pipelines/Kubeflow-Pipelines/)** allows you to set up pipelines. Each pipeline encapsulates analytical workflows, and can be shared, reused, and scheduled.
![Kubeflow Pipelines](images/readme/kubeflow_pipeline.png)

[![Integrate with PaaS](images/IntegratePaaS.PNG)]()
## Integrate with Platform as a Service (PaaS) offerings
We can integrate with many Platform as a Service (PaaS) offerings, like Databricks or AzureML.

# Collaboration
## Share code among team members

[![Share Code](images/ShareCode.PNG)](/Collaboration/)
Use GitHub or GitLab to share code, or request a 
**[shared workspace](/Collaboration/)**
.

<!-- prettier-ignore -->
!!! tip "Ask for help in production"
    The Advanced Analytics Workspace support staff are happy to help with
    production oriented use cases, and we can probably save you lots of time.
    Don't be shy to [ask us for help](Help)!

# How do I get data? How do I submit data?

- Every workspace can be equipped with its own storage.

- There are also storage buckets to publish datasets; either for internal use or
  for wider release.

We will give an overview of the technologies here, and in the next sections
there will be a more in-depth description of each of them.

<!-- prettier-ignore -->
!!! example "Browse some datasets"
    Browse some [datasets](https://datasets.covid.cloud.statcan.ca) here. These
    data sets are meant to store widely shared data. Either data that has been
    brought it, or data to be released out as a product. **As always, ensure
    that the data is not sensitive.**
