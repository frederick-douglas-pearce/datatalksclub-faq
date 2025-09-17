---
id: ecba2d4d27
question: Pipenv with Jupyter
sort_order: 1600
---

Problem description. How can we use Jupyter notebooks with the Pipenv environment?

Solution: Refer to this [stackoverflow question](https://stackoverflow.com/questions/47295871/is-there-a-way-to-use-pipenv-with-jupyter-notebook). Basically install jupyter and ipykernel using pipenv. And then register the kernel with `python -m ipykernel install --user --name=my-virtualenv-name` inside the Pipenv shell. If you are using Jupyter notebooks in VS Code, doing this will also add the virtual environment in the list of kernels.

Added by Ron Medina

