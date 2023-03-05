import requests
import datetime
import pytz

DATABASE_ID = "YOUR_DATABASE_ID"
NOTION_API_KEY = "YOUR_NOTION_API_KEY"

today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
afterweek = today + datetime.timedelta(weeks=1)
today = format(today, '%Y-%m-%d')
afterweek = format(afterweek, '%Y-%m-%d')

url = "https://api.notion.com/v1/databases/" + DATABASE_ID + "/query"

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer " + NOTION_API_KEY
}

# データ取得
data = {
    "filter": {"and":
        [
            {"and":[{
                "property": "Due Date",
                "date": {"after": today}
            },
            {
                "property": "Due Date",
                "date": {"before": afterweek}
            }]},
            {"or":[{
                "property": "Status",
                "select": {"equals": "To Do"}
            },
            {
                "property": "Status",
                "select": {"equals": "In Progress"}
            }]}
        ]}
}

response = requests.post(url, headers=headers, json=data)
data = response.json()

print('1週間後までの予定をお知らせします。\n')
for info in reversed(data["results"]):
    print('Title: ', info['properties']['Task']['title'][0]['plain_text'])
    print('Status: ', info['properties']['Status']['select']['name'])
    print('DueDate: ', info['properties']['Due Date']['date']['start'])
    print('- - - - - - -')