# Chapter 7: Trees (二元樹)

本章節包含 **NeetCode 150** 中的所有樹 (Trees) 相關題目。
樹是被廣泛使用的資料結構，更是技術面試中的重中之重。

## 🎨 互動式視覺化演算法

我們為本章節的所有 15 道題目製作了精美的互動式 D3.js 視覺化工具。
這些工具可以幫助你直觀地理解遞歸 (Recursion)、深度優先搜尋 (DFS) 和廣度優先搜尋 (BFS) 的運作過程。

<div style="text-align: center; margin: 30px 0;">
    <a href="index.html" target="_blank" style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; padding: 15px 30px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.2rem; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4); transition: transform 0.2s;">
        🚀 開啟互動式視覺化演算法 (Visualizer Hub)
    </a>
</div>

> **💡 提示**: 點擊上方按鈕將開啟獨立的 HTML 頁面，建議使用大螢幕瀏覽以獲得最佳體驗。

## 📚 題目列表

以下是本章節包含的題目及其詳細題解：

| 題目 (Problem)                                                                           | 難度 (Difficulty) | 重點概念 (Key Concepts)      |
| :--------------------------------------------------------------------------------------- | :---------------- | :--------------------------- |
| [Invert Binary Tree](01_Invert_Binary_Tree.md)                                           | Easy              | Recursion, Swap              |
| [Maximum Depth of Binary Tree](02_Maximum_Depth_of_Binary_Tree.md)                       | Easy              | DFS, BFS                     |
| [Diameter of Binary Tree](03_Diameter_of_Binary_Tree.md)                                 | Easy              | DFS, Global Max              |
| [Balanced Binary Tree](04_Balanced_Binary_Tree.md)                                       | Easy              | Bottom-up DFS                |
| [Same Tree](05_Same_Tree.md)                                                             | Easy              | Recursion, Structural Check  |
| [Subtree of Another Tree](06_Subtree_of_Another_Tree.md)                                 | Easy              | Dual Recursion               |
| [Lowest Common Ancestor of a Binary Search Tree](07_Lowest_Common_Ancestor_BST.md)       | Medium            | BST Properties               |
| [Binary Tree Level Order Traversal](08_Binary_Tree_Level_Order_Traversal.md)             | Medium            | BFS, Queue                   |
| [Binary Tree Right Side View](09_Binary_Tree_Right_Side_View.md)                         | Medium            | BFS, Queue                   |
| [Count Good Nodes in Binary Tree](10_Count_Good_Nodes.md)                                | Medium            | DFS, Path Max                |
| [Validate Binary Search Tree](11_Validate_BST.md)                                        | Medium            | DFS, Range Check             |
| [Kth Smallest Element in a BST](12_Kth_Smallest_Element_BST.md)                          | Medium            | In-order Traversal           |
| [Construct Binary Tree from Preorder and Inorder Traversal](13_Construct_Binary_Tree.md) | Medium            | Array Slicing, Recursion     |
| [Binary Tree Maximum Path Sum](14_Binary_Tree_Maximum_Path_Sum.md)                       | Hard              | DFS, Split vs Path           |
| [Serialize and Deserialize Binary Tree](15_Serialize_Deserialize_Binary_Tree.md)         | Hard              | BFS/DFS, String Manipulation |

---

## 🧠 學習重點

1. **遞歸思維 (Recursive Thinking)**: 樹的問題絕大多數可以通過遞歸解決。學會定義 Base Case 和 Recursive Step 是關鍵。
2. **遍歷方式 (Traversals)**:
   - **DFS (深度優先)**: Pre-order, In-order, Post-order。
   - **BFS (廣度優先)**: Level-order (使用 Queue)。
3. **BST 性質**: Binary Search Tree 的左小右大特性是解題捷徑。
4. **返回值與全局變數**: 有些問題需要「自底向上」傳遞資訊 (如高度)，同時更新「全局最大值」(如直徑、路徑和)。

Happy Coding! 🌲
