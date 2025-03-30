import json
import os

act_url_prefix = 'https://portalx.yzu.edu.tw/PortalSocialVB/FPage/PageActivityDetail.aspx?Menu=Act&ActID='

def json_to_markdown_table(data):
    if not data:
        return "No data available"

    # 取得所有鍵作為表頭
    headers = [key for key in data[0].keys() if key not in ['類型', 'SDGs', 'UCAN共通職能', 'ActID']]

    # 建立 Markdown 表頭
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "|" + "|".join(["----"] * len(headers)) + "|\n"

    # 填充表格內容
    for item in data:
        row = []
        for key in headers:
            if key == "活動名稱":
                row.append(f"[{item[key]}]({act_url_prefix}{item['ActID']})")
            else:
                row.append(str(item[key]))
        markdown += "| " + " | ".join(row) + " |\n"

    return markdown


with open('data/full/full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ongoing = []
not_yet = []
others = []

for item in data:
    if "線上報名" in item['報名日期']:
        ongoing.append(item)
        continue

    if "報名尚未開始" in item['報名日期']:
        not_yet.append(item)
        continue

    others.append(item)

# 轉換為 Markdown 表格
md_table_ongoing = json_to_markdown_table(ongoing)
md_table_not_yet = json_to_markdown_table(not_yet)
md_table_others = json_to_markdown_table(others)

jump_to = '快速跳轉： [報名進行中](#報名進行中) | [報名尚未開始](#報名尚未開始) | [其他](#其他)'

markdown_content = f"""
# 完整列表

{jump_to}

# 報名進行中

{md_table_ongoing}

{jump_to}

# 報名尚未開始

{md_table_not_yet}

{jump_to}

# 其他

{md_table_others}

{jump_to}
"""

md_path = os.path.join('data', 'full')
os.makedirs(md_path, exist_ok=True)  # make sure that the dir exists

with open(os.path.join(md_path, "full.md"), 'w+', encoding='utf-8') as f:
    f.write(markdown_content)

print("json->md done")
