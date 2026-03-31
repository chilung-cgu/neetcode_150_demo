# 04 Reverse Bits — Interview English Script (C++)

> Source aligned with: `docs/18_Bit_Manipulation/04_Reverse_Bits.md`

> Quick links: [Source Solution](../04_Reverse_Bits.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Reverse Bits. | 我先重述 Reverse Bits。 | Restatement |
| Input is a 32-bit unsigned integer n. | 輸入是 32 位無號整數 n。 | Restatement |
| We need to reverse its bit order and return the new value. | 要把位元順序完全反轉後回傳。 | Restatement |
| I will build result bit by bit from least significant side of n. | 我會從 n 的低位逐步建立結果。 | Restatement |
| Loop runs exactly 32 rounds. | 迴圈固定跑 32 輪。 | Restatement |
| This gives constant time and constant space. | 這可得到常數時間與常數空間。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should input be treated strictly as uint32_t? | 輸入是否嚴格當作 uint32_t？ | Clarify |
| Is fixed 32-iteration solution preferred? | 是否偏好固定 32 輪解法？ | Clarify |
| Can I use shift and bitwise or operators directly? | 可直接使用位移與 OR 運算嗎？ | Clarify |
| Should complexity be reported as O(1) due to fixed word size? | 複雜度是否以固定字長記為 O(1)？ | Clarify |
| Do you want mention of divide-and-conquer bit-mask variant too? | 是否要補充分治遮罩版本？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| There is no meaningful brute force beyond direct 32-bit simulation. | 這題其實沒有更笨的暴力法，核心就是 32 位模擬。 | Approach |
| A string-conversion approach is possible but unnecessary overhead. | 可轉字串反轉，但有不必要負擔。 | Approach |
| Bitwise simulation is clearer and faster. | 位運算模擬更直觀也更快。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Initialize result to zero. | 先把 result 設為 0。 | Approach |
| For each of 32 rounds, shift result left by one. | 每輪先把 result 左移一位。 | Approach |
| Extract lowest bit of n with n and one. | 用 n&1 取出 n 的最低位。 | Approach |
| OR that bit into result, then shift n right by one. | 把該 bit OR 進 result，再把 n 右移一位。 | Approach |
| After 32 rounds, all bits are reversed. | 32 輪後位元就完全反轉。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I declare uint32_t result equals zero. | 我宣告 uint32_t result=0。 | Coding |
| I start loop from i zero to thirty-one. | 我讓 i 從 0 跑到 31。 | Coding |
| Each round, shift result left by one. | 每輪把 result 左移一位。 | Coding |
| Read current bit as n and one. | 取目前位元 bit=n&1。 | Coding |
| Merge bit into result using OR. | 用 OR 把 bit 合併到 result。 | Coding |
| Shift n right by one to expose next bit. | n 右移一位準備下一輪。 | Coding |
| After loop, return result. | 迴圈後回傳 result。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run a short conceptual example with binary one-zero-one. | 我先用簡短概念例 101 手跑。 | Dry-run |
| Round one takes last one and appends to result. | 第一輪取末位 1 放進 result。 | Dry-run |
| Round two takes zero and appends. | 第二輪取 0 放進去。 | Dry-run |
| Round three takes one and appends. | 第三輪取 1 放進去。 | Dry-run |
| Bit sequence becomes reversed order one-zero-one in this symmetric toy case. | 這個對稱小例下反轉後仍是 101。 | Dry-run |
| In real 32-bit input, same mechanism runs full 32 rounds. | 真實 32 位輸入同理跑滿 32 輪。 | Dry-run |
| Final integer corresponds to reversed 32-bit pattern. | 最終整數即對應反轉後 32 位模式。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals zero should return zero. | 案例一：n=0 應回 0。 | Edge test |
| Case two: n equals one should return highest-bit-only value. | 案例二：n=1 應回最高位為 1 的值。 | Edge test |
| Case three: input with alternating bits. | 案例三：位元交錯模式輸入。 | Edge test |
| Case four: input with highest bit already set. | 案例四：原本最高位就為 1。 | Edge test |
| Case five: all ones should stay all ones after reverse. | 案例五：全 1 反轉後仍全 1。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(1) because loop count is fixed at 32. | 時間複雜度是 O(1)，因迴圈固定 32 次。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We always execute exactly 32 iterations for uint32 input. | 對 uint32 我們固定執行 32 次。 | Complexity |
| Each iteration does constant-time bit operations. | 每輪都是常數級位元操作。 | Complexity |
| So runtime is O(1) under fixed word size model. | 在固定字長模型下時間是 O(1)。 | Complexity |
| We use only a few scalar variables, so extra memory is O(1). | 只用少量純量變數，額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me think in terms of consuming bits from right to left. | 我用從右到左消耗位元的角度思考。 | If stuck |
| Every round I take one bit from n. | 每輪我從 n 取一個 bit。 | If stuck |
| I shift result first to make room. | 先左移 result 騰出空間。 | If stuck |
| Then append extracted bit. | 再把取出的 bit 補上。 | If stuck |
| This naturally builds reversed order. | 這會自然形成反向順序。 | If stuck |
| I must run full 32 rounds even if n becomes zero early. | 就算 n 提早變 0，也必須跑滿 32 輪。 | If stuck |
| Otherwise leading zeros would be mishandled. | 否則前導零會處理錯。 | If stuck |
| Let me verify with n equals one quickly. | 我快速驗證 n=1。 | If stuck |
| Result should be one shifted to top bit. | 結果應是 1 被移到最高位。 | If stuck |
| Great, loop structure is correct. | 很好，迴圈結構正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with fixed-length bit simulation. | 我用固定長度位元模擬解題。 | Wrap-up |
| We consume one bit from n and append to result each round. | 每輪從 n 取一位並附加到 result。 | Wrap-up |
| Running all 32 rounds guarantees correctness. | 跑滿 32 輪可保證正確。 | Wrap-up |
| Complexity is O(1) time and O(1) space. | 複雜度是 O(1) 時間、O(1) 空間。 | Wrap-up |
| This is the standard interview implementation. | 這是標準面試寫法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: reverse 32-bit pattern. | 目標：反轉 32 位元模式。 | Cheat sheet |
| Use uint32_t for clarity. | 用 uint32_t 比較清楚。 | Cheat sheet |
| res = 0 initially. | 初始 res=0。 | Cheat sheet |
| Repeat 32 times. | 重複 32 次。 | Cheat sheet |
| res <<= 1. | res 左移一位。 | Cheat sheet |
| bit = n & 1. | bit=n&1。 | Cheat sheet |
| res |= bit. | res|=bit。 | Cheat sheet |
| n >>= 1. | n 右移一位。 | Cheat sheet |
| Return res. | 回傳 res。 | Cheat sheet |
| n=0 => 0. | n=0 => 0。 | Cheat sheet |
| n=1 => top bit set. | n=1 => 最高位為 1。 | Cheat sheet |
| all ones stays all ones. | 全 1 反轉仍全 1。 | Cheat sheet |
| Time O(1) fixed rounds. | 時間 O(1)（固定輪數）。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: early break when n==0. | 常見錯誤：n==0 就提早停止。 | Cheat sheet |
| Common bug: wrong shift direction. | 常見錯誤：位移方向寫反。 | Cheat sheet |
| Keep operations unsigned-safe. | 保持無號位元語義。 | Cheat sheet |
| Explain room-making then append bit. | 解釋成「先騰位再塞 bit」。 | Cheat sheet |
| Verify with known LeetCode sample. | 用 LeetCode 範例驗證。 | Cheat sheet |
| Small, robust, interview-ready. | 小巧穩定，面試友善。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ 32-iteration bit reversal.
- Constraint alignment: ✅ Unsigned fixed-width handling.
- Language simplicity: ✅ Concise spoken format.
