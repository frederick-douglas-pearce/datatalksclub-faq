---
id: 590e5d8c20
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_be1c5cff.png
question: 'Py4J Error - ModuleNotFoundError: No module named ''py4j'' (Solve with
  latest version)'
sort_order: 3440
---

If below does not work, then download the latest available py4j version with

conda install -c conda-forge py4j

Take care of the latest version number in the website to replace appropriately.

<{IMAGE:image_1}>

Now add

export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"

export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH"

in your  .bashrc file.

