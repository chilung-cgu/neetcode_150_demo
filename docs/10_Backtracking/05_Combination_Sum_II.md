---
title: "Combination Sum II (組合總和 II)"
description: "題目給一個**可能包含重複數字**的陣列 `candidates` 和一個目標 `target`。 找出所有唯一組合，使得和為 `target`。 每個數字在每個組合中 **只能使用一次**。 解集 **不能包含重複的組合**。"
tags:
  - Backtracking
  - Recursion
difficulty: Medium
---

# Combination Sum II (組合總和 II) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #40** — [題目連結](https://leetcode.com/problems/combination-sum-ii/) | [NeetCode 解說](https://neetcode.io/problems/combination-target-sum-ii)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個**可能包含重複數字**的陣列 `candidates` 和一個目標 `target`。
找出所有唯一組合，使得和為 `target`。
每個數字在每個組合中 **只能使用一次**。
解集 **不能包含重複的組合**。

-   **Input**: `candidates = [10,1,2,7,6,1,5], target = 8`
    -   Sorted: `[1,1,2,5,6,7,10]`
    -   Process:
        -   `1` -> need 7. Next: `1` -> need 6. `6` -> ok. `[1,1,6]`
        -   `1` -> need 7. `2` -> need 5. `5` -> ok. `[1,2,5]`
        -   `1` -> need 7. `7` -> ok. `[1,7]`
        -   `2` -> need 6. `6` -> ok. `[2,6]`
    -   Note: `[1,7]` can come from first `1` or second `1`. We must avoid duplicate `[1,7]`.
-   **Output**: `[[1,1,6],[1,2,5],[1,7],[2,6]]`
-   **Constraints**:
    -   $1 <= candidates.length <= 100$
    -   $1 <= candidates[i] <= 50$
    -   $1 <= target <= 30$

---

## 2. 🐢 Brute Force Approach (暴力解)

Backtracking + Set 去重。

-   **Time**: $O(2^N \times N)$.
-   Space: $O(N)$ stack.

---

## 3. 💡 The "Aha!" Moment (優化)

這題結合了 **Combination Sum I** (找和為 target) 和 **Subsets II** (去重)。

核心邏輯：

1.  **Sort `candidates`**。
2.  **DFS Backtracking**:
    -   Decision: 選 `candidates[i]`，或不選。
    -   但因為我們用迴圈 `for i from index to end`，所以實際上是「選第 `i` 個當作下一個元素」。
3.  **重複處理**:
    -   在迴圈中，如果 `i > index` 且 `candidates[i] == candidates[i-1]`，則跳過 (Continue)。
    -   這代表「如果在同一層決策中，已經試過這個數值了，就不要再試一次」。

**Pruning**:

-   如果 `target - candidates[i] < 0`，因為已經排序，後面的數字更大，一定也不行。直接 `break` (比 continue 更優)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../combination_sum_ii_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../combination_sum_ii_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking (With Sorting & Pruning)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;

        sort(candidates.begin(), candidates.end());

        backtrack(candidates, target, 0, current, result);
        return result;
    }

private:
    void backtrack(vector<int>& candidates, int target, int start,
                   vector<int>& current, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            // Pruning: if current > target, no need to check further (since sorted)
            if (candidates[i] > target) {
                break;
            }

            // Skip duplicates in the same recursion level
            if (i > start && candidates[i] == candidates[i-1]) {
                continue;
            }

            current.push_back(candidates[i]);

            // Recurse with i + 1 because each element can only be used once
            backtrack(candidates, target - candidates[i], i + 1, current, result);

            current.pop_back();
        }
    }
};
```

### Python Reference

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue

                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()

                prev = candidates[i]

        backtrack([], 0, target)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> current;

        // 1. 必先排序，為了去重和剪枝
        sort(candidates.begin(), candidates.end());

        dfs(candidates, target, 0, current, res);
        return res;
    }

    void dfs(vector<int>& candidates, int target, int start, vector<int>& current, vector<vector<int>>& res) {
        // 找到目標
        if (target == 0) {
            res.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            // 剪枝：如果當前數字已經大於剩餘目標，後面的數字更大，一定也不行
            if (candidates[i] > target) {
                break;
            }

            // 去重：如果當前數字跟上一個一樣，且不是這一層的第一個選擇
            // (i > start 表示這是這一層 loop 的第 2+ 次迭代)
            // 那麼就跳過，因為同樣的數值在這一層已經被選過一次了
            if (i > start && candidates[i] == candidates[i-1]) {
                continue;
            }

            // 選擇
            current.push_back(candidates[i]);

            // 遞迴：注意這裡是 i + 1，因為每個數字只能用一次
            dfs(candidates, target - candidates[i], i + 1, current, res);

            // 回溯
            current.pop_back();
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(2^N)$
    -   In worst case (all elements sum up to target), we explore power set.
-   **Space Complexity**: $O(N)$
    -   Recursion stack.

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
- [Combination Sum (組合總和)](02_Combination_Sum.md)
