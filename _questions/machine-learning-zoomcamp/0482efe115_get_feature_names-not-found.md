---
course: machine-learning-zoomcamp
id: 0482efe115
question: Get_feature_names() not found
section: Miscellaneous
sort_order: 4020
---

Problem: In the course this function worked to get the features from the dictVectorizer instance: dv.get_feature_names(). But in my computer did not work. I think it has to do with library versions and but apparently that function will be deprecated soon:

Old: [[scikit-learn.org](https://scikit-learn.org/0.22/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names)](https://scikit-learn.org/0.22/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names)

New: [[scikit-learn.org](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.get_feature_names)

Solution: change the line dv.get_feature_names() to list(dv.get_feature_names_out))

Ibai Irastorza

