import os

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.database import DatabaseForPostgresqlServers
from diagrams.custom import Custom

from diagrams.k8s.compute import Deployment, Pod, StatefulSet
from diagrams.k8s.network import NetworkPolicy, Service

from diagrams.onprem.network import Istio

from diagrams.onprem.vcs import Github
from diagrams.onprem.vcs import Gitlab

from diagrams.onprem.gitops import Argocd

def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    with Cluster("aaw-argocd-manifests repo"):
        with Cluster("/profiles-argocd-system/template/"):
            github_manifests = Github(
                "gitea/manifest.yaml"
            )
    with Cluster("gitlab.k8s"):
        with Cluster("aaw-dev-cc-00 repo"):
            gitlab_tf = Gitlab("argocd_operator.tf")
    with Cluster("Azure"):
        postgres = DatabaseForPostgresqlServers("Azure Managed Postgres")
    with Cluster("Kubernetes Cluster"):
        with Cluster("daaas-system namespace"):
            network_controller = Deployment("profiles-controller-network")
            profiles_controller_gitea = Deployment("profiles-controller-gitea")
            profiles_argocd_system = Argocd(
                "profiles-argocd-system"
            )
            profiles_controller_argocd = Argocd(
                "profiles-controller"
            )

        with Cluster("user namespace"):
            gitea_argocd = Argocd("gitea-<user-namespace>")
            gitea_ss = StatefulSet("gitea-0")
            gitea_pod = Pod("gitea-0")
            gitea_postgres = StatefulSet("gitea-postgres-0")
            gitea_http_service = Service("gitea-http")
            istio_vs = Istio("gitea-virtualservice")
            network_policy = NetworkPolicy("gitea-ingress")
        with Cluster("kubeflow namespace"):
            kubeflow_gateway = Istio("kubeflow-gateway")

        # Gitea Statefulset manages a Gitea pod
        gitea_ss >> Edge(style="dashed", color="firebrick") >> gitea_pod

        # Network policy permits kubeflow gateway pods to communicate with pods
        # exposed by the gitea-http service.
        kubeflow_gateway - Edge(style="dashed", color="purple") - network_policy - Edge(
            style="dashed", color="purple"
        ) - gitea_http_service

        # Gitea controller is deployed by the profiles-controller ArgoCD Application
        profiles_controller_argocd >> Edge(color="orange") >> profiles_controller_gitea
        # Gitea controller creates various components in user's namespace
        profiles_controller_gitea >> Edge(color="blue") >> istio_vs
        profiles_controller_gitea >> Edge(color="blue") >> gitea_argocd

        # Network policy controller creates the network policy that allows kubeflow
        # gateway traffic to be sent to gitea pods.
        network_controller >> Edge(color="brown") >> network_policy

        # Network traffic enters through the kubeflow gateway and is routed to the
        # gitea-http service by the Istio VirtualService.
        kubeflow_gateway >> Edge(color="red") >> istio_vs >> Edge(
            color="red"
        ) >> gitea_http_service >> Edge(color="red") >> gitea_pod

        # TODO: Update this with plans for managed postgres
        gitea_ss >> Edge(style="dashed", color="firebrick") >> postgres

        # argocd_operator.tf deploys argocd operator, one argocd installation is the
        # profiles-argocd-system that watches and deploys per-namespace applications.
        gitlab_tf >> Edge(color="orange") >> profiles_argocd_system

        # The ArgoCD Application deployed into a user's namespace watches the
        # /profiles-argocd-system/template/gitea/manifest.yaml which deploys all of
        # the necessary kubernetes resources to deploy a Gitea Statefulset.
        gitea_argocd >> Edge(style="dotted", color="green") >> github_manifests

        github_manifests >> Edge(style="dotted", color="green") >> gitea_ss
        github_manifests >> Edge(style="dotted", color="green") >> gitea_postgres
        github_manifests >> Edge(style="dotted", color="green") >> gitea_http_service

        gitea_argocd >> Edge(color="green") >> gitea_ss
        gitea_argocd >> Edge(color="green") >> gitea_postgres
        gitea_argocd >> Edge(color="green") >> gitea_http_service

        # profiles-argocd-system ArgoCD installation manages gitea-<user-namespace> ArgoCD
        # applications in the user's namespace.
        profiles_argocd_system >> Edge(color="orange") >> gitea_argocd