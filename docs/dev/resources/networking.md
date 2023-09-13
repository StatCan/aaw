# Networking Common Tasks and Information

## Quick Access
[Allow Connection to Sites on the Internet from a ProB workload](#allowing-connection-to-sites-on-the-internet)

[Allow Connection to internal application](#allow-connection-to-internal-application)

[DNS pitfalls](#dns-pitfalls-to-internal-application-connecting)

[The `Priority` field in the fwprcg](#the-priority-field)

[In which repo should we define our resources?](#in-which-repository-should-we-define-the-resources)

----
### Allowing Connection to sites on the Internet
This is a bit more niche, as our unclassified notebooks already have connection to the internet, but this can come up when we have a Protected B certified application like seen in https://github.com/StatCan/aaw-private/issues/125 where it's accessible to the internet, but unaccecssible from our Protected B workloads.

To handle this we want to declare a [firewall_policy_rule_collection_group](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/firewall_policy_rule_collection_group) in our terraform files. 

Regarding certain fields, the rule collection group type we chose was [`application rule`](https://learn.microsoft.com/en-us/azure/firewall/policy-rule-sets#application-rules) as we are filtering based on FQDNs.

The `source address` is the subnet address of our protected-b node pool. 

-------------
### Allow Connection to internal application in an already peered network
An example of this can be seen in https://github.com/StatCan/aaw-private/issues/127 

- __Important!__: This solution does not work fully just yet, because of the [DNS pitfall](#dns-pitfalls-to-internal-application-connecting) that we encountered so this will need to be updated.

Like above, this also requires a [firewall_policy_rule_collection_group](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/firewall_policy_rule_collection_group) in our terraform files. 
Regarding certain fields, the rule collection group type we chose was [`network rule`](https://learn.microsoft.com/en-us/azure/firewall/policy-rule-sets#network-rules) as in this case we are working with IP/subnet addresses
In the example, the `source_addresses`s were two entries, one for our unclassified node pool subnet and the other for our protected b node pool subnet.

Additionally, it will require an [azurem_route](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/route) to manage the [routing (azure docs)](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#user-defined). 
The `address_prefix`is the destination to which the route applies (in this case the subnet that the database resides in).
Then for the `next_hop_type` we chose `VirtualAppliance` as we have to get to the cloud main firewall first. 
The `next_hop_in_ip_address` is the cloud main firewall ip.


The other aspect to this is that we also need flow to be opened up on the other side, as in the flow has to be allowed from the firewall to the actual application. This is out of the AAW's hands so an SR must be submitted for this to be done.

>  If the application is in a network that is not already peered, in addition to the route you will neeed to create an [`azurem_virtual_network_peering`](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network_peering.html) resource.

-----------
### DNS Pitfalls to internal application connecting
This is more of an unlucky coincidence in merge request 268 to the `workspaces-infrastructure` done for the task above. We added some DNS related resources in `dns.tf` for `postgres azure databases` where our defined resources interfered with our AAW jfrog configuration. The private DNS zone configuration of `pgazdb` for `postgres.database.azure.com` was taking over all requests for that zone and caused artifactory to no longer be able to resolve with its database.

------------
### The `priority` field
This is an argument in the [firewall_policy_rule_collection_group](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/firewall_policy_rule_collection_group) block that is required. 
Something that isn't immediately obvious is that the value for `priority` should be unique, this is easier to see if you have access to the firewall resource in azure.

--------
### In which repository should we define the resources?
It is important to remember that the `firewall.tf` file in our `terraform-azure-statcan-aaw-network` is mirrored and publically accessible. So for the examples in [Allow Connection to Sites on the Internet from a ProB workload](#allowing-connection-to-sites-on-the-internet) and [Allow Connection to internal application](#allow-connection-to-internal-application) we placed the firewall definitions inside the specific environment (dev / prod) files.

At the end of the day they all end up in the same place / created by azure anyways. If you are lost, try searching through files to see if there are similar definitions in the files (for example the DNS changes were in the `dns.tf` file) or just ask.