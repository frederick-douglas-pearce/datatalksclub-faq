---
id: bcedbb12fe
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_6e1c348d.png
question: 'Could not install packages due to an OSError: [WinError 5] Access is denied'
sort_order: 3490
---

When I ran the command:

```bash
pip install grpcio==1.42.0 tensorflow-serving-api==2.7.0
```

to install the libraries on a Windows machine, I encountered the following error:

```
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'C:\\Users\\Asia\\anaconda3\\Lib\\site-packages\\google\\protobuf\\internal\\_api_implementation.cp39-win_amd64.pyd'
```

Consider using the `--user` option or check the permissions.

<{IMAGE:image_1}>

### Solution Description:

I was able to successfully install the libraries using the following command:

```bash
pip --user install grpcio==1.42.0 tensorflow-serving-api==2.7.0
```

---

### Kubernetes Deployment Issue: Pods Not Starting

**Solution:** This issue can be caused by several factors:

- **Resource Allocation:** Ensure that your Pods have enough CPU and memory resources allocated. If resources are too low, the Kubernetes scheduler might fail to schedule your Pods.

- **Image Issues:** Verify that the Docker image specified for your Pod is correctly built and accessible. If the image cannot be pulled from the repository, the Pod won’t start.