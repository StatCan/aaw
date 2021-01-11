<!-- markdownlint-disable no-bare-urls no-duplicate-header -->

# Data Analytics as a Service

We encourage you to watch our YouTube presentation given at Stratosphere:

- [YouTube](https://www.youtube.com/watch?v=quYuuEAqNm0)
- [SlideDeck](https://govcloud.blob.core.windows.net/docs/daaas-cncf.pdf)

# Table of Contents

1. [Ingresses](#ingresses)
   * [Services](#services)
   * [Elastic Instances](#elastic-stack-instances)
   * [MinIO Instances](#minio-instances)
   * [MLFlow Instances](#mlflow-instances)
1. [GitHub Links](#important-links)
   * [Terraform](#terraform)
   * [Repositories](#repositories)

## Ingresses

A routinely updated list of some of the baseline services offered by the DAaaS platform as a service.

### Services

The fundamental services that can be used to assist you on your data science journey.

- https://analytics-platform.statcan.gc.ca
- https://daaas.covid.cloud.statcan.ca
- https://kubeflow.covid.cloud.statcan.ca
- https://kubecost.covid.cloud.statcan.ca
- https://mlflow.covid.cloud.statcan.ca
- https://grafana.covid.cloud.statcan.ca
- https://shiny.covid.cloud.statcan.ca
- https://vault.covid.cloud.statcan.ca
- https://istio-grafana.covid.cloud.statcan.ca
- https://istio-kiali.covid.cloud.statcan.ca
- https://logging-elastic.covid.cloud.statcan.ca
- https://logging-kibana.covid.cloud.statcan.ca

> **Note**: The list above is non-exhaustive and only reflects a small subset of services.

### Elastic Instances

The [Elastic Cloud](https://github.com/elastic/cloud-on-k8s) operator automates the deployment, provisioning, management, and orchestration of Elasticsearch, Kibana, and Beats on Kubernetes.

- https://elastic.covid.cloud.statcan.ca
- https://kibana.covid.cloud.statcan.ca

> **Note**: You can request your own instance of Elastic + Kibana using our [Web Form](https://daaas.covid.cloud.statcan.ca/forms/request-elastic-instance)

### MinIO Instances

The [MinIO Operator](https://github.com/statcan/minio-operator) automates the deployment, provisioning, management, and orchestration of MinIO and MinIO Console on Kubernetes.

- https://minio-premium-tenant-1.covid.cloud.statcan.ca
- https://minio-console-premium-tenant-1.covid.cloud.statcan.ca
- https://minio-standard-tenant-1.covid.cloud.statcan.ca
- https://minio-console-standard-tenant-1.covid.cloud.statcan.ca

> **Note**: You can request your own instance of MinIO using our [Web Form](https://daaas.covid.cloud.statcan.ca/forms/request-elastic-instance)

### MLFlow Instances

The [MLFlow Operator](https://github.com/statcan/mlflow-operator) automates the deployment, provisioning, management, and orchestration of MLFlow on Kubernetes.

- https://mlflow-standard-tenant-1.covid.cloud.statcan.ca

> **Note**: You can request your own instance of MLFlow using our [Web Form](https://daaas.covid.cloud.statcan.ca/forms/request-elastic-instance)

## GitHub Links

### Terraform

- https://github.com/StatCan/terraform-kubernetes-aks-daaas
- https://github.com/StatCan/terraform-kubernetes-aks-platform-daaas
- https://github.com/StatCan/terraform-kubernetes-aks-daaas-private (private) // [[GitHub Action][github_action_tf_daaas]]
- https://github.com/StatCan/terraform-kubernetes-aks-platform-daaas-private (private) // [[GitHub Action][github_action_tf_daaas_platform]]

### Repositories

- https://github.com/StatCan?q=daaas
- https://github.com/StatCan/actions // [[GitHub Action][github_action_actions]]
- https://github.com/StatCan/boathouse // [[GitHub Action][github_action_boathouse]]
- https://github.com/StatCan/charts // [[GitHub Action][github_action_charts]]
- https://github.com/StatCan/daaas // [[GitHub Action][github_action_daaas]]
- https://github.com/StatCan/daaas-containers // [[GitHub Action][github_action_daaas_containers]]
- https://github.com/StatCan/gatekeeper-policies // [[GitHub Action][github_action_gatekeeper_policies]]
- https://github.com/StatCan/goofys-injector // [[GitHub Action][github_action_goofys_injector]]
- https://github.com/StatCan/gpu-toleration-injector // [[GitHub Action][github_action_gpu_toleration_injector]]
- https://github.com/StatCan/jupyter-apis // [[GitHub Action][github_action_jupyter_apis]]
- https://github.com/StatCan/jupyter-notebooks // [[GitHub Action][github_action_jupyter_notebooks]]
- https://github.com/StatCan/kubecost // [[GitHub Action][github_action_kubecost]]
- https://github.com/StatCan/kubeflow // [[GitHub Action][github_action_kubeflow]]
- https://github.com/StatCan/kubeflow-containers // [[GitHub Action][github_action_kubeflow_containers]]
- https://github.com/StatCan/kubeflow-containers-desktop // [[GitHub Action][github_action_kubeflow_containers_desktop]]
- https://github.com/StatCan/kubeflow-controller // [[GitHub Action][github_action_kubeflow_controller]]
- https://github.com/StatCan/kubeflow-manifest // [[GitHub Action][github_action_kubeflow_manifest]]
- https://github.com/StatCan/kubeflow-mlops // [[GitHub Action][github_action_kubeflow_mlops]]
- https://github.com/StatCan/kubeflow-opa-sync // [[GitHub Action][github_action_kubeflow_opa_sync]]
- https://github.com/StatCan/minio-credential-injector // [[GitHub Action][github_action_minio_credential_injector]]
- https://github.com/StatCan/minio-operator // [[GitHub Action][github_action_minio_operator]]
- https://github.com/StatCan/mlflow-operator // [[GitHub Action][github_action_mlflow_operator]]
- https://github.com/StatCan/namespace-injector // [[GitHub Action][github_action_namespace_injector]]
- https://github.com/StatCan/r-dashboards // [[GitHub Action][github_action_r_dashboards]]
- https://github.com/StatCan/r-notebooks // [[GitHub Action][github_action_r_notebooks]]
- https://github.com/StatCan/shiny // [[GitHub Action][github_action_shiny]]
- https://github.com/StatCan/statcan.orchardcore // [[GitHub Action][github_action_orchardcore]]
- https://github.com/StatCan/vault-plugin-secrets-minio // [[GitHub Action][github_action_vault_plugin_secrets_minio]]

<!-- Links Referenced -->

[github_action_tf_daaas]:                    https://github.com/StatCan/terraform-kubernetes-aks-daaas-private/actions
[github_action_tf_daaas_platform]:           https://github.com/StatCan/terraform-kubernetes-aks-platform-daaas-private/actions
[github_action_tf_daaas_vault]:              https://github.com/StatCan/terraform-vault-daaas/actions
[github_action_actions]:                     https://github.com/StatCan/actions/actions
[github_action_boathouse]:                   https://github.com/StatCan/boathouse/actions
[github_action_charts]:                      https://github.com/StatCan/charts/actions
[github_action_daaas]:                       https://github.com/StatCan/daaas/actions
[github_action_daaas_containers]:            https://github.com/StatCan/daaas-containers/actions
[github_action_gatekeeper_policies]:         https://github.com/StatCan/gatekeeper-policies/actions
[github_action_goofys_injector]:             https://github.com/StatCan/goofys-injector/actions
[github_action_gpu_toleration_injector]:     https://github.com/StatCan/gpu-toleration-injector/actions
[github_action_jupyter_apis]:                https://github.com/StatCan/jupyter-apis/actions
[github_action_jupyter_notebooks]:           https://github.com/StatCan/jupyter-notebooks/actions
[github_action_kubecost]:                    https://github.com/StatCan/kubecost/actions
[github_action_kubeflow]:                    https://github.com/StatCan/kubeflow/actions
[github_action_kubeflow_containers]:         https://github.com/StatCan/kubeflow-containers/actions
[github_action_kubeflow_containers_desktop]: https://github.com/StatCan/kubeflow-containers-desktop/actions
[github_action_kubeflow_controller]:         https://github.com/StatCan/kubeflow-controller/actions
[github_action_kubeflow_manifest]:           https://github.com/StatCan/kubeflow-manifest/actions
[github_action_kubeflow_mlops]:              https://github.com/StatCan/kubeflow-mlops/actions
[github_action_kubeflow_opa_sync]:           https://github.com/StatCan/kubeflow-opa-sync/actions
[github_action_minio_credential_injector]:   https://github.com/StatCan/minio-credential-injector/actions
[github_action_minio_operator]:              https://github.com/StatCan/minio-operator/actions
[github_action_mlflow_operator]:             https://github.com/StatCan/mlflow-operator/actions
[github_action_namespace_injector]:          https://github.com/StatCan/namespace-injector/actions
[github_action_r_dashboards]:                https://github.com/StatCan/r-dashboards/actions
[github_action_r_notebooks]:                 https://github.com/StatCan/r-notebooks/actions
[github_action_shiny]:                       https://github.com/StatCan/shiny/actions
[github_action_orchardcore]:                 https://github.com/StatCan/statcan.orchardcore/actions
[github_action_vault_plugin_secrets_minio]:  https://github.com/StatCan/vault-plugin-secrets-minio/actions
