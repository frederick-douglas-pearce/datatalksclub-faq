---
id: eb3d73e55e
question: Root Mean Squared Error
sort_order: 1330
---

To use RMSE without math or numpy, ‘sklearn.metrics’ has a mean_squared_error function with a squared kwarg (defaults to True). Setting squared to False will return the RMSE.

from sklearn.metrics import mean_squared_error

rms = mean_squared_error(y_actual, y_predicted, squared=False)

See details: [https://stackoverflow.com/questions/17197492/is-there-a-library-function-for-root-mean-square-error-rmse-in-python](https://stackoverflow.com/questions/17197492/is-there-a-library-function-for-root-mean-square-error-rmse-in-python)

Ahmed Okka

