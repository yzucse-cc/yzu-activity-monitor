import json
import os
import to_md

with open('data/full/full.json', 'r', encoding='utf-8') as f:
    full = json.load(f)

cs = [] # for cs students
ds = [] # for dorm students
oc = [] # for oc students
ol = [] # other limitation
nl = [] # no limitation

for a in full:  # activity
    if "報名已截止" in a["報名日期"]:
        continue

    if "限資工系" in a["活動名稱"]:
        cs.append(a)
        continue

    if "限住宿生" in a["活動名稱"]:
        ds.append(a)
        continue

    if "僑生" in a["活動名稱"]:
        oc.append(a)
        continue

    if "限" in a["活動名稱"]:
        ol.append(a)
        continue

    nl.append(a)

cs_md = "# 限資工系\n\n" + to_md.json_to_md(cs)
ds_md = "# 限住宿生\n\n" + to_md.json_to_md(ds)
oc_md = "# 限僑生\n\n" + to_md.json_to_md(oc)
ol_md = "# 其他有「限」字\n\n" + to_md.json_to_md(ol)
nl_md = "# 其他無「限」字\n\n" + to_md.json_to_md(nl)

by_limitation_path = os.path.join('data', 'by-limitation')
os.makedirs(by_limitation_path, exist_ok=True)       # make sure that the dir exists

with open(os.path.join(by_limitation_path, 'for-cs-student.md'), 'w+', encoding='utf-8') as f:
    f.write(cs_md)

with open(os.path.join(by_limitation_path, 'for-dorm-student.md'), 'w+', encoding='utf-8') as f:
    f.write(ds_md)

with open(os.path.join(by_limitation_path, 'for-oc-student.md'), 'w+', encoding='utf-8') as f:
    f.write(oc_md)

with open(os.path.join(by_limitation_path, 'other-limitation.md'), 'w+', encoding='utf-8') as f:
    f.write(ol_md)

with open(os.path.join(by_limitation_path, 'no-limitation.md'), 'w+', encoding='utf-8') as f:
    f.write(nl_md)

print("by-limitation json->md done")
