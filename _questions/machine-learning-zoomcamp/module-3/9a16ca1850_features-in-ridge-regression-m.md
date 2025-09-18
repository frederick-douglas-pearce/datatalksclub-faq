---
id: 9a16ca1850
question: Features in Ridge Regression Model
sort_order: 1240
---

Make sure that the features used in a Ridge Regression model are only numerical, not categorical.

- Drop all categorical features first before proceeding.

While it's true that Ridge Regression accepts only numerical values, categorical ones can be useful for your model. You need to transform them using one-hot encoding before training the model.

- To avoid the error of non-convergence, set `sparse=True` when performing one-hot encoding.