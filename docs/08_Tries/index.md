# Chapter 8: Tries (前綴樹)

本章節包含 3 道關鍵的 Trie (Prefix Tree) 相關題目。
Trie 是一種高效的樹狀資料結構，專門用於處理字串搜尋、自動補全與拼字檢查等應用場景。

## 🎨 互動式視覺化演算法

我們為本章節製作了互動式 D3.js 視覺化工具，幫助你理解 Trie 的構建過程以及複雜的搜尋邏輯。

<div style="text-align: center; margin: 30px 0;">
    <a href="index.html" target="_blank" style="background: linear-gradient(135deg, #f59e0b, #ec4899); color: white; padding: 15px 30px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.2rem; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4); transition: transform 0.2s;">
        🚀 開啟互動式視覺化演算法 (Visualizer Hub)
    </a>
</div>

> **💡 提示**:
>
> - **基礎練習**: 先從 _Implement Trie_ 開始，掌握 `insert` 和 `search` 的基本邏輯。
> - **進階挑戰**: _Word Search II_ 是 Google 面試的高頻題，結合了 Trie, Backtracking 與 Grid DFS，非常值得深入研究。

## 📚 題目列表

以下是本章節包含的題目及其詳細題解：

| 題目 (Problem)                                                              | 難度 (Difficulty) | 重點概念 (Key Concepts)     |
| :-------------------------------------------------------------------------- | :---------------- | :-------------------------- |
| [Implement Trie (Prefix Tree)](01_Implement_Trie_Prefix_Tree.md)            | Medium            | Tree Structure, HashMap     |
| [Design Add and Search Words Data Structure](02_Design_Add_Search_Words.md) | Medium            | DFS, Backtracking, Wildcard |
| [Word Search II](03_Word_Search_II.md)                                      | Hard              | Trie, DFS, Optimization     |

---

## 🧠 學習重點

1. **結構定義**: 每個 Trie Node 通常包含一個 HashMap (或長度 26 的 Array) 指向子節點，以及一個 Boolean 標記 `isEndOfWord`。
2. **通配符處理**: 當遇到 `.` 或模糊搜尋時，需要遍歷所有非子空節點 (Backtracking)。
3. **效率優化**:
   - 相比 HashMap 用於存儲單詞集合，Trie 在處理前綴 (Prefix) 查詢時極具優勢 (`O(L)` vs `O(N*L)` where N is number of words)。
   - 在 _Word Search II_ 中，利用 Trie 可以迅速剪枝無效的 DFS 路徑。

Happy Coding! 🌳
