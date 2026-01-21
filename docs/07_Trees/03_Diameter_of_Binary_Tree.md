---
title: "Diameter of Binary Tree (二元樹的直徑)"
description: "題目求二元樹的 **直徑**。直徑是指樹中 **任意兩個節點** 之間的最長路徑長度（邊的數量）。 這條路徑 **不一定經過 root**。"
tags:
  - 
Tree  - Binary Tree  - DFS
difficulty: Easy
---

# Diameter of Binary Tree (二元樹的直徑) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #543** — [題目連結](https://leetcode.com/problems/diameter-of-binary-tree/) | [NeetCode 解說](https://neetcode.io/problems/diameter-of-binary-tree)


## 1. 🧐 Problem Dissection (釐清問題)

題目求二元樹的 **直徑**。直徑是指樹中 **任意兩個節點** 之間的最長路徑長度（邊的數量）。
這條路徑 **不一定經過 root**。

-   **Input**:
    ```
          1
         / \
        2   3
       / \
      4   5
    ```

-   **Output**: 3 (Path: 4-2-1-3 or 5-2-1-3)
-   **Input**: `root = [1,2]`
-   **Output**: 1 (Path: 2-1)
-   **Constraints**:
    -   $1 <= nodes <= 10^4$
    -   $-100 <= Node.val <= 100$

---

## 2. 🐢 Brute Force Approach (暴力解)

對於樹中的每一個節點，假設該節點是「轉折點」(Highest Node of the path)，計算經過該節點的最長路徑：
`Left Height + Right Height`。
遍歷所有節點，取最大值。
`Height` 需要 $O(N)$ 計算。

-   **Time**: $O(N^2)$ (如果樹不平衡)。
-   **Result**: 效率可以再優化。

---

## 3. 💡 The "Aha!" Moment (優化)

不需要分開計算 Height。我們可以在計算 Height 的過程中，順便計算 Diameter。
這是一個 **Bottom-up DFS**。

對於任意節點 `curr`：

1.  遞迴取得左子樹的高度 `LH`。
2.  遞迴取得右子樹的高度 `RH`。
3.  經過 `curr` 的最長路徑長度是 `LH + RH`。用這值去更新全域的 `maxDiameter`。
4.  回傳給父節點這棵子樹的高度：`1 + max(LH, RH)`。

這樣只需要一次 DFS 就能算完。

**Height Definition**:

-   Null node: 0 (or -1 depending on edge vs node counting, problem says "length of path between two nodes" which is edge count. So height of leaf is 0? No, let's use standard height: null is 0, leaf is 1. Then edge path length is `LH + RH` directly).
-   Example:
    -   Node 4 (leaf): L=0, R=0. Path=0. Return 1.
    -   Node 5 (leaf): L=0, R=0. Path=0. Return 1.
    -   Node 2: L=1, R=1. Path=1+1=2 (Edges involved: 4-2, 2-5). Return 1+1=2.
    -   Node 3: L=0, R=0. Path=0. Return 1.
    -   Node 1: L=2, R=1. Path=2+1=3. Return 3.
-   Result Match!

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../diameter_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../diameter_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive DFS (Bottom-up)

```cpp
#include <algorithm>
#include <iostream>

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
private:
    int diameter;

    // 回傳該子樹的高度 (Max depth)
    int height(TreeNode* node) {
        if (!node) return 0;

        int leftHeight = height(node->left);
        int rightHeight = height(node->right);

        // 更新全局最大直徑
        // 經過這個 node 的路徑長度 = 左高 + 右高
        // (注意：这里的 Height 是以 node 數計算的，null 是 0，leaf 是 1)
        // 路徑長度 (edges) 正好等於 (leftHeight nodes) + (rightHeight nodes)
        // 例如 leaf: 0+0=0 edges.
        // Node [2,4,5]: left 1, right 1 => 2 edges (4->2->5).
        diameter = max(diameter, leftHeight + rightHeight);

        // 回傳给 parent 的是高度
        return 1 + max(leftHeight, rightHeight);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        diameter = 0;
        height(root);
        return diameter;
    }
};
```

### Python Reference

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
    int maxD = 0; // 用來記錄遍歷過程中的最大直徑

    // DFS 函數：計算深度，並在過程中更新直徑
    int dfs(TreeNode* root) {
        if (root == nullptr) {
            return 0; // 空節點高度為 0
        }

        int left = dfs(root->left);   // 左子樹高度
        int right = dfs(root->right); // 右子樹高度

        // 核心邏輯：
        // 經過 root 的最長路徑 = 左子樹高度 + 右子樹高度
        // 更新全域最大值
        maxD = max(maxD, left + right);

        // 返回給父節點的值：自己的高度
        return 1 + max(left, right);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        maxD = 0;
        dfs(root);
        return maxD;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   DFS 遍歷每個節點一次。
-   **Space Complexity**: $O(h)$
    -   Recursive stack depth.

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 路徑可以不經過 root 嗎？
- N-ary Tree?

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有理解直徑 = 左深度 + 右深度
- ⚠️ 忘記更新全域最大值

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 Bottom-up DFS
- 💎 清晰的 DFS 返回值設計

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Maximum Depth of Binary Tree (二元樹的最大深度)](02_Maximum_Depth_of_Binary_Tree.md)
- [Binary Tree Maximum Path Sum (二元樹中的最大路徑和)](14_Binary_Tree_Maximum_Path_Sum.md)
