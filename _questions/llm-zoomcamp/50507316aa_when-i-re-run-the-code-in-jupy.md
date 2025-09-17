---
course: llm-zoomcamp
id: 50507316aa
question: When I re-run the code in Jupyter notebook multiple times for homework#1,
  the index building code snippet fails.
section: 'Module 1: Introduction'
sort_order: 340
---

The solution is to delete any potential existing  index with the same name before attempting to create the index (see code snippet below).

# Check if the index exists and delete it if it does

if es_client.indices.exists(index=index_name):

print(f"Deleting existing index: {index_name}")

es_client.indices.delete(index=index_name)

print(f"Index {index_name} deleted.")

However, with this approach sometimes when you re-run the code multiple times, the index gets messed up and you for example will see a different score output each time you execute the code for question#3 in homework1. To fix this 1) Go to docker desktop and stop Elasticsearch container , delete the container image and re-initiate the Elasticsearch container by creating it from scratch per the instructions ‘1.6 Searching with ElasticSearch’ 2) Change the name of the index in your code to anything other than -> index_name = "course-questions"

