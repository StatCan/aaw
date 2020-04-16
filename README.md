# DAaaS Proof of Concept

## Background

In order to help guide the general direction of DAaaS and what we think can help quickly on-board data scientists to a public cloud environment a proof of concept prototype has been created using primarily open source technologies.

Firstly, we're interested in leveraging the tools and experience that we have already obtained at Statistics Canada. This would mean utilizing Kubernetes (via Azure Kubernetes Service) to orchestrate all of the data science workloads. The Terraform configuration (Infrastructure as Code) already exists and we have launched a cluster within a day with all of our common platform tools and the various data analytics tools; KubeFlow, Jupyterhub, and the Databricks operator to name a few, as well as access to CPU and GPU machines that can autoscale on demand. The Databricks operator allows us to manage Databricks from a unified control plane, utilizing Desired State Configuration and showcases an example of how Kubernetes can control PAAS services. All these tools align with industry standards for data analytics.

> Note: To learn more about why Kubernetes is a good fit to manage Azure Databricks, we recommend quickly reading over the first half of the [Azure Data Bricks Operator](https://blog.openshift.com/wp-content/uploads/OpenShift-Commons-MSFT-Azure-Databricks-Operator.pdf) presentation by Microsoft which essentially describes vision. Then to see how Kubeflow can launch complex databricks operations as a pipeline which can be one of many potential outcomes; please see these [examples](https://github.com/kubeflow/pipelines/tree/0708cd723e088696ee86d523576c2daf08b5aa01/samples/contrib/azure-samples/kfp-azure-databricks). Additionally, in the links below we highlighted some reference architectures.

Statistics Canada has experience operating Kubernetes and data analytics/science pipelines on top of it. Since Kubernetes is a general computation orchestrator, we can run supporting services, applications, and more following a common deployment and management methodology. Additionally with the integration with Kubernetes Role-Based Access Control (RBAC) and the Open Policy Agent, we can have fine-grained control over the configuration of data analytics pipelines.

> Note: We had to remove all references to the hostname at the moment but hope in the future can make available.

## Key Highlights

When you want to work with cloud native services in `Azure`, `AWS`, `GCP`, etc. you start to think about how you can nicely manage these services without having to have a whole second paradigm in your flows and actually deliver and bring disparate systems up.

### Pipelines

* When you break down pipelines into their semantic parts the reality is they are a highly cohesive system, but they're loosely coupled meaning some of the components might not know about each other. They typically use a common agreed upon interface, so they know what to expect
* With respect to pipelines **relationship is king** and should be a first-class consideration as part of software delivery
* In current DAaaS the pipeline system is being developed so that it can support:
  * Unknown component configuration and relationships at build time
  * High flexibility and reusable components reducing on-boarding and operational time
  * Has 1 to many custom transforms whether is a bunch of spark jobs, python scripts, or anything else that can be run as part of a pipeline
  * Support for forks in the data stream where some of the data could go off to modern data warehouses such as Azure Synapse, others can simply go to object or regular storage, and others through a path on the system we might not know at design-time
  * Support single point of configuration for a pipeline where all the components, relationships, and parameters are defined in the same place
  * Create a unified workflow for the 200 data scientists that can embrace both open source software but also work with external dependencies (Databricks, PaaS services)

### Kubernetes

* Kubernetes is an industry-standard, unified control plane using Desired State Configuration
  * Well-defined catalog of operations that can be performed
  * Kubernetes enabled centralized control of access policies
  * Desired State Configuration allows for configuration modularity and re-use, allowing for packaging and compartmentalization of complexity across clouds
  * The operator pattern enables the configuration of external resources using standard and familiar constructs (e.g. a simple YAML file to maintain an external resource)
  * Enables the integration with custom components such as Event Hubs (streaming), Databricks, and even Azure Synapse
  * Where possible we align with the TBS directive that says we should be using open-source technologies first
* Through the Databricks Operator created by Azure, we can:
  * Launch customizable Spark notebooks through Kubernetes objects, which call the Databricks API (and the operator also updates the status of the job in Kubernetes)
  * Interact with Kubernetes secrets backed by Azure Keyvault enabling secure storage

## Azure Kubernetes Service

![aks](images/aks_ui.png "Azure Kubernetes Service")

Launched a secured Cloud Native Platform for Government based on the version we open sourced to the [GC Accelerators](https://github.com/canada-ca-terraform-modules?q=kubernetes). The platform is built using open source software projects, primarily from the Cloud Native Computing Foundation (CNCF).

What can you do it with / what have we done with it?

* Infrastructure and platform tools deployed using Infrastructure as Code (Terraform)
  * Cluster, monitoring, logging and deployment tools
* Public-available cluster and web endpoints
* Authentication against the Statistics Canada Cloud directory
* Base for all of the components discussed later
* Access to different machine types (CPU, GPU and high-memory) based on use-case

### Services

* https://istio-kiali.example.ca
* https://grafana.example.ca
* https://istio-grafana.example.ca (private)
* https://prometheus.example.ca (private)
* https://alertmanager.example.ca (private)

### Source Code

* https://github.com/StatCan/terraform-kubernetes-aks-daaas
* https://github.com/StatCan/terraform-kubernetes-aks-platform-daaas
* https://github.com/StatCan/charts
* https://github.com/StatCan/gatekeeper-policies
* https://govcloud.ca
* https://govcloud.blob.core.windows.net/docs/azure-aks-platform.pdf

## Kubeflow

![kubeflow](images/kubeflow_ui.png "Kubeflow")

Kubeflow is a suite of tools for running Machine Learning (ML) workflows on Kubernetes. It is an open-source tool used by large research institutions (like CERN) for machine learning workloads and backed by a large community (10k stars on GitHub). It has been deployed into our AKS cluster, and connected to the Statistics Canada Cloud user directory for authentication and will be expanded to others through integration with GitHub authentication.

What can you do it with / what have we done with it?

* Created and open sourced GitHub Action for KubeFlow (upgrade API, and added support for X-Auth-Token)
* Authorization done via OpenID Connect (OIDC)
* Cluster will autoscale automatically based on demand
* Pipeline created from GitHub Actions
* Pipelines controlled through code
* Pipelines calling PAAS services like DataBricks
* Shared and individual workspaces for Jupyter Notebooks
* Launched KubeFlow via Kustomize to AKS

![kubeflow pipeline](images/kubeflow_pipeline.png "Kubeflow Pipeline")

The two images demonstrate a pipeline definition and an execution.

These pipelines were deployed through GitHub Actions, and the bottom one was executed in an Azure Databricks cluster.

![kubeflow controlling databricks](images/kubeflow_databricks.png "KubeFlow controlling DataBricks")

![kubeflow github action](images/kubeflow_action.png "GitHub action running DataBricks Pipeline")

The above picture demonstrates the GitHub Action deploying the pipeline.

The below picture demonstrates sharing a workspace with other contributors.

![kubeflow shared workspaces](images/kubeflow_workspaces.png "Kubeflow shared workspaces")

#### Source Code

* https://github.com/StatCan/gpu-toleration-injector
* https://github.com/StatCan/kubeflow-containers
* https://github.com/StatCan/kubeflow-controller
* https://github.com/StatCan/kubeflow-github-action
* https://github.com/StatCan/kubeflow-manifest

## Kubeflow Containers

![kubeflow containers](images/kubeflow_containers.png "Kubeflow Containers")

Created a set of of ready-to-run container images for various types of roles related to data science. We provide a convenient and tailored experience of Jupyter including all the tools data scientists need to do their work.

What can you do it with / what have we done with it?

* Built and deployed all container images to Azure Container Registry via GitHub Actions
* Extended from the officially supported Jupyter container images providing additional data science tools
* Task-specific images based on required tools
  * Geomatics (R and Geo specific tooling)
  * Machine learning (Tensorflow, Tensorboard, Keras, etc)
  * Full workspace: VS Code, VNC Server, and other graphical tools
* Images are built for CPU compute and GPU compute (NVIDIA/CUDA)

![kubeflow containers github action](images/kubeflow_containers_action.png "Build and Deploy container images to Azure Container Registry")

The above picture demonstrates the GitHub Actions workflow to build and deploy container images to the Azure Container Registry.

#### Source Code

* https://github.com/StatCan/kubeflow-containers
* https://github.com/StatCan/kubeflow-containers/actions

## Jupyter Notebooks (Examples)

![jupyter notebooks](images/jupyter_notebooks.png "Jupyter Notebooks")

We have created a variety of example Jupyter Notebooks utilizing the data science tools deployed. This includes simple examples to complete, training to model serving pipelines (MLOps).

What can you do it with / what have we done with it?

* Languages: Python, R
* Technologies: Tensorflow, PyTorch, Keras
* Storage: Accessing data stored in S3-compatible storage
* Integration with PAaaS offerings: Azure Databricks and MLflow
* Demonstration of a fully baked end to end pipeline from training to model serving in Kubeflow
* Custom data science containers / algorithms for analyzing, processing, and training data:
   * [Tensorflow Transform](https://github.com/StatCan/datascience-containers/blob/master/preprocessing/tft/src/transform.py) for preprocessing raw data to data used to train a ML model
   * [Tensorflow Boosted Trees Classifier](https://github.com/StatCan/datascience-containers/blob/master/training/dnntrainer/src/trainer/boosted.py) to predict and work with structured data
   * [Prediction](https://github.com/StatCan/datascience-containers/blob/master/training/predict/src/predict.py) runs data through the predicted model
   * [Confusion Matrix](https://github.com/StatCan/datascience-containers/blob/master/metrics/confusion_matrix/src/confusion_matrix.py) for visualization of algorithm performance
   * [Receiver Operating Characteristic](https://github.com/StatCan/datascience-containers/blob/master/metrics/roc/src/roc.py) for performance measurement for classification problem
   * [Tensorflow Serving](https://github.com/StatCan/datascience-containers/blob/master/serving/deployer/src/deploy.sh) for delivering and updating the model

![advanced pipeline example](images/jupyter_notebooks_kubeflow.png "Advanced pipeline example")

The above picture demonstrates an advanced learning and training pipeline on Kubeflow.

#### Source Code

* https://github.com/StatCan/datascience-containers
* https://github.com/StatCan/jupyter-notebooks

## MinIO

![minio ui](images/minio_ui.png "Minio UI")

MinIO provides an S3-compatible API to access data stored locally or within an Azure Blob storage account.

What can you do it with / what have we done with it?

* Expose acccess to data stored in an Azure Blob storage account via an S3-compatible API
  * Available for use within Kubeflow pipelines and from Jupyter notebooks
* Basic SQL-like access to data files
* Intend to provide a MinIO service for each project backed by an Azure Storage account
  * Leverage the MinIO operator for MinIO lifecycle management

![minio api](images/minio_api.png "Jupyter notebook interacting with MinIO")

The above picture demonstrates a Jupyter Notebook interacting with MinIO through an API.

## Shiny

![shiny server](images/shiny_ui.png "Shiny Server")

Shiny is an application server for serving R-based visualization applications created by data scientists.

What can you do it with / what have we done with it?

* Launched Shiny Server to AKS via GitHub Actions
* Created a helm chart to be called by GitHub Actions
* Shiny Server extended behind Nginx proxy
* Integrated with Azure Files for application hosting

![shiny github action](images/shiny_action.png "Deploy Shiny to AKS")

The above picture demonstrates the GitHub Actions workflow to build and deploy it to AKS.

The below picture demonstrates the file share containing all R applications served by Shiny.

![azure files](images/shiny_azure_files.png "Shiny with Azure Files mount point")

#### Source Code

* https://github.com/StatCan/shiny
* https://github.com/StatCan/shiny/actions
* https://github.com/StatCan/charts/tree/master/stable/shiny

## NodeJS (https://covid19.example.ca)

![covid map](images/covid_ui.png "Covid-19 Map")

Covid-19 is an interactive, animated COVID-19 coronavirus map to track the outbreak over time by country and by region for selected countries (including China, Italy, Korea, Japan, France, Germany, United States). It was launched into our environment to demonstrate running web applications and we saw opportunity to improve it to better demonstrate the spread of COVID-19 across Canada.

What can you do it with / what have we done with it?

* Launched NodeJS react application to AKS via GitHub Actions
* Created a helm chart to be called by GitHub Actions
* Forked popular open source repo on GitHub and containerized
* Started to work on french interface and design improvements
* Looking at integrating with the Statistics Canada dataset
* Looking at feasibility of KubeFlow (Machine Learning) to add spread prediction

![covid github action](images/covid_action.png "Deploy Covid-19 to AKS")

The above picture demonstrates the action which builds and deploys the COVID-19 application.

### Source Code

* https://github.com/StatCan/covid19
* https://github.com/StatCan/covid19/actions
* https://github.com/StatCan/charts/tree/master/stable/covid

## .NET (https://portal.example.ca)

![portal ui](images/portal_ui.png "Portal UI")

The main portal for the DAaaS platform which will provide data scientists with both the list of supported services as well useful datasets that they can leverage in their machine learning journey. The portal will also offer helpful documentation, resources, tutorials, and support for the multiple types of data scientists using the platform.

What can you do it with / what have we done with it?

* Launched OrchardCMS application to AKS via GitHub Actions
* Created a helm chart to be called by GitHub Actions
* Working on latest iteration of the mockup templates
* The addition of content as well as helpful datasets to leverage

![portal github action](images/portal_action.png "Deploy Portal to AKS")

The above picture demonstrates the action which builds and deploys the Portal web application.

### Source Code

* https://github.com/StatCan/StatCan.OrchardCore
* https://github.com/StatCan/StatCan.OrchardCore/actions
* https://github.com/StatCan/charts/tree/master/stable/orchard-cms

## MLflow (https://mlflow.example.ca)

![mlflow ui](images/mlflow_ui.png "MLflow UI")

Launched MLflow alongside with its web ui in a highly available fashion on top of Kubernetes. MLflow was configured to use an Azure storage account for the backend artifact store.

> Note: With MLflow 1.1, you can now run MLflow Projects on Kubernetes clusters. Any MLflow Project with a Docker Environment is supported. MLflow executes your Project code as a Kubernetes Job and periodically monitors its status until completion.

What can you do it with / what have we done with it?

* Launched MLflow python application to AKS via GitHub Actions
* Created a helm chart to be called by GitHub Actions
* Extended container image to support Azure storage backend for the artifact store
* File store is configured as an persistent volume
* Artifact store is configured as an Azure storage account
* Efficient use of Gunicorn workers

![mlflow github action](images/mlflow_action.png "Deploy MLflow to AKS")

The above picture demonstrates the action which builds and deploys the Mlflow application.

### Source Code

* https://github.com/StatCan/mlflow
* https://github.com/StatCan/mlflow/actions
* https://github.com/StatCan/charts/tree/master/stable/mlflow

## Dremio (https://dremio.example.ca)

![dremio ui](images/dremio_ui.png "Dremio UI")

We experimented with Dremio to provide a common way of accessing data stored in various sources (e.g., Azure Storage account, Azure Data Lake, S3, MSSQL, etc.).

What can you do it with / what have we done with it?

* Launched the Open Source version with the Helm chart (Highly available, with Zookeeper or Etcd backend)
* Currently experimental due to limitations in authentication in the free version
* Support for many data sources:
  * Azure Storage Account
  * Azure Data Lake
  * S3
  * MSSQL / MySQL / PostgreSQL
  * Elasticsearch

![dremio github action](images/dremio_action.png "Deploy Dremio to AKS")

The above picture demonstrates the action which builds and deploys the Dremio application.

### Source Code

* https://github.com/StatCan/dremio
* https://github.com/StatCan/dremio/actions
* https://github.com/StatCan/charts/tree/master/stable/dremio

## Important Links

### Resources

* Azure DataBricks and Kubernetes ([PDF](https://blog.openshift.com/wp-content/uploads/OpenShift-Commons-MSFT-Azure-Databricks-Operator.pdf)) ([YouTube](https://www.youtube.com/watch?v=gBgXI5WmcWg))
* KubeFlow pipeline supporting complex DataBricks operations ([Link](https://github.com/kubeflow/pipelines/tree/0708cd723e088696ee86d523576c2daf08b5aa01/samples/contrib/azure-samples/kfp-azure-databricks))
* Reference Architectures:
  * Train a recommendation model using Azure DataBricks and deploy as an API ([Link](https://github.com/MicrosoftDocs/architecture-center/blob/master/docs/reference-architectures/ai/real-time-recommendation.md))
  * Recommended ways to train and deploy machine learning models on Azure ([Link](https://github.com/microsoft/AIReferenceArchitectures))
  * ComCast case study using Azure DataBricks and AKS ([Link](https://www.topbots.com/ml-model-deployment-with-mlflow-kubernetes/))

#### Source Code

* https://github.com/StatCan?q=daaas
* https://github.com/StatCan/terraform-kubernetes-aks-daaas
* https://github.com/StatCan/terraform-kubernetes-aks-platform-daaas
* https://github.com/StatCan/terraform-kubernetes-aks-daaas-private (private)
* https://github.com/StatCan/terraform-kubernetes-aks-platform-daaas-private (private)
* https://github.com/StatCan/charts
* https://github.com/StatCan/covid19
* https://github.com/StatCan/daaas
* https://github.com/StatCan/datascience-containers
* https://github.com/StatCan/dremio
* https://github.com/StatCan/gatekeeper-policies
* https://github.com/StatCan/jupyter-notebooks
* https://github.com/StatCan/gpu-toleration-injector
* https://github.com/StatCan/kubeflow-containers
* https://github.com/StatCan/kubeflow-controller
* https://github.com/StatCan/kubeflow-github-action
* https://github.com/StatCan/kubeflow-manifest
* https://github.com/StatCan/mlflow
* https://github.com/StatCan/shiny
* https://github.com/StatCan/statcan.orchardcore

#### GitHub Actions

* https://github.com/StatCan/charts/actions
* https://github.com/StatCan/covid19/actions
* https://github.com/StatCan/dremio/actions
* https://github.com/StatCan/gpu-toleration-injector/actions
* https://github.com/StatCan/kubeflow-containers/actions
* https://github.com/StatCan/kubeflow-controller/actions
* https://github.com/StatCan/kubeflow-github-action/actions
* https://github.com/StatCan/mlflow/actions
* https://github.com/StatCan/shiny/actions
* https://github.com/StatCan/StatCan.OrchardCore/actions
* https://github.com/StatCan/terraform-kubernetes-aks-daaas-private/actions (private)
* https://github.com/StatCan/terraform-kubernetes-aks-platform-daaas-private/actions (private)

#### Public

* https://kubeflow.example.ca
* https://portal.example.ca
* https://shiny.example.ca
* https://covid19.example.ca
* https://istio-kiali.example.ca
* https://grafana.example.ca
* https://istio-grafana.example.ca (private)
* https://prometheus.example.ca (private)
* https://alertmanager.example.ca (private)

#### Recommended Reading

* https://kubeflow.org/docs/started/getting-started/
* https://towardsdatascience.com/tagged/kubernetes
* https://medium.com/kredaro-engineering/ai-tales-building-machine-learning-pipeline-using-kubeflow-and-minio-4b88da30437b
