---
id: 247c0014d8
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_46ecce14.png
question: How to fix error after running the Docker run command
sort_order: 2050
---

<{IMAGE:image_1}>

Solution

This error occurred because there was another instance of Gunicorn running. To resolve it, follow these steps:

1. List all Docker containers:
   
   ```bash
   docker ps -a
   ```

2. List all Docker images:
   
   ```bash
   docker images
   ```

3. Stop the container:
   
   ```bash
   docker stop <container ID>
   ```

4. Remove the container:
   
   ```bash
   docker rm <container ID>
   ```

5. Remove the image:
   
   ```bash
   docker rmi <image>
   ```

Rebuild the Docker image and run it again. This time, it should work correctly, allowing you to serve the test script to the endpoint.