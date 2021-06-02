There are many ways collaborate on the platform. Which is best for your
situation depends on what you're sharing and how many people you want to share
with. Scenarios roughly break down into what you want to share (**Data**,
**Code**, or **Compute Environments** (e.g.: sharing the same virtual machines))
and who you want to share it with (**No one**, **My Team**, or **Everyone**).
This leads to the following table of options

|             |           **Private**            |                  **Team**                  |  **StatCan**  |
| :---------: | :------------------------------: | :----------------------------------------: | :-----------: |
|  **Code**   | GitLab/GitHub or personal folder |        GitLab/GitHub or team folder        | GitLab/GitHub |
|  **Data**   |    Personal folder or bucket     | Team folder or bucket, or shared namespace | Shared Bucket |
| **Compute** |        Personal namespace        |              Shared namespace              |      N/A      |

<!-- prettier-ignore -->
??? question "What is the difference between a bucket and a folder?"
    Buckets are like Network Storage. See the [Storage overview](../5-Storage/Overview.md) for more discussion of the differences between these two ideas.

Choosing the best way to share code, data, and compute all involve different
factors, but you can generally mix and match (share code with your team through
github, but store your data privately in a personal bucket). These cases are
described more in the below sections.

## Share code among team members

In most cases, it is easiest to share code using GitHub or GitLab to share code.
The advantage of sharing with GitHub or GitLab is that it works with users
across namespaces, and keeping code in git is a great way to manage large
software projects.

<!-- prettier-ignore -->
??? note "Don't forget to include a License!"
    If your code is public, do not forget to keep with the Innovation Team's guidelines and use a proper License if your work is done for Statistics Canada.

If you need to share code without publishing it on a repository,
[sharing a namespace](#share-compute-namespace-in-kubeflow) might work as well.

## Share compute (namespace) in Kubeflow

<!-- prettier-ignore -->
!!! danger "Sharing a namespace means you share **everything** in the namespace"
    Kubeflow does not support granular sharing of one resource (one notebook, one MinIO bucket, etc.), but instead sharing of **all** resources. If you want to share a Jupyter Notebook server with someone, you must share your entire namespace and **they will have access to all other resources (MinIO buckets, etc.)**.

In Kubeflow every user has a **namespace** that contains their work (their
notebook servers, pipelines, disks, etc.). Your namespace belongs to you, but
can be shared if you want to collaborate with others. You can also
[request a new namespace](Request-a-Namespace.md) (either for yourself or to
share with a team). One option for collaboration is to share namespaces with
others.

The advantage of sharing a Kubeflow namespace is that it lets you and your
colleagues share the compute environment and MinIO buckets associated with the
namespace. This makes it a very easy and free-form way to share.

To share your namespace, see [managing contributors](#managing-contributors)

<!-- prettier-ignore -->
??? tip "Ask for help in production"
    The Advanced Analytics Workspace support staff are happy to help with production oriented use cases, and we can probably save you lots of time. Don't be shy about [asking us for help](../Help.md)!

## Share data

Once you have a shared namespace, you have two shared storage approaches

| Storage Option                                      | Benefits                                                         |
| :-------------------------------------------------- | :--------------------------------------------------------------- |
| Shared Jupyter Servers/Workspaces                   | More amenable to small files, notebooks, and little experiments. |
| Shared Buckets (see [Storage](../5-Storage/Overview.md)) | Better suited for use in pipelines, APIs, and for large files.   |

To learn more about the technology behind these, check out the
[Storage overview](../5-Storage/Overview.md).

### Sharing with StatCan

In addition to private buckets, or team-shared private buckets, you can also
place your files in _shared storage_. Within all bucket storage options
(`minimal`, `premium`, `pachyderm`), you have a private bucket, **and** a folder
inside of the `shared` bucket. Take a look, for instance, at the link below:

- [`shared/blair-drummond/`](https://minimal-tenant1-minio.covid.cloud.statcan.ca/minio/shared/blair-drummond/)

Any **logged in** user can see these files and read them freely.

### Sharing with the world

Ask about that one in our [Slack channel](https://statcan-aaw.slack.com). There
are many ways to do this from the IT side, but it's important for it to go
through proper processes, so this is not done in a "self-serve" way that the
others are. That said, it is totally possible.

## Recommendation: Combine them all

It's a great idea to always use git, and using git along with shared workspaces
is a great way to combine ad hoc sharing (through files) while also keeping your
code organized and tracked.

## Managing contributors

You can add or remove people from a namespace you already own through the
**Manage Contributors** menu in Kubeflow.

![Contributors Menu](../images/kubeflow_contributors.png)

<!-- prettier-ignore -->
!!! info "Now you and your colleagues can share access to a server!"
    Try it out!
