# 01 Climbing Stairs — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/01_Climbing_Stairs.md`

> Quick links: [Source Solution](../01_Climbing_Stairs.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the climbing stairs problem. | 我先重述爬樓梯題目。 | Restatement |
| We need the number of ways to reach step n. | 要求到第 n 階的方法數。 | Restatement |
| At each move we can climb one or two steps. | 每一步可爬 1 階或 2 階。 | Restatement |
| This is a counting problem, not path listing. | 這是計數題，不需列出路徑。 | Restatement |
| The recurrence is Fibonacci-like. | 其遞推關係類似 Fibonacci。 | Restatement |
| I will use O(1) space dynamic programming. | 我會用 O(1) 空間的 DP。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is n always at least one? | n 是否保證至少為 1？ | Clarify |
| Do we only return count, not actual sequences? | 是否只回傳數量，不回傳路徑？ | Clarify |
| Can I assume answer fits 32-bit integer under constraints? | 在此限制下是否可假設 32-bit 足夠？ | Clarify |
| Is recursive explanation okay before optimized DP? | 是否可先解釋遞迴再轉 DP？ | Clarify |
| Should I prioritize constant-space implementation? | 是否優先展示常數空間實作？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursion tries one-step and two-step branches every time. | 暴力遞迴每次分成走 1 階與 2 階。 | Approach |
| This repeats the same subproblems many times. | 這會重複計算大量子問題。 | Approach |
| Time grows exponentially, around O(two to the n). | 時間會指數成長，約 O(2^n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Define ways[i] as ways to reach step i. | 定義 ways[i] 為到第 i 階的方法數。 | Approach |
| Transition is ways[i] equals ways[i-1] plus ways[i-2]. | 轉移為 ways[i]=ways[i-1]+ways[i-2]。 | Approach |
| Base values are ways[1] equals one and ways[2] equals two. | 基底是 ways[1]=1、ways[2]=2。 | Approach |
| We only need previous two values at each iteration. | 每次迭代只需要前兩個值。 | Approach |
| So we keep rolling variables and achieve O(1) space. | 用滾動變數即可達成 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I handle base cases n equals one and n equals two first. | 我先處理 n=1 與 n=2 的基底。 | Coding |
| I initialize twoStepsBefore as one and oneStepBefore as two. | 我設 twoStepsBefore=1、oneStepBefore=2。 | Coding |
| Then I iterate i from three to n. | 接著 i 從 3 迭代到 n。 | Coding |
| Current ways is oneStepBefore plus twoStepsBefore. | current 方式數是前兩者相加。 | Coding |
| I shift twoStepsBefore to oneStepBefore. | 我把 twoStepsBefore 更新為舊 oneStepBefore。 | Coding |
| I shift oneStepBefore to current. | 我把 oneStepBefore 更新為 current。 | Coding |
| After loop, oneStepBefore stores answer for n. | 迴圈後 oneStepBefore 即 n 的答案。 | Coding |
| I return that value. | 我回傳該值。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n equals three. | 我手跑 n=3。 | Dry-run |
| Base gives twoStepsBefore one and oneStepBefore two. | 基底得到 twoStepsBefore=1、oneStepBefore=2。 | Dry-run |
| At i equals three, current is two plus one equals three. | i=3 時 current=2+1=3。 | Dry-run |
| Update rolling values and finish loop. | 更新滾動值後迴圈結束。 | Dry-run |
| Final answer is three ways. | 最終答案是 3 種。 | Dry-run |
| The three ways are one-one-one, one-two, and two-one. | 三種方式為 1+1+1、1+2、2+1。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals one should return one. | 案例一：n=1 應回 1。 | Edge test |
| Case two: n equals two should return two. | 案例二：n=2 應回 2。 | Edge test |
| Case three: n equals three should return three. | 案例三：n=3 應回 3。 | Edge test |
| Case four: a larger n like five should return eight. | 案例四：較大 n 如 5 應回 8。 | Edge test |
| Case five: verify monotonic increase for positive n. | 案例五：正整數 n 下答案應單調增加。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We run one loop from three up to n. | 我們只跑一個從 3 到 n 的迴圈。 | Complexity |
| Each iteration does constant arithmetic and assignments. | 每次迭代只有常數次運算與指定。 | Complexity |
| Therefore runtime is linear O(n). | 因此時間是線性 O(n)。 | Complexity |
| We store only two previous states and one current value, so O(1) space. | 只存前兩狀態與 current，因此空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me express this as recurrence first. | 我先把它寫成遞推式。 | If stuck |
| To reach step i, I must come from i minus one or i minus two. | 到 i 階只能從 i-1 或 i-2 來。 | If stuck |
| So ways[i] equals ways[i-1] plus ways[i-2]. | 所以 ways[i]=ways[i-1]+ways[i-2]。 | If stuck |
| Base values are simple: one and two. | 基底值很簡單：1 與 2。 | If stuck |
| I do not need full DP array here. | 這題不需要完整 DP 陣列。 | If stuck |
| Rolling two variables is enough. | 兩個滾動變數就足夠。 | If stuck |
| Let me verify with n equals four quickly. | 我快速驗證 n=4。 | If stuck |
| Sequence becomes one, two, three, five. | 序列會是 1、2、3、5。 | If stuck |
| Result five is correct for n four. | n=4 答案 5 正確。 | If stuck |
| Great, I can finalize confidently. | 很好，我可以有把握收尾。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved climbing stairs with Fibonacci-style DP. | 我用 Fibonacci 風格 DP 解出爬樓梯。 | Wrap-up |
| The key recurrence is ways[i] equals ways[i-1] plus ways[i-2]. | 核心遞推是 ways[i]=ways[i-1]+ways[i-2]。 | Wrap-up |
| Base cases handle n one and n two. | 基底處理 n=1 與 n=2。 | Wrap-up |
| Rolling variables give O(1) space. | 滾動變數可達 O(1) 空間。 | Wrap-up |
| Runtime is linear in n. | 執行時間對 n 為線性。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem asks count of ways. | 題目要方法數。 | Cheat sheet |
| Move options are one or two steps. | 每步可走 1 或 2。 | Cheat sheet |
| Recurrence is Fibonacci-like. | 遞推類 Fibonacci。 | Cheat sheet |
| ways[i] = ways[i-1] + ways[i-2]. | ways[i]=ways[i-1]+ways[i-2]。 | Cheat sheet |
| Base: ways[1]=1. | 基底：ways[1]=1。 | Cheat sheet |
| Base: ways[2]=2. | 基底：ways[2]=2。 | Cheat sheet |
| Handle n<=2 directly. | n<=2 直接回傳。 | Cheat sheet |
| Use two rolling vars. | 使用兩個滾動變數。 | Cheat sheet |
| Iterate from 3 to n. | 從 3 迭代到 n。 | Cheat sheet |
| current = prev1 + prev2. | current=prev1+prev2。 | Cheat sheet |
| Shift prev2=prev1. | 更新 prev2=prev1。 | Cheat sheet |
| Shift prev1=current. | 更新 prev1=current。 | Cheat sheet |
| Return prev1 at end. | 結尾回傳 prev1。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| n=3 -> 3. | n=3 得 3。 | Cheat sheet |
| n=4 -> 5. | n=4 得 5。 | Cheat sheet |
| Common bug: wrong base values. | 常見錯誤：基底值寫錯。 | Cheat sheet |
| Common bug: off-by-one loop bounds. | 常見錯誤：迴圈邊界 off-by-one。 | Cheat sheet |
| Mention memoization alternative briefly. | 可簡述 memoization 替代法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Space-optimized DP recurrence is preserved.
- No hallucinated constraints: ✅ Uses source movement and counting semantics.
- Language simplicity: ✅ Short, interview-spoken, and easy to deliver.
