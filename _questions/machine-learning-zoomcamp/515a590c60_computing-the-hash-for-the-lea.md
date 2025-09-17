---
course: machine-learning-zoomcamp
id: 515a590c60
question: Computing the hash for the leaderboard and project review
section: 1. Introduction to Machine Learning
sort_order: 260
---

Leaderboard Links:

2024 - [[DataTalks Course](https://courses.datatalks.club/ml-zoomcamp-2024/leaderboard)](https://courses.datatalks.club/ml-zoomcamp-2024/leaderboard)

2023 - [[Google Docs](https://docs.google.com/spreadsheets/d/e/2PACX-1vSNK_yGtELX1RJK1SSRl4xiUbD0XZMYS6uwHnybc7Mql-WMnMgO7hHSu59w-1cE7FeFZjkopbh684UE/pubhtml)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSNK_yGtELX1RJK1SSRl4xiUbD0XZMYS6uwHnybc7Mql-WMnMgO7hHSu59w-1cE7FeFZjkopbh684UE/pubhtml)

2022 - [[Google Docs](https://docs.google.com/spreadsheets/d/e/2PACX-1vQzLGpva63gb2rIilFnpZMRSb-buyr5oGh8jmDtIb8DANo4n6hDalra_WRCl4EZwO1JvaC4UIS62n5h/pubhtml)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQzLGpva63gb2rIilFnpZMRSb-buyr5oGh8jmDtIb8DANo4n6hDalra_WRCl4EZwO1JvaC4UIS62n5h/pubhtml)

Python Code:

from hashlib import sha1

def compute_hash(email):

return sha1(email.lower().encode('utf-8')).hexdigest()

You need to call the function as follows:

print(compute_hash('YOUR_EMAIL_HERE'))

The quotes are required to denote that your email is a string.

(By Wesley Barreto)

You can also use this website directly by entering your email: [[sha1-online.com](http://www.sha1-online.com)](http://www.sha1-online.com/). Then, you just have to copy and paste your hashed email in the “research” bar of the leaderboard to get your scores.

(Mélanie Fouesnard)

