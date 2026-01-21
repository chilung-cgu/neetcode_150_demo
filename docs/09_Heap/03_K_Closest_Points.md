# K Closest Points to Origin (最接近原點的 K 個點) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #973** — [題目連結](https://leetcode.com/problems/k-closest-points-to-origin/) | [NeetCode 解說](https://neetcode.io/problems/k-closest-points-to-origin)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個點座標陣列 `points`，其中 `points[i] = [xi, yi]`，以及一個整數 `k`。
請回傳距離原點 `(0, 0)` 最近的 `k` 個點。
距離使用 **Euclidean Distance** (歐幾里得距離)：$\sqrt{x^2 + y^2}$。
因為只需要比較大小，不需要開根號，直接比較 $x^2 + y^2$ 即可。

-   **Input**: `points = [[1,3],[-2,2]], k = 1`
    -   Dist([1,3]) = $1^2 + 3^2 = 10$.
    -   Dist([-2,2]) = $(-2)^2 + 2^2 = 8$.
    -   8 < 10, so `[-2,2]` is closer.
-   **Output**: `[[-2,2]]`
-   **Input**: `points = [[3,3],[5,-1],[-2,4]], k = 2`
    -   Dist([3,3]) = 18
    -   Dist([5,-1]) = 26
    -   Dist([-2,4]) = 20
    -   Closest 2: 18 and 20.
-   **Output**: `[[3,3],[-2,4]]`
-   **Constraints**:
    -   $1 <= k <= points.length <= 10^4$
    -   $-10^4 < x_i, y_i < 10^4$

---

## 2. 🐢 Brute Force Approach (暴力解)

計算所有點到原點的距離，然後排序。取前 `k` 個。

-   Sort: $O(N \log N)$.
-   Space: $O(N)$ (to store distances or sorted copy).

---

## 3. 💡 The "Aha!" Moment (優化)

這又是典型的 **Top K** 問題。
有兩種主要解法：

**Approach 1: Max-Heap (大頂堆)**
維護一個大小為 `k` 的 Max-Heap，存放目前為止「最近」的 k 個點的距離。
Max-Heap 的頂端是這 k 個點中「最遠」的那個。
當遇到一個新點，如果它的距離比 Heap Top 還小，代表它比目前第 k 近的點還要近，所以把 Heap Top 踢掉，換新點進去。

-   **Time**: $O(N \log k)$. (Better than sort if $k \ll N$)

**Approach 2: Quick Select (Hoare's Selection Algorithm)**
類似 QuickSort，我們選一個 pivot，把小於 pivot 的放左邊，大於 pivot 的放右邊。
如果 pivot 剛好在 index `k`，那左邊的就是前 k 個。
平均時間複雜度 $O(N)$，最壞 $O(N^2)$。 (標準函式庫 `std::nth_element` 就是用這個)。

這題 $N$ 是 $10^4$，Heap $O(N \log k)$ 很穩。Quick Select 跟面試官討論後通常可以加分，但寫起來比較繁瑣。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../k_closest_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../k_closest_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Max-Heap (Standard Top-K)

```cpp
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Max-Heap: store pair<distance_squared, index>
        priority_queue<pair<long, int>> pq;

        for (int i = 0; i < points.size(); i++) {
            long dist = (long)points[i][0] * points[i][0] + (long)points[i][1] * points[i][1];

            pq.push({dist, i});

            if (pq.size() > k) {
                pq.pop();
            }
        }

        vector<vector<int>> result;
        while (!pq.empty()) {
            int idx = pq.top().second;
            result.push_back(points[idx]);
            pq.pop();
        }

        return result;
    }
};
```

### Approach: Quick Select (Optimized)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // std::nth_element partial sorts the range such that
        // the element at the nth position is the one that would be in that position
        // if the range was fully sorted.
        // All elements before it are <= to it.

        auto dist = [](const vector<int>& p) {
            return p[0] * p[0] + p[1] * p[1];
        };

        nth_element(points.begin(), points.begin() + k, points.end(),
            [&](const vector<int>& a, const vector<int>& b) {
                return dist(a) < dist(b);
            });

        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
};
```

### Python Reference (Min-Heap based N smallest)

```python
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res

    # Or using nsmallest
    # return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // 使用 Max-Heap 來維護前 K 個最小距離的點
        // C++ 預設 priority_queue 是 Max-Heap
        // 內容物是 pair<距離平方, 在原陣列的index>
        priority_queue<pair<long long, int>> maxHeap;

        for (int i = 0; i < points.size(); i++) {
            long long x = points[i][0];
            long long y = points[i][1];
            long long dist = x*x + y*y;

            // 將當前點加入堆
            maxHeap.push({dist, i});

            // 如果堆的大小超過 K，代表我們存了 K+1 個點
            // 因為是 Max-Heap，堆頂是這 K+1 個點中「距離最遠」的
            // 我們把最遠的踢掉，剩下的就是比較近的 K 個
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }

        // 將堆中的結果轉成答案 vector
        vector<vector<int>> result;
        while (!maxHeap.empty()) {
            int index = maxHeap.top().second;
            result.push_back(points[index]);
            maxHeap.pop();
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

**Using Max-Heap**:

-   **Time Complexity**: $O(N \log k)$
    -   We iterate through $N$ points.
    -   Each push/pop operation on a heap of size $k$ takes $O(\log k)$.
-   **Space Complexity**: $O(k)$
    -   Heap stores $k$ elements.

**Using Quick Select (`nth_element`)**:

-   **Time Complexity**: $O(N)$ average, $O(N^2)$ worst case.
-   **Space Complexity**: $O(1)$ (in-place) or $O(\log N)$ (stack).

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
- [Kth Largest Element in an Array (陣列中的第 K 大元素)](04_Kth_Largest_Element_Array.md)
