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
    """Diagram class for the blob-csi system. The diagram includes most of the system from terraform, github,
    argocd, kubernetes and azure. Some intricacies related to azure subscription, node pools and netowrking have
    been ommitted in the interest of simplicity."""

    tf_colour = "purple"
    azure_colour = "#0080FF"
    kubernetes_colour = "navyblue"
    kubeflow_connect_colour = "green"
    argocd_colour = "orange"

    mounts_label = "mounts"
    deploy_label = "deploys"
    provision_label = "provisions"
    queries_label = "queries"
    watches_label = "watches"
    connects_label = "connects"
    allows_egress_label = "allows egress"
    allows_ingress_label = "allows ingress"
    claims_label = "claims"
    connects_with_style = "dashed"
    auth_label = "authenticates with"

    # Node scaling
    important_icon_width = "3"
    important_icon_height = "3"
    # Edge Scaling

    global_edge_width = "6"
    # To check for edge widths using ctrl-f: use this regex pattern: , minlen=(?:(?!\)).)*

    # Terraform declarations
    with Cluster("gitlab.k8s"):
        # https://gitlab.k8s.cloud.statcan.ca/cloudnative/aaw/daaas-infrastructure/aaw-dev-cc-00
        with Cluster("aaw-dev-cc-00 repo"):
            with Cluster("argocd_operator.tf"):
                tf_argocd_operator = Custom("argocd_operator", icon_path="img/terraform.png")
            with Cluster("azure-blob-csi-system.tf"):
                tf_aaw_premium_unclassified_secret = Custom("aawdevcc00samgpremium", icon_path="img/terraform.png")
                tf_aaw_protb_secret = Custom("aawdevcc00samgprotb", icon_path="img/terraform.png")
                tf_azure_blob_prot_b_secret = Custom("azure_blob_csi_fdi_protected_b", icon_path="img/terraform.png")
                tf_azure_blob_prot_b_spn_secret = Custom("azure_blob_csi_fdi_protected_b_spn", icon_path="img/terraform.png")
                tf_azure_blob_unclass_secret = Custom("azure_blob_csi_fdi_unclassified", icon_path="img/terraform.png")
                tf_azure_blob_unclass_spn_secret = Custom("azure_blob_csi_fdi_unclassified_spn", icon_path="img/terraform.png")
            with Cluster("fdi_gateway.tf"):
                tf_opa_gateway_unclassified = Custom("fdi_opa_gateway_unclassified", icon_path="img/terraform.png")
                tf_opa_gateway_protected_b = Custom("fdi_opa_gateway_protb", icon_path="img/terraform.png")
        # https://gitlab.k8s.cloud.statcan.ca/cloudnative/aaw/terraform-advanced-analytics-workspaces-infrastructure/-/tree/main/
        with Cluster("Advanced Analytics Workspace Infrastructure"):
            with Cluster("dns.tf"):
                # private dns zone, link and record
                tf_fdi_private_dns = Custom("azurerm_private_dns_zone", icon_path="img/terraform.png")
                tf_fdi_vnet_link = Custom("azurerm_private_dns_zone_virtual_network_link", icon_path="img/terraform.png")
                tf_fdi_dns_record = Custom("azurerm_private_dns_a_record", icon_path="img/terraform.png")
            with Cluster("dev_cc_00.tf"):
                # firewall route and rule
                tf_aaw_to_fdi_protb_route = Custom("azurerm_route", icon_path="img/terraform.png")
                with Cluster("azurerm_firewall_policy_rule_collection_group"):
                    tf_aaw_fdi_protb_firewall_rule = Custom("aaw_dev_cc_00_fdi_protb", icon_path="img/terraform.png")

    with Cluster("github.com"):
        # https://github.com/StatCan/aaw-network-policies
        with Cluster("aaw-network-policies repo"):
            with Cluster("azure-blob-csi-system.yaml"):
                github_allow_blob_csi_to_internet = Custom("allow-azure-blob-csi-to-internet", icon_path="img/github.png")
                github_allow_egress_pcont_opa_protb = Custom("allow-egress-profiles-controller-to-fdi-opa-gateway-protected-b", icon_path="img/github.png")
                github_allow_egress_pcont_opa_unclass = Custom("allow-egress-profiles-controller-to-fdi-opa-gateway-unclassified", icon_path="img/github.png")
                github_allow_ingress_pcont_opa_protb = Custom("allow-ingress-profiles-controller-to-fdi-opa-gateway-protected-b", icon_path="img/github.png")
                github_allow_ingress_pcont_opa_unclass = Custom("allow-ingress-profiles-controller-to-fdi-opa-gateway-unclassified", icon_path="img/github.png")
            with Cluster("daaas-system.yaml"):
                github_allow_profiles_controller_to_internet = Custom("allow-profile-controller-to-internet", icon_path="img/github.png")
        with Cluster("aaw-argocd-manifests repo"):
            # blob-csi controller deployment
            with Cluster("/daaas-system/profile-controllers/profiles-controller"):
                github_blobcsi_profiles_controller = Custom("profiles-controller", icon_path="img/github.png")
            # blob-csi driver deployment
            with Cluster("/daaas-system/blob-csi-driver"):
                github_blob_csi_driver = Custom("blob-csi-driver", icon_path="img/github.png")

        # blob-csi injector
        # with Cluster("/daaas-system/blob-csi-injector"):
            # argman_blob_csi_injector = Custom("blob-csi-injector", icon_path="img/github.png")

    with Cluster("Azure"):
        with Cluster("FDI-DEV-RESEARCH"):
            with Cluster("Storage Accounts"):
                with Cluster("fdiunclassdev"):
                    # unclass fdi containers
                    azure_fdi_unclass_dfs = BlobStorage("fdi-user-unclassified-container-adls")
                with Cluster("fdiprotbdev"):
                    # prot-b fdi containers
                    azure_fdi_protb_dfs = BlobStorage("fdi-user-protb-container-adls")
                with Cluster("fdiminioextmeta"):
                    #user-protb-containeo internal and external-opa containers store opa bundles
                    fdi_protb_bundle = BlobStorage("fdi-protb-bundle")
                    fdi_unclass_bundle = BlobStorage("fdi-unclass-bundle")
        with Cluster("Storage Accounts"):
            # User containers are created in each storage account for AAW.
            with Cluster("aawdevcc00samgpremium"):
                azure_unclassified_container = BlobStorage("user-unclassified")
            with Cluster("aawdevcc00samgprotb"):
                azure_protected_b_container = BlobStorage("user-protected-b")

        with Cluster("Networking"):
            # FDI firewall configuration that allows protected-b connectivity from AAW prot-b nodepool
            fdi_private_dns = DNSPrivateZones("dfs")
            fdi_vnet_link = VirtualNetworks("aaw_dev_cc_00_dfs")
            fdi_dns_record = DNSPrivateZones("fdipvprotb_dev_dfs") # no icon exists for a record yet, so use zones icon

            fdi_aaw_to_fdi_protb_route = RouteTables("aaw_dev_cc_00_to_fdi_protb")
            fdi_aaw_to_fdi_firewall_rule = Firewall("aks-dev-to-fdi-dev-storage")

    with Cluster("Kubernetes Cluster"):
        # PV
        aaw_pv_user_unclassified = PersistentVolume("user-unclassified")
        aaw_pv_user_unclassified_ro = PersistentVolume("user-unclassified-ro")
        aaw_pv_user_protected_b = PersistentVolume("user-protected-b")
        fdi_pv_user_unclassified = PersistentVolume("fdi-user-pv-unclassified")
        fdi_pv_user_protected_b = PersistentVolume("fdi-user-pv-protected-b")

        with Cluster("argocd-operator-system"):
            argocd_operator = Argocd("argocd-operator", icon_path="img/argo.png", height=important_icon_height, width=important_icon_width, imagescale="false")

        with Cluster("daaas-system"):
            # profiles controller
            blobcsi_profiles_controller = Pod("blob-csi.go", height=important_icon_height,
                width=important_icon_width, imagescale="false")
            allow_profiles_controller_to_internet = NetworkPolicy("allow-profile-controller-to-internet")
            allow_egress_pcont_opa_protb = NetworkPolicy("allow-egress-profiles-controller-to-fdi-opa-gateway-protected-b")
            allow_egress_pcont_opa_unclass = NetworkPolicy("allow-egress-profiles-controller-to-fdi-opa-gateway-unclassified")
            # blob_csi_injector = Pod("blob-csi-injector")

        with Cluster("user namespace"):
            # PVC
            aaw_pvc_user_unclassified = PersistentVolumeClaim("aaw-user-pvc-unclassified")
            aaw_pvc_user_unclassified_ro = PersistentVolumeClaim("aaw-user-pvc-unclassified-ro")
            aaw_pvc_user_protected_b = PersistentVolumeClaim("aaw-user-pvc-protected-b")
            fdi_pvc_user_unclassified = PersistentVolumeClaim("fdi-user-pvc-unclassified")
            fdi_pvc_user_protected_b = PersistentVolumeClaim("fdi-user-pvc-protected-b")
            kubeflow_user_notebook = Kubeflow("kubeflow-notebook", icon_path="img/kubeflow.png", height=important_icon_height,
                width=important_icon_width, imagescale="false")

        with Cluster("fdi-gateway-unclassified-system"):
            # minio-gateway-opa pod (opa gateway that controller queries)
            minio_gateway_opa_unclassified = Pod("minio-gateway-opa")
            bundle_secret_unclassified     = Secret("bundle-secret")
            allow_ingress_pcont_opa_unclass = NetworkPolicy("allow-ingress-fdi-opa-gateway-unclassified-from-profiles-controller")
        with Cluster("fdi-gateway-protected-b-system"):
            # minio-gateway-opa pod (opa gateway that controller queries)
            minio_gateway_opa_protected_b = Pod("minio-gateway-opa")
            bundle_secret_protected_b     = Secret("bundle-secret")
            allow_ingress_pcont_opa_protb = NetworkPolicy("allow-ingress-fdi-opa-gateway-protected-b-from-profiles-controller")
        with Cluster("azure-blob-csi-system"):
            # pods
            # blob-csi-driver
            blob_csi_driver = Pod("blob-csi-driver", height=important_icon_height,
                width=important_icon_width, imagescale="false")
            # secrets
            aaw_premium__unclassified_secret = Secret("aawdevcc00samgpremium")
            aaw_protb_secret = Secret("aawdevcc00samgprotb")
            azure_blob_prot_b_secret = Secret("azure-blob-csi-fdi-protected-b")
            azure_blob_prot_b_spn_secret = Secret("azure-blob-csi-fdi-protected-b-spn")
            azure_blob_unclass_secret = Secret("azure-blob-csi-fdi-unclassified")
            azure_blob_unclass_spn_secret = Secret("azure-blob-csi-fdi-unclassified-spn")

            allow_blob_csi_to_internet = NetworkPolicy("allow-azure-blob-csi-to-internet")

        # ----- Deployments ----- #
        # Terraform deploys the argocd operator
        tf_argocd_operator >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> argocd_operator
        # Argocd manages the continuous deployment of the blobcsi controller, blobcsi driver,
        # netpols (and much much more (not in picture due to scope)
        argocd_operator << Edge(color=argocd_colour, xlabel=watches_label, minlen="1") << [github_blobcsi_profiles_controller,
            github_blob_csi_driver,
            github_allow_blob_csi_to_internet,
            github_allow_egress_pcont_opa_protb,
            github_allow_egress_pcont_opa_unclass,
            github_allow_ingress_pcont_opa_protb,
            github_allow_ingress_pcont_opa_unclass,
            github_allow_profiles_controller_to_internet]

        argocd_operator - Edge(color=argocd_colour, xlabel=deploy_label, minlen=global_edge_width) >> [allow_blob_csi_to_internet,
            allow_egress_pcont_opa_protb,
            allow_egress_pcont_opa_unclass,
            allow_ingress_pcont_opa_protb,
            allow_ingress_pcont_opa_unclass,
            allow_profiles_controller_to_internet,
            blob_csi_driver,
            blobcsi_profiles_controller]

        # Terraform deploys the below secrets
        tf_aaw_premium_unclassified_secret >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> aaw_premium__unclassified_secret
        tf_aaw_protb_secret >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> aaw_protb_secret
        tf_azure_blob_prot_b_secret >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> azure_blob_prot_b_secret
        tf_azure_blob_prot_b_spn_secret >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> azure_blob_prot_b_spn_secret
        tf_azure_blob_unclass_secret >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> azure_blob_unclass_secret
        tf_azure_blob_unclass_spn_secret >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> azure_blob_unclass_spn_secret

        # Terraform deploys the unclassified and prot-b opa gateways
        tf_opa_gateway_unclassified >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> [minio_gateway_opa_unclassified, bundle_secret_unclassified]
        tf_opa_gateway_protected_b >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) >> [minio_gateway_opa_protected_b, bundle_secret_protected_b]

        # Terraform deploys firewall rules for FDI integration
        tf_fdi_private_dns >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) \
            >> fdi_private_dns
        tf_fdi_vnet_link >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) \
            >> fdi_vnet_link
        tf_fdi_dns_record >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) \
            >> fdi_dns_record
        tf_aaw_to_fdi_protb_route >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) \
            >> fdi_aaw_to_fdi_protb_route
        tf_aaw_fdi_protb_firewall_rule >> Edge(color=tf_colour, xlabel=deploy_label, minlen=global_edge_width) \
            >> fdi_aaw_to_fdi_firewall_rule
        # Blobcsi controller provisions the following
        blobcsi_profiles_controller >> Edge(color=kubernetes_colour, xlabel=provision_label, minlen=global_edge_width) >> [
            # PVs
            aaw_pv_user_unclassified,
            aaw_pv_user_unclassified_ro,
            aaw_pv_user_protected_b,
            fdi_pv_user_unclassified,
            fdi_pvc_user_protected_b,
            # PVCs
            fdi_pvc_user_unclassified,
            fdi_pv_user_protected_b
        ]

        # blobcsi controller creates azure containers per user for AAW
        blobcsi_profiles_controller \
            >> Edge(color=kubernetes_colour, xlabel=auth_label, minlen=global_edge_width) \
            >> aaw_premium__unclassified_secret \
            >> Edge(color=kubernetes_colour, minlen=global_edge_width) \
            >> allow_profiles_controller_to_internet \
            >> Edge(color=azure_colour, xlabel=provision_label, minlen=global_edge_width) \
            >> azure_unclassified_container
        blobcsi_profiles_controller \
            >> Edge(color=kubernetes_colour, xlabel=auth_label, minlen=global_edge_width) \
            >> aaw_protb_secret \
            >> Edge(color=kubernetes_colour, minlen=global_edge_width) \
            >> allow_profiles_controller_to_internet \
            >> Edge(color=azure_colour, xlabel=provision_label, minlen=global_edge_width) \
            >> azure_protected_b_container

        # Blobcsi controller provisions FDI PVs after querying OPA gateways for permissions
        blobcsi_profiles_controller  \
            >> Edge(color=kubernetes_colour, style=connects_with_style, minlen=global_edge_width) \
            >> allow_egress_pcont_opa_unclass \
            >> Edge(color=kubernetes_colour, style=connects_with_style, minlen=global_edge_width) \
            >> allow_ingress_pcont_opa_unclass \
            >> Edge(color=kubernetes_colour, style=connects_with_style, minlen=global_edge_width) \
            >> minio_gateway_opa_unclassified \

        blobcsi_profiles_controller \
            >> Edge(color=kubernetes_colour, style=connects_with_style, minlen=global_edge_width) \
            >> allow_egress_pcont_opa_protb \
            >> Edge(color=kubernetes_colour, style=connects_with_style, minlen=global_edge_width) \
            >> allow_ingress_pcont_opa_protb \
            >> Edge(color=kubernetes_colour, style=connects_with_style, minlen=global_edge_width) \
            >> minio_gateway_opa_protected_b \

        # OPA Gateways supply the profiles controller by providing
        # http endpoints serving bundles as json responses to get requests
        minio_gateway_opa_unclassified \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=auth_label, minlen=global_edge_width) \
            >> bundle_secret_unclassified \
            >> Edge(color=azure_colour, style=connects_with_style, minlen=global_edge_width) \
            >> fdi_unclass_bundle \


        minio_gateway_opa_protected_b \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=auth_label, minlen=global_edge_width) \
            >> bundle_secret_protected_b \
            >> Edge(color=azure_colour, style=connects_with_style, minlen=global_edge_width) \
            >> fdi_protb_bundle \

        # blob-csi driver mounts AAW specific PVs to azure containers auth with storage account and storage account key
        blob_csi_driver \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> aaw_pv_user_unclassified \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=auth_label, minlen=global_edge_width) \
            >> aaw_premium__unclassified_secret \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> allow_blob_csi_to_internet \
            >> Edge(color=azure_colour, style=connects_with_style, xlabel=mounts_label, minlen=global_edge_width) \
            >> azure_unclassified_container

        blob_csi_driver \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> aaw_pv_user_unclassified_ro \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=auth_label, minlen=global_edge_width) \
            >> aaw_premium__unclassified_secret \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> allow_blob_csi_to_internet \
            >> Edge(color=azure_colour, style=connects_with_style, xlabel=mounts_label, minlen=global_edge_width) \
            >> azure_unclassified_container

        blob_csi_driver \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> aaw_pv_user_protected_b \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=auth_label, minlen=global_edge_width) \
            >> aaw_protb_secret \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> allow_blob_csi_to_internet \
            >> Edge(color=azure_colour, style=connects_with_style, xlabel=mounts_label, minlen=global_edge_width) \
            >> azure_protected_b_container

        # blob-csi driver mounts fdi PVs using service principal auth
        blob_csi_driver \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> fdi_pv_user_unclassified \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=auth_label, minlen=global_edge_width) \
            >> [azure_blob_unclass_spn_secret, azure_blob_unclass_secret] \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> allow_blob_csi_to_internet \
            >> Edge(color=azure_colour, style=connects_with_style, xlabel=mounts_label, minlen=global_edge_width) \
            >> azure_fdi_unclass_dfs

        blob_csi_driver \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> fdi_pv_user_protected_b \
            >> Edge(color=kubernetes_colour, style=connects_with_style, xlabel=auth_label, minlen=global_edge_width) \
            >> [azure_blob_prot_b_spn_secret, azure_blob_prot_b_secret] \
            >> Edge(color=azure_colour, style=connects_with_style, xlabel=connects_label, minlen=global_edge_width) \
            >> fdi_aaw_to_fdi_firewall_rule \
            >> Edge(color=azure_colour, style=connects_with_style, xlabel=mounts_label, minlen=global_edge_width) \
            >> azure_fdi_protb_dfs

        # Kubeflow users can now use their provisioned (and mounted) PV's through a PVC in their namespace :)
        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pvc_user_unclassified \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pv_user_unclassified
        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pvc_user_unclassified_ro \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pv_user_unclassified_ro
        kubeflow_user_notebook \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pvc_user_protected_b \
            >> Edge(color=kubeflow_connect_colour, style=connects_with_style, xlabel=claims_label, minlen=global_edge_width) \
            >> aaw_pv_user_protected_b

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
        # Implement logic for how blob-csi-driver mounts PV's from:
        # 3. Ensure that connections are setup from kubeflow to fdi pvcs
        # 4. Double check everything looks good, and try to optimize diagram layout and directionality