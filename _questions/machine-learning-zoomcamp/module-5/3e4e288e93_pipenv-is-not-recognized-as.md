---
id: 3e4e288e93
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_6db28918.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_3b4fce52.png
- description: 'image #3'
  id: image_3
  path: images/machine-learning-zoomcamp/image_b2712e9d.png
- description: 'image #4'
  id: image_4
  path: images/machine-learning-zoomcamp/image_a4cd7017.png
question: '''pipenv'' is not recognized as an internal or external command, operable
  program or batch file.'
sort_order: 1990
---

This error happens because pipenv is already installed but you can't access it from the path.

This error comes out if you run.

pipenv  --version

pipenv shell

Solution for Windows

Open this option

<{IMAGE:image_1}>

Click here

<{IMAGE:image_2}>

Click in Edit Button

<{IMAGE:image_3}>

Make sure the next two locations are on the PATH, otherwise, add it.

C:\Users\AppData\....\Python\PythonXX\

C:\Users\AppData\....\Python\PythonXX\Scripts\

<{IMAGE:image_4}>

Added by Alejandro Aponte

Note: this answer assumes you don’t use Anaconda. For Windows, using Anaconda would be a better choice and less prone to errors.

