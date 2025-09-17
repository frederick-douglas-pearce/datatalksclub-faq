---
id: 6e251d34b6
question: How can I read a small number of rows from the parquet file directly?
sort_order: 3560
---

from pyarrow.parquet import ParquetFile

pf = ParquetFile('fhvhv_tripdata_2021-01.parquet')

#pyarrow builds tables, not dataframes

tbl_small = next(pf.iter_batches(batch_size = 1000))

#this function converts the table to a dataframe of manageable size

df = [tbl_small.to](http://tbl_small.to/)_pandas()

Alternatively without PyArrow:

df = spark.read.parquet('fhvhv_tripdata_2021-01.parquet')

df1 = df.sort('DOLocationID').limit(1000)

pdf = df1.select("*").toPandas()

