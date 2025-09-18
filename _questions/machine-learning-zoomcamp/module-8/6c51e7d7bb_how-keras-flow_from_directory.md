---
id: 6c51e7d7bb
question: How does keras flow_from_directory know the names of classes in images?
sort_order: 2870
---

Keras `flow_from_directory` understands the names of classes from the names of folders.

### Explanation

- When using `train_gen.flow_from_directory()`, the class names are derived from the folder names within the specified directory.
- For example, if you create a folder named "xyz", it will be considered a class.
- This behavior aligns with the function name `flow_from_directory`.

A detailed explanation can be found in this [tutorial](https://vijayabhaskar96.medium.com/tutorial-image-classification-with-keras-flow-from-directory-and-generators-95f75ebe5720).

### Error with TensorFlow Importing using Saturn Cloud Preconfigured Template

```python
TypeError: Unable to convert function return value to a Python type! The signature was () -> handle.
```

### Solution

1. Uninstall and reinstall TensorFlow that you obtained from Saturn Cloud.
2. Repeat the reinstallation process two or three times if necessary.
   
- This approach addresses potential dependency conflicts.
- TensorFlow relies on various libraries (e.g., protobuf, numpy, grpcio) that might cause issues.
- Reinstalling ensures all dependencies align with the correct version, resolving underlying issues.

### Additional Note

- It may take a moment for the system to recognize environment changes after package installation.
- Sometimes, multiple installation attempts are required to transition to the correct state, especially after restarting the Jupyter kernel.

