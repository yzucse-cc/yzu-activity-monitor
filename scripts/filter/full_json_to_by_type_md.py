import json
import os
import to_md

with open('data/full/full.json', 'r', encoding='utf-8') as f:
    full = json.load(f)

nos = [] # non-online signup

for a in full:  # activity
    if a["類型"] == "線上報名":
        continue

    nos.append(a)

nos_md = "# 非線上報名\n\n" + to_md.json_to_md(nos)

by_type_path = os.path.join('data', 'by-type')
os.makedirs(by_type_path, exist_ok=True)       # make sure that the dir exists

with open(os.path.join(by_type_path, 'non-online-signup.md'), 'w+', encoding='utf-8') as f:
    f.write(nos_md)

print("by-type json->md done")
