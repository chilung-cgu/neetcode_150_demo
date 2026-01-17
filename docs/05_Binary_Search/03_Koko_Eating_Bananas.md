# Koko Eating Bananas (Koko 吃香蕉)

## 1. 🧐 Problem Dissection (釐清問題)

Koko 愛吃香蕉。這裡有 `n` 串香蕉 (`piles`)，第 `i` 串有 `piles[i]` 根。
警衛離開了 `h` 小時。
Koko 每小時可以選擇一串香蕉吃掉 `k` 根（如果那串少於 `k` 根，她就全吃掉，這小時剩下的時間也不會去吃別串）。
請問最小的整數 `k` 是多少，才能讓她在 `h` 小時內吃完所有香蕉？

-   **Input**: `piles = [3,6,7,11], h = 8`
-   **Output**: `4`
    -   如果 k=4：
    -   `3` -> 1 hr (eat 3)
    -   `6` -> 2 hrs (4, then 2)
    -   `7` -> 2 hrs (4, then 3)
    -   `11` -> 3 hrs (4, 4, then 3)
    -   Total: 1+2+2+3 = 8 hrs. OK.
-   **Key Insight**:
    -   如果 Koko 吃超快 (k = very large)，肯定吃得完，但我們想求**最小**的 k。
    -   如果 Koko 吃超慢 (k = 1)，可能吃不完。
    -   這是一個典型的 **Binary Search on Answer** 問題。

-   **Constraints**:
    -   $1 <= piles.length <= 10^4$.
    -   `piles.length <= h <= 10^9`. (Time limit is huge, but `h >= piles.length` guarantees solvability).

---

## 2. 🐢 Brute Force Approach (暴力解)

從 `k=1` 開始嘗試，直到找到第一個滿足條件的 `k`。

-   對於每個 `k`，我們需要遍歷 `piles` 計算總時間。
-   計算時間：`time = ceil(pile / k)`。
-   假設最大堆大概是 `maxP`。
-   **Time**: $O(maxP \cdot n)$。如果 `maxP` 是 $10^9$ and `n` 是 $10^4$，那會超時。

---

## 3. 💡 The "Aha!" Moment (優化)

我們發現 `k` 與「所需時間」成反比。
`k` 越大，所需時間越少。
這是單調的。所以我們可以對 `k` 進行 **二分搜尋**。

**搜尋範圍**:

-   `Low`: 1 (最慢速度)。
-   `High`: `max(piles)` (最快速度，也就是一小時吃掉最大的一串，再快也沒意義因為一小時只能吃一串)。

**Binary Search**:

-   `mid = (low + high) / 2`。
-   計算如果速度是 `mid`，需要多少小時 `hours`。
-   如果 `hours <= h` (吃得完)：`mid` 可能是答案，但也許我們可以吃更慢一點？ -> `result = mid`, `high = mid - 1`。
-   如果 `hours > h` (吃不完)：`mid` 太慢了！ -> `low = mid + 1`。

**Hours Calculation**:
`hours = sum(ceil(pile / k))`
`ceil(x/y)` 可以寫成 `(x + y - 1) / y` (Integer arithmetic trick).

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../koko_bananas_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../koko_bananas_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Binary Search on Answer

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        // 找到最大堆作為上限
        int right = 0;
        for (int p : piles) right = max(right, p);

        int res = right; // 初始化為最大值，確保有解

        while (left <= right) {
            int k = left + (right - left) / 2;

            // 計算以速度 k 需要多少小時
            long long hours = 0;
            for (int p : piles) {
                // ceil(p / k)
                hours += (p + k - 1) / k;
            }

            if (hours <= h) {
                // 吃得完，嘗試更慢的速度
                res = k;
                right = k - 1;
            } else {
                // 吃不完，需要更快的速度
                left = k + 1;
            }
        }

        return res;
    }
};
```

### Python Reference

```python
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        // 最大速度只需到 max(piles)。
        // 因為一小時只能吃一堆，就算速度比這一堆還多，你也只能吃完這一堆然後發呆。
        // 所以速度超過 max(piles) 並不會讓你吃更快 (時間數不會減少)。
        int r = 0;
        for (int p : piles) r = max(r, p);

        int result = r;

        while (l <= r) {
            int k = l + (r - l) / 2;

            // 計算總時數
            long long totalTime = 0; // 防止溢位，雖然 h <= 10^9 int 夠，但保險
            for (int p : piles) {
                // 向上取整的整數運算技巧： (a + b - 1) / b 等同於 ceil(a/b)
                totalTime += ((long long)p + k - 1) / k;
            }

            // 檢查是否滿足條件
            if (totalTime <= h) {
                // 可以在 h 小時內吃完 -> 這是一個可能的解
                // 但我們想找「最小」速度，所以嘗試往左找
                result = k;
                r = k - 1;
            } else {
                // 超時了 -> 速度太慢，往右找更快的
                l = k + 1;
            }
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n \cdot \log(\max(P)))$
    -   我們對速度 `k` 進行二分搜尋，範圍是 $1 \dots \max(P)$。這需要 $\log(\max(P))$ 次迭代。
    -   每次迭代，我們需要遍歷 `piles` 來計算時間，花費 $O(n)$。
    -   所以是 $O(n \log(\max(P)))$。
-   **Space Complexity**: $O(1)$
    -   只使用常數變數。
