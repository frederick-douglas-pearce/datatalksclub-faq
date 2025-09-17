---
course: data-engineering-zoomcamp
id: '3549528659'
question: Docker - Docker won't start or is stuck in settings (Windows 10 / 11)
section: 'Module 1: Docker and Terraform'
sort_order: 620
---

First off, make sure you're running the latest version of Docker for Windows, which you can download from [here](https://docs.docker.com/desktop/install/windows-install/). Sometimes using the menu to "Upgrade" doesn't work (which is another clear indicator for you to uninstall, and reinstall with the latest version)

If docker is stuck on starting, first try to switch containers by right clicking the [docker symbol](https://imgur.com/vsVUAzK) from the running programs and switch the containers from windows to linux or vice versa

[Windows 10 / 11 Pro Edition] The Pro Edition of Windows can run Docker either by using Hyper-V or WSL2 as its backend (Docker Engine)

In order to use Hyper-V as its back-end, you MUST have it enabled first, which you can do by following the tutorial: [Enable Hyper-V Option on Windows 10 / 11](https://www.c-sharpcorner.com/article/install-and-configured-docker-desktop-in-windows-10/)

If you opt-in for WSL2, you can follow the same steps as detailed in the [tutorial here](https://pureinfotech.com/install-wsl-windows-11/)

