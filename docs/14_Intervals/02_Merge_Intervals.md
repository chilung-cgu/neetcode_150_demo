---
title: "Merge Intervals (合併區間)"
description: "給定一個區間陣列 `intervals`，其中 `intervals[i] = [start_i, end_i]`。 請合併所有 **重疊 (overlapping)** 的區間，並回傳一個不重疊的區間陣列，該陣列需覆蓋輸入中的所有區間。"
tags:
  - 
Intervals  - Sorting
difficulty: Medium
---

# Merge Intervals (合併區間) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #56** — [題目連結](https://leetcode.com/problems/merge-intervals/) | [NeetCode 解說](https://neetcode.io/problems/merge-intervals)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個區間陣列 `intervals`，其中 `intervals[i] = [start_i, end_i]`。
請合併所有 **重疊 (overlapping)** 的區間，並回傳一個不重疊的區間陣列，該陣列需覆蓋輸入中的所有區間。

-   **Input**: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
-   **Output**: `[[1,6],[8,10],[15,18]]`
    -   解釋：`[1,3]` 和 `[2,6]` 重疊，合併得到 `[1,6]`。
-   **Input**: `intervals = [[1,4],[4,5]]`
-   **Output**: `[[1,5]]`
    -   解釋：區間可僅在端點接觸（如 `[1,4]` 和 `[4,5]`），這也被視為重疊。
-   **Constraints**:
    -   $1 <= intervals.length <= 10^4$
    -   $intervals[i].length == 2$
    -   $0 <= start_i <= end_i <= 10^4$

---

## 2. 🐢 Brute Force Approach (暴力解)

將所有區間視為圖的節點。如果兩區間重疊，則連一條邊。
我們需要找出所有的 **連通分量 (Connected Components)**。
對於每個分量，合併後的區間是 `[min(starts), max(ends)]`。

-   **Time**: $O(N^2)$ 建圖。

---

## 3. 💡 The "Aha!" Moment (優化)

如果我們先將區間 **按照起始時間 (Start Time) 排序**，那麼重疊的區間一定會是連續出現的。
我們可以遍歷排序後的列表：

1.  從第一個區間開始，設為 `current_interval`。
2.  看下一個區間 `next_interval`：
    -   如果 `next_interval.start <= current_interval.end`：說明重疊。
        -   合併：`current_interval.end = max(current_interval.end, next_interval.end)`。
    -   否則：說明 `next_interval` 開始於 `current_interval` 結束之後，斷開了。
        -   將 `current_interval` 加入結果。
        -   更新 `current_interval = next_interval`。
3.  最後別忘了把最後一個 `current_interval` 加入結果。

這種方法只需一次遍歷，主要時間花費在排序上。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../merge_intervals_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../merge_intervals_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Sort & Merge

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};

        // 1. Sort by start time
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> result;
        // Start with the first interval
        result.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); i++) {
            // Get the last added interval from result (reference to modify it)
            vector<int>& last = result.back();

            // Check for overlap
            if (intervals[i][0] <= last[1]) {
                // Merge: Update the end time to the max of both
                last[1] = max(last[1], intervals[i][1]);
            } else {
                // No overlap: Add the current interval as a new one
                result.push_back(intervals[i]);
            }
        }

        return result;
    }
};
```

### Python Reference

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                # Merge
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};

        // 步驟 1: 按照起始時間排序
        // 這是解決所有區間問題的常見起手式
        sort(intervals.begin(), intervals.end());

        // 步驟 2: 初始化結果，放入第一個區間
        vector<vector<int>> result;
        result.push_back(intervals[0]);

        // 步驟 3: 遍歷剩下的區間
        for (int i = 1; i < intervals.size(); i++) {
            // 取出目前結果集中的最後一個區間 (也就是我們正在嘗試擴展的那個)
            // 使用 reference (&) 以便直接修改它
            vector<int>& last = result.back();

            // 檢查當前遍歷到的區間 (intervals[i]) 是否與 last 重疊
            // 由於已經排序，intervals[i].start >= last.start 必定成立
            // 所以只要 intervals[i].start <= last.end 就代表重疊
            if (intervals[i][0] <= last[1]) {
                // 發生重疊，合併區間
                // 新的結束時間取兩者最大值
                last[1] = max(last[1], intervals[i][1]);
            } else {
                // 沒有重疊，將當前區間加入結果，成為新的待合併區間
                result.push_back(intervals[i]);
            }
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \log N)$
    -   Sorting takes $O(N \log N)$.
    -   The linear scan takes $O(N)$.
-   **Space Complexity**: $O(N)$ or $O(\log N)$
    -   Depends on the sorting algorithm implementation (usually $O(\log N)$ stack space).
    -   Result list takes $O(N)$.

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
- [Insert Interval (插入區間)](01_Insert_Interval.md)
- [Non-overlapping Intervals (無重疊區間)](03_Non_Overlapping_Intervals.md)
