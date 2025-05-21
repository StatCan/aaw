## Accessing SRM Portal

- On your work laptop, go to <https://srm.statcan.ca>
- Login with your UserID and Network A password

## Logging Into Jira

- On your work laptop, go to <https://jirab.statcan.ca>
- Login with your UserID and Network B password

## Logging into Azure

- Go to <https://portal.azure.com>
- Login with your cloud email (firstname.lastname@cloud.statcan.ca) and password

## Logging into Azure-Cli
- On your Cloud VM (Linux), install Azure CLI using the following command: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
    * Further details on installation can be found here: <https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux>
- Login using the command `az login`, use your cloud email (firstname.lastname@cloud.statcan.ca) and password

### Accessing AAW & DAS clusters on AKS (Azure Kubernetes Service)
- Ensure you are logged into Azure-Cli
- Set your subscription to the subscription name `AAW`
- You should now be able to access clusters such as `das-dev-cc-00-aks`




