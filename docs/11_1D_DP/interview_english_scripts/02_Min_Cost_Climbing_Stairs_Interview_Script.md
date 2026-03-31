# 02 Min Cost Climbing Stairs — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/02_Min_Cost_Climbing_Stairs.md`

> Quick links: [Source Solution](../02_Min_Cost_Climbing_Stairs.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the min-cost climbing stairs problem. | 我先重述最小成本爬樓梯題。 | Restatement |
| cost[i] is the price to step on stair i. | cost[i] 是踩到第 i 階的花費。 | Restatement |
| From each step we can move one or two stairs up. | 每一步可往上 1 階或 2 階。 | Restatement |
| We may start from step zero or step one. | 可從第 0 階或第 1 階開始。 | Restatement |
| Goal is minimum total cost to reach the top. | 目標是到達頂端的最小總花費。 | Restatement |
| I will use rolling DP with O(1) extra space. | 我會用滾動 DP，額外空間 O(1)。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is top considered one position beyond last index? | 頂端是否是最後索引再往上一格？ | Clarify |
| Is starting at index zero or one both free initially? | 從 0 或 1 起步都不需先額外費用嗎？ | Clarify |
| Should we return only minimum cost, not path? | 是否只回傳最小花費，不回路徑？ | Clarify |
| Are all costs non-negative integers? | cost 是否皆為非負整數？ | Clarify |
| Is in-place cost mutation acceptable as alternative solution? | 可否提 in-place 修改 cost 作替代法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursion tries both one-step and two-step moves. | 暴力遞迴會嘗試 1 階與 2 階兩分支。 | Approach |
| It recomputes overlapping states repeatedly. | 它會重複計算重疊狀態。 | Approach |
| That leads to exponential time. | 因此時間呈指數成長。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Define dp[i] as min cost to reach step i. | 定義 dp[i] 為到達第 i 階的最小花費。 | Approach |
| Transition is min of coming from i-1 or i-2. | 轉移為從 i-1 或 i-2 來的較小值。 | Approach |
| Formula is dp[i] equals min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]). | 公式為 dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])。 | Approach |
| Base values are dp[0]=0 and dp[1]=0. | 基底值是 dp[0]=0、dp[1]=0。 | Approach |
| We only need previous two states, so rolling variables are enough. | 只需前兩狀態，滾動變數即可。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I set n as cost length and initialize prev2 and prev1 to zero. | 我設 n 為 cost 長度，prev2/prev1 先設 0。 | Coding |
| I iterate i from two up to n inclusive. | i 從 2 迭代到 n。 | Coding |
| Option one is prev1 plus cost at i minus one. | 選項一是 prev1+cost[i-1]。 | Coding |
| Option two is prev2 plus cost at i minus two. | 選項二是 prev2+cost[i-2]。 | Coding |
| current is minimum of those two options. | current 取兩者較小。 | Coding |
| Then I shift prev2 to prev1 and prev1 to current. | 然後把 prev2 更新為 prev1，prev1 更新為 current。 | Coding |
| After loop prev1 represents dp[n]. | 迴圈結束後 prev1 就是 dp[n]。 | Coding |
| I return prev1 as final minimum cost. | 我回傳 prev1 作最終最小花費。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run cost [10,15,20]. | 我手跑 cost=[10,15,20]。 | Dry-run |
| Start with prev2 zero and prev1 zero. | 起始 prev2=0、prev1=0。 | Dry-run |
| At i equals two, current is min(15,10), so ten. | i=2 時 current=min(15,10)=10。 | Dry-run |
| Shift gives prev2 zero and prev1 ten. | 更新後 prev2=0、prev1=10。 | Dry-run |
| At i equals three, current is min(30,15), so fifteen. | i=3 時 current=min(30,15)=15。 | Dry-run |
| End of loop, answer is fifteen. | 迴圈結束，答案是 15。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: minimal length two costs array. | 案例一：最小長度 2 的 cost。 | Edge test |
| Case two: many zeros should allow zero total cost path. | 案例二：多個 0 時可達成總花費 0。 | Edge test |
| Case three: strictly increasing costs. | 案例三：嚴格遞增成本。 | Edge test |
| Case four: alternating high and low costs. | 案例四：高低交錯成本。 | Edge test |
| Case five: verify start-at-one is better than start-at-zero. | 案例五：確認從 1 開始比從 0 開始更便宜。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We process each step index once from two to n. | 我們從 2 到 n 每個索引處理一次。 | Complexity |
| Each iteration performs constant-time min and assignments. | 每次迭代只有常數時間 min 與指定。 | Complexity |
| Therefore runtime is linear O(n). | 因此時間是線性 O(n)。 | Complexity |
| Only prev2 prev1 and current are stored, so space is O(1). | 僅儲存 prev2/prev1/current，所以空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define state clearly as min cost to reach step i. | 我先明確定義狀態為到 i 的最小成本。 | If stuck |
| Top is step n, not index n minus one. | 頂端是 step n，不是索引 n-1。 | If stuck |
| Transition comes from i-1 or i-2 only. | 轉移只會從 i-1 或 i-2 來。 | If stuck |
| I pay cost when stepping from previous stair. | 成本是在從前一階踏出時累加。 | If stuck |
| Formula uses cost[i-1] and cost[i-2]. | 公式用到 cost[i-1] 與 cost[i-2]。 | If stuck |
| Base dp[0] and dp[1] are both zero. | 基底 dp[0]、dp[1] 都是 0。 | If stuck |
| Rolling variables can replace full array safely. | 滾動變數可安全取代整個陣列。 | If stuck |
| Let me verify quickly with [10,15,20]. | 我快速用 [10,15,20] 驗證。 | If stuck |
| I get fifteen, so indexing is correct. | 得到 15，索引轉換正確。 | If stuck |
| Great, I can present the final answer now. | 很好，我可以給出最終答案。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved this with bottom-up DP and rolling variables. | 我用自底向上 DP 與滾動變數解題。 | Wrap-up |
| State is minimum cost to reach each step index. | 狀態是到每一階的最小成本。 | Wrap-up |
| Transition chooses cheaper path from one-step or two-step jump. | 轉移在 1 階與 2 階來源中選較便宜者。 | Wrap-up |
| Space is optimized to O(1). | 空間優化到 O(1)。 | Wrap-up |
| Runtime is O(n), clean and interview-friendly. | 時間 O(n)，實作乾淨且面試友好。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: minimum path cost on stairs. | 題型：樓梯最小路徑成本。 | Cheat sheet |
| Start can be step 0 or step 1. | 起點可在 0 或 1。 | Cheat sheet |
| Top is step n. | 頂端是 step n。 | Cheat sheet |
| Define dp[i] min cost to reach i. | 定義 dp[i] 為到 i 的最小成本。 | Cheat sheet |
| Base dp[0]=0. | 基底 dp[0]=0。 | Cheat sheet |
| Base dp[1]=0. | 基底 dp[1]=0。 | Cheat sheet |
| Transition from i-1 and i-2. | 由 i-1 與 i-2 轉移。 | Cheat sheet |
| Formula uses cost[i-1], cost[i-2]. | 公式用 cost[i-1]、cost[i-2]。 | Cheat sheet |
| current = min(path1, path2). | current 取兩路徑較小。 | Cheat sheet |
| Roll prev2 prev1 each step. | 每步更新 prev2 與 prev1。 | Cheat sheet |
| Iterate i from 2 to n. | i 從 2 跑到 n。 | Cheat sheet |
| Answer is dp[n]. | 答案是 dp[n]。 | Cheat sheet |
| Rolling answer is prev1. | 滾動版本答案是 prev1。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Validate [10,15,20] -> 15. | 驗證 [10,15,20] 得 15。 | Cheat sheet |
| Handle zeros naturally. | 可自然處理 0 成本。 | Cheat sheet |
| Common bug: wrong top index meaning. | 常見錯誤：頂端索引定義錯。 | Cheat sheet |
| Common bug: off-by-one in formula. | 常見錯誤：公式索引 off-by-one。 | Cheat sheet |
| Alternative: in-place mutate cost array. | 替代法：原地修改 cost。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Bottom-up recurrence and rolling optimization preserved.
- No hallucinated constraints: ✅ Matches source start rules and top-step definition.
- Language simplicity: ✅ Short, clear, and interview-delivery oriented.
