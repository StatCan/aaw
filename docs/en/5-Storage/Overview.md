# Storage

Several storage options are available to AAW users to access and import their data. Below you will find a description of each kind. There are separate documentation pages for connecting to each kind of storage.

## Kubeflow Volumes

Kubeflow uses virtual disks called Volumes. You will encounter these on the Notebook Server creation screen. These disks come in two varieties, called Workspace Volumes and Data Volumes. Both Data and Workspace Volumes can be reused and mounted to different Notebook Servers, just not at the same time. 

### Workspace Volumes

Workspace Volumes are similar in concept and function to the hard drive in your laptop, it's where all the software is stored and it's the default storage device for all your stuff. 

### Data Volumes

If you need more storage, then a Data Volume may be necessary.

## Azure Blob Storage

If you need to collaborate with others, then Azure Blob Storage (as provisioned by FDI) may be the best option for you and your data. See [Choosing Your Storage](#choosing-your-storage) for more information.

## Choosing Your Storage

Depending on your and your project's unique needs and requirements, either Kubeflow Volumes or Azure Blob Storage (or both) may be most suitable:

|                                                          Type |                                                       Simultaneity |                                                   Speed | Total size               | Shareability |
| :------------------------------------------------------------ | :----------------------------------------------------------------------- | :------------------------------------------------------ | ------------------------ | -------------------------- |
| **[Azure Blob Storage](AzureBlobStorage.md)** | Simultaneous access from many notebook servers at the same time | Fast-ish (Fast download, modest upload, modest latency) | Infinite (within reason) | Shareable                      |
|                                          **[Kubeflow Volumes](KubeflowVolumes.md)** |                                    One notebook server at a time |                        Fastest (throughput and latency) | <=512GB total per disk  | Not shareable                         |

<!-- prettier-ignore -->
!!! Info "If you're unsure which to choose, don't sweat it"
    These are guidelines, not an exact science - pick what sounds best now and run with it.  The best choice for a complicated usage is non-obvious and often takes hands-on experience, so just trying something will help.  For most situations both options work well even if they're not perfect, and remember that data can always be copied later if you change your mind.
