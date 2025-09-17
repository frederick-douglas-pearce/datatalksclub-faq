---
course: machine-learning-zoomcamp
id: 4076e3f3a6
question: '''kind'' is not recognized as an internal or external command, operable
  program or batch file. (In Windows)'
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3590
---

Problem: I download kind from the next command:

curl.exe -Lo kind-windows-amd64.exe [[kind.sigs.k8s.io](https://kind.sigs.k8s.io/dl/v0.17.0/kind-windows-amd64)](https://kind.sigs.k8s.io/dl/v0.17.0/kind-windows-amd64)

When I try

kind --version

I get: 'kind' is not recognized as an internal or external command, operable program or batch file

Solution: The default name of executable is kind-windows-amd64.exe, so that you have to rename this file to  kind.exe. Put this file in specific folder, and add it to PATH

Alejandro Aponte

