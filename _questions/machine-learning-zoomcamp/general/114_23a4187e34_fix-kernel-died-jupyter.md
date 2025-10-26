---
id: 23a4187e34
question: How do I fix 'Kernel appears to have died' error in Jupyter Notebook?
sort_order: 114
---

Kernel crashes with the message 'Kernel appears to have died. It will restart automatically' due to a variety of common causes, including memory pressure, infinite loops, outdated packages, or resource limits. Try the following steps:

1) Increase memory allocation for analysis tasks: reduce dataset size for testing
```python
# Reduce dataset size for testing
df_sample = df.sample(frac=0.1, random_state=42)
```

2) Clear output and restart kernel: Kernel → Restart & Clear Output. Then re-run cells one by one to identify which cell causes the crash.

3) Check for infinite loops or memory leaks: monitor memory usage while running
```python
# Add memory monitoring
import psutil
print(f"Memory usage: {psutil.virtual_memory().percent}%")
```

4) Update your packages: Outdated libraries can cause kernel crashes
```
pip install --upgrade jupyter notebook ipykernel
```

5) Check system resources: Monitor CPU and RAM usage while running the notebook
```bash
# Linux/Mac
top
# Or use htop for better visualization
htop
```

If the issue persists, try running your code in a Python script instead of a notebook to see if it's a Jupyter-specific issue.