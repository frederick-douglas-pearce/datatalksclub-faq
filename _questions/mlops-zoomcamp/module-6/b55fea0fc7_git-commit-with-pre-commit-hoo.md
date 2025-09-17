---
id: b55fea0fc7
question: Git commit with pre-commit hook raises error ‘'PythonInfo' object has no
  attribute 'version_nodot'
sort_order: 2300
---

Problem description

git commit -m 'Updated xxxxxx'

[INFO] Initializing environment for [GitHub](https://github.com/pre-commit/pre-commit-hooks.)

[INFO] Installing environment for [GitHub](https://github.com/pre-commit/pre-commit-hooks.)

[INFO] Once installed this environment will be reused.

An unexpected error has occurred: CalledProcessError: command:

…

return code: 1

expected return code: 0

stdout:

AttributeError: 'PythonInfo' object has no attribute 'version_nodot'

Solution description

Clear app-data of the virtualenv

python -m virtualenv api -vvv --reset-app-data

Added by MarcosMJD

