---
id: c58d3563a6
question: 'Python - These won''t work. You need to make sure you use Int64:'
sort_order: 2430
---

Incorrect:

df['DOlocationID'] = pd.to_numeric(df['DOlocationID'], downcast=integer) or

df['DOlocationID'] = df['DOlocationID'].astype(int)

Correct:

df['DOlocationID'] = df['DOlocationID'].astype('Int64')

