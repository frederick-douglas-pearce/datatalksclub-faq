---
course: data-engineering-zoomcamp
id: e839b64165
question: How to run a dbt-core project as an Airflow Task Group on Google Cloud Composer
  using a service account JSON key
section: Project
sort_order: 4330
---

[Install](https://cloud.google.com/composer/docs/composer-2/install-python-dependencies#install_custom_packages_in_a_environment) the [astronomer-cosmos](https://github.com/astronomer/astronomer-cosmos) package as a dependency. (see Terraform [example](https://github.com/wndrlxx/ca-trademarks-data-pipeline/blob/4e6a0e757495a99e01ff6c8b981a23d6dc421046/terraform/main.tf#L100)).

Make a new folder, dbt/, inside the dags/ folder of your Composer GCP bucket and copy paste your dbt-core project there. (see [example](https://github.com/wndrlxx/ca-trademarks-data-pipeline/tree/4e6a0e757495a99e01ff6c8b981a23d6dc421046/dags/dbt/ca_trademarks_dp))

Ensure your profiles.yml is configured to authenticate with a service account key. (see BigQuery [example](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup#service-account-file))

Create a new DAG using the DbtTaskGroup class and a ProfileConfig specifying a profiles_yml_filepath that points to the location of your JSON key file. (see [example](https://github.com/wndrlxx/ca-trademarks-data-pipeline/blob/4e6a0e757495a99e01ff6c8b981a23d6dc421046/dags/6_dbt_cosmos_task_group.py#L47))

Your dbt lineage graph should now appear as tasks inside a task group like this:

![Image](images/data-engineering-zoomcamp/image_bd4861e1.png)

