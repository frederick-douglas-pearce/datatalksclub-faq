---
id: 0a4f9065b1
question: Loading the dataset directly through Kaggle Notebooks
sort_order: 650
---

For users of kaggle notebooks, the dataset can be loaded through widget using the below command. Please remember that ! before wget is essential

!wget [https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv)

Once the dataset is loaded to the kaggle notebook server, it can be read through the below pandas command

df = pd.read_csv('housing.csv')

Harish Balasundaram

