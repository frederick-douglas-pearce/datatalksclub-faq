---
id: 1fda7c57b0
question: 'ValueError: shapes not aligned'
sort_order: 800
---

```
X_train = prepare_X(df_train)
w_0, w = train_linear_regression(X_train, y_train)

X_val = prepare_X(df_val)
y_pred = w_0 + X_val.dot(w)

rmse(y_val, y_pred)
```

We get:

```
ValueError                                Traceback (most recent call last)
Input In [132], in <cell line: 5>()
      2 w_0, w = train_linear_regression(X_train, y_train)
      4 X_val = prepare_X(df_val)
----> 5 y_pred = w_0 + X_val.dot(w)
      7 rmse(y_val, y_pred)

ValueError: shapes (4128,) and (1,) not aligned: 4128 (dim 0) != 1 (dim 0)
```


If we try to perform an arithmetic operation between 2 arrays of different shapes or different dimensions, it throws an error like operands could not be broadcast together with shapes. There are some scenarios when broadcasting can occur and when it fails.

If this happens sometimes we can use * operator instead of dot() method to solve the issue. So that the error is solved and also we get the dot product.


```python
X_train = prepare_X(df_train)
w_0, w = train_linear_regression(X_train, y_train)

X_val = prepare_X(df_val)
y_pred = w_0 + (X_val * w)

rmse(y_val, y_pred)
```

Output:

0.5713144443358035


(Santhosh Kumar)

