---
id: 1ed7cd56e9
question: How do I set up a virtual environment for the machine learning zoomcamp
  course?
sort_order: 112
---

You can set up a virtual environment using venv, uv, or conda:
**Using uv (recommended):**
```bash
uv venv mlzoomcamp-env
source mlzoomcamp-env/bin/activate  # On Windows: mlzoomcamp-env\Scripts\activate
uv pip install -r requirements.txt
```
**Using venv:**
```bash
python -m venv mlzoomcamp-env
source mlzoomcamp-env/bin/activate  # On Windows: mlzoomcamp-env\Scripts\activate
pip install -r requirements.txt
```
**Using conda:**
```bash
conda create -n mlzoomcamp python=3.10
conda activate mlzoomcamp
pip install -r requirements.txt
```