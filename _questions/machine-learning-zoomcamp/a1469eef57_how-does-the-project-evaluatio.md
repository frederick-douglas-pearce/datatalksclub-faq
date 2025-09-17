---
course: machine-learning-zoomcamp
id: a1469eef57
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_5d15610e.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_ca88b4f9.png
question: How does the project evaluation work for you as a peer reviewer?
section: Projects (Midterm and Capstone)
sort_order: 3810
---

I am not sure how the project evaluate assignment works? Where do I find this? I have access to all the capstone 2 project, perhaps, I can randomly pick any to review.

Answer:

The link provided for example (2023/Capstone link ): [https://docs.google.com/forms/d/e/1FAIpQLSdgoepohpgbM4MWTAHWuXa6r3NXKnxKcg4NDOm0bElAdXdnnA/viewform](https://docs.google.com/forms/d/e/1FAIpQLSdgoepohpgbM4MWTAHWuXa6r3NXKnxKcg4NDOm0bElAdXdnnA/viewform) contains a list of all submitted projects to be evaluated. More specific, you are to review 3 assigned peer projects. In the spreadsheet are 3 hash values of your assigned peer projects. However, you need to derive the your hash value of your email address and find the value on the spreadsheet under the (reviewer_hash) heading.

To calculate your hash value run the python code below:

from hashlib import sha1

def compute_hash(email):

return sha1(email.lower().encode('utf-8')).hexdigest()

# Example usage **** enter your email below (Example1@gmail.com)****

email = "Example1@gmail.com"

hashed_email = compute_hash(email)

print("Original Email:", email)

print("Hashed Email (SHA-1):", hashed_email)

Edit the above code to replace [Example1@gmail.com](mailto:Example1@gmail.com) as your email address

Store and run the above python code from your terminal. See below as the Hashed Email (SHA-1) value

<{IMAGE:image_1}>

You then go to the link: [https://docs.google.com/spreadsheets/d/e/2PACX-1vR-7RRtq7AMx5OzI-tDbkzsbxNLm-NvFOP5OfJmhCek9oYcDx5jzxtZW2ZqWvBqc395UZpHBv1of9R1/pubhtml?gid=876309294&single=true](https://docs.google.com/spreadsheets/d/e/2PACX-1vR-7RRtq7AMx5OzI-tDbkzsbxNLm-NvFOP5OfJmhCek9oYcDx5jzxtZW2ZqWvBqc395UZpHBv1of9R1/pubhtml?gid=876309294&single=true)

Lastly, copy the “Hashed Email (SHA-1): bd9770be022dede87419068aa1acd7a2ab441675” value and search for 3 identical entries. There you should see your peer project to be reviewed.

<{IMAGE:image_2}>

By Emmanuel Ayeni

