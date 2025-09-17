---
id: '1913720953'
question: 'Downloading the data from the NY Taxis datasets gives error : 403 Forbidden'
sort_order: 630
---

Problem: While following the steps in the videos you may have problems trying to download with wget the files. Usually it is a 403 error type (Forbidden access).

Solution: The links point to files on cloudfront.net, something like this:[https://d37ci6vzurychx.cloudfront.net/tOSError: Could not open parquet input source '<Buffer>': Invalid: Parquet OSError: Could not open parquet input source '<Buffer>': Invalid: Parquet rip+data/green_tripdata_2021-01.parquet](https://d37ci6vzurychx.cloudfront.net/trip+data/green_tripdata_2021-01.parquet)

I’m not download the dataset directly, i use dataset URL and run this in the file.

Update(27-May-2023): Vikram

I am able to download the data from the below link. This is from the official  NYC trip record page ([TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)). Copy link from page directly as the below url might get changed if the NYC decides to move away from this. Go to the page , right click and use copy link.

wget [d37ci6vzurychx.cloudfront.net](https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet)

(Asif)

