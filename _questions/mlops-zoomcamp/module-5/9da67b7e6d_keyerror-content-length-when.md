---
id: 9da67b7e6d
question: KeyError ‘content-length’ when running prepare.py
sort_order: 1950
---

Problem: When running prepare.py getting KeyError: ‘content-length’

Solution: From Emeli Dral:It seems to me that the link we used in prepare.py to download taxi data does not work anymore. I substituted the instruction:

url = f"[https://nyc-tlc.s3.amazonaws.com/trip+data/{file}](https://nyc-tlc.s3.amazonaws.com/trip+data/%7Bfile%7D)

by the

url = f"[https://d37ci6vzurychx.cloudfront.net/trip-data/{file}](https://d37ci6vzurychx.cloudfront.net/trip-data/%7Bfile%7D)"

in the prepare.py and it worked for me. Hopefully, if you do the same you will be able to get those data.

