---
id: 1c7dc011f1
question: 'Homework: Getting Wrong RMSE that is not matching or close to answer options
  in HW 2(Regression) of 2024 Cohort.'
sort_order: 4280
---

The following piece of code, which involves shuffling, is crucial to getting RMSE values close to the answer options in the homework:

```python
import numpy as np

df = orig_df.copy()

base = ['ram','storage','screen','final_price']

my_df = df[base]

idx = np.arange(n)

np.random.seed(s)

np.random.shuffle(idx)

df_shuffled = my_df.iloc[idx]

df_train = df_shuffled.iloc[idx[:n_train]].copy()

df_val = df_shuffled.iloc[idx[n_train:n_train+n_val]].copy()

df_test = df_shuffled.iloc[idx[n_train+n_val:]].copy()

df_train = df_train.reset_index(drop=True)

df_val = df_val.reset_index(drop=True)

df_test = df_test.reset_index(drop=True)

y_train = df_train.final_price.values

y_val = df_val.final_price.values

y_test = df_test.final_price.values

del df_train['final_price']
del df_val['final_price']
del df_test['final_price']
```

- Ensure the logic is correct to avoid incorrect RMSE calculations.

**CUDA ran out of memory in Google Colab**

When running models on Google Colab or Kaggle, you might encounter a runtime error related to CUDA running out of memory. Here are some tips to address this:

- Reduce the batch size.
- Use lower precision.
- Clear the cache to free up unused GPU memory:

  ```python
  import torch
torch.cuda.empty_cache()
  ```

- Delete unnecessary variables.

For more details, refer to the following resources:

- [Stack Overflow](https://stackoverflow.com/questions/54374935/how-can-i-fix-this-strange-error-runtimeerror-cuda-error-out-of-memory)
- [Medium Article](https://medium.com/@snk.nitin/how-to-solve-cuda-out-of-memory-error-850bb247cfb2)