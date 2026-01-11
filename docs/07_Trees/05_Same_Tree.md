# Same Tree (相同的樹)

## 1. 🧐 Problem Dissection (釐清問題)

題目給兩棵 Binary Tree `p` 和 `q`。
判斷它們是否 **完全相同**。
相同意味著：

1.  結構相同 (Structure).
2.  每個對應節點的值相同 (Value).

-   **Input**: `p = [1,2,3], q = [1,2,3]`
-   **Output**: `true`
-   **Input**: `p = [1,2], q = [1,null,2]`
-   **Output**: `false` (Structure differs)
-   **Constraints**:
    -   $0 <= nodes <= 100$
    -   $-10^4 <= Node.val <= 10^4$

---

## 2. 🐢 Brute Force Approach (暴力解)

同時遍歷兩棵樹 (DFS/BFS)。
每一步都檢查：

-   `p` 和 `q` 是否同时為 null? (是 -> OK)
-   `p` 和 `q` 只有一個為 null? (是 -> False)
-   `p->val != q->val`? (是 -> False)
-   Recursively check left and right.

---

## 3. 💡 The "Aha!" Moment (優化)

這就是一個同步 DFS。沒有太多優化空間，因為已經是最簡潔的 $O(N)$。

**Logic**:
`isSame(p, q)` is true IF:

1.  Both null -> True.
2.  One null, one not -> False.
3.  Values different -> False.
4.  `isSame(p->left, q->left)` AND `isSame(p->right, q->right)`.

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive DFS

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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base cases

        // 1. Both are null -> Identical
        if (!p && !q) return true;

        // 2. One is null, one is not -> Not identical
        if (!p || !q) return false;

        // 3. Values are different -> Not identical
        if (p->val != q->val) return false;

        // Recursive step: Check left value AND check right value
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

### Python Reference

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Condition 1: 兩個都到底了，代表這一路下來都一樣 -> True
        if (p == nullptr && q == nullptr) {
            return true;
        }

        // Condition 2: 其中一個到底了，另一個還有，結構不同 -> False
        // Condition 3: 兩個都沒到底，但是值不同 -> False
        if (p == nullptr || q == nullptr || p->val != q->val) {
            return false;
        }

        // Recursive Step: 只有當左子樹相同 且 右子樹相同時，整棵樹才相同
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   $n$ 是較小那棵樹的節點數。
-   **Space Complexity**: $O(h)$
    -   Recursive stack depth.
