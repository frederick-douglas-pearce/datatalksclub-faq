---
id: 3653e07733
question: How do I fix 'Kernel appears to have died' error in Jupyter Notebook?
sort_order: 112
---

If your Jupyter kernel crashes with "Kernel appears to have died. It will restart automatically" there are a few common fixes to try:

1) Increase memory allocation
- The kernel often crashes due to insufficient memory. You can test with a smaller sample first:
```python
# Reduce dataset size for testing
df_sample = df.sample(frac=0.1, random_state=42)
```

2) Clear output and restart kernel
- Go to Kernel → Restart & Clear Output, then re-run cells one by one to identify which cell causes the crash.

3) Check for infinite loops or memory leaks
- You can monitor memory usage during execution:
```python
# Add memory monitoring
import psutil
print(f"Memory usage: {psutil.virtual_memory().percent}%")
```

4) Update your packages
- Outdated libraries can cause kernel crashes: 
```bash
pip install --upgrade jupyter notebook ipykernel
```

5) Check system resources
- Monitor CPU and RAM usage while running the notebook:
```bash
# Linux/Mac
top
```
- Or use htop for a nicer visualization:
```bash
htop
```

6) If the issue persists
- Try running your code in a Python script instead of a notebook to determine if it's a Jupyter-specific issue.