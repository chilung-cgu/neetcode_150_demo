# 全專案演算法視覺化架構計畫書 (Scalable Visualization Architecture Plan)

## 1. 可行性分析 (Feasibility Analysis)

### 1.1 技術相容性

- **MkDocs 相容性**：✅ 完全相容。MkDocs 預設會將 `docs/` 下的所有靜態檔案（如 `.html`, `.css`, `.js`）原封不動地複製到 `site/` 輸出目錄。
- **GitHub Pages 支援**：✅ 支援。GitHub Pages 僅是靜態網站託管，只要 HTML/JS/CSS 檔案存在即可運作，無需後端伺服器。
- **本地預覽**：✅ 支援。`mkdocs serve` 本身就是一個 Python 寫的輕量級 HTTP Server，完美解決了直接開啟 HTML 檔案可能遇到的 CORS 或模組載入問題。

### 1.2 規模化挑戰與解決方案

| 挑戰           | 解決方案                                                                                                          |
| -------------- | ----------------------------------------------------------------------------------------------------------------- |
| **程式碼重複** | 建立 **Shared Core Library** (`viz-core.js`, `viz-style.css`)，封裝通用邏輯（如柱狀圖繪製、堆疊操作、動畫控制）。 |
| **開發效率**   | 使用 **Antigravity Workflow** 與 **Skill** 自動生成每個題目的視覺化模板。                                         |
| **樣式衝突**   | 採用 `iframe` 嵌入策略，確保視覺化工具的 CSS 不會與 MkDocs 主題（Material）產生衝突，且易於 RWD 調整。            |

---

## 2. 系統架構設計 (System Architecture)

### 2.1 檔案結構建議

```
docs/
├── assets/
│   ├── css/
│   │   └── visualizer.css      # 共用樣式 (配色、RWD、控制面板)
│   └── js/
│       └── visualizer-core.js  # 核心引擎 (動畫佇列、圖表渲染、步驟控制)
├── 01_Arrays_and_Hashing/
│   └── ...
├── 04_Stack/
│   ├── 07_Largest_Rectangle_in_Histogram.md
│   └── scripts/                # 建議：將 JS 邏輯分離
│       └── leetcode_84.js      # 該題特定的演算法步驟邏輯
└── ...
```

_備註：為保持簡易性，初期可將特定題目邏輯直接寫在該題的 `.html` 檔案中，待複雜度提升再分離 JS。_

### 2.2 Shared Core Library 功能

- **State Management**: 管理 `steps` 陣列、目前 `stepIndex`、播放/暫停狀態。
- **Animation Loop**: 處理自動播放的計時器與速度控制。
- **UI Renderers**:
  - `renderBarChart(data, highlights)`
  - `renderStack(stack)`
  - `renderCodeBlock(lines, activeLine)`
  - `renderControls()` (自動生成 上一步/下一步/播放 按鈕)

---

## 3. 開發流程 (Development Workflow)

我們將引入 Antigravity **Slash Command** 來標準化開發流程：

### 3.1 新增 Visualizer Workflow (`/add-visualizer`)

當使用者輸入 `/add-visualizer` 並指定題目時，Agent 將執行以下步驟：

1.  **分析題目**：讀取 Markdown 與程式碼，理解演算法邏輯。
2.  **生成模板**：呼叫 `generate-viz-template` Skill，在該題目同級目錄下產生 `[題目名稱]_visualizer.html`。
3.  **實作邏輯**：填寫演算法的 `generateSteps()` 函式，將邏輯轉換為視覺化步驟。
4.  **嵌入文件**：自動修改 markdown，插入 `iframe` 程式碼。

### 3.2 核心 Skill (`visualize_algo`)

建立專屬 Skill 資料夾 `.agent/skills/visualize_algo/`，包含：

- `template.html`: 標準化的 HTML 骨架。
- `generator.py`: 用於生成特定題目邏輯的 Python 腳本。

---

## 4. 實作路徑 (Implementation Roadmap)

### Phase 1: 基礎建設 (Foundation)

- [ ] 提取 LeetCode 84 的共用樣式至 `docs/stylesheets/visualizer.css`。
- [ ] 提取共用控制邏輯至 `docs/javascripts/visualizer-core.js`。
- [ ] 重構 LeetCode 84 v2，改用上述共用資源，驗證架構可行性。

### Phase 2: 自動化工具 (Automation)

- [ ] 建立 `/add-visualizer` workflow 文件。
- [ ] 實作 `visualize_algo` skill 模板。

### Phase 3: 規模化 (Scaling)

- [ ] 選擇具代表性的題目（如 "Trapping Rain Water", "Min Stack"）進行試產。
- [ ] 逐步推廣至其他章節。

---

## 5. 結論

此方案無需額外伺服器資源，完全依賴現有的 MkDocs 建置流程。透過模組化 (Shared Libs) 與自動化 (Agent Skills)，可以高效地將 150 題全部視覺化，且保證風格一致、易於維護。
