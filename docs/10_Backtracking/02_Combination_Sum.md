# Combination Sum (組合總和)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個**無重複**元素的整數陣列 `candidates` 和一個目標整數 `target`。
找出 `candidates` 中所有可以使數字和為 `target` 的唯一組合。
相同數字可以 **無限次** 重複使用。
解集不能包含重複的組合。

-   **Input**: `candidates = [2,3,6,7], target = 7`
-   **Output**: `[[2,2,3],[7]]`
    -   $2+2+3=7$
    -   $7=7$
-   **Input**: `candidates = [2,3,5], target = 8`
-   **Output**: `[[2,2,2,2],[2,3,3],[3,5]]`
-   **Constraints**:
    -   $1 <= candidates.length <= 30$
    -   $2 <= candidates[i] <= 40$
    -   $1 <= target <= 40$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Backtracking**:
對每個數字，我們可以選擇：

1.  選這個數字 (然後目標減去數字，繼續遞迴，**且因為可以重複選，index 不變**)。
2.  不選這個數字 (目標不變，**index + 1**)。

Base case:

-   `target == 0`: 找到一組解。
-   `target < 0` or `index` out of bounds: 失敗。

---

## 3. 💡 The "Aha!" Moment (優化)

這就是經典的 **Unbounded Knapsack** 變形，用 Backtracking 窮舉所有路徑。
決策樹：

-   Node: current target, current index.
-   Edges: Include `candidates[i]` OR Move to `candidates[i+1]`.

**Pruning (剪枝)**:

-   如果 `target < candidates[i]`，且 candidates 是 **sorted** 的，那後面的都不用看了 (因為都比當前大)。
-   這題 Constraints 很小 (target <= 40)，所以就算不 sorting，基本的 backtracking 也能過。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../combination_sum_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../combination_sum_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking (DFS)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        // Sorting helps in pruning earlier (optional)
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, current, result);
        return result;
    }

private:
    void dfs(vector<int>& candidates, int target, int index,
             vector<int>& current, vector<vector<int>>& result) {
        // Base case: Success
        if (target == 0) {
            result.push_back(current);
            return;
        }

        // Base case: Failure or Out of bounds
        if (target < 0 || index == candidates.size()) {
            return;
        }

        // Decision 1: Include candidates[index]
        // Only if it doesn't exceed target (Pruning)
        if (candidates[index] <= target) {
            current.push_back(candidates[index]);
            // Stay at same index because we can reuse the same element
            dfs(candidates, target - candidates[index], index, current, result);
            current.pop_back(); // Backtrack
        }

        // Decision 2: Exclude candidates[index] and move next
        // Skip current element and move to next unique element
        // (Though problem says candidates are unique, so just index + 1)
        dfs(candidates, target, index + 1, current, result);
    }
};
```

### Python Reference

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Decision 1: Include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Decision 2: Skip candidates[i]
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;

        // 遞迴搜索
        // start index 用來防止重複組合 (e.g. [2,3] 和 [3,2])
        // 因為我們每次遞迴只允許選擇 "當前 index 及之後" 的數字，不回頭選前面的
        backtrack(candidates, target, 0, path, res);
        return res;
    }

    void backtrack(vector<int>& candidates, int target, int start, vector<int>& path, vector<vector<int>>& res) {
        // 找到解
        if (target == 0) {
            res.push_back(path);
            return;
        }

        // 剪枝：如果 target < 0，這條路不通
        if (target < 0) return;

        for (int i = start; i < candidates.size(); i++) {
            // 選取 candidates[i]
            path.push_back(candidates[i]);

            // 關鍵：遞迴時傳入 'i' 而不是 'i+1'，代表可以重複使用當前數字
            // 但不能傳入 'start' 或 '0'，否則會產生重複組合 (Permutations)
            backtrack(candidates, target - candidates[i], i, path, res);

            // Backtrack
            path.pop_back();
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^{\frac{T}{M}})$
    -   $N$ is number of candidates.
    -   $T$ is target.
    -   $M$ is minimum value in candidates.
    -   Tree height is roughly $T/M$. Branching factor is $N$.
    -   This is an exponential upper bound.
-   **Space Complexity**: $O(T/M)$
    -   Recursion stack depth (longest possible combination).
