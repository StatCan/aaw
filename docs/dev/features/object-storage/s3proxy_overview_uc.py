
import os
from diagrams import Cluster, Diagram, Edge

from diagrams.custom import Custom

from diagrams.onprem.container import Docker


from diagrams.k8s.network import Service
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
        service_worker = Custom("service-worker", icon_path="img/setting-gears.png")
    with Cluster("aks-cluster"):
        with Cluster("istio-system"):
            ingress_gateway = Istio("istio-kubeflow-ingress-gateway")
            envoy_filter = Envoy("EnvoyFilter")
        with Cluster("user-namespace"):
            ns = NS("user-namespace")
            virtual_service = Istio("user-virtual-service")
            svc = Service("s3proxy-web")
            with Cluster("s3proxy-pod"):
                s3proxy_pod = Pod("s3proxy-pod")
                nginx = Docker("nginx")
                s3proxy = Docker("s3proxy")
                unclassified_volume = Volume("unclassified")
                unclassified_pvc = PersistentVolumeClaim("blob-csi-unclassified")
        premium_pv = PersistentVolume("blob-csi-pv")

    # Requests to `/unclassified` or `/unclassified-ro` or `/protected-b` get intercepted by service worker
    browser >> Edge(label="request", color="green") >> service_worker

    # request enters the cluster through the kubeflow ingress gateway
    service_worker >> Edge(label="request", color="green") >> ingress_gateway

    # ingress gateway forwards request to s3proxy service
    ingress_gateway >> Edge(label="request", color="green") >> svc
    svc >> Edge(label="static files", color="green") >> nginx

    # AJAX calls to s3proxy service pass through to s3proxy container
    nginx >> Edge(label="s3 API calls", color="green") >> s3proxy

    # Virtual service configures routes for requests to the user's s3proxy service
    virtual_service >> Edge(label="configures", style="dashed", color="black") >> ingress_gateway

    # Envoy Filter configures kubeflow ingress gateway
    envoy_filter >> Edge(label="configures", style="dashed", color="black") >> ingress_gateway

    # s3proxy runs in filesystem mode, where the volume containing the filesystem is
    # mounted by blob-fuse
    s3proxy >> Edge(label="backed by", style="dashed", color="black") >> unclassified_volume

    # premium volume mounts to pod
    unclassified_volume >> Edge(label="mounts", style="dashed", color="black") >> s3proxy_pod

    # premium volume is provisioned by a namespaced persistent volume claim
    unclassified_pvc - Edge(label="binds", style="dashed", color="black") - unclassified_volume
    unclassified_pvc - Edge(label="binds", style="dashed", color="black") - premium_pv
