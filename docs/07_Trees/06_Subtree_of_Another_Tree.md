---
title: "Subtree of Another Tree (另一棵樹的子樹)"
description: "題目給兩棵 Binary Tree `root` 和 `subRoot`。 判斷 `subRoot` 是否是 `root` 的 **Subtree**。 Subtree 意味著：`root` 中的某個節點的所有後代結構与值都和 `subRoot` 完全相同。 (必須是完全 match，不能只是部分 "
tags:
  - Tree
  - Binary Tree
  - DFS
difficulty: Easy
---

# Subtree of Another Tree (另一棵樹的子樹) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #572** — [題目連結](https://leetcode.com/problems/subtree-of-another-tree/) | [NeetCode 解說](https://neetcode.io/problems/subtree-of-a-binary-tree)


## 1. 🧐 Problem Dissection (釐清問題)

題目給兩棵 Binary Tree `root` 和 `subRoot`。
判斷 `subRoot` 是否是 `root` 的 **Subtree**。
Subtree 意味著：`root` 中的某個節點的所有後代結構与值都和 `subRoot` 完全相同。
(必須是完全 match，不能只是部分 match)

-   **Input**:
    ```
    root: [3,4,5,1,2]     subRoot: [4,1,2]
         3                    4
        / \                  / \
       4   5                1   2
      / \
     1   2
    ```

-   **Output**: `true`
-   **Input**: `root = [3,4,5,1,2,null,null,null,null,0]`, `subRoot = [4,1,2]`
    (Node 2 has a child 0 in root, but Node 2 is leaf in subRoot)

-   **Output**: `false`
-   **Constraints**:
    -   $0 <= nodes <= 2000$
    -   $-10000 <= Node.val <= 10000$

---

## 2. 🐢 Brute Force Approach (暴力解)

利用我們剛剛寫好的 `isSameTree`。
遍歷 `root` 的每一個節點，檢查以該節點為根的子樹是否和 `subRoot` 相同。

-   **Time**: $O(m \times n)$。 `m` 是 `root` 節點數，`n` 是 `subRoot` 節點數。
-   **Result**: 這是最標準的解法，Given Constraints $N \le 2000$， $2000^2 = 4 \times 10^6$，是可以接受的。

---

## 3. 💡 The "Aha!" Moment (優化)

雖然 $O(MN)$ 可以過，但可以用 **Merkle Tree / Serialize (Hash)** 技巧優化到 $O(M+N)$。
不過這涉及字串處理或複雜的 Hash，面試中通常寫 $O(MN)$ 已經足夠好。

**Logic (DFS)**:
`isSubtree(root, subRoot)` is true IF:

1.  `subRoot` is null -> Always true (empty tree is subtree of any tree).
2.  `root` is null -> False (subRoot is not null).
3.  `isSameTree(root, subRoot)` is true.
4.  `isSubtree(root->left, subRoot)` is true.
5.  `isSubtree(root->right, subRoot)` is true.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../subtree_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../subtree_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Check Same Tree for Every Node

```cpp
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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!subRoot) return true; // Empty set is subset of any set
        if (!root) return false;   // subRoot not null but root is null

        // 1. Check if current trees are identical
        if (isSameTree(root, subRoot)) {
            return true;
        }

        // 2. Check if subRoot represents a subtree of left or right child
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

private:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        if (p->val != q->val) return false;

        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // Base Cases
        // 如果 subRoot 是空，它一定是任何樹的子樹
        if (subRoot == nullptr) return true;
        // 如果 root 已經空了 (但 subRoot 不空)，那就不可能是子樹
        if (root == nullptr) return false;

        // Step 1: 檢查「當前這棵樹」是否跟 subRoot 完全一樣
        if (isSameTree(root, subRoot)) {
            return true;
        }

        // Step 2: 如果不一樣，遞迴去 root 的左子樹和右子樹找看看
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

private:
    // 這是上一題的 Helper Function，判斷兩棵樹是否完全相同
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        if (p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   $M$ is `root` nodes, $N$ is `subRoot` nodes.
    -   對於 `root` 中的每一個節點，我們最多可能花 $O(N)$ 時間去檢查 `isSameTree`。
    -   如果樹是平衡的，或者 `subRoot` 很小，實際效能會接近 $O(M)$。
-   **Space Complexity**: $O(M)$
    -   DFS Stack Depth。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如何優化時間複雜度？
- 用序列化檢查？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ isSameTree 調用位置錯誤
- ⚠️ 沒有從每個節點開始檢查

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 Merkle Hash 優化
- 💎 KMP 串匹配優化

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Same Tree (相同的樹)](05_Same_Tree.md)
