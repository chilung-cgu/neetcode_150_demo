---
description: 標準化演算法視覺化器開發流程，確保包含邏輯解釋與高品質 D3.js 視覺效果
---

# Algorithm Visualizer Standard SKILL

此 Skill 定義了專案中所有演算法視覺化器的最高開發標準 (Gemini Dynamic View Level)。所有新的視覺化器或升級都**必須**嚴格遵守此規範。

目標：達到與 Gemini Dynamic View 同等級的互動性與教育深度，拒絕平庸的 "亮燈式" 視覺化。

## 1. 核心架構 (Mandatory)

每個視覺化器必須使用專案統一的 `AlgorithmVisualizer` class (`core.js`)。

### 1.1 Step Object 必備欄位 (Strict)

每個動畫步驟 (Step Object) **必須** 包含以下欄位，這不是選項，是強制要求：

```javascript
{
    // [Required] 狀態數據 (State)
    // 包含足夠重建畫面的所有數據 (nodes, links, pointers, dpTable, stack, indices 等)
    // 盡量使用 Immutable pattern (copy arrays/objects) 確保回放正確
    nodes: [...],
    pointers: { left: 0, right: 5 },

    // [Required] 操作描述 (UI 顯示)
    // 簡短描述當前發生了什麼 (What)
    msg: "比較 nums[0] 與 nums[5]",

    // [Required] 程式碼高亮
    // 精確對應右側 C++ 代码的行號 (0-based)
    highlightLines: [1, 2, 3],

    // [CRITICAL] 邏輯解釋卡片數據 (Logic Card)
    // 這是教育核心。必須解釋 "Why" (為什麼這麼做) 而不僅是 "What"。
    // 必須使用自然語言詳細解釋邏輯。
    explanation: {
        title: "標題 (例如：發現重複值 / DP 狀態轉移)",
        text: "詳細說明。例如：'因為 nums[left] < nums[right]，根據貪婪邏輯，移動較小的那邊可能獲得更大面積...'",
        formula: "數學公式 (例如：Area = (5 - 0) * min(2, 8))"
    }
}
```

### 1.2 UI 佈局標準 (DOM Structure)

所有 HTML 必須遵循以下 DOM 結構，確保佈局一致且 RWD 友善：

```html
<div class="main-layout">
  <div class="canvas-area">
    <!-- 視覺化主卡片 -->
    <div class="viz-card">
      <div class="viz-title">題目名稱</div>

      <!-- 1. 自訂輸入區 (必須存在) -->
      <div class="custom-input-section">
        <div class="input-row">
          <label>Input:</label>
          <input ... />
          <button onclick="runVisualizer()">Run</button>
        </div>
        <!-- 預設範例按鈕 -->
        <div class="examples">...</div>
      </div>

      <!-- 2. 主要繪圖區 (D3 Canvas) -->
      <!-- 必須有足夠高度 (min-height: 400px+)，並使用 SVG viewBox 實現響應式 -->
      <div class="visualization-area">
        <svg id="viz-svg"></svg>
        <!-- 必須包含 Legend (圖例) -->
        <div class="legend">...</div>
      </div>

      <!-- 3. 狀態統計區 (Stats Panel) -->
      <div class="stats-panel">
        <div class="stat-box">
          <div class="label">Max</div>
          <div class="val" id="maxVal">0</div>
        </div>
      </div>

      <!-- 4. Step Breakdown (當前步驟簡述) -->
      <div class="step-breakdown">
        <div id="stepText">Ready</div>
      </div>

      <!-- 5. 控制區 (Controls) -->
      <div class="controls">
        <button id="prevBtn">Prev</button>
        <button id="nextBtn">Next</button>
        <button id="resetBtn">Reset</button>
        <button id="playBtn">Auto Play</button>
        <select id="speedSelect">
          ...
        </select>
      </div>
    </div>

    <!-- [CRITICAL] 邏輯解釋卡片 (必須顯眼) -->
    <div class="viz-card logic-card">
      <div class="viz-title">邏輯解釋 (Logic Explanation)</div>
      <div class="explanation" id="explanation"></div>
    </div>
  </div>

  <!-- 程式碼面板 -->
  <div class="code-area">
    <div class="viz-card" style="height: 100%;">
      <div class="viz-title">C++ Algorithm</div>
      <div class="code-panel" id="codeDisplay"></div>
    </div>
  </div>
</div>
```

## 2. D3.js 高品質視覺化規範

### 2.1 必須使用 D3.js (SVG)

- **禁止** 只用簡單的 HTML Divs 排列 (除非是純文本日誌)。
- **必須** 使用 SVG (`<svg>`) 繪製結構 (Array, Tree, Graph, DP Table)。
- **必須** 使用 `viewBox` 屬性確保 SVG 可隨視窗縮放，不能寫死 `width="800"`。

### 2.2 視覺元素標準

- **Array/DP**: 使用 SVG `<rect>` + `<text>`，避免 HTML Table。
- **Tree/Graph**: 使用 `d3.forceSimulation` 或 `d3.tree` / `d3.hierarchy` 佈局。
- **Pointer (指針)**: 必須有明確的箭頭或高亮框 (e.g. `pointers` layer)，且會有平滑移動動畫。
- **Text**: 文字必須清晰，對比度高 (使用 CSS 變數 `var(--viz-text)` 等)。

### 2.3 配色系統 (Tailwind/CSS Variables)

請使用以下標準色票：

- **Node/Base**: `#3b82f6` (Blue-500)
- **Active/Processing**: `#fbbf24` (Amber-400) - 當前正在計算/比較的節點
- **Success/Valid**: `#22c55e` (Green-500) - 已確認/已加入結果集
- **Error/Invalid**: `#ef4444` (Red-500) - 不符合條件/被剪枝
- **Auxiliary**: `#a855f7` (Purple-500) - 輔助結構 (Stack/Queue)
- **Background**: `rgba(30, 41, 59, 0.4)` (Slate-800 alpha) - 繪圖區背景

### 2.4 動畫原則 (High-End Polish)

1.  **Object Constancy**: 使用 D3 Data Key (`.data(data, d => d.id)`) 確保元素身份一致，實現平滑過渡 (Transitions)。
2.  **Transitions**: 所有狀態改變（顏色、位置、大小）必須有動畫 `transition().duration(500)`。
3.  **Enter/Update/Exit**:
    - Enter: 淡入或從小變大 (Pop in)
    - Update: 移動或變色
    - Exit: 淡出或縮小移除

## 3. 開發流程 CheckList (每題必對照)

在提交任何視覺化器之前，**必須** 自我審查以下點：

- [ ] **邏輯完整性**: `explanation` 是否解釋了 "Why"？(e.g. 為什麼選這個區間？為什麼 dp[i] 是這個值？)
- [ ] **視覺清晰度**: 是否能一眼看出當前指針在哪？當前比較的兩個元素是誰？
- [ ] **所有節點可見**: 確保 SVG `viewBox` 設定正確，且 Force Graph 有邊界限制，節點不會飛出畫面。
- [ ] **互動性**: "自訂測試" 輸入框是否能處理極端值？(空字串、單節點等)
- [ ] **程式碼對應**: 上一步/下一步時，右側代碼高亮是否準確對應？

## 4. 範例代碼 (Step Generation 結構)

```javascript
function simulate(data) {
  const steps = [];
  // ... logic ...

  // Example Step Push
  steps.push({
    // State Snapshots (Clone objects!)
    pointers: { i, j },
    dpArray: [...dp],
    graphNodes: JSON.parse(JSON.stringify(nodes)),

    // Narrative
    msg: `檢查 dp[${i}] = ${dp[i]}`,
    highlightLines: [5, 6], // Code lines

    // Deep Explanation
    explanation: {
      title: "狀態轉移 (State Transition)",
      text: "因為 s[i] == s[j]，我們繼承左下角 dp[i+1][j-1] 的結果。這代表內部子字串已經是回文...",
      formula: "dp[i][j] = dp[i+1][j-1]",
    },
  });

  return steps;
}
```
