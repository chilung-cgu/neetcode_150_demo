# Happy Number (快樂數)

## 1. 🧐 Problem Dissection (釐清問題)

一個**快樂數**定義如下：

1.  對於一個正整數 $n$，將每個位數的平方相加，得到一個新的數。
2.  重複該過程。
3.  如果最後變成 `1`，則它是快樂數。
4.  如果進入一個 **不包含 1 的循環**，則它不是快樂數。

-   **Input**: `n = 19`
-   **Output**: `true`
    -   $1^2 + 9^2 = 82$
    -   $8^2 + 2^2 = 68$
    -   $6^2 + 8^2 = 100$
    -   $1^2 + 0^2 + 0^2 = 1$
-   **Input**: `n = 2`
-   **Output**: `false`
    -   $2 \to 4 \to 16 \to 37 \to 58 \to 89 \to 145 \to 42 \to 20 \to 4$ (Cycle detected).

---

## 2. 🐢 Brute Force Approach (暴力解)

使用 HashSet 記錄出現過的數字。
每次計算新的平方和：

-   如果等於 1，Return True。
-   如果已經在 Set 中，Return False (Cycle Detected)。
-   否則加入 Set，繼續。

這是否會陷入無限增長？
不會。對於較大的數字，下一項會變小。
例如 $999 \to 81+81+81 = 243$。
$9999 \to 324$。
所以它最終會收斂到一個較小的範圍（幾百以內）並形成循環。

---

## 3. 💡 The "Aha!" Moment (優化)

**Floyd's Tortoise and Hare (Cycle Detection)**:
這本質上是在鏈表中檢測環。
每一個數指向它的下一個數（平方和）。
我們可以使用快慢指針：

-   `slow` 每次走一步。
-   `fast` 每次走兩步。
-   如果 `fast` 遇到 1，它是快樂數。
-   如果 `slow` 追上 `fast`，說明有環，不是快樂數。
-   空間複雜度降為 $O(1)$。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../happy_number_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../happy_number_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Fast & Slow Pointers

```cpp
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = sumOfSquares(n);

        while (fast != 1 && slow != fast) {
            slow = sumOfSquares(slow);            // Move 1 step
            fast = sumOfSquares(sumOfSquares(fast)); // Move 2 steps
        }

        return fast == 1;
    }

private:
    int sumOfSquares(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
};
```

### Python Reference

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSq(n)

        while fast != 1 and slow != fast:
            slow = self.sumSq(slow)
            fast = self.sumSq(self.sumSq(fast))

        return fast == 1

    def sumSq(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isHappy(int n) {
        // Floyd's Tortoise and Hare Algorithm
        // 慢指針 (Tortoise)
        int slow = n;
        // 快指針 (Hare)，先走一步，確保進入循環條件
        int fast = sumOfSquares(n);

        // 條件：如果 fast 到達 1，我們成功了
        // 如果 slow == fast，我們發現了環，失敗了
        while (fast != 1 && slow != fast) {
            slow = sumOfSquares(slow);            // 慢指針走一步
            fast = sumOfSquares(sumOfSquares(fast)); // 快指針走兩步
        }

        // 如果是因為 fast == 1 退出，則為真
        // 如果是因為 slow == fast 退出且不為 1，則為假
        return fast == 1;
    }

private:
    // 輔助函數：計算各位數字的平方和
    int sumOfSquares(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log N)$
    -   Finding the next number involves iterating through digits, which is $O(\log N)$.
    -   The cycle length is small and constant for 32-bit integers.
-   **Space Complexity**: $O(1)$
    -   No extra data structures (unlike HashSet solution).
