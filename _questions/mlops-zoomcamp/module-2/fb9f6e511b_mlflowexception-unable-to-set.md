---
id: fb9f6e511b
question: 'MlflowException: Unable to Set a Deleted Experiment'
sort_order: 940
---

raise MlflowException(

mlflow.exceptions.MlflowException: Cannot set a deleted experiment 'random-forest-hyperopt' as the active experiment. You can restore the experiment, or permanently delete the experiment to create a new one.

There are many options to solve in this link: [https://stackoverflow.com/questions/60088889/how-do-you-permanently-delete-an-experiment-in-mlflow](https://stackoverflow.com/questions/60088889/how-do-you-permanently-delete-an-experiment-in-mlflow)

✅Had deleted the experiment from the mlflow ui, and this command in CLI works mlflow gc --backend-store-uri sqlite:///backend.db (use the filename.db that you had used, obviously)

⛔ Below suggestion didn’t work, as .trash/ was already empty

rm -rf mlruns/.trash/*

zsh: sure you want to delete all the files in /home/ellacharmed/github/mlops-zoomcamp/cohorts/2024/02-experiment-tracking/homework/mlruns/.trash [yn]? y

zsh: no matches found: mlruns/.trash/*

