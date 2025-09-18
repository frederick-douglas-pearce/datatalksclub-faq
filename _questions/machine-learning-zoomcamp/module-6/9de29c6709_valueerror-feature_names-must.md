---
id: 9de29c6709
question: 'ValueError: feature_names must be string, and may not contain [, ] or <'
sort_order: 2600
---

This error occurs because the list of feature names contains unsupported characters like "<". To fix this issue, replace those problematic characters with supported ones.

To create a consistent list of features without special characters, use the following code:

```python
features = [f.replace('=<', '_').replace('=', '_') for f in features]
```

This will replace any instances of "=<" and "=" with "_", ensuring that the feature names only consist of supported characters.