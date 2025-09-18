---
id: e6d04a94b1
question: CUDA toolkit and cuDNN Install for Tensorflow
sort_order: 4090
---

Install Nvidia drivers: [https://www.nvidia.com/download/index.aspx](https://www.nvidia.com/download/index.aspx).

### Windows:

- Install Anaconda prompt: [https://www.anaconda.com/](https://www.anaconda.com/)
- Two options:
  1. Install package `tensorflow-gpu` in Anaconda.
  2. Install the Tensorflow way: [https://www.tensorflow.org/install/pip#windows-native](https://www.tensorflow.org/install/pip#windows-native)

### WSL/Linux:

- WSL: Use the Windows Nvidia drivers, do not modify them.
- Two options:
  1. Install the Tensorflow way: [https://www.tensorflow.org/install/pip#linux_1](https://www.tensorflow.org/install/pip#linux_1)
     - Make sure to follow step 4 to install CUDA by environment.
     - Also run:

     ```bash
     echo 'export XLA_FLAGS=--xla_gpu_cuda_data_dir=$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
     ```
  2. Install CUDA toolkit 11.x.x: [https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)
  
- Install cuDNN: [https://developer.nvidia.com/rdp/cudnn-download](https://developer.nvidia.com/rdp/cudnn-download)

Now you should be able to perform training/inference with GPU in Tensorflow.

### Learning in Public:

Provide the LinkedIn link to where you posted about your progress using `#mlzoomcamp` tag. The scores for this part will be capped at 7 points.

### Kaggle Assistance:

If you had issues uploading datasets to Kaggle, see this guide for help: [Kaggle](https://www.kaggle.com/code/dansbecker/finding-your-files-in-kaggle-kernels/noteboo)k.