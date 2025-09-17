---
id: c8d2668615
question: 'Fix warning Warning: Python 3.12 was not found on your system… Neither
  ''pyenv'' nor ''asdf'' could be found to install Python.'
sort_order: 2340
---

This is due to the fact the Pipfile is expecting Python 3.12, but the local container is probably running an older version (mainly the one shown in video [5.6 - Environment Management : Docker](https://www.youtube.com/watch?v=wAtyYZ6zvAs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=57), which is Python 3.8.12-slim. In order to fix this simply the `Dockerfile` to run an appropriate version, like shown below:

FROM python:3.12.7-slim

Both python versions (local version, shown in Pipfile and container version) must be congruent so as to guarantee compatibility.

(added by Jon Areas)

