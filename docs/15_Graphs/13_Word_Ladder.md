# Word Ladder (字詞接龍)

## 1. 🧐 Problem Dissection (釐清問題)

給定兩個單詞 `beginWord` 和 `endWord`，以及一個字典 `wordList`。
請找出從 `beginWord` 變換到 `endWord` 的 **最短轉換序列** 的長度。
變換規則：
1.  每次只能改變一個字母。
2.  變換過程中的中間單詞必須都在 `wordList` 中。

-   **Input**: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`
-   **Output**: `5`
    -   Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" (5 words).
-   **Input**: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]`
-   **Output**: `0`
    -   "cog" not in list.
-   **Constraints**:
    -   1 <= word length <= 10.
    -   1 <= wordList length <= 5000.
    -   All words same length.

---

## 2. 🐢 Brute Force Approach (暴力解)

這是一個最短路徑問題。
如果把單詞看作節點，如果兩個單詞只差一個字母則連邊。
我們要找從 `beginWord` 到 `endWord` 的最短路徑。
BFS 是解決無權圖最短路徑的標準算法。

如果對於每個單詞，嘗試所有可能的 26*L 變換來尋找鄰居，時間複雜度為 $O(M \times L \times 26)$，其中 $M$ 是單詞數，$L$ 是單詞長度。

---

## 3. 💡 The "Aha!" Moment (優化)

這是標準的 **BFS**。
技巧在於如何高效地找到鄰居。

**Option 1: Pre-process Adjacency List**
-   對於每一對單詞，檢查是否只差 1 個字母。$O(M^2 \times L)$.
-   如果 $M$ 很大 (5000)，這個建圖過程會太慢。

**Option 2: Generate Neighbors via Wildcard Map**
-   對於單詞 "hot"，我們可以生成模式 "*ot", "h*t", "ho*"。
-   建立一個 Map: `pattern -> list of words`。
-   例如 `*ot -> [hot, dot, lot]`。
-   這樣在 BFS 時，對於 "hit"，生成 "*it", "h*t", "hi*"，然後直接從 Map 中查找鄰居。
-   **Time**: $O(M \times L^2)$ 用於預處理，$O(M \times L)$ 用於 BFS 查找。

**Input Constraints Analysis**:
-   $M=5000, L=10$.
-   $M^2 \times L = 2.5 \times 10^8$ (Might TLE).
-   $M \times L^2 \times 26 = 5000 \times 100 \times 26 \approx 1.3 \times 10^7$ (Safe).
-   注意：也可以不預處理 Map，而是在 BFS 過程中動態生成 `a-z` 的變換並檢查 `wordSet`。這也是 $O(M \times L \times 26)$。這個方法通常比較省空間且不需要維護複雜的 Map。

**Algorithm (Dynamic Neighbor Generation)**:
1.  將 `wordList` 放入 `unordered_set` 以便 $O(1)$ 查找。
2.  Queue 初始化 `q.push(beginWord)`。
3.  Level-by-level BFS。
4.  對於當前單詞，嘗試修改每一個位置的字符 (a-z)。
5.  如果修改後的單詞存在於 Set 中，則加入 Queue 並從 Set 中移除（避免重複訪問）。
6.  如果遇到 `endWord`，回傳當前層數 + 1。

---

## 4. 💻 Implementation (程式碼)

### Approach: BFS with Set

```cpp
#include <vector>
#include <string>
#include <unordered_set>
#include <queue>

using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the list, impossible
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        queue<string> q;
        q.push(beginWord);
        
        int level = 1;
        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                
                if (curr == endWord) return level;
                
                // Try changing each character
                // We modify 'curr' directly and restore it to save space
                for (int j = 0; j < curr.size(); j++) {
                    char originalChar = curr[j];
                    
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == originalChar) continue;
                        
                        curr[j] = c;
                        
                        // If transformed word is in dictionary
                        if (wordSet.find(curr) != wordSet.end()) {
                            q.push(curr);
                            wordSet.erase(curr); // Mark as visited
                        }
                    }
                    
                    // Restore
                    curr[j] = originalChar;
                }
            }
            level++;
        }
        
        return 0;
    }
};
```

### Python Reference

```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
                
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res += 1
            
        return 0
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // 使用 Set 以便 O(1) 查找單詞是否存在
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // 如果目標單詞不在字典中，永遠無法到達
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        queue<string> q;
        q.push(beginWord);
        
        // 初始長度為 1 (包含 beginWord 本身)
        int level = 1;
        
        while (!q.empty()) {
            int size = q.size(); // 當前層的節點數
            
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                
                // 找到目標
                if (curr == endWord) return level;
                
                // 嘗試將當前單詞的每個字符替換成 'a' 到 'z'
                for (int j = 0; j < curr.size(); j++) {
                    char originalChar = curr[j];
                    
                    for (char c = 'a'; c <= 'z'; c++) {
                        // 跳過自己
                        if (c == originalChar) continue;
                        
                        curr[j] = c;
                        
                        // 檢查變換後的單詞是否在字典中
                        if (wordSet.find(curr) != wordSet.end()) {
                            q.push(curr);
                            // 關鍵優化：一旦訪問過，就從字典中移除
                            // 這相當於標記為 visited，防止重複訪問和死循環
                            wordSet.erase(curr);
                        }
                    }
                    
                    // 還原字符，以便嘗試下一個位置的變換
                    curr[j] = originalChar;
                }
            }
            // 每遍歷完一層，路徑長度加 1
            level++;
        }
        
        return 0; // 無法到達
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times L \times 26)$
    -   $M$: Number of words in list.
    -   $L$: Length of each word.
    -   Each word is processed at most once. For each word, we iterate $L$ positions and try 26 chars.
-   **Space Complexity**: $O(M \times L)$
    -   Queue and Set store words.
