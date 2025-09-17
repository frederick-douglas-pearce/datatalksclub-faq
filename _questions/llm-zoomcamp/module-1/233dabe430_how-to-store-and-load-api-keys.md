---
id: 233dabe430
question: How to store and load API keys using .env file
sort_order: 250
---

Store the API key in a .env file, then

import os

from dotenv import load_dotenv

load_dotenv(os.path.abspath("<path-to-.env>"))

os.getenv("API_KEY_abc")

Make sure to add the .env file in the .gitignore.

