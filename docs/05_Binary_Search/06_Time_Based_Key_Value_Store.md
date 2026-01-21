---
title: "Time Based Key-Value Store (基於時間的鍵值存儲)"
description: "設計一個 `TimeMap` 資料結構，支援以下操作："
tags:
  - 
Binary Search  - Array
difficulty: Medium
---

# Time Based Key-Value Store (基於時間的鍵值存儲) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #981** — [題目連結](https://leetcode.com/problems/time-based-key-value-store/) | [NeetCode 解說](https://neetcode.io/problems/time-based-key-value-store)


## 1. 🧐 Problem Dissection (釐清問題)

設計一個 `TimeMap` 資料結構，支援以下操作：

1.  `set(key, value, timestamp)`: 儲存 `key` 在 `timestamp` 的 `value`。
2.  `get(key, timestamp)`: 回傳 `key` 在 `timestamp` 時的 `value`。
    -   如果該時間點沒有對應的值，回傳 **小於等於** `timestamp` 的最大時間點的值 (prev_value)。
    -   如果所有時間點都比 `timestamp` 大，回傳空字串 `""`。

-   **Input**:
    -   `set("foo", "bar", 1)`
    -   `get("foo", 1)` -> "bar"
    -   `get("foo", 3)` -> "bar" (最接近 3 且 <= 3 的是 1)
    -   `set("foo", "bar2", 4)`
    -   `get("foo", 4)` -> "bar2"
    -   `get("foo", 5)` -> "bar2"
-   **Constraints**:
    -   `timestamp` 是嚴格遞增的 (for set operations)。這是一個非常重要的提示！
    -   $1 <= key.length, value.length <= 100$.
    -   All `set` timestamps are strictly increasing.

---

## 2. 🐢 Brute Force Approach (暴力解)

用一個 `HashMap<string, HashMap<int, string>>`。
對於 `get`，遍歷 inner map 的所有 keys 找最大的那個。

-   **Time**: $O(N)$ for get.
-   **Result**: 效率不夠好。

---

## 3. 💡 The "Aha!" Moment (優化)

因為 `set` 的 `timestamp` 是 **嚴格遞增** 的，所以對於每個 `key`，我們可以存一個 `vector<pair<int, string>>`，它裡面的時間戳自然就是 **Sorted** 的。

既然是 Sorted Array，找「小於等於 `timestamp` 的最大值」就是標準的 **Binary Search (Upper Bound)** 問題。

**Store Structure**:
`unordered_map<string, vector<pair<int, string>>> store;`

**Get Algorithm**:

1.  找到 `key` 對應的 `vector`。如果没有，return `""`。
2.  對 `vector` 進行二分搜尋。
    -   找 `target <= timestamp` 的最大值。
    -   這等價於找 `upper_bound(timestamp)` 的前一個元素，或者自己手寫 Binary Search。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../time_map_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../time_map_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Map + Binary Search

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class TimeMap {
private:
    // Key -> List of {Timestamp, Value}
    unordered_map<string, vector<pair<int, string>>> store;

public:
    TimeMap() {

    }

    void set(string key, string value, int timestamp) {
        store[key].push_back({timestamp, value});
    }

    string get(string key, int timestamp) {
        if (store.find(key) == store.end()) {
            return "";
        }

        // 取得該 key 的所有歷史紀錄 (已排序)
        const vector<pair<int, string>>& history = store[key];

        // Binary Search
        int left = 0;
        int right = history.size() - 1;
        string res = "";

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int time = history[mid].first;

            if (time <= timestamp) {
                // 這個時間點是合法的 (<= query time)
                // 我們先把這個值記下來，然後試試看有沒有更晚(更接近 timestamp)的
                res = history[mid].second;
                left = mid + 1;
            } else {
                // 這個時間點太晚了 (> query time)
                right = mid - 1;
            }
        }

        return res;
    }
};
```

### Python Reference

```python
class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [val, time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # Binary Search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class TimeMap {
private:
    // 使用 Hash Map 來儲存每個 key 的時間序列
    // 因為 set 的 timestamp 是遞增的，所以 vector 裡的 int 也是自動排序好的
    // pair<int, string> : <timestamp, value>
    unordered_map<string, vector<pair<int, string>>> m;

public:
    TimeMap() {}

    void set(string key, string value, int timestamp) {
        m[key].push_back({timestamp, value});
    }

    string get(string key, int timestamp) {
        // 如果 key 不存在，直接回傳空字串
        if (m.find(key) == m.end()) return "";

        const auto& vec = m[key];

        // 手寫 Binary Search 找 <= timestamp 的最大值
        // 也可以使用 std::upper_bound 然後往前減一格，但手寫比較直觀且易於解釋
        int l = 0;
        int r = vec.size() - 1;
        string res = "";

        while (l <= r) {
            int mid = l + (r - l) / 2;
            int t = vec[mid].first;

            if (t == timestamp) {
                return vec[mid].second; // 剛好命中
            } else if (t < timestamp) {
                // 找到一個比 query time 早的合法值
                // 記錄下來，並嘗試往右找看看有沒有更晚的
                res = vec[mid].second;
                l = mid + 1;
            } else {
                // 找到一個比 query time 晚的值，不合法
                r = mid - 1;
            }
        }

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**:
    -   `set`: $O(1)$ (Average for Map) + $O(1)$ (Push back).
    -   `get`: $O(1)$ (Map lookup) + $O(\log N)$ (Binary search), where $N$ is the number of entries for that key.
-   **Space Complexity**: $O(N)$
    -   儲存所有 set 進來的資料。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果需要支援刪除？
- 如何優化記憶體？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ Binary Search 找 upper_bound 錯誤
- ⚠️ 資料結構設計不當

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 討論 std::map 的 upper_bound 應用
- 💎 設計決策的解釋
