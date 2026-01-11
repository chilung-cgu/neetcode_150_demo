# Meeting Rooms (會議室)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個會議時間區間的陣列 `intervals`，其中 `intervals[i] = [start_i, end_i]`。
請判斷一個人是否能夠 **參加所有的會議**。
(即判斷是否有任何兩個會議時間重疊)。

-   **Input**: `intervals = [[0,30],[5,10],[15,20]]`
-   **Output**: `false`
    -   解釋：[0,30] 與 [5,10] 重疊。
-   **Input**: `intervals = [[7,10],[2,4]]`
-   **Output**: `true`
    -   解釋：此人可以先參加 [2,4]，再參加 [7,10]。
-   **Constraints**:
    -   $0 <= intervals.length <= 10^4$
    -   $intervals[i].length == 2$
    -   $0 <= start_i < end_i <= 10^6$

---

## 2. 🐢 Brute Force Approach (暴力解)

比較每對會議 `(i, j)`，檢查它們是否重疊。

-   **Time**: $O(N^2)$。

---

## 3. 💡 The "Aha!" Moment (優化)

如果我們將會議按照 **開始時間** 排序，我們只需要檢查 **相鄰** 的兩個會議是否重疊即可。
如果 `intervals[i]` 與 `intervals[i+1]` 不重疊，那麼 `intervals[i]` 也不可能與 `intervals[i+2]` 重疊（因為 `i+2` 開始得更晚）。

**Logic**:

1.  Sort intervals by start time.
2.  Iterate from `i = 0` to `N-2`:
    -   Check if `intervals[i].end > intervals[i+1].start`.
    -   If true -> return `false` (overlap detected).
3.  Return `true`.

---

## 4. 💻 Implementation (程式碼)

### Approach: Sort & Scan

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        if (intervals.empty()) return true;

        // 1. Sort by start time
        sort(intervals.begin(), intervals.end());

        // 2. Check overlap between adjacent intervals
        for (int i = 0; i < intervals.size() - 1; i++) {
            // Overlap condition: Current meeting ends AFTER next meeting starts
            if (intervals[i][1] > intervals[i+1][0]) {
                return false;
            }
        }

        return true;
    }
};
```

### Python Reference

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i: i[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False

        return True
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        // 邊界情況：沒有會議或只有一個會議，當然可以參加
        if (intervals.empty()) return true;

        // 步驟 1: 根據開始時間排序
        // 這樣我們只需要比較相鄰的會議
        sort(intervals.begin(), intervals.end());

        // 步驟 2: 遍歷檢查
        for (int i = 0; i < intervals.size() - 1; i++) {
            // 前一個會議的結束時間 (intervals[i][1])
            // 下一個會議的開始時間 (intervals[i+1][0])
            // 如果 前一個結束 > 下一個開始，代表時間重疊
            if (intervals[i][1] > intervals[i+1][0]) {
                return false; // 無法參加所有會議
            }
        }

        // 如果都沒有重疊，則可以參加
        return true;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \log N)$
    -   Sorting dominates the complexity.
-   **Space Complexity**: $O(1)$ or $O(\log N)$
    -   Sorting space.
