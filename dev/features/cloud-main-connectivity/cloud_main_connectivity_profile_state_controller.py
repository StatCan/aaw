import os

from diagrams.onprem.workflow import Kubeflow
from diagrams import Cluster, Diagram, Edge
from diagrams.azure.compute import AKS
from diagrams.custom import Custom
from diagrams.k8s.compute import Deployment, Pod, StatefulSet
from diagrams.k8s.network import NetworkPolicy, Service
from diagrams.k8s.group import NS
from diagrams.k8s.rbac import RoleBinding


def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    with Cluster("Advanced Analytics Workspace"):
        with Cluster("aaw-prod-cc-00"):
            aaw_prod_cc_00 = AKS("aaw-prod-cc-00")
        with Cluster("non-employee-namespace"):
            non_stc_employee_kf_profile = Kubeflow("non-stc-employee-kf-profile")
            non_stc_employee_ns = NS("non-stc-employee")
            john_doe_rb_1 = RoleBinding("john.doe@cloud.statcan.ca")
            alice_rb = RoleBinding("alice@external.ca")
        with Cluster("employee-namespace"):
            stc_employee_kf_profile = Kubeflow("stc-employee-kf-profile")
            stc_employee_ns = NS("non-stc-employee")
            jane_doe_rb = RoleBinding("jane.doe@statcan.gc.ca")
            john_doe_rb_2 = RoleBinding("john.doe@cloud.statcan.ca")
        with Cluster("daaas-system"):
            profile_state_controller = Pod("profile-state-controller")
            daaas_system_ns = NS("daaas-system")

        # Profile State Controller watches rolebindings associated with each
        # Kubeflow profile to detect whether emails from a non-statcan domain
        # are present.
        john_doe_rb_1 >> Edge(style="dashed", color="black") >> profile_state_controller
        john_doe_rb_2 >> Edge(style="dashed", color="black") >> profile_state_controller
        alice_rb >> Edge(style="dashed", color="black") >> profile_state_controller
        jane_doe_rb >> Edge(style="dashed", color="black") >> profile_state_controller

        # Non-employee Kubeflow profiles and namespaces get the label
        # `state.aaw.statcan.gc.ca/non-employee-users=true`
        profile_state_controller >> Edge(style="dashed", color="red", label="non-employee-users=true") >> non_stc_employee_kf_profile
        profile_state_controller >> Edge(style="dashed", color="red", label="non-employee-users=true") >> non_stc_employee_ns

        # Employee Kubeflow profiles and namespaces get the label
        # `state.aaw.statcan.gc.ca/non-employee-users=false`
        profile_state_controller >> Edge(style="dashed", color="red", label="non-employee-users=false") >> stc_employee_kf_profile
        profile_state_controller >> Edge(style="dashed", color="red", label="non-employee-users=false") >> stc_employee_ns