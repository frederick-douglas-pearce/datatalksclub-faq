---
id: 1a166fc048
question: Error invoking API Gateway deploy API locally
sort_order: 3220
---

Problem: Trying to test API gateway in [9.7 - API Gateway: Exposing the Lambda Function](https://www.youtube.com/watch?v=wyZ9aqQOXvs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR), running: $ python test.py

With error message:

{'message': 'Missing Authentication Token'}

Solution:

Need to get the deployed API URL for the specific path you are invoking. Example:

[<random](https://<random) string>.execute-api.us-east-2.amazonaws.com/test/predict

Added by Andrew Katoch

