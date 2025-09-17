---
course: data-engineering-zoomcamp
id: dda62d0ef0
question: Storage Bucket Permission Denied Error when running the gcp_setup flow
section: 'Module 2: Workflow Orchestration'
sort_order: 1910
---

When following the [youtube lesson](https://www.youtube.com/watch?v=nKqjjLJ7YXs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=23) and then running the [gcp_setup flow](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/02-workflow-orchestration/flows/05_gcp_setup.yaml), I get the following error:

I tried manually creating the bucket in the GCP console, but this showed me that the bucket already existed. So I came up with another name for the bucket and it worked.

The GCP bucket name has to be unique globally across all buckets, even if those are not your buckets, because the bucket will be accessible by URL.

