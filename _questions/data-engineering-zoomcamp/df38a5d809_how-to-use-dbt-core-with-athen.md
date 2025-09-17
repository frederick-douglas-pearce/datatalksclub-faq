---
course: data-engineering-zoomcamp
id: df38a5d809
question: How to use dbt-core with Athena?
section: Project
sort_order: 4370
---

If you don’t have access to dbt Cloud which is already natively being supported by AWS, refer here:[ 1](https://aws.amazon.com/blogs/big-data/from-data-lakes-to-insights-dbt-adapter-for-amazon-athena-now-supported-in-dbt-cloud/),[ 2](https://youtu.be/JEizJAaaBkg?si=niTYdWoeiyC_w3h7),[ 3](https://docs.getdbt.com/guides/athena?step=1), &[ 4](https://docs.getdbt.com/docs/core/connect-data-platform/athena-setup), you can use the community built[ dbt-Athena Adapter](https://dbt-athena.github.io/) for dbt-Core.

Key Features

Enables dbt to work with AWS Athena using dbt Core

Allows data transformation using CREATE TABLE AS or CREATE VIEW SQL queries

Not yet supported features:

Python models

Persisting documentation for views

This adapter can be a valuable resource for those who need to work with Athena using dbt Core, and I hope this entry can help others discover it.

