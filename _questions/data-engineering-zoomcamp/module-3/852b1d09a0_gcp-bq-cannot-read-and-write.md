---
id: 852b1d09a0
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_199a39eb.jpg
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_e2a4f6bc.jpg
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_9f3cd4ef.jpg
question: 'GCP BQ - Cannot read and write in different locations: source: asia-south2,
  destination: US'
sort_order: 2190
---

Solution: This problem arises if your gcs and bigquery storage is in different regions.

One potential way to solve it:

Go to your google cloud bucket and check the region in field named “Location”

<{IMAGE:image_1}>

Now in bigquery, click on three dot icon near your project name and select create dataset.

<{IMAGE:image_2}>

In region filed choose the same regions as you saw in your google cloud bucket

<{IMAGE:image_3}>

