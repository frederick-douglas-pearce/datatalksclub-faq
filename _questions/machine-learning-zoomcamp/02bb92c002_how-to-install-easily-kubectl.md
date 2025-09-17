---
course: machine-learning-zoomcamp
id: 02bb92c002
question: How to install easily kubectl on windows ?
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3510
---

To install kubectl on windows using the terminal in vscode (powershell), I followed this tutorial: [https://medium.com/@ggauravsigra/install-kubectl-on-windows-af77da2e6fff](https://medium.com/@ggauravsigra/install-kubectl-on-windows-af77da2e6fff)

I first downloaded kubectl with curl, with these command lines: [https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/#install-kubectl-binary-with-curl-on-windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/#install-kubectl-binary-with-curl-on-windows)

At step 3, I followed the tutorial with the copy of the exe file in a specific folder on C drive.

Then I added this folder path to PATH in my environment variables.

Kind can be installed the same way with the curl command on windows, by specifying a folder that will be added to the path environment variable.

Added by Mélanie Fouesnard

