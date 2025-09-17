---
id: cbaecfefaf
question: Data Type Error when running fact table
sort_order: 2940
---

If you encounter data type error on trip_type column, it may due to some nan values that isn’t null in bigquery.

Solution: try casting it to FLOAT datatype instead of NUMERIC

