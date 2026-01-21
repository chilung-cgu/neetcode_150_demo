# Binary Tree Maximum Path Sum (二元樹中的最大路徑和) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 **非空** 二元樹的根節點 `root`。
找出 **最大路徑和**。
路徑可以從樹中的 **任意節點開始**，並在 **任意節點結束**（同一條路徑上的節點連接順序必須是父子關係）。
這條路徑 **至少包含一個節點**。
路徑不一定經過 root。

-   **Input**: `root = [1,2,3]`
    ```
      1
     / \
    2   3
    ```
    路徑: 2 -> 1 -> 3. Sum = 2+1+3 = 6.

-   **Output**: 6
-   **Input**: `root = [-10,9,20,null,null,15,7]`
    ```
       -10
       /  \
      9   20
         /  \
        15   7
    ```
    Max Path: 15 -> 20 -> 7. Sum = 15+20+7 = 42.
    (注意：如果包含 -10，則是 9 -> -10 -> 20 -> 15 (34) or 15 -> 20 -> -10 (25)，都沒有 42 大)

-   **Constraints**:
    -   $1 <= nodes <= 3 \times 10^4$
    -   $-1000 <= Node.val <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

對每個節點，計算經過它的最大路徑和。
這跟 Diameter 很像，但每個節點有權重（可能是負的）。

-   **Time**: $O(N^2)$。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 Diameter of Binary Tree 的加強版。
我們依然用 **Bottom-up DFS**。

對於任意一個節點 `curr`，有兩種「最大值」概念：

1.  **貢獻給父節點的最大單邊路徑和 (Max Branch Sum)**:
    -   必須包含 `curr`。
    -   可以包含 `curr` 的左子樹 max path，或者 `curr` 的右子樹 max path (只能選一邊，或者都不選)。
    -   `return curr->val + max(0, leftBranch, rightBranch)`。
    -   (如果不選 branch，就是只包含 `curr` 自己，因為 branch 可能為負)。
    2.  **以 `curr` 為轉折點的最大路徑和 (Max Path Sum through node)**:
    -   這是我們用來更新全域答案 (`globalMax`) 的候選值。
    -   這條路徑形狀是 `Left -> Curr -> Right`。
    -   Sum = `curr->val + max(0, leftBranch) + max(0, rightBranch)`。

注意 `max(0, ...)` 很重要，因為如果子樹路徑和是負的，我們寧願切斷它（不包含它）。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../max_path_sum_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../max_path_sum_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive DFS (Bottom-up)

```cpp
#include <climits>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    int globalMax;

public:
    int maxPathSum(TreeNode* root) {
        globalMax = INT_MIN;
        maxOutcome(root);
        return globalMax;
    }

private:
    // 回傳包含該 node 的最大單邊路徑和 (給父節點用)
    int maxOutcome(TreeNode* node) {
        if (!node) return 0;

        // 遞迴取得左右子樹的 Max Branch Sum
        // 如果是負的，我們就忽略 (取 0)，相當於切斷那條路
        int leftMax = max(maxOutcome(node->left), 0);
        int rightMax = max(maxOutcome(node->right), 0);

        // 更新 Global Max (以當前 node 為 "最高點" 的拱形路徑)
        // 路徑：Left Branch -> Node -> Right Branch
        int currentPathSum = node->val + leftMax + rightMax;
        globalMax = max(globalMax, currentPathSum);

        // 回傳給父節點：只能選一邊 (或者只選自己)
        return node->val + max(leftMax, rightMax);
    }
};
```

### Python Reference

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
    int maxScore = INT_MIN; // 全域最大值

public:
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return maxScore;
    }

    // DFS 函數：計算從 node 開始往下的「最大單邊路徑和」
    int dfs(TreeNode* node) {
        if (node == nullptr) return 0;

        // 1. 遞迴計算左子樹的最大單邊收益
        // 如果收益是負的，我們寧願不要這條路 (取 0)
        int leftGain = max(dfs(node->left), 0);

        // 2. 遞迴計算右子樹的最大單邊收益
        int rightGain = max(dfs(node->right), 0);

        // 3. 嘗試更新全域最大值
        // 這裡考慮的路徑是：左子樹 -> 當前節點 -> 右子樹
        // 這是一條完整的路徑 (以當前節點為頂點)
        int priceNewPath = node->val + leftGain + rightGain;
        maxScore = max(maxScore, priceNewPath);

        // 4. 回傳收益給父節點
        // 對於父節點來說，它只能選擇「當前節點 + 左邊」或者「當前節點 + 右邊」
        // 因為路徑不能分叉
        return node->val + max(leftGain, rightGain);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   每個節點遍歷一次。
-   **Space Complexity**: $O(h)$
    -   Recursion stack.
