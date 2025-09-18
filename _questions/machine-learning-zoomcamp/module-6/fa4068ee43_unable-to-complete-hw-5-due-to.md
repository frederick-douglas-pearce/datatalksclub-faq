---
id: fa4068ee43
question: 'Homework: Unable to complete HW 5 due to running Docker on M1 and not using
  Docker Desktop.'
sort_order: 2370
---

### Solution

- If you replaced Docker Desktop with 'lima', you can create an instance of Lima using the [following template](https://gist.github.com/akrylysov/7c1ea3bac409da2758e525f2f82e6373). Follow the instructions listed on the page to create an instance using the supplied template.
- Switch your current Docker context to the context associated with this new (running) image.
- Use `svizor/zoomcamp-model:3.11.5-slim` as a base image and run your built image without issues.

#### Simple Solution:

- Specify the platform:

  ```bash
  docker run --platform linux/amd64 -it --rm -p 9696:9696 <your-docker-image-name>
  ```

### Additional Q&A

#### Q: Why do I get the error `TypeError: Expecting a sequence of strings for feature names, got: <class 'numpy.ndarray'>` when using xgb.DMatrix?

**A:** This error occurs because recent versions of xgb.DMatrix expect the `feature_names` parameter to be a list of strings rather than a NumPy array. Older tutorial videos might use `feature_names=dv.get_feature_names_out()` directly, which now results in this error.

**Solution:** Convert `dv.get_feature_names_out()` to a list using `.tolist()`. Here's an updated example:

```python
# Convert feature names to a list
feature_names = dv.get_feature_names_out().tolist()

# Create DMatrix objects with the corrected feature names
dfulltrain = xgb.DMatrix(X_full_train, 
                         label=y_full_train, 
                         feature_names=feature_names)

dtest = xgb.DMatrix(X_test, 
                    feature_names=feature_names)
```

**Explanation:** The `dv.get_feature_names_out()` method returns a NumPy array, but `xgb.DMatrix` now expects `feature_names` to be a list of strings. Using `.tolist()` converts the array into a compatible format, allowing the code to run without errors.