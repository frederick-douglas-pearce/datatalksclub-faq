---
id: ba50d9e0bc
images:
- description: 'image #1'
  id: image_1
  path: images/mlops-zoomcamp/image_f76f8e53.png
question: Mage in Codespaces in a subfolder under mlops-zoomcamp repository
sort_order: 1320
---

Issue (1) you get errors like:

[+] Running 1/1

✘ magic-database Error too many requests: You have reached your pull rate limit. You may increase the limit by authenticating and upgra...                       1.2s

Error response from daemon: too many requests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading:[ [docker.com](https://www.docker.com/increase-rate-limi)t](https://www.docker.com/increase-rate-limit)

Issue (2) you get these popups with different % values but all saying space is in single digits.

<{IMAGE:image_1}>

Solution: It is not recommended to setup Mage as a subfolder of mlops-zoomcamp. See findings in this [thread](https://datatalks-club.slack.com/archives/C02R98X7DS9/p1716963258584219).

