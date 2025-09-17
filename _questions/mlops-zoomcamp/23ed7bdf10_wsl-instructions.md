---
course: mlops-zoomcamp
id: 23ed7bdf10
question: WSL instructions
section: 'Module 1: Introduction'
sort_order: 310
---

If you wish to use WSL on your windows machine, here are the setup instructions:

Command: Sudo apt install wget

Get [Anaconda download address here](https://www.anaconda.com/download#downloads). wget <download address>

[Turn on Docker Desktop W](https://docs.docker.com/desktop/windows/wsl/#turn-on-docker-desktop-wsl-2)[Free Download | Anaconda](https://www.anaconda.com/download#downloads)[SL2](https://docs.docker.com/desktop/windows/wsl/#turn-on-docker-desktop-wsl-2)

Command: git clone <github repository address>

[VSCODE on WSL](https://code.visualstudio.com/docs/remote/wsl)

Jupyter: pip3 install jupyter

Added by Gregory Morris ([gwm1980@gmail.com](mailto:gwm1980@gmail.com))

All in all softwares at one shop:

You can use anaconda which has all built in services like pycharm, jupyter

Added by Khaja Zaffer ([khajazaffer@aln.iseg.ulisboa.pt](mailto:khajazaffer@aln.iseg.ulisboa.pt))

Alternatively, you can download miniforge, which is a more lightweight open-source version of conda, which doesn’t rely on the proprietary Anaconda repository and allows you to use mamba, as a default package manager, which greatly improves environment solving speed.

For a clear, step-by-step guide to installing miniforge, the Texas Tech University High Performance Computing Center has an excellent comprehensive guide:

[Installing Miniforge3 Guide by TTU HPCC](https://www.depts.ttu.edu/hpcc/userguides/application_guides/Miniforge.php)

Added by Jon Areas ([areasjx@gmail.com](mailto:areasjx@gmail.com))

For windows “wsl --install” in Powershell

Added by Vadim Surin ([vdmsurin@gmai.com](mailto:vdmsurin@gmai.com))

If python is still showing as 3.10 after installing anaconda with Python 3.9, try running ‘source .bashrc’ from ${HOME} folder, for any reason if its still not working, add ‘export PATH=”<anaconda install path>/bin:$PATH”’

