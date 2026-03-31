# 06 Sum of Two Integers — Interview English Script (C++)

> Source aligned with: `docs/18_Bit_Manipulation/06_Sum_of_Two_Integers.md`

> Quick links: [Source Solution](../06_Sum_of_Two_Integers.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Sum of Two Integers. | 我先重述 Sum of Two Integers。 | Restatement |
| We need to compute a plus b without using plus or minus operators. | 不能用加減運算子，要算出 a+b。 | Restatement |
| I will simulate binary addition using bit operations. | 我會用位運算模擬二進位加法。 | Restatement |
| XOR gives sum without carry. | XOR 可得到不含進位的和。 | Restatement |
| AND then left shift gives carry bits. | AND 再左移可得到進位。 | Restatement |
| Repeat until carry becomes zero. | 重複直到進位變 0。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should we assume 32-bit signed integer behavior? | 是否假設 32 位有號整數行為？ | Clarify |
| Is using bitwise operators and shifts fully allowed? | 位運算與位移是否完全允許？ | Clarify |
| Do we need to discuss negative-number handling explicitly? | 是否要明確說明負數處理？ | Clarify |
| Is C++ two's-complement overflow behavior assumed by platform constraints? | 是否以平台補數語意為前提？ | Clarify |
| Should I keep implementation iterative only? | 是否採純迭代實作？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Arithmetic operators are banned, so normal brute force is not applicable. | 因禁用加減，普通暴力法不適用。 | Approach |
| Conceptually we still need full-adder style per-bit simulation. | 概念上仍需全加器逐位模擬。 | Approach |
| Bitwise formulation is the clean direct path. | 位運算表達是最直接乾淨路徑。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Compute partial sum as a xor b. | 先算部分和 sum=a^b。 | Approach |
| Compute carry as a and b, then shift left by one. | 再算 carry=(a&b)<<1。 | Approach |
| Assign a to partial sum and b to carry. | 把 a 更新為部分和，b 更新為進位。 | Approach |
| Loop while b is not zero. | 當 b 不為 0 就持續迴圈。 | Approach |
| When carry is zero, a is final answer. | 進位歸零時，a 就是最終答案。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I enter loop while b is not zero. | 我用 while(b!=0) 進入迴圈。 | Coding |
| I compute carry as unsigned of a and b shifted left one. | 我先算 carry=(unsigned)(a&b)<<1。 | Coding |
| I compute sum without carry as a xor b. | 再算不含進位的和 a^b。 | Coding |
| I assign a to that xor result. | 把 a 更新為 xor 結果。 | Coding |
| I assign b to carry for next round propagation. | 把 b 更新為 carry 供下一輪傳遞。 | Coding |
| Loop repeats until carry chain disappears. | 反覆直到進位鏈消失。 | Coding |
| Then I return a. | 最後回傳 a。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run a equals one and b equals two. | 我用 a=1、b=2 手跑。 | Dry-run |
| First xor is three, carry is zero. | 第一次 xor=3，carry=0。 | Dry-run |
| Carry is zero so loop ends immediately. | carry=0 所以迴圈立刻結束。 | Dry-run |
| Return a equals three. | 回傳 a=3。 | Dry-run |
| For carry example, a=3 and b=5 takes multiple rounds. | 若看進位案例，a=3、b=5 會跑多輪。 | Dry-run |
| Each round pushes carry left until no overlap remains. | 每輪都把進位往左推直到不重疊。 | Dry-run |
| Final result matches normal addition. | 最終結果會與一般加法一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: both numbers zero. | 案例一：兩數皆為 0。 | Edge test |
| Case two: positive plus negative. | 案例二：正數加負數。 | Edge test |
| Case three: negative plus negative. | 案例三：負數加負數。 | Edge test |
| Case four: values near integer boundaries. | 案例四：接近整數邊界的值。 | Edge test |
| Case five: one operand already zero. | 案例五：其中一個運算元本身為 0。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(1) under fixed 32-bit integer width. | 固定 32 位前提下時間是 O(1)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each iteration resolves part of carry propagation. | 每輪都會推進一部分進位傳播。 | Complexity |
| In 32-bit integers, carry can propagate at most across fixed bit-width. | 在 32 位整數中，進位最多跨固定字長。 | Complexity |
| So loop count is bounded by constant, giving O(1) runtime. | 因此迴圈次數受常數上限，時間為 O(1)。 | Complexity |
| Only scalar temporaries are used, so memory is O(1). | 只用純量暫存，空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me decompose addition into sum and carry parts. | 我先把加法拆成和與進位兩部分。 | If stuck |
| XOR is sum without carry. | XOR 就是不含進位的和。 | If stuck |
| AND finds positions that generate carry. | AND 找出會產生進位的位置。 | If stuck |
| Shift carry left because carry affects next higher bit. | 進位左移因為它影響更高一位。 | If stuck |
| Then repeat with new a and b. | 再用新 a、b 繼續重複。 | If stuck |
| Process stops once carry is zero. | 當 carry 為 0 就停止。 | If stuck |
| I use unsigned cast before left shift for safety. | 左移前先轉 unsigned 較安全。 | If stuck |
| Let me verify with one positive and one negative case. | 我驗證一個正負混合案例。 | If stuck |
| If output matches normal arithmetic, logic is confirmed. | 若結果與一般加法一致則邏輯成立。 | If stuck |
| Great, implementation is complete. | 很好，實作完成。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it by iterating xor-sum and shifted carry. | 我用 xor 和位移進位反覆迭代解題。 | Wrap-up |
| This exactly mirrors full-adder behavior in binary. | 這精準對應二進位全加器行為。 | Wrap-up |
| It works for positive and negative integers under fixed width. | 在固定字長下可處理正負整數。 | Wrap-up |
| Complexity is O(1) time and O(1) space. | 複雜度是 O(1) 時間與 O(1) 空間。 | Wrap-up |
| This is the canonical interview answer without plus or minus. | 這是不使用加減時的經典面試解。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: compute a+b without plus/minus. | 目標：不用加減算出 a+b。 | Cheat sheet |
| Use binary full-adder idea. | 使用二進位全加器概念。 | Cheat sheet |
| sum = a ^ b. | sum=a^b。 | Cheat sheet |
| carry = (a & b) << 1. | carry=(a&b)<<1。 | Cheat sheet |
| Update a = sum. | 更新 a=sum。 | Cheat sheet |
| Update b = carry. | 更新 b=carry。 | Cheat sheet |
| Repeat while b != 0. | 當 b!=0 持續。 | Cheat sheet |
| Return a. | 回傳 a。 | Cheat sheet |
| XOR handles non-carry bits. | XOR 處理非進位位。 | Cheat sheet |
| AND+shift handles carry bits. | AND+位移處理進位位。 | Cheat sheet |
| Cast to unsigned before shift in C++ implementation. | C++ 實作可先轉 unsigned 再位移。 | Cheat sheet |
| Works for negatives with two's-complement semantics. | 在補數語義下可處理負數。 | Cheat sheet |
| Time O(1) fixed word size. | 固定字長下時間 O(1)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Test 1+2 => 3. | 測 1+2 => 3。 | Cheat sheet |
| Test -2+3 => 1. | 測 -2+3 => 1。 | Cheat sheet |
| Common bug: forgetting carry shift. | 常見錯誤：忘記進位左移。 | Cheat sheet |
| Common bug: not looping until carry zero. | 常見錯誤：未迴圈到 carry 歸零。 | Cheat sheet |
| Keep explanation sum-vs-carry separated. | 說明時分開「和」與「進位」。 | Cheat sheet |
| Short, robust bit-manipulation pattern. | 這是精簡且穩健的位運算模板。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ XOR + carry iterative method.
- Constraint alignment: ✅ No plus/minus operators used.
- Language simplicity: ✅ Clear interview-ready wording.
