---
title: "Gas Station (加油站)"
description: "圓形路線上有 `n` 個加油站。 `gas[i]`：第 `i` 個加油站有的油量。 `cost[i]`：從第 `i` 個站開到第 `i+1` 個站需要消耗的油量。 油箱容量是無限的。 從其中一個加油站出發，是否能繞一圈回到起點？ 如果可以，回傳起點的 index（保證唯一）。如果不可以，回傳 -1。"
tags:
  - Greedy
difficulty: Medium
---

# Gas Station (加油站) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #134** — [題目連結](https://leetcode.com/problems/gas-station/) | [NeetCode 解說](https://neetcode.io/problems/gas-station)


## 1. 🧐 Problem Dissection (釐清問題)

圓形路線上有 `n` 個加油站。
`gas[i]`：第 `i` 個加油站有的油量。
`cost[i]`：從第 `i` 個站開到第 `i+1` 個站需要消耗的油量。
油箱容量是無限的。
從其中一個加油站出發，是否能繞一圈回到起點？
如果可以，回傳起點的 index（保證唯一）。如果不可以，回傳 -1。

-   **Input**: `gas = [1,2,3,4,5], cost = [3,4,5,1,2]`
-   **Output**: `3`
    -   Start 3 (gas 4). Next need 1. Current tank = 4 - 1 + 5 = 8.
    -   And so on.
-   **Input**: `gas = [2,3,4], cost = [3,4,3]`
-   **Output**: `-1`
-   **Constraints**:
    -   $n == gas.length == cost.length$
    -   $1 <= n <= 10^5$

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試以每一個站作為起點。
`check(start)`: 模擬開一圈。

-   **Time**: $O(N^2)$。 TLE for $10^5$.

---

## 3. 💡 The "Aha!" Moment (優化)

**Key Insight 1**:
如果所有 `gas` 的總和 < 所有 `cost` 的總和，那麼絕對不可能跑完一圈。直接回傳 -1。

**Key Insight 2**:
如果總油量 >= 總消耗，那麼**一定有解**（題目也暗示解唯一）。

**Greedy Strategy**:
我們嘗試從 `start = 0` 開始，並維護 `total_tank` (累積的淨剩餘油量)。
如果在到達某個站 `i` 時，`current_tank < 0`，這意味著：
**從 `start` 到 `i` 之間的所有站點，都不可能作為起點。**
為什麼？
因為到達 `i` 時油變負了。如果在 `start` 和 `i` 之間選一個 `k` 作為起點，那麼從 `start` 到 `k` 的累積油量一定是正的（否則在 `k` 之前就已經斷了）。
既然 `start` -> `i` 是負的，而 `start` -> `k` 是正的，那 `k` -> `i` 一定是更負的！
所以，我們只能選擇 `i + 1` 作為新的起點。

因此：
遍歷一次。如果 `current_tank` 變負，重置為 0，並將起點設為下一個點。
只要總和非負，最後找到的那個起點就是答案。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../gas_station_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../gas_station_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy (One Pass)

```cpp
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        long long totalGas = 0;
        long long totalCost = 0;

        // 1. Check if solution exists
        for (int i = 0; i < gas.size(); i++) {
            totalGas += gas[i];
            totalCost += cost[i];
        }

        if (totalGas < totalCost) return -1;

        // 2. Find start position
        int start = 0;
        long long currentTank = 0;

        for (int i = 0; i < gas.size(); i++) {
            currentTank += (gas[i] - cost[i]);

            // If tank drops below 0, it means we cannot reach i from 'start'
            // Furthermore, no station between 'start' and 'i' can be a valid start
            // So we try starting from i + 1
            if (currentTank < 0) {
                start = i + 1;
                currentTank = 0;
            }
        }

        return start;
    }
};
```

### Python Reference

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start = i + 1

        return start
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        long long totalGas = 0;
        long long totalCost = 0;

        // 先計算總油量和總消耗，如果總油量不足，直接回傳 -1
        // (也可以在一個迴圈內做，但分開寫更清晰)
        for (int x : gas) totalGas += x;
        for (int x : cost) totalCost += x;

        if (totalGas < totalCost) return -1;

        // 既然總油量足夠，那一定有解 (題目保證唯一解)
        // 使用 Greedy 找起點
        int start = 0;
        long long currentTank = 0;

        for (int i = 0; i < gas.size(); i++) {
            // 累加當前的淨油量 (gas - cost)
            currentTank += (gas[i] - cost[i]);

            // 如果開到這裡油箱變負的了
            // 說明從目前的 start 到 i 這是不可行的
            // 而且 start 到 i 中間的任一點也不可能作為起點 (因為 start 到它們累積是正的，扣掉正的會更慘)
            // 所以直接嘗試從 i + 1 開始
            if (currentTank < 0) {
                start = i + 1;
                currentTank = 0;
            }
        }

        // 為什麼不需要檢查 start 是否跑完整圈？
        // 因為前面的總和检查保證了 total sum >= 0。
        // 如果我們找到了唯一的有效區間 [start, n-1]，使得這個區間 sum >= 0，
        // 那麼剩下的 [0, start-1] 區間的 sum 雖然是負的，但 [start, n-1] 的正值一定足夠彌補它 (因為 total >= 0)。
        return start;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Single pass.
-   **Space Complexity**: $O(1)$
    -   No extra space.

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
