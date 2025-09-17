---
id: e8df9f0d12
question: 'When trying to run a streamlit app using docker-compose, I get: Error response
  from daemon: failed to create task for container: failed to create shim task: OCI
  runtime create failed: runc create failed: unable to start container process: exec:
  "streamlit": executable file not found in $PATH: unknown. The app runs fine outside
  of docker-compose'
sort_order: 560
---

Make sure to create a Dockerfile and run ‘docker-compose up –build’ when adding streamlit to docker-compose

