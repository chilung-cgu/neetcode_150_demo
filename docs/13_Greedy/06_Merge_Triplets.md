---
title: "Merge Triplets to Form Target Triplet (合併三元組以形成目標三元組)"
description: "給定一個二維整數陣列 `triplets`，其中每個 `triplets[i] = [ai, bi, ci]`。 以及一個整數陣列 `target = [x, y, z]`。 定義操作 **Merge**: 兩個三元組 `[a1, b1, c1]` 和 `[a2, b2, c2]` 合併後變成 `["
tags:
  - Greedy
difficulty: Medium
---

# Merge Triplets to Form Target Triplet (合併三元組以形成目標三元組) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #1899** — [題目連結](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | [NeetCode 解說](https://neetcode.io/problems/merge-triplets-to-form-target)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個二維整數陣列 `triplets`，其中每個 `triplets[i] = [ai, bi, ci]`。
以及一個整數陣列 `target = [x, y, z]`。
定義操作 **Merge**: 兩個三元組 `[a1, b1, c1]` 和 `[a2, b2, c2]` 合併後變成 `[max(a1, a2), max(b1, b2), max(c1, c2)]`。
你可以執行任意次合併操作。
問是否能得到 `target` 三元組？

-   **Input**: `triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]`
-   **Output**: `true`
    -   Merge [2,5,3] and [1,7,5] -> [max(2,1), max(5,7), max(3,5)] = [2,7,5].
-   **Input**: `triplets = [[2,3,4],[1,2,3],[1,2,3]], target = [3,2,5]`
-   **Output**: `false`
    -   Need z=5. But max z in eligible triplets is 4.
-   **Constraints**:
    -   $1 <= triplets.length <= 10^5$
    -   $1 <= ai, bi, ci, x, y, z <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試所有子集的組合？
這不是求和，這是求 `max`。
只要子集中某個 column 的最大值等於 target 即可。
但也有限制：如果在取最大值的過程中，另一個 column 的值超過了 target，那麼這個三元組就不能用。

---

## 3. 💡 The "Aha!" Moment (優化)

**Greedy Filtering**:

1.  **Filter (過濾)**:
    任何一個三元組 `t`，如果 `t[0] > target[0]` 或 `t[1] > target[1]` 或 `t[2] > target[2]`，那麼這個三元組 **絕對不能選**。
    因為 `max` 操作只會讓值變大，如果你已經超過了 target，那以後怎麼合併都回不來了。

2.  **Verify (驗證)**:
    過濾掉那些「有害」的三元組後，剩下的都是「安全」的 (所有維度都小於等於 target)。
    我們將所有剩下的「安全」三元組全部合併起來（取 max）。
    如果合併後的結果等於 `target`，則 Return `true`。
    如果合併後的結果某一位小於 `target`，因為我們已經用盡了所有可用的材​​料，所以 Return `false`。

    只需檢查是否有三元組分別貢獻了 `target[0]`, `target[1]`, `target[2]` 即可。
    即：是否存在 `t` (safe) 使得 `t[0] == target[0]`？
    是否存在 `t` (safe) 使得 `t[1] == target[1]`？
    是否存在 `t` (safe) 使得 `t[2] == target[2]`？
    如果三個條件都滿足，則 True。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../merge_triplets_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../merge_triplets_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy Filtering

```cpp
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        // Track which parts of the target we have achieved
        bool foundX = false;
        bool foundY = false;
        bool foundZ = false;

        for (const auto& t : triplets) {
            // Filter: If any component is greater than target, discard this triplet completely
            if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2]) {
                continue;
            }

            // If valid, check if it contributes to matching the target
            if (t[0] == target[0]) foundX = true;
            if (t[1] == target[1]) foundY = true;
            if (t[2] == target[2]) foundZ = true;
        }

        return foundX && foundY && foundZ;
    }
};
```

### Python Reference

```python
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        // 我們需要找到是否有有效的三元組能分別滿足 target 的 x, y, z
        bool x_ok = false;
        bool y_ok = false;
        bool z_ok = false;

        for (auto& t : triplets) {
            // 關鍵過濾步驟：
            // 如果這個三元組的任何一個值大於 target 的對應值，
            // 這個三元組就是「有毒」的，一旦選了它，max 操作會讓結果永遠大於 target，
            // 所以我們必須直接跳過它。
            if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2]) {
                continue;
            }

            // 如果這是一個「安全」的三元組 (所有值 <= target)
            // 我們看看它能不能貢獻出 target 想要的值
            if (t[0] == target[0]) x_ok = true;
            if (t[1] == target[1]) y_ok = true;
            if (t[2] == target[2]) z_ok = true;

            // 如果三個值都已經湊齊了，可以提早回傳
            if (x_ok && y_ok && z_ok) return true;
        }

        return x_ok && y_ok && z_ok;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Iterate triplets once.
-   **Space Complexity**: $O(1)$
    -   No extra space.

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 你會如何處理更大的輸入？
- 有沒有更好的空間複雜度？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有考慮邊界條件
- ⚠️ 未討論複雜度

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 主動討論 trade-offs
- 💎 提供多種解法比較
