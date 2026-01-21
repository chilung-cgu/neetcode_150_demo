# Reverse Bits (顛倒位元) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

## 1. 🧐 Problem Dissection (釐清問題)

給定一個 32 位的無符號整數 `n`。
請將其二進制表示顛倒（Reverse bits），並回傳結果。

-   **Input**: `n = 00000010100101000001111010011100` (43261596)
-   **Output**: `964176192` (`00111001011110000010100101000000`)
-   **Constraints**:
    -   Follow up: Can you iterate fewer than 32 times? (e.g. Divide and Conquer)

---

## 2. 🐢 Brute Force Approach (暴力解)

遍歷 32 位。
每次取出 `n` 的最後一位 (`n & 1`)。
將其加到 `res` 的正確位置（通過左移）。
`n` 右移一位。

```cpp
uint32_t res = 0;
for (int i = 0; i < 32; i++) {
    res = (res << 1) + (n & 1);
    n >>= 1;
}
return res;
```
-   **Time**: $O(1)$ (32 iterations).
-   **Space**: $O(1)$.

---

## 3. 💡 The "Aha!" Moment (優化)

**Divide and Conquer (Bit Masking)**:
如果不使用循環，可以利用分治法。

1.  交換相鄰的 1 位：`0x55555555` (0101...)
    -   `n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)`
2.  交換相鄰的 2 位：`0x33333333` (0011...)
    -   `n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)`
3.  交換相鄰的 4 位：`0x0F0F0F0F`
4.  交換相鄰的 8 位：`0x00FF00FF`
5.  交換相鄰的 16 位：`0x0000FFFF`

這種方法在某些不支持循環或者需要並行處理的硬件上很有用。對於通用刷題，循環法已經足夠快。
這裡我們演示標準的循環法，因為它最易讀。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../reverse_bits_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../reverse_bits_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iteration

```cpp
#include <cstdint>

using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i = 0; i < 32; i++) {
            // Shift result to outputmake room for new bit
            res = res << 1;

            // Get the last bit of n
            int bit = n & 1;

            // Add it to result (strictly speaking, OR or ADD both work for 0/1)
            res = res | bit;

            // Shift n to process next bit
            n = n >> 1;
        }
        return res;
    }
};
```

### Python Reference

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;

        // 必須循環 32 次，即使 n 變成 0 了，我們也要繼續補 0 到高位
        // 例如 n = 1 (0...01)，翻轉後應該是 10...0 (2^31)
        for (int i = 0; i < 32; i++) {
            // 將結果左移一位，騰出最低位
            res = res << 1;

            // 取出 n 的最低位
            int bit = n & 1;

            // 將取出的位放到 res 的最低位
            // (因為 res 剛左移過，最低位是 0，可以用 | 或 +)
            res = res | bit;

            // 將 n 右移一位，準備處理下一位
            n = n >> 1;
        }

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(1)$.
    -   Always 32 iterations.
-   **Space Complexity**: $O(1)$.
