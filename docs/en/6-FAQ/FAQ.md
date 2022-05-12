**IMPORTANT** If your question does not appear in this document, please reach
out to us on [Slack](https://statcan-aaw.slack.com/) in the #general channel.

# General

## What is the AAW?

The Advanced Analytics Workspace is a platform within the Data Analytics as a
Service (DAaaS) program at Statistics Canada. It is available to users at
Statistics Canada and to external collaborators. It comprises multiple open
source data science tools and is based on Kubeflow and uses MinIO for storage.

## What is Kubeflow?

Kubeflow is a free and open-source machine learning platform designed to enable
using machine learning pipelines to orchestrate complicated workflows running on
Kubernetes (e.g. doing data processing then using TensorFlow or PyTorch to train
a model, and deploying to TensorFlow Serving or Seldon). Kubeflow was based on
Google's internal method to deploy TensorFlow models called TensorFlow
Extended.

## What is MinIO?

MinIO is a type of high performance object storage. It is API compatible with
the Amazon S3 cloud storage service. It can handle unstructured data such as
photos, videos, log files, backups, and container images with (currently) the
maximum supported object size of 5TB.

## What are Namespaces?

Namespaces isolate users or a group of Kubeflow users. A Kubeflow user can own
more than one namespace and they can invite users to join their namespace to
enable collaboration on the same data and code.

## What are GPUs for?

GPUs are efficient matrix multipliers. When training a machine learning model,
especially a neural network, most of the performed calculations are matrix
multiplications, hence GPUs are well suited for training neural networks. If you
do not need to train a neural network model then you probably don't need a GPU.
Since GPUs consume a lot of energy they are expensive to run in the cloud so
please use them sparingly.

# Questions and Answers Related to the AAW Portal

## Who Can Access the AAW?

Anyone with a Statistics Canada (@statcan.gc.ca) email address can access the
AAW. If an external partner / department needs to have access, they would need a
Statistics Canada cloud account and they would need to apply and reach an
agreement with Statistics Canada.

## How Can I Access the Portal?

The AAW and its services are accessible from the
[AAW Portal](https://analytics-platform.statcan.gc.ca/covid19).

## What services are available from the Portal?

From the AAW portal you can find Kubeflow and MinIO.

- [Kubeflow](https://kubeflow.aaw.cloud.statcan.ca/)
- [MinIO](https://minio.aaw.cloud.statcan.ca/)

## Where can I find extra documentation?

The portal contains links to our user guide, videos, and our slack channel. If
the user guide and videos don't contain the answers you are looking for,
contact us on Slack.

## Can I leave feedback?

Of course, we welcome all sorts of feedback. Simply follow the Leave Feedback
link on our portal and leave your comment.

- [Advanced Analytics Workspace Portal](https://analytics-platform.statcan.gc.ca/covid19)

## Is there a preference for @statcan.gc.ca or @cloud.statcan.ca?

While you are free to use either one, your workspaces will only be available to
the associated account. To simplify use of the AAW it is recommended to pick an
email address and stick to that one.

# Questions and Answers Related to Slack

## Why can't I access Slack?

There are many possibilities why a user cannot access our Slack workspace. Your
department may have denied access to Slack, to find out, check:
[Is this blocked in my department.ca](https://isthisblockedinmydepartment.ca/service/slack/).
Another common issue is that the AAW team may need to add your department email
domain to permit access in Slack.

## Which channel within the AAW Slack workspace do I leave my request / question / concerns?

Please use the #general channel.

# Questions and Answers Related to Kubeflow

## Namespace(s)

### Where can I find which namespace I am presently using?

You can find your namespace in Kubeflow in the upper left corner next to
the Kubeflow icon.

### Can I share data from my namespace(s) with other users?

You can definitely share your namespace with other users. As an owner of a
namespace, you are able to add contributors.

### Can I have multiple namespaces and be the owner of all of them?

The quick answer is yes. In order to be the owner of multiple namespaces, you
will need to request AAW to create the namespaces for you. You will need to
provide your email address and the namespace name of your choices. We typically
ask that your namespace name is unique and by project.

### How do I add other people to my namespace (for collaboration)?

On the left sidebar, you will find MANAGE CONTRIBUTORS. As an owner, you will be
able to add contributors by entering their email address. The email address is
the one that the contributor uses to login to KUBEFLOW. Be advised: when adding
users to your namespace, the email address field is case sensitive and some
users have capitalisation, so make sure to add their email address exactly as it
appears in the Kubeflow interface.

### Can a namespace change ownership?

Yes it is possible to transfer ownership of contributor namespaces. Please ask
us and we will do that for you.

### What is the difference between non-Protected B (unclassified) and Protected B workspaces?

- **UNCLASSIFIED / NON-PROTECTED B WORKSPACE**

  - This workspace has **NO ACCESS** to confidential and classified statistical
    data.

  - This workspace has access to the internet.

- **PROTECTED B**

  - A Protected B workspace does not have internet access.
  - Creating a Protected B workspace doesn't mean that you will automatically
    have rights to access to confidential Protected B data. A user will need to
    submit a request through our Customer Success Unit which will need to
    analyze the needs, acquire a Sponsor, and get OPMIC approval.

## CREATING WORKSPACES / NOTEBOOKS

### What are the differences between the types of volumes?

- Workspace volumes are equivalent to your home directory on a Unix-like
  operating system such as Linux. On the AAW this is where your Python and R packages will be installed. You can store anything you like in your workspace volume but the AAW offers additional storage options for large datasets.
- Data volumes are more appropriate for datasets and can be mounted to any location in your server. A data volume can only be attached to one server at a time.
- MinIO is our cloud storage offering. Your MinIO buckets can store data you want to share across projects and servers.

### Does AAW offer real-time collaboration with workspaces?

Workspaces cannot have multiple instances. A workspace is 1 tenant at a time.

### How long does it take to create a notebook server?

It really should be approximately 2-10 minutes. If it takes longer please reach
out to our Slack Channel for further support.

### Is there an upper bound on time to create a new notebook server?

If we're hitting our limits on the number of compute nodes it could take longer
than 10 minutes while the cluster scales up, making room for additional nodes.
Additionally, there's also the case where a new node needs to join the cluster
and that may take anywhere from a few minutes to half an hour depending on the
node type and how Azure (our underlying cloud computing platform) is feeling
that day.

### Can I change the configuration of my server after it's been created?

You cannot do this from the Kubeflow interface. If you want to scale your server
up or down the easiest way to do this is to destroy your server while keeping
your storage volumes. You can then create a new server and attach the existing
volumes. Additionally you can reach out to us on Slack and we can help you.

## WORKSPACES / NOTEBOOKS (Working with)

### What different file formats can I use in R or Python?

R and Python can open most file formats. Some of these might include:

- CSV
- XLS, XLSX
- ZIP
- JSON
- XML
- SQLITE
- SAS7BDAT
- HDF
- DOC, DOCX
- And many more...

### Because AAW does not offer PowerBI, what are the alternatives?

AAW does offer a flavor of R Shiny as well as Plotly Dash. You can always export
PowerBI data and make use of it in our platform. At the moment, no. We are
currently looking into solutions for sharing data between the AAW and CAE (which
supports Power BI).

### Where can we access public data for StatCan?

You can find publicly accessible StatCan Data at the following locations:

- [English StatCan Data](https://www150.statcan.gc.ca/n1/en/type/data?MM=1)
- [Données du StatCan](https://www150.statcan.gc.ca/n1/fr/type/donnees?MM=1)

### How can I get access to Statcan Protected B data?

A user will need to request access through the Customer Success Unit (CSU). A
user will also need to provide a namespace, get a sponsor as well as getting
approval from OPMIC. Once the process has been approved, our Fair Data
Infrastructure (FDI) team will then create a folder on Net A which in turn will
give access to user(s) through the active directory. The data will then be able
to transfer from Net A to AAW Cloud.

### Can I share data with internal and external users?

The short answer is yes as long as they are part of the same namespace.

### Do we need to shut down the notebook servers in order to save costs?

There are no guidelines on how to stop any running workspaces as a cost-saving
measure.

### How do you suspend your server (to save costs)?

As of now you must destroy your server. Make sure to save the data volumes, they
can be reused with a new server. The version of KUBEFLOW in the dev branch has
an option to suspend the session. Once that has rolled out to production, users
will have the ability to suspend workspaces to save on costs.

### How much does the AAW cost?

StatCan is currently covering the cost for the time being for all workspace
usage for all users (internal and external). In the near future (fiscal year
2022-23), AAW will start cost recovery by charging usage from external users. To
give you a rough estimate of costs, please consult the following table.

#### CPU Only

| **Use Case**               | **Compute Resources** |            |       | **Time (Hours/Week)** | **Cost (CAD)** |           |            |
|----------------------------|-----------------------|------------|-------|-----------------------|----------|-----------|------------|
|                            | _CPU_                 | _RAM (GB)_ | _GPU_ |                       | _Weekly_ | _Monthly_ | _Annually_ |
| CPU: Occasional Use        | 2                     | 8.0        | 0     | 8                     | $1.14   | $4.89   | $59.11    |
| CPU: During Business Hours | 2                     | 8.0        | 0     | 40                    | $5.68   | $24.44  | $295.54    |
| CPU: 24/7                  | 2                     | 8.0        | 0     | 168                   | $23.87  | $102.64 | $1,241.28   |

#### Add a GPU

| **Use Case**               | **Compute Resources** |            |       | **Time (Hours/Week)** | **Cost** |           |            |
|----------------------------|-----------------------|------------|-------|-----------------------|----------|-----------|------------|
|                            | _CPU_                 | _RAM (GB)_ | _GPU_ |                       | _Weekly_ | _Monthly_ | _Annually_ |
| GPU: Occasional Use        | 0                     | 0          | 1     | 8                     | $34.47   | 148.2124  | 1792.336   |
| GPU: During Business Hours | 0                     | 0          | 1     | 40                    | $172.34   | 741.062   | 8961.68    |
| GPU: 24/7                  | 0                     | 0          | 1     | 168                   | $723.83  | 3112.4604 | 37639.056  |

### What packages are available?

We offer all the R and Python packages found on the Python Package Index (PyPI),
Conda Forge and CRAN. The packages stored in those official repositories are
mirrored and scanned on our end. If you want to know what is available, please
check out the following sources.

If you find something on Awesome Open Source that is not available on the AAW,
please let us know!

### Is there a way to see the configuration of the notebook server?

The configuration defines the amount of compute resources each server has at its
disposal. If you want to know how much compute power each server has, take a
look at the server list in the Kubeflow interface. The amount of CPU and memory
and information about attached volumes can be found there.

If you have many servers and would like an aggregated view of the above
information, open up your notebook server, start a terminal session and enter
the following command:

`kubectl describe quota -n your-name-space`

This will give you an overview of how much compute power you are consuming on
the cluster.

## Storage, Databases and MinIO

### How can I access MinIO?

- [MinIO Portal](https://minio.aaw.cloud.statcan.ca/)
- You can access your MinIO account from the
[MinIO Portal](https://minio.aaw.cloud.statcan.ca/). You'll need your
Statistics Canada Windows username and password.

### What are the steps for getting Protected B data into MinIO?

One must consult with FDI (F.A.I.R. Data Infrastructure) before Protected B Data
can be loaded into MinIO. The FDI team owns an Azure Data Factory pipeline for
moving data, typically from on premise, to an Azure Storage Account and MinIO is
our S3 gateway to that storage account.

### How do I transfer Protected B data from one cloud to another cloud?

Statcan has an Electronic File Transfer (EFT) system that is made to securely
transfer data between external partners, I don't know of any cloud specific
mechanism

### **How can I programmatically access MinIO from JupyterLab?

[This Github repository](https://github.com/StatCan/aaw-contrib-jupyter-notebooks/tree/master/self-serve-storage)
has examples of how to programmatically access MinIO. Additionally, this
repository is cloned automatically into the JupyterLab and R Studio images.

### Why are my empty files not appearing in my MinIO bucket?

Empty text files are filtered out of the Protected B data service.

### How can I get access to Statcan Protected B data?

A user will need to request access through the Customer Success Unit (CSU). A
user will also need to provide a namespace, get a sponsor as well as getting
approval from OPMIC. Once the process has been approved, our Fair Data
Infrastructure (FDI) team will then create a folder on Net A which in turn will
give access to user(s) through the active directory. The data will then be able
to transfer from Net A to AAW Cloud.

### Can I host a database on AAW?

No. But you can use SQLite, which is a database in a file. You can also use
Parquet files which offer a performant file-based alternative to databases.

### What's a good size for the different volumes?

16GB is pretty safe. It's mostly going to be your Python/R packages that are
stored in the main storage volume.

### Are there any preloaded datasets in AAW that we can access and use for both R and Python notebooks?

Our JupyterLab images come with some example notebooks and data, they can be
found in /aaw-contrib-jupyter-notebooks/. The R Studio image also has some
example notebooks and data, they can be found in /aaw-contrib-r-notebooks/.

## SAS

[SAS Kernel for Jupyter](https://github.com/sassoftware/sas_kernel)

### Can we use SAS in the AAW?

If you are a StatCan employee then the answer is yes! You can use Saspy (a
Python package for running SAS code). SAS is also supported by JupyterLab's
[Cell Magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cell-magics)!
You can use SAS Studio from within JupyterLab. You can import sas7bdat files
into R and Python using readily available libraries.

### Does using SAS entail different costs than the others?

We are using the Statistics Canada SAS licenses so the cost has already been
taken care of by Statistics Canada.

### Are there a limited number of licenses or instances that can be run?

SAS support is currently experimental and will rely on existing Statistics
Canada SAS software licenses.

### Where can I get more information about SAS on the AAW?

The internet abounds with documents on how to use SAS with Python, the following
are a couple of good places to start your research.

- [An Introduction to SASPy and Jupyter Notebooks](https://www.sas.com/content/dam/SAS/support/en/sas-global-forum-proceedings/2018/2822-2018.pdf)
- [SASPy | SAS Support](https://support.sas.com/en/software/saspy.html)

## Advanced

### Can I Create My Own Web API Service Powered by Kubernetes?

You can create an API from within your namespace. For the time being, it's done
by creating
[Seldon Deployments](https://www.kubeflow.org/docs/external-add-ons/serving/seldon/)
or by creating Kubernetes Deployments/StatefulSets.

Seldon is for the deployment of ML models, requiring model artifacts. Now those
artifacts could in principle be arbitrary python code to some extent. The API
web servers are set up through python gunicorn. If you have a particular use
case in mind, we can discuss it.

## Additional Resources

See the following link for additional resources to help you get the most out of
the Advanced Analytics Workspace!

## Contribute!

If you find the AAW to be useful and you'd like to contribute to its success,
please check out our Github repositories, review the code and submit a pull
request!

[https://github.com/StatCan/daaas](https://github.com/StatCan/daaas)
