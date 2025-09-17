---
id: c6f2a2afe5
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_03f8bfd8.jpg
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_a95d78a7.jpg
question: How to fix when %%capture output is not working in Google Collab Notebook
sort_order: 2400
---

I was using Google Collab Notebook for the 2024 cohort HW 06. For the Q6 here, the

<{IMAGE:image_1}>

<{IMAGE:image_2}>

was not working in the Collab Notebook. This led me to find a solution which is as follows:

# import the required libraries

import io

import sys

# Capture output using io.StringIO

output_capture = io.StringIO()

sys.stdout = output_capture  # Redirect stdout to the StringIO buffer

# Train the model with eta=0.3

model_eta_03 = xgb.train(xgb_params, dtrain, num_boost_round=num_rounds, verbose_eval=2, evals=watchlist)

# Reset stdout

sys.stdout = sys.__stdout__

# Retrieve and print the captured output

captured_output = output_capture.getvalue()

And, we need to slightly modify the parser function for only one line:

for line in output.stdout.strip().split('\n'):    # replace this line 3 in Alexey’s parser function with

for line in output.strip().split('\n'):

And  then call the df_score_03 = parse_xgb_output(captured_output)for getting the desired dataframe.

(Added by Siddhartha Gogoi)

