# Implement Trie (Prefix Tree) (實作字典樹)

## 1. 🧐 Problem Dissection (釐清問題)

題目要求實作一個 `Trie` 類別 (Prefix Tree)，包含以下方法：

1.  `insert(String word)`: 將單字 `word` 插入 Trie。
2.  `search(String word)`: 回傳 `word` 是否在 Trie 中（必須是完整單字）。
3.  `startsWith(String prefix)`: 回傳 Trie 中是否有任何單字以 `prefix` 開頭。

-   **Input**:
    ```
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True
    ```

-   **Constraints**:
    -   `word` and `prefix` consist only of lowercase English letters (a-z).
    -   $1 <= length <= 2000$.
    -   At most $3 \times 10^4$ calls.

---

## 2. 🐢 Brute Force Approach (暴力解)

用一個 `HashSet` 存所有 words。

-   `insert`: $O(1)$ 或 $O(L)$ (Depends on hash)。
-   `search`: $O(1)$ 或 $O(L)$。
-   `startsWith`: 必須遍歷 Set 中的所有字串，檢查是否以 prefix 開頭。時間 $O(N \times L)$。太慢。

---

## 3. 💡 The "Aha!" Moment (優化)

使用 **Trie (N-ary Tree)** 結構。
每個節點包含：

1.  **Children**: 一個大小為 26 的 Array (對應 'a'-'z')，指向下一個節點。
2.  **EndOfWord**: 一個 boolean，標記是否在此處結束一個完整的單字。

**Operations**:

-   `insert(word)`: 從 root 開始，沿著 word 的每個 char 往下走/建立節點。最後將最後一個節點的 `EndOfWord` 設為 true。 $O(L)$。
-   `search(word)`: 從 root 開始走。如果卡住（child 為 null）回傳 false。走完後檢查 `EndOfWord` 是否為 true。 $O(L)$。
-   `startsWith(prefix)`: 同 search，但走完後不需要檢查 `EndOfWord`，只要沒卡住就回傳 true。 $O(L)$。

---

## 4. 💻 Implementation (程式碼)

### Approach: Array for Children

```cpp
#include <string>
#include <vector>

using namespace std;

class Trie {
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

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
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
        TrieNode* curr = root;
        for (char c : word) {
            int index = c - 'a';
            if (!curr->children[index]) {
                return false;
            }
            curr = curr->children[index];
        }
        return curr->isEndOfWord;
    }

    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char c : prefix) {
            int index = c - 'a';
            if (!curr->children[index]) {
                return false;
            }
            curr = curr->children[index];
        }
        return true;
    }
};
```

### Python Reference

```python
class TrieNode:
    def __init__(self):
        self.children = {} # Map char -> TrieNode
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Trie {
    // 定義內部節點結構
    struct Node {
        // 使用 Array 優化存取速度 (知道只有 a-z)
        // 也可以用 HashMap<char, Node*>
        Node* children[26];
        bool isEnd;

        Node() {
            isEnd = false;
            // 初始化指標為 nullptr (C++ 不會自動做)
            for(int i=0; i<26; i++) children[i] = nullptr;
        }
    };

    Node* root;

public:
    Trie() {
        root = new Node();
    }

    // O(L) Time, O(L) Space
    void insert(string word) {
        Node* curr = root;
        for (char c : word) {
            int idx = c - 'a';
            // 如果路徑不存在，創建新節點
            if (curr->children[idx] == nullptr) {
                curr->children[idx] = new Node();
            }
            curr = curr->children[idx];
        }
        // 標記單字結尾
        curr->isEnd = true;
    }

    // O(L) Time, O(1) Space
    bool search(string word) {
        Node* curr = root;
        for (char c : word) {
            int idx = c - 'a';
            if (curr->children[idx] == nullptr) {
                return false; // 路徑中斷，單字不存在
            }
            curr = curr->children[idx];
        }
        // 必須剛好在 End 位停下才是 True
        return curr->isEnd;
    }

    // O(L) Time, O(1) Space
    bool startsWith(string prefix) {
        Node* curr = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (curr->children[idx] == nullptr) {
                return false; // Prefix 不存在
            }
            curr = curr->children[idx];
        }
        // 只要能走完 Prefix 即可，不一定要是單字結尾
        return true;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(L)$ for insert, search, startsWith. $L$ is word length.
-   **Space Complexity**: $O(N \times L \times 26)$ worst case (sparse).
    -   $N$ words, length $L$.
    -   Each node has 26 pointers.
