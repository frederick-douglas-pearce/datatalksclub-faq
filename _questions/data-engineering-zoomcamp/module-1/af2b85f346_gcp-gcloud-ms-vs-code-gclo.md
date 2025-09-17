---
id: af2b85f346
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_df9492cb.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_6b01ae01.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_bc858c4b.png
- description: 'image #4'
  id: image_4
  path: images/data-engineering-zoomcamp/image_a231d54c.png
- description: 'image #5'
  id: image_5
  path: images/data-engineering-zoomcamp/image_2f5bf08c.png
question: GCP gcloud + MS VS Code - gcloud auth hangs
sort_order: 1600
---

If you are using MS VS Code and running gcloud in WSL2, when you first try to login to gcp via the gcloud cli gcloud auth application-default login, you will see a message like this, and nothing will happen

<{IMAGE:image_1}>

And there might be a prompt to ask if you want to open it via browser, if you click on it, it will open up a page with error message

<{IMAGE:image_2}>

Solution : you should instead hover on the long link, and ctrl + click the long linkClick configure Trusted Domains herePopup will appear, pick first or second entry

<{IMAGE:image_3}>

<{IMAGE:image_4}>

<{IMAGE:image_5}>

Next time you gcloud auth, the login page should popup via default browser without issues

