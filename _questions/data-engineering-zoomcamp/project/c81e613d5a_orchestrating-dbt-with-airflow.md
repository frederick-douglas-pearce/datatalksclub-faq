---
id: c81e613d5a
question: Orchestrating dbt with Airflow
sort_order: 4280
---

The trial dbt account provides access to dbt API. Job will still be needed to be added manually. Airflow will run the job using a python operator calling the API. You will need to provide api key, job id, etc. (be careful not committing it to Github).

Detailed explanation here: [https://docs.getdbt.com/blog/dbt-airflow-spiritual-alignment](https://docs.getdbt.com/blog/dbt-airflow-spiritual-alignment)

Source code example here: [https://github.com/sungchun12/airflow-toolkit/blob/95d40ac76122de337e1b1cdc8eed35ba1c3051ed/dags/examples/dbt_cloud_example.py](https://github.com/sungchun12/airflow-toolkit/blob/95d40ac76122de337e1b1cdc8eed35ba1c3051ed/dags/examples/dbt_cloud_example.py)

