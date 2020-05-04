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
format `firstname.lastname`. Picture below.


![Buckets / Object Storage](images/minio_self_serve_bucket.png)

## Sharing

You can easily share individual files.

![Minio File Sharing](images/minio_self_serve_share.png)


## Programmatic Access

TODO: Ask Will & Zach
