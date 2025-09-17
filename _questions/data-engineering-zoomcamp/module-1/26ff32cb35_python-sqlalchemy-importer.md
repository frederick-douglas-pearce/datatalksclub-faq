---
id: 26ff32cb35
question: 'Python - SQLAlchemy - ImportError: cannot import name ''TypeAliasType''
  from ''typing_extensions''.'
sort_order: 1360
---

Error raised during the jupyter notebook’s cell execution:

from sqlalchemy import create_engine.

Solution: Version of Python module “typing_extensions” [>= 4.6.0](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md#release-460-may-22-2023). Can be updated by Conda or pip.

