# Counting Bits (計算位元)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個整數 `n`。
請回傳一個長度為 `n + 1` 的陣列 `ans`，對於每個 `i` ($0 \le i \le n$)，`ans[i]` 表示數字 `i` 的二進制表示中 `1` 的個數。
請**不要**對每個數字調用 `popcount` 或 `hammingWeight` 函數，這將導致 $O(k \times n)$ 的複雜度。
請設計一個 **$O(n)$** 的算法。

-   **Input**: `n = 2`
-   **Output**: `[0,1,1]`
    -   0 (0), 1 (1), 2 (10 -> 1)
-   **Input**: `n = 5`
-   **Output**: `[0,1,1,2,1,2]`

---

## 2. 🐢 Brute Force Approach (暴力解)

對 0 到 n 的每個數字調用前一題的 `hammingWeight`。

-   **Time**: $O(n \times \log n)$。
-   雖然 `log n` 很小 (32)，但我們可以做得更好。

---

## 3. 💡 The "Aha!" Moment (優化)

**Dynamic Programming (Bit Manipulation Relations)**:
觀察二進制數字的規律：

-   `0`: 0 (0)
-   `1`: 1 (1) -> `dp[0] + 1`
-   `2`: 10 (1) -> `dp[1]` (左移 1 位，1 的個數不變)
-   `3`: 11 (2) -> `dp[1] + 1`
-   `4`: 100 (1) -> `dp[2]`

**Relation**:
1.  **Offset Approach**: `dp[i] = dp[i - offset] + 1`。
2.  **LSB Approach**: `i` 的位元數等於 `i >> 1` (除以 2) 的位元數加上 `i & 1` (最後一位是否為 1)。
    -   `dp[i] = dp[i >> 1] + (i & 1)`。
    -   這非常直觀：`i` 右移一位就是去掉最後一位，剩下的位元數我們已經算過了。如果被去掉的那位是 1，就加回來。

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (LSB)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n + 1);
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            // dp[i] = dp[i / 2] + (i % 2)
            dp[i] = dp[i >> 1] + (i & 1);
        }

        return dp;
    }
};
```

### Python Reference

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
```
*(Python reference uses the Offset approach, equivalent to `dp[i] = dp[i ^ mostSigBit] + 1`)*

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        // 大小為 n+1 的陣列，初始化為 0
        vector<int> dp(n + 1);
        dp[0] = 0;

        // 從 1 開始遍歷到 n
        for (int i = 1; i <= n; i++) {
            // 核心轉移方程：
            // i >> 1 代表將 i 的二進制向右移一位 (相當於 i / 2)
            // dp[i >> 1] 是我們之前已經計算過的結果
            // (i & 1) 檢查 i 的最後一位是否為 1
            // 例如：i = 6 (110)
            // i >> 1 = 3 (011), dp[3] = 2
            // i & 1 = 0
            // dp[6] = 2 + 0 = 2。正確。
            // 例如：i = 7 (111)
            // i >> 1 = 3 (011), dp[3] = 2
            // i & 1 = 1
            // dp[7] = 2 + 1 = 3。正確。
            dp[i] = dp[i >> 1] + (i & 1);
        }

        return dp;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Single pass.
-   **Space Complexity**: $O(N)$
    -   To store the result.
