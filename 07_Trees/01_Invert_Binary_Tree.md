# Invert Binary Tree (翻轉二元樹)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Binary Tree 的 root，請翻轉這棵樹，使所有左右子樹交換位置。
Max Howell (Homebrew creator) 曾經在面試被 Google 問這題而被拒，非常有名。

-   **Input**:
    ```
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    ```
-   **Output**:
    ```
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    ```
-   **Constraints**:
    -   The number of nodes in the tree is in the range `[0, 100]`.
    -   `-100 <= Node.val <= 100`.

---

## 2. 🐢 Brute Force Approach (暴力解)

這題沒有所謂的暴力解，因為必須訪問每個節點一次來交換。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個典型的 **DFS (Pre-order / Post-order) Traversal** 問題。
對於樹中的每一個節點：
1.  交換它的左子節點和右子節點 `swap(node->left, node->right)`.
2.  遞迴地對左子樹做同樣的事。
3.  遞迴地對右子樹做同樣的事。

順序可以是：
-   Swap -> Recurse Left -> Recurse Right (Pre-order)
-   Recurse Left -> Recurse Right -> Swap (Post-order)
-   In-order (Left -> Swap -> Left) 比較麻煩因为 Swap 後左右變了，要注意。

**BFS (Level Order)** 也可以：用 Queue 存節點，每次 Pop 出來就 Swap 它的左右子節點，然後把它們 Push 進 Queue。

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
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        
        // Swap
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recurse
        invertTree(root->left);
        invertTree(root->right);
        
        return root;
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
             return None
        
        # Swap
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case: 如果節點為空，直接返回
        if (root == nullptr) {
            return nullptr;
        }
        
        // 核心操作：交換左右子樹指針
        // 就像是在照鏡子
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // 遞迴處理子樹
        // 注意：即使交換了，我們依然要對這兩個子節點進行遞迴
        // 先後的邏輯是：先交換當前層的左右指針，然後深入下一層去交換它們內部的指針
        invertTree(root->left);  // 因為已經交換過，這其實是去原本的 right child
        invertTree(root->right); // 這其實是去原本的 left child
        
        return root;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   訪問每個節點一次。
-   **Space Complexity**: $O(h)$
    -   遞迴深度，最壞情況下 (Skewed Tree) 是 $O(n)$，平均情況 (Balanced) 是 $O(\log n)$。
