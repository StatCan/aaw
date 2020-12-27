## v1.0.0 @ [statcan/kubeflow-containers](https://github.com/statcan/kubeflow-containers/releases/tag/v1.0.0)

Features / Updates:

- Update to jupyter/datascience-notebook
  - Update base image to jupyter/datascience-notebook:42f4c82a07ff
  - Refined container image list to JupyterLab-CPU, JupyterLab-PyTorch, JupyterLab-Tensorflow, and RStudio
  - Updated to Docker Bits hierarchical structure
- Update Visual Studio code-server to [v3.8.0](https://github.com/cdr/code-server/releases/tag/v3.8.0)
  - Added default extensions Python and R
  - Revert to Dark theme

> **Note**: N/A

## v1.0.0 @ [statcan/kubeflow-manifest](https://github.com/statcan/kubeflow-manifest/releases/tag/v1.0.0)

Features / Updates:

- Update to Kubeflow [v1.2.0](https://github.com/kubeflow/kubeflow/releases/tag/v1.2.0)
  - Updated to v1.2.0 of Kubeflow
  - Updated to new Kustomize format [kubeflow-5440](https://github.com/kubeflow/kubeflow/issues/5440)
  - Enabled Multi User pipelines
  - Disabled endpoints for GKE

> **Note**: As of this release we now have Multi-User Pipelines support. Please see the following issue for more information at [kubeflow-5440](https://github.com/kubeflow/kubeflow/issues/5440)

## v1.0.0 @ [statcan/minio-operator](https://github.com/statcan/minio-operator/releases/tag/v1.0.0)

Features / Updates:

- Update for MinIO Operator [v3.0.29](https://github.com/minio/operator/releases/tag/v3.0.29)
  - Updated to v3.0.29 of the MinIO Operator image
  - Deprecation of older MinIO tenants in favor of standard and premium
  - Addition of new Open Policy Agent rules
  - Synced the old tenants to the new tenants
- Update for MinIO Console [v0.4.6](https://github.com/minio/console/releases/tag/v0.4.6)
  - Updated to v0.4.6 of the MinIO Console image
- Update for MinIO Server [RELEASE.2020-12-10T01-54-29Z](https://github.com/minio/minio/tree/RELEASE.2020-12-10T01-54-29Z)
  - Updated to RELEASE.2020-12-10T01-54-29Z of the MinIO Server image

> **Note**: This was unfortunately a breaking change as we were initially using a very early alpha release. Please see the following issue for more information at [daaas-300](https://github.com/StatCan/daaas/issues/300)
