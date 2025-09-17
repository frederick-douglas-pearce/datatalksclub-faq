---
id: b024daf322
question: Which type of SQL is used in Spark? Postgres? MySQL? SQL Server?
sort_order: 3490
---

Actually Spark SQL is one independent “type” of SQL - Spark SQL.

The several SQL providers are very similar:

SELECT [attributes]

FROM [table]

WHERE [filter]

GROUP BY [grouping attributes]

HAVING [filtering the groups]

ORDER BY [attribute to order]

(INNER/FULL/LEFT/RIGHT) JOIN [table2]

ON [attributes table joining table2] (...)

What differs the most between several SQL providers are built-in functions.

For Built-in Spark SQL function check this link: [https://spark.apache.org/docs/latest/api/sql/index.html](https://spark.apache.org/docs/latest/api/sql/index.html)

Extra information on SPARK SQL :

[https://databricks.com/glossary/what-is-spark-sql#:~:text=Spark%20SQL%20is%20a%20Spark,on%20existing%20deployments%20and%20data](https://databricks.com/glossary/what-is-spark-sql#:~:text=Spark%20SQL%20is%20a%20Spark,on%20existing%20deployments%20and%20data).

