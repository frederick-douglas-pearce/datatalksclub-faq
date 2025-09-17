---
id: ea9c96ab72
question: 'kafka.errors.NoBrokersAvailable: NoBrokersAvailable'
sort_order: 4020
---

If you have this error, it most likely that your kafka broker docker container is not working.

Use docker ps to confirm

Then in the docker compose yaml file folder, run docker compose up -d to start all the instances.

