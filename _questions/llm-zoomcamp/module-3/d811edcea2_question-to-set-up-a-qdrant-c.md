---
id: d811edcea2
question: 'Question: To set up a Qdrant client, when to use client = QdrantClient("[localhost:6333](http://localhost:6333)")
  vs client = QdrantClient(":memory:")?'
sort_order: 440
---

Use the former if you are running Qdrant in Docker locally and it connects your notebook to the Qdrant server running in Docker.

The latter option creates an in-memory Qdrant instance that runs inside your Python process (no Docker, no persistence, no networking). It’s:

Only for testing or prototyping

Not connected to your Docker-based Qdrant

Wiped clean when the notebook or script stops

