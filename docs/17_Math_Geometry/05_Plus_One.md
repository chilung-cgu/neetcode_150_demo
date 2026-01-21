# Plus One (加一) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #66** — [題目連結](https://leetcode.com/problems/plus-one/) | [NeetCode 解說](https://neetcode.io/problems/plus-one)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個**大整數**，以陣列 `digits` 形式表示（最高位在前）。
請計算該整數 **加 1** 後的結果，並以同樣的陣列形式回傳。

-   **Input**: `digits = [1,2,3]`
-   **Output**: `[1,2,4]`
-   **Input**: `digits = [4,3,2,1]`
-   **Output**: `[4,3,2,2]`
-   **Input**: `digits = [9]`
-   **Output**: `[1,0]`
-   **Input**: `digits = [9,9]`
-   **Output**: `[1,0,0]`

主要挑戰在於**進位 (Carry)**。
如果全部都是 9，例如 `[9,9,9]`，結果會變長 `[1,0,0,0]`。

---

## 2. 🐢 Brute Force Approach (暴力解)

將陣列轉換為數字（例如 `[1,2,3]` -> `123`），加 1，再轉換回陣列。
問題：整數溢出。如果輸入有 100 位數，根本存不下。
必須直接在陣列上操作。

---

## 3. 💡 The "Aha!" Moment (優化)

**Iterate Backwards (Digit by Digit)**:
從最後一位開始遍歷 `digits[i]`：

1.  如果 `digits[i] < 9`：
    -   `digits[i]++`。
    -   沒有進位，任務結束，直接回傳 `digits`。
2.  如果 `digits[i] == 9`：
    -   `digits[i] = 0`。
    -   繼續向前遍歷（處理進位）。
3.  如果遍歷完整個陣列還沒回傳（例如 `[9,9,9]` 變成了 `[0,0,0]`）：
    -   說明所有位數都是 9，產生了新的最高位。
    -   創建一個新陣列，長度為 `n+1`，第一位為 `1`，其餘為 `0`。
    -   或者直接在原陣列前插入 `1`（如果語言支持動態數組）。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../plus_one_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../plus_one_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterate Backwards

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();

        // Iterate from the last digit to the first
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits; // No carry, return immediately
            }
            // Carry happens, set current digit to 0
            digits[i] = 0;
        }

        // If we're here, it means all digits were 9 (e.g., 999 -> 000)
        // Need to add a leading 1 (999 -> 1000)
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

### Python Reference

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        # If all digits were 9
        return [1] + digits
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();

        // 從個位數（陣列末尾）開始向前遍歷
        for (int i = n - 1; i >= 0; i--) {
            // 如果當前位數小於 9，直接加 1 就不會有進位
            if (digits[i] < 9) {
                digits[i]++;
                // 不需要處理前面的位數了，直接回傳結果
                return digits;
            }

            // 如果當前位數是 9，加 1 後變成 10
            // 該位數變為 0，並產生進位傳給下一輪 (i-1)
            digits[i] = 0;
        }

        // 程式執行到這裡，意味著所有的位數都是 9 (例如 99 -> 00)
        // 我們需要在最前面補一個 1 (變成 100)
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   In worst case (all 9s), we iterate mostly once.
    -   `insert` at begin might take $O(N)$ in C++ (moving elements). But amortized it's fine.
-   **Space Complexity**: $O(1)$
    -   In-place modification (ignoring input/output space).

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
