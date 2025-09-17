---
id: b3fe59d431
question: 'Video 3.3.4 Training Metrics RMSE chart does not show due to the error:
  KeyError: ‘rmse_LinearRegression’'
sort_order: 1520
---

Solution: Check the difference between xgboost and sklearn pipelines. In xgboost pipeline there is a track_experiment callback while in sklearn pipeline is not.

Please add those lines:

You can refer them in my similar commit

[Lines to be added](https://github.com/nilarte/mlops-zoomcamp-mage/commit/16c01dfcc2541a03a49f4744d0b0f0207c06e99d#diff-a97c890cfc31702e4b94f1e9a05558ebb8a57349fc9ccf153e82ae53af1bd53e)

Added by Nilesh Arte

