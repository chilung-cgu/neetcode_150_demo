---
title: "Design Add and Search Words Data Structure (設計新增與搜尋單字的資料結構)"
description: "題目要求設計一個資料結構 `WordDictionary`，支援："
tags:
  - 
Trie  - String
difficulty: Medium
---

# Design Add and Search Words Data Structure (設計新增與搜尋單字的資料結構) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #211** — [題目連結](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [NeetCode 解說](https://neetcode.io/problems/design-add-and-search-words-data-structure)


## 1. 🧐 Problem Dissection (釐清問題)

題目要求設計一個資料結構 `WordDictionary`，支援：

1.  `addWord(word)`: 新增單字。
2.  `search(word)`: 搜尋單字。
    -   輸入的 `word` 可能包含 `.`，代表 **wildcard** (匹配任何一個字元)。
    -   例如：`search("bad")` -> true, `search(".ad")` -> true, `search("b..")` -> true.

-   **Input**:
    ```
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True
    ```

-   **Constraints**:
    -   $1 <= word.length <= 25$
    -   `word` in `addWord` consists of lowercase English letters.
    -   `word` in `search` consists of '.' or lowercase English letters.
    -   At most $10^4$ calls.

---

## 2. 🐢 Brute Force Approach (暴力解)

用 `HashSet` 存所有字。
`search` 時，如果包含 `.`，遍歷 Set 中所有長度相同的字，逐字元比對。

-   **Time**: $O(N \times L)$ for generic search.
-   **Result**: 有點慢，但因為 $L$ 很小 (25)，可能可以過。

---

## 3. 💡 The "Aha!" Moment (優化)

使用 **Trie (Prefix Tree)**。

-   `addWord`: 標準 Trie 插入，$O(L)$。
-   `search`: 使用 **DFS (Backtracking)**。
    -   如果當前 char 是 `.`，則遞迴遍歷當前節點的 **所有** 非空 children。只要有一條路徑回傳 true，就回傳 true。
    -   如果當前 char 是普通字母，則只走對應的 child。
    -   如果是字串結尾，檢查 `EndOfWord`。

這樣就把 $O(N)$ 的搜尋空間縮小到 Trie 的分支上，效率更高。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../word_dictionary_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../word_dictionary_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Trie + DFS for Wildcard

```cpp
#include <string>
#include <vector>

using namespace std;

class WordDictionary {
private:
    struct TrieNode {
        TrieNode* children[26];
        bool isEndOfWord;

        TrieNode() {
            isEndOfWord = false;
            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
        }
    };

    TrieNode* root;

    bool searchInNode(string& word, int index, TrieNode* node) {
        // Base case: 遍歷完 word 的所有字元
        if (index == word.length()) {
            return node->isEndOfWord;
        }

        char c = word[index];
        if (c == '.') {
            // Wildcard: 嘗試所有可能的子節點
            for (int i = 0; i < 26; i++) {
                if (node->children[i] && searchInNode(word, index + 1, node->children[i])) {
                    return true;
                }
            }
            return false;
        } else {
            // 一般字元
            int charIndex = c - 'a';
            if (!node->children[charIndex]) {
                return false;
            }
            return searchInNode(word, index + 1, node->children[charIndex]);
        }
    }

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            int index = c - 'a';
            if (!curr->children[index]) {
                curr->children[index] = new TrieNode();
            }
            curr = curr->children[index];
        }
        curr->isEndOfWord = true;
    }

    bool search(string word) {
        return searchInNode(word, 0, root);
    }
};
```

### Python Reference

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word

        return dfs(0, self.root)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class WordDictionary {
    struct TrieNode {
        TrieNode* next[26];
        bool isEnd = false;
        TrieNode() { // 重要：初始化
            for(int i=0; i<26; i++) next[i] = nullptr;
        }
    };

    TrieNode* root;

    // DFS Helper Function
    bool dfs(const string& word, int index, TrieNode* curr) {
        // Base case: 如果字串已經比對完畢
        if (index == word.size()) {
            return curr->isEnd;
        }

        char c = word[index];

        if (c == '.') {
            // 如果是點，匹配任何存在的子節點
            for (int i = 0; i < 26; i++) {
                if (curr->next[i] != nullptr) {
                    // 只要有一條路通，就回傳 true
                    if (dfs(word, index + 1, curr->next[i])) {
                        return true;
                    }
                }
            }
            return false; // 所有子節點都走不通
        } else {
            // 一般字元，必須精確匹配
            if (curr->next[c - 'a'] == nullptr) {
                return false;
            }
            return dfs(word, index + 1, curr->next[c - 'a']);
        }
    }

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->next[c - 'a'] == nullptr) {
                curr->next[c - 'a'] = new TrieNode();
            }
            curr = curr->next[c - 'a'];
        }
        curr->isEnd = true;
    }

    bool search(string word) {
        return dfs(word, 0, root);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**:
    -   `addWord`: $O(L)$。
    -   `search`:
        -   對於沒有 `.` 的情況：$O(L)$。
        -   對於有 `.` 的情況 (Worst case `.....`)：需要遍歷整棵樹 $O(26^L)$。但實際上因為 L 很小 (25)，且字典單字有限，會剪枝很多。
-   **Space Complexity**: $O(N \times L \times 26)$ (Trie storage)。Recursive stack $O(L)$。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 你會如何處理更大的輸入？
- 有沒有更好的空間複雜度？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有考慮邊界條件
- ⚠️ 未討論複雜度

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 主動討論 trade-offs
- 💎 提供多種解法比較

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Implement Trie (Prefix Tree) (實作字典樹)](01_Implement_Trie_Prefix_Tree.md)
- [Word Search II (單字搜尋 II)](03_Word_Search_II.md)
