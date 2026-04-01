---
title: "01. Valid Palindrome"
description: "題目要求我們寫一個函式來判斷一個字串 `s` 是否為 **Palindrome (回文)**。 所謂「回文」，是指正著讀跟反著讀都一樣的字串。 但是在比對之前，我們必須先進行**資料清洗 (Data Cleaning)**："
tags:
  - Two Pointers
  - Array
difficulty: Easy
---

![Two Pointers Hero](../assets/images/banners/two_pointers.png){ class="header-banner" }

# 01. Valid Palindrome <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #125** — [題目連結](https://leetcode.com/problems/valid-palindrome/) | [NeetCode 解說](https://neetcode.io/problems/is-palindrome)


(驗證回文串)

## 1. 🧐 Problem Dissection (釐清問題)

題目要求我們寫一個函式來判斷一個字串 `s` 是否為 **Palindrome (回文)**。
所謂「回文」，是指正著讀跟反著讀都一樣的字串。
但是在比對之前，我們必須先進行**資料清洗 (Data Cleaning)**：

1.  **Case Insensitive**: 大寫字母要視為小寫（'A' == 'a'）。
2.  **Alphanumeric Only**: 只保留字母 (a-z) 和數字 (0-9)，忽略所有其他符號（如空白、逗號、冒號等）。

- **Input**: "A man, a plan, a canal: Panama"
- **Output**: `true`
  - 解釋：清洗後變成 "amanaplanacanalpanama"，這是一個回文。
- **Input**: "race a car"
- **Output**: `false`
  - 解釋：清洗後變成 "raceacar"，reversed 是 "racaecar"，不匹配。

- **Constraints**:
  - $1 <= s.length <= 2 * 10^5$。
  - 字串包含 Printable ASCII characters。

---

## 2. 🐢 Brute Force Approach (暴力解)

最直覺的方法是依序執行以下步驟：

1.  建立一個新的字串 `filtered_s`。
2.  遍歷原字串 `s`，如果字元是 alphanumeric，就轉成小寫並 append 到 `filtered_s`。
3.  建立一個反轉字串 `reversed_s = reverse(filtered_s)`。
4.  比較 `filtered_s == reversed_s`。

- **Time Complexity**: $O(n)$。我們遍歷了幾次字串，但總體還是線性的。
- **Space Complexity**: $O(n)$。我們需要額外的記憶體來儲存 `filtered_s` 和 `reversed_s`。
- **Trade-off**: 這方法簡單易懂，但在 Embedded System 中，如果字串很長 (e.g., Log file)，分配額外記憶體可能會導致 OOM (Out of Memory) 或增加 Memory Fragmentation。我們能否原地 (In-place) 完成？

---

## 3. 💡 The "Aha!" Moment (優化)

**Two Pointers (雙指標)** 是處理「陣列/字串前後比對」問題的標準武器。

我們不需要建立新字串，直接在原字串上跑：

1.  設定 `left` 指標在開頭，`right` 指標在結尾。
2.  當 `left < right` 時：
    - 如果你是指標，你會遇到什麼問題？ -> "中間有很多垃圾符號"。
    - 所以，如果 `s[left]` 不是 alphanumeric，`left` 就一直往右移。
    - 如果 `s[right]` 不是 alphanumeric，`right` 就一直往左移。
    - 當兩邊都停在「有效字元」上時，比對它們（轉小寫後）。
    - 如果不一樣 -> `return false`。
    - 如果一樣 -> `left++`, `right--`，繼續縮小範圍。
3.  如果指標交錯都沒發現錯誤，那就是 `true`。

- **優點**：完全不需要額外記憶體 allocation。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../valid_palindrome_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../valid_palindrome_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Two Pointers (In-place)

```cpp
#include <string>
#include <cctype> // for isalnum, tolower

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // 1. Move left pointer if not alphanumeric
            // 注意邊界檢查 left < right，防止越界 (雖然後面有總 while 擋著，但 inner loop 也要小心)
            while (left < right && !isalnum(s[left])) {
                left++;
            }

            // 2. Move right pointer if not alphanumeric
            while (left < right && !isalnum(s[right])) {
                right--;
            }

            // 3. Compare characters (case-insensitive)
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }

            // 4. Update pointers
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
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        // 定義雙指標，分別指向頭尾
        int L = 0;
        int R = s.size() - 1;

        // 迴圈條件：當左指標還在右指標左邊時繼續
        while (L < R) {
            // Step 1: 略過左邊的非英數字符
            // isalnum() 是標準庫函式，檢查是否為 A-Z, a-z, 0-9
            while (L < R && !isalnum(s[L])) {
                L++;
            }

            // Step 2: 略過右邊的非英數字符
            while (L < R && !isalnum(s[R])) {
                R--;
            }

            // Step 3: 比對字符
            // tolower() 將大寫轉小寫，非字母則不變
            if (tolower(s[L]) != tolower(s[R])) {
                return false; // 發現不匹配，立即回傳失敗
            }

            // 收縮範圍
            L++;
            R--;
        }

        return true;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - `left` 指標只會往右走，`right` 指標只會往左走。
  - 兩者最多在中間相遇，總共遍歷的字元數不超過 $n$。
  - `isalnum` 和 `tolower` 都是 $O(1)$ 操作。
- **Space Complexity**: $O(1)$
  - 即使字串長度 $10^5$，我們也只用了 2 個整數變數 (`L`, `R`) 來記錄位置。
  - 這是 **In-place** 演算法，對 Memory 非常友善。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如何處理 Unicode 和多語言？
- 如果允許刪除一個字元呢？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有忽略非字母數字字元
- ⚠️ 大小寫處理錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 一次遍歷完成
- 💎 主動討論雙指標的優勢

---

## 📚 Related Problems (相關題目)

### 站內相關

### 進階挑戰
- [Valid Palindrome Ii](https://leetcode.com/problems/valid-palindrome-ii/) — LeetCode
