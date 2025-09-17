---
id: a31defac51
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_d2b29adb.png
question: Why do we need the Staging dataset?
sort_order: 2730
---

<{IMAGE:image_1}>

Vic created three different datasets in the videos.. dbt_<name> was used for development and you used a production dataset for the production environment. What was the use for the staging dataset?

R: Staging, as the name suggests, is like an intermediate between the raw datasets and the fact and dim tables, which are the finished product, so to speak. You'll notice that the datasets in staging are materialised as views and not tables.

Vic didn't use it for the project, you just need to create production and dbt_name + trips_data_all that you had already.

