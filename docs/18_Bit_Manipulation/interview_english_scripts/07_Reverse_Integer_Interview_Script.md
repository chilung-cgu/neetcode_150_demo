# 07 Reverse Integer — Interview English Script (C++)

> Source aligned with: `docs/18_Bit_Manipulation/07_Reverse_Integer.md`

> Quick links: [Source Solution](../07_Reverse_Integer.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Reverse Integer. | 我先重述 Reverse Integer。 | Restatement |
| Given a 32-bit signed integer x, we reverse its decimal digits. | 給定 32 位有號整數 x，要反轉十進位數字。 | Restatement |
| If reversed value overflows signed 32-bit range, return zero. | 若反轉後溢出 32 位有號範圍，回傳 0。 | Restatement |
| We should not rely on 64-bit storage. | 不應依賴 64 位儲存。 | Restatement |
| I will pop last digit and push into result iteratively. | 我會反覆 pop 尾數再 push 到結果。 | Restatement |
| Overflow must be checked before each push. | 每次 push 前都要先做溢位檢查。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should behavior follow 32-bit signed range exactly? | 是否嚴格遵循 32 位有號範圍？ | Clarify |
| Is returning zero on overflow mandatory? | 溢位是否必須回傳 0？ | Clarify |
| Can we assume C++ modulo on negatives as usual? | 可否採 C++ 對負數取模行為？ | Clarify |
| Do you prefer math-only approach over string reversal? | 你偏好純數學法而非字串反轉嗎？ | Clarify |
| Should we mention INT_MAX and INT_MIN boundary digits explicitly? | 是否要明講 INT_MAX/INT_MIN 邊界位數？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| String conversion can reverse digits quickly in code length. | 字串轉換法程式較短可快速反轉。 | Approach |
| But this is less ideal for low-level numeric interview intent. | 但對低階數值面試重點不夠理想。 | Approach |
| Math approach with explicit overflow guard is preferred. | 面試更偏好帶溢位檢查的數學法。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Repeatedly pop digit as x modulo ten and shrink x by division. | 反覆用 x%10 pop 一位，再 x/=10。 | Approach |
| Before push, check if rev would overflow after rev times ten plus pop. | push 前先檢查 rev*10+pop 是否會溢位。 | Approach |
| Positive overflow check uses INT_MAX over ten and last digit seven. | 正溢位檢查用 INT_MAX/10 與尾數 7。 | Approach |
| Negative overflow check uses INT_MIN over ten and last digit minus eight. | 負溢位檢查用 INT_MIN/10 與尾數 -8。 | Approach |
| If safe, update rev equals rev times ten plus pop. | 安全時才更新 rev=rev*10+pop。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize rev to zero. | 我先初始化 rev=0。 | Coding |
| While x is not zero, continue processing digits. | 當 x!=0 持續處理位數。 | Coding |
| Pop digit as x modulo ten. | 用 x%10 取出尾數 pop。 | Coding |
| Update x by integer division by ten. | 再做 x/=10 去掉尾數。 | Coding |
| Check positive overflow condition before push. | push 前先檢查正溢位條件。 | Coding |
| Check negative overflow condition before push. | push 前再檢查負溢位條件。 | Coding |
| If overflow risk exists, return zero immediately. | 若有溢位風險就立刻回 0。 | Coding |
| Otherwise set rev to rev times ten plus pop. | 否則更新 rev=rev*10+pop。 | Coding |
| After loop, return rev. | 迴圈結束回傳 rev。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run x equals one-two-zero. | 我用 x=120 手跑。 | Dry-run |
| Pop zero, rev stays zero. | pop 出 0，rev 仍是 0。 | Dry-run |
| Pop two, rev becomes two. | 再 pop 2，rev 變 2。 | Dry-run |
| Pop one, rev becomes twenty-one. | 再 pop 1，rev 變 21。 | Dry-run |
| x reaches zero, loop stops. | x 變 0，迴圈結束。 | Dry-run |
| Return twenty-one, leading zero is naturally removed. | 回傳 21，前導零自然消失。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: x equals zero. | 案例一：x=0。 | Edge test |
| Case two: negative input like minus one-two-three. | 案例二：負數輸入如 -123。 | Edge test |
| Case three: value ending with zeros. | 案例三：尾端有零的值。 | Edge test |
| Case four: overflow-positive example like one-five-three-four-two-three-six-four-six-nine. | 案例四：正向溢位例 1534236469。 | Edge test |
| Case five: near boundary values around INT_MAX and INT_MIN. | 案例五：INT_MAX、INT_MIN 附近邊界值。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(number of digits), effectively O(1) for 32-bit ints. | 時間是 O(位數)，對 32 位整數可視為 O(1)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each loop removes one decimal digit from x. | 每輪都會移除 x 的一個十進位位數。 | Complexity |
| So iteration count equals digit count of x. | 迭代次數等於 x 的位數。 | Complexity |
| For fixed 32-bit integers this is bounded by constant. | 對固定 32 位整數此上限為常數。 | Complexity |
| We use only scalar variables x, pop, and rev, so memory is O(1). | 僅用 x、pop、rev 等純量，空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me split operation into pop and push. | 我先把流程拆成 pop 與 push。 | If stuck |
| pop is x modulo ten, then x divided by ten. | pop 是 x%10，再做 x/=10。 | If stuck |
| push is rev times ten plus pop. | push 是 rev*10+pop。 | If stuck |
| Overflow must be checked before push. | 溢位必須在 push 前檢查。 | If stuck |
| Compare rev against INT_MAX over ten and INT_MIN over ten. | 用 INT_MAX/10 與 INT_MIN/10 比較 rev。 | If stuck |
| Handle equal-boundary cases with pop seven and minus eight limits. | 等邊界時用 pop 7 與 -8 限制。 | If stuck |
| If unsafe, return zero immediately. | 不安全就立刻回 0。 | If stuck |
| Let me test with 120 and -123 quickly. | 我快速測 120 與 -123。 | If stuck |
| Then test known overflow sample. | 再測已知溢位樣例。 | If stuck |
| Great, boundary behavior is verified. | 很好，邊界行為已驗證。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with digit pop-push plus pre-check overflow guards. | 我用位數 pop-push 加前置溢位檢查解題。 | Wrap-up |
| The solution is pure arithmetic and interview-friendly. | 這是純數學法且面試友善。 | Wrap-up |
| Overflow cases safely return zero as required. | 溢位情況會安全回 0。 | Wrap-up |
| Complexity is O(digits) time and O(1) space. | 複雜度是 O(位數) 時間與 O(1) 空間。 | Wrap-up |
| This is the standard robust implementation. | 這是標準且穩健的實作。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: reverse decimal digits of 32-bit signed int. | 目標：反轉 32 位有號整數十進位位數。 | Cheat sheet |
| Return 0 on overflow. | 溢位回 0。 | Cheat sheet |
| Initialize rev=0. | 初始化 rev=0。 | Cheat sheet |
| While x != 0 loop. | 當 x!=0 迴圈。 | Cheat sheet |
| pop = x % 10. | pop=x%10。 | Cheat sheet |
| x /= 10. | x/=10。 | Cheat sheet |
| Check rev > INT_MAX/10. | 檢查 rev>INT_MAX/10。 | Cheat sheet |
| Check rev == INT_MAX/10 and pop > 7. | 檢查 rev==INT_MAX/10 且 pop>7。 | Cheat sheet |
| Check rev < INT_MIN/10. | 檢查 rev<INT_MIN/10。 | Cheat sheet |
| Check rev == INT_MIN/10 and pop < -8. | 檢查 rev==INT_MIN/10 且 pop<-8。 | Cheat sheet |
| If any true, return 0. | 任一成立就回 0。 | Cheat sheet |
| Else rev = rev*10 + pop. | 否則 rev=rev*10+pop。 | Cheat sheet |
| End loop, return rev. | 迴圈結束回 rev。 | Cheat sheet |
| Example 123 => 321. | 範例 123=>321。 | Cheat sheet |
| Example -123 => -321. | 範例 -123=>-321。 | Cheat sheet |
| Example 120 => 21. | 範例 120=>21。 | Cheat sheet |
| Overflow sample returns 0. | 溢位樣例回 0。 | Cheat sheet |
| Time O(digits), bounded for 32-bit. | 時間 O(位數)，32 位下有上限。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Explain guard-before-push clearly. | 口述重點是「先檢查再 push」。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Pop/push with overflow guards.
- Constraint alignment: ✅ 32-bit boundary handling preserved.
- Language simplicity: ✅ Clear spoken interview style.
