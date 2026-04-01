---
title: "Insert Interval (插入區間)"
description: "給定一個**非重疊 (non-overlapping)** 且 **已排序 (sorted)** 的區間列表 `intervals`，其中 `intervals[i] = [start_i, end_i]` 代表第 `i` 個區間的起始和結束。 另給定一個新的區間 `newInterval = [s"
tags:
  - Intervals
  - Sorting
difficulty: Medium
---

# Insert Interval (插入區間) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #57** — [題目連結](https://leetcode.com/problems/insert-interval/) | [NeetCode 解說](https://neetcode.io/problems/insert-new-interval)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個**非重疊 (non-overlapping)** 且 **已排序 (sorted)** 的區間列表 `intervals`，其中 `intervals[i] = [start_i, end_i]` 代表第 `i` 個區間的起始和結束。
另給定一個新的區間 `newInterval = [start, end]`。
請將 `newInterval` 插入到 `intervals` 中，使得 `intervals` 仍然保持有序且不重疊（如果有重疊，則需要合併）。
你可以假設 `intervals` 初始是按 `start` 升序排列的。

-   **Input**: `intervals = [[1,3],[6,9]], newInterval = [2,5]`
-   **Output**: `[[1,5],[6,9]]`
    -   解釋：`[2,5]` 與 `[1,3]` 重疊，合併為 `[1,5]`。`[6,9]` 不受影響。
-   **Input**: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]`
-   **Output**: `[[1,2],[3,10],[12,16]]`
    -   解釋：`[4,8]` 與 `[3,5],[6,7],[8,10]` 都有重疊，全併起來變成 `[3,10]`。
-   **Constraints**:
    -   $0 <= intervals.length <= 10^4$
    -   $intervals[i].length == 2$
    -   $0 <= start <= end <= 10^5$
    -   `intervals` is sorted by start in ascending order.

---

## 2. 🐢 Brute Force Approach (暴力解)

最直觀的方法：

1.  將 `newInterval` 直接加入到 `intervals` 列表中。
2.  根據 start time 重新排序整個列表。
3.  遍歷排序後的列表，執行標準的 "Merge Intervals" 操作（如果當前區間與前一個重疊，則合併）。

-   **Time Complexity**: $O(N \log N)$，因為需要排序。
-   **Space Complexity**: $O(N)$ (若不允許原地修改)。

---

## 3. 💡 The "Aha!" Moment (優化)

題目給定 `intervals` 已經是 **排序好** 且 **無重疊** 的。這是非常強的條件。
我們可以用 $O(N)$ 一次遍歷完成。

我們可以將所有區間分為三類：

1.  **完全在左邊 (Strictly Left)**：當前區間的 `end` < `newInterval.start`。這些直接加入結果。
2.  **重疊 (Overlapping)**：當前區間與 `newInterval` 有交集。即 `intervals[i].start <= newInterval.end` 且 `intervals[i].end >= newInterval.start`。
    -   我們不需要把這些區間加入結果，而是用它們來 **擴展** `newInterval`。
    -   `newInterval.start = min(newInterval.start, current.start)`
    -   `newInterval.end = max(newInterval.end, current.end)`
3.  **完全在右邊 (Strictly Right)**：當前區間的 `start` > `newInterval.end`。
    -   一旦遇到第一個這樣的區間，說明 `newInterval` 的合併已經結束了。
    -   我們可以先將最終合併好的 `newInterval` 加入結果。
    -   然後將剩下所有的區間直接加入結果。

邏輯流：

-   遍歷區間：
    -   If `current.end < newInterval.start`: Push `current` to result.
    -   Else if `current.start > newInterval.end`:
        -   Push `newInterval` to result.
        -   Push `current` and all remaining intervals.
        -   Return result.
    -   Else (Overlap):
        -   Merge into `newInterval`.
-   Loop 結束後，別忘了把 `newInterval` 加入結果（如果它還沒被加進去，例如它比所有區間都大，或者它合併到了最後）。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../insert_interval_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../insert_interval_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: One Pass (Greedy)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int i = 0;
        int n = intervals.size();

        // 1. Add all intervals that come strictly before the new interval
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }

        // 2. Merge all overlapping intervals
        // Check if current interval overlaps with newInterval
        // Overlap condition: intervals[i].start <= newInterval.end
        // (Since we already passed checked intervals[i].end < newInterval.start,
        //  we know intervals[i].end >= newInterval.start logic is somewhat implicit or guaranteed to overlap if intervals[i].start <= newInterval.end)
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }

        // Add the merged interval
        result.push_back(newInterval);

        // 3. Add remaining intervals
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }

        return result;
    }
};
```

### Python Reference

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # If newInterval is strictly before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # If newInterval is strictly after current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # Merge logic
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int i = 0;
        int n = intervals.size();

        // 步驟 1: 處理所有在 newInterval 左邊且無重疊的區間
        // 條件：當前區間的結束時間 < newInterval 的開始時間
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }

        // 步驟 2: 處理重疊區間並合併
        // 條件：當前區間與 newInterval 重疊
        // 因為上面的 while 迴圈已經排除了所有 end < newInterval.start 的區間
        // 所以這裡只要檢查 start 是否 <= newInterval.end 即可確保重疊
        while (i < n && intervals[i][0] <= newInterval[1]) {
            // 合併：取最小起點和最大終點
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }

        // 將合併完成後的 newInterval 加入結果
        result.push_back(newInterval);

        // 步驟 3: 處理剩下在右邊且無重疊的區間
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   We iterate through the intervals exactly once.
-   **Space Complexity**: $O(1)$ (ignoring output space) or $O(N)$ (for result).
    -   We create a new list for the result.

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
