# Number of 1 Bits (位元 1 的個數) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #191** — [題目連結](https://leetcode.com/problems/number-of-1-bits/) | [NeetCode 解說](https://neetcode.io/problems/number-of-1-bits)


## 1. 🧐 Problem Dissection (釐清問題)

這是一個非常經典的位運算問題，也叫 **Hamming Weight**。
給定一個無符號整數 `n`，請計算它的二進制表示中有多少個 `1`。

-   **Input**: `n = 00000000000000000000000000001011` (11)
-   **Output**: `3`
-   **Input**: `n = 11111111111111111111111111111101`
-   **Output**: `31`

---

## 2. 🐢 Brute Force Approach (暴力解)

循環 32 次，每次檢查最低位是否為 1 (`n & 1`)，然後右移一位 (`n >>= 1`)。

-   **Time**: $O(32) = O(1)$。
-   **Algorithm**:
    ```cpp
    int res = 0;
    while (n) {
        res += n & 1;
        n >>= 1;
    }
    return res;
    ```

---

## 3. 💡 The "Aha!" Moment (優化)

**Brian Kernighan's Algorithm**:
這是一個稍微更快的算法，它的循環次數等於 **1 的個數**，而不是固定的 32 次。
核心操作是 `n = n & (n - 1)`。
這個操作會 **消除 n 的二進制表示中最低位的那個 1**。

-   Example: `n = 10100` (20)
-   `n - 1 = 10011` (19)
-   `n & (n - 1)` = `10100 & 10011` = `10000` (eliminate lowest 1)
-   Next: `10000 & 01111` = `00000` (eliminate lowest 1)
-   Total 2 ops.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../count_bits_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../count_bits_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Brian Kernighan's Algorithm

```cpp
#include <cstdint>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }
};
```

### Python Reference

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        // 只要 n 不為 0，就表示還有 1 存在
        while (n != 0) {
            // Brian Kernighan's algorithm
            // n & (n - 1) 的作用是將 n 的二進制中最右邊的 1 變成 0
            // 例如：1100 -> 1000
            n = n & (n - 1);

            // 每消除一個 1，計數器加 1
            count++;
        }
        return count;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(k)$, where $k$ is the number of set bits.
    -   In worst case $k=32$, so $O(1)$.
-   **Space Complexity**: $O(1)$.
