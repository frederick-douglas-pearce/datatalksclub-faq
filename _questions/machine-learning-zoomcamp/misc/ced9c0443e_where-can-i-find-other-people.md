---
id: ced9c0443e
question: 'Cohort 2024: Where can I find other people’s projects to peer review them
  and where do I post mine for peer review?'
sort_order: 4320
---

The review assignments will be available on [CoursePlatform](https://courses.datatalks.club/ml-zoomcamp-2024/) after the first phase of the project is over, i.e., after the submission deadline. After that, you will have one week to complete the review.

Saturn Cloud errors in Jupyter Notebook:

```
ImportError: cannot import name 'runtime_version' from 'google.protobuf'
```

Can be resolved by updating protobuf:

```bash
!pip install -U protobuf
```

Works for TensorFlow 2.17.0 and protobuf 4.25.5 (5.29.0 after updating).

Additionally, updating TensorFlow to 2.18.0 can resolve the issue of the `model.fit` function hanging:

```bash
!pip install -U tensorflow
```