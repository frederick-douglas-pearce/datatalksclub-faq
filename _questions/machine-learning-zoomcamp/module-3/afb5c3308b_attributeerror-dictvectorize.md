---
id: afb5c3308b
question: 'AttributeError: ''DictVectorizer'' object has no attribute ''get_feature_names'''
sort_order: 1320
---

The solution is to use `get_feature_names_out` instead. See details: [https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html)