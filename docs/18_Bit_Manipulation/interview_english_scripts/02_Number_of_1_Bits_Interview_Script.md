# 02 Number of 1 Bits — Interview English Script (C++)

> Source aligned with: `docs/18_Bit_Manipulation/02_Number_of_1_Bits.md`

> Quick links: [Source Solution](../02_Number_of_1_Bits.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Number of One Bits. | 我先重述 Number of 1 Bits。 | Restatement |
| Given an unsigned integer n, we count how many bits are one. | 給定無號整數 n，要數出 bit=1 的個數。 | Restatement |
| This is also called Hamming Weight. | 這題也叫 Hamming Weight。 | Restatement |
| I will use Brian Kernighan's trick. | 我會用 Brian Kernighan 技巧。 | Restatement |
| n and n minus one clears the lowest set bit. | n&(n-1) 可清掉最低位的 1。 | Restatement |
| Repeating until n is zero gives exact count. | 重複到 n=0 就得到精確計數。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should I treat input strictly as 32-bit unsigned? | 是否要嚴格視為 32 位無號整數？ | Clarify |
| Is returning int count acceptable? | 回傳 int 計數可以嗎？ | Clarify |
| Do you prefer Kernighan method over fixed 32-iteration loop? | 偏好 Kernighan 還是固定 32 次迴圈？ | Clarify |
| Should complexity mention k equals number of set bits? | 複雜度是否要寫成 k=1 的個數？ | Clarify |
| Are bitwise operators guaranteed available in target language? | 目標語言是否都可用位運算？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline loops up to 32 times and checks n and one each step. | 基線法最多迴圈 32 次，每步檢查 n&1。 | Approach |
| Then shift n right by one every iteration. | 每輪把 n 右移一位。 | Approach |
| It is O(32) which is O(1), but not as elegant as clearing bits directly. | 雖是 O(1)，但不如直接清位元優雅。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use loop while n is not zero. | 當 n 不為 0 時迴圈。 | Approach |
| In each round set n to n and n minus one. | 每輪令 n = n & (n-1)。 | Approach |
| This removes exactly one set bit each time. | 這每次都會移除一個 1。 | Approach |
| Increment counter each removal. | 每移除一次就把計數加一。 | Approach |
| Complexity is O(k) where k is number of one bits. | 複雜度是 O(k)，k 為 1 的數量。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize count to zero. | 我先把 count 設為 0。 | Coding |
| While n is not zero, continue. | 當 n!=0 就繼續。 | Coding |
| Update n as n and n minus one. | 把 n 更新為 n&(n-1)。 | Coding |
| Increment count by one. | count 加一。 | Coding |
| Loop ends when all set bits are cleared. | 所有 1 清完時迴圈結束。 | Coding |
| Return count. | 回傳 count。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n equals binary one-zero-one-one. | 我用二進位 1011 手跑。 | Dry-run |
| First round clears lowest one: one-zero-one-zero, count one. | 第一輪清最低位 1 變 1010，count=1。 | Dry-run |
| Second round clears again: one-zero-zero-zero, count two. | 第二輪再清，變 1000，count=2。 | Dry-run |
| Third round clears last one: zero, count three. | 第三輪清最後一個 1 變 0，count=3。 | Dry-run |
| Loop stops at zero. | n=0 時停止。 | Dry-run |
| Final answer is three. | 最終答案是 3。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals zero should return zero. | 案例一：n=0 應回 0。 | Edge test |
| Case two: n with single one bit. | 案例二：只有一個 1 的 n。 | Edge test |
| Case three: n all ones in 32-bit range. | 案例三：32 位全 1。 | Edge test |
| Case four: highest bit set only. | 案例四：僅最高位為 1。 | Edge test |
| Case five: random mixed bits. | 案例五：隨機混合位元。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(k), k equals number of set bits. | 時間複雜度是 O(k)，k 為 1 的個數。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each loop iteration clears exactly one set bit. | 每輪迭代都清除一個 1。 | Complexity |
| Therefore number of iterations equals set-bit count k. | 因此迭代次數正好等於 set bit 數量 k。 | Complexity |
| Runtime is O(k), upper-bounded by word size like 32. | 時間是 O(k)，且上限受字長如 32 限制。 | Complexity |
| We only use count and n variables, so memory is O(1). | 只用 count 與 n，記憶體 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me use the n and n minus one identity. | 我先用 n&(n-1) 的恆等技巧。 | If stuck |
| This operation always removes the lowest set bit. | 這個操作一定移除最低位 1。 | If stuck |
| So counting removals equals counting ones. | 所以移除次數就等於 1 的個數。 | If stuck |
| I do not need to inspect every bit position. | 我不需要逐位檢查全部位置。 | If stuck |
| Loop condition is simply while n not zero. | 迴圈條件就是 n!=0。 | If stuck |
| After update, increment count. | 每次更新後 count++。 | If stuck |
| Let me test with n equals zero quickly. | 我先快速測 n=0。 | If stuck |
| Then test with n equals eleven binary. | 再測二進位 1011。 | If stuck |
| The iteration count matches expected ones. | 迭代次數與 1 的數量一致。 | If stuck |
| Great, implementation is complete. | 很好，實作就完成了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with Brian Kernighan bit-clearing loop. | 我用 Brian Kernighan 清位元迴圈解題。 | Wrap-up |
| Each iteration removes one set bit. | 每輪都移除一個 1。 | Wrap-up |
| Count of iterations equals Hamming weight. | 迭代次數即 Hamming weight。 | Wrap-up |
| Complexity is O(k) time and O(1) extra space. | 複雜度是 O(k) 時間、O(1) 空間。 | Wrap-up |
| This is concise and interview-standard. | 這是精簡且標準的面試解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: count one bits in unsigned integer. | 目標：計算無號整數中的 1 位元數。 | Cheat sheet |
| Use Kernighan method. | 使用 Kernighan 方法。 | Cheat sheet |
| Start count = 0. | 初始 count=0。 | Cheat sheet |
| While n != 0. | 當 n!=0。 | Cheat sheet |
| n = n & (n-1). | n = n&(n-1)。 | Cheat sheet |
| count++. | count++。 | Cheat sheet |
| Return count. | 回傳 count。 | Cheat sheet |
| Why works: clears one set bit each round. | 原理：每輪清一個 1。 | Cheat sheet |
| Iterations equal number of ones. | 迭代次數等於 1 的數量。 | Cheat sheet |
| Time O(k). | 時間 O(k)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| k <= 32 for uint32. | 對 uint32 而言 k<=32。 | Cheat sheet |
| Test n=0 => 0. | 測 n=0 => 0。 | Cheat sheet |
| Test n=11 => 3. | 測 n=11 => 3。 | Cheat sheet |
| Test all-ones word. | 測全 1 位元字。 | Cheat sheet |
| Common bug: using signed shifts carelessly. | 常見錯誤：有號位移使用不慎。 | Cheat sheet |
| Common bug: forgetting loop increments count. | 常見錯誤：忘記迴圈中 count++。 | Cheat sheet |
| Alternative: fixed 32-bit scan. | 替代法：固定 32 位掃描。 | Cheat sheet |
| Kernighan often fewer iterations. | Kernighan 通常迭代更少。 | Cheat sheet |
| Explain with one binary example. | 用一個二進位例子說明最清楚。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Kernighan bit trick.
- Constraint alignment: ✅ Unsigned bit-count semantics preserved.
- Language simplicity: ✅ Clear, compact interview speech.
