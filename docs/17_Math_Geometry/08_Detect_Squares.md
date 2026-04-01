---
title: "Detect Squares (檢測正方形)"
description: "你需要設計一個數據結構，支持以下兩個操作："
tags:
  - Math
  - Matrix
difficulty: Medium
---

# Detect Squares (檢測正方形) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #2013** — [題目連結](https://leetcode.com/problems/detect-squares/) | [NeetCode 解說](https://neetcode.io/problems/count-squares)


## 1. 🧐 Problem Dissection (釐清問題)

你需要設計一個數據結構，支持以下兩個操作：

1.  `add(point)`: 加入一個點 `(x, y)` 到數據結構中。點可以重複（視為不同的點）。
2.  `count(point)`: 給定一個查詢點 `(qx, qy)`，計算有多少個正方形可以由 `(qx, qy)` 以及數據結構中已有的三個點組成。且該正方形必須是 **軸對齊 (Axis-aligned)** 的（邊平行於 x 軸和 y 軸）。

-   **Input**:
    -   `add([3, 10])`
    -   `add([11, 2])`
    -   `add([3, 2])`
    -   `count([11, 10])`
-   **Output**: `1`
    -   Square: `(3, 10), (11, 10), (11, 2), (3, 2)`.
-   **Input**:
    -   `count([14, 8])` -> `0`
    -   `add([11, 2])` (Duplicate)
    -   `count([11, 10])` -> `2`

---

## 2. 🐢 Brute Force Approach (暴力解)

對於 `count(qx, qy)`，遍歷所有已存儲的點作為第二個點 `(x1, y1)`。

-   如果 `x1 == qx` 或 `y1 == qy`，這不能作為對角線點（如果它們在同一行或列，只能構成邊）。
-   如果 `abs(qx - x1) == abs(qy - y1)`，則這兩個點可以構成正方形的對角線。
-   然後檢查另外兩個點 `(qx, y1)` 和 `(x1, qy)` 是否存在。
-   如果存在，增加計數（乘上這兩個點出現的頻率）。

---

## 3. 💡 The "Aha!" Moment (優化)

**Hash Map for Frequency**:
我們需要快速查找某個點是否存在以及它的出現次數。
使用 `Map<String, Int>` 或者 `points[x][y] = count`。
由於坐標範圍是 $[0, 1000]$，我們可以使用二維數組或 Map。

**Algorithm**:

1.  `points` 存儲所有點的頻率。
2.  `savedPoints` 列表存儲所有添加過的點（為了遍歷）。
3.  `add(x, y)`:
    -   `cntPoints[x][y]++`。
    -   `savedPoints.add({x, y})`。
4.  `count(qx, qy)`:
    -   遍歷 `savedPoints` 中的每個點 `(x, y)`。
    -   **條件 1**: `abs(qx - x) == abs(qy - y)` (必須構成對角線，且是正方形)。
    -   **條件 2**: `x != qx` (面積不能為 0，避免自身)。
    -   如果滿足，則另外兩個點必然是 `(x, qy)` 和 `(qx, y)`。
    -   `res += cntPoints[x][y] * cntPoints[x][qy] * cntPoints[qx][y]`。
    -   注意：這裡 `cntPoints[x][y]` 用於乘法是因為如果數據結構中有多個相同的點，它們都能構成正方形。但在遍歷 `savedPoints` 時，我們其實是在遍歷每一個實體點。
    -   **修正**: 更好的做法是遍歷 **唯一的點的集合**，然後乘上該對角點的頻率。或者遍歷所有點（包括重複），然後只乘上另外兩個點的頻率。
    -   NeetCode 推薦：遍歷 `List` (所有點)。對於每個點 `P(x, y)`，如果它能和 `Q(qx, qy)` 構成對角線，那麼正方形數量增加 `count(x, qy) * count(qx, y)`。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../detect_squares_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../detect_squares_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Map Counting

```cpp
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

class DetectSquares {
public:
    DetectSquares() {

    }

    void add(vector<int> point) {
        int x = point[0];
        int y = point[1];
        pointCounts[x][y]++;
        points.push_back(point);
    }

    int count(vector<int> point) {
        int qx = point[0];
        int qy = point[1];
        int res = 0;

        for (const auto& p : points) {
            int x = p[0];
            int y = p[1];

            // Check if (x, y) can form a diagonal with (qx, qy)
            // Condition 1: Must not be the same point (area > 0)
            // Condition 2: |qx - x| == |qy - y| (Square property)
            if (abs(qx - x) != abs(qy - y) || x == qx) {
                continue;
            }

            // If valid diagonal, look for the other two corners:
            // (x, qy) and (qx, y)
            // We multiply their frequencies
            res += pointCounts[x][qy] * pointCounts[qx][y];
        }

        return res;
    }

private:
    // Using simple map or 2D array since constraints are small (0 <= x, y <= 1000)
    // A 1001x1001 array is efficient enough
    int pointCounts[1001][1001] = {0};
    vector<vector<int>> points;
};
```

### Python Reference

```python
class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point

        for x, y in self.pts:
            if (abs(qx - x) != abs(qy - y)) or x == qx:
                continue

            res += self.ptsCount[(x, qy)] * self.ptsCount[(qx, y)]

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class DetectSquares {
public:
    DetectSquares() {
        // 初始化，這裡不需要特別做什麼，因為我們使用固定大小的數組並初始化為 0
    }

    void add(vector<int> point) {
        int x = point[0];
        int y = point[1];
        // 記錄該坐標點的出現次數
        pointCounts[x][y]++;
        // 將該點加入列表，以便遍歷
        // 注意：這裡我們會存儲重複的點
        points.push_back(point);
    }

    int count(vector<int> point) {
        int qx = point[0];
        int qy = point[1];
        int res = 0;

        // 遍歷所有已存儲的點 (x, y)
        // 嘗試將 (x, y) 作為正方形的對角點
        for (const auto& p : points) {
            int x = p[0];
            int y = p[1];

            // 判斷是否為合法的對角點：
            // 1. |qx - x| == |qy - y|：確保長寬相等，即為正方形
            // 2. x != qx：確保不是同一個點，且邊長不為 0
            if (abs(qx - x) != abs(qy - y) || x == qx) {
                continue;
            }

            // 如果 (x, y) 是對角點，那麼另外兩個頂點必須是：
            // (x, qy) 和 (qx, y)
            // 正方形的數量等於這兩個點存在的次數之積
            // 注意：我們不需要乘上 (x, y) 的次數，因為我們正在遍歷 `points` 列表，
            // 列表中的每個 (x, y) 實體本身就代表了一次計數。
            res += pointCounts[x][qy] * pointCounts[qx][y];
        }

        return res;
    }

private:
    // 因為坐標範圍是 [0, 1000]，使用 2D 數組比 HashMap 更快且方便
    int pointCounts[1001][1001] = {0};
    vector<vector<int>> points;
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**:
    -   `add`: $O(1)$.
    -   `count`: $O(N)$, where $N$ is the number of points added so far.
-   **Space Complexity**: $O(N + 1000^2)$.
    -   $O(N)$ for the list of points.
    -   $O(1000^2)$ for the frequency grid (constant but large).

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
