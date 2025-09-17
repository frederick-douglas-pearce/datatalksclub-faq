---
course: data-engineering-zoomcamp
id: c2a18da218
question: 'GCP BQ - Error Message in BigQuery: annotated as a valid Timestamp, please
  annotate it as TimestampType(MICROS) or TimestampType(MILLIS)'
section: 'Module 3: Data Warehousing'
sort_order: 2140
---

Background:

`pd.read_parquet`

`pd.to_datetime`

`pq.write_to_dataset`

Reference:

[https://stackoverflow.com/questions/48314880/are-parquet-file-created-with-pyarrow-vs-pyspark-compatible](https://stackoverflow.com/questions/48314880/are-parquet-file-created-with-pyarrow-vs-pyspark-compatible)

[https://stackoverflow.com/questions/57798479/editing-parquet-files-with-python-causes-errors-to-datetime-format](https://stackoverflow.com/questions/57798479/editing-parquet-files-with-python-causes-errors-to-datetime-format)

[https://www.reddit.com/r/bigquery/comments/16aoq0u/parquet_timestamp_to_bq_coming_across_as_int/?share_id=YXqCs5Jl6hQcw-kg6-VgF&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=1](https://www.reddit.com/r/bigquery/comments/16aoq0u/parquet_timestamp_to_bq_coming_across_as_int/?share_id=YXqCs5Jl6hQcw-kg6-VgF&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=1)

Solution:

Add `use_deprecated_int96_timestamps=True` to `pq.write_to_dataset` function, like below

pq.write_to_dataset(

table,

root_path=root_path,

filesystem=gcs,

use_deprecated_int96_timestamps=True

# Write timestamps to INT96 Parquet format

)

