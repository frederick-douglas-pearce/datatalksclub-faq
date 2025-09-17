---
course: mlops-zoomcamp
id: fa23739c18
question: Empty Records in Kinesis Get Records with LocalStack
section: 'Module 6: Best practices'
sort_order: 2280
---

Problem descriptionFollowing video 6.3, at minute 11:23, get records command returns empty Records.

Solution description

Add --no-sign-request to Kinesis get records call: aws --endpoint-url=[[localhost:4566](http://localhost:4566)](http://localhost:4566/) kinesis get-records --shard-iterator […] --no-sign-request

