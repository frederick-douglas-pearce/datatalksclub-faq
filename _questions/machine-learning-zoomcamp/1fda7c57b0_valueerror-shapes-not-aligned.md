---
course: machine-learning-zoomcamp
id: 1fda7c57b0
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_cec8e139.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_73cda421.png
question: 'ValueError: shapes not aligned'
section: 2. Machine Learning for Regression
sort_order: 800
---

<{IMAGE:image_1}>

If we try to perform an arithmetic operation between 2 arrays of different shapes or different dimensions, it throws an error like operands could not be broadcast together with shapes. There are some scenarios when broadcasting can occur and when it fails.

If this happens sometimes we can use * operator instead of dot() method to solve the issue. So that the error is solved and also we get the dot product.

<{IMAGE:image_2}>

(Santhosh Kumar)

