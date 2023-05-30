
import os
from diagrams import Cluster, Diagram, Edge

from diagrams.custom import Custom

from diagrams.k8s.rbac import User
from diagrams.k8s.rbac import RoleBinding

from diagrams.k8s.controlplane import API
from diagrams.k8s.infra import ETCD

from diagrams.k8s.podconfig import CM


from diagrams.k8s.group import NS
from diagrams.k8s.compute import Pod

from diagrams.onprem.workflow import Kubeflow


def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    with Cluster("browser"):
        browser = Custom("browser", icon_path="img/browser.png")
    with Cluster("aks-cluster"):
        with Cluster("profile-state-controller"):
            profile_state_controller = Pod("profile-state-controller")
            non_employee_exceptions = CM("non-employee-exceptions")

        with Cluster("user-namespace"):
            k8s_user_ns = NS("user-namespace")
            k8s_user_profile = Kubeflow("user-profile")
            ns_rolebinding = RoleBinding("ns-contributors")

        with Cluster("kubeflow-system-namespace"):
            kf_notebook_controller = Pod("notebook-controller")
            spawner_ui_config = CM("spawner_ui_config.yamll")

        with Cluster("system-namespace"):
            etcd = ETCD("k8s-etcd")
            k8s_api_server = API("k8s-api-server")
            gatekeeper_server = Pod("opa-gatekeeper")
        gatekeeper_policy = Custom("opa-gatekeeper-policies", icon_path="img/opa.png")
        
    # Configmaps are mounted to profile state controller pod and list exception cases for each capability
    non_employee_exceptions >> Edge(label="mounts", style="dashed", color="black") >> profile_state_controller

    # User or service account attempts to create resource by posting manifest to k8s API server
    kf_notebook_controller >> Edge(label="posts resource manifest", style="dashed", color="orange") >> k8s_api_server

    # OPA Gatekeeper policies specify deny rules at validating admission control
    gatekeeper_policy >> Edge(label="configures", style="dashed", color="black") >> gatekeeper_server
    k8s_api_server >> Edge(label="validating admission webhook", style="dashed", color="orange") >> gatekeeper_server
    gatekeeper_server >> Edge(label="allow/deny decision", style="dashed", color="orange") >> k8s_api_server

    # If OPA Gatekeeper doesn't deny the request, k8s API server posts the manifest to etcd
    k8s_api_server >> Edge(label="posts resource manifest", style="dashed", color="green") >> etcd

    # Profile State Controller watches Kubeflow profiles and checks the subjects of role bindings
    profile_state_controller >> Edge(label="watches", style="dashed", color="black") >> ns_rolebinding
    profile_state_controller >> Edge(label="watches", style="dashed", color="black") >> k8s_user_profile

    # Profile State Controller applies capability labels to user profile and namespace
    profile_state_controller >> Edge(label="applies label", style="solid", color="green") >> k8s_user_profile
    profile_state_controller >> Edge(label="applies label", style="solid", color="green") >> k8s_user_ns

    # Spawner UI config configures UI to disable sas image if exists user in namespace without sas notebook capability
    spawner_ui_config >> Edge(label="conditionally disables sas icon", style="dashed", color="black") >> browser