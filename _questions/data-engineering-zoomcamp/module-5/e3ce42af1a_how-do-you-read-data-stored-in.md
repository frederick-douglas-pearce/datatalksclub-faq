---
id: e3ce42af1a
question: How do you read data stored in gcs on pandas with your local computer?
sort_order: 3670
---

To do thispip install gcsfs,

Thereafter copy the uri path to the file and use df = pandas.read_csc(gs://path)

