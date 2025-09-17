---
course: machine-learning-zoomcamp
id: ac3fde375f
question: 'and (sparse=False) produce the same type of one-hot encodings: [pandas.get_dummies()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html)
  [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html)'
section: 3. Machine Learning for Classification
sort_order: 1120
---

![Image](images/machine-learning-zoomcamp/image_e1899130.png)

(sparse=True) produces  format, which is both more memory efficient and converges better during fit(). Basically it stores non-zero values and indices instead of adding a column for each class of each feature (models of cars produced 900+ columns alone in the current task). [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html) [CSR](https://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_row_(CSR,_CRS_or_Yale_format))

Using “sparse” format like on the picture above, both via  and (sparse=False) - is slower (around 6-8min for Q6 task - Linear/Ridge Regression) for high amount of classes (like models of cars for eg) and gives a bit “worse” results in both Logistic and Linear/Ridge Regression, while also producing convergence warnings for Linear/Ridge Regression. [pandas.get_dummies()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html) [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html)

Larkin Andrii

