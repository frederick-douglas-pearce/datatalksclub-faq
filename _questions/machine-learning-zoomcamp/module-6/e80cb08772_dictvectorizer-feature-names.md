---
id: e80cb08772
question: DictVectorizer feature names
sort_order: 2580
---

The DictVectorizer has a function to get the feature names [get_feature_names_out()](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.get_feature_names_out:~:text=always%202%2Dd.-,get_feature_names_out,-(input_features%3D). This is helpful for example if you need to analyze feature importance but use the dict vectorizer for one hot encoding. Just keep in mind it does return a numpy array so you may need to convert this to a list depending on your usage for example dv.get_feature_names_out() will return a ndarray array of string objects. list(dv.get_feature_names_out()) will convert to a standard list of strings. Also keep in mind that you first need to fit the predictor and response arrays before you have access to the feature names.

Quinn Avila

