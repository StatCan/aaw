# Welcome to the Advanced Analytics Workspace

<center>
![Statistics](images/statistics-on-the-moon.jpg)
</center>

## The Advanced Analytics Workspace Documentation

_Welcome to the world of data science and machine learning!_

<!-- prettier-ignore -->
!!! info "What is the AAW?"
    **[Advanced Analytics Workspace](https://analytics-platform.statcan.gc.ca/)** is an open source platform designed for data scientists, data stewards, analysts and researchers familiar with open source tools and coding. Developed by data scientists for data scientists, AAW provides a flexible environment that enables advanced practitioners to get their work done with ease.

The AAW is a comprehensive solution for data science and data analytics.  With the AAW, you can customize notebook server deployments to suit your specific data science needs. We have a small number of custom Docker images made by our team.

<!-- prettier-ignore -->
!!! info "What is Kubeflow?"
    The AAW is based on [Kubeflow](https://www.kubeflow.org/), an open source comprehensive solution for deploying and managing end-to-end ML workflows.

Whether you're just getting started or already knee-deep in data analysis, the Advanced Analytics Workspace has everything you need to take your work to the next level. From powerful tools for data pipelines to cloud storage for your datasets, our platform has it all. Need to collaborate with colleagues or publish your results? No problem. We offer seamless collaboration features that make it easy to work together and share your work with others.

No matter what stage of your data science journey you're at, the Advanced Analytics Workspace has the resources you need to succeed.

## Getting Started with the AAW

<center>
![image](https://user-images.githubusercontent.com/8212170/158243976-0ee25082-f3dc-4724-b8c3-1430c7f2a461.png)
</center>

### The AAW Portal

The AAW portal homepage is available for internal users only. However, external users with a cloud account granted access by the business sponsor can access the platform through the analytics-platform URL.

<!-- prettier-ignore -->
!!! info annotate "AAW Portal Homepage"
    - [**Portal Homepage for Statistics Canada Employees**](https://www.statcan.gc.ca/data-analytics-service/aaw)
    - [**Portal Homepage for External Users**](https://analytics-platform.statcan.gc.ca/covid19)

### Kubeflow Account

<!-- prettier-ignore -->
!!! important "Attention External Users!"
    Users external to Statistics Canada will require a cloud account granted access by the business sponsor.

<!-- prettier-ignore -->
!!! important "Attention Statistics Canada Employees!"
    Users internal to Statistics Canada can get started right away without any additional sign up procedures, just head to  [https://kubeflow.aaw.cloud.statcan.ca/](https://kubeflow.aaw.cloud.statcan.ca/).

<!-- prettier-ignore -->
!!! note ""
    <center>
    [![Kubeflow is the Heart of the AAW!](./images/Kubeflow.PNG)](https://kubeflow.aaw.cloud.statcan.ca/)
    <h3>**[👉 Click here to setup your Kubeflow account! 👈](https://kubeflow.aaw.cloud.statcan.ca/)**</h3>
    </center>

**[Kubeflow](1-Experiments/Kubeflow/)** is a powerful and flexible open source platform that allows for dynamic leverage of cloud compute, with users having the ability to control compute, memory, and storage resources used. 

Kubeflow simplifies the following tasks:

- Creating customizable environments to work with data with user-controlled resource provisioning (custom CPU, GPU, RAM and storage).
- Managing notebook servers including Ubuntu Desktop (via noVNC), R Studio, JupyterLab with Python, R, Julia and SAS for Statistics Canada employees.

<!-- prettier-ignore -->
!!! info "Kubeflow Dashboard"
    - [**Kubeflow Dashboard**](https://kubeflow.aaw.cloud.statcan.ca/) Use this link once you have your cloud account!

Getting started with the Advanced Analytics Workspace (AAW) is easy and quick. First, you'll want to login to Kubeflow to create your first notebook server running JupyterLab, RStudio or Ubuntu Desktop. We encourage you to join our Slack channel to connect with other data scientists and analysts, ask questions, and share your experiences with the AAW platform.

### Slack

<center>
[![Ask Platform Related Questions on Slack!](images/SlackAAW.PNG)](https://statcan-aaw.slack.com/)
</center>

- **[Click here sign in to our Slack Support Workspace](https://statcan-aaw.slack.com/)**

- **Use the _General_ Channel!**

At StatCan, we understand that embarking on a new project can be overwhelming, and you're likely to have many platform-related questions along the way. That's why we've created a dedicated  **[Slack channel](https://statcan-aaw.slack.com/)** to provide you with the support you need. Our team of experts is standing by to answer your questions, address any concerns, and guide you through every step of the process.

To join our  **[Slack channel](https://statcan-aaw.slack.com/)**, simply click on the link provided and follow the instructions. You'll be prompted to create an account in the upper right-hand corner of the page. If you have an `@statcan.gc.ca` email address, use it when signing up as this will ensure that you are automatically approved and can start engaging with our community right away.

Once you've created your account, you'll have access to a wealth of resources and information, as well as the opportunity to connect with other users who are working on similar projects. Our  **[Slack channel](https://statcan-aaw.slack.com/)** is the perfect place to ask questions, share insights, and collaborate with your peers in real-time. Whether you're just getting started with a new project or you're looking for expert advice on a complex issue, our team is here to help.

So don't hesitate - join our **[Slack channel](https://statcan-aaw.slack.com/)** today and start getting the answers you need to succeed. We look forward to welcoming you to our community!

Click on the link, then choose "Create an account" in the upper right-hand corner.

<!-- prettier-ignore -->
!!! note ""
    <center>
    ![Use your @statcan.gc.ca email!](images/SlackAAW2.png)
    <h3>Use your @statcan.gc.ca email address so that you will be automatically approved.</h3>
    </center>

## 🧭 Getting Started

To access AAW services, you need to log in to Kubeflow with your StatCan guest cloud account. Once logged in, select Notebook Servers and click the "New Server" button to get started.

1. Login to [Kubeflow](https://kubeflow.aaw.cloud.statcan.ca/) with your StatCan guest cloud account. You will be prompted to authenticate the account.
2. Select Notebook Servers.
3. Click the "➕ New Server" button.

## 🧰 Tools Offered

AAW is a flexible platform for data analysis and machine learning. It offers a range of languages, including Python, R, and Julia. AAW also supports development environments such as VS Code, R Studio, and Jupyter Notebooks. Additionally, Linux virtual desktops are available for users who require additional tools such as OpenM++ and QGIS.

Here's a list of tools we offer:

- 📜 Languages:
  - 🐍 Python
  - 📈 R
  - 👩‍🔬 Julia
- 🧮 Development environments:
  - VS Code
  - R Studio
  - Jupyter Notebooks
- 🐧 Linux virtual desktops for additional tools (🧫 OpenM++, 🌏 QGIS etc.)

Sharing code, disks, and workspaces (e.g.: two people sharing the same virtual machine) is described in more detail in the [Collaboration](4-Collaboration/Overview.md) section. Sharing data through buckets is described in more detail in the **[Azure Blob Storage](./5-Storage/AzureBlobStorage.md)**
section.

### 💡 Help

- Disk (also called Volumes on the Notebook Server creation screen)
- Containers (Blob Storage)
- Data Lakes (coming soon)

- 📗 AAW Portal Documentation
  - [https://statcan.github.io/aaw/](https://statcan.github.io/aaw/)
- 📘 Kubeflow Documentation
  - [https://www.kubeflow.org/docs/](https://www.kubeflow.org/docs/)  
- 🤝 Slack Support Channel
  - [https://statcan-aaw.slack.com](https://statcan-aaw.slack.com)

## 🐱 Demos

If you require a quick onboarding demo session, need help, or have any questions, please reach out to us through our [🤝 Slack Support Channel](https://statcan-aaw.slack.com).

## Contributing

If you have any bugs to report or features to request please do so via https://github.com/Statcan/daaas.
