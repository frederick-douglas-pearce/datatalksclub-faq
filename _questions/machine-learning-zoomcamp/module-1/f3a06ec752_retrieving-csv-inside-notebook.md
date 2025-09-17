---
id: f3a06ec752
question: Downloading a csv file inside notebook
sort_order: 280
---

The best way is to use pandas and give it the URL directly:

url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'
df = pd.read_csv(url)

You can also execute cmd/bash commands inside Jupyter: 

!wget [raw.githubusercontent.com](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv)

To download the data too. The exclamation mark !, lets you execute shell commands inside your notebooks. This works generally for shell commands such as ls, cp, mkdir, mv etc . . .

For instance, if you then want to move your data into a data directory alongside your notebook-containing directory, you could execute the following:!mkdir -p ../data/

!mv housing.csv ../data/

