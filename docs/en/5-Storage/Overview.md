# Storage overview

Several storage options are available for AAW users to access and import their data. Below is a description of each type. There are separate documentation pages for connecting to each storage type.

## Kubeflow Volumes (Disks)

Kubeflow uses virtual disks called Volumes. You will encounter them on the server notebook creation screen. These drives come in two varieties, called Workspace Volumes and Data Volumes. Data and workspace volumes can be reused and mounted on different notebook servers, but not at the same time.

### Workspace volumes

Workspace volumes are similar in concept and function to your laptop's hard drive, it's where all software is stored and it's the default storage device for all your stuff.

### Data volumes

If you need more storage, a data volume may be required. This is conceptually similar to connecting a high-capacity USB hard drive to your PC.

## Azure Blob Storage (Containers)

If you need to collaborate with others, Azure Blob Storage (as provided by FDI) may be the best option for you and your data. See #choosing-your-storage for more information.

## Choose your storage

Depending on your and your project's unique needs and requirements, Kubeflow Volumes or Azure Blob Storage (or both) may be best suited:

| Type                                                       | Simultaneity                                                      | Speed                                                   | Capacity                 | Shareability  |
| :--------------------------------------------------------- | :---------------------------------------------------------------- | :------------------------------------------------------ | ------------------------ | ------------- |
| **[Azure Blob Storage (Containers)](AzureBlobStorage.md)** | Simultaneous access from multiple laptop servers at the same time | Fast-ish (fast download, modest upload, modest latency) | Infinite (within reason) | Shareable     |
| **[Kubeflow Volumes (Disks)](KubeflowVolumes.md)**         | One Notebook Server at a Time                                     | Fastest (throughput and latency)                        | <=512 GB total per disk  | Not shareable |

<!-- prettier-ignore -->
!!! Info “If you don’t know which one to choose, don’t worry!”
      These are guidelines, not an exact science: choose what sounds best now and apply it. The best choice for complicated use is not obvious and often requires hands-on experience, so just try something. In most situations, both options work well even if they aren't perfect, and remember that the data can always be copied later if you change your mind.
