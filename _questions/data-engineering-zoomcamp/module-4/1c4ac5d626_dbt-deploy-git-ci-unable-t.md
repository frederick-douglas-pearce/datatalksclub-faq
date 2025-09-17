---
id: 1c4ac5d626
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_7800f401.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_8efd4f76.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_4e68416b.png
question: Dbt deploy + Git CI - Unable to configure Continuous Integration (CI) with
  Github
sort_order: 2790
---

If you’re trying to configure CI with Github and on the job’s options you can’t see Run on Pull Requests? on triggers, you have to reconnect with Github using native connection instead clone by SSH. Follow these steps:

On Profile Settings > Linked Accounts connect your Github account with dbt project allowing the permissions asked. More info at [https://docs.getdbt.com/docs/collaborate/git/connect-gith](https://docs.getdbt.com/docs/collaborate/git/connect-github)

<{IMAGE:image_1}>

Disconnect your current Github’s configuration from Account Settings > Projects (analytics) > Github connection. At the bottom left appears the button Disconnect, press it.

Once we have confirmed the change, we can configure it again. This time, choose Github and it will appear in all repositories which you have allowed to work with dbt. Select your repository and it’s ready.

<{IMAGE:image_2}>

Go to the Deploy > job configuration’s page and go down until Triggers and now you can see the option Run on Pull Requests:

<{IMAGE:image_3}>

