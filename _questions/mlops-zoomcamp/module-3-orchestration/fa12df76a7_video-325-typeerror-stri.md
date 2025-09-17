---
id: fa12df76a7
question: 'Video 3.2.5 -  TypeError: string indices must be integers'
sort_order: 1410
---

If you had remove and re-add blocks, especially from the above issue with Global Data Products, remove the connections from the hyperparameter_tuning/sklearn block in the Tree panel to its upstream blocks and re-add them. Don’t forget to [Ctrl+S] to save Pipeline.

Video 3.2.8 Error with Xgboost pipeline: ValueError: not enough values to unpack (expected 3, got 1)

Solution: Ensure that you have created the variables as in the video and you have this order in your code.

data → [training_set](http://localhost:6789/pipelines/xgboost_training/edit?sideview=tree#)

data_2 → [hyperparameter_tuning/xgboost](http://localhost:6789/pipelines/xgboost_training/edit?sideview=tree#)

If not, remove the connections for the xgboost and reconnect starting with the training set, followed by hyperparameter_tuning/xgboost.

Added by Oluwadara Adedeji

