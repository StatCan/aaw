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


        # cnn_egress_gateway_debug pod runs under cnn_egress_gateway_debug_sa service account
        cnn_egress_gateway_debug >> Edge(style="dashed", color="black", label="runs under") >> cnn_egress_gateway_debug_sa
        # Rolebinding allows pods running under cnn_egress_gateway_debug service account to get secrets in the cloud-main-system namespace
        cnn_egress_gateway_debug_sa - Edge(style="dashed", color="black") - allow_get_secrets_rb -  Edge(style="dashed", color="black") - allow_get_secrets_role

        # Network policies are set up in both directions to allow ingress from collin-brown and egress to cloud-main-system
        allow_egress_to_cloud_main - Edge(style="dashed", color="green", label="allows") - cloud_main_system_ns
        allow_ingress_from_collin_brown - Edge(style="dashed", color="green", label="allows") - collin_brown_ns

        # VirtualService routes requests to edition.cnn.com to the egress gateway in `cloud-main-system`
        jupyter_notebook >> Edge(color="green", label="routes") >> cnn_virtual_service
        # Virtual services describe **how you route your traffic to a given destination**, while destination rules
        # describe what happens to traffic for that destination. In our case, the destination rule
        # simply has the traffic routed directly to the egress gateway.
        cnn_virtual_service >> Edge(color="green",label="routes") >> cnn_destination_rule
        cnn_destination_rule >> Edge(color="green",label="routes") >> cnn_egress_gateway_debug
        # The ServiceEntry adds the external service (edition.cnn.com) to Istio's service mesh so that
        # routing logic can be applied to the external service.
        cnn_egress_gateway_debug >> Edge(color="green",label="routes") >> cnn_service_entry
        cnn_service_entry >> Edge(color="green",label="routes") >> cnn_site
