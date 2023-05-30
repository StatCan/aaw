import os

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.database import DatabaseForPostgresqlServers
from diagrams.custom import Custom
from diagrams.k8s.compute import Deployment, Pod, StatefulSet
from diagrams.k8s.network import NetworkPolicy, Service
from diagrams.k8s.podconfig import Secret
from diagrams.k8s.storage import PersistentVolume, PersistentVolumeClaim
from diagrams.azure.storage import BlobStorage
from diagrams.azure.network import Firewall, RouteTables, DNSPrivateZones, VirtualNetworks
from diagrams.onprem.workflow import Kubeflow
from diagrams.onprem.gitops import Argocd

def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext

with Diagram(myself(), show=False):
    important_icon_width = "3"
    important_icon_height = "3"
    kubeflow_connect_colour = "green"
    azure_colour = "#0080FF"
    connects_with_style = "dashed"
    global_edge_width = "4"
    claims_label = "claims"

    with Cluster("Kubernetes Clusters"):
        # PV
        aaw_pv_user_unclassified_premium = PersistentVolume("user-unclassified")
        aaw_pv_user_unclassified_premium_ro = PersistentVolume("user-unclassified-ro")
        aaw_pv_user_protected_b = PersistentVolume("user-protected-b")
        fdi_pv_user_unclassified = PersistentVolume("fdi-user-pv-unclassified")
        fdi_pv_user_protected_b = PersistentVolume("fdi-user-pv-protected-b")

        with Cluster("user namespace"):
            # PVC
            kubeflow_user_notebook = Kubeflow("kubeflow-notebook", icon_path="icons/kubeflow.png", height=important_icon_height, width=important_icon_width, imagescale="false")
            fdi_pvc_user_unclassified = PersistentVolumeClaim("fdi-user-pvc-unclassified")
            fdi_pvc_user_protected_b = PersistentVolumeClaim("fdi-user-pvc-protected-b")
            aaw_pvc_user_premium_unclassified = PersistentVolumeClaim("aaw-user-pvc-unclassified")
            aaw_pvc_user_premium_unclassified_ro = PersistentVolumeClaim("aaw-user-pvc-unclassified-ro")
            aaw_pvc_user_protected_b = PersistentVolumeClaim("aaw-user-pvc-protected-b")

    with Cluster("Azure"):
        with Cluster("FDI-DEV-RESEARCH"):
            with Cluster("Storage Accounts"):
                with Cluster("fdiunclassdev"):
                    # unclass fdi containers
                    azure_fdi_unclass_dfs = BlobStorage("fdi-user-unclassified-container-adls")
                with Cluster("fdiprotbdev"):
                    # prot-b fdi containers
                    azure_fdi_protb_dfs = BlobStorage("fdi-user-protb-container-adls")
        with Cluster("Storage Accounts"):
            # User containers are created in each storage account for AAW.
            with Cluster("aawdevcc00samgpremium"):
                azure_premium_container = BlobStorage("user-unclassified")
            with Cluster("aawdevcc00samgprotb"):
                azure_protected_b_container = BlobStorage("user-protected-b")

        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> fdi_pvc_user_unclassified \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> fdi_pv_user_unclassified

        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> fdi_pvc_user_protected_b \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> fdi_pv_user_protected_b

        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pvc_user_premium_unclassified \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pv_user_unclassified_premium

        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pvc_user_premium_unclassified_ro \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pv_user_unclassified_premium_ro

        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pvc_user_protected_b \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pv_user_protected_b

        aaw_pv_user_unclassified_premium \
            >> Edge(colour=azure_colour,style=connects_with_style,minlen=global_edge_width) \
            >> azure_premium_container

        aaw_pv_user_unclassified_premium_ro \
            >> Edge(colour=azure_colour,style=connects_with_style,minlen=global_edge_width) \
            >> azure_premium_container

        aaw_pv_user_protected_b \
            >> Edge(colour=azure_colour,style=connects_with_style,minlen=global_edge_width) \
            >> azure_protected_b_container

        fdi_pv_user_unclassified \
            >> Edge(colour=azure_colour,style=connects_with_style,minlen=global_edge_width) \
            >> azure_fdi_unclass_dfs

        fdi_pv_user_protected_b \
            >> Edge(colour=azure_colour,style=connects_with_style,minlen=global_edge_width) \
            >> azure_fdi_protb_dfs