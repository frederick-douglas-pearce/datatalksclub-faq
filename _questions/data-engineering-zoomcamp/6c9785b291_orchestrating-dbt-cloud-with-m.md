---
course: data-engineering-zoomcamp
id: 6c9785b291
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_981381c8.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_ebc771b3.png
question: Orchestrating dbt cloud with Mage
section: Project
sort_order: 4300
---

You can trigger your dbt job in Mage pipeline. For this get your dbt cloud api key under settings/Api tokens/personal tokens. Add it safely to  your .env

For example

dbt_api_trigger=dbt_**

Navigate to job page and find api trigger  link

Then create a custom mage Python block with a simple http request like [here](https://github.com/Nogromi/ukraine-vaccinations/blob/master/2_mage/vaccination/custom/trigger_dbt_cloud.py)

<{IMAGE:image_1}>

<{IMAGE:image_2}>

from dotenv import load_dotenvfrom pathlib import Pathdotenv_path = Path('/home/src/.env')load_dotenv(dotenv_path=dotenv_path)dbt_api_trigger= os.getenv(dbt_api_trigger)

url = f"[cloud.getdbt.com](https://cloud.getdbt.com/api/v2/accounts/{dbt_account_id}/jobs/<job_id>/run/")

headers = {        "Authorization": f"Token {dbt_api_trigger}",        "Content-Type": "application/json" }

body = {        "cause": "Triggered via API"    }    response = requests.post(url, headers=headers, json=body)

voila! You triggered dbt job form your mage pipeline.

