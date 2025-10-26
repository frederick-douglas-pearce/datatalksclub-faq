---
id: 0813ed21c8
question: How do I fix a ModuleNotFoundError when running Jupyter notebooks?
sort_order: 113
---

## Debugging ModuleNotFoundError in Jupyter notebooks
If you encounter a ModuleNotFoundError when running Jupyter notebooks, try the following comprehensive steps:

1) Ensure required dependencies are installed

```bash
pip install -r requirements.txt
```

2) Verify Jupyter is using the correct Python environment

```bash
jupyter kernelspec list
```

3) If needed, install the kernel for your virtual environment

```bash
python -m ipykernel install --user --name=ml-zoomcamp
```

4) Restart the Jupyter kernel and try again
In Jupyter, Kernel → Restart & Clear Output or run:
```bash
jupyter notebook --clear-output
```

5) Make sure you're importing the correct package name
Check the actual package name and verify your import matches it, e.g.:
```bash
pip show scikit-learn
```

6) Clear the Jupyter notebook cache and restart
```bash
jupyter notebook --clear-output
```

7) Reinstall the problematic package (force-reinstall)
```bash
pip install --force-reinstall <package-name>
```

8) If you're using a virtual environment, activate it before starting Jupyter
- Linux/macOS:
```bash
source venv/bin/activate
```
- Windows:
```bash
venv\Scripts\activate
```
Then start Jupyter:
```bash
jupyter notebook
```

9) Check Python path conflicts by inspecting in a notebook cell
```python
import sys
print(sys.path)
print(sys.executable)
```

10) For Conda environments, install packages using conda instead of pip
```bash
conda install <package-name>
```

If the problem persists, ensure you're in the correct directory and that the module is actually installed in your active environment with `pip list`.