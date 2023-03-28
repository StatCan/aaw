<!-- markdownlint-disable no-bare-urls no-duplicate-header -->

# Data Analytics as a Service

Data Analytics as a Service for the Government of Canada and external collaborators.

## Frequently Asked Questions (FAQ)

If your question does not appear in this document, please reach out to us on our [Slack Support Channel](https://statcan-aaw.slack.com/).

### Who can access the AAW?

- Anyone with a Statistics Canada (`@statcan.gc.ca`) email address can access the AAW.

### What data formats are supported in the AAW?

The AAW includes tools that allow data science users to open almost any file. The AAW supports many commonly used file formats, including (but not limited to):

- csv
- xlsx
- json
- xml
- sas7bdat
- sqlite
- many others... just ask :-)

### How much does the AAW cost?

#### CPU Only

| **Use Case**               | **Compute Resources** |            |       | **Time (Hours/Week)** | **Cost** |           |            |
|----------------------------|-----------------------|------------|-------|-----------------------|----------|-----------|------------|
|                            | _CPU_                 | _RAM (GB)_ | _GPU_ |                       | _Weekly_ | _Monthly_ | _Annually_ |
| CPU: Occasional Use        | 2                     | 8          | 0     | 8                     | 1.1367   | 4.88781   | 59.1084    |
| CPU: During Business Hours | 2                     | 8          | 0     | 40                    | 5.6835   | 24.43905  | 295.542    |
| CPU: 24/7                  | 2                     | 8          | 0     | 168                   | 23.8707  | 102.64401 | 1241.2764  |

#### Add a GPU

| **Use Case**               | **Compute Resources** |            |       | **Time (Hours/Week)** | **Cost** |           |            |
|----------------------------|-----------------------|------------|-------|-----------------------|----------|-----------|------------|
|                            | _CPU_                 | _RAM (GB)_ | _GPU_ |                       | _Weekly_ | _Monthly_ | _Annually_ |
| GPU: Occaisonal Use        | 0                     | 0          | 1     | 8                     | 34.468   | 148.2124  | 1792.336   |
| GPU: During Business Hours | 0                     | 0          | 1     | 40                    | 172.34   | 741.062   | 8961.68    |
| GPU: 24/7                  | 0                     | 0          | 1     | 168                   | 723.828  | 3112.4604 | 37639.056  |

### What are the steps for getting Protected B data into MinIO?

- One must consult with FDI (F.A.I.R. Data Infrastructure) before Protected B Data can be loaded into MinIO. The FDI team owns an Azure Data Factory pipeline for moving data, typically from on premise, to an Azure Storage Account and MinIO is our S3 gateway to that storage account.

### Can we use Power BI on the AAW?

- At the moment, no. We are currently looking into solutions for sharing data between the AAW and CAE (which supports Power BI).

### Does using SAS entail different costs than the others? Are there a limited number of licenses or instances that can be run?

- SAS support is currently experimental and will rely on existing Statistics Canada SAS software licenses.

### How do you suspend your server (to save costs)?

- Press the suspend server button (square to the left of the garbage can icon to delete a server). This will suspend the workspace to save on costs.
- Please keep in mind all data that is not stored on persistent disks (persistent workspace volume or persistent data volumes) is deleted when a workspace is suspended. In particular data on non-persistent disks and data on the filesystem outside the workspace or data volume (for instance the `/tmp` folder) will be permanently lost.
- When suspended the workspace and data volumes remain locked and cannot be deleted or attached to another server.
- To resume a suspended server, press the resume button (triangle icon to the left of the garbage can). When resumed the server will have the same workspace and data volumes as before (with all data kept as-is if the volumes were persistent) and has the exact same specification (CPU, RAM, GPU, and other settings). Things stored outside the home directory and persistent data volumes (like conda virtual environments) will be gone and will need to be recreated if necessary.

### How do I add other people to my namespace (for collaboration)?

1. Do we need to stop any running instances in our notebooks when we’re not using it? If so, how do we do this? I checked the documentation and there is no guidelines on how to stop any running notebooks as a cost-saving measure.

### Are there any pre-loaded data (datasets) in AAW that we can access and use for both R and Python notebooks?

- Our JupyterLab images come with some example notebooks and data, they can be found in `/aaw-contrib-jupyter-notebooks/`.
- Our R Studio image also has some example notebooks and data, they can be found in `/aaw-contrib-r-notebooks/`.

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

### Developer Notes:
Fix spelling by executing `fix-spelling-en` and `fix-spelling-fr` 
Adding to the sensitive or insensitive category
Ignoring will simply ignore the error for this round. It will trigger again next execution. 