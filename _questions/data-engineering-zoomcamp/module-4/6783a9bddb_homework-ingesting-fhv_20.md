---
id: 6783a9bddb
question: Homework - Ingesting FHV_20?? data
sort_order: 3140
---

Issue: If you’re having problems loading the FHV_20?? data from the github repo into GCS and then into BQ (input file not of type parquet), you need to do two things. First, append the URL Template link with ‘?raw=true’ like so:

URL_TEMPLATE = URL_PREFIX + "/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet?raw=true"

Second, update make sure the URL_PREFIX is set to the following value:URL_PREFIX = "[https://github.com/alexeygrigorev/datasets/](https://github.com/alexeygrigorev/datasets/blob/master/nyc-tlc/fhv)[blob](https://github.com/alexeygrigorev/datasets/blob/master/nyc-tlc/fhv)[/master/nyc-tlc/fhv](https://github.com/alexeygrigorev/datasets/blob/master/nyc-tlc/fhv)"

It is critical that you use this link with the keyword blob. If your link has ‘tree’ here, replace it. Everything else can stay the same, including the curl -sSLf command. ‘

