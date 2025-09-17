---
id: 59fc88dea8
question: How to output only a certain number of decimal places
sort_order: 550
---

You can use round() function or f-strings

round(number, 4)  - this will round number up to 4 decimal places

print(f'Average mark for the Homework is {avg:.3f}') - using F string

Also there is pandas.Series. round idf you need to round values in the whole Series

Please check the documentation[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.round.html#pandas.Series.round](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.round.html#pandas.Series.round)

Added by Olga Rudakova

