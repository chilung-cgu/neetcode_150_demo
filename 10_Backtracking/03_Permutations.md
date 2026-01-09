# Permutations (全排列)

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
