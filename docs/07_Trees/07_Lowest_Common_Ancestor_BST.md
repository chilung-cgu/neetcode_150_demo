# Lowest Common Ancestor of a BST (二元搜尋樹的最近共同祖先) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #235** — [題目連結](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [NeetCode 解說](https://neetcode.io/problems/lowest-common-ancestor-of-a-binary-search-tree)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 **Binary Search Tree (BST)**，以及兩個節點 `p` 和 `q`。
找出這兩個節點在 BST 中的 **最近共同祖先 (Lowest Common Ancestor, LCA)**。

LCA 定義：對於節點 T，如果 p 和 q 都在 T 的子樹中（或者 T 本身就是 p 或 q），且 T 的深度最大（離 root 最遠），則 T 為 LCA。

BST 性質：

-   Left child < Parent
-   Right child > Parent

-   **Input**: `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8`
-   **Output**: 6 (因為 2 < 6 < 8，分叉點在 6)
-   **Input**: `root = [6,2,8...], p = 2, q = 4`
-   **Output**: 2 (2 是 2 的祖先，也是 4 的祖先，LCA 是 2)
-   **Constraints**:
    -   $2 <= nodes <= 10^5$
    -   $-10^9 <= Node.val <= 10^9$
    -   All Node.val are unique.
    -   p != q.

---

## 2. 🐢 Brute Force Approach (暴力解)

這是 General Binary Tree 的解法：
遞迴遍歷。

-   如果 root == p 或 root == q，回傳 root。
-   左邊找 LCA，右邊找 LCA。
-   如果左右都有回傳值，代表 root 是分叉點 -> 也就是 LCA。
-   **Time**: $O(N)$。
-   **Result**: 有效，但沒利用到 BST 的性質。

---

## 3. 💡 The "Aha!" Moment (優化)

利用 **BST 的性質**：
假設當前節點是 `root`，目標是 `p` 和 `q`。

1.  如果 `p` 和 `q` 都比 `root` 小 (`p->val < root->val` && `q->val < root->val`)：
    -   LCA 一定在左子樹。我們往左走。
2.  如果 `p` 和 `q` 都比 `root` 大 (`p->val > root->val` && `q->val > root->val`)：
    -   LCA 一定在右子樹。我們往右走。
3.  否則 (一個比 root 大，一個比 root 小，或者其中一個就是 root)：
    -   **split point (分叉點)** 就在這裡！
    -   `root` 就是 LCA。

這是 $O(h)$ 的解法，比 $O(N)$ 快。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../lca_bst_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../lca_bst_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative (O(1) Space)

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* curr = root;

        while (curr) {
            if (p->val < curr->val && q->val < curr->val) {
                // p, q 都在左邊
                curr = curr->left;
            } else if (p->val > curr->val && q->val > curr->val) {
                // p, q 都在右邊
                curr = curr->right;
            } else {
                // 分叉點，或者 curr 就是 p 或 q
                return curr;
            }
        }

        return nullptr;
    }
};
```

### Approach: Recursive

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        return root;
    }
};
```

### Python Reference

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // 利用 BST 性質：左小右大
        // 我們從 root 開始往下找
        TreeNode* curr = root;

        while (curr != nullptr) {
            // Case 1: p 和 q 都比當前節點小 -> 它們一定都在左子樹
            if (p->val < curr->val && q->val < curr->val) {
                curr = curr->left;
            }
            // Case 2: p 和 q 都比當前節點大 -> 它們一定都在右子樹
            else if (p->val > curr->val && q->val > curr->val) {
                curr = curr->right;
            }
            // Case 3: 一大一小 (分叉)，或者其中一個等於 curr -> 找到了 LCA
            else {
                return curr;
            }
        }

        return nullptr;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(h)$
    -   我們只走單一路徑，高度為 $h$。
    -   對於 Balanced BST 是 $O(\log n)$，最壞情況 $O(n)$。
-   **Space Complexity**: $O(1)$
    -   Iterative 寫法不需要 stack。Recursive 是 $O(h)$。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 普通二元樹的 LCA？
- 有父指標的解法？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有利用 BST 性質
- ⚠️ 遞迴方向選擇錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 利用 BST 性質
- 💎 O(h) 迭代解法
