---
course: llm-zoomcamp
id: fe87f03913
question: Elasticsearch version error
section: 'Workshops: Agents'
sort_order: 810
---

Error : elasticsearch.BadRequestError: BadRequestError(400, 'media_type_header_exception', 'Invalid media-type value on headers [Content-Type, Accept]', Accept version must be either version 8 or 7, but found 9. Accept=application/vnd.elasticsearch+json; compatible-with=9)

Fix :

pip uninstall elasticsearch

pip install elasticsearch==8.10.0

