# Overview

The platform uses [Gitea](https://gitea.io/en-us/) for multitenant (per-namespace) source control. Each namespace that opts-in for source control gets its own dedicated Gitea instances - one for unclassified data, and one for protected-b data.

## Add Gitea Deployment to Kubeflow Profile

We have created an `addGitea` jsonnet function in the [aaw-kubeflow-profiles]() repository. See this [aaw-kubeflow-profiles example](https://github.com/StatCan/aaw-kubeflow-profiles/blob/6a7cb58d880337996d5f02aef46f53680283b5ee/profile-aaw-fc.jsonnet#L4-L6) for how to add Gitea to a Kubeflow profile.

## Feature Deployment

Per-namespace Gitea is handled through the [aaw-kubeflow-profiles-controller](https://github.com/StatCan/aaw-kubeflow-profiles-controller) repository; see the `README.md` of this repository for documentation about how the `aaw-kubeflow-profiles-controller` is updated and deployed.

Responsible for deploying [gitea](https://github.com/go-gitea/gitea) as [argocd](https://github.com/argoproj/argo-cd) applications per `Profile`. Currently, [argocd](https://github.com/argoproj/argo-cd) applications are deployed by the gitea controller based on the customized gitea manifest found [here](https://github.com/StatCan/aaw-argocd-manifests/tree/aaw-dev-cc-00/profiles-argocd-system/template/gitea).

The diagram below highlights the key components involved with the Gitea controller.

![gitea controller](gitea_controller.png)

## Infrastructure Deployment

**Related PRs**:

- [Deploy Profiles Automation ArgoCD App](https://gitlab.k8s.cloud.statcan.ca/cloudnative/aaw/daaas-infrastructure/aaw-prod-cc-00/-/merge_requests/73)
- [Add Postgresql variables and secrets](https://gitlab.k8s.cloud.statcan.ca/cloudnative/aaw/daaas-infrastructure/aaw-prod-cc-00/-/merge_requests/74)