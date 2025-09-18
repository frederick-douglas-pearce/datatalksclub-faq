---
id: 46dbe4810d
question: 'Docker - Error during connect: In the default daemon configuration on Windows,
  the docker client must be run with elevated privileges to connect.: Post: "[//./pipe/docker_engine](http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/containers/create")
  : open //./pipe/docker_engine: The system cannot find the file specified'
sort_order: 580
---

To resolve this issue on Windows, follow these guidelines based on your version:

- **Windows 10 Pro / 11 Pro Users**: Ensure Hyper-V is enabled, as Docker can use it as a backend.
  1. Follow the [Enable Hyper-V Option on Windows 10 / 11](https://www.c-sharpcorner.com/article/install-and-configured-docker-desktop-in-windows-10/) tutorial.

- **Windows 10 Home / 11 Home Users**: The 'Home' version doesn't support Hyper-V, so use WSL2 (Windows Subsystem for Linux).
  1. Refer to [install WSL on Windows 11](https://pureinfotech.com/install-wsl-windows-11/) for detailed instructions.

If you encounter the "WslRegisterDistribution failed with error: 0x800701bc" error:

- Update the WSL2 Linux Kernel by following the guidelines at [GitHub: WSL Issue 5393](https://github.com/microsoft/WSL/issues/5393).