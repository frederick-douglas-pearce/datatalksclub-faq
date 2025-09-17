---
course: data-engineering-zoomcamp
id: c18119ba32
question: Invalid dataset ID Error Error when running the gcp_setup flow
section: 'Module 2: Workflow Orchestration'
sort_order: 1920
---

When following the [youtube lesson](https://www.youtube.com/watch?v=nKqjjLJ7YXs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=23) and then running the [gcp_setup flow](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/02-workflow-orchestration/flows/05_gcp_setup.yaml),  it works until the create_bq_dataset task, where I got the following error:

While not very apparent from the error message, we are not suppose to use a dash in the dataset name, so I changed the dataset name to “de_zoomcamp” and it worked.

