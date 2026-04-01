---
title: "Meeting Rooms II (會議室 II)"
description: "給定一個會議時間區間的陣列 `intervals`，其中 `intervals[i] = [start_i, end_i]`。 請找出 **最少需要幾間會議室** 才能舉行所有會議。"
tags:
  - Intervals
  - Sorting
difficulty: Medium
---

# Meeting Rooms II (會議室 II) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #253** — [題目連結](https://leetcode.com/problems/meeting-rooms-ii/) | [NeetCode 解說](https://neetcode.io/problems/meeting-schedule-ii)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個會議時間區間的陣列 `intervals`，其中 `intervals[i] = [start_i, end_i]`。
請找出 **最少需要幾間會議室** 才能舉行所有會議。

-   **Input**: `intervals = [[0,30],[5,10],[15,20]]`
-   **Output**: `2`
    -   解釋：此時有兩個會議時間重疊：[0,30] 和 [5,10]。需要兩間房。第 3 個會議 [15,20] 可以復用 [5,10] 的房間。
-   **Input**: `intervals = [[7,10],[2,4]]`
-   **Output**: `1`
-   **Constraints**:
    -   $1 <= intervals.length <= 10^4$
    -   $0 <= start_i < end_i <= 10^6$

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一個時間點，計算同時進行的會議數量，取最大值。
時間點是連續的，但我們可以只關注所有區間的端點。

-   **Time**: $O(N^2)$ (如果遍歷所有區間來檢查每個點) 或者 $O(Range)$ (掃描線)。

---

## 3. 💡 The "Aha!" Moment (優化)

這題本質上是求 **「同一時間最大重疊區間數」**。

**Algorithm 1: Min-Heap**

1.  按 **Start Time** 排序。
2.  使用一個 **Min-Heap** 來儲存目前 **正在使用** 的會議室的 **結束時間**。
3.  遍歷會議：
    -   對於新會議 `newInterval`：
    -   如果 `newInterval.start >= min_heap.top()`：說明最早結束的那場會議已經結束了。我們可以復用這間房間。Pop heap (釋放房間)。
    -   Push `newInterval.end` (使用房間)。
    -   Heap 的大小就是所需的房間數。
4.  答案是遍歷過程中 Heap 達到過的最大大小。 (或者是最後 Heap 的大小，因為只增不減的邏輯是: 如果復用則 pop+push，沒復用則 push。Heap size 代表 active rooms)。

**Algorithm 2: Chronological Ordering (Two Pointers)**
我們可以把「開始」和「結束」事件分開來看。

1.  將所有的 `start_times` 取出並排序。
2.  將所有的 `end_times` 取出並排序。
3.  使用兩個指針 `s` (start pointer) 和 `e` (end pointer)。
4.  遍歷 `s`：
    -   如果 `start[s] < end[e]`：代表一個會議要開始了，但是還沒有會議結束。所以需要一個新房間。`count++`, `s++`。
    -   如果 `start[s] >= end[e]`：代表在會議 `s` 開始之前，已經有會議 `e` 結束了。我們可以釋放一個房間 (邏輯上)。`count--`, `e++`, `s++` (同時新會議進來，所以實際 active rooms 不變)。
5.  記錄過程中 `count` 的最大值。

**Comparison**:
Alg 1 需要 Heap 操作 $O(N \log N)$。
Alg 2 需要排序兩個陣列 $O(N \log N)$，然後線性掃描 $O(N)$。空間 $O(N)$。
兩者複雜度相當。Alg 2 在空間常數上可能稍好 (不需要 Priority Queue 結構與動態分配)。
我們實現 Alg 2，因為它更直觀地展示了「時間軸上的事件」概念。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../meeting_rooms_ii_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../meeting_rooms_ii_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Chronological Ordering

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;

        vector<int> starts;
        vector<int> ends;
        int n = intervals.size();

        // 分離並收集 start 和 end
        for(const auto& i : intervals) {
            starts.push_back(i[0]);
            ends.push_back(i[1]);
        }

        // 排序
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        int s = 0, e = 0;
        int count = 0;
        int maxRooms = 0;

        while (s < n) {
            // 如果有會議開始的時間 < 最早結束的時間
            // 說明我們需要開新房間
            if (starts[s] < ends[e]) {
                count++;
                s++;
            } else {
                // 會議結束了，釋放房間
                // (注意：同時 s 也會增加，因為我們處理下一個 start 事件，
                // 這裡可以理解為：一個會議結束，騰出空位給當前這個 starts[s])
                // 嚴格來說，這裡應該是 count-- (釋放)，然後 loop 繼續判斷。
                // 但為了簡潔，當 start >= end 時，等於是 (釋放一個 + 佔用一個)，淨值不變。
                // 我們可以直接 s++, e++，count 不變。
                // 但為了邏輯清晰，寫成釋放的邏輯：
                count--;
                e++;
            }
            maxRooms = max(maxRooms, count);
        }

        return maxRooms;
    }
};
```

### Python Reference

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;

        int n = intervals.size();
        vector<int> start(n);
        vector<int> end(n);

        // 將開始時間和結束時間分開儲存
        for (int i = 0; i < n; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        // 分別排序
        // 這樣做的意義是把時間軸上的「事件」有序化
        // 我們不在乎哪個 start 對應哪個 end，只在乎在某個時間點，有多少個 start 還沒 end
        sort(start.begin(), start.end());
        sort(end.begin(), end.end());

        int s = 0; // start 指針
        int e = 0; // end 指針
        int count = 0; // 當前使用房間數
        int maxRooms = 0; // 歷史最大房間數

        while (s < n) {
            // 如果下一個會議的開始時間，早於目前最早結束會議的結束時間
            // 代表我們必須多開一間房間
            if (start[s] < end[e]) {
                count++;
                s++;
            } else {
                // 如果 start[s] >= end[e]，代表在 start[s] 開始之前（或同時），
                // 有一個會議已經結束了 (end[e])。
                // 所以我們可以釋放一間房間。
                count--;
                e++;
            }

            // 更新最大值
            maxRooms = max(maxRooms, count);
        }

        return maxRooms;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \log N)$
    -   Sorting two arrays takes $O(N \log N)$.
    -   Two pointers pass takes $O(N)$.
-   **Space Complexity**: $O(N)$
    -   Start and End arrays.

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
- [Meeting Rooms (會議室)](04_Meeting_Rooms.md)
