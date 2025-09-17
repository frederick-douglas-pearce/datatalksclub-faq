---
course: data-engineering-zoomcamp
id: e532c9677e
question: 'Docker-Compose - cannot execute binary file: Exec format error'
section: 'Module 1: Docker and Terraform'
sort_order: 990
---

This error means the docker-compose executable can’t be opened in current OS. Make sure the file you download from github matches your system environment.

As of 2025/1/17, docker-compose ([v2.32.4](https://github.com/docker/compose/releases/tag/v2.32.4)) [docker-compose-linux-aarch64](https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-linux-aarch64) does not work, try v2.32.3 [docker-compose-linux-x86_64](https://github.com/docker/compose/releases/download/v2.32.3/docker-compose-linux-x86_64)

