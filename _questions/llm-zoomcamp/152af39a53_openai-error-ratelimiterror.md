---
course: llm-zoomcamp
id: 152af39a53
images:
- description: 'image #1'
  id: image_1
  path: images/llm-zoomcamp/image_d8b5644f.png
question: '￼OpenAI: Error: RateLimitError: Error code: 429 -'
section: 'Module 1: Introduction'
sort_order: 150
---

RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: [https://platform.openai.com/docs/guides/error-codes/api-errors.](https://platform.openai.com/docs/guides/error-codes/api-errors.)', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}

The above errors are related to your OpenAI API account’s quota.There is no free usage of OpenAI’s API so you will be required to add funds using a credit card (see pay as you go in the OpenAI settings at [platform.openai.com](http://platform.openai.com)). Once added, re-run your python command and you should receive a successful return code.

Steps to resolve:

Add credits to your account [here](https://platform.openai.com/settings/organization/billing/overview) (min $5)

In chat.completions.create(model='gpt-4o', …) specify one of the available for you models:

<{IMAGE:image_1}>

You might need to recreate an API key after adding credits to your account and update it locally.

