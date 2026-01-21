# Kth Smallest Element in a BST (BST 中第 K 小的元素) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #230** — [題目連結](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [NeetCode 解說](https://neetcode.io/problems/kth-smallest-element-in-a-bst)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 BST 的 root 和一個整數 k。
請找出這棵樹中 **第 k 小** (1-indexed) 的元素值。

-   **Input**: `root = [3,1,4,null,2], k = 1`
    ```
       3
      / \
     1   4
      \
       2
    ```

-   **Output**: 1
-   **Input**: `root = [5,3,6,2,4,null,null,1], k = 3`
    ```
           5
          / \
         3   6
        / \
       2   4
      /
     1
    ```
    Sorted: 1, 2, 3, 4, 5, 6
    3rd smallest: 3

-   **Output**: 3
-   **Constraints**:
    -   $1 <= k <= n <= 10^4$
    -   $0 <= Node.val <= 10^4$

---

## 2. 🐢 Brute Force Approach (暴力解)

將所有節點數值存入一個 vector，然後 sort。

-   對於 BST，如果在存的時候用 In-order Traversal，就不需要 sort。
-   **Time**: $O(N)$ (Traversal) + $O(0)$ (Already sorted).
-   **Space**: $O(N)$ (Vector).

---

## 3. 💡 The "Aha!" Moment (優化)

不需要存所有的值。我們只需要在 **In-order Traversal** (Left -> Root -> Right) 的過程中計數。
每次訪問一個節點，`k--`。
當 `k == 0` 時，當前節點就是第 k 小的元素。回傳它並停止遍歷。

**Iterative Method**:
使用 Stack 模擬 Recursion，可以更早 return。

1.  一直往左走並 push stack。
2.  Pop stack (這是當前最小的)。
3.  `k--`。Check if `k == 0`.
4.  往右走一步 (`curr = curr->right`)。
5.  重複。

**Recursive Method**:
也可以，但需要一個 Global 變數或 Reference 變數來傳遞 k 和 result。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../kth_smallest_bst_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../kth_smallest_bst_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative In-order Traversal

```cpp
#include <stack>

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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> st;
        TreeNode* curr = root;

        while (curr || !st.empty()) {
            // 1. Go as left as possible
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }

            // 2. Process node (Backtrack)
            curr = st.top();
            st.pop();

            k--;
            if (k == 0) {
                return curr->val;
            }

            // 3. Go right
            curr = curr->right;
        }

        return -1; // Should not reach here
    }
};
```

### Approach: Recursive In-order

```cpp
class Solution {
    int result = -1;
    int count = 0;
public:
    int kthSmallest(TreeNode* root, int k) {
        traverse(root, k);
        return result;
    }

    // Return true if answer found (to stop recursion early)
    bool traverse(TreeNode* node, int k) {
        if (!node) return false;

        if (traverse(node->left, k)) return true;

        count++;
        if (count == k) {
            result = node->val;
            return true;
        }

        return traverse(node->right, k);
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        // 使用 Stack 模擬中序遍歷 (In-order Traversal)
        // 因為中序遍歷 BST 會得到由小到大的序列
        stack<TreeNode*> st;
        TreeNode* curr = root;

        while (curr != nullptr || !st.empty()) {
            // 步驟 1: 盡可能往左走，將沿途節點壓入 Stack
            while (curr != nullptr) {
                st.push(curr);
                curr = curr->left;
            }

            // 步驟 2: 取出 Stack 頂部節點 (這是當前未處理節點中的最小值)
            curr = st.top();
            st.pop();

            // 步驟 3: 這是第幾小的？
            k--;
            if (k == 0) {
                return curr->val; // 找到第 k 小
            }

            // 步驟 4: 轉向右子樹
            curr = curr->right;
        }

        return -1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(H + k)$
    -   $H$ 是樹的高度 (一開始往左鑽到底需要 $O(H)$)。
    -   之後每一次 pop 操作是 $O(1)$ (平均)，我們做 $k$ 次。
    -   所以是 $O(H + k)$。在最壞情況下 (k=n)，是 $O(n)$。
-   **Space Complexity**: $O(H)$
    -   Stack 的大小最多為樹高。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果 BST 頻繁修改？
- 第 K 大？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ In-order 順序錯誤
- ⚠️ 沒有提前終止

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 迭代 In-order
- 💎 Augmented BST 概念

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Validate Binary Search Tree (驗證二元搜尋樹)](11_Validate_BST.md)
