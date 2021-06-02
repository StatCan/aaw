# Storage 
The platform provides several types of storage:

- Disk (also called Volumes on the Notebook Server creation screen)
- Bucket ("Blob" or S3 storage, provided through MinIO)
- Data Lakes (coming soon)

Depending on your use case, either disk or bucket may be most suitable:

|   Type |                                                       Simultaneous Users |                                                   Speed | Total size               | Sharable with Other Users            |
| -----: | -----------------------------------------------------------------------: | ------------------------------------------------------: | ------------------------ | ------------------------------------ |
|   **[Disk](Disks.md/)**|                                    One machine/notebook server at a time |                        Fastest (throughput and latency) | <=512GB total per drive  | No                                   |
| **[Bucket](MinIO.md/)** | Simultaneous access from many machines/notebook servers at the same time | Fast-ish (Fast download, modest upload, modest latency) | Infinite (within reason) | [Yes] |

<!-- prettier-ignore -->
??? info "If you're unsure which to choose, don't sweat it"
    These are guidelines, not an exact science - pick what sounds best now and run with it.  The best choice for a complicated usage is non-obvious and often takes hands-on experience, so just trying something will help.  For most situations both options work well even if they're not perfect, and remember that data can always be copied later if you change your mind.
    
