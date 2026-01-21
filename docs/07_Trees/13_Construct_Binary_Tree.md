# Construct Binary Tree from Preorder and Inorder Traversal (從前序與中序遍歷構造二元樹) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目給兩個整數陣列 `preorder` 和 `inorder`，分別代表同一棵樹的前序遍歷和中序遍歷結果。
請構造並回傳這棵 Binary Tree。

-   **Preorder**: `root` -> `left` -> `right`
-   **Inorder**: `left` -> `root` -> `right`

-   **Input**: `preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]`
-   **Output**: `[3,9,20,null,null,15,7]`
    ```
      3
     / \
    9  20
      /  \
     15   7
    ```

-   **Key Insight**:
    -   `preorder[0]` 永遠是 **Root**。
    -   在 `inorder` 中找到 Root 的位置，可以將陣列切分為 **Left Subtree** 和 **Right Subtree**。
    -   接著遞迴處理。

-   **Constraints**:
    -   $1 <= preorder.length <= 3000$
    -   `inorder.length == preorder.length`
    -   unique values.

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每個遞迴步驟：

1.  取 `preorder[0]` 作為 root。
2.  遍歷 `inorder` 找到 root 的 index `k`。
3.  切分 `inorder` 為 `left: [0...k-1]`, `right: [k+1...end]`。
4.  切分 `preorder`。
    -   左子樹長度為 `k` (假設 inorder 從 0 開始)。
    -   `pre_left: [1...k]`, `pre_right: [k+1...end]`。
5.  遞迴构造。
-   **Time**: $O(N^2)$。因為每次都要在 inorder 中搜尋 root，且 slicing array 需要複製。
-   **Result**: 題目規模 3000， $O(N^2)$ 約 $9 \times 10^6$，是可以接受的，但可以優化。

---

## 3. 💡 The "Aha!" Moment (優化)

不需要每次遍歷 `inorder` 來找 root。
我們可以用 **Hash Map** 預先儲存 `value -> index` 的映射：`inorder_map`。
這樣查找 root index 只需 $O(1)$。

此外，不需要複製 array (slicing)，只需傳遞 **index pointers** (`p_start`, `p_end`, `i_start`, `i_end`)。
或者更簡單：只傳遞 `root` 在 `preorder` 中的 index，以及當前子樹在 `inorder` 中的範圍 `(left, right)`。

**Algorithm**:

1.  Map `inorder` values to indices.
2.  Function `build(preStart, inStart, inEnd)`:
    -   if `preStart > preEnd` or `inStart > inEnd`: return null.
    -   Root value = `preorder[preStart]`.
    -   Root index in inorder = `map[rootValue]`.
    -   Left subtree size = `rootIndex - inStart`.
    -   `root->left = build(preStart + 1, inStart, rootIndex - 1)`
    -   `root->right = build(preStart + 1 + leftSize, rootIndex + 1, inEnd)`
    -   Return root.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../construct_tree_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../construct_tree_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Map + Recursion

```cpp
#include <vector>
#include <unordered_map>

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // Build map for O(1) lookup
        for (int i = 0; i < inorder.size(); i++) {
            inorderMap[inorder[i]] = i;
        }

        return build(preorder, 0, 0, inorder.size() - 1);
    }

private:
    unordered_map<int, int> inorderMap;

    // preStart: index of current root in preorder
    // inStart, inEnd: range of current subtree in inorder
    TreeNode* build(vector<int>& preorder, int preStart, int inStart, int inEnd) {
        if (inStart > inEnd) {
            return nullptr;
        }

        int rootVal = preorder[preStart];
        TreeNode* root = new TreeNode(rootVal);

        int inIndex = inorderMap[rootVal];
        int leftSubtreeSize = inIndex - inStart;

        root->left = build(preorder, preStart + 1, inStart, inIndex - 1);
        root->right = build(preorder, preStart + 1 + leftSubtreeSize, inIndex + 1, inEnd);

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
    unordered_map<int, int> inMap; // 儲存 inorder 值到索引的映射
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // 預處理 Inorder Map，加速查找
        for(int i = 0; i < inorder.size(); i++) {
            inMap[inorder[i]] = i;
        }

        return helper(preorder, 0, inorder.size() - 1, 0); // 這裡稍微改參數傳遞，更直觀一點
        // 不過 C++ 版本我上面用了 preStart, inStart, inEnd。
        // 用 preStart 來決定 root，用 inStart/inEnd 來決定子樹邊界。
    }

private:
    // preIndex: 現在處理到 preorder 的哪裡 (可以直接用 reference 傳遞一個 global index)
    // 或者像上面的寫法：計算 offset
    // 這裡我們改用一個更簡單的寫法： global preIndex

    /*
       Updated Implementation Logic for clarity:
       使用一個全局指標 `preIdx` 追蹤前序遍歷的進度。
       每次函式呼叫都會消耗一個 preorder 的元素做為 root。
    */
};

// Re-write the cleaner C++ class for the file content
class CleanerSolution {
    unordered_map<int, int> inMap;
    int preIdx = 0;

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for(int i = 0; i < inorder.size(); i++) {
            inMap[inorder[i]] = i;
        }
        preIdx = 0;
        return build(preorder, 0, inorder.size() - 1);
    }

    TreeNode* build(vector<int>& preorder, int inStart, int inEnd) {
        // Base case: 範圍無效
        if (inStart > inEnd) return nullptr;

        // 從 preorder 取出當前 root
        int rootVal = preorder[preIdx];
        preIdx++; // 移動到下一個

        TreeNode* root = new TreeNode(rootVal);

        // 找到 root 在 inorder 的位置
        int inIndex = inMap[rootVal];

        // 遞迴構造左右子樹
        // 注意：一定是先 Left 後 Right，因為 Preorder 是 Root -> Left -> Right
        // 我們的 preIdx 會先遍歷完左子樹的所有節點，才會跑到右子樹
        root->left = build(preorder, inStart, inIndex - 1);
        root->right = build(preorder, inIndex + 1, inEnd);

        return root;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   每個節點被創建一次。Map lookup 是 $O(1)$。
-   **Space Complexity**: $O(n)$
    -   Hash Map 存 $n$ 個元素。Recursive stack $O(h)$。
