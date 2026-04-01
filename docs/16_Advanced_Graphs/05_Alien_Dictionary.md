---
title: "Alien Dictionary (外星人字典)"
description: "有一種外星語言，使用英語字母，但順序不同。 給定一份該語言的單詞列表 `words`，其中的單詞已經 **按照該語言的字典序排序**。 請你根據這份列表，推導出該語言中字母的順序。 如果有多種可能的順序，回傳任意一種。 如果給定的列表不合法（無法推導出有效順序），回傳空字串 `""`。"
tags:
  - Graph
  - Dijkstra
  - MST
difficulty: Hard
---

# Alien Dictionary (外星人字典) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

> 📌 **LeetCode #269** — [題目連結](https://leetcode.com/problems/alien-dictionary/) | [NeetCode 解說](https://neetcode.io/problems/foreign-dictionary)


## 1. 🧐 Problem Dissection (釐清問題)

有一種外星語言，使用英語字母，但順序不同。
給定一份該語言的單詞列表 `words`，其中的單詞已經 **按照該語言的字典序排序**。
請你根據這份列表，推導出該語言中字母的順序。
如果有多種可能的順序，回傳任意一種。
如果給定的列表不合法（無法推導出有效順序），回傳空字串 `""`。

-   **Input**: `["wrt", "wrf", "er", "ett", "rftt"]`
-   **Output**: `"wertf"`
-   **Input**: `["z", "x"]`
-   **Output**: `"zx"`
-   **Input**: `["z", "x", "z"]`
-   **Output**: `""` (Cycle: z < x and x < z)
-   **Logic**:
    -   比較相鄰的兩個單詞 `w1` 和 `w2`。
    -   找到第一個不同的字母，例如 `w1[i]` 和 `w2[i]`。
    -   由於 `w1` 排在 `w2` 前面，這意味著字母 `w1[i]` 在字母表中排在 `w2[i]` 前面。這構成一條有向邊 `w1[i] -> w2[i]`。
    -   如果 `w1` 是 `w2` 的前綴且 `w1.length > w2.length`（例如 `["apple", "app"]`），這是不合法的，直接回傳空。

---

## 2. 🐢 Brute Force Approach (暴力解)

這是典型的 **拓撲排序 (Topological Sort)** 問題。
暴力解實際上就是構建圖並遍歷。沒有特別的 "Brute Force" 替代方案。

---

## 3. 💡 The "Aha!" Moment (優化)

**Algorithm (Kahn's Algorithm - BFS)**:

1.  **Build Graph**:
    -   初始化 `adj` (Map<Char, Set<Char>>) 和 `indegree` (Map<Char, Int>)。
    -   將所有出現過的字符都加入 `indegree` 並設為 0（確保所有字符都被考慮）。
    -   遍歷相鄰單詞對 `(w1, w2)`：
        -   找出第一個不同的字符 `c1, c2`。
        -   如果 `w2` 是 `w1` 的前綴但 `len(w1) > len(w2)`，return `""`。
        -   否則，添加邊 `c1 -> c2`。
        -   更新 `indegree[c2]++`。
2.  **BFS (Topological Sort)**:
    -   將所有 `indegree == 0` 的字符加入 Queue。
    -   BFS loop:
        -   Pop `curr`，Append to `result`。
        -   遍歷鄰居 `next`， `indegree[next]--`。
        -   如果 `indegree` 變為 0，Push `next`。
3.  **Check Cycle**:
    -   如果 `result.length == unique_chars.size()`，回傳 `result`。
    -   否則，說明有環，回傳 `""`。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../alien_dictionary_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../alien_dictionary_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Kahn's Algorithm (BFS)

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> adj;
        unordered_map<char, int> indegree;

        // 1. Initialize indegree for all unique characters
        for (const string& w : words) {
            for (char c : w) {
                indegree[c] = 0;
            }
        }

        // 2. Build Graph
        for (int i = 0; i < words.size() - 1; i++) {
            string w1 = words[i];
            string w2 = words[i+1];

            // Check prefix edge case (e.g., "abc", "ab" is invalid)
            if (w1.size() > w2.size() && w1.compare(0, w2.size(), w2) == 0) {
                return "";
            }

            // Find first difference
            for (int j = 0; j < min(w1.size(), w2.size()); j++) {
                if (w1[j] != w2[j]) {
                    // w1[j] comes before w2[j]
                    if (adj[w1[j]].find(w2[j]) == adj[w1[j]].end()) {
                        adj[w1[j]].insert(w2[j]);
                        indegree[w2[j]]++;
                    }
                    break; // Only the first difference determines order
                }
            }
        }

        // 3. BFS (Topological Sort)
        queue<char> q;
        for (auto const& [key, val] : indegree) {
            if (val == 0) {
                q.push(key);
            }
        }

        string result = "";
        while (!q.empty()) {
            char curr = q.front();
            q.pop();
            result += curr;

            for (char neighbor : adj[curr]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        // 4. Verify no cycles
        if (result.size() != indegree.size()) {
            return "";
        }

        return result;
    }
};
```

### Python Reference

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False=visited, True=current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)
            return False

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {
        // adj: 鄰接表，Key: 字符，Value: 它的後繼字符集合
        unordered_map<char, unordered_set<char>> adj;
        // indegree: 入度表，Key: 字符，Value: 入度
        unordered_map<char, int> indegree;

        // 1. 初始化：收集所有出現過的唯一字符
        for (const string& w : words) {
            for (char c : w) {
                indegree[c] = 0;
            }
        }

        // 2. 建圖：比較相鄰單詞
        for (int i = 0; i < words.size() - 1; i++) {
            string w1 = words[i];
            string w2 = words[i+1];

            // 特殊情況檢查：前綴問題
            // 如果 w2 是 w1 的前綴且 w2 更短 (例如 "abc", "ab")，這在字典序中是不合法的
            // 因為 "ab" 應該排在 "abc" 前面
            if (w1.size() > w2.size() && w1.compare(0, w2.size(), w2) == 0) {
                return "";
            }

            // 找出第一個不同的字符
            for (int j = 0; j < min(w1.size(), w2.size()); j++) {
                if (w1[j] != w2[j]) {
                    // w1[j] 排在 w2[j] 前面 -> 建立有向邊 w1[j] -> w2[j]

                    // 避免重複添加邊 (這會導致入度計算錯誤)
                    if (adj[w1[j]].find(w2[j]) == adj[w1[j]].end()) {
                        adj[w1[j]].insert(w2[j]);
                        indegree[w2[j]]++;
                    }
                    // 找到第一個不同點就停止比較這兩個單詞
                    break;
                }
            }
        }

        // 3. BFS 拓撲排序 (Kahn's Algorithm)
        queue<char> q;
        // 將所有入度為 0 的字符加入 Queue
        for (auto const& [key, val] : indegree) {
            if (val == 0) {
                q.push(key);
            }
        }

        string result = "";
        while (!q.empty()) {
            char curr = q.front();
            q.pop();
            result += curr;

            // 遍歷後繼字符
            for (char neighbor : adj[curr]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        // 4. 環檢測
        // 如果結果長度不等於字符總數，說明圖中有環
        if (result.size() != indegree.size()) {
            return "";
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(C)$
    -   $C$ - total length of all words.
    -   We iterate through all characters to initialize.
    -   Building graph takes $O(C)$ comparisons.
    -   BFS takes $O(V + E)$, where $V \le 26, E \le 26^2$. Since limited by alphabet size, it's effectively constant relative to large input words.
-   **Space Complexity**: $O(1)$ or $O(U + min(U^2, N))$
    -   $U$ is number of unique characters (max 26).
    -   Storage for adj list and indegree is bounded by alphabet size.

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
- [Course Schedule (課程表)](../15_Graphs/08_Course_Schedule.md)
