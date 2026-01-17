---
description: 為指定的 NeetCode 題目添加互動式演算法視覺化
---

# /add-visualizer Workflow

此 workflow 用於為 NeetCode 150 題目快速添加互動式視覺化。

## 使用方式

```
/add-visualizer [題目路徑或名稱]
```

**範例：**

```
/add-visualizer 02_Two_Pointers/05_Trapping_Rain_Water
```

---

## Workflow 步驟

### 1. 分析題目

- 讀取目標 Markdown 檔案 (`docs/[category]/[problem].md`)
- 理解演算法邏輯與資料結構
- 識別需要視覺化的關鍵狀態 (e.g., pointers, stack, dp table)

### 2. 生成視覺化檔案

- 複製模板 `docs/assets/visualizer/template.html`
- 重命名為 `[problem_name]_visualizer.html`
- 放置於與 Markdown 同層目錄

### 3. 實作演算法步驟

- 填寫 `generateSteps()` 函式
- 每個 step 需包含：
  - `barStates[]` 或其他視覺狀態
  - `stack[]` 或指標位置
  - `explanation: { title, text, formula? }`
  - `highlightLines[]` (對應程式碼行號)

### 4. 嵌入文件

- 在 Markdown 的 Section 3 (優化說明) 後添加：

```markdown
### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../[problem]_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../[problem]_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>
```

### 5. 驗證

- 執行 `mkdocs serve`
- 確認 iframe 載入正確
- 測試上一步/下一步功能

---

## 注意事項

> [!IMPORTANT]
>
> - iframe `src` 使用 `../` 前綴，因為 MkDocs 會將 `.md` 編譯為 `folder/index.html`
> - 視覺化 HTML 檔案需引用 `../assets/visualizer/style.css` 和 `../assets/visualizer/core.js`
