# Subsets II (子集 II) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個**可能包含重複數字**的整數陣列 `nums`。
回傳所有可能的 **唯一** 子集 (Power Set)。
解集 **不能包含重複的子集**。

-   **Input**: `nums = [1,2,2]`
    -   Subsets of `[1,2]` (first 2): `[], [1], [2], [1,2]`
    -   Add second 2:
        -   `[2]`, `[1,2]`, `[2,2]`, `[1,2,2]`
    -   Combined & Unique: `[[],[1],[1,2],[1,2,2],[2],[2,2]]`
-   **Output**: `[[],[1],[1,2],[1,2,2],[2],[2,2]]`
-   **Input**: `nums = [0]`
-   **Output**: `[[],[0]]`
-   **Constraints**:
    -   $1 <= nums.length <= 10$
    -   $-10 <= nums[i] <= 10$

---

## 2. 🐢 Brute Force Approach (暴力解)

用 `std::set<vector<int>>` 來自動去重。

-   先 Sort `nums` (確保子集裡的元素順序一致，以便 Set 去重)。
-   生成所有子集。
-   放入 Set。
-   轉回 Vector。
-   **Time**: $O(N \times 2^N \times \log(2^N))$. Set insertion adds complexity.

---

## 3. 💡 The "Aha!" Moment (優化)

不需要 Set，我們可以在生成過程中直接跳過重複的元素。

**前提**: `nums` 必須先 **Sort**。
`nums = [1, 2, 2]`

在 DFS 決策時：

-   **Include**: 正常選 `nums[i]`。
-   **Exclude** (`nums[i]`):
    -   如果我們決定 **不選** `nums[i]`，那麼緊接著的 `nums[i+1]` 如果跟 `nums[i]` 一樣，我們也 **不能選** `nums[i+1]`。
    -   因為如果選了 `nums[i+1]` 但沒選 `nums[i]` (且它們值一樣)，這跟「選了 `nums[i]` 但沒選 `nums[i+1]`」是一樣的結果（對於子集來說）。
    -   而「選了 `nums[i]` ...」這個分支我們在前面的 Include logic 已經做過了。

**Loop-based DFS**:
在 `for (int i = start; i < n; i++)` 迴圈中：

-   我們選 `nums[i]` 作為當前子集的新元素。
-   如果 `i > start` 且 `nums[i] == nums[i-1]`，代表這個數字已經在「同一層」被選過了，再選就會產生重複的子集開頭，所以 **continue**。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../subsets_ii_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../subsets_ii_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking (With Sorting & Loop Skip)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;

        // Sorting is crucial for handling duplicates
        sort(nums.begin(), nums.end());

        backtrack(nums, 0, current, result);
        return result;
    }

private:
    void backtrack(vector<int>& nums, int start, vector<int>& current, vector<vector<int>>& result) {
        // Every combination we reach is a valid subset
        result.push_back(current);

        for (int i = start; i < nums.size(); i++) {
            // Skip duplicates:
            // If current element is same as previous, and it's not the first element
            // in this particular recursive step (i > start), skip it.
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }

            // Include nums[i]
            current.push_back(nums[i]);

            // Recurse
            backtrack(nums, i + 1, current, result);

            // Backtrack
            current.pop_back();
        }
    }
};
```

### Python Reference

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # All subsets that don't include nums[i]
            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;

        // 1. 排序：讓重複的數字靠在一起
        sort(nums.begin(), nums.end());

        dfs(nums, 0, subset, res);
        return res;
    }

    // DFS / Backtracking
    void dfs(vector<int>& nums, int index, vector<int>& subset, vector<vector<int>>& res) {
        // 每次進到 DFS，當前的 subset 都是一個合法的子集 (包含空集合)
        res.push_back(subset);

        for (int i = index; i < nums.size(); i++) {
            // 2. 去重邏輯：
            // 如果當前數字 nums[i] 與上一個數字 nums[i-1] 相同，
            // 且這個數字不是我們這一輪迴圈遍歷的第一個數字 (i > index)，
            // 那麼就跳過它，因為以 nums[i-1] 開頭的所有子集已經在上一輪迴圈做過了。
            if (i > index && nums[i] == nums[i-1]) {
                continue;
            }

            // 選取 nums[i]
            subset.push_back(nums[i]);

            // 遞迴下一層
            dfs(nums, i + 1, subset, res);

            // Backtrack
            subset.pop_back();
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \times 2^N)$
    -   即使有重複，最壞情況下 (無重複) 也是 $2^N$ 個子集。
    -   Sorting $O(N \log N)$ 被 cover。
-   **Space Complexity**: $O(N)$
    -   Recursion stack.
