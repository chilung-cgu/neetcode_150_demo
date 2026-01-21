---
title: "Non-overlapping Intervals (無重疊區間)"
description: "給定一個區間陣列 `intervals`。 你需要移除 **最少數量** 的區間，使得剩餘的區間互不重疊。"
tags:
  - 
Intervals  - Sorting
difficulty: Medium
---

# Non-overlapping Intervals (無重疊區間) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #435** — [題目連結](https://leetcode.com/problems/non-overlapping-intervals/) | [NeetCode 解說](https://neetcode.io/problems/non-overlapping-intervals)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個區間陣列 `intervals`。
你需要移除 **最少數量** 的區間，使得剩餘的區間互不重疊。

-   **Input**: `intervals = [[1,2],[2,3],[3,4],[1,3]]`
-   **Output**: `1`
    -   解釋：移除 `[1,3]` 後，剩下的 `[1,2], [2,3], [3,4]` 互不重疊。
-   **Input**: `intervals = [[1,2],[1,2],[1,2]]`
-   **Output**: `2`
    -   解釋：你需要移除兩個 `[1,2]` 才能剩下一個不重疊的。
-   **Constraints**:
    -   $1 <= intervals.length <= 10^5$
    -   $intervals[i].length == 2$
    -   $start_i < end_i$

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試移除所有可能的區間子集，檢查剩餘的是否重疊，並找出移除數量最少的。

-   **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個經典的 **Interval Scheduling** 問題。
我們的目標是：**保留盡可能多** 的不重疊區間。
(移除最少 = 保留最多)。

**Greedy Strategy**:

1.  **Sort**: 按照 **起始時間 (Start Time)** 排序。
2.  **Iterate**: 遍歷區間，維護前一個保留區間的結束時間 `prevEnd`。
    -   對於當前區間 `current`：
    -   如果不重疊 (`current.start >= prevEnd`)：
        -   很好，保留它。更新 `prevEnd = current.end`。
    -   如果重疊 (`current.start < prevEnd`)：
        -   必須移除其中一個。
        -   移除哪一個？當然是移除 **結束時間較晚** 的那個！
        -   為什麼？因為結束時間越晚，越容易與後面的區間重疊。為了給後面留出更多空間，我們要保留結束時間較早的那個。
        -   此時，我們把重疊計數加 1。
        -   更新 `prevEnd = min(prevEnd, current.end)` (也就是保留了結束得較早的那個)。

*註：另一種常見做法是按結束時間排序，然後貪心地選結束最早的。兩種都可以，按 Start 排序的邏輯比較容易跟 Merge Intervals 統一記憶。*

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../non_overlapping_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../non_overlapping_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy (Sort by Start)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;

        // 1. Sort by start time
        sort(intervals.begin(), intervals.end());

        int res = 0;
        int prevEnd = intervals[0][1];

        for (int i = 1; i < intervals.size(); i++) {
            // Overlap detected?
            if (intervals[i][0] < prevEnd) {
                res++;
                // Greedy choice: keep the one that ends first
                // to minimize chance of overlapping with subsequent intervals
                prevEnd = min(prevEnd, intervals[i][1]);
            } else {
                // No overlap, just update prevEnd
                prevEnd = intervals[i][1];
            }
        }

        return res;
    }
};
```

### Python Reference

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                # Overlap
                res += 1
                # Remove the one with larger end time (keep smaller end)
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;

        // 1. 按起始時間排序
        sort(intervals.begin(), intervals.end());

        int removeCount = 0;
        // 紀錄「上一個保留區間」的結束時間
        int prevEnd = intervals[0][1];

        for (int i = 1; i < intervals.size(); i++) {
            // 檢查當前區間是否與前一個重疊
            // 由於已排序，start >= prevStart，所以只要看 start < prevEnd
            if (intervals[i][0] < prevEnd) {
                // 發生重疊，必須移除一個
                removeCount++;

                // 貪心策略：
                // 我們有兩個選擇：移除 prev (上一個) 或 current (當前)
                // 為了讓後面的空間最大化，我們應該保留「結束時間較早」的那個
                // 換句話說，如果 prevEnd > currentEnd，我們應該只要 current，丟棄 prev
                // 所以 prevEnd 更新為兩者的最小值
                prevEnd = min(prevEnd, intervals[i][1]);
            } else {
                // 沒有重疊，這個區間可以安全保留
                // 更新 prevEnd 為當前區間的結束時間
                prevEnd = intervals[i][1];
            }
        }

        return removeCount;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \log N)$
    -   Due to sorting. Iteration is $O(N)$.
-   **Space Complexity**: $O(1)$ or $O(\log N)$
    -   Sorting space. No extra data structures used.

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

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Merge Intervals (合併區間)](02_Merge_Intervals.md)
