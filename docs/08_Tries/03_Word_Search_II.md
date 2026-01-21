# Word Search II (單字搜尋 II) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目給定一個 `m x n` 的字符網格 `board` 和一個單字列表 `words`。
請找出 `words` 中所有存在於 `board` 上的單字。
單字必須由網格中 **相鄰** 的字母組成（水平或垂直），同一個儲存格內的字母在同一個單字中最多只能使用一次。

-   **Input**:
    ```
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    ```

-   **Output**: `["eat","oath"]`
-   **Constraints**:
    -   $m, n <= 12$
    -   $1 <= words.length <= 3 \times 10^4$
    -   $1 <= word.length <= 10$

---

## 2. 🐢 Brute Force Approach (暴力解)

對 `words` 中的每個單字，呼叫一次 Word Search (Backtracking) 在 `board` 上搜尋。

-   **Time**: $O(K \times M \times N \times 4^L)$。
    -   $K$ is number of words.
    -   $M, N$ board size.
    -   $L$ is max word length.
-   **Result**: 效率極差。因為 $K$ 很大 ($30,000$)。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是典型的 **Backtracking + Trie**。
與其對每個單字遍歷 board，不如 **遍歷一次 board**，然後在走的過程中同時匹配所有單字。

1.  **Build Trie**: 將所有 `words` 插入 Trie。
2.  **DFS (Backtracking)**: 對 board 的每個格子 `(r, c)`，從 Trie 的 root 開始 DFS。
3.  **Optimization (Pruning)**:
    -   當我們找到一個單字 (`EndOfWord == true`)，將其加入結果，並 **標記為已找到** (避免重複)。甚至可以從 Trie 中移除該單字以優化後續搜尋 (Pruning)。
    -   如果當前 DFS 路徑在 Trie 中沒有對應的 child，直接回溯 (Pruning)。

這種做法的時間複雜度主要取決於 Board 大小與 Trie 的深度，而不是 Word 的數量。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../word_search_ii_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../word_search_ii_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking with Trie

```cpp
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
    struct TrieNode {
        TrieNode* children[26];
        string* word; // Store pointer to word at leaf

        TrieNode() {
            word = nullptr;
            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
        }
    };

    void insert(TrieNode* root, string& word) {
        TrieNode* curr = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!curr->children[idx]) {
                curr->children[idx] = new TrieNode();
            }
            curr = curr->children[idx];
        }
        curr->word = &word;
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (string& w : words) {
            insert(root, w);
        }

        vector<string> result;
        int m = board.size();
        int n = board[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, i, j, root, result);
            }
        }

        return result;
    }

private:
    void dfs(vector<vector<char>>& board, int r, int c, TrieNode* node, vector<string>& result) {
        char letter = board[r][c];
        int idx = letter - 'a';

        if (letter == '#' || !node->children[idx]) {
            return;
        }

        TrieNode* nextNode = node->children[idx];
        if (nextNode->word) {
            result.push_back(*nextNode->word);
            nextNode->word = nullptr; // Deduplicate: found once, no need to find again
        }

        board[r][c] = '#'; // Mark visited

        int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (auto& d : dirs) {
            int newR = r + d[0];
            int newC = c + d[1];
            if (newR >= 0 && newR < board.size() && newC >= 0 && newC < board[0].size()) {
                dfs(board, newR, newC, nextNode, result);
            }
        }

        board[r][c] = letter; // Backtrack

        // Optimization: Leaf pruning (Optional but good for performance)
        // If nextNode has no children, we can remove it from parent's children array
        // to avoid visiting empty paths again. (Not implemented here for simplicity)
    }
};
```

### Python Reference

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] not in node.children or node.children[board[r][c]].refs < 1 or
                (r, c) in visit):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
    struct TrieNode {
        TrieNode* children[26];
        string* word; // 這裡直接存字串的指標，用來快速取得結果，也兼作 isEndOfWord 標記

        TrieNode() {
            word = nullptr;
            for(int i=0; i<26; i++) children[i] = nullptr;
        }
    };

    // Trie Insert
    void insert(TrieNode* root, string& s) {
        TrieNode* curr = root;
        for(char c : s) {
            int idx = c - 'a';
            if(!curr->children[idx]) curr->children[idx] = new TrieNode();
            curr = curr->children[idx];
        }
        curr->word = &s; // 標記單字結尾，並保存單字內容
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // 1. Build Trie
        TrieNode* root = new TrieNode();
        for(auto& w : words) insert(root, w);

        vector<string> res;
        int m = board.size();
        int n = board[0].size();

        // 2. DFS from each cell
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dfs(board, i, j, root, res);
            }
        }
        return res;
    }

private:
    void dfs(vector<vector<char>>& board, int r, int c, TrieNode* node, vector<string>& res) {
        char ch = board[r][c];

        // 如果已經訪問過 (#) 或者 Trie 中沒有這個分支
        if(ch == '#' || !node->children[ch - 'a']) return;

        TrieNode* nextNode = node->children[ch - 'a'];

        // 找到一個單字
        if(nextNode->word != nullptr) {
            res.push_back(*nextNode->word);
            nextNode->word = nullptr; // 避免重複加入同一個單字 (Deduplication)
            // 可選：可以實作計數器來剪枝 Trie，如果一個節點下方的單字都找完了，可以把這個節點剪掉
        }

        // 標記為訪問
        board[r][c] = '#';

        // 遞迴四個方向
        const int dirs[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        for(auto& d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];
            if(nr >= 0 && nr < board.size() && nc >= 0 && nc < board[0].size()) {
                dfs(board, nr, nc, nextNode, res); // 傳入 nextNode 繼續往下走
            }
        }

        // Backtrack
        board[r][c] = ch;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N \times 4^L)$
    -   Need to start DFS from each cell.
    -   However, the Trie effectively prunes the $4^L$ search.
    -   In reality, it's roughly $O(M \times N \times L)$ in typical cases because most paths die quickly.
-   **Space Complexity**: $O(K \times L)$ for Trie.
