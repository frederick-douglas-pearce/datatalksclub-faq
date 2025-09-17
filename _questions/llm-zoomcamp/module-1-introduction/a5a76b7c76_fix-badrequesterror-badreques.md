---
id: a5a76b7c76
question: 'Fix BadRequestError: BadRequestError(400, ''media_type_header_exception'',
  ''Invalid media-type value on headers [Content-Type, Accept]'', Accept version must
  be either version 8 or 7, but found 9. Accept=application/vnd.elasticsearch+json;
  compatible-with=9)'
sort_order: 200
---

When try to connect to the Elasticsearch server/node version  8.17.6 (as instructed for the Homework 1) running from with the Docker container with the python client elasticsearch version 9.x or more, we run into the BadRequestError mentioned above.

This happens because pip install elasticsearch install elasticsearch 9.x python client which runs into compatibility issues with the Elasticsearch 8.17.6. So we can use

pip install "elasticsearch>=8,<9"  for mitigation of the problem.

(Added by Siddhartha Gogoi)

