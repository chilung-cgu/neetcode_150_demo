---
description: 對視覺化器進行高標準品質審核，確保每個檔案都具備互動性、動態性、複雜度標示等完整功能
---

# 視覺化器高標準審核工作流程

此 workflow 用於對 NeetCode 150 視覺化器進行全面的品質審核，確保每個檔案都符合高標準。

## 高標準檢查項目

每個視覺化器必須同時具備以下 6 項特徵：

| 項目        | 說明                 | 檢測關鍵字                                             |
| ----------- | -------------------- | ------------------------------------------------------ |
| Interactive | 自訂輸入或多範例切換 | `custom-input-section`, `runCustomInput`, `setExample` |
| Dynamic     | 演算法步驟動態生成   | `generateAlgorithmSteps`                               |
| Complexity  | 時間/空間複雜度標示  | `complexity-badge`                                     |
| Explanation | 演算法解說區塊       | `id="explanation"`                                     |
| CoreJS      | 使用統一核心框架     | `core.js`                                              |
| Controls    | 完整播放控制按鈕     | `prevBtn`, `nextBtn`                                   |

---

## 執行步驟

### 1. 創建審核腳本

在專案根目錄創建 `audit_visualizers.py`：

```python
import os
import re

DOCS_DIR = 'docs'
OUTPUT_FILE = 'visualizer_quality_report.md'

features_check = {
    'Interactive': [r'custom-input-section', r'runCustomInput', r'setExample', r'<input'],
    'Dynamic': [r'generateAlgorithmSteps', r'generateSteps', r'function generate'],
    'Complexity': [r'complexity-badge'],
    'Explanation': [r'explanation', r'id="explanation"'],
    'CoreJS': [r'core\.js'],
    'Controls': [r'prevBtn', r'nextBtn']
}

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    results = {}
    for feature, patterns in features_check.items():
        results[feature] = any(re.search(p, content) for p in patterns)
    return results

def main():
    files = []
    for root, dirs, filenames in os.walk(DOCS_DIR):
        for f in filenames:
            if f.endswith('_visualizer.html'):
                files.append(os.path.join(root, f))
    files.sort()

    report_lines = ["# 視覺化器高標準逐一檢測報告", f"\n檢測總數: {len(files)}\n"]
    report_lines.append("| ID | 檔案 | 互動性 | 動態生成 | 複雜度 | 解說 | CoreJS | 狀態 |")
    report_lines.append("|---|---|---|---|---|---|---|---|")

    pass_count = 0
    for idx, filepath in enumerate(files, 1):
        name = os.path.basename(filepath)
        res = check_file(filepath)
        all_pass = all(res.values())
        if all_pass: pass_count += 1
        status = "✅" if all_pass else "❌"
        row = f"| {idx} | {name} | {'✅' if res['Interactive'] else '❌'} | {'✅' if res['Dynamic'] else '❌'} | {'✅' if res['Complexity'] else '❌'} | {'✅' if res['Explanation'] else '❌'} | {'✅' if res['CoreJS'] else '❌'} | {status} |"
        report_lines.append(row)

    report_lines.append(f"\n**合格統計**: {pass_count}/{len(files)}")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    print(f"Pass rate: {pass_count}/{len(files)}")

if __name__ == '__main__':
    main()
```

// turbo

### 2. 執行審核腳本

```bash
python3 audit_visualizers.py
```

### 3. 檢視報告

開啟 `visualizer_quality_report.md`，查看哪些檔案未通過檢測。

### 4. 修正未達標檔案

對於每個標記為 ❌ 的項目，進行以下修正：

#### 缺少 Interactive（自訂輸入）

在 `<div class="viz-card">` 內加入：

```html
<div
  class="custom-input-section"
  style="margin-bottom: 15px; padding: 10px; background: var(--viz-bg-secondary); border-radius: 8px;"
>
  <div style="font-weight:bold; margin-bottom:8px;">🎮 自訂測試</div>
  <div style="display: flex; gap: 10px; flex-wrap: wrap;">
    <button onclick="setExample(1)">範例 1</button>
    <button onclick="setExample(2)">範例 2</button>
  </div>
</div>
```

並在 JS 中加入：

```javascript
function setExample(n) {
  // 根據 n 設定不同的測試資料
  init();
}
```

#### 缺少 Complexity（複雜度標示）

在控制區塊後加入：

```html
<div class="complexity-badge">
  <span class="label">Time:</span> O(n)
  <span class="label" style="margin-left: 12px;">Space:</span> O(1)
</div>
```

### 5. 重新執行審核

```bash
python3 audit_visualizers.py
```

重複步驟 3-5 直到達成 100% 合格率。

// turbo

### 6. 提交變更

```bash
git add . && git commit -m "[Visualizer] 🟢 100% High Standard Compliance Verified"
git push
```

---

## 補充說明

- 此 workflow 可與 `/add-visualizer` 搭配使用
- 新增視覺化器後，應執行此審核確保符合高標準
- 審核腳本 `audit_visualizers.py` 可以保留在專案中供未來使用
