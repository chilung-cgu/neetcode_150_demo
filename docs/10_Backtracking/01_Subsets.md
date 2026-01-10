# Subsets (子集)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `nums`，其中的元素 **互不相同**。
請回傳該陣列的所有可能 **子集 (Power Set)**。
解集 **不能包含重複的子集**。

-   **Input**: `nums = [1,2,3]`
-   **Output**: `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`
-   **Input**: `nums = [0]`
-   **Output**: `[[],[0]]`
-   **Constraints**:
    -   $1 <= nums.length <= 10$
    -   $-10 <= nums[i] <= 10$
    -   All the numbers of `nums` are unique.

---

## 2. 🐢 Brute Force Approach (暴力解)

這題本身就是要窮舉所有子集，所有解法本質上都是 $O(2^N)$。
只差在實現方式（Backtracking vs Iterative/Bit Manipulation）。

---

## 3. 💡 The "Aha!" Moment (優化)

**Approach 1: Backtracking (DFS)**
對於每個元素，我們有兩個選擇：
1.  **包含它** (Include)。
2.  **不包含它** (Exclude)。
這構成了一棵二元決策樹。
-   決策樹深度為 $N$。
-   葉子節點數為 $2^N$。

**Approach 2: Cascading (Iterative)**
初始為 `[[]]`。
對每個新數字 `n`，把現有所有子集複製一份，並在複製的那份中加入 `n`。
-   Start: `[[]]`
-   Add 1: `[[], [1]]`
-   Add 2: `[[], [1], [2], [1,2]]`
-   Add 3: `[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]`

**Approach 3: Bit Manipulation**
$N \le 10$，可以用一個 bitmask `0` 到 `2^N - 1` 來代表每個子集。
`i`-th bit 為 1 代表選第 `i` 個數。

**DFS** 是面試中最通用的 Backtracking 模板。

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking (DFS)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        dfs(nums, 0, current, result);
        return result;
    }
    
private:
    void dfs(vector<int>& nums, int index, vector<int>& current, vector<vector<int>>& result) {
        // Base case: 遍歷完所有元素
        if (index == nums.size()) {
            result.push_back(current);
            return;
        }
        
        // Decision 1: Exclude nums[index] (Don't add it)
        // 直接跳到下一個 index
        dfs(nums, index + 1, current, result);
        
        // Decision 2: Include nums[index] (Add it)
        current.push_back(nums[index]);
        dfs(nums, index + 1, current, result);
        
        // Backtrack (Remove it to restore state for previous recursive call)
        current.pop_back();
    }
};
```

### Python Reference

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res; // 存放最終結果
        vector<int> curr;        // 存放當前子集
        
        // 從 index 0 開始遞迴
        dfs(nums, 0, curr, res);
        return res;
    }
    
    // DFS 函數：決定 index 位置的元素「選」還是「不選」
    void dfs(const vector<int>& nums, int index, vector<int>& curr, vector<vector<int>>& res) {
        // Base Case: 已經對每個元素都做過決定了
        if (index == nums.size()) {
            res.push_back(curr); // 把當前形成的子集加入結果
            return;
        }
        
        // 選項 1: 包含 nums[index]
        curr.push_back(nums[index]);
        dfs(nums, index + 1, curr, res);
        
        // Backtrack (回溯): 撤銷剛才的選擇，恢復狀態
        curr.pop_back();
        
        // 選項 2: 不包含 nums[index]
        dfs(nums, index + 1, curr, res);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \times 2^N)$
    -   總共有 $2^N$ 個子集。
    -   每個子集需要 $O(N)$ 的時間來複製/構建 (平均是 size/2)。
    -   更精確地說，複製總量是 $0 \times \binom{N}{0} + 1 \times \binom{N}{1} + \dots + N \times \binom{N}{N} = N 2^{N-1}$。
-   **Space Complexity**: $O(N)$
    -   Recursion stack depth $N$.
    -   (不包含 Output space $O(N \times 2^N)$).
