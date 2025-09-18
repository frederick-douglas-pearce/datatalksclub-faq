---
id: 0482efe115
question: Get_feature_names() not found
sort_order: 4020
---

Problem: In the course, the function `dv.get_feature_names()` was used to get features from the `DictVectorizer` instance. However, it didn't work on my computer. This issue may relate to library versions, and the function is reportedly to be deprecated soon.

- **Old documentation:** [https://scikit-learn.org/0.22/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names](https://scikit-learn.org/0.22/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names)

- **New documentation:** [https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names)

Solution:

- Change the line:

  ```python
  dv.get_feature_names()
  ```

  To:

  ```python
  list(dv.get_feature_names_out())
  ```