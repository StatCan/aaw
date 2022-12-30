# Overview

MinIO is a cloud-native scalable object store. We use MinIO for buckets (blob or
S3 storage). Buckets are good at three things:

- Large amounts of data - Buckets can be huge: way bigger than hard drives. And
  they are still fast.
- Accessible by multiple consumers at once - You can access the same data source
  from multiple Notebook Servers and pipelines at the same time without needing
  to duplicate the data.
- Sharing - You can share files from a bucket by sharing a URL that you can get
  through a simple web interface. This is great for sharing data with people
  outside of your workspace.

# Setup

## MinIO Mounted Folders on a Notebook Server

<!-- prettier-ignore -->
!!! warning "MinIO mounts are not currently working on Protected B servers."

Your MinIO storage are mounted as directories if you select the option
`Mount MinIO storage into the minio/ folder` when creating a Notebook Server.

The MinIO storage is located in `~/minio`:

![MinIO folders mounted as Jupyter Notebook directories](../images/minio_automount_folder.png)

These folders can be used like any other - you can copy files to/from using the
file browser, write from Python/R, etc. The only difference is that the data is
being stored in the MinIO service rather than on a local disk (and is thus
accessible wherever you can access your MinIO bucket, rather than just from the
Notebook Server it is attached).

<!-- prettier-ignore -->
??? warning "Files copied into a mounted MinIO folder might take a few moments to be readable"
    When you copy files into a MinIO folder, they are immediately stored and accessible in MinIO (e.g.: you can immediately see them in the [Web Portal](#minio-web-portal)).  But, new files may take a few moments for the mounting service to notice and serve them in the mounted folder.  If your use case needs access to these files immediately after copying them, try the other read methods ([the mc tool](#minio-command-line-tool) or [Other S3 Compliant Methods](#other-s3-compliant-methods)).

## Bucket Types and Access Scopes

The following MinIO tenants (e.g.: separate services) are available:

|                   Tenant | Access via File Browser            | Access via `mc`                               | Access via Web                                                 | Protected-b/Unclassified Notebooks |
| -----------------------: | ---------------------------------- | --------------------------------------------- | -------------------------------------------------------------- | ---------------------------------- |
|        gateway-standard  | `~/minio/standard`                 | `mc ls gateway-standard`        | [link](https://minio.aaw.cloud.statcan.ca/minio/login)         | Unclassified                       |
|        gateway-premium   | `~/minio/premium`                  | `mc ls gateway-premium`         | [link](https://minio-premium.aaw.cloud.statcan.ca/minio/login) | Unclassified                       |
| fdi-gateway-unclassified | `~/minio/fdi-gateway-unclassified` | `mc ls fdi-gateway-unclassified` | N/A                                                            | Unclassified                       |
|      gateway-standard-ro | MinIO mounts not working.          | `mc ls gateway-standard-ro`        | N/A                                                            | Protected-B                        |
|      gateway-premium-ro  | MinIO mounts not working.          | `mc ls gateway-premium-ro`         | N/A                                                            | Protected-B                        |
|      gateway-protected-b | MinIO mounts not working.          | `mc ls gateway-protected-b`        | N/A                                                            | Protected-B                        |
|  fdi-gateway-protected-b | MinIO mounts not working.          | `mc ls fdi-gateway-protected-b`  | N/A                                                            | Protected-B                        |

Accessing all MinIO tenants is the same. The difference between tenants is the
storage type behind them:

- **[Standard](https://minio.aaw.cloud.statcan.ca/minio/login):** By default,
  use this one. It is backed by an SSD and provides a good balance of cost and
  performance.
- **[Premium](https://minio-premium.aaw.cloud.statcan.ca/minio/login):** Use
  this if you need high read/write speeds and don't mind paying ~2x the storage
  cost. These are somewhat faster than the standard storage.

Generally if you aren't sure which you need, start with **Standard**. You can
always change your mind if you see your work limited by file transfer speeds.

Within each bucket type, everyone has two storage locations they can use, each
providing different access scopes:

|                                        |                                                                                                                  Private                                                                                                                  |                                                        Shared                                                        |
| -------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |
|                                Summary | Accessible only by someone within your namespace (typically only by you from your own notebook servers/remote desktop, unless you're working in a [shared namespace](../4-Collaboration/Overview.md#share-compute-namespace-in-kubeflow)) | Writable only by you, but readable by anyone with access to the platform. Great for sharing public data across teams |
| Mount location in the Notebook Server: |                                                                                            `~/minio/standard/private/myfolder/myfile`                                                                                            |                                  `~/minio/standard/shared/myfolder/myfile`                                  |
|    Location in `mc` tool/MinIO portal: |                                                                                                   `firstname-lastname/myfolder/myfile`                                                                                                    |                                     `shared/firstname-lastname/myfolder/myfile`                                      |

<!-- prettier-ignore -->
??? info "You can see many directories in the shared MinIO bucket, but you can only write to your own"
    Everyone has read access to all folders in the `shared` MinIO bucket, but write permissions are always restricted to the owner.

## Accessing Internal Data

AAW has an integration with the FAIR Data Infrastructure team that allows users
to transfer unclassified and protected-b data to Azure Storage Accounts. These
storage accounts are used my MinIO Gateway instances, thus allowing users to
access this data from Notebook Servers.

Please reach out to the FAIR Data Infrastructure team if you have a use case for
this data.

# Once you've got the basics ...

## MinIO Web Portal

The MinIO service can be accessible through a
[web portal](https://minio.aaw.cloud.statcan.ca/minio/login). To sign in using
your existing credentials, use the "Log in with OpenID" button.

![MinIO sign-in view, indicating the OpenID option](../images/minio_self_serve_login.png)

From this portal you can browse to your personal bucket, which has the same name
as your Kubeflow namespace (likely `firstname-lastname`):

![MinIO browser with personal bucket using first name, last name format (hyphenated)](../images/minio_self_serve_bucket.png)

This lets you browse, upload/download, delete, or share files.

## Browse Datasets

<!-- prettier-ignore -->
!!! warning "The link below is not currently working."

Browse some [datasets](https://datasets.covid.cloud.statcan.ca) here. These data
sets are meant to store widely shared data. Either data that has been brought
it, or data to be released out as a product. **As always, ensure that the data
is not sensitive.**

## MinIO Command Line Tool

MinIO provides the command line tool `mc` to access your data from a terminal.
`mc` can communicate with one or more MinIO instances to let you upload/download
files. For example:

<!-- prettier-ignore -->
??? info "To run the below example yourself, replace `BUCKETNAME`'s value with your first/last name."
    For example: `BUCKETNAME=john-smith`.

```sh
#!/bin/sh

# The name of your bucket.  This MUST be the same as your namespace's name.
# Typically this is "firstname-lastname", but it might be different if working in a shared namespace
BUCKETNAME=firstname-lastname

# Get your personal credentials for the "gateway-standard" MinIO instance
# (this initializes $MINIO_URL, $MINIO_ACCESS_KEY, and $MINIO_SECRET_KEY environment variables)
source /vault/secrets/minio-gateway-standard

# Create a MinIO alias (called "standard") for "standard" using your credentials
mc config host add standard $MINIO_URL $MINIO_ACCESS_KEY $MINIO_SECRET_KEY

# Create a bucket under your name
# NOTE: You can *only* create buckets named the same as your namespace. Any
# other name will be rejected.

# Private bucket ("mb" = "make bucket")
mc mb -p standard/${BUCKETNAME}

# Shared bucket
mc mb -p standard/shared/${BUCKETNAME}

# There you go! Now you can copy over files or folders!
# Create test.txt (if it does not exist) and copy it to your bucket:
[ -f test.txt ] || echo "This is a test" > test.txt
mc cp test.txt standard/${BUCKETNAME}/test.txt
```

Now open the [MinIO Web Portal](#minio-web-portal) or browse to
`~/minio/standard/private` to see your test file!

<!-- prettier-ignore -->
??? tip "`mc` can do a lot"
    In addition to copying files, `mc` can do a lot more (like `mc ls gateway-standard/FIRSTNAME-LASTNAME` to list the contents of a bucket).  Check out the [mc docs](https://docs.min.io/docs/minio-client-complete-guide.html) or run `mc --help` for more information.

<!-- prettier-ignore -->
??? tip "See the example notebooks!"
    There is a template provided for connecting in `R`, `python`, or by the
    command line, provided in [jupyter-notebooks/self-serve-storage](https://github.com/StatCan/aaw-contrib-jupyter-notebooks/tree/master/self-serve-storage) (also auto-mounted to all jupyter notebook servers in `~/jupyter-notebook`). You can
    copy-paste and edit these examples! They should suit most of your needs.

## MinIO Python client

You can also connect to MinIO using a python client such as `minio` or `boto3`.

```python
import json, minio, re

# Get rid of http:// in minio URL
http = lambda url: re.sub('^https?://', '', url)

# Get the MinIO creds
with open("/vault/secrets/minio-gateway-standard.json") as secrets:
    d = json.load(f)

# Create the minio client.
s3Client = Minio(
    http(d['MINIO_URL']),
    access_key=d['MINIO_ACCESS_KEY'],
    secret_key=d['MINIO_SECRET_KEY'],
    secure=False,
    region="us-west-1"
)
```

<!-- prettier-ignore -->
!!! tip "But I want to be secure"
    The `secure=False` thing is a bit misleading. It disables `https`
    because this traffic is **inside** the cluster, and the cluster
    auto-magically applies mutual TLS. So your applications don't need
    to worry about https. **Your connection is secure by default.**

<!-- prettier-ignore -->
!!! question "But I'm not in us-west?"
    The "us-west-1" is an artifact of weird S3 API standards. It is
    **required**, even if it doesn't make sense.

## Other S3-Compliant Methods

MinIO is S3 compliant - it uses the same standard as Amazon S3 and other bucket
services. Tools designed to use S3 will generally also work with MinIO, for
example Python packages and instructions on how to access files from S3. Some
examples of this are shown in
[jupyter-notebooks/self-serve-storage](https://github.com/StatCan/aaw-contrib-jupyter-notebooks/tree/master/self-serve-storage).

## Sharing from Private Buckets

You can easily share individual files from a private bucket. Just use the
"share" option for a specific file and you will be provided a link that you can
send to a collaborator!

![MinIO browser with a shareable link to a file](../images/minio_self_serve_share.png)

## Get MinIO Credentials

<!-- prettier-ignore -->
!!! warning "The methods below have not been tested recently, since certain MinIO changes. These may require adjustment."

<!-- prettier-ignore -->
!!! note "The following methods still work, but you often don't need this anymore because of automation!"
    If you're accessing MinIO from on a Notebook Server or in a Kubeflow Pipeline, these credentials will automatically be loaded into the `mc` command line tool for you. You can use the `mc` tool without accessing credentials like shown below (e.g.: just type `mc ls gateway-standard/MY_NAMESPACE/`). If you do need credentials, you can still get them from `/vault/secrets/minio-*`

To access your MinIO buckets programmatically (for example through the
[`mc` command line tool](#MinIO-Command-Line-Tool), or via Python or R) you
require personal MinIO credentials. Methods for obtaining these credentials are
outlined here.

### Method 1: Get Credentials from Vault

To get your MinIO credentials, you can use the
[Vault](https://vault.covid.cloud.statcan.ca/ui/vault/auth?with=oidc). Select
method OIDC, leave **Role** blank and Sign in with OIDC Provider.

![vault_Signin](../images/vault_signin.png)

Run the following command in the terminal located at the top right corner:

```sh
# Replace standard with premium depending on your Bucket type
read minio_standard_tenant_1/keys/profile-yourfirstname-yourlastname
```

![Vault AccessKey](../images/accessKey.png)

### Method 2: Get Credentials from Running Notebook Server

Open a terminal in your Notebook and run:

```sh
cat /vault/secrets/minio-gateway-standard

# Output:
# export MINIO_URL="http://minio.minio-gateway-standard ..."
# export MINIO_ACCESS_KEY="..."
# export MINIO_SECRET_KEY="..."
```

## Pricing

<!-- prettier-ignore -->
??? info "Pricing models are tentative and may change"
    As of writing, pricing is covered by the platform for initial users.  This guidance explains how things are expected to be priced priced in future, but this may change.

Exact pricing for MinIO resources are hard to state because they're prorated
across multiple users. In general though, the underlying storage is provided by
[Azure Manage Disks](https://azure.microsoft.com/en-us/pricing/details/managed-disks/)
and they give a rough guide for MinIO storage cost based on the MinIO instance:

- premium:
  - See **Premium SSD Managed Disks**
- standard:
  - See **Standard SSD Managed Disks**
  - Typically 50% the cost of `premium`
