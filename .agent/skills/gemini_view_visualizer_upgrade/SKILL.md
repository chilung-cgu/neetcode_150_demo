# Gemini Dynamic View Visualizer Upgrade Skill

## 用途

將演算法視覺化器升級至「Gemini Dynamic View」精緻度等級。適用於 LeetCode 風格的演算法教學頁面。

## 🧠 核心原則 (Logic First)

在開始任何視覺化設計前，必須先通過以下邏輯驗證：

1.  **演算法正確性**：代碼是否能通過所有 Edge Cases (空輸入、單元素、重複元素)？
2.  **數據結構完整性**：
    - Heap: Min/Max 屬性、Complete Binary Tree 結構、0-indexed 公式。
    - Trie: Word End 標記、Prefix 共享。
    - Backtracking: State Space Tree、回溯狀態復原、剪枝條件。
3.  **步驟細粒度**：動畫步驟 (`steps`) 是否足夠細緻？(e.g., Heap Sift Down 不應只是一張快照，而是一系列比較與交換)。

## 🎨 設計規範 (Gemini Dynamic View)

1.  **色彩系統**
    - 背景: 深色漸層 `#1e293b` -> `#0f172a`
    - 主色: Google Blue `#3b82f6`, Purple `#a855f7`
    - 狀態: Success `#22c55e`, Warning `#fbbf24`, Error `#ef4444`
2.  **UI 組件**
    - **語言規範**：**必須使用繁體中文 (Traditional Chinese)** 撰寫所有介面文字、按鈕標籤與步驟說明。
    - **State Panel**: 顯示關鍵變數 (e.g., `k`, `maxVal`, `path`).
    - **Step Breakdown**: 左側藍條高亮，自然語言解釋當前步驟。
    - **Dual View**: 對於複雜結構 (Heap, Graph)，同時展示邏輯視圖 (Tree) 與存儲視圖 (Array/AdjList)。
3.  **程式碼同步 (Code Sync)**
    - 確保 HTML 中有 `<div id="codeDisplay">`
    - 在 `step` 物件中必須包含 `highlightLines` 屬性（數組）。
    - **嚴禁** 使用 `hl` 簡寫，除非在 `onStepChange` 中有明確的映射邏輯。建議直接使用 `highlightLines`。
4.  **動畫物理**
    - 使用 CSS Transitions 或 D3 Transitions。
    - 避免瞬間跳變，物體移動應有軌跡 (e.g., Sift Down 節點交換)。

## 🛠️ 實作模板 (Code Snippets)

### 1. D3 Binary Tree (適用於 Heap/Tree)

```javascript
const hierarchy = d3.hierarchy({ idx: 0 }, (d) => {
  const children = [];
  const left = 2 * d.idx + 1,
    right = 2 * d.idx + 2;
  if (left < size) children.push({ idx: left });
  if (right < size) children.push({ idx: right });
  return children.length ? children : null;
});
const treeLayout = d3.tree().size([width, height]);
const nodes = treeLayout(hierarchy).descendants();
// ... render nodes and links
```

### 2. State Snapshot Pattern

```javascript
function snapshot(msg, focusId, highlightLines) {
  return {
    // Deep copy critical structures
    structure: JSON.parse(JSON.stringify(currentStructure)),
    // UI State
    focusId: focusId,
    message: msg,
    highlightLines: highlightLines, // 確保名稱正確
  };
}
```

### 3. CSS for "Glowing" Nodes

```css
.node.current {
  fill: #fbbf24;
  filter: drop-shadow(0 0 8px rgba(251, 191, 36, 0.6));
  transition:
    fill 0.3s,
    filter 0.3s;
}
```

## 🚀 執行檢查清單 (Refinement)

- [ ] **介面中文化**：標題、按鈕、輸入框 placeholder、步驟說明、狀態標籤。
- [ ] **代碼高亮**：檢查 `steps` 中是否有名為 `highlightLines` 的屬性，且 ID 對應正確。
- [ ] **邏輯驗證**：演算法是否正確處理了 Edge Cases。
- [ ] **動畫流暢度**：是否使用了 CSS/D3 Transition。
