---
id: 3b78e09b80
question: How do I set up a virtual environment for the ML Zoomcamp course, and which
  tools should I use (uv, venv, or conda)?
sort_order: 104
---

You can set up a virtual environment using uv (recommended), venv, or conda.

Using uv (recommended):
```bash
uv venv mlzoomcamp-env
source mlzoomcamp-env/bin/activate  # On Windows: mlzoomcamp-env\\Scripts\\activate
uv pip install -r requirements.txt
````
Using venv:
```bash
python -m venv mlzoomcamp-env
source mlzoomcamp-env/bin/activate  # On Windows: mlzoomcamp-env\\Scripts\\activate
pip install -r requirements.txt
````
Using conda:
```bash
conda create -n mlzoomcamp python=3.10
conda activate mlzoomcamp
pip install -r requirements.txt
```

Note: Install Python easily with Anaconda (especially on Windows). Use uv for virtual environments and package installs (recommended over conda for this course). The uv + FastAPI workshop is included in Module 5.
