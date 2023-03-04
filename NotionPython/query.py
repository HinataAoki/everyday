import requests
import datetime
import pytz

DATABASE_ID = "YOUR_DATABASE_ID"
NOTION_API_KEY = "YOUR_NOTION_API_KEY"

today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
date = format(today, '%Y-%m-%d')

url = "https://api.notion.com/v1/databases/" + DATABASE_ID + "/query"

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer " + NOTION_API_KEY
}

# データ取得
data = {
    "filter": {
        "property": "Due Date",
        "date": {
            "before": date,
            # "equals": date,
            # "after": date,
        }
    }
}

response = requests.post(url, headers=headers, json=data)
data = response.json()
print(data)