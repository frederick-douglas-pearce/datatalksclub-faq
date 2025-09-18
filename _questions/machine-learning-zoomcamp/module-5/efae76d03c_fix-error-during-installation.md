---
id: efae76d03c
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_a22bc45c.png
question: 'Docker: Fix error during installation of Pipfile inside Docker container'
sort_order: 2040
---

<{IMAGE:image_1}>

I tried the first solution on Stackoverflow which recommended running `pipenv lock` to update the Pipfile.lock. However, this didn’t resolve it. The following switch to the pipenv installation worked:

```bash
RUN pipenv install --system --deploy --ignore-pipfile
```