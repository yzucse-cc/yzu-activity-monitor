act_url_prefix = 'https://portalx.yzu.edu.tw/PortalSocialVB/FPage/PageActivityDetail.aspx?Menu=Act&ActID='

def _json_to_md_table(data):
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


def json_to_md(data):
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
    md_table_ongoing = _json_to_md_table(ongoing)
    md_table_not_yet = _json_to_md_table(not_yet)
    md_table_others = _json_to_md_table(others)

    jump_to = '快速跳轉： [報名進行中](#報名進行中) | [報名尚未開始](#報名尚未開始) | [其他](#其他)'

    return f"""
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