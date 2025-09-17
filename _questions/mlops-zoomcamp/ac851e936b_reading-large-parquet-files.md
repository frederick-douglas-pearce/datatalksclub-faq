---
course: mlops-zoomcamp
id: ac851e936b
question: Reading large parquet files
section: 'Module 1: Introduction'
sort_order: 510
---

I have faced a problem while reading the large parquet file. I tried some workarounds but they were NOT successful with Jupyter.

The error message is:

IndexError: index 311297 is out of bounds for axis 0 with size 131743

I solved it by performing the homework directly as a python script.

Added by Ibraheem Taha ([ibraheemtaha91@gmail.com](mailto:ibraheemtaha91@gmail.com))

You can try using the Pyspark library

Answered by kamaldeen ([kamaldeen32@gmail.com](mailto:kamaldeen32@gmail.com))

Parquet format can be read in chunks: [link](http://blog.clairvoyantsoft.com/efficient-processing-of-parquet-files-in-chunks-using-pyarrow-b315cc0c62f9). (IK)

