# My Favourite Place — Hong Kong Disneyland 我最鍾意嘅地方

HTML Final Project 功課網站：一個關於「我最鍾意嘅地方 — 香港迪士尼樂園」的四頁網站。
A four-page school website about my favourite place, Hong Kong Disneyland.

---

## 1. 檔案清單 Files

| 檔案 File | 用途 What it is | 交功課？Submitted? |
|---|---|---|
| `index.html` | 首頁（網站導航）Home page / navigation | ✅ 要 Yes |
| `intro.html` | 樂園簡介（歷史、基本資料）About the park | ✅ 要 Yes |
| `attractions.html` | 八個主題園區、遊樂設施、表演 Attractions | ✅ 要 Yes |
| `visit.html` | 交通、開放時間、門票、貼士 Visiting tips | ✅ 要 Yes |
| `css/style.css` | 全站共用樣式表 Shared style sheet | ✅ 要 Yes |
| `images/*.svg` | 四張自己畫的插圖（城堡、小火車、旋轉木馬、煙花）4 hand-drawn illustrations | ✅ 要 Yes |
| `check_page.py` | 交功課前自我檢查的程式 Structure checker | ❌ 唔交 Not submitted |
| `README.md` | 這個說明檔 This file | ❌ 唔交 Not submitted |

交功課時，把上面標 ✅ 的檔案（4 個 `.html`、`css/` 和 `images/` 整個資料夾）壓縮成
一個 `.ZIP` 檔上載。To submit: zip the ✅ files only.

---

## 2. 怎樣開啟 How to open

雙擊 `index.html` 就可以用瀏覽器開啟（唔需要上網、唔需要安裝任何東西）。
Double-click `index.html`. No internet and no installation needed — the whole site works offline.

---

## 3. 交功課前一定要做的個人化 To do before submitting

1. **填上姓名、班別和日期**：四個網頁的最底（頁尾）都有 `姓名 Name：____　班別 Class：____　日期 Date：____`，
   請用文字編輯器（例如 VS Code、Notepad++、瀏覽器開發者工具）直接改，填上自己的資料。
2. **把「我」的經歷改成自己的**：`index.html` 和 `intro.html` 裡的個人段落（例如「我第一次去…」）只是示範，
   請改成你自己真實的經歷，這樣老師問起你都答得出來。
3. **`visit.html` 的門票價錢和開放時間**：資料是 2026年10月27日 在官網看到的，如果你遲些才交，
   可以先上官網核對一次再更新，並把「瀏覽日期」改成你查看的日期。

---

## 4. 對照題目要求 What the project asks for

題目要求：至少三個網頁（`index.html` 為導航、`intro.html` 為簡介）、包含學過的所有 HTML 元素。

| 題目要求的元素 | 在這個網站哪裡用到 Where it is used |
|---|---|
| `<h1>` – `<h6>` 六級標題 | `intro.html`「樂園的歷史」一節由 `<h1>` 到 `<h6>` 順序示範；每頁都有 `<h1>`–`<h3>` |
| `<p>` 段落 | 四頁都有 |
| `<b>` 粗體 | 四頁都有（關鍵字用粗體） |
| `<i>`、`<u>`、`<small>`、`<sup>` | `index.html` 斜體句子、頁尾填空線；註腳上標在 `intro.html` |
| `<img>` 圖片 | `index.html` 城堡、`intro.html` 小火車、`attractions.html` 旋轉木馬＋煙花、`visit.html` 小火車 |
| `<a href="...">` 連結 | 每頁的導覽列（連去其他三頁）、`index.html` 連去 `visit.html#sources`、三頁的「資料來源」外連 |
| `<ul>`、`<ol>`、`<li>` 清單 | 四頁都有；`index.html` 網站導覽〈無序〉、`attractions.html` 我的最愛〈有序〉 |
| `<table>`、`<tr>`、`<th>`、`<td>` 表格 | 四頁都有（快速資料、基本資料、園區一覽、表演、門票、出發前檢查） |
| `style` 樣式 | `css/style.css` 由每頁 `<link>` 載入；`visit.html` 另有一個 `<style>` 區塊；`index.html` 有 `style="text-align:center"` 行內樣式 |
| 其他 | `<header>`、`<nav>`、`<main>`、`<section>`、`<footer>`、`<hr>`、`<br>`、`<meta charset="UTF-8">` |

---

## 5. 交功課前自我檢查 Self-check

在 terminal 執行（需要 Python 3，只用標準庫）：

```
python3 check_page.py
```

它會檢查：四個網頁是否存在、所有要求的標籤是否用過、圖片檔案是否存在、內部連結是否有效、
**有沒有用到 JavaScript**、有沒有連去任何外部資源（完全離線都用得）。
全部 ✔ 就代表可以交。

---

## 6. 版權與資料來源 Copyright and sources

- 網站內的四張插圖都是**自己用 SVG 畫的**，沒有使用迪士尼官方的標誌、角色圖案或相片，
  以免侵犯版權。（圖片檔內的 `alt` 文字和插圖說明都已註明。）
- 文字資料來源（瀏覽日期：2026年10月27日）：
  - 香港迪士尼樂園官方網站 — 首頁 <https://www.hongkongdisneyland.com/zh-hk/>
  - 官方網站 — 遊樂設施 <https://www.hongkongdisneyland.com/zh-hk/attractions/theme-park/>
  - 官方網站 — 奇妙夢想城堡 <https://www.hongkongdisneyland.com/zh-hk/attractions/castle-magical-dreams/>
  - 官方網站 — 樂園時間表 <https://www.hongkongdisneyland.com/calendars/>
  - 官方網站 — 門票 <https://www.hongkongdisneyland.com/zh-hk/tickets/>
  - 維基百科 —「香港迪士尼樂園」<https://zh.wikipedia.org/wiki/香港迪士尼樂園>