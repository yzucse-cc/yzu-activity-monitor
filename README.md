# 元智活動監視 YZU Activity Monitor

使用 Python 整理元智 Portal 上公開的[活動查詢列表](https://portalx.yzu.edu.tw/PortalSocialVB/FMain/PageActivityAll.aspx)。

資料由 GitHub Actions 自動更新於每天 18:00 (UTC+8)。

*GitHub Actions last updated*: <!--START_GA_LAST_UPDATED--> `2025-04-18 18:18:09 (UTC+8)` <!--END_GA_LAST_UPDATED-->

## 完整列表

提供三種格式，適用不同用途。

| 格式                            | 說明                       |
|-------------------------------|--------------------------|
| [Markdown](data/full/full.md) | 網頁好讀版，移除不重要的欄位，並依報名狀態分類。 |
| [csv](data/full/full.csv)     | 完整內容，在網頁上會顯示為表格          |
| [JSON](data/full/full.json)   | 完整內容，網路資料交換格式            |

## 篩選的列表

以關鍵字比對進行簡單篩選的列表，可能有誤判或漏網之魚，僅供參考。

每個篩選方式皆分為「報名進行中」、「報名尚未開始」與「其他」。

連結皆為 Markdown 網頁好讀版。

### 依時數

以是否有標註時數篩選。

[活動時數](data/by-hour/activity-hours.md) | [課程時數](data/by-hour/course-hours.md) | [多元學習護照時數](data/by-hour/diverse-learning.md) | [無標註時數](data/by-hour/no-hour.md)

### 依限制

以活動名稱包含關鍵字篩選。

[限資工系](data/by-limitation/for-cs-student.md) | [限住宿生](data/by-limitation/for-dorm-student.md) | [限僑生](data/by-limitation/for-oc-student.md) | [其他有「限」字](data/by-limitation/other-limitation.md) | [其他無「限」字](data/by-limitation/no-limitation.md)

### 依類型

由於幾乎都是線上報名，故將所有非線上報名合併。

[非線上報名](data/by-type/non-online-signup.md)
