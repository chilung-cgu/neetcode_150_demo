# Maximum Depth of Binary Tree (二元樹的最大深度) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #104** — [題目連結](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [NeetCode 解說](https://neetcode.io/problems/maximum-depth-of-binary-tree)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Binary Tree 的 root，求其最大深度。
最大深度是從 root 到最遠 leaf node 的路徑上的節點數。

-   **Input**: `root = [3,9,20,null,null,15,7]`
    ```
      3
     / \
    9  20
      /  \
     15   7
    ```

-   **Output**: 3
-   **Input**: `root = [1,null,2]`
-   **Output**: 2
-   **Constraints**:
    -   $0 <= nodes <= 10^4$
    -   $-100 <= Node.val <= 100$

---

## 2. 🐢 Brute Force Approach (暴力解)

DFS 走訪每條路徑，記錄最大值。

---

## 3. 💡 The "Aha!" Moment (優化)

這也是標準的 **Top-down** 或 **Bottom-up** 遞迴問題。

**Recursive DFS (Bottom-up)**:
對於一個節點，它的深度 = `1 + max(depth(left), depth(right))`。

-   Base Case: 如果節點是 `null`，深度為 0。
-   Recursive Step: 回傳 `1 + max(left_depth, right_depth)`。

**Iterative BFS (Level Order)**:
用 Queue。每遍歷完一層，深度 + 1。

-   **Time**: $O(n)$。
-   **Space**: $O(w)$ (max width of tree)。

**Iterative DFS (Stack)**:
用 Stack 存 pair `(node, depth)`。

-   每次 pop，更新 `res = max(res, depth)`。
-   Push children with `depth + 1`.

遞迴寫法最簡潔 (1-2 行)。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../max_depth_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../max_depth_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive DFS

```cpp
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
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

### Approach: Iterative BFS (Level Order)

```cpp
#include <queue>

using namespace std;

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        queue<TreeNode*> q;
        q.push(root);
        int depth = 0;

        while (!q.empty()) {
            int levelSize = q.size();

            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            depth++;
        }

        return depth;
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Base case: 碰到 null，深度為 0
        if (root == nullptr) {
            return 0;
        }

        // 遞迴計算左子樹深度
        int leftDepth = maxDepth(root->left);
        // 遞迴計算右子樹深度
        int rightDepth = maxDepth(root->right);

        // 當前節點的深度 = 1 (自己) + 左右子樹中較深的那個
        return 1 + max(leftDepth, rightDepth);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   必須訪問每個節點一次。
-   **Space Complexity**: $O(h)$
    -   Recursive Stack height. $O(n)$ worst case, $O(\log n)$ average.
