# Longest Repeating Character Replacement (替換後的最長重複字元子串) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #424** — [題目連結](https://leetcode.com/problems/longest-repeating-character-replacement/) | [NeetCode 解說](https://neetcode.io/problems/longest-repeating-character-replacement)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字串 `s` 和一個整數 `k`。
我們最多可以將字串中的任意 `k` 個字元替換成其他字元。
目標是：在替換不超過 `k` 次的情況下，找出最常的子字串，該子字串由 **完全相同的字元** 組成。
回傳該長度。

- **Input**: `s = "ABAB", k = 2`
- **Output**: `4` (Change both 'A's to 'B' -> "BBBB", or both 'B's to 'A' -> "AAAA")
- **Input**: `s = "AABABBA", k = 1`
- **Output**: `4` (Replace middle 'B' with 'A' -> "AAAABBA", the "AAAA" part)
- **Constraints**:
  - $s.length <= 10^5$.
  - 只包含 uppercase English letters. (Count array size 26).

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試所有可能的子字串 `s[i...j]`。
對於每個子字串：

1.  找出出現最多次的字元頻率 `maxFreq`。
2.  計算需要替換的字元數：`replacements = length - maxFreq`。
3.  如果 `replacements <= k`，則此子字串合法，更新 Max Length。

- **Time**: $O(n^3)$ or $O(n^2)$.
- **Result**: TLE.

---

## 3. 💡 The "Aha!" Moment (優化)

這也是一個 **Sliding Window** 問題。

我們維護一個窗口 `[left, right]`，以及窗口內每個字母的計數 `count`。
對於任何窗口，要把它變成「全字母相同」，最好的策略是：
**保留出現次數最多的那個字母 (Dominant Character)，把其他所有雜魚都換掉。**

所以，窗口是否合法的條件是：
`WindowLength - MaxFrequency <= k`

`WindowLength` = `right - left + 1`
`MaxFrequency` = 窗口內出現最多次的那個字母的次數。

演算法：

1.  Expand `right`。
2.  Update `count[s[right]]`，並可能更新全局 `maxFreq` (注意這裡有個小優化)。
3.  Check condition: `(r - l + 1) - maxFreq > k`?
    - 如果 True (需要替換太多)，則窗口無效。
    - Shrink `left` (move `left` forward)，並更新 `count[s[left]]--`。
4.  Update global `result`.

**關於 maxFreq 的優化**:
當我們 Shrink `left` 時，`maxFreq` 可能會下降 (如果我們移除的是 Dominant Char)。
但在求「最長」子字串的問題中，我們其實不需要精確縮小 `maxFreq`。
因為只有當我們找到一個比歷史 `maxFreq` 更大的頻率時，窗口才有可能**突破歷史最大長度**。
所以我們只需要維護一個歷史最大 `maxFreq` 即可，這讓邏輯簡化很多。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../longest_repeating_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../longest_repeating_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Sliding Window

```cpp
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);
        int left = 0;
        int maxFreq = 0; // 當前窗口內出現最多次字母的次數
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            // Update count
            count[s[right] - 'A']++;

            // Update maxFreq
            // 這裡的 maxFreq 可以是「歷史窗口最大」或「當前窗口最大」
            // 為了嚴謹，標準做法是維護「當前」。
            // 但在這裡，我們用歷史最大也行，因為如果 shrinking 導致 maxFreq 變小，
            // 窗口長度勢必也變小，不可能更新 result。只有 maxFreq 變大才可能創紀錄。
            maxFreq = max(maxFreq, count[s[right] - 'A']);

            // Check condition
            // window_len - maxFreq 就是「需要被替換的雜魚數量」
            if ((right - left + 1) - maxFreq > k) {
                // 如果需要替換得太多，就要縮小窗口
                count[s[left] - 'A']--;
                left++;
                // 注意：這裡不需要重新掃描 count 來找新的 maxFreq
                // 雖然真正的 maxFreq 可能變小了，但這不影響我們找「更長」的目標
            }

            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};
```

### Python Reference

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        // 頻率表，只包含 A-Z
        vector<int> count(26, 0);
        int l = 0;
        int maxf = 0; // 窗口中最頻繁字元的數量
        int res = 0;

        for (int r = 0; r < s.length(); r++) {
            // 加入新的字元 s[r]
            count[s[r] - 'A']++;

            // 更新 maxf
            // 這一步很關鍵：我們允許 maxf 稍微「不準確」(偏大)。
            // 有效條件是 len - maxf <= k。
            // 也就是 len <= maxf + k。
            // 我們想要 maximize len，所以我們需要更大的 maxf。
            // 如果 shrink 導致真實的 local maxf 變小，那 len 也不可能變大。
            // 我們只在乎有沒有機會讓 maxf 變大。
            maxf = max(maxf, count[s[r] - 'A']);

            // 檢查有效性
            // 窗口長度 - 最頻繁字元數 = 其他雜魚數 (需要被替換的)
            // 如果雜魚數 > k，我們就沒救了，必須 shrink
            if ((r - l + 1) - maxf > k) {
                // shrink 左邊
                count[s[l] - 'A']--;
                l++;
            }

            // 這裡的窗口保證是有效的 (或是剛剛 shrink 到變有效了)
            // 實際上，這寫法 window 寬度只會增加不會減少 (因為 if 裡面 l 只有 ++ 一次)
            // 所以最終 (r - l + 1) 不一定是當下 valid 的長度，但一定遍歷過的最大 valid 長度。
            res = max(res, r - l + 1);
        }

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - `right` 掃描一遍 $0 \to n$。
  - `left` 掃描一遍 $0 \to n$。
  - 總共 $2n$ operations。
- **Space Complexity**: $O(1)$
  - 我們使用了一個大小為 26 的陣列 `count`。這與 `n` 無關。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果有多種字元可替換？
- 如何處理大小寫？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有維護窗口內最多字元計數
- ⚠️ 替換次數計算錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 理解 maxCount 不需要遞減的巧妙設計
- 💎 公式: window_size - maxCount <= k

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Longest Substring Without Repeating Characters (無重複字元的最長子字串)](02_Longest_Substring_Without_Repeating.md)
