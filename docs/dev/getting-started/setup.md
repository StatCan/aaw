# Setup

## If you just recieved your work laptop

1. Set up your laptop using the Onboarding Manual on your laptop.
2. Ask your supervisor for all the passwords you will need.
3. Once you have set up, be sure to change your passwords.

Below are some more tips and getting-started guides.

## Setting up your Linux Workstation

Once you have a virtual Linux workstation, you'll want to install a few tools to interact with k8s clusters. Use this script to get started.

### Instructions for Script

1. Copy and paste the script below into a text file named `install-tools.sh`:

``` bash
#!/usr/bin/env bash

KUBECTL_VERSION=latest # vX.XX.XX should be atleast +/- 1 version of your kubernetes version
KUBECTL_URL=https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl
KUBECTL_CHECKSUM=https://dl.k8s.io/release/$(KUBECTL_VERSION)/bin/linux/amd64/kubectl.sha256

AZCLI_URL=https://aka.ms/InstallAzureCLIDeb

ARGO_CLI_VERSION=latest # v3.4.5
ARGO_CLI_URL=https://github.com/argoproj/argo-workflows/releases/download/${ARGO_CLI_VERSION}/argo-linux-amd64.gz

# AzureCLI - installation script from Azure
  curl -sLO "${AZCLI_URL}" \
  && bash InstallAzureCLIDeb \
  && rm InstallAzureCLIDeb \
  && echo "azcli: ok" \
&& \
# argo cli
  curl -sLO  ${ARGO_CLI_URL}\
  && echo "${ARGO_CLI_SHA}  argo-linux-amd64.gz"  | sha256sum -c - \
  && gunzip argo-linux-amd64.gz \
  && chmod +x argo-linux-amd64 \
  && sudo mv ./argo-linux-amd64 /usr/local/bin/argo \
  && argo version

# Install kubectl and kubelogin
az aks install-cli
```

2. Make the script executable

``` bash
chmod +x install-tools.sh
```

3. Run the script

``` bash
sudo ./install-tools.sh
```

## Connect to the Kubernetes Cluster

There are two Kubernetes clusters you'll want to interact with, `dev` and `prod`. To connect to either cluster, follow the instructions below, replacing `dev` with `prod` as necessary.

1. In a new Terminal window, execute `az login`.

You should be prompt to login using your cloud account

2. Execute `az account set --subscription aaw`

3. Get credentials for either `dev` or `prod``:

#### For `dev` execute: 

``` bash
az aks get-credentials --resource-group aaw-dev-cc-00-rg-aks --name aaw-dev-cc-00-aks
``` 

#### For `prod` execute:

``` bash
az aks get-credentials --resource-group aaw-prod-cc-00-rg-aks --name aaw-prod-cc-00-aks
```

That should generate a file under `~/.kube/config`.

4. Then execute `kubectl get po -n org-ces-system`. If you are getting a forbidden error, try executing the following command:  `export KUBECONFIG="~/.kube/config"`. You should now see a list of all containers under `org-ces-system` namespace.
5. Welcome to the cluster. :-)

## Switch Between Clusters

Let's say you are connected to `prod` and you'd like ot connect to `dev`, or vice-versa, you'll need these commands:

#### Dev Cluster

``` bash
kubectl config use-context aaw-dev-cc-00-aks
```

#### Prod Cluster

``` bash
kubectl config use-context aaw-prod-cc-00-aks
```

## Connect to Kibana (DEV)

Once you are authenticated (see section above), execute the following:

``` bash
kubectl -n org-ces-system get secrets vetting-es-elastic-user -o jsonpath='{.data.elastic}' | base64 --decode
```

Returned data is the password to authenticate to Kibana.
Once you have done that, go to https://org-ces-system-vetting-kb.aaw-dev.cloud.statcan.ca/. The username is `elastic` and the password is the string you got from the above command.

## Useful commands

Get all pods inside our namespace:
``` bash
kubectl get pods -n org-ces-system
```

Get all secrets inside our namespace:
``` bash
kubectl get secrets -n org-ces-system
```

Get yaml content of secret vetting-es-elastic-user:
``` bash
kubectl get secrets -n org-ces-system vetting-es-elastic-user -o yaml
```

Print a file to the console (useful to open error.log files on the pod):
``` bash
cat FILETOOPEN
```

Copy a file/folder from a container to local hard drive
``` bash
kubectl cp CONTAINER_ID:SOURCE_PATH DESTINATION_PATH -n org-ces-system
```

Map the DEV kubecost API to port 9090 locally:
``` bash
kubectl port-forward -n kubecost-system svc/kubecost-cost-analyzer 9090:9090
```

### New to Linux

If you are new to Linux then this link may be useful:

- [Linux Journey](https://linuxjourney.com/)

## Connect to Cloud Main DEV kubernetes cluster

1. Open a Terminal on your cloud Linux VM and execute the following command (you have to change the path so it matches where the kubeconfig.canadacentral.json" is located): 

``` bash
export KUBECONFIG="~/Documents/git/k8s-cancentral-01-dev-shared/kubeconfig.canadacentral.json"
```

2. Run the following command: 

``` bash
kubectl cluster-info
```

3. You will see a message on-screen to open https://microsoft.com/devicelogin and enter a code. Do it.

4. You should be now authenticated. To connect to our pods, first list all pods by running:

``` bash
kubectl get pods -n vdl
```
5. You should see pod name starting by "vetting-" followed by numbers. That is our web application container.
6. The other pod name starting by "vetting-posgresql-" is the database container.

## Explore Statistics Canada’s Internal Communications Network

- [Home](https://icn-rci.statcan.ca)
- [New Employee Handbook](https://icn-rci.statcan.ca/24/24g/24g_000-eng.html)
- [StatCan and the Cloud](https://icn-rci.statcan.ca/07/0706/0706_070-eng.html)

## Complete the Mandatory Training

You should complete the training for New Employees and All Employees as soon as possible.

### Accessing the Mandatory Training

- [All Training Courses](https://icn-rci.statcan.ca/07/07m/07m08/07m08_007-eng.html)
- [Registration](https://idp.csps-efpc.gc.ca/idp/RegistrationUtilities)
  - To create an account you will need access to your
    firstname.lastname@statcan.gc.ca email and PRI
- After creating an account, do the training on your personal laptop

<!-- prettier-ignore -->
!!! Hint 
    The Klick Training will have to be done through Net A, just navigate to [The Admin System Portal](http://adminsystemportal) on Internet Explorer in Net A

## Additional Links

- [Kubernetes Cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Overview](https://kubernetes.io/docs/reference/kubectl/overview/)
- [Onboarding to Kubernetes](https://confluenceb.statcan.ca/display/CSC/Onboarding+to+Kubernetes)