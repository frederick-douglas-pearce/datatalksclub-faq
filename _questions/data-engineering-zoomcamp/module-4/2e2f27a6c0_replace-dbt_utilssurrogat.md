---
id: 2e2f27a6c0
question: 'Replace: {{ dbt_utils.surrogate_key([      field_a,      field_b,      field_c,     …,     field_z     ])
  }}'
sort_order: 2700
---

For this instead:{{ dbt_utils.generate_surrogate_key([      field_a,      field_b,      field_c,     …,     field_z]) }}

add a global variable in dbt_project.yml(...)

