<!-- markdownlint-disable no-bare-urls no-duplicate-header -->

# Data Analytics as a Service

Data Analytics as a Service for the Government of Canada and external
collaborators.

## Presentations

We highly encourage you to watch our YouTube presentation given at Stratosphere:

- [YouTube](https://www.youtube.com/watch?v=quYuuEAqNm0)
- [SlideDeck](https://govcloud.blob.core.windows.net/docs/daaas-cncf.pdf)

## Security

A discussion about some of the security best practices in use by this platform:

- [aaw-security-proposal](https://github.com/StatCan/aaw-security-proposal)

## Advanced Analytics Workspace

The following is a list of all the `general` related repositories for the
Advanced Analytics Workspace project.

| Repository                                                                                                | Description                                                                                   | Visibility |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------- |
| [aaw-argocd-applications](https://github.com/StatCan/aaw-argocd-applications)                             | ArgoCD Applications                                                                           | Private    |
| [aaw-argocd-manifests](https://github.com/StatCan/aaw-argocd-manifests)                                   | Manifests used for ArgoCD deployments                                                         | Public     |
| [aaw-argoflow-azure](https://github.com/StatCan/aaw-argoflow-azure)                                       | Kubeflow deployment powered by ArgoCD                                                         | Public     |
| [aaw-contrib-containers](https://github.com/StatCan/aaw-contrib-containers)                               | Containers to be used for general purpose Data Science                                        | Public     |
| [aaw-contrib-jupyter-notebooks](https://github.com/StatCan/aaw-contrib-jupyter-notebooks)                 | Containers built to be used with Kubeflow for Data Science                                    | Public     |
| [aaw-contrib-r-notebooks](https://github.com/StatCan/aaw-contrib-r-notebooks)                             | R Notebooks to be used with Advanced Analytics Workspace platform                             | Public     |
| [aaw-gatekeeper-constraints](https://github.com/StatCan/aaw-gatekeeper-constraints)                       | Gatekeeper constraints built specifically for AAW                                             | Private    |
| [aaw-goofys-injector](https://github.com/StatCan/aaw-goofys-injector)                                     | Mount an S3 bucket, Data Lake, Blob Storage as a file system in a Notebook                    | Public     |
| [aaw-inferenceservices-controller](https://github.com/StatCan/aaw-inferenceservices-controller)           | Kubernetes controller for managing inference services                                         | Public     |
| [aaw-kubeflow-manifest](https://github.com/StatCan/aaw-kubeflow-manifest)                                 | Kustomize installation manifests for Kubeflow                                                 | Public     |
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

| Repository                                                                                                                                  | Description                                                                  | Visibility |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------- |
| [terraform-aaw-managed-databases](https://github.com/StatCan/terraform-aaw-managed-databases)                                               | Terraform to deploy Azure Managed Databases                                  | Private    |
| [terraform-aaw-vault](https://github.com/StatCan/terraform-aaw-vault)                                                                       | Terraform for configuring Hashicorp Vault                                    | Private    |
| [terraform-advanced-analytics-workspaces-infrastructure](https://github.com/StatCan/terraform-advanced-analytics-workspaces-infrastructure) | Terraform to deploy the infrastructure for the Advanced Analytics Workspaces | Private    |
| [terraform-aaw-infrastructure-aaw-dev-cc-00](https://github.com/StatCan/terraform-aaw-infrastructure-aaw-dev-cc-00)                         | Terraform to deploy the AAW infrastructure for the development environment   | Private    |
| [terraform-aaw-infrastructure-aaw-prod-cc-00](https://github.com/StatCan/terraform-aaw-infrastructure-aaw-prod-cc-00)                       | Terraform to deploy the AAW infrastructure for the production environment    | Private    |

## Community Engagement

The following is a list of some of the `collaborative` work we made available to
improve upstream projects.

| Repository                                                                                  | Description                                                 | Visibility |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------- |
| [boathouse](https://github.com/StatCan/boathouse)                                           | Manage Kubernetes storage mounts with Goofys                | Public     |
| [jupyter-apis](https://github.com/StatCan/jupyter-apis)                                     | Golang replacement for the Kubeflow Jupyter Web APIs        | Public     |
| [jupyterlab-language-pack-fr_FR](https://github.com/StatCan/jupyterlab-language-pack-fr_FR) | JupyterLab fr-FR Language Pack                              | Public     |
| [vault-plugin-secrets-minio](https://github.com/StatCan/vault-plugin-secrets-minio)         | Vault plugin which will provision multi-user keys for Minio | Public     |

The following is a list of some of the `forked` projects where we have provided
multilingual support and other UX related enhancements.

| Repository                                                          | Description                                 | Visibility |
| ------------------------------------------------------------------- | ------------------------------------------- | ---------- |
| [kubeflow](https://github.com/StatCan/kubeflow)                     | Multilingual support for Kubeflow           | Public     |
| [kubeflow-pipelines](https://github.com/StatCan/kubeflow-pipelines) | Multilingual support for Kubeflow Pipelines | Public     |
| [minio](https://github.com/StatCan/minio)                           | Multilingual support for MinIO              | Public     |
| [minio-console](https://github.com/StatCan/minio-console)           | Multilingual support for MinIO Console      | Public     |
| [rstudio](https://github.com/StatCan/rstudio)                       | Multilingual support for RStudio            | Public     |
