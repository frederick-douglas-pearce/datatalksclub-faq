---
id: 167b32b84c
question: 'BentoML not working with –production flag at any stage: e.g. with bentoml
  serve and while running the bentoml container'
sort_order: 3930
---

You might see a long error message related to sparse matrices, and in the swagger UI, you receive a code 500 error with an empty string as output.

**Potential Reason:**

- If you have set `DictVectorizer` or `OneHotEncoder` (OHE) to sparse while training and stored this in a pipeline or custom object during the BentoML model saving stage in `train.py`, each input becomes a different sized sparse matrix when called in `service.py`. This inconsistency prevents batching due to varying lengths.

**Solution:**

- Ensure that BentoML model signatures have `batchable` set to `False` for production when saving the BentoML model in `train.py`.