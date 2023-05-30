import os
import profile

from diagrams import Cluster, Diagram, Edge

from diagrams.custom import Custom

from diagrams.azure.network import Firewall
from diagrams.azure.network import RouteTables
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.network import Subnets
from diagrams.azure.network import RouteFilters

def myself() -> str:
    f = os.path.basename(__file__)
    no_ext = ".".join(f.split(".")[:-1])
    return no_ext


with Diagram(myself(), show=False):
    with Cluster("Cloud Main"):
        pass
    with Cluster("Advanced Analytics Workspace"):
        with Cluster("aaw-prod-aks-vnet"):
            azure_aks_vnet = VirtualNetworks("azurerm_virtual_network aks")
            azure_aks_route_table = RouteTables("azurerm_route_table network")
            azure_aks_route_rule = RouteFilters("azurerm_route network_default")
            with Cluster("azurerm_subnet cloud-main-system"):
                azure_cloudmain_subnet = Subnets("azurerm_subnet cloud-main-system")
                non_stc_employee_nb = Custom("non-employee-nb", icon_path="img/jupyter.png")
            with Cluster("azurerm_subnet cloud-main-system"):
                azure_cloudmain_subnet = Subnets("azurerm_subnet cloud-main-system")

        with Cluster("aaw-prod-hub-vnet"):
            azure_hub_vnet = VirtualNetworks("azurerm_virtual_network hub")
            with Cluster("azurerm_subnet hub_firewall"):
                azure_cloudmain_subnet = Subnets("azurerm_subnet hub_firewall")
                azure_hub_firewall = Firewall("azurerm_firewall firewall")


    # There is a network peering between aks vnet and aaw-hub vnet
    azure_aks_vnet - Edge(style="dashed", color="black", label="azurerm_virtual_network_peering") - azure_hub_vnet

    # There is a route table assocaition between the cloud-main-system subnet and the
    # network route table in the aaw-prod-aks-vnet
    azure_cloudmain_subnet >> Edge(style="dashed", color="black", label="azurerm_subnet_rt_association") >> azure_aks_route_table

    # The aaw-prod-aks-vnet route table has a route allowing
    # The route table in the aaw-prod-aks-vnet routes all outgoing traffic to the AAW hub firewall
    azure_aks_route_table >> Edge(style="dashed", color="green", label="next hop") >> azure_hub_firewall