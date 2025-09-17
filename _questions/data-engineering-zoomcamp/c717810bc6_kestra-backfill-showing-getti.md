---
course: data-engineering-zoomcamp
id: c717810bc6
question: 'Kestra: Backfill showing getting executed but not getting results or showing
  up in executions:'
section: 'Module 3: Data Warehousing'
sort_order: 2000
---

It seems to be a bug. Current fix is to remove the timezone from triggers in the script. More on this bug is [here](https://github.com/kestra-io/kestra/issues/7227).

