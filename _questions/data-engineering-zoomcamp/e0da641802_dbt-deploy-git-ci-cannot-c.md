---
course: data-engineering-zoomcamp
id: e0da641802
question: Dbt deploy + Git CI - cannot create CI checks job for deployment to Production.
  See more discussion in  [slack chat](https://datatalks-club.slack.com/archives/C01FABYF2RG/p1707972535660619)
section: 'Module 4: analytics engineering with dbt'
sort_order: 2780
---

Error:

Triggered by pull requests

This feature is only available for dbt repositories connected through dbt Cloud's native integration with Github, Gitlab, or Azure DevOps

Solution: Contrary to the , don’t use the Git Clone option. Use the Github one instead. Step-by-step guide to UN-LINK Git Clone and RE-LINK with Github in the next entry below [guide on DTC repo](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md)

![Image](images/data-engineering-zoomcamp/image_c35c101c.png)

