---
course: llm-zoomcamp
id: de32098d49
question: What other alternatives to ElasticSearch are there?
section: Certificates
sort_order: 670
---

You could use some of this free alternatives for elastic search

[Milvus](https://milvus.io/): an open source library that has the same functionalities that has elastic

[OpenSearch](https://opensearch.org/): also a free open source library that has the same functionalities as elastic

Let's imagine, today I start using multi-qa-distilbert-cos-v1  ([huggingface.co](https://huggingface.co/sentence-transformers/multi-qa-distilbert-cos-v)1).

I create embeddings and index them.

Tomorrow, the author of the model decides to update it because of some reason.

What happens with all indexed embeddings? Do they become incompatible and I will need to re-index everything?

There is an option to save the model locally also. This way even if the cloud model changes your code should work.

