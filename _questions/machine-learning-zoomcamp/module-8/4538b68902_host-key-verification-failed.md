---
id: 4538b68902
question: Host key verification failed.
sort_order: 2820
---

**Problem description:**

Getting an error using 

```bash
git clone git@github.com:alexeygrigorev/clothing-dataset-small.git
```

The error:

```
Cloning into 'clothing-dataset'...

Host key verification failed.

fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

**Solution description:**

When cloning the repo, you can also choose HTTPS, then it should work. This error occurs when your SSH key is not configured.

Use the following command:

```bash
git clone https://github.com/alexeygrigorev/clothing-dataset-small.git
```