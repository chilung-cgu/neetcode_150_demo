# Permutations (全排列) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #46** — [題目連結](https://leetcode.com/problems/permutations/) | [NeetCode 解說](https://neetcode.io/problems/permutations)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個**無重複**數字的陣列 `nums`。
回傳所有可能的 **排列 (Permutations)**。
順序不重要。

-   **Input**: `nums = [1,2,3]`
-   **Output**: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
-   **Input**: `nums = [0,1]`
-   **Output**: `[[0,1],[1,0]]`
-   **Constraints**:
    -   $1 <= nums.length <= 6$
    -   $-10 <= nums[i] <= 10$
    -   All integers are unique.

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
第一層選一個數字，剩下的 $n-1$ 個數字做全排列。

-   **Time**: $O(N! \times N)$。
-   $N=6$， $6! = 720$，非常小。

---

## 3. 💡 The "Aha!" Moment (優化)

這也是標準的 **Backtracking**。
我們可以維護一個 `visited` 陣列（或 set），表示哪些數字已經被選過了。

或者，使用 **Swap** 的方式：

-   在 `dfs(index)` 函數中，我們決定第 `index` 位置要放哪個數字。
-   我們可以將 `nums[index]` 與 `nums[i]` (其中 `i >= index`) 交換。
-   交換後遞迴 `dfs(index + 1)`。
-   Backtrack 時交換回來。
-   這種方法不需要額外的空間來存 `visited`。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../permutations_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../permutations_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking (Swap-based)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(nums, 0, result);
        return result;
    }

private:
    void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
        // Base case: 所有的位置都填滿了
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }

        for (int i = start; i < nums.size(); i++) {
            // Swap current element with start element
            swap(nums[start], nums[i]);

            // Recurse for the next index
            backtrack(nums, start + 1, result);

            // Backtrack (Swap back)
            swap(nums[start], nums[i]);
        }
    }
};
```

### Approach: Backtracking (Visited Set)

```cpp
#include <vector>
#include <vector>

using namespace std;

class Solution2 {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        vector<bool> visited(nums.size(), false);
        dfs(nums, visited, current, result);
        return result;
    }

    void dfs(vector<int>& nums, vector<bool>& visited, vector<int>& current, vector<vector<int>>& result) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                current.push_back(nums[i]);
                dfs(nums, visited, current, result);
                current.pop_back();
                visited[i] = false;
            }
        }
    }
};
```

### Python Reference

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]] # return copy

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)

            nums.append(n)

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        // 我們使用 swap 的方式，直接在原陣列上修改，節省空間
        // start 代表當前要決定的位置 (0 ~ n-1)
        solve(nums, 0, result);
        return result;
    }

    void solve(vector<int>& nums, int start, vector<vector<int>>& result) {
        // Base Case: start 到達陣列結尾，代表找到一個排列
        if (start == nums.size()) {
            result.push_back(nums); // 存入當前 nums 的狀態
            return;
        }

        // 嘗試將 index 'start' 之後的每一個數字放到 'start' 位置
        for (int i = start; i < nums.size(); i++) {
            // [Decision]: 讓 nums[i] 來到 nums[start] 的位置
            swap(nums[start], nums[i]);

            // [Recursion]: 決定下一個位置 (start + 1)
            solve(nums, start + 1, result);

            // [Backtrack]: 恢復交換，還原陣列狀態，以便下一輪迴圈嘗試別的數字
            swap(nums[start], nums[i]);
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \times N!)$
    -   總共有 $N!$ 個排列。
    -   每個排列複製到 result 需要 $O(N)$。
-   **Space Complexity**: $O(N)$
    -   Recursion stack depth.

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
- [Subsets II (子集 II)](04_Subsets_II.md)

### 進階挑戰
- [Permutations Ii](https://leetcode.com/problems/permutations-ii/) — LeetCode
