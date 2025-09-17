---
course: llm-zoomcamp
id: 02df9d0302
question: 'Docker: How do I store data persistently in Elasticsearch?'
section: 'Module 1: Introduction'
sort_order: 230
---

When you stop the container, the data you previously added to elastic will be gone. To avoid it, we can add volume mapping:

docker volume create elasticsearch_data

docker run -it \

--rm \

--name elasticsearch \

-p 9200:9200 \

-p 9300:9300 \

-v elasticsearch_data:/usr/share/elasticsearch/data \

-e "discovery.type=single-node" \

-e "xpack.security.enabled=false" \

docker.elastic.co/elasticsearch/elasticsearch:8.4.3

