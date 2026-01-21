# Last Stone Weight (最後一顆石頭的重量) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #1046** — [題目連結](https://leetcode.com/problems/last-stone-weight/) | [NeetCode 解說](https://neetcode.io/problems/last-stone-weight)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `stones`，代表石頭的重量。
每一回合，我們選出 **最重的兩顆石頭**，設重量為 `x` 和 `y` (x <= y)。

-   如果 `x == y`: 兩顆石頭都銷毀。
-   如果 `x != y`: `x` 銷毀，`y` 的重量變為 `y - x`。
重複這個過程直到剩下一顆石頭或沒有石頭。
如果有剩，回傳它的重量；否則回傳 0。

-   **Input**: `stones = [2,7,4,1,8,1]`
-   **Process**:
    -   Max are 8 and 7. diff = 1. Remaining: `[2,4,1,1,1]`.
    -   Max are 4 and 2. diff = 2. Remaining: `[2,1,1,1]`.
    -   Max are 2 and 1. diff = 1. Remaining: `[1,1,1]`.
    -   Max are 1 and 1. diff = 0. Remaining: `[1]`.
-   **Output**: 1
-   **Constraints**:
    -   $1 <= stones.length <= 30$
    -   $1 <= stones[i] <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

每一輪都對陣列進行 Sorting，取出最後兩個（最大）。

-   Sorting: $O(N \log N)$.
-   Operation: $N$ times.
-   Total: $O(N^2 \log N)$.
因為 $N$ 只有 30，暴力解也能過，但不是最優。

---

## 3. 💡 The "Aha!" Moment (優化)

我們需要一直「快速取出最大值」並「放入新值」。
這就是 **Max-Heap (大頂堆)** 的標準使用場景。

**Algorithm**:

1.  把所有石頭放入 Max-Heap。
2.  當 Heap size > 1 時：
    -   Pop 出最大值 `y`。
    -   Pop 出次大值 `x`。
    -   如果 `x != y`，Push `y - x` 回 Heap。
3.  如果 Heap 為空，回傳 0；否則回傳 Top。

**Complexity**:

-   Build Heap: $O(N)$.
-   Pop/Push operations: $O(\log N)$. Loop $N$ times.
-   Total: $O(N \log N)$.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../last_stone_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../last_stone_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Max-Heap

```cpp
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // C++ priority_queue is Max-Heap by default
        priority_queue<int> pq(stones.begin(), stones.end());

        while (pq.size() > 1) {
            int y = pq.top();
            pq.pop();
            int x = pq.top();
            pq.pop();

            if (x != y) {
                pq.push(y - x);
            }
        }

        return pq.empty() ? 0 : pq.top();
    }
};
```

### Python Reference

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python uses Min-Heap, so we negate values to simulate Max-Heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)  # Largest (most negative)
            second = heapq.heappop(stones) # Second largest

            # first <= second (since they are negative)
            # abs(first) >= abs(second)
            # new weight = abs(first) - abs(second)
            # push -new_weight => push second - first
            if second > first:
                heapq.heappush(stones, first - second)

        if stones:
            return -stones[0]
        else:
            return 0
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // 1. 建立 Max-Heap (C++ 預設 priority_queue 即為大頂堆)
        // 初始建堆的時間複雜度為 O(N)
        priority_queue<int> pq(stones.begin(), stones.end());

        // 2. 模擬過程，直到剩下 1 顆或 0 顆石頭
        while (pq.size() > 1) {
            // 取出最重的兩顆石頭
            int y = pq.top(); pq.pop(); // 第一重的
            int x = pq.top(); pq.pop(); // 第二重的

            // 如果重量不同，剩下的碎塊重量放回堆中
            if (x != y) {
                pq.push(y - x);
            }
            // 如果重量相同，兩顆都消失，不需要 push 任何東西
        }

        // 3. 回傳結果
        if (pq.empty()) {
            return 0;
        } else {
            return pq.top();
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n \log n)$
    -   建堆 $O(n)$。
    -   每次操作 (pop 兩次 push 一次) 花費 $O(\log n)$。最多操作 $n$ 次。
-   **Space Complexity**: $O(n)$
    -   Priority Queue 存儲石頭。
