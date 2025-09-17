---
id: 7fa713d6c7
question: module is not available (Can't connect to HTTPS URL)
sort_order: 1580
---

First check if SSL module configured with following command:

Python -m sslIf the output of this is empty there is no problem with SSL configuration.Then you should upgrade your pipenv package in your current environment to resolve the problem.

Added by Kenan Arslanbay

