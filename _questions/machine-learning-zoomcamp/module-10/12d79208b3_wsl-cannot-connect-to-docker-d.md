---
id: 12d79208b3
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_41f796fe.png
question: WSL Cannot Connect To Docker Daemon
sort_order: 3460
---

Due to the uncertainties associated with machines, sometimes you can get the error message like this when you try to run a docker command:

”Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?”

Solution: The solution is simple. The Docker Desktop might no longer be connecting to the WSL Linux distro. What you need to do is go to your Docker Desktop setting and then click on resources. Under resources, click on WSL Integration. You will get a tab like the image below:

<{IMAGE:image_1}>

Just enable additional distros. That’s all. Even if the additional distro is the same as the default WSL distro.

Odimegwu David

