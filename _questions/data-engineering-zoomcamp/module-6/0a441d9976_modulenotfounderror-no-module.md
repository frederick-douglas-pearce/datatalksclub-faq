---
id: 0a441d9976
question: 'ModuleNotFoundError: No module named ''avro'''
sort_order: 3950
---

✅SOLUTION: pip install confluent-kafka[avro].

For some reason, Conda also doesn't include this when installing confluent-kafka via pip.

More sources on Anaconda and confluent-kafka issues:

[https://github.com/confluentinc/confluent-kafka-python/issues/590](https://github.com/confluentinc/confluent-kafka-python/issues/590)

[https://github.com/confluentinc/confluent-kafka-python/issues/1221](https://github.com/confluentinc/confluent-kafka-python/issues/1221)

[https://stackoverflow.com/questions/69085157/cannot-import-producer-from-confluent-kafka](https://stackoverflow.com/questions/69085157/cannot-import-producer-from-confluent-kafka)

