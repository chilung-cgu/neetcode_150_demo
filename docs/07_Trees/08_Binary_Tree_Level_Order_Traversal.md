---
title: "Binary Tree Level Order Traversal (二元樹的層序遍歷)"
description: "題目給一個 Binary Tree 的 root。 請回傳其節點值的 **層序遍歷 (Level Order Traversal)**。 (i.e., from left to right, level by level)。"
tags:
  - Tree
  - Binary Tree
  - DFS
difficulty: Medium
---

# Binary Tree Level Order Traversal (二元樹的層序遍歷) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #102** — [題目連結](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [NeetCode 解說](https://neetcode.io/problems/level-order-traversal-of-binary-tree)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Binary Tree 的 root。
請回傳其節點值的 **層序遍歷 (Level Order Traversal)**。 (i.e., from left to right, level by level)。

-   **Input**: `root = [3,9,20,null,null,15,7]`
    ```
      3
     / \
    9  20
      /  \
     15   7
    ```

-   **Output**: `[[3],[9,20],[15,7]]`
-   **Input**: `root = [1]`
-   **Output**: `[[1]]`
-   **Input**: `root = []`
-   **Output**: `[]`
-   **Constraints**:
    -   $0 <= nodes <= 2000$
    -   $-1000 <= Node.val <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

這題本質就是 **BFS (Breadth-First Search)**。
所謂暴力解就是 DFS 並傳入 depth，然後把值加到對應 depth 的 vector 中。

-   **DFS Pre-order with Depth**:
    -   `vec[depth].push_back(node->val)`
    -   Recurse left/right with `depth + 1`.
-   這其實也很有效率，只是不是「直觀」的 Level Order (因為是先深後廣)。

---

## 3. 💡 The "Aha!" Moment (優化)

標準 **BFS (Queue)** 解法。
維護一個 Queue，初始時放入 root。
每一輪迴圈處理 **一層**：

1.  記下當前 queue 的大小 `len = q.size()`。這就是這一層的節點數。
2.  迴圈 `len` 次：
    -   Pop 節點。
    -   加入當前層的結果 list。
    -   將 children (Left, Right) Push 進 queue。
3.  將這一層的結果 list 加入最終答案。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../level_order_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../level_order_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative BFS (Queue)

```cpp
#include <vector>
#include <queue>

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel;

            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();

                currentLevel.push_back(node->val);

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            result.push_back(currentLevel);
        }

        return result;
    }
};
```

### Approach: Recursive DFS (Optional)

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        dfs(root, 0, result);
        return result;
    }

    void dfs(TreeNode* node, int depth, vector<vector<int>>& result) {
        if (!node) return;

        if (depth == result.size()) {
            result.push_back({});
        }

        result[depth].push_back(node->val);
        dfs(node->left, depth + 1, result);
        dfs(node->right, depth + 1, result);
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()

        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        // Edge case
        if (root == nullptr) return result;

        // 使用 Queue 進行 BFS
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            // 關鍵步驟：先記錄這一層有多少節點
            // 這樣我們可以一次處理完一整層，並把它們跟下一層的節點（剛加入的 children）區分開來
            int size = q.size();
            vector<int> level;

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                // 處理當前節點
                level.push_back(node->val);

                // 將子節點加入 Queue，成為 "下一層"
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            // 將這一層的結果存入總表
            result.push_back(level);
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   每個節點進出 Queue 一次。
-   **Space Complexity**: $O(n)$
    -   Queue 的最大長度是樹的最大寬度 (葉子節點層)，對於滿二元樹來說是 $n/2$。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- Zigzag Level Order?
- Bottom-up Level Order?

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ BFS 層次分離錯誤
- ⚠️ 沒有先記錄層大小

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 DFS 也能實現
- 💎 時間空間複雜度分析

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Binary Tree Right Side View (二元樹的右視圖)](09_Binary_Tree_Right_Side_View.md)

### 進階挑戰
- [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) — LeetCode
