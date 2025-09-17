---
course: mlops-zoomcamp
id: 7032c161df
images:
- description: 'image #1'
  id: image_1
  path: images/mlops-zoomcamp/image_168171a5.png
question: MLflow.xgboost Autolog Model Signature Failure
section: 'Module 2: Experiment tracking'
sort_order: 930
---

Got the same warning message as Warrie Warrie when using “mlflow.xgboost.autolog()”

<{IMAGE:image_1}>

It turned out that this was just a warning message and upon checking MLflow UI (making sure that no “tag” filters were included), the model was actually automatically tracked in the MLflow.

Added by Bengsoon Chuah, Asked by Warrie Warrie, Answered by Anna Vasylytsya & Ivan Starovit

