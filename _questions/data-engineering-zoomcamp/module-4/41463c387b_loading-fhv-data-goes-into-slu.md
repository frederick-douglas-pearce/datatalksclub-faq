---
id: 41463c387b
question: Loading FHV Data goes into slumber using Mage?
sort_order: 3230
---

Try loading the data using jupyter notebooks in a local environment. There might be bandwidth issues with Mage.

Load the data into a pandas dataframe using the urls, make necessary transformations, upload the gcp bucket / alternatively download the parquet/csv files locally and then upload to GCP manually.

