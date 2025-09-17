---
course: machine-learning-zoomcamp
id: efae76d03c
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_a22bc45c.png
question: Fix error during installation of Pipfile inside Docker container
section: 5. Deploying Machine Learning Models
sort_order: 2040
---

<{IMAGE:image_1}>

I tried the first solution on Stackoverflow which recommended running `pipenv lock` to update the Pipfile.lock. However, this didn’t resolve it. But the following switch to the pipenv installation worked

RUN pipenv install --system --deploy --ignore-pipfile

