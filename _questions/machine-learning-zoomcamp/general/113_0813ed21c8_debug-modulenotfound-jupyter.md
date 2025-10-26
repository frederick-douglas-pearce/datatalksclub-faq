---
id: 0813ed21c8
question: How do I debug ModuleNotFoundError when running Jupyter notebooks?
sort_order: 113
---

## Debugging ModuleNotFoundError in Jupyter notebooks
If you encounter a ModuleNotFoundError when running Jupyter notebooks, try the following steps:

1) Install the required dependencies

```bash
pip install -r requirements.txt
```

2) Ensure Jupyter is using the correct Python environment

```bash
jupyter kernelspec list
```

3) If needed, install the kernel for your virtual environment

```bash
python -m ipykernel install --user --name=ml-zoomcamp
```

After completing these steps, restart Jupyter and try running the notebook again.