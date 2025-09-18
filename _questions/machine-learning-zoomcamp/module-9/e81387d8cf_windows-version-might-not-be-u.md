---
id: e81387d8cf
question: 'Windows: Windows version might not be up-to-date'
sort_order: 3130
---

### Problem Description

When running the command:

```bash
$ docker build -t dino_dragon
```

you receive the following message:

```
Using default tag: latest
[2022-11-24T06:48:47.360149000Z][docker-credential-desktop][W] Windows version might not be up-to-date: The system cannot find the file specified.
error during connect: This error may indicate that the docker daemon is not running.: Post
```

### Solution Description

- Ensure that Docker is not stopped by a third-party program.