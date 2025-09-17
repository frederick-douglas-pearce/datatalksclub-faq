---
id: 66ccbb7da0
question: How can I remove all Docker containers, images, and volumes, and builds
  from the terminal?
sort_order: 540
---

1. Delete all containers (including running ones):

```

docker rm -f

```

2. Remove all images:

```

docker rmi -f

```

3. Delete all volumes:

```

docker volume rm

```

