---
description: 為 NeetCode 題目添加高品質互動式演算法視覺化器
---

# 添加視覺化器 Workflow

此 workflow 用於為 NeetCode 150 題目創建高品質的互動式演算法視覺化器。

## 品質標準

每個視覺化器必須包含：

1. **繁體中文技術解說** - 所有說明文字使用繁體中文
2. **演算法公式顯示** - 顯示關鍵公式（如 `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`）
3. **準確的步驟模擬** - 動態生成步驟，非硬編碼
4. **視覺狀態追蹤** - Stack、Heap、DP 表格等資料結構視覺化
5. **C++ 程式碼高亮** - 當前執行行高亮顯示

## 檔案結構

```
docs/
├── XX_Category/
│   ├── 01_Problem_Name.md          # 題目說明文件
│   └── problem_name_visualizer.html # 視覺化器
└── assets/
    └── visualizer/
        ├── core.js                  # 核心類別 AlgorithmVisualizer
        └── style.css                # 共用樣式
```

## 創建步驟

// turbo-all

### 1. 確認題目資訊

```bash
# 查看題目的 .md 檔案
cat docs/XX_Category/NN_Problem_Name.md
```

### 2. 使用模板創建視覺化器

視覺化器 HTML 結構：

```html
<!DOCTYPE html>
<html lang="zh-TW">
  <head>
    <meta charset="UTF-8" />
    <title>題目名稱 - 視覺化</title>
    <link rel="stylesheet" href="../assets/visualizer/style.css" />
    <style>
      /* 題目特定的 CSS */
    </style>
  </head>
  <body>
    <div class="main-layout">
      <div class="canvas-area">
        <div class="viz-card">
          <div class="viz-title">題目名稱（演算法類型）</div>
          <!-- 視覺化區域 -->
          <div class="controls">
            <button class="viz-btn" id="prevBtn">← 上一步</button>
            <div class="step-indicator">
              步驟 <span id="currentStep">0</span> /
              <span id="totalSteps">0</span>
            </div>
            <button class="viz-btn primary" id="nextBtn">下一步 →</button>
            <button class="viz-btn" onclick="resetVisualization()">
              ↻ 重置
            </button>
          </div>
          <div class="state-grid">
            <!-- 狀態顯示 -->
          </div>
        </div>
        <div class="viz-card">
          <div class="viz-title">演算法說明</div>
          <div class="explanation" id="explanation"></div>
        </div>
      </div>
      <div class="code-area">
        <div class="viz-card">
          <div class="viz-title">演算法 (C++)</div>
          <div class="code-panel" id="codeDisplay"></div>
        </div>
      </div>
    </div>
    <script src="../assets/visualizer/core.js"></script>
    <script>
      const codeStructure = [
        { line: "code line 1", id: 0 },
        // ... 更多程式碼行
      ];

      function generateAlgorithmSteps() {
        const steps = [];
        // 動態生成演算法步驟
        // 每個 step 包含：
        // - 當前狀態
        // - highlightLines: 要高亮的程式碼行
        // - explanation: { title, text, formula }
        return steps;
      }

      let viz;
      function init() {
        viz = new AlgorithmVisualizer({
          codeLines: codeStructure,
          onStepChange: (step) => {
            // 更新視覺化狀態
          },
        });
        viz.setSteps(generateAlgorithmSteps());
      }

      function resetVisualization() {
        init();
      }
      window.addEventListener("load", init);
    </script>
  </body>
</html>
```

### 3. 關鍵實作要點

- **步驟生成**：使用 `generateAlgorithmSteps()` 動態生成，模擬真實演算法執行
- **說明格式**：每個步驟包含 `title`（標題）、`text`（解說）、`formula`（公式，可選）
- **程式碼高亮**：透過 `highlightLines` 陣列指定當前執行的程式碼行

### 4. 在題目 .md 中嵌入視覺化器

在題目的 .md 檔案中，於 "Aha! 時刻" 區段後加入：

```html
<div class="visualizer-container">
  <iframe
    src="./problem_name_visualizer.html"
    height="750"
    style="width: 100%; border: none; border-radius: 12px;"
  ></iframe>
</div>
```

## 參考範例

高品質視覺化器範例：

- `docs/04_Stack/leetcode_84_visualizer.html` - Largest Rectangle in Histogram
- `docs/01_Arrays_and_Hashing/two_sum_visualizer.html` - Two Sum
- `docs/11_1D_DP/coin_change_visualizer.html` - Coin Change
