---
course: llm-zoomcamp
id: 8d23fe792f
question: 'Authentication: Safe and easy way to store and load API keys'
section: 'Module 1: Introduction'
sort_order: 240
---

You can store your different API keys in a yaml file that you will add in your .gitignore file. Be careful to never push or share this file.

For example, you can create a new file named “api_keys.yml” in your repository.

Then, do not forget to add it in your .gitignore file:

#api_keys

api_keys.yml

You can now fill your api_keys.yml file:

OPENAI_API_KEY: “sk[...]”

GROQ_API_KEY: “gqk_[...]”

Save your file.

You will need the pyyaml library to load your yaml file, so run this command in your terminal:

pip install pyyaml

Now, open your jupyter notebook.

You can load your yaml file and the associated keys with this code:

import yaml

# Open the file

with open('api_keys.yml', 'r') as file:

# Load the data from the file

data = yaml.safe_load(file)

# Get the API key (Groq example here)

groq_api_key = data['GROQ_API_KEY']

Now, you can easily replace the “api_key” value directly with the loaded values without loading your environment variables.

Added by Mélanie Fouesnard

