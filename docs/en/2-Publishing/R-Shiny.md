# Overview

R-Shiny is an R package that makes it easy to build interactive web apps in R. 

!!! info "R Shiny App Hosting"
    We currently do not support hosting R Shiny apps but you are able to create them. We want to enable R Shiny app hosting in the future.

![Shiny Homepage](../images/readme/shiny_ui.png)

### R Shiny

_Publish Professional Quality Graphics_

[![InteractiveDashboard](../images/InteractiveDashboard.PNG)](/2-Publishing/R-Shiny/)

R Shiny is an open source web application framework that allows data scientists and analysts to create interactive, web-based dashboards and data visualizations using the R programming language. One of the main advantages of R Shiny is that it offers a straightforward way to create high-quality, interactive dashboards without the need for extensive web development expertise. With R Shiny, data scientists can leverage their R coding skills to create dynamic, data-driven web applications that can be shared easily with stakeholders.

Another advantage of R Shiny is that it supports a variety of data visualizations that can be easily customized to meet the needs of the project. Users can create a wide range of charts and graphs, from simple bar charts and scatter plots to more complex heatmaps and network graphs. Additionally, R Shiny supports a variety of interactive widgets that allow users to manipulate and explore data in real-time.

![R Shiny Server](../images/readme/shiny_ui.png)

R Shiny is also highly extensible and can be integrated with other open source tools and platforms to build end-to-end data science workflows. With its powerful and flexible features, R Shiny is a popular choice for building data visualization dashboards for a wide range of applications, from scientific research to business analytics. Overall, R Shiny offers a powerful, customizable, and cost-effective solution for creating interactive dashboards and data visualizations.

Use **[R-Shiny](/2-Publishing/R-Shiny/)** to build interactive web apps straight from R. You can deploy your R Shiny dashboard by submitting a pull request to our [R-Dashboards GitHub repository](https://github.com/StatCan/R-dashboards).

# Setup

## Just send a pull request!

All you have to do is send a pull request to
[our R-Dashboards repository](https://github.com/StatCan/R-dashboards). Include
your repository in a folder with the name you want (for example,
"air-quality-dashboard"). Then we will approve it and it will come online.

If you need extra R libraries to be installed, send your list to
[the R-Shiny repository](https://github.com/StatCan/shiny) by creating a GitHub
Issue and we will add the dependencies.

![Example Dashboard](../images/example_shiny_dashboard.png)

<!-- prettier-ignore -->
!!! example "See the above dashboard here"
    The above dashboard is in GitHub. Take a look at
    [the source](https://github.com/StatCan/R-dashboards/tree/master/bus-dashboard),
    and [see the dashboard live](https://shiny.covid.cloud.statcan.ca/bus-dashboard).

# Once you've got the basics ...

## Embedding dashboards into your websites

<!-- prettier-ignore -->
!!! failure "Embedding dashboards in other sites"
    We have not had a chance to look at this or prototype it yet, but if you
    have a use-case, feel free to reach out to engineering. We will work with
    you to figure something out.
