
import os
from diagrams import Cluster, Diagram, Edge

from diagrams.k8s.rbac import RoleBinding

from diagrams.onprem.network import Istio

from diagrams.k8s.podconfig import CM

from diagrams.k8s.network import Netpol

from diagrams.k8s.group import NS
from diagrams.k8s.compute import Pod

from diagrams.onprem.workflow import Kubeflow


def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    with Cluster("aks-cluster"):
        with Cluster("profile-state-controller"):
            profile_state_controller = Pod("profile-state-controller")
            non_employee_exceptions = CM("non-employee-exceptions")

        with Cluster("allowed-user-ns"):
            allowed_k8s_user_ns = NS("allowed-user-namespace")
            allowed_k8s_user_profile = Kubeflow("allowed-user-profile")
            allowed_ns_rolebinding = RoleBinding("allowed-ns-contributors")
            egress_netpol = Netpol("allow-egress-to-cloud-main-system")
            cloud_main_vs = Istio("cloud-main-virtual-service")

        with Cluster("non-allowed-user-ns"):
            non_allowed_k8s_user_ns = NS("non-allowed-user-namespace")
            non_allowed_k8s_user_profile = Kubeflow("non-allowed-user-profile")
            non_allowed_ns_rolebinding = RoleBinding("non-allowed-ns-contributors")

        with Cluster("kubeflow-profiles-namespace"):
            cloud_main_controller = Pod("cloud-main-controller")
            network_policy_controller = Pod("network-controller")

        with Cluster("cloud-main-system"):
            ingress_netpol = Netpol("allow-ingress-from-user-ns")

    # network policy in cloud-main-system selects namespaces with exists-non-cloud-main-users: false
    # and allows ingress from those namespaces
    ingress_netpol >> Edge(label="label selector", style="dashed", color="green") >> allowed_k8s_user_ns

    # per-namespace network policy controller creates allow-egress network policy to allowed namespaces
    network_policy_controller >> Edge(label="creates", style="solid", color="green") >> egress_netpol
    cloud_main_controller >> Edge(label="creates", style="solid", color="green") >> cloud_main_vs

    # Configmaps are mounted to profile state controller pod and list exception cases for each capability
    non_employee_exceptions >> Edge(label="mounts", style="dashed", color="black") >> profile_state_controller

    # Profile State Controller watches Kubeflow profiles and checks the subjects of role bindings
    profile_state_controller >> Edge(label="watches", style="dashed", color="black") >> allowed_ns_rolebinding
    profile_state_controller >> Edge(label="watches", style="dashed", color="black") >> allowed_k8s_user_profile
    profile_state_controller >> Edge(label="watches", style="dashed", color="black") >> non_allowed_ns_rolebinding
    profile_state_controller >> Edge(label="watches", style="dashed", color="black") >> non_allowed_k8s_user_profile

    # Profile State Controller applies capability labels to user profile and namespace
    profile_state_controller >> Edge(label="applies label", style="solid", color="green") >> allowed_k8s_user_profile
    profile_state_controller >> Edge(label="applies label", style="solid", color="green") >> allowed_k8s_user_ns
    profile_state_controller >> Edge(label="applies label", style="solid", color="red") >> non_allowed_k8s_user_profile
    profile_state_controller >> Edge(label="applies label", style="solid", color="red") >> non_allowed_k8s_user_ns
