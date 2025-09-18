---
id: 45482efa5e
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_852cd1cd.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_6476267e.png
question: Identifying highly correlated feature pairs easily through unstack
sort_order: 1050
---

To identify highly correlated feature pairs using unstack:

```python
import pandas as pd

data_corr = pd.DataFrame(data_num.corr().round(3).abs().unstack().sort_values(ascending=False))

print(data_corr.head(10))
```

You can also use seaborn to create a heatmap with the correlation:

```python
import seaborn as sns

sns.heatmap(df[numerical_features].corr(),
            annot=True,
            square=True,
            fmt=".2g",
            cmap="crest")
```

To refine your heatmap and plot only a triangle, with a blue to red color gradient, that will show every correlation between your numerical variables without redundant information:

<{IMAGE:image_1}>

Which outputs, in the case of a churn dataset:

<{IMAGE:image_2}>
