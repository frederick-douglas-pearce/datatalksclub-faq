---
id: ec4bbfcf11
question: 'Failed loading Bento from directory /home/bentoml/bento: Failed to import
  module "service": No module named ''sklearn'''
sort_order: 3920
---

I was getting the below error message when I was trying to create docker image using bentoml

[bentoml-cli] `serve` failed: Failed loading Bento from directory /home/bentoml/bento: Failed to import module "service": No module named 'sklearn'

Solution description

The cause was because , in bentofile.yaml, I wrote sklearn instead of scikit-learn. Issue was fixed after I modified the packages list as below.

packages: # Additional pip packages required by the service

- xgboost

- scikit-learn

- pydantic

Asia Saeed

