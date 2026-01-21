# Palindrome Partitioning (分割回文串) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #131** — [題目連結](https://leetcode.com/problems/palindrome-partitioning/) | [NeetCode 解說](https://neetcode.io/problems/palindrome-partitioning)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字串 `s`，將 `s` 分割成若干個子字串，使得 **每一個子字串都是回文 (Palindrome)**。
回傳所有可能的分割方案。

-   **Input**: `s = "aab"`
-   **Output**: `[["a","a","b"],["aa","b"]]`
-   **Input**: `s = "a"`
-   **Output**: `[["a"]]`
-   **Constraints**:
    -   $1 <= s.length <= 16$
    -   s contains only lowercase English letters.

---

## 2. 🐢 Brute Force Approach (暴力解)

**Backtracking**:
從 index 0 開始，嘗試切割出第一段 `s[0...i]`。
如果 `s[0...i]` 是回文，則遞迴處理剩餘的 `s[i+1...]`。

-   **Time**: $O(N \times 2^N)$。最壞情況（如 "aaaa"），每個切割點都可行。
-   **Space**: $O(N)$ stack.

---

## 3. 💡 The "Aha!" Moment (優化)

這題是典型的 backtracking，規模很小 ($N=16$)。
優化點在於 **如何快速判斷 `s[start...i]` 是否為回文**。

1.  **Naive check**: 雙指標從兩頭往中間掃，時間 $O(L)$。總時間複雜度約 $O(N \cdot 2^N)$。因為 $N=16$，這樣完全可以。
2.  **DP Precomputation (Optional)**:
    -   建立一個 $N \times N$ 的 table `isPalindrome[i][j]`。
    -   `isPalindrome[i][j] = (s[i] == s[j]) && isPalindrome[i+1][j-1]`。
    -   這樣查詢回文只要 $O(1)$。
    -   但由於 $N$ 很小，這個優化對實際運行時間影響不大，甚至可能因為 overhead 變慢。面試時可以提到。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../palindrome_partition_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../palindrome_partition_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking with Naive Palindrome Check

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> current;
        dfs(s, 0, current, result);
        return result;
    }

private:
    void dfs(const string& s, int start, vector<string>& current, vector<vector<string>>& result) {
        // Base case: Reached end of string
        if (start == s.length()) {
            result.push_back(current);
            return;
        }

        for (int i = start; i < s.length(); i++) {
            // Check if substring s[start...i] is a palindrome
            if (isPalindrome(s, start, i)) {
                // If yes, include it in partition
                current.push_back(s.substr(start, i - start + 1));

                // Recurse for the rest
                dfs(s, i + 1, current, result);

                // Backtrack
                current.pop_back();
            }
        }
    }

    bool isPalindrome(const string& s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
```

### Python Reference

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> path; // 存放當前的分割方案
        dfs(s, 0, path, res);
        return res;
    }

    // start: 當前要開始切割的起始位置
    void dfs(const string& s, int start, vector<string>& path, vector<vector<string>>& res) {
        // 如果 start 已經到底，代表整個字串都被成功分割了
        if (start == s.size()) {
            res.push_back(path);
            return;
        }

        // 嘗試所有可能的切割終點 i
        for (int i = start; i < s.size(); i++) {
            // 判斷 s[start ... i] 是否回文
            if (isPalindrome(s, start, i)) {
                // 是回文，加入當前方案
                path.push_back(s.substr(start, i - start + 1));

                // 繼續處理剩下的字串 (從 i + 1 開始)
                dfs(s, i + 1, path, res);

                // Backtrack：移除剛才加進去的子字串，嘗試下一個切割點
                path.pop_back();
            }
        }
    }

    // 檢查回共有 helper function
    bool isPalindrome(const string& s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \cdot 2^N)$
    -   In the worst case (e.g., "aaaa"), we have $2^{N-1}$ possible partition points.
    -   Checking palindrome takes $O(N)$.
    -   Copying result takes $O(N)$.
-   **Space Complexity**: $O(N)$
    -   Max recursion depth is $N$.
