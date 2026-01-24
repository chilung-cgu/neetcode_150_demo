# Antigravity Visualization Standards (v1.0)

為了確保在不同 Session 和 Quota 限制下，視覺化器的風格與品質保持一致，請遵循以下標準。

## 1. 技術棧 (Tech Stack)

- **Core**: Vanilla JS (ES6+)
- **Rendering**: **D3.js v7** (用於 SVG/Tree/Graph), HTML/CSS Grid (用於 Arrays/Matrix)
- **Logic Abstraction**: `core.js` (`AlgorithmVisualizer` class)
  - 負責：Step Management, Play/Pause, Speed Control, Theme Toggle.
  - 禁止：在個別 HTML 中重寫播放邏輯。
- **Styling**: `style.css` (共用樣式庫)

## 2. 視覺風格 (Visual Style)

### 色彩系統 (Color Palette)

使用 Tailwind CSS 風格的顏色變數：

- **Background**: Deep Slate Gradient (`linear-gradient(135deg, #1e293b, #0f172a)`)
- **Primary (Nodes/Bars)**: Google Blue (`#3b82f6`)
- **Accent (Active/Highlight)**: Amber (`#fbbf24`) with Drop Shadow
- **Success (Found/Leaf)**: Emerald (`#22c55e`)
- **Danger (Pruned/Invalid)**: Red (`#ef4444`)
- **Secondary (Visited/History)**: Slate (`#64748b`)
- **Text**: White / Light Slate (`#e2e8f0`, `#94a3b8`)

### 元件設計 (Components)

- **Nodes**: 圓形 SVG，半徑通常為 20px，帶有 `transition: all 0.3s`。
- **Edges (Links)**: 曲線 (`d3.linkVertical` 或 `d3.linkHorizontal`)，粗細 1.5px -> 2.5px (Active)。
- **Arrays**: Flexbox 或 Grid 佈局，每個元素為圓角矩形，索引標註在上方。
- **Matrix/Grid**: CSS Grid，單元格使用 `transform: scale(1.1)` 進行高亮動畫。

## 3. 實作模式 (Implementation Pattern)

### A. 數據驅動 (Data-Driven Steps)

不要直接在演算法邏輯中操作 DOM。應該生成「快照 (Snapshots)」。

```javascript
// ✅ 正確模式
const steps = [];
// ... algorithm logic ...
steps.push({
  tree: JSON.parse(JSON.stringify(treeStructure)), // Snapshot
  highlightLines: [1, 2],
  msg: "當前狀態說明",
});
// ...
viz.setSteps(steps);
```

### B. D3 渲染 Loop (Render Function)

使用 D3 的 Enter/Update/Exit 模式或 Merge 模式。

```javascript
function render(step) {
  const nodes = svg.selectAll(".node").data(step.nodes, d => d.id);

  // Enter & Update
  nodes.enter().append("g")...
       .merge(nodes)
       .transition().duration(300)
       .attr("transform", ...)

  // Exit
  nodes.exit().remove();
}
```

### C. 程式碼同步 (Code Sync)

必須提供 `codeStructure` 並在每一步驟中正確傳遞 `highlightLines` (Array of IDs)。禁止使用 `hl` 簡寫。

## 4. Quota 與 Session 管理策略

由於 Quota 限制導致任務分批：

1.  **Start w/ Standards**: 新 Session 開始時，Agent **必須** 先閱讀此文檔 (`visualizer_standards.md`)。
2.  **Reference Implementation**: 參考 `10_Backtracking` 或 `09_Heap` 中的實作作為 Gold Standard。
3.  **Refactoring**: 如果發現舊代碼 (06-07章) 風格不符，應建立專門的 Refactoring Task，而不是混合在其他任務中。

---

_Created by Antigravity, 2026-01-24_
