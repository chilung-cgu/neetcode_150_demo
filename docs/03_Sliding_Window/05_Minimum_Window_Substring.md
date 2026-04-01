---
title: "Minimum Window Substring (最小覆蓋子字串)"
description: "題目給兩個字串 `s` 和 `t`。請在 `s` 中找出一個 **最短子字串**，該子字串包含 `t` 中的 **所有字元 (包含重複數量)**。 如果不存在，回傳空字串 `""`。"
tags:
  - Sliding Window
  - String
difficulty: Hard
---

# Minimum Window Substring (最小覆蓋子字串) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

> 📌 **LeetCode #76** — [題目連結](https://leetcode.com/problems/minimum-window-substring/) | [NeetCode 解說](https://neetcode.io/problems/minimum-window-with-characters)


## 1. 🧐 Problem Dissection (釐清問題)

題目給兩個字串 `s` 和 `t`。請在 `s` 中找出一個 **最短子字串**，該子字串包含 `t` 中的 **所有字元 (包含重複數量)**。
如果不存在，回傳空字串 `""`。

- **Input**: `s = "ADOBECODEBANC", t = "ABC"`
- **Output**: `"BANC"` (包含 A, B, C，長度 4)。雖然 "ADOBEC" 也包含，但長度 6 太長。
- **Input**: `s = "a", t = "aa"`
- **Output**: `""` (s 只有一個 a，不夠 t 的兩個 a)。
- **Constraints**:
  - $m, n <= 10^5$.
  - 英文字母 (大小寫敏感)。

---

## 2. 🐢 Brute Force Approach (暴力解)

找出 `s` 所有的 substring，檢查是否 covering `t`。

- **Time**: $O(n^3)$ or $O(n^2)$.
- **Result**: TLE.

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 "Permutation in String" 的**動態長度版**。

1.  **Map**: 我們需要一個 `targetMap` 記錄 `t` 中每個字元需要的次數。
2.  **Window**: 維護一個窗口 `[left, right]` 和 `windowMap`。
3.  **Count `have` vs `need`**:
    - 我們不需要每次都比對兩個整個 Map ($O(52)$)。
    - 我們可以維護兩個變數：
      - `need`: `t` 中有多少個 **獨特 (Unique) 字元** 需要被滿足。
      - `have`: 目前窗口中，有多少個獨特字元 **已經達標** (次數 >= target)。
4.  **Flow**:
    - **Expand (`right`)**: 加入字元。如果該字元的 `windowCount == targetCount`，則 `have++`。
    - **Shrink (`left`)**: 當 `have == need` 時，表示目前窗口是合法的 (Valid)。我們嘗試縮小它 (move `left`) 來找最小長度。
      - 移出字元前，先記錄當前長度 `right - left + 1`，如果比 `minLen` 小就更新。
      - 移出字元。如果該字元的 `windowCount < targetCount`，則 `have--`。這時窗口變回非法，跳出 shrink loop，繼續 expand。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../minimum_window_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../minimum_window_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Optimized Sliding Window

```cpp
#include <string>
#include <vector>
#include <climits>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty()) return "";

        unordered_map<char, int> countT, window;
        for (char c : t) countT[c]++;

        int have = 0, need = countT.size();
        int res[2] = {-1, -1};
        int resLen = INT_MAX;
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s[r];
            window[c]++;

            // 如果此字元在 t 中，且數量剛好達標，have+1
            if (countT.count(c) && window[c] == countT[c]) {
                have++;
            }

            // 當所有條件都滿足時，嘗試縮小窗口
            while (have == need) {
                // update result
                if (r - l + 1 < resLen) {
                    res[0] = l;
                    res[1] = r;
                    resLen = r - l + 1;
                }

                // pop from left
                window[s[l]]--;
                if (countT.count(s[l]) && window[s[l]] < countT[s[l]]) {
                    have--;
                }
                l++;
            }
        }

        return resLen == INT_MAX ? "" : s.substr(res[0], resLen);
    }
};
```

### Python Reference

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # Update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # pop from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";

        // 使用 Array 優化 Map，因為是 char (ASCII 128)
        vector<int> countT(128, 0);
        vector<int> window(128, 0);

        for (char c : t) countT[c]++;

        // 統計 t 有多少種「獨特」字符需要被滿足
        int need = 0;
        for (int i = 0; i < 128; i++) {
            if (countT[i] > 0) need++;
        }

        int have = 0;
        int l = 0;
        int minLen = INT_MAX;
        int startL = 0; // 記錄最佳解的起始位置

        for (int r = 0; r < s.size(); r++) {
            char c = s[r];
            window[c]++;

            // 關鍵：只有當數量「剛好」達到 target 時，have 才加 1
            // 如果數量超過 target，have 不變 (因為這個 char 早就達標了)
            if (countT[c] > 0 && window[c] == countT[c]) {
                have++;
            }

            // 當所有獨特字符都達標 (have == need) -> 窗口合法
            while (have == need) {
                // 1. 嘗試比較當前長度，若是最小值則更新
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    startL = l;
                }

                // 2. 嘗試移出左邊元素 (shrink) 到非法為止
                char leftChar = s[l];
                window[leftChar]--;

                // 如果移除這個字導致該字符數量 < target，那麼窗口變為非法，只能跳出迴圈繼續找右邊
                if (countT[leftChar] > 0 && window[leftChar] < countT[leftChar]) {
                    have--;
                }

                l++;
            }
        }

        return minLen == INT_MAX ? "" : s.substr(startL, minLen);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n + m)$
  - $O(m)$ 建立 `countT`。
  - $O(n)$ 掃描 `s`。雖然有 inner loop，但 `left` 和 `right` 都只前進不後退，所以是 $2n$。
- **Space Complexity**: $O(1)$ (Assuming size of charset is fixed 128/256)
  - 如果 charset 很大，則是 $O(k)$ where k is unique chars。

---

## 7. 💼 Interview Tips (面試技巧) ⭐ 高頻題

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果需要返回所有最小視窗？
- 如何處理重複字元？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有正確計算 required/formed
- ⚠️ 窗口收縮條件錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 O(n) 時間複雜度
- 💎 清晰的擴展/收縮邏輯

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Permutation in String (字串的排列包含)](04_Permutation_in_String.md)
