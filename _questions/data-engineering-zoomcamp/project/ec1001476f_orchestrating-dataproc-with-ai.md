---
id: ec1001476f
question: Orchestrating DataProc with Airflow
sort_order: 4290
---

[https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html)

[https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_modules/airflow/providers/google/cloud/operators/dataproc.html](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_modules/airflow/providers/google/cloud/operators/dataproc.html)

Give the following roles to you service account:

DataProc Administrator

Service Account User (explanation [here](https://stackoverflow.com/questions/63941429/user-not-authorized-to-act-as-service-account-when-using-workload-identity))

Use DataprocSubmitPySparkJobOperator, DataprocDeleteClusterOperator and  DataprocCreateClusterOperator.

When using  DataprocSubmitPySparkJobOperator, do not forget to add:

dataproc_jars = ["gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.24.0.jar"]

Because DataProc does not already have the BigQuery Connector.

