---
id: 0a545e0e4c
images:
- description: 'image #1'
  id: image_1
  path: images/mlops-zoomcamp/image_10815a9d.png
- description: 'image #2'
  id: image_2
  path: images/mlops-zoomcamp/image_e3defff0.png
question: Viewing SQLite Data Raw & Deleting Experiments Manually
sort_order: 1100
---

All the experiment and other tracking information in mlflow are stored in sqllite database provided while initiating the mlflow ui command. This database can be inspected using Pycharm’s Database tab by using the SQLLite database type. Once the connection is created as below, the tables can be queried and inspected using regular SQL. The same applies for any SQL backed database such as postgres as well.

This is very useful to understand the entity structure of the data being stored within mlflow and useful for any kind of systematic archiving of model tracking for longer periods.

Added by Senthilkumar Gopal

<{IMAGE:image_1}>

<{IMAGE:image_2}>

