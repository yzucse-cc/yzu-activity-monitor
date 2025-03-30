import os
import requests
from bs4 import BeautifulSoup
import json

url = "https://portalx.yzu.edu.tw/PortalSocialVB/FMain/PageActivityAll.aspx"

response = requests.get(url)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.content, "html.parser")

div_activity = soup.find(id="divPageActivityList")
if not div_activity:
    raise Exception("divPageActivityList not found")

table = div_activity.find("table", class_="table_1")
if not table:
    raise Exception("table_1 not found")

rows = table.find_all("tr")
header = [cell.get_text(separator=" ", strip=True) for cell in rows[0].find_all("td")] + ["ActID"]
rows = rows[1:]  # remove title row
activities = []

for row in rows:
    cells = row.find_all("td")
    row_data = [cell.get_text(separator=" ", strip=True) for cell in cells]

    if row_data:
        link = cells[2].find("a")
        if link:
            row_data.append(link.get("href").replace("../FPage/FirstToPage.aspx?PassPage=ActDetail&ActID=", ""))
        else:
            row_data.append("")

        activity = dict(zip(header, row_data))
        activities.append(activity)

json_path = os.path.join('data', 'full')
os.makedirs(json_path, exist_ok=True)       # make sure that the dir exists

with open(os.path.join(json_path, "full.json"), "w+", encoding="utf-8") as jsonfile:
    json.dump(activities, jsonfile, ensure_ascii=False, indent=4)

print("web->json done")
