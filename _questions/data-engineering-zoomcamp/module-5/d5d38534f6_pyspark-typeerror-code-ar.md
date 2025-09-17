---
id: d5d38534f6
question: 'PySpark - TypeError: code() argument 13 must be str, not int  , while executing
  `import pyspark`  (Windows/ Spark 3.0.3 - Python 3.11)'
sort_order: 3360
---

This is because Python 3.11 has some inconsistencies with such an old version of Spark. The solution is a downgrade in the Python version. Python 3.9 using a conda environment takes care of it. Or install newer PySpark >= 3.5.1 works for me (Ella) [[source](https://datatalks-club.slack.com/archives/C01FABYF2RG/p1709470599276889)].

