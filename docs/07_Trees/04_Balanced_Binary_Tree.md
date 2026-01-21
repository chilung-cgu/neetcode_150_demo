# Balanced Binary Tree (平衡二元樹) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #110** — [題目連結](https://leetcode.com/problems/balanced-binary-tree/) | [NeetCode 解說](https://neetcode.io/problems/balanced-binary-tree)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Binary Tree，判斷它是否是 **高度平衡 (Height-Balanced)** 的。
**Height-Balanced**: 一個二元樹中，**每個節點** 的左右子樹的高度差絕對值不超過 1。

-   **Input**: `root = [3,9,20,null,null,15,7]`
    ```
      3
     / \
    9  20
      /  \
     15   7
    ```

-   **Output**: `true` (9 height 1, 20 height 2. Diff 1. Max balance OK.)
-   **Input**: `root = [1,2,2,3,3,null,null,4,4]`
    ```
           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    ```

-   **Output**: `false` (Node 1 left height 4, right height 1. Diff > 1)
-   **Constraints**:
    -   $0 <= nodes <= 5000$
    -   $-10000 <= Node.val <= 10000$

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每個節點 `root`，計算 `height(root->left)` 和 `height(root->right)`。
如果 `abs(left - right) > 1`，回傳 false。
否則遞迴檢查 `isBalanced(root->left)` 和 `isBalanced(root->right)`。

-   **Time**: $O(N^2)$。因為對於上層節點，計算 height 會重複訪問下層所有節點。
-   **Result**: 效率不佳。

---

## 3. 💡 The "Aha!" Moment (優化)

這也是一個 **Bottom-up DFS**。
我們可以修改 `height()` 函數，讓它不僅回傳高度，還能在發現 **不平衡** 時回傳一個特殊信號 (例如 -1)。

**Modified DFS**:

-   如果左子樹回傳 -1 (不平衡)，直接回傳 -1。
-   如果右子樹回傳 -1 (不平衡)，直接回傳 -1。
-   如果 `abs(left - right) > 1`，回傳 -1。
-   否則回傳 `1 + max(left, right)`。

最後在 `main` 函數檢查 `dfs(root) != -1`。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../balanced_tree_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../balanced_tree_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive DFS (Bottom-up with -1 flag)

```cpp
#include <algorithm>
#include <cmath>

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
public:
    bool isBalanced(TreeNode* root) {
        return dfsHeight(root) != -1;
    }

private:
    // Returns height of tree if balanced, -1 if unbalanced
    int dfsHeight(TreeNode* root) {
        if (!root) return 0;

        int leftHeight = dfsHeight(root->left);
        if (leftHeight == -1) return -1; // Propagate failure

        int rightHeight = dfsHeight(root->right);
        if (rightHeight == -1) return -1; // Propagate failure

        if (abs(leftHeight - rightHeight) > 1) {
            return -1; // Current node unbalanced
        }

        return 1 + max(leftHeight, rightHeight);
    }
};
```

### Python Reference

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        // 如果 dfsHeight 回傳 -1，代表發現不平衡
        return checkHeight(root) != -1;
    }

private:
    // Helper function:
    // 如果平衡，回傳高度 (>= 0)
    // 如果不平衡，回傳 -1
    int checkHeight(TreeNode* node) {
        if (node == nullptr) return 0;

        // Check Left Subtree
        int leftH = checkHeight(node->left);
        if (leftH == -1) return -1; // 提早結束

        // Check Right Subtree
        int rightH = checkHeight(node->right);
        if (rightH == -1) return -1; // 提早結束

        // Check Current Node
        if (abs(leftH - rightH) > 1) {
            return -1; // 當前節點不平衡
        }

        // 回傳高度
        return 1 + max(leftH, rightH);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   Bottom-up 每個節點只計算一次。
-   **Space Complexity**: $O(h)$
    -   Recursive stack depth.
