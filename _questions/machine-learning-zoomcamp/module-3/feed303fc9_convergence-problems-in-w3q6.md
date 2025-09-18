---
id: feed303fc9
question: Convergence Problems in W3Q6
sort_order: 1130
---

If you're encountering the following warning:

```plaintext
ConvergenceWarning: The max_iter was reached which means the coef_ did not converge
```

This may be due to the ridge regression solver requiring features to be of the same scale.

### Solutions:

1. **Use Different Scalers**:
   - Experiment with different scalers as the Ridge solver is sensitive to the scale of features.
   - Refer to [notebook-scaling-ohe.ipynb](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/03-classification/notebook-scaling-ohe.ipynb) for examples.

2. **StandardScaler and OneHotEncoder**:
   - Apply `StandardScaler` to numeric fields.
   - Use `OneHotEncoder` with `sparse=False` for categorical features.
   - Separate the features (numeric and categorical) before applying the encoder, which may prevent the warning.