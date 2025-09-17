---
id: 28f6392ce5
question: Hack to load yellow and green trip data for 2019 and 2020
sort_order: 2580
---

I initially followed [data-engineering-zoomcamp/03-data-warehouse/extras/web_to_gcs.py at main · DataTalksClub/data-engineering-bootcamp (github.com)](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/03-data-warehouse/extras/web_to_gcs.py)

But it was taking forever for the yellow trip data and when I tried to download and upload the parquet files directly to GCS, that works fine but when creating the Bigquery table, there was a schema inconsistency issue

Then I found another hack shared in the slack which was suggested by Victoria.

[[Optional] Hack for loading data to BigQuery for Week 4 - YouTube](https://www.youtube.com/watch?v=Mork172sK_c&t=22s&ab_channel=Victoria)

Please watch until the end as there is few schema changes required to be done

