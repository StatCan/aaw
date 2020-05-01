# Starting on the DAaaS Platform

![The DAaaS Platform](images/readme/portal_ui.png)

**Link to the portal [here](https://portal.example.ca)**

We'll break down the standard tasks into three categories

1. **Experimentation / Analysis**

2. **Publishing**

3. **Large scale production**

All are important, and we will address all of them, but we will place the most
emphasis on the first two, as these are most widely applicable. 

# For Experiments

<!--  ![Kubeflow](images/logo-kubeflow.png){: style="max-height:200px"} -->

## Jupyter notebooks

 - `R` and `Python`, along with whatever other languages you might need.
 
 - The machines can be as big as you need. They're for large analyses.
 
 - You can easily share your workspace with your team, and share data and
   notebooks.

![Jupyter Notebooks](images/jupyter_in_action.png)

## Desktops with ML-Workspace

   Notebooks are more easily shared than desktops, but we also have the ability
   to run Desktop applications (like QGIS, or VS-Code) in a browser. 

[**Learn More**](1-Experiments/1-Kubeflow)

# For Publishing

## R Shiny

![R Shiny](images/logo-RStudio.png){: style="max-height:100px; display: block; margin-left: auto; margin-right: auto;"}

The platform is designed to host any kind of open source application you want.
We have an R-Shiny server for hosting R-Shiny apps

 ![R Shiny Server](images/readme/shiny_ui.png)
 
To create any an R-Shiny Dashboard, you just have to submit a Github Pull
request to the [Statcan Github](https://github.com/statcan/shiny). 
 
## NodeJS, Flask

![NodeJS Dashbaords](images/readme/covid_ui.png){: style="max-height:400px; display: block; margin-left: auto; margin-right: auto;"}

You can also create custom apps. For example:
 
 - Flask 
 - Dash
 - NodeJS or any other Open Source app in a Docker container

!!! example "See an example NodeJS app we have"
    The NodeJS pictured above can be found
    [here](https://covid19.example.ca). This app is in [the Statcan
    Github Repo](https://github.com/statcan/covid19). In the same way, you can
    submit your own custom apps and we can host them on the platform.


To create any any of these, create an issue on the 
[Statcan Github](https://github.com/statcan/daaas) asking for help, 
and we will add your application.


# For Production

If an experiment turns into a product, then one of the following may be needed:

 - Kubeflow pipelines for high-volume/intensity work
 - Automation pipelines
 
![Kubeflow Pipelines](images/readme/kubeflow_pipeline.png)

!!! tip "Ask for help in production."
    The DAaaS engineers are happy to help with production oriented use
    cases, and they can probably save you lots of time. Don't be shy to
    ask them for help!

# How do I get data? How do I submit data?

![Browse Datasets](images/readme/minio_ui.png)

 - Every workspace can be equipped with its own storage.

 - There are also storage buckets to publish datasets too; either for
   internal use or for wider release.

We will give an overview of the technologies here, and in the next sections
there will be a more in-depth FAQ of each of them. 

!!! example "Browse some datasets"
    Browse some [datasets](https://datasets.example.ca) here. These
    data sets are meant to store widely shared data. Either data that has been
    brought it, or data to be released out as a product. **As always, ensure
    that the data is not sensitive.**



