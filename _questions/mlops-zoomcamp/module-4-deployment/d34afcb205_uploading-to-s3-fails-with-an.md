---
id: d34afcb205
question: 'Uploading to s3 fails with "An error occurred (InvalidAccessKeyId) when
  calling the PutObject operation: The AWS Access Key Id you provided does not exist
  in our records."'
sort_order: 1720
---

Even though the upload works using aws cli and boto3 in Jupyter notebook.

Solution set the AWS_PROFILE environment variable (the default profile is called default)

