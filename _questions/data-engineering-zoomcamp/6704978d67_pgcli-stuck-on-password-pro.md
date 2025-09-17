---
course: data-engineering-zoomcamp
id: 6704978d67
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_93f08019.png
question: PGCLI -  stuck on password prompt
section: 'Module 1: Docker and Terraform'
sort_order: 1110
---

If your Bash prompt is stuck on the password command for postgres

<{IMAGE:image_1}>

Use winpty:

winpty pgcli -h localhost -p 5432 -u root -d ny_taxi

Alternatively, try using Windows terminal or terminal in VS code.

