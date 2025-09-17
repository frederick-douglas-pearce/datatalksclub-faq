---
course: mlops-zoomcamp
id: d41cd73af9
question: 'HTTPError: HTTP Error 403: Forbidden when call apply_model() in score.ipynb'
section: 'Module 4: Deployment'
sort_order: 1800
---

Solution: instead of input_file = f'[https://s3.amazonaws.com/nyc-tlc/trip+data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet](https://s3.amazonaws.com/nyc-tlc/trip+data/%7Btaxi_type%7D_tripdata_%7Byear:04d%7D-%7Bmonth:02d%7D.parquet)'  use input_file = f'[https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet](https://d37ci6vzurychx.cloudfront.net/trip-data/%7Btaxi_type%7D_tripdata_%7Byear:04d%7D-%7Bmonth:02d%7D.parquet)'

Ilnaz Salimov

[salimovilnaz777@gmail.com](mailto:salimovilnaz777@gmail.com)

