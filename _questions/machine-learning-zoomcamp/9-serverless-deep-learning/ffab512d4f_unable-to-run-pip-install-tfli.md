---
id: ffab512d4f
question: Unable to run pip install tflite_runtime from github wheel links?
sort_order: 3380
---

To overcome this issue, you can download the whl file to your local project folder and in the Docker file add the following lines:

COPY <file-name> .

RUN pip install <file-name>

Abhijit Chakraborty

