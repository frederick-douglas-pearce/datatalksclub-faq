---
id: 19a42e2005
question: How to combine train and validation datasets
sort_order: 890
---

Use ‘pandas.concat’ function ([https://pandas.pydata.org/docs/reference/api/pandas.concat.html](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)) to combine two dataframes. To combine two numpy arrays use numpy.concatenate ([https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)) function. So the code would be as follows:

df_train_combined = pd.concat([df_train, df_val])

y_train = np.concatenate((y_train, y_val), axis=0)

(George Chizhmak)

