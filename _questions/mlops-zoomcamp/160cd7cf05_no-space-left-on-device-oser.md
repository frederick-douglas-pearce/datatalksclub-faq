---
course: mlops-zoomcamp
id: 160cd7cf05
question: No Space Left on Device - OSError[Errno 28]
section: 'Module 2: Experiment tracking'
sort_order: 960
---

You do not have enough disk space to install the requirements. You can either increase the base EBS volume by following [this link](https://n2ws.com/blog/how-to-guides/how-to-increase-the-size-of-an-aws-ebs-cloud-volume-attached-to-a-linux-machine#:~:text=First%2C%20go%20to%20your%20volume,your%20requirements%20necessitate%20this%20step) or add an external disk to your instance and configure conda installation to happen on the external disk.

Abinaya Mahendiran

On GCP: I added another disk to my vm and followed [this guide](https://cloud.google.com/compute/docs/disks/add-persistent-disk) to mount the disk. Confirm the mount by running df -H (disk free) command in bash shell. I also deleted Anaconda and instead used miniconda. I downloaded miniconda in the additional disk that I mounted and when installing miniconda, enter the path to the extra disk instead of the default disk, this way conda is installed on the extra disk.

Yang Cao

