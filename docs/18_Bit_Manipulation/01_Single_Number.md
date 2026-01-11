# Single Number (只出現一次的數字)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個非空整數陣列 `nums`，除了某個元素只出現一次以外，其餘每個元素均出現兩次。
找出那個只出現了一次的元素。
你必須設計並實現一個線性時間複雜度 $O(n)$ 的算法，且只使用常數額外空間 $O(1)$。

-   **Input**: `[2,2,1]`
-   **Output**: `1`
-   **Input**: `[4,1,2,1,2]`
-   **Output**: `4`

---

## 2. 🐢 Brute Force Approach (暴力解)

使用 Hash Map 統計每個數字出現的次數。遍歷 Map 找出次數為 1 的數字。

-   **Time**: $O(n)$。
-   **Space**: $O(n)$。不符合空間要求。

---

## 3. 💡 The "Aha!" Moment (優化)

**XOR (異或運算)**:
利用 XOR 的性質：

1.  $a \oplus 0 = a$
2.  $a \oplus a = 0$
3.  $a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$ (結合律與交換律)

因為除了目標數字出現一次，其他都出現兩次。
將所有數字進行 XOR 運算，成對的數字會互相抵銷變成 0，最後剩下的就是那個只出現一次的數字。

---

## 4. 💻 Implementation (程式碼)

### Approach: Bit Manipulation (XOR)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int n : nums) {
            res ^= n;
        }
        return res;
    }
};
```

### Python Reference

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        // 遍歷所有數字，將它們進行異或運算
        for (int n : nums) {
            // 利用 x ^ x = 0 的性質
            // 所有出現兩次的數字都會被消除
            // 唯獨出現一次的數字會被保留下來
            res ^= n;
        }
        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   One pass through the array.
-   **Space Complexity**: $O(1)$
    -   Only one variable needed.
