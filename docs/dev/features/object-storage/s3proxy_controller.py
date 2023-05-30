import os

from diagrams import Cluster, Diagram, Edge

from diagrams.k8s.podconfig import CM

from diagrams.k8s.network import Service
from diagrams.k8s.network import NetworkPolicy

from diagrams.k8s.group import NS
from diagrams.k8s.compute import Deployment

from diagrams.onprem.workflow import Kubeflow

from diagrams.onprem.gitops import Argocd

from diagrams.onprem.vcs import Github

from diagrams.onprem.network import Istio


def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    with Cluster("aks-cluster"):
        with Cluster("daaas-system"):
            s3proxy_controller = Deployment("profiles-controller-s3proxy")
        with Cluster("user-namespace"):
            profile = Kubeflow("user-profile")
            ns = NS("user-namespace")
            virtual_service = Istio("user-virtual-service")
            nginx_cm = CM("nginx-config")
            argocd_app = Argocd("s3proxy")
            s3proxy = Deployment("s3proxy")
            s3proxy_svc = Service("s3proxy")
            web_svc = Service("s3proxy-web")
            s3proxy_cm = CM("s3proxy-config")
            allow_pro_b_nb_to_s3proxy = NetworkPolicy("allow-protected-b-notebook-to-s3proxy")
            allow_s3proxy_from_pro_b_nb = NetworkPolicy("allow-s3proxy-from-protected-b-notebook")
    with Cluster("github"):
        github_repo = Github("aaw-argocd-manifests")

    # s3proxy controller watches kubeflow profiles and deploys vs, cm, and argocd app
    s3proxy_controller >> Edge(label="watches", color="black", style="dashed") >> profile
    s3proxy_controller >> Edge(label="deploys", color="green", style="dashed") >> virtual_service
    s3proxy_controller >> Edge(label="deploys", color="green", style="dashed") >> nginx_cm
    s3proxy_controller >> Edge(label="deploys", color="green", style="dashed") >> argocd_app

    # Argocd app watches aaw-argocd-manifests repo and deploys services, cm, and deployment
    argocd_app >> Edge(label="watches", color="black", style="dashed") >> github_repo
    argocd_app >> Edge(label="deploys", color="green", style="dashed") >> s3proxy
    argocd_app >> Edge(label="deploys", color="green", style="dashed") >> s3proxy_svc
    argocd_app >> Edge(label="deploys", color="green", style="dashed") >> web_svc
    argocd_app >> Edge(label="deploys", color="green", style="dashed") >> s3proxy_cm
    argocd_app >> Edge(label="deploys", color="green", style="dashed") >> allow_pro_b_nb_to_s3proxy
    argocd_app >> Edge(label="deploys", color="green", style="dashed") >> allow_s3proxy_from_pro_b_nb


