# Count Good Nodes in Binary Tree (計算二元樹中的好節點) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Binary Tree 的 root。
一個節點 X 被稱為 **Good** (好節點)，如果從根節點到 X 的路徑上，沒有任何節點的值 **大於** X 的值。
也就是說，X 必須是從 Root 到 X 路徑上的 **最大值** (或之一)。

-   **Input**: `root = [3,1,4,3,null,1,5]`
    ```
        3  (Good, max=3)
       / \
      1   4 (Good, max=4)
     /   / \
    3   1   5 (Good, max=5)
    (Good, max=3)  (Not Good, max=4 > 1)
    ```

-   **Output**: 4 (Nodes: 3, 3, 4, 5)
-   **Constraints**:
    -   $0 <= nodes <= 10^5$
    -   $-10^4 <= Node.val <= 10^4$

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每個節點，檢查它的所有祖先是否都小於等於它。
這需要記錄路徑，或者每個節點都往上找（如果能往上）。

-   **Time**: $O(N \times L)$，L 是平均深度。最壞 $O(N^2)$。
-   **Result**: 效率太差。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個 **Top-down DFS** 的經典應用。
我們從上往下走的時候，只要帶著「目前為止看到的最大值 (`maxVal`)」這個資訊傳給子節點即可。

對於任意節點 `curr`:

1.  如果 `curr->val >= maxVal`：
    -   這個節點是 **Good Node**。
    -   更新 `newMax = curr->val`。
2.  遞迴左子樹 `dfs(curr->left, newMax)`。
3.  遞迴右子樹 `dfs(curr->right, newMax)`。
4.  回傳 Good Nodes 的總數。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../count_good_nodes_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../count_good_nodes_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive DFS (Top-down)

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
public:
    int goodNodes(TreeNode* root) {
        if (!root) return 0;
        return dfs(root, root->val);
    }

private:
    int dfs(TreeNode* node, int maxSoFar) {
        if (!node) return 0;

        int count = 0;
        if (node->val >= maxSoFar) {
            count = 1;
            maxSoFar = node->val;
        }

        count += dfs(node->left, maxSoFar);
        count += dfs(node->right, maxSoFar);

        return count;
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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        // 初始時，maxSoFar 可以設為 INT_MIN，或者直接設為 root->val
        // 題目有 Constraints -10^4 <= val <= 10^4，所以用一個極小值也可以
        return dfs(root, INT_MIN);
    }

    // dfs 回傳子樹中 good nodes 的總數
    int dfs(TreeNode* node, int maxSoFar) {
        if (node == nullptr) {
            return 0;
        }

        int good = 0;
        // 檢查當前節點是否是 Good Node
        if (node->val >= maxSoFar) {
            good = 1;
            // 更新路徑上的最大值
            maxSoFar = node->val;
        }
        // 如果 node->val < maxSoFar，maxSoFar 保持不變

        // 累加左右子樹的結果
        good += dfs(node->left, maxSoFar);
        good += dfs(node->right, maxSoFar);

        return good;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   DFS 訪問每個節點一次。
-   **Space Complexity**: $O(h)$
    -   Recursion stack depth.
