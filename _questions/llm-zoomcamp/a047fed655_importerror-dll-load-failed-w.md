---
course: llm-zoomcamp
id: a047fed655
question: 'ImportError: DLL load failed while importing onnxruntime_pybind11_state:
  A dynamic link library (DLL) initialization routine failed.'
section: 'Module 2: Vector Search'
sort_order: 430
---

If you use Anaconda or Miniconda, you can try re-installing onnxruntime with conda

conda install -c conda-forge onnxruntime

One of the ways you can create an environment to use "qdrant-client[fastembed]>=1.14.2" which throws this error is to create the environment using Conda. Here are the steps -

Create a Conda environment usingconda create --name llm-zoomcamp-env python=3.10

Activate your new environmentconda activate llm-zoomcamp-env

Install the dependencypip install "qdrant-client[fastembed]>=1.14.2"

Use this environment either using Jupyter notebook or in VSCode/CursorFor VSCode/Cursor -> Ctrl+Shift+P/Cmd+Shift+P -> Select Python Enterpreter -> Select llm-zoomcamp-env

