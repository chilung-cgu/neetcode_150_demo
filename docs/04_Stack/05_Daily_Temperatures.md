---
title: "Daily Temperatures (每日溫度)"
description: "題目給一個整數陣列 `temperatures`，代表每天的氣溫。 請回傳一個陣列 `answer`，其中 `answer[i]` 代表「在第 `i` 天之後，要等幾天才能遇到**更高**的溫度」。 如果之後都沒有更高的溫度，填 `0`。"
tags:
  - 
Stack  - Monotonic Stack
difficulty: Medium
---

# Daily Temperatures (每日溫度) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #739** — [題目連結](https://leetcode.com/problems/daily-temperatures/) | [NeetCode 解說](https://neetcode.io/problems/daily-temperatures)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `temperatures`，代表每天的氣溫。
請回傳一個陣列 `answer`，其中 `answer[i]` 代表「在第 `i` 天之後，要等幾天才能遇到**更高**的溫度」。
如果之後都沒有更高的溫度，填 `0`。

-   **Input**: `temperatures = [73,74,75,71,69,72,76,73]`
-   **Output**: `[1,1,4,2,1,1,0,0]`
-   **Constraints**:
    -   $1 <= temperatures.length <= 10^5$.
    -   $30 <= temperatures[i] <= 100$.

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一天 `i`，往後遍歷 `j > i`，直到找到 `temp[j] > temp[i]`。

-   `answer[i] = j - i`.
-   **Time**: $O(n^2)$。
-   **Result**: TLE。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 **Monotonic Stack (單調堆疊)** 的經典應用。

想像我們在遍歷氣溫。有些日子（例如 `75` 度）在等待一個更高的溫度出現。
當我們遇到一個新溫度 `T` 時：

1.  如果 `T` 比之前的還低（例如 `71`）：那麼 `71` 無法解決 `75` 的等待，反而 `71` 也要開始等待。Push `71` 入棧。
2.  如果 `T` 比之前的還高（例如 `72`）：那麼 `72` 就是 `71` (還有 `69`) 的救星！
    -   `71` 等到了更高溫。計算等待天數，Pop `71`。
    -   但 `72` 比 `75` 小，所以 `75` 還在等。Push `72` 入棧。

**單調堆疊性質**：
Stack 裡儲存的 index 對應的溫度，一定是 **單調遞減** 的。
因為如果我們遇到了一個比 top 大的數，我們就會一直 Pop 直到它小於 top (或空)。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../daily_temperatures_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../daily_temperatures_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Monotonic Stack

```cpp
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> results(n, 0); // Initialize with 0
        stack<pair<int, int>> stk; // stores {temp, index}

        for (int i = 0; i < n; i++) {
            int t = temperatures[i];

            // 當前溫度 t 如果比 stack top 的溫度還高
            // 說明 stack top 的那一天等到了！
            while (!stk.empty() && t > stk.top().first) {
                int stackT = stk.top().first;
                int stackInd = stk.top().second;
                stk.pop();

                results[stackInd] = i - stackInd;
            }

            stk.push({t, i});
        }

        return results;
    }
};
```

### Python Reference

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> ans(n, 0);

        // Stack 存 index 即可，溫度可以查 array
        stack<int> indices;

        for (int i = 0; i < n; i++) {
            // While Stack 不為空，且當前溫度 > Stack Top 對應的溫度
            // 這意味著 Stack Top 那一天的「更高溫」終於出現了，就是現在 (i)！
            while (!indices.empty() && temperatures[i] > temperatures[indices.top()]) {
                int prevDay = indices.top();
                indices.pop();

                // 算出等待天數
                ans[prevDay] = i - prevDay;
            }

            // 當前這一天還沒找到更高溫，先入棧等待
            indices.push(i);
        }

        return ans;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   乍看有 double loop (`for` + `while`)，但注意 stack 操作。
    -   每個元素只會被 Push 進 Stack 一次。
    -   每個元素只會被 Pop 出 Stack 一次。
    -   總操作次數是 $2n$，所以是線性時間。
-   **Space Complexity**: $O(n)$
    -   在最壞情況下 (溫度嚴格遞減 `[100, 99, 98...]`)，所有元素都會留在 Stack 中直到最後。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- Next Greater Element II (circular)?
- 如何處理相等的溫度？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ Stack 儲存錯誤的資訊
- ⚠️ 單調性維護錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 Monotonic Decreasing Stack
- 💎 解釋為何從右到左也可行

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Car Fleet (車隊)](06_Car_Fleet.md)
- [Largest Rectangle in Histogram (直方圖中的最大矩形)](07_Largest_Rectangle_in_Histogram.md)

### 進階挑戰
- [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) — LeetCode
