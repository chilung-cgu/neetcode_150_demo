# Palindromic Substrings (回文子字串個數)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字串 `s`，計算其中有多少個回文子字串。
相同內容但位置不同的子字串，視為不同的。

-   **Input**: `s = "abc"`
-   **Output**: `3` ("a", "b", "c")
-   **Input**: `s = "aaa"`
-   **Output**: `6` ("a", "a", "a", "aa", "aa", "aaa")
-   **Constraints**:
    -   $1 <= s.length <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

與上題類似，枚舉所有子字串 ($O(N^2)$) 並檢查是否回文 ($O(N)$)。
總時間 $O(N^3)$。太慢。

---

## 3. 💡 The "Aha!" Moment (優化)

這題根本就是 **Longest Palindromic Substring** 的變形。
我們同樣可以使用 **Expand Around Center**。
每一個中心點，向外擴展，**每擴展成功一次，計數就 +1**。

中心點：
-   單字元中心：$N$ 個。
-   雙字元中心：$N-1$ 個。

-   **Time**: $O(N^2)$。這是最優解。

---

## 4. 💻 Implementation (程式碼)

### Approach: Expand Around Center

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Count odd length palindromes centered at i
            count += countPalindromes(s, i, i);
            
            // Count even length palindromes centered at i and i+1
            count += countPalindromes(s, i, i + 1);
        }
        
        return count;
    }
    
private:
    int countPalindromes(const string& s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            count++;
            left--;
            right++;
        }
        return count;
    }
};
```

### Python Reference

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # Odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # Even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        return count
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int totalCount = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // 1. 奇數長度回文，以 s[i] 為中心 (e.g. "a", "aba")
            totalCount += expand(s, i, i);
            
            // 2. 偶數長度回文，以 s[i], s[i+1] 為中心 (e.g. "aa", "abba")
            totalCount += expand(s, i, i + 1);
        }
        
        return totalCount;
    }
    
    // 擴展函數：回傳以此中心擴展得到的「回文個數」 (不是長度)
    int expand(const string& s, int l, int r) {
        int count = 0;
        // 只要還在邊界內且字符相等，就是一個新的回文
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            count++;
            l--;
            r++;
        }
        return count;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^2)$
    -   Expanding around each center takes up to $O(N)$.
    -   There are $2N-1$ centers.
-   **Space Complexity**: $O(1)$
    -   No extra space.
