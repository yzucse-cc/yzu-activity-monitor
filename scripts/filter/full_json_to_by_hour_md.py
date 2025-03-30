import json
import os
import to_md

with open('data/full/full.json', 'r', encoding='utf-8') as f:
    full = json.load(f)

ah = [] # activity hours
ch = [] # course hours
dl = [] # diverse learning
nh = [] # no hour

for a in full:  # activity
    if "報名已截止" in a["報名日期"]:
        continue

    if a["服務學習"] == "無" and a["多元學習護照時數"] == "無":
        nh.append(a)
        continue

    if a["服務學習"] == "無":    # dl only
        dl.append(a)
        continue

    if "活動時數" in a["服務學習"]:
        ah.append(a)
        continue

    if "課程時數" in a["服務學習"]:
        ch.append(a)
        continue

ah_md = "# 活動時數\n\n" + to_md.json_to_md(ah)
ch_md = "# 課程時數\n\n" + to_md.json_to_md(ch)
dl_md = "# 多元學習護照時數\n\n" + to_md.json_to_md(dl)
nh_md = "# 無時數\n\n" + to_md.json_to_md(nh)

by_hour_path = os.path.join('data', 'by-hour')
os.makedirs(by_hour_path, exist_ok=True)       # make sure that the dir exists

with open(os.path.join(by_hour_path, 'activity-hours.md'), 'w+', encoding='utf-8') as f:
    f.write(ah_md)

with open(os.path.join(by_hour_path, 'course-hours.md'), 'w+', encoding='utf-8') as f:
    f.write(ch_md)

with open(os.path.join(by_hour_path, 'diverse-learning.md'), 'w+', encoding='utf-8') as f:
    f.write(dl_md)

with open(os.path.join(by_hour_path, 'no-hour.md'), 'w+', encoding='utf-8') as f:
    f.write(nh_md)

print("by-hour json->md done")
