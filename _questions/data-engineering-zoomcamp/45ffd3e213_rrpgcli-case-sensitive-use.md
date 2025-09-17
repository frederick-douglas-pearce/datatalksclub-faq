---
course: data-engineering-zoomcamp
id: 45ffd3e213
question: RRPGCLI - case sensitive use “Quotations” around columns with capital letters
section: 'Module 1: Docker and Terraform'
sort_order: 1150
---

PULocationID will not be recognized but “PULocationID” will be. This is because unquoted "Localidentifiers are case insensitive. [See docs](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS).

