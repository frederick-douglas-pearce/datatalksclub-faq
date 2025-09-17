---
id: 631e3d040c
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_008f5d2a.png
question: Why linear regression doesn’t provide a “perfect” fit?
sort_order: 730
---

linear regression often provides a good approximation of the underlying relationship but rarely achieves a "perfect" fit in real-world applications.

Q: “In lesson 2.8 why is y_pred different from y? After all, we trained X_train to get the weights that when multiplied by X_train should give exactly y, or?”

A: linear regression is a pretty simple model, it neither can nor should fit 100% (nor any other model, as this would be the sign of overfitting). This picture might illustrate some intuition behind this, imagine X is a single feature:

<{IMAGE:image_1}>

As our model is linear, how would you draw a line to fit all the "dots"?

You could "fit" all the "dots" on this pic using something like [scipy.optimize.curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) (non-linear least squares) if you wanted to, but imagine how it would perform on previously unseen data.

Added by Andrii Larkin

