---
title: "Container With Most Water (盛最多水的容器)"
description: "題目給一個整數陣列 `height`，長度為 `n`。 有 `n` 條垂直線，第 `i` 條線的兩端點分別是 `(i, 0)` 和 `(i, height[i])`。 我们要找出兩條線，讓這兩條線與 X 軸形成的容器 (Container) 能裝最多的水。 回傳最大水量。"
tags:
  - Two Pointers
  - Array
difficulty: Medium
---

# Container With Most Water (盛最多水的容器) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #11** — [題目連結](https://leetcode.com/problems/container-with-most-water/) | [NeetCode 解說](https://neetcode.io/problems/max-water-container)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `height`，長度為 `n`。
有 `n` 條垂直線，第 `i` 條線的兩端點分別是 `(i, 0)` 和 `(i, height[i])`。
我们要找出兩條線，讓這兩條線與 X 軸形成的容器 (Container) 能裝最多的水。
回傳最大水量。

- **計算公式**: `Area = min(height[left], height[right]) * (right - left)`
  - 高度由較短的那根決定 (短板效應)。
  - 寬度是兩根柱子的距離。
- **Output**: 最大面積。
- **Input**: `[1,8,6,2,5,4,8,3,7]`
- **Output**: `49` (由 index 1 (height 8) 和 index 8 (height 7) 組成，寬度 7，高度 7，面積 49)。

---

## 2. 🐢 Brute Force Approach (暴力解)

試過所有可能的組合。
for `i` from 0 to n:
for `j` from i+1 to n:
calculate area
update max

- **Time Complexity**: $O(n^2)$。
- **Result**: TLE。 $n$ 可以到 $10^5$。

---

## 3. 💡 The "Aha!" Moment (優化)

我們希望這兩個因子都最大化：

1.  **Width** (`right - left`)
2.  **Height** (`min(height[left], height[right])`)

最寬的容器必定是 `L=0`, `R=n-1`。我們可以從這個狀態開始，慢慢縮小寬度，試圖找到更高的板子來彌補寬度的損失。

**Two Pointers 策略**:

1.  設 `L` 在頭，`R` 在尾。計算當前 Area。
2.  **關鍵決策 (Greedy)**: 我們該移動哪根柱子？
    - 假設 `height[L] < height[R]`。
    - 容器的高度受限於 `height[L]`。
    - 如果我們移動 `R` (往左)，寬度變小，且高度**不可能超過**原本的 `height[L]` (因為短板還是 L)。所以面積**一定變小**。
    - 如果我們移動 `L` (往右)，寬度變小，但我們**有可能**遇到一個更高的板子，讓這新的短板變高，進而增加面積。
    - **結論**: 永遠移動**較短**的那根柱子。如果一樣高，兩邊都可以動 (或者一起動)。

這種貪婪策略保證了我們不會錯過最大解，因為我們捨棄的每個狀態都已被證明「不可能比當前更好」。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../container_water_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../container_water_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy Two Pointers

```cpp
#include <vector>
#include <algorithm> // for max, min

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;

        while (left < right) {
            // 計算當前面積
            // 寬度: right - left
            // 高度: min(height[left], height[right])
            // 這裡為了效能，可以手寫 min
            int h = min(height[left], height[right]);
            int w = right - left;
            int current_area = h * w;

            max_area = max(max_area, current_area);

            // Greedy Move: 移動較短的那邊
            // 因為受限於短邊，如果不移短邊，移長邊只會讓寬度變小，高度卻無法增加(被短邊卡死)
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return max_area;
    }
};
```

### Python Reference

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int res = 0; // 用來存最大面積

        while (l < r) {
            // 算出當前柱子形成的面積。注意：這不一定是中間有水，而是單純兩線之間的矩形面積
            // 木桶理論：水的高度取決於最短的那塊木板
            int area = (r - l) * min(height[l], height[r]);
            res = max(res, area);

            // 核心邏輯：
            // 如果左邊柱子比右邊矮，那這根左柱子已經發揮了它在這個寬度下的最大潛力了。
            // 任何以這根左柱子為邊、且寬度更小的容器，面積一定更小。
            // 所以我們可以放心的丟棄這根左柱子，去找下一根可能的潛力股。
            if (height[l] < height[r]) {
                l++;
            } else {
                // 同理，如果右邊比較矮（或相等），移動右邊
                r--;
            }
        }

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - 雙指標從兩端向中間移動，每個元素最多被訪問一次。
- **Space Complexity**: $O(1)$
  - 只需常數個變數 (`l`, `r`, `res`)。

**證明 (Proof of Correctness)**:
假設最佳解是 `(optL, optR)`。我們的指針初始化在 `(0, n-1)`。
由於我們規定每次都移動較短的那邊，這意味著我們是在不斷縮減搜索區間 `[L, R]`。
如果我們的演算法錯過了 `(optL, optR)`，那只能是因為在某個時刻，我們移動了 `optL` (雖然它可能比較高) 或者移動了 `optR`。
但我們的規則是「只移動較短的」。如果我們處在 `L=optL` 且 `R > optR` 的狀態：

1.  如果 `height[optL] > height[R]` -> 我們會移動 `R` (正確，朝 `optR` 前進)。
2.  如果 `height[optL] < height[R]` -> 我們會移動 `optL`? - 等等，如果 `height[optL]` 真的比右邊那個非最佳解還短，那這就不會是最佳解的一部分了嗎？- 也不一定，可能 `optR` 非常近。
    這是一個經典的**反證法**證明題，結論是：這個貪婪策略是安全的，我們排除了所有「不可能比當前更好」的解。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果允許傾斜容器呢？
- Trapping Rain Water 的差異？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 移動錯誤的指標
- ⚠️ 不理解為何可以安全移動較短的那邊

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 清晰解釋貪心策略的正確性
- 💎 與暴力解的對比

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Trapping Rain Water (接雨水)](05_Trapping_Rain_Water.md)
