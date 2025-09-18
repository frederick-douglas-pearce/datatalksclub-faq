---
id: 07af4ad134
question: How to calculate Root Mean Squared Error?
sort_order: 1310
---

We can use `sklearn` and `numpy` packages to calculate Root Mean Squared Error:

```python
from sklearn.metrics import mean_squared_error
import numpy as np

RMSE = np.sqrt(mean_squared_error(y_pred, y_val/y_test))
```

You can also refer to this code from Alexey’s notebook for Week 2:

```python
def rmse(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)
```

[GitHub Repository](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb)