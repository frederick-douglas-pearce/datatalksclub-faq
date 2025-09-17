---
id: 58586a16a6
question: DBT - Why changing the target schema to “marts” actually creates a schema
  named “dbt_marts” instead?
sort_order: 2840
---

It is a default behaviour of dbt to [append custom schema to initial schema](https://docs.getdbt.com/docs/build/custom-schemas#why-does-dbt-concatenate-the-custom-schema-to-the-target-schema). To override this behaviour simply create a macro named “generate_schema_name.sql”:

{% macro generate_schema_name(custom_schema_name, node) -%}

{%- set default_schema = target.schema -%}

{%- if custom_schema_name is none -%}

{{ default_schema }}

{%- else -%}

{{ custom_schema_name | trim }}

{%- endif -%}

{%- endmacro %}

Now you can override default custom schema in “dbt_project.yml”:

