---
course: data-engineering-zoomcamp
id: eab34fffe6
question: dbt job - Triggered by pull requests is disabled prerequisites when I try
  to create a new Continuous Integration job in dbt cloud.
section: 'Module 4: analytics engineering with dbt'
sort_order: 2530
---

Solution:

Check if you’re on the Developer Plan. As per the [prerequisites](https://docs.getdbt.com/docs/deploy/ci-jobs#prerequisites), you'll need to be enrolled in the Team Plan or Enterprise Plan to set up a CI Job in dbt Cloud.

So If you're on the Developer Plan, you'll need to upgrade to utilise CI Jobs.

Note from another user: I’m in the Team Plan (trial period) but the option is still disabled. What worked for me instead was this. It works for the Developer (free) plan.

