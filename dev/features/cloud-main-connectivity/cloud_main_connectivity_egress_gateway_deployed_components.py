import os

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.compute import AKS
from diagrams.custom import Custom
from diagrams.k8s.others import CRD
from diagrams.k8s.compute import Deployment
from diagrams.k8s.group import NS
from diagrams.k8s.network import NetworkPolicy
from diagrams.k8s.rbac import RoleBinding, Role, ServiceAccount
from diagrams.k8s.podconfig import Secret
from diagrams.onprem.compute import Server

from diagrams.onprem.network import Istio


def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    cnn_site = Server("edition.cnn.com")
    with Cluster("aaw-dev-cc-00"):
        aaw_dev_cc_00 = AKS("aaw-dev-cc-00")
        with Cluster("istio-operator-system"):
            istio_operator_system_ns = NS("istio-operator-system")
            istio_operator_controller = Deployment("istio-operator")
        with Cluster("cloud-main-system"):
            cloud_main_system_ns = NS("cloud-main-system")
            cnn_egress_gateway_debug = Deployment("cnn-egress-gateway-debug")
            cnn_egress_gateway_debug_sa = ServiceAccount("cnn-egress-gateway-debug-sa")
            cnn_egress_gateway_debug_sa_token = Secret("cnn-egress-gateway-debug-sa-token")
            istio_operator = CRD("cnn-egress-gateway-debug")
            # rbac
            allow_get_secrets_role = Role("allow-get-secrets")
            allow_get_secrets_rb = RoleBinding("allow-get-secrets")
            # network policy
            allow_ingress_from_collin_brown = NetworkPolicy("allow-ingress-from-collin-brown")
            # istio
            cnn_gateway = Istio("cnn-gateway")
        with Cluster("collin-brown"):
            collin_brown_ns = NS("collin-brown")
            jupyter_notebook = Custom("test-employee-notebook", icon_path="img/jupyter.png")
            # network policy
            allow_egress_to_cloud_main = NetworkPolicy("allow-egress-to-cloud-main")
            # istio
            cnn_virtual_service = Istio("cnn-virtual-service")
            cnn_destination_rule = Istio("cnn-destination-rule")
            cnn_service_entry = Istio("cnn-service-entry")

        # Istio Operator Controller watches a set of namespaces for deployments of IstioOperator resources
        istio_operator_controller >> Edge(style="dashed", color="black", label="watches") >> cloud_main_system_ns
        # IstioOperator currently deploys an egress gateway into the `cloud-main-system` namespace
        istio_operator >> Edge(style="dashed", color="purple", label="deploys") >> cnn_egress_gateway_debug
        # IstioOperator deploys service account and secret with service account JWT into cloud-main-system namespace
        istio_operator >> Edge(style="dashed", color="purple", label="deploys") >> cnn_egress_gateway_debug_sa
        istio_operator >> Edge(style="dashed", color="purple", label="deploys") >> cnn_egress_gateway_debug_sa_token

        # cnn_egress_gateway_debug pod runs under cnn_egress_gateway_debug_sa service account
        cnn_egress_gateway_debug >> Edge(style="dashed", color="black", label="runs under") >> cnn_egress_gateway_debug_sa
        # Rolebinding allows pods running under cnn_egress_gateway_debug service account to get secrets in the cloud-main-system namespace
        cnn_egress_gateway_debug_sa - Edge(style="dashed", color="black") - allow_get_secrets_rb -  Edge(style="dashed", color="black") - allow_get_secrets_role

        # Istio Gateway resource configures egress gateway
        cnn_gateway >> Edge(style="dashed", color="brown", label="configures") >> cnn_egress_gateway_debug

        # Service entry adds the external site edition.cnn.com to the service mesh
        cnn_service_entry >> Edge(style="dashed", color="blue", label="adds to mesh") >> cnn_site

        # Istio configurations are exported to relevant namespaces
        cnn_destination_rule >> Edge(style="dashed", color="blue", label="exports") >> cloud_main_system_ns
        cnn_destination_rule >> Edge(style="dashed", color="blue", label="exports") >> collin_brown_ns

        cnn_service_entry >> Edge(style="dashed", color="blue", label="exports") >> cloud_main_system_ns
        cnn_service_entry >> Edge(style="dashed", color="blue", label="exports") >> collin_brown_ns

        cnn_virtual_service >> Edge(style="dashed", color="blue", label="exports") >> cloud_main_system_ns
        cnn_virtual_service >> Edge(style="dashed", color="blue", label="exports") >> collin_brown_ns