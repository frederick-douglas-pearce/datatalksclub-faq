---
id: d039adfb76
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_07f863ec.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_df52218e.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_deaf91b1.png
- description: 'image #4'
  id: image_4
  path: images/data-engineering-zoomcamp/image_8584c5ce.png
question: 'Java Kafka: Tests are not picked up in VSCode'
sort_order: 4150
---

Situation: in VS Code, usually there will be a triangle icon next to each test. I couldn’t see it at first and had to do some fixes.

Solution:

([Source](https://stackoverflow.com/a/66527032))

VS Code

→ Explorer (first icon on the left navigation bar)

<{IMAGE:image_1}>

→ JAVA PROJECTS (bottom collapsable)

→  icon next in the rightmost position to JAVA PROJECTS

<{IMAGE:image_2}>

<{IMAGE:image_3}>

→  clean Workspace

→ Confirm by clicking Reload and Delete

Now you will be able to see the triangle icon next to each test like what you normally see in python tests.

E.g.:

<{IMAGE:image_4}>

You can also add classes and packages in this window instead of creating files in the project directory

