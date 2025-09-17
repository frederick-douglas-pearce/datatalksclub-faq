---
course: machine-learning-zoomcamp
id: 03e27c386a
question: Isn't it easier to use DictVertorizer or get dummies before splitting the
  data into train/val/test? Is there a reason we wouldn't do this? Or is it the same
  either way?
section: 3. Machine Learning for Classification
sort_order: 1290
---

(Question by Connie S.)

The reason it's good/recommended practice to do it after splitting is to avoid data leakage - you don't want any data from the test set influencing the training stage (similarly from the validation stage in the initial training). See e.g. scikit-learn documentation on "Common pitfalls and recommended practices": [[scikit-learn.org](https://scikit-learn.org/stable/common_pitfalls.html)](https://scikit-learn.org/stable/common_pitfalls.html)

Answered/added by Rileen Sinha

