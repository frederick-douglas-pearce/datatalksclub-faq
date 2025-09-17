---
course: machine-learning-zoomcamp
id: 8b5cf23fcf
question: 'Error: Could not find a version that satisfies the requirement tflite_runtime
  (from versions:none)'
section: 9. Serverless Deep Learning
sort_order: 3230
---

Problem: When trying to install tflite_runtime with

!pip install --extra-index-url[ ](https://google-coral.github.io/py-repo/)[https://google-coral.github.io/py-repo/](https://google-coral.github.io/py-repo/) tflite_runtime

one gets an error message above.

Solution:

fflite_runtime is only available for the os-python version combinations that can be found here: [https://google-coral.github.io/py-repo/tflite-runtime/](https://google-coral.github.io/py-repo/tflite-runtime/)

your combination must be missing here

you can see if any of these work for you [https://github.com/alexeygrigorev/tflite-aws-lambda/tree/main/tflite](https://github.com/alexeygrigorev/tflite-aws-lambda/tree/main/tflite)

and install the needed one using pip

eg

pip install [https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl](https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl)

as it is done in the lectures code:

[https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/09-serverless/code/Dockerfile#L4](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/09-serverless/code/Dockerfile#L4)

Alternatively, use a virtual machine (with VM VirtualBox, for example) with a Linux system. The other way is to run a code at a virtual machine within cloud service, for example you can use Vertex AI Workbench at GCP (notebooks and terminals are provided there, so all tasks may be performed).

Added by Alena Kniazeva, modified by Alex Litvinov

