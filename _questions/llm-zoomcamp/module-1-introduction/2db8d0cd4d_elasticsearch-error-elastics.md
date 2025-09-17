---
id: 2db8d0cd4d
question: 'ElasticSearch: ERROR: Elasticsearch exited unexpectedly'
sort_order: 210
---

If you get this error, it’s likely that elasticsearch doesn’t get enough RAM

I specified the RAM size to the configuration (-m 4GB)

docker run -it \

--rm \

--name elasticsearch \

-m 4GB \

-p 9200:9200 \

-p 9300:9300 \

-e "discovery.type=single-node" \

-e "xpack.security.enabled=false" \

docker.elastic.co/elasticsearch/elasticsearch:8.4.3

(-m 2gb should also work)

Another possible solution may be to set the memory_lock to false:

docker run -it \

--rm \

--name elasticsearch \

-p 9200:9200 \

-p 9300:9300 \

-e "discovery.type=single-node" \

-e see"xpack.security.enabled=false" \

-e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \

-e "bootstrap.memory_lock=false" \

docker.elastic.co/elasticsearch/elasticsearch:8.4.3

