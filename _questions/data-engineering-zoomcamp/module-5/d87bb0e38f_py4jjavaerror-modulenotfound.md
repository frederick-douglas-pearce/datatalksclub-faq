---
id: d87bb0e38f
question: 'Py4JJavaError - ModuleNotFoundError: No module named ''py4j''` while executing
  `import pyspark`'
sort_order: 3430
---

You need to look for the Py4J file and note the version of the filename. Once you know the version, you can update the export command accordingly, this is how you check yours:` ls ${SPARK_HOME}/python/lib/ ` and then you add it in the export command, mine was:export PYTHONPATH=”${SPARK_HOME}/python/lib/Py4J-0.10.9.5-src.zip:${PYTHONPATH}”

Make sure that the version under `${SPARK_HOME}/python/lib/` matches the filename of py4j or you will encounter `ModuleNotFoundError: No module named 'py4j'` while executing `import pyspark`.

For instance, if the file under `${SPARK_HOME}/python/lib/` was `py4j-0.10.9.3-src.zip`.

Then the export PYTHONPATH statement above should be changed to `export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.3-src.zip:$PYTHONPATH"` appropriately.

Additionally, you can check for the version of ‘py4j’ of the spark you’re using from [here](https://spark.apache.org/docs/latest/api/python/getting_started/install.html) and update as mentioned above.

~ Abhijit Chakraborty: Sometimes, even with adding the correct version of py4j might not solve the problem. Simply run pip install py4j and problem should be resolved.

