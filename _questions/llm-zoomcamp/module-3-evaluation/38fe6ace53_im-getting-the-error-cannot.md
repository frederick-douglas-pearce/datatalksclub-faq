---
id: 38fe6ace53
question: I'm getting the error “cannot import name 'VectorSearch' from 'minsearch'”
  even though I installed the latest version of minsearch. How can I fix it?
sort_order: 450
---

If you're working with Jupyter notebooks, make sure the kernel you're using has the correct version of minsearch. You can check the version in your kernel with: minsearch.__version__

You can also try installing the latest version directly from a notebook cell using:

%pip install -U minsearch

%pip is a Jupyter magic command that makes sure the package gets installed in the same environment your notebook kernel is using (unlike !pip, which might install it somewhere else).

Added by Marcelo Nieva

