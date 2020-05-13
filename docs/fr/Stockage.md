# Storage

The platform has a range of different types of storage meant for a variety of
use-cases, so this storage section applies whether you're experimenting,
creating pipelines, or publishing. 

At the surface, there are two kinds of storage

- Disks (also called Volumes)

- Buckets (S3 or "Blob" storage)


## Disks

![Data Volumes](images/kubeflow_existing_volume.png)

Disks are the familiar Hard-drive/SDD style file systems! You can mount the
disks into your Kubeflow server, and even if you delete your server, you can
remount the disks, as they are never destroyed by default. This is a super
simple way to store your data, and if you share a workspace with a team, your
whole team can use the same server's disk just like a shared drive.


## Buckets


![Buckets / Object Storage](images/minio_self_serve_bucket.png)

Buckets are slightly more complicated, but they are good at three things:

- Large amounts of data
  - Buckets can be huge. Way bigger than hard-drives. And they are fast.
  
- Sharing
  - You can share files from a bucket by sharing a URL that you can get through
    a simple web interface. This is great for sharing data with people outside
    of your workspace.
    
    
- Programmatic Access
  - Most importantly, it's much easier for pipelines and web-browsers to access
    data from buckets than from a hard drive. So if you want to use pipelines,
    you basically have to configure them to work with a bucket.
    

# Bucket Storage

We have four available storage instances buckets

**Self-Serve**

- [Minimal](https://minimal-tenant1-minio.example.ca)

- [Premium](https://premium-tenant1-minio.example.ca)

- [Pachyderm](https://pachyderm-tenant1-minio.example.ca)

**Publicly Available**

- [Public (Read-Only)](https://datasets.example.ca)


## Self-Serve

In any of the three self-serve options, you can create a personal bucket. To log
in, simply use **OpenID** as below

![Buckets / Object Storage](images/minio_self_serve_login.png)

Once you are logged in, you are allowed to create a personal bucket with the
format `firstname-lastname`. Picture below.


![Buckets / Object Storage](images/minio_self_serve_bucket.png)

## Sharing

You can easily share individual files.

![Minio File Sharing](images/minio_self_serve_share.png)


## Programmatic Access

There is a plan in the works to let you access your bucket-storage just with a folder
but in the meantime you can access it programmatically with the command line tool `mc`, 
or via S3 API calls in R or Python

!!! danger "Must set a kubeflow configuration"
    You must check the box to inject the credentials in order to proceed.
    ![Minio Credentials Option](images/kubeflow_minio_option.png)
	Otherwise, your notebook server won't have access.

!!! tip "See the example notebooks!"
    There is a template provided for connecting in `R`, `python`, or by the commandline,
	provided in `jupyter-notebooks/self-serve-storage`. You can copy-paste and edit these
	examples! They should suite most of your needs.
	
### Connecting with `mc`

To connect, simply run the following (replace `FULLNAME=blair-drummond` with your actual `firstname-lastname`)

```sh
#!/bin/sh

FULLNAME=blair-drummond

# Get the credentials
source /vault/secrets/minio-minimal-tenant1

# Add the storage under the alias "minio-minimal"
mc config host add minio-minimal $MINIO_URL $MINIO_ACCESS_KEY $MINIO_SECRET_KEY

# Create a bucket under your name
# NOTE: Everyone gets their own bucket FIRSTNAME-LASTNAME
# but your cannot just create another bucket.

# The private bucket. "mb" = make bucket
mc mb minio-minimal/${FULLNAME}

# The shared bucket
mc mb minio-minimal/shared/${FULLNAME}

# There you go! Now you can copy over files or folders!
[ -f test.txt ] || echo "This is a test" > test.txt
mc cp test.txt minio-minimal/${FULLNAME}/test.txt
```

Now open [minimal-tenant1-minio.example.ca](https://minimal-tenant1-minio.example.ca), you will see your test file there!

You can use `mc` to copy files to/from the bucket. It is very fast. You can also use `mc --help` to see what other options you have,
like `mc ls minio-minimal/FIRSTNAME-LASTNAME/` to list the contents of your bucket.


??? tip "Other storage options"
    To use one of the other storage options; 

	- pachyderm

	- premium

	Simply replace `minimal` in the above program with one of these.
	
