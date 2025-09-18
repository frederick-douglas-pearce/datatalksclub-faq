---
id: f7d54cfa6f
question: Reading the dataset directly from GitHub
sort_order: 640
---

The dataset can be read directly into a pandas DataFrame from a GitHub link using the technique shown below:

```python
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv")
```