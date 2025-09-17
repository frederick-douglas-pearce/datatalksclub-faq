---
id: 993a359b90
question: How do I copy files from a different folder into docker container’s working
  directory?
sort_order: 2260
---

You can copy files from your local machine into a Docker container using the docker cp command. Here's how to do it:

In the Dockerfile, you can provide the folder containing the files that you want to copy over. The basic syntax is as follows:

COPY ["src/predict.py", "models/xgb_model.bin", "./"]Gopakumar Gopinathan

