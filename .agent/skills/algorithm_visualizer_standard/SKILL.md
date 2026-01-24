---
description: 標準化演算法視覺化器開發流程，確保包含邏輯解釋與高品質 D3.js 視覺效果
---

# Algorithm Visualizer Standard SKILL

此 Skill 定義了專案中所有演算法視覺化器的開發標準。所有新的視覺化器或升級都**必須**嚴格遵守此規範，特別是**邏輯解釋 (Explanation)** 的完整性。

## 1. 核心架構 (Mandatory)

每個視覺化器必須使用專案統一的 `AlgorithmVisualizer` class (`core.js`)。

### 1.1 Step Object 必備欄位

每個動畫步驟 (Step Object) **必須** 包含以下欄位，缺一不可：

```javascript
{
    // [Required] 狀態數據 (State)
    // 根据具体题目，包含如 nodes, links, pointers, dpTable 等
    nodes: [...],

    // [Required] 操作描述 (UI 顯示)
    msg: "當前操作的簡短描述",

    // [Required] 程式碼高亮
    highlightLines: [1, 2, 3],

    // [CRITICAL] 邏輯解釋卡片數據 (Logic Card)
    // 這是教育核心，絕對不能遺漏！
    explanation: {
        title: "標題 (例如：發現重複值)",
        text: "詳細的自然語言解釋。說明為什麼這樣做，背後的邏輯是什麼。",
        formula: "數學公式或邏輯表達式 (例如：slow == fast)"
    }
}
```

### 1.2 UI 佈局標準

所有 HTML 必須遵循以下 DOM 結構：

```html
<div class="main-layout">
  <div class="canvas-area">
    <div class="viz-card">
      <div class="viz-title">題目名稱</div>
      <!-- 自訂輸入區 -->
      <div class="custom-input-section">...</div>

      <!-- 主要繪圖區 (D3/Canvas) -->
      <div class="visualization-area">
        <svg id="viz-svg">...</svg>
      </div>

      <!-- Step Breakdown (程式碼邏輯) -->
      <div class="step-breakdown">
        <div class="step-breakdown-title">Step Breakdown</div>
        <div class="step-breakdown-text" id="stepBreakdown"></div>
      </div>

      <!-- 控制區 -->
      <div class="controls">...</div>
    </div>

    <!-- [CRITICAL] 邏輯解釋卡片 -->
    <div class="viz-card">
      <div class="viz-title">演算法說明</div>
      <div class="explanation" id="explanation"></div>
    </div>
  </div>

  <!-- 程式碼面板 -->
  <div class="code-area">
    <div class="viz-card" style="height: 100%;">
      <div class="viz-title">Code</div>
      <div class="code-panel" id="codeDisplay"></div>
    </div>
  </div>
</div>
```

## 2. D3.js 視覺化規範

### 2.1 配色系統 (Tailwind/CSS Variables)

請使用以下標準色票，不要使用預設顏色：

- **Node/Base**: `#3b82f6` (Blue-500) -> `#2563eb` (Blue-600) Gradient
- **Active/Highlight**: `#fbbf24` (Amber-400) - 用於當前關注點
- **Success/Done**: `#22c55e` (Green-500) - 用於已完成、已排序、找到目標
- **Error/Delete**: `#ef4444` (Red-500) - 用於不匹配、刪除
- **Auxiliary**: `#a855f7` (Purple-500) - 用於輔助結構 (Heap, Stack, Map)

### 2.2 動畫原則

1.  **Object Constancy**: 使用 D3 的 data binding key (例如 `d => d.id`) 確保元素在 update 時是平滑過渡，而不是銷毀重建。
2.  **Transitions**: 所有位置移動 (`translate`)、顏色變化都應有 `.transition().duration(500)`。
3.  **Enter/Update/Exit**: 正確處理 D3 的數據生命週期。

## 3. 開發流程 CheckList

每次建立或重構視覺化器時，請檢查：

- [ ] **Explanation Object**: 確認 `simulate` 或 `generateSteps` 函數中，**每個** `push` 的步驟都有 `explanation` 物件。
- [ ] **Step Breakdown**: 確認畫面上有顯示 Step Breakdown (程式碼層級的細節)。
- [ ] **Logic Card**: 確認畫面右側有顯示「演算法說明」卡片，並且內容會隨步驟更新。
- [ ] **Interactive**: 自訂輸入 (Custom Input) 功能是否正常運作？
- [ ] **Responsive**: 介面是否在大螢幕上佈局合理 (Flex/Grid)？

## 4. 範例代碼 (Step Generation)

```javascript
function simulate(data) {
    const steps = [];

    // Step 1: Init
    steps.push({
        // ... state ...
        msg: "初始化",
        highlightLines: [0],
        explanation: {
            title: "初始化變數",
            text: "設定指針 i = 0, j = 0...",
            formula: "i=0, j=0"
        }
    });

    // Loop
    while(...) {
        // Step X
        steps.push({
            // ... state ...
            msg: `比較 A[${i}] 與 B[${j}]`,
            highlightLines: [5],
            explanation: {
                title: "元素比較",
                text: `因為 ${val1} < ${val2}，所以我們移動...`,
                formula: `${val1} < ${val2}`
            }
        });
    }

    return steps;
}
```
