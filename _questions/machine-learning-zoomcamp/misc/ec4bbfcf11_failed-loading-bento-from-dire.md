---
id: ec4bbfcf11
question: 'Failed loading Bento from directory /home/bentoml/bento: Failed to import
  module "service": No module named ''sklearn'''
sort_order: 3920
---

I was getting the following error message when trying to create a Docker image using BentoML:

```bash
[bentoml-cli] `serve` failed: Failed loading Bento from directory /home/bentoml/bento: Failed to import module "service": No module named 'sklearn'
```

### Solution Description

The issue was due to a typo in `bentofile.yaml`. I had mistakenly written `sklearn` instead of `scikit-learn`. The issue was resolved by modifying the packages list as shown below:

```yaml
packages: # Additional pip packages required by the service
  - xgboost
  - scikit-learn
  - pydantic
```