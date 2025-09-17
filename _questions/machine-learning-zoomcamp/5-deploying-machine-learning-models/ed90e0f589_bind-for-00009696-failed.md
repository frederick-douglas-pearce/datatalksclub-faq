---
id: ed90e0f589
question: 'Bind for 0.0.0.0:9696 failed: port is already allocated'
sort_order: 2060
---

I was getting the below error when I rebuilt the docker image although the port was not allocated, and it was working fine.

Error message:

Error response from daemon: driver failed programming external connectivity on endpoint beautiful_tharp (875be95c7027cebb853a62fc4463d46e23df99e0175be73641269c3d180f7796): Bind for 0.0.0.0:9696 failed: port is already allocated.

Solution description

Issue has been resolved running the following command:

docker kill $(docker ps -q)

[https://github.com/docker/for-win/issues/2722](https://github.com/docker/for-win/issues/2722)

Asia Saeed

