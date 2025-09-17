---
course: machine-learning-zoomcamp
id: 98e0d0b961
question: Error building docker image on M1 Mac
section: 9. Serverless Deep Learning
sort_order: 3210
---

Problem:

While trying to build docker image in Section 9.5 with the command:

docker build -t clothing-model .

It throws a pip install error for the tflite runtime whl

ERROR: failed to solve: process "/bin/sh -c pip install [[GitHub](https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl)](https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl)" did not complete successfully: exit code: 1

Try to use this link: [[GitHub](https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl)](https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl)

If the link above does not work:

The problem is because of the arm architecture of the M1. You will need to run the code on a PC or Ubuntu OS.

Or try the code bellow.

Added by Dashel Ruiz Perez

Solution:

To build the Docker image, use the command:

docker build --platform linux/amd64 -t clothing-model .

To run the built image, use the command:

docker run -it --rm -p 8080:8080 --platform linux/amd64 clothing-model:latest

Added by Daniel Egbo

