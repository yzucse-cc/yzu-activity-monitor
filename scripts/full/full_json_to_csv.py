import csv
import os
import json

with open('data/full/full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if data:
    csv_path = os.path.join('data', 'full')
    os.makedirs(csv_path, exist_ok=True)  # make sure that the dir exists

    header = data[0].keys()
    with open(os.path.join(csv_path, "full.csv"), "w+", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

    print("json->csv done")

else:
    print("no data in json")
