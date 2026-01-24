---
description: 將 Linked List 視覺化器升級至 Gemini Dynamic View 等級精緻度
---

# Linked List 視覺化器精緻化升級 Skill

此 Skill 用於將 Linked List 類別的演算法視覺化器升級至 **Gemini Dynamic View 等級**精緻度。

## 設計原則

### 核心視覺元素

1. **圓形節點設計**
   - 使用 `border-radius: 50%` 創建圓形節點
   - 漸層背景：`linear-gradient(145deg, #3b82f6, #2563eb)`
   - 陰影效果：`box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3)`

2. **深色漸層背景**

   ```css
   .visualization-area {
     background: linear-gradient(135deg, #1e293b 0%, #0f172a 50%, #1e293b 100%);
   }
   ```

3. **發光效果 (Glow Effect)**
   - 當前操作節點有黃色發光

   ```css
   .node.active {
     box-shadow:
       0 0 25px rgba(251, 191, 36, 0.6),
       0 0 50px rgba(251, 191, 36, 0.3);
   }
   ```

4. **Pointer 標籤**
   - 在節點下方顯示指向該節點的 pointer 名稱
   - 顏色編碼：groupPrev(綠)、kth(紫)、curr(黃)、prev(橙)

   ```html
   <span class="node-pointer-label curr">curr</span>
   ```

5. **SVG 曲線箭頭**
   - 使用 SVG 繪製美觀的曲線箭頭
   - 反轉時變色：正常(灰)、反轉中(紅)、已反轉(綠)

6. **Step Breakdown 區域**
   - 每步顯示當前操作的程式碼說明
   - 例如：`curr->next = prev; // 1→3`

### 題目特化設計

每道 Linked List 題目有不同的「Aha! 時刻」，需獨立設計：

| 題目                | 視覺化重點                 | 關鍵 Pointer               |
| ------------------- | -------------------------- | -------------------------- |
| Reverse Linked List | prev/curr/next 移動        | prev, curr, next           |
| Merge Two Lists     | 比較與連接                 | l1, l2, merged             |
| Reorder List        | 找中點、反轉後半、交錯合併 | slow, fast, second         |
| Remove Nth Node     | 雙指針間隔                 | fast, slow                 |
| Copy Random         | 節點複製與 random 指向     | curr, copy                 |
| Add Two Numbers     | 進位計算                   | l1, l2, carry              |
| Linked List Cycle   | 快慢指針相遇               | slow, fast                 |
| Find Duplicate      | Floyd 循環檢測             | slow, fast                 |
| LRU Cache           | 雙向鏈表操作               | head, tail, node           |
| Merge K Lists       | 最小堆選擇                 | heap, current              |
| Reverse K-Group     | 分組反轉                   | groupPrev, kth, curr, prev |

---

## 實作步驟

### 1. 分析題目演算法

```bash
# 查看題目 .md 檔案
cat docs/06_Linked_List/NN_Problem_Name.md
```

理解：

- 使用哪些 pointer？
- pointer 如何移動？
- 連結如何變化？

### 2. 設計視覺化重點

確定：

- 需要追蹤的 pointer 列表
- pointer 顏色編碼
- 步驟細粒度（每個 pointer 移動 = 1 步）

### 3. 實作 HTML 結構

```html
<!-- 主視覺化區域 -->
<div class="visualization-area">
  <div class="linked-list-container">
    <div class="pointer-indicators" id="pointerIndicators">
      <!-- 動態生成 -->
    </div>
    <div class="nodes-row" id="nodesRow">
      <!-- 動態生成 -->
    </div>
  </div>
  <div class="legend-bar">
    <!-- 圖例 -->
  </div>
</div>

<div class="step-breakdown">
  <div class="step-breakdown-title">Step Breakdown</div>
  <div class="step-breakdown-text" id="stepBreakdown"></div>
</div>
```

### 4. 實作步驟生成函數

```javascript
function generateAlgorithmSteps(list) {
    const steps = [];

    // 每個 pointer 移動都是獨立步驟
    steps.push({
        nodes: [...],
        pointers: { ptr1: idx1, ptr2: idx2, ... },
        highlightLines: [lineIds],
        stepText: 'ptr1 = ptr1->next',
        explanation: { title, text, formula }
    });

    return steps;
}
```

### 5. 實作渲染函數

```javascript
function renderLinkedList(step) {
  // 1. 渲染節點（圓形 + 顏色）
  // 2. 渲染 pointer 標籤
  // 3. 渲染連結箭頭
  // 4. 更新狀態面板
  // 5. 更新 Step Breakdown
}
```

---

## CSS 模板

```css
/* 圓形節點 */
.node {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: linear-gradient(145deg, #3b82f6, #2563eb);
  color: white;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

/* 發光效果 */
.node.active {
  box-shadow:
    0 0 25px rgba(251, 191, 36, 0.6),
    0 0 50px rgba(251, 191, 36, 0.3);
  transform: scale(1.08);
}

/* Pointer 標籤 */
.node-pointer-label {
  position: absolute;
  bottom: -24px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 0.65rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
}
```

---

## 參考範例

高品質視覺化器標竿：

- [reverse_k_group_visualizer.html](file:///data/leo/chichi/neetcode_150_demo/docs/06_Linked_List/reverse_k_group_visualizer.html)

## 驗證清單

- [ ] 圓形節點 + 漸層背景
- [ ] DUMMY 節點（若適用）
- [ ] Pointer 標籤即時追蹤
- [ ] SVG 箭頭（支援方向變化）
- [ ] 發光效果（當前操作節點）
- [ ] Step Breakdown 區域
- [ ] 程式碼同步高亮
- [ ] 自訂輸入功能
- [ ] 自動播放功能
