# 04 House Robber II — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/04_House_Robber_II.md`

> Quick links: [Source Solution](../04_House_Robber_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate House Robber Two. | 我先重述 House Robber II。 | Restatement |
| Houses are arranged in a circle this time. | 這次房子是環狀排列。 | Restatement |
| First and last houses are adjacent. | 第一間與最後一間相鄰。 | Restatement |
| We still cannot rob two adjacent houses. | 仍不能同時搶相鄰房屋。 | Restatement |
| We need the maximum total money. | 要求可搶到的最大總金額。 | Restatement |
| I will split into two linear robber subproblems. | 我會拆成兩個線性子問題。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is array length at least one? | 陣列長度是否至少為 1？ | Clarify |
| For one house, can we directly return that value? | 若只有一間房可直接回該值嗎？ | Clarify |
| Is output just maximum amount, no chosen indices needed? | 是否只回最大金額，不需回索引？ | Clarify |
| Can helper function reuse House Robber One logic? | 可否用 helper 重用 House Robber I 邏輯？ | Clarify |
| Is O(n) time and O(1) extra space expected? | 是否期望 O(n) 時間與 O(1) 額外空間？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force explores rob or skip for every house with circular constraint. | 暴力法在環狀限制下枚舉每間房搶或不搶。 | Approach |
| Circular adjacency of first and last complicates direct recursion. | 首尾相鄰讓直接遞迴更複雜。 | Approach |
| Complexity becomes exponential. | 複雜度會是指數級。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Because first and last cannot both be robbed, split cases. | 因首尾不能同搶，所以拆兩種情況。 | Approach |
| Case one robs from index zero to n minus two. | 情況一考慮範圍 0 到 n-2。 | Approach |
| Case two robs from index one to n minus one. | 情況二考慮範圍 1 到 n-1。 | Approach |
| Each case is standard linear House Robber DP. | 每種情況都是線性 House Robber DP。 | Approach |
| Final answer is max of the two case results. | 最終答案取兩種結果較大者。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I handle n equals one separately and return nums[0]. | 我先特判 n=1 回 nums[0]。 | Coding |
| I compute max1 using helper on range zero to n minus two. | 用 helper 算範圍 0 到 n-2 的 max1。 | Coding |
| I compute max2 using helper on range one to n minus one. | 用 helper 算範圍 1 到 n-1 的 max2。 | Coding |
| Helper uses rolling DP prev2 and prev1. | helper 用滾動 DP 的 prev2、prev1。 | Coding |
| For each index in range, current is max(prev1, prev2+nums[i]). | 範圍內每點 current=max(prev1,prev2+nums[i])。 | Coding |
| Then shift prev2 to prev1 and prev1 to current. | 然後更新 prev2=prev1、prev1=current。 | Coding |
| Helper returns prev1 for that linear segment. | helper 回傳該線性段的 prev1。 | Coding |
| Main function returns max(max1, max2). | 主函式回傳 max(max1,max2)。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [2,3,2]. | 我手跑 nums=[2,3,2]。 | Dry-run |
| n is three, so not single-house edge case. | n=3，不是單房邊界。 | Dry-run |
| Case one range [2,3] gives three. | 情況一範圍 [2,3] 給 3。 | Dry-run |
| Case two range [3,2] also gives three. | 情況二範圍 [3,2] 也給 3。 | Dry-run |
| Max of both cases is three. | 兩者取大為 3。 | Dry-run |
| That matches expected output. | 與預期輸出一致。 | Dry-run |
| Circular conflict is handled by split strategy. | 環狀衝突由拆分策略正確處理。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals one returns nums[0]. | 案例一：n=1 回 nums[0]。 | Edge test |
| Case two: n equals two returns max of two values. | 案例二：n=2 回兩值較大者。 | Edge test |
| Case three: all equal values in a circle. | 案例三：環狀全相同值。 | Edge test |
| Case four: high values at both ends cannot both be taken. | 案例四：首尾都高值但不可同取。 | Edge test |
| Case five: zeros mixed with positive values. | 案例五：0 與正值混合。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We run linear robber helper twice on two ranges. | 我們在兩個範圍各跑一次線性 helper。 | Complexity |
| Each helper scans its range once with constant work per step. | 每個 helper 單次掃描，步驟工作量為常數。 | Complexity |
| Total runtime is proportional to n, so O(n). | 總時間與 n 成正比，因此 O(n)。 | Complexity |
| Helpers keep only rolling variables, so extra space is O(1). | helper 只用滾動變數，額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me isolate the circular part first. | 我先隔離環狀帶來的差異。 | If stuck |
| The only new constraint is first-last adjacency. | 唯一新增限制是首尾相鄰。 | If stuck |
| So both ends cannot be chosen together. | 所以首尾不可能同時被選。 | If stuck |
| That naturally yields two linear scenarios. | 這自然形成兩個線性情境。 | If stuck |
| Scenario A excludes last, scenario B excludes first. | 情境 A 排除尾端，情境 B 排除首端。 | If stuck |
| Each scenario is plain House Robber One. | 每個情境都可用 House Robber I。 | If stuck |
| Then take max of both scenario results. | 最後取兩情境結果較大者。 | If stuck |
| Let me verify with [1,2,3,1]. | 我用 [1,2,3,1] 驗證。 | If stuck |
| I get four, matching sample answer. | 得到 4，符合範例答案。 | If stuck |
| Great, circular handling is now clear and correct. | 很好，環狀處理已清楚且正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved House Robber Two by reducing it to two linear runs. | 我把 House Robber II 化成兩次線性求解。 | Wrap-up |
| This avoids direct circular-state complexity. | 這可避免直接處理環狀狀態複雜度。 | Wrap-up |
| Both runs reuse the standard rolling DP helper. | 兩次都重用標準滾動 DP helper。 | Wrap-up |
| Final answer is max of excluding first or excluding last. | 最終答案是排除首端與排除尾端兩者取大。 | Wrap-up |
| Runtime remains O(n) with O(1) extra space. | 複雜度維持 O(n) 時間、O(1) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: circular House Robber. | 題型：環狀 House Robber。 | Cheat sheet |
| First and last are adjacent. | 首尾相鄰。 | Cheat sheet |
| Cannot take both ends together. | 首尾不可同時取。 | Cheat sheet |
| Split into two linear cases. | 拆成兩個線性情境。 | Cheat sheet |
| Case A: range [0, n-2]. | 情境 A：範圍 [0,n-2]。 | Cheat sheet |
| Case B: range [1, n-1]. | 情境 B：範圍 [1,n-1]。 | Cheat sheet |
| Solve each by House Robber I helper. | 各自用 House Robber I helper。 | Cheat sheet |
| Helper uses prev1 and prev2. | helper 使用 prev1、prev2。 | Cheat sheet |
| current = max(prev1, prev2+nums[i]). | current=max(prev1,prev2+nums[i])。 | Cheat sheet |
| Shift states each iteration. | 每次迭代更新狀態。 | Cheat sheet |
| Helper returns segment max loot. | helper 回傳區段最大值。 | Cheat sheet |
| Final answer = max(caseA, caseB). | 最終答案=max(情境A,情境B)。 | Cheat sheet |
| n=1 special case first. | 先處理 n=1 特例。 | Cheat sheet |
| n=2 answer is max of two. | n=2 答案是兩者 max。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Validate [2,3,2] -> 3. | 驗證 [2,3,2] 得 3。 | Cheat sheet |
| Validate [1,2,3,1] -> 4. | 驗證 [1,2,3,1] 得 4。 | Cheat sheet |
| Common bug: forgetting n=1 edge. | 常見錯誤：漏掉 n=1。 | Cheat sheet |
| Common bug: running helper on wrong ranges. | 常見錯誤：helper 範圍寫錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Two-range reduction plus linear helper preserved.
- No hallucinated constraints: ✅ Correct circular adjacency interpretation.
- Language simplicity: ✅ Concise interview delivery with clear split strategy.
