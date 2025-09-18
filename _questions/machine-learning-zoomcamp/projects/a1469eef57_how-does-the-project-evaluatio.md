---
id: a1469eef57
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_5d15610e.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_ca88b4f9.png
question: How does the project evaluation work for you as a peer reviewer?
sort_order: 3810
---

The link provided contains a list of all submitted projects to be evaluated. Specifically, you are to review 3 assigned peer projects. In the spreadsheet, there are 3 hash values of your assigned peer projects. You need to derive the hash value of your email address and find the value on the spreadsheet under the `reviewer_hash` heading.

To calculate your hash value, run the following Python code:

```python
from hashlib import sha1

def compute_hash(email):
    return sha1(email.lower().encode('utf-8')).hexdigest()

# Example usage - enter your email below (Example1@gmail.com)
email = "Example1@gmail.com"
hashed_email = compute_hash(email)

print("Original Email:", email)
print("Hashed Email (SHA-1):", hashed_email)
```

Edit the above code to replace `Example1@gmail.com` with your email address, then store and run the Python code from your terminal. See below as the Hashed Email (SHA-1) value:

<{IMAGE:image_1}>

Then go to the link provided: [Google Spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vR-7RRtq7AMx5OzI-tDbkzsbxNLm-NvFOP5OfJmhCek9oYcDx5jzxtZW2ZqWvBqc395UZpHBv1of9R1/pubhtml?gid=876309294&single=true)

1. Copy the "Hashed Email (SHA-1): bd9770be022dede87419068aa1acd7a2ab441675" value.
2. Search for 3 identical entries.
3. There you should see your peer projects to be reviewed.

<{IMAGE:image_2}>
