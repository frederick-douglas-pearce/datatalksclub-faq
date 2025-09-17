---
id: 1cc0ab1fea
question: Error importing cimpl dll when running avro examples
sort_order: 3940
---

ImportError: DLL load failed while importing cimpl: The specified module could not be found

Verify Python Version:

Make sure you are using a compatible version of Python with the Avro library. Check the Python version and compatibility requirements specified by the Avro library documentation.

... you may have to load librdkafka-5d2e2910.dll in the code. Add this before importing avro:

from ctypes import CDLL

CDLL("C:\\Users\\YOUR_USER_NAME\\anaconda3\\envs\\dtcde\\Lib\\site-packages\\confluent_kafka.libs\librdkafka-5d2e2910.dll")

It seems that the error may occur depending on the OS and python version installed.

ALTERNATIVE:

ImportError: DLL load failed while importing cimpl

✅SOLUTION: $env:CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1 in Powershell.

You need to set this DLL manually in Conda Env.

Source: [https://githubhot.com/repo/confluentinc/confluent-kafka-python/issues/1186?page=2](https://githubhot.com/repo/confluentinc/confluent-kafka-python/issues/1186?page=2)

