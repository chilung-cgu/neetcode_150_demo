# Serialize and Deserialize Binary Tree (二元樹的序列化與反序列化) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

> 📌 **LeetCode #297** — [題目連結](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [NeetCode 解說](https://neetcode.io/problems/serialize-and-deserialize-binary-tree)


## 1. 🧐 Problem Dissection (釐清問題)

題目要求設計兩個演算法：

1.  `serialize(root)`: 將一棵 Binary Tree 轉換成一個 string。
2.  `deserialize(data)`: 將這個 string 轉換回原本的 Binary Tree。

序列化的格式由你決定，只要能保證還原即可。
LeetCode 通常使用 Level Order (BFS) 來表示，例如 `[1,2,3,null,null,4,5]`，但你可以使用任何有效的格式 (Preorder DFS is usually easier)。

-   **Input**: `root = [1,2,3,null,null,4,5]`
    ```
      1
     / \
    2   3
       / \
      4   5
    ```

-   **Output**: Same tree object.
-   **Constraints**:
    -   $0 <= nodes <= 10^4$
    -   $-1000 <= Node.val <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

這題本身就是考設計。

-   你可以存成 XML, JSON，但太 verbose。
-   你可以存成 `(1(2)(3(4)(5)))` 這種括號表示法 (Preorder)。

---

## 3. 💡 The "Aha!" Moment (優化)

最簡單且高效的方法是 **Preorder DFS (Root -> Left -> Right)**。

**Serialize (Preorder)**:

-   遍歷樹。
-   如果是非空節點，append `val` + `,` (Delimiter)。
-   如果是空節點，append `N` + `,` (Null Marker)。
-   Result String: `1,2,N,N,3,4,N,N,5,N,N,`

**Deserialize**:

-   將 string 根據 `,` split 成 values queue/stream。
-   `1` -> Create Node(1). Recursively build left.
    -   Next is `2` -> Create Node(2). Recursively build left.
        -   Next is `N` -> Return null.
    -   Recursively build right (of 2).
        -   Next is `N` -> Return null.
-   Recursively build right (of 1).
    -   Next is `3` -> ...
-   依此類推。

**Why Preorder?**
因為 Root 永遠在最前面，我們一讀就知道當前子樹的 Root 是誰，然後可以直接開始遞迴構造左子樹，剩下的就是右子樹。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../serialize_tree_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../serialize_tree_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Preorder DFS

```cpp
#include <string>
#include <sstream>
#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "N";

        // Preorder: Root, Left, Right
        // Use comma as delimiter
        return to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        string segment;
        queue<string> q;

        while (getline(ss, segment, ',')) {
            q.push(segment);
        }

        return deserializeHelper(q);
    }

private:
    TreeNode* deserializeHelper(queue<string>& q) {
        if (q.empty()) return nullptr;

        string val = q.front();
        q.pop();

        if (val == "N") {
            return nullptr;
        }

        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(q);
        node->right = deserializeHelper(q);

        return node;
    }
};
```

### Python Reference

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)


    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if self.i >= len(vals):
                return None

            token = vals[self.i]
            self.i += 1

            if token == "N":
                return None

            node = TreeNode(int(token))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Codec {
public:

    // Encodes a tree to a single string.
    // 使用 Preorder Traversal (前序遍歷)
    // 每個節點值後面加一個逗號 ','
    // 空節點用 "N" 表示
    string serialize(TreeNode* root) {
        if (root == nullptr) {
            return "N";
        }
        // 遞迴拼接字串 (效率稍微低一點，但逻辑清晰。面試可用 stringstream 優化)
        return to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    // 先將字串 split 成一個 Queue
    TreeNode* deserialize(string data) {
        queue<string> q;
        stringstream ss(data);
        string s;
        // Split by comma
        while (getline(ss, s, ',')) {
            q.push(s);
        }
        return helper(q);
    }

private:
    TreeNode* helper(queue<string>& q) {
        if (q.empty()) return nullptr;

        string s = q.front();
        q.pop();

        // 遇到 "N" 代表是空節點，回傳 nullptr
        if (s == "N") {
            return nullptr;
        }

        // 否則建立新節點
        TreeNode* node = new TreeNode(stoi(s));

        // 遞迴建立左右子樹 (利用 Preorder 的順序)
        node->left = helper(q);
        node->right = helper(q);

        return node;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   Serialize: 訪問每個節點一次。
    -   Deserialize: 處理每個 split 出來的 token 一次。
-   **Space Complexity**: $O(n)$
    -   Serialize: String/Recursion Stack.
    -   Deserialize: Queue/Recursion Stack.

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- N-ary Tree?
- 壓縮序列化？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 序列化格式不一致
- ⚠️ 反序列化指標管理錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 BFS vs DFS 方案比較
- 💎 null 節點的處理
