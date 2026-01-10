# Validate Binary Search Tree (驗證二元搜尋樹)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Binary Tree Root，請判斷它是否是一個 **Valid BST**。

**BST 定義**：
1.  **左子樹** 的所有節點值必須 **小於** 當前節點的值。
2.  **右子樹** 的所有節點值必須 **大於** 當前節點的值。
3.  左子樹和右子樹也必須是 Valid BST。

-   **Input**: `root = [2,1,3]`
    ```
      2
     / \
    1   3
    ```
-   **Output**: `true`
-   **Input**: `root = [5,1,4,null,null,3,6]`
    ```
      5
     / \
    1   4
       / \
      3   6
    ```
-   **Output**: `false` (4 < 5, OK. But 4's right child is 6. Wait, 4 must be > 5? No. 4 is Right Child of 5, so 4 must be > 5. Here 4 < 5, so invalid immediately.)
    Let's re-read the example properly.
    Node 5 -> Right 4. 4 < 5. Invalid.
    Let's check 3 is left child of 4.
    Proper example:
    ```
      5
     / \
    1   6
       / \
      3   7
    ```
    Is this valid?
    Node 5 -> Right 6 (OK). Node 6 -> Left 3.
    3 is < 6 (OK). BUT 3 is in the Right Subtree of 5. So 3 must be > 5. (3 < 5 -> Invalid).

-   **Constraints**:
    -   $1 <= nodes <= 10^4$
    -   $-2^{31} <= Node.val <= 2^{31} - 1$

---

## 2. 🐢 Brute Force Approach (暴力解)

對每個節點，收集左子樹所有值確認 max < root，收集右子樹所有值確認 min > root。
-   **Time**: $O(N^2)$。
-   **Result**: 效率不佳。

---

## 3. 💡 The "Aha!" Moment (優化)

**Approach 1: Recursive DFS with Range (Top-down)**
每個節點都必須在一個區間 `(min, max)` 內。
-   Root 區間: `(-inf, +inf)`
-   Left child: `(min, root->val)`
-   Right child: `(root->val, max)`
-   如果節點值不在區間內，回傳 False。
-   注意要用 `long long` 因為 node val 可能是 INT_MAX/MIN。

**Approach 2: In-order Traversal (Bottom-up)**
BST 的 **In-order Traversal** 結果必須是 **Strictly Increasing** 的。
-   遍歷過程中記錄 `prev` 節點的值。
-   檢查 `curr->val > prev->val`。
-   如果不是，回傳 False。

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive DFS with Range (Top-down)

```cpp
#include <climits>

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
    bool isValidBST(TreeNode* root) {
        return validate(root, LONG_MIN, LONG_MAX);
    }
    
private:
    bool validate(TreeNode* node, long long minVal, long long maxVal) {
        if (!node) return true;
        
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        return validate(node->left, minVal, node->val) &&
               validate(node->right, node->val, maxVal);
    }
};
```

### Approach: Iterative In-order Traversal

```cpp
#include <stack>

using namespace std;

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*> st;
        TreeNode* prev = nullptr;
        TreeNode* curr = root;
        
        while (curr || !st.empty()) {
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            
            curr = st.top();
            st.pop();
            
            if (prev && curr->val <= prev->val) {
                return false;
            }
            prev = curr;
            
            curr = curr->right;
        }
        
        return true;
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // 使用 long long 來處理邊界情況 (e.g., node val 是 INT_MAX)
        // 區間是開區間 (minVal, maxVal)，亦即 minVal < node->val < maxVal
        return helper(root, LONG_MIN, LONG_MAX);
    }
    
    // DFS Helper
    bool helper(TreeNode* node, long long minVal, long long maxVal) {
        if (!node) return true;
        
        // 檢查當前節點是否違反區間限制
        // 注意：BST 定義通常不允許重複值 (除非題目說允許，LeetCode 題目通常是嚴格小於/大於)
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        // 遞迴檢查左右子樹，並更新區間
        // 左子樹：上限變為當前節點值
        // 右子樹：下限變為當前節點值
        return helper(node->left, minVal, node->val) &&
               helper(node->right, node->val, maxVal);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   每個節點遍歷一次。
-   **Space Complexity**: $O(h)$
    -   Recursion stack.
