---
id: 186389973c
images:
- description: 'image #1'
  id: image_1
  path: images/mlops-zoomcamp/image_ad7daf39.png
question: 'Connection in use: (''127.0.0.1'', 5000)'
sort_order: 810
---

You have something running on the 5000 port. You need to stop it.

Answer: On terminal in mac .

Run ps -A | grep gunicorn

Look for the number process id which is the 1st number after running the command

<{IMAGE:image_1}>

kill 13580

where 13580  represents the process number.

[Source](https://stackoverflow.com/questions/60531166/how-to-safely-shutdown-mlflow-ui#:~:text=I%20also%20met%20a%20similar,and%20kill%20%5BPID%5D%20manually.)

[warrie.warrieus@gmail.com](mailto:warrie.warrieus@gmail.com)

Or by executing the following command it will kill all the processes using port 5000:

>> sudo fuser -k 5000/tcp

Answered by Vaibhav Khandelwal

Just execute in the command below in the command line to kill the running port

->> kill -9 $(ps -A | grep python | awk '{print $1}')

Answered by kamaldeen (kamaldeen32@gmail.com)

Change to different port (5001 in this case)

>> mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

Answered by krishna (nellaikrishna@gmail.com)

