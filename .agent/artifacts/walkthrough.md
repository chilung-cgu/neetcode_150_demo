# Walkthrough - LeetCode 84 Visualization Integration

## Unlocked Capabilities (已解鎖功能)

這份文件記錄了如何將高品質的互動式演算法視覺化工具整合至 MkDocs 文件中。

### 1. 核心視覺化架構 (Core Visualization Architecture)

我們建立了模組化的共用資源，位於 `docs/assets/visualizer/`：

- **Style (`style.css`)**: 定義了 **Premium Glassmorphism** 風格 (深色背景、毛玻璃卡片、Neon 霓虹光暈)。
- **Core Logic (`core.js`)**: 封裝了 `AlgorithmVisualizer` 類別，負責狀態管理、DOM 操作與圖表繪製。

### 2. LeetCode 84 整合範例

成功重構並嵌入了 `Largest Rectangle in Histogram` 的視覺化：

- **Iframe Embedding**: 在 Markdown 中使用 `iframe` 完美嵌入，不干擾文件閱讀。
- **Fullscreen Mode**: 提供全螢幕連結，讓使用者能沈浸式操作。
- **Interactive Features**: 支援上一步/下一步、重置、鍵盤操作 (左右鍵)。

## Demonstration (成果展示)

### Visualizer Design

![Glassmorphism Design](file:///data/leo/.gemini/antigravity/brain/722066e4-446b-4b36-93f7-87b269b89961/visualizer_glassmorphism_look_1768651353858.png)
_圖：整合後的視覺化介面，呈現深色毛玻璃風格與動態程式碼高亮_

## Validation (驗證結果)

- [x] **Localhost Verification**: 確認 `http://localhost:8084/04_Stack/leetcode_84_visualizer.html` 顯示正常。
- [x] **Design Check**: 長條圖顏色正確 (Orange=Current, Green=Stack)，程式碼高亮同步。
- [x] **Integration Check**: Markdown Iframe 顯示正確。
- [x] **UI Polish**: 程式碼區塊寬度增加至 450px，優化字體大小與閱讀體驗。
- [x] **Architectural Fix**: 修正文件引用路徑為 `../assets/`，解決 MkDocs 資料夾結構導致的 404 問題。
- [x] **Deployment Fix**: 確認提交 `leetcode_84_visualizer.html` 的路徑修正 (此為導致使用者看到無樣式頁面的主因)。

## Next Steps (後續規劃)

- 觀察 GitHub Pages 部署狀態。
- 根據此架構，開始 Phase 2 自動化工作 (`/add-visualizer`)。
