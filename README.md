<!-- markdownlint-disable no-bare-urls no-duplicate-header -->

# 🧙🔮 Welcome to Advanced Analytics Workspace (AAW)

> "What we want to do is make a leapfrog product that is way smarter than any mobile device has ever been, and super-easy to use. This is what iPhone is. OK? So, we're going to reinvent the phone."
> -- Steve Jobs

_Please find below additional information, videos and links to help better understand how to get started with Advanced Analytics Workspace (AAW)._

Advanced Analytics Workspace (AAW) is an open-source platform designed for data science and machine learning (ML) practitioners. Developed by data scientists for data scientists, AAW provides an unrestricted environment that enables advanced practitioners to get their work done with ease.

Built on the Kubeflow project, AAW is a comprehensive solution for deploying and managing end-to-end ML workflows. It simplifies the deployment of ML workflows on Kubernetes, making it simple, portable, and scalable. With AAW, you can customize your notebook deployments to suit your specific data science needs. Additionally, we have a small number of expertly crafted images made by our team of data science experts.

Advanced Analytics Workspace (AAW) is our **_open source platform for data science and machine learning (ML)_** for **advanced practitioners** to get their work done in an **unrestricted environment** made by data scientists _for_ data scientists. With AAW, you can customize your notebook deployments to suit your data science needs. We also have a small number of expertly crafted images made by our expert data science team.

AAW is based on the Kubeflow project which is an open source comprehensive solution for deploying and managing end-to-end ML workflows. Kubeflow is designed to make deployments of ML workflows on **Kubernetes** simple, portable and scalable.

🔔 **Important!** Users external to Statistics Canada will require a cloud account granted access by the business sponsor.

🔔 **Important!** Users internal to Statistics Canada can get started right away without any additional sign up procedures, just head to  [https://kubeflow.aaw.cloud.statcan.ca/](https://kubeflow.aaw.cloud.statcan.ca/).

## 🔗 Helpful Links

### 🛎️ AAW Services

The AAW portal homepage is available for internal users only. However, external users with a cloud account granted access by the business sponsor can access the platform through the analytics-platform URL.

- 🌀 AAW Portal Homepage
  - **Internal Only** [https://www.statcan.gc.ca/data-analytics-service/aaw](https://www.statcan.gc.ca/data-analytics-service/aaw)
  - **Internal/External** [https://analytics-platform.statcan.gc.ca/covid19](https://analytics-platform.statcan.gc.ca/covid19)

- 🤖 Kubeflow Dashboard
  - [https://kubeflow.aaw.cloud.statcan.ca/](https://kubeflow.aaw.cloud.statcan.ca/) 

### 💡 Help

The AAW Portal Documentation and Kubeflow Documentation provide helpful resources to get started with AAW. If you need further assistance, our Slack Support Channel is available for support.

- 📗 AAW Portal Documentation
  - [https://statcan.github.io/daaas/](https://statcan.github.io/daaas/)
- 📘 Kubeflow Documentation
  - [https://www.kubeflow.org/docs/](https://www.kubeflow.org/docs/)  
- 🤝 Slack Support Channel
  - [https://statcan-aaw.slack.com](https://statcan-aaw.slack.com)

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

## 🐱 Demos

If you require a quick onboarding demo session, need help, or have any questions, please reach out to us through our [🤝 Slack Support Channel](https://statcan-aaw.slack.com).

## Frequently Asked Questions

For frequently asked questions, please refer to the FAQ section in our Github repository, located [here](https://github.com/StatCan/daaas/blob/master/README.md).

If your question does not appear in this document, please reach out to us on our [Slack Support Channel](https://statcan-aaw.slack.com/).

**Thank you for choosing Advanced Analytics Workspace!**

## Presentations

We highly encourage you to watch our YouTube presentation given at Stratosphere:

- [YouTube](https://www.youtube.com/watch?v=quYuuEAqNm0)
- [SlideDeck](https://govcloud.blob.core.windows.net/docs/daaas-cncf.pdf)
- [AAW Onboarding Presentation (work in progress)](https://docs.google.com/presentation/d/12yTDlbMCmbg0ccdea2h0vwhs5YTa_GHm_3DieG5A-k8/edit#slide=id.g113e8bbc6e6_0_27)

## Security

A discussion about some of the security best practices in use by this platform:

- [aaw-security-proposal](https://github.com/StatCan/aaw-security-proposal)

## Advanced Analytics Workspace

The following is a list of all the `general` related repositories for the Advanced Analytics Workspace project.

| Repository                                                                                                | Description                                                                                   | Visibility |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| [aaw-argocd-applications](https://github.com/StatCan/aaw-argocd-applications)                             | ArgoCD Applications                                                                           | Private    |
| [aaw-argocd-manifests](https://github.com/StatCan/aaw-argocd-manifests)                                   | Manifests used for ArgoCD deployments                                                         | Public     |
| [aaw-argoflow-azure](https://github.com/StatCan/aaw-argoflow-azure)                                       | Kubeflow deployment powered by ArgoCD                                                         | Public     |
| [aaw-kubeflow-containers](https://github.com/StatCan/aaw-kubeflow-containers)                             | Containers to be used within Kubeflow                                                         | Public     |
| [aaw-contrib-containers](https://github.com/StatCan/aaw-contrib-containers)                               | Containers to be used for general purpose Data Science                                        | Public     |
| [aaw-contrib-jupyter-notebooks](https://github.com/StatCan/aaw-contrib-jupyter-notebooks)                 | Jupyter Notebooks to be used with the Advanced Analytics Workspace platform                   | Public     |
| [aaw-contrib-r-notebooks](https://github.com/StatCan/aaw-contrib-r-notebooks)                             | R Notebooks to be used with Advanced Analytics Workspace platform                             | Public     |
| [aaw-gatekeeper-constraints](https://github.com/StatCan/aaw-gatekeeper-constraints)                       | Gatekeeper constraints built specifically for AAW                                             | Private    |
| [aaw-goofys-injector](https://github.com/StatCan/aaw-goofys-injector)                                     | Mount an S3 bucket, Data Lake, Blob Storage as a file system in a Notebook                    | Public     |
| [aaw-inferenceservices-controller](https://github.com/StatCan/aaw-inferenceservices-controller)           | Kubernetes controller for managing inference services                                         | Public     |
| [aaw-kubeflow-manifests](https://github.com/StatCan/aaw-kubeflow-manifests)                               | Kustomize installation manifests for Kubeflow                                                 | Public     |
| [aaw-kubeflow-controller](https://github.com/StatCan/aaw-kubeflow-controller)                             | Kubeflow controller which sets PodDefaults + Vault policies for each Profile detected         | Public     |
| [aaw-kubeflow-mlops](https://github.com/StatCan/aaw-kubeflow-mlops)                                       | Kubeflow MLOps pipeline using GitHub Actions                                                  | Public     |
| [aaw-kubeflow-opa-sync](https://github.com/StatCan/aaw-kubeflow-opa-sync)                                 | Synchronize profile editors into the Open Policy Agent for use in MinIO Access Control        | Public     |
| [aaw-kubeflow-pipelines-secret-scanner](https://github.com/StatCan/aaw-kubeflow-pipelines-secret-scanner) | Scan all Kubeflow pipelines for exposed secrets                                               | Public     |
| [aaw-kubeflow-profiles](https://github.com/StatCan/aaw-kubeflow-profiles)                                 | Kubeflow profile manifests stored in YAML                                                     | Private    |
| [aaw-kubeflow-profiles-controller](https://github.com/StatCan/aaw-kubeflow-profiles-controller)           | Kubeflow profiles controller which allows for custom configuration for an individual profile  | Public     |
| [aaw-minio-credential-injector](https://github.com/StatCan/aaw-minio-credential-injector)                 | Mutating webhook which adds minio credential annotations to notebook pods                     | Public     |
| [aaw-network-policies](https://github.com/StatCan/aaw-network-policies)                                   | Kubernetes network policies for AAW                                                           | Private    |
| [aaw-prob-notebook-controller](https://github.com/StatCan/aaw-prob-notebook-controller)                   | Kubernetes controller for managing Authorization Policies associated to Protected-B Notebooks | Public     |
| [aaw-security-proposal](https://github.com/StatCan/aaw-security-proposal)                                 | Proposal for the implementation of Protected B workloads in AAW                               | Public     |
| [aaw-toleration-injector](https://github.com/StatCan/aaw-toleration-injector)                             | Kubernetes toleration injector with support for GPUs and Node Pools                           | Public     |

## Terraform

The following is a list of all the `terraform` related repositories for the
Advanced Analytics Workspace project.

### Install the AAW Platform and Infrastructure

```sh
## Installs AAW Platform and Infrastructure
##
## └─── https://github.com/statcan/terraform-advanced-analytics-workspaces-infrastructure
##      ├─── https://github.com/statcan/aaw-dev-cc-00
##      ├─── https://github.com/statcan/aaw-prod-cc-00
##      │    ├── https://github.com/statcan/terraform-azure-statcan-aaw-environment
##      │    │   ├── https://github.com/statcan/terraform-statcan-aaw-network
##      │    │   └── https://github.com/statcan/terraform-azure-statcan-cloud-native-environment-infrastructure
##      │    │       ├── https://github.com/canada-ca-terraform-modules/terraform-azurerm-kubernetes-cluster
##      │    │       └── https://github.com/canada-ca-terraform-modules/terraform-azurerm-kubernetes-cluster-nodepool
##      │    └─── https://github.com/statcan/terraform-statcan-aaw-platform (see below)
##      └─── https://github.com/statcan/terraform-azure-statcan-aaw-region-environment
```

| Component | Repository                                                                                                                                                    | Description                                                                                  |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| AAW       | [terraform-advanced-analytics-workspaces-infrastructure](https://github.com/statcan/terraform-advanced-analytics-workspaces-infrastructure-example)           | Reference implementation for an Advanced Analytics Workspaces (AAW) infrastructure pipeline  |
| AAW       | [aaw-dev-cc-00](https://github.com/statcan/terraform-statcan-aaw-infrastructure-example)                                                                      | Reference implementation for an Advanced Analytics Workspaces (AAW) development environment  |
| AAW       | [aaw-prod-cc-00](https://github.com/statcan/terraform-statcan-aaw-infrastructure-example)                                                                     | Reference implementation for an Advanced Analytics Workspaces (AAW) production environment   |
| AAW       | [terraform-azure-statcan-aaw-environment](https://github.com/statcan/terraform-azure-statcan-aaw-environment)                                                 | Terraform module of Advanced Analytics Workspaces (AAW) per-environment Azure configuration  |
| AAW       | [terraform-azure-statcan-aaw-network](https://github.com/statcan/terraform-azure-statcan-aaw-network)                                                         | Terraform module of Advanced Analytics Workspaces (AAW) networking                           |
| AAW       | [terraform-azure-statcan-cloud-native-environment-infrastructure](https://github.com/statcan/terraform-azure-statcan-cloud-native-environment-infrastructure) | Terraform module for Statistics Canada's Cloud Native Environment Azure Cloud Infrastructure |
| AAW       | [terraform-azurerm-kubernetes-cluster](https://github.com/statcan/terraform-azurerm-kubernetes-cluster)                                                       | Terraform module for Azure Kubernetes Service (AKS) cluster                                  |
| AAW       | [terraform-azurerm-kubernetes-cluster-nodepool](https://github.com/statcan/terraform-azurerm-kubernetes-cluster-nodepool)                                     | Terraform module for Azure Kubernetes Service (AKS) nodepool                                 |
| AAW       | [terraform-azure-statcan-aaw-region-environment](https://github.com/statcan/terraform-azure-statcan-aaw-region-environment)                                   | Terraform module of Advanced Analytics Workspaces (AAW) per-region configuration of Azure    |
| AAW       | [terraform-statcan-aaw-platform](https://github.com/statcan/terraform-statcan-aaw-platform)                                                                   | Terraform module for the Advanced Analytics Workspaces (AAW) platform                        |

### Install the Cloud Native Platform

```sh
## Statistics Canada's Cloud Native Platform (CNP)
##
## └─── https://github.com/statcan/terraform-statcan-aaw-platform
##      ├─── https://github.com/statcan/terraform-azure-statcan-cloud-native-platform-infrastructure
##      │    ├─── aad_pod_identity
##      │    ├─── cert_manager
##      │    ├─── vault
##      │    └─── velero
##      ├─── https://github.com/statcan/terraform-statcan-kubernetes-core-platform
##      │    ├─── aad_pod_identity
##      │    ├─── cert_manager
##      │    ├─── fluentd
##      │    ├─── gatekeeper
##      │    ├─── kubecost
##      │    ├─── prometheus
##      │    ├─── vault_agent
##      │    └─── velero
##      ├─── https://github.com/statcan/terraform-statcan-kubernetes-app-platform
##      │    ├─── istio operator
##      │    └─── istio gateway handling
##      └─── https://github.com/statcan/terraform-kubernetes-namespace
##           └─── daaas-system
```

| Component | Repository                                                                                                                                              | Description                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| CNS       | [terraform-azure-statcan-cloud-native-platform-infrastructure](https://github.com/statcan/terraform-azure-statcan-cloud-native-platform-infrastructure) | Terraform module for Statistics Canada Azure Cloud Native Platform Infrastructure |
| CNS       | [terraform-statcan-kubernetes-core-platform](https://github.com/statcan/terraform-statcan-kubernetes-core-platform)                                     | Terraform module for Statistics Canada Core Kubernetes Platform                   |
| CNS       | [terraform-statcan-kubernetes-app-platform](https://github.com/statcan/terraform-statcan-kubernetes-app-platform)                                       | Terraform module for Statistics Canada Kubernetes Application Platform            |

### Misc

| Repository                                                                                    | Description                                                | Visibility |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|------------|
| [terraform-aaw-managed-databases](https://github.com/StatCan/terraform-aaw-managed-databases) | Terraform module for deployment of Azure Managed Databases | Private    |
| [terraform-aaw-vault](https://github.com/StatCan/terraform-aaw-vault)                         | Terraform module for configuring Hashicorp Vault           | Private    |

## Community Engagement

The following is a list of some of the `collaborative` work we made available to
improve upstream projects.

| Repository                                                                                  | Description                                                 | Visibility |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------|------------|
| [boathouse](https://github.com/StatCan/boathouse)                                           | Manage Kubernetes storage mounts with Goofys                | Public     |
| [jupyter-apis](https://github.com/StatCan/jupyter-apis)                                     | Golang replacement for the Kubeflow Jupyter Web APIs        | Public     |
| [jupyterlab-language-pack-fr_FR](https://github.com/StatCan/jupyterlab-language-pack-fr_FR) | JupyterLab fr-FR Language Pack                              | Public     |
| [vault-plugin-secrets-minio](https://github.com/StatCan/vault-plugin-secrets-minio)         | Vault plugin which will provision multi-user keys for Minio | Public     |

The following is a list of some of the `forked` projects where we have provided
multilingual support and other UX related enhancements.

| Repository                                                          | Description                                 | Visibility |
|---------------------------------------------------------------------|---------------------------------------------|------------|
| [kubeflow](https://github.com/StatCan/kubeflow)                     | Multilingual support for Kubeflow           | Public     |
| [kubeflow-pipelines](https://github.com/StatCan/kubeflow-pipelines) | Multilingual support for Kubeflow Pipelines | Public     |
| [minio](https://github.com/StatCan/minio)                           | Multilingual support for MinIO              | Public     |
| [minio-console](https://github.com/StatCan/minio-console)           | Multilingual support for MinIO Console      | Public     |
| [rstudio](https://github.com/StatCan/rstudio)                       | Multilingual support for RStudio            | Public     |
