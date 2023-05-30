
import os
from diagrams import Cluster, Diagram, Edge

from diagrams.custom import Custom

from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker

from diagrams.k8s.network import Service
from diagrams.k8s.network import NetworkPolicy

from diagrams.k8s.group import NS
from diagrams.k8s.compute import Pod

from diagrams.k8s.storage import Volume
from diagrams.k8s.storage import PersistentVolume
from diagrams.k8s.storage import PersistentVolumeClaim

from diagrams.onprem.network import Istio
from diagrams.onprem.network import Envoy

def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    with Cluster("browser"):
        browser = Custom("browser", icon_path="img/browser.png")
    with Cluster("aks-cluster"):
        with Cluster("istio-system"):
            ingress_gateway = Istio("kubeflow-ingress-gateway?")
        with Cluster("user-namespace-pb"):
            ns = NS("user-namespace-pb")
            svc = Service("s3proxy-protected-b")
            svc_web = Service("s3proxy-protected-b-web")
            pro_b_notebook = Pod("noVNC-pro-b")
            allow_pro_b_nb_to_s3proxy = NetworkPolicy("allow-protected-b-notebook-to-s3proxy")
            allow_s3proxy_from_pro_b_nb = NetworkPolicy("allow-s3proxy-from-protected-b-notebook")
            with Cluster("s3proxy-protected-b-pod"):
                s3proxy_pod = Pod("s3proxy-pod")
                nginx = Docker("nginx")
                s3proxy = Docker("s3proxy")
                protected_b_volume = Volume("protected-b")
                protected_b_pvc = PersistentVolumeClaim("blob-csi-protected-b")
        premium_pv = PersistentVolume("blob-csi-pv")

    # User is in noVNC notebook and desktop environment is streamed to browser through VDI.
    browser - Edge(label="vdi", color="green") - ingress_gateway
    ingress_gateway - Edge(label="vdi", color="green") - pro_b_notebook

    # protected-b pod communicates to the s3proxy-web service directly
    pro_b_notebook >> Edge(label="API calls to s3proxy", color="green") >> svc
    pro_b_notebook >> Edge(label="static files", color="green") >> svc_web

    # ingress gateway forwards request to s3proxy service
    svc >> Edge(label="API calls to s3proxy", color="green") >> nginx
    svc_web >> Edge(label="static files", color="green") >> nginx

    # AJAX calls to s3proxy service pass through to s3proxy container
    nginx >> Edge(label="s3 API calls", color="green") >> s3proxy

    # s3proxy runs in filesystem mode, where the volume containing the filesystem is
    # mounted by blob-fuse
    s3proxy >> Edge(label="backed by", style="dashed", color="black") >> protected_b_volume

    # premium volume mounts to pod
    protected_b_volume >> Edge(label="mounts", style="dashed", color="black") >> s3proxy_pod

    # premium volume is provisioned by a namespaced persistent volume claim
    protected_b_pvc - Edge(label="binds", style="dashed", color="black") - protected_b_volume
    protected_b_pvc - Edge(label="binds", style="dashed", color="black") - premium_pv
