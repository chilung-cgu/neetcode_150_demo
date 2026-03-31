# 03 House Robber — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/03_House_Robber.md`

> Quick links: [Source Solution](../03_House_Robber.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the House Robber problem. | 我先重述 House Robber。 | Restatement |
| We have money in each house along one street. | 一條街上每間房子有不同金額。 | Restatement |
| We cannot rob two adjacent houses in the same night. | 同一晚不能搶相鄰兩間房。 | Restatement |
| We need the maximum total amount we can rob. | 要找可搶到的最大總金額。 | Restatement |
| This is an optimization with local exclusion constraint. | 這是有鄰接排斥限制的最佳化問題。 | Restatement |
| I will solve it with rolling dynamic programming. | 我會用滾動 DP 來解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are all house values non-negative? | 房屋金額是否皆為非負？ | Clarify |
| Is input guaranteed non-empty? | 輸入是否保證非空？ | Clarify |
| Do we return only max amount, not robbed indices? | 只回傳最大金額，不需回傳索引嗎？ | Clarify |
| Is O(1) extra space expected after DP idea? | 提出 DP 後是否期待 O(1) 空間？ | Clarify |
| Can I explain recurrence before coding details? | 可否先講遞推再寫程式？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries rob or skip at each house recursively. | 暴力遞迴在每間房做搶或不搶。 | Approach |
| State recurrence is max(nums[i]+f(i+2), f(i+1)). | 狀態是 max(nums[i]+f(i+2), f(i+1))。 | Approach |
| Without memoization this is exponential. | 不做記憶化時是指數時間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let prev1 be best result up to previous house. | 令 prev1 為到前一間房的最佳解。 | Approach |
| Let prev2 be best result up to house before previous. | 令 prev2 為到前前一間房的最佳解。 | Approach |
| For current money x, best is max(prev1, prev2 plus x). | 當前金額 x 的最佳值是 max(prev1, prev2+x)。 | Approach |
| Then shift prev2 to prev1 and prev1 to current best. | 接著把 prev2 更新為 prev1，prev1 更新為 current。 | Approach |
| This gives linear time and constant extra space. | 如此可達線性時間與常數空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize prev2 and prev1 as zero. | 我先把 prev2 與 prev1 設為 0。 | Coding |
| I iterate each house value in nums once. | 我遍歷 nums 中每個房屋金額一次。 | Coding |
| current equals max of skipping or robbing this house. | current 等於跳過或搶這間的較大值。 | Coding |
| Skip case is prev1 unchanged. | 跳過情況就是維持 prev1。 | Coding |
| Rob case is prev2 plus current house value. | 搶劫情況是 prev2+當前金額。 | Coding |
| After compute current, I shift prev2 to prev1. | 算完 current 後，我把 prev2 更新成舊 prev1。 | Coding |
| I set prev1 to current best. | 我把 prev1 更新為 current 最佳值。 | Coding |
| At end, prev1 is the final maximum loot. | 最後 prev1 就是最大可搶金額。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [2,7,9,3,1]. | 我手跑 nums=[2,7,9,3,1]。 | Dry-run |
| Start prev2 zero prev1 zero. | 起始 prev2=0、prev1=0。 | Dry-run |
| House two gives current two. | 金額 2 時 current=2。 | Dry-run |
| House seven gives current seven. | 金額 7 時 current=7。 | Dry-run |
| House nine gives current eleven by robbing two and nine. | 金額 9 時 current=11（搶 2 與 9）。 | Dry-run |
| House three keeps current eleven. | 金額 3 時 current 維持 11。 | Dry-run |
| House one gives final twelve. | 金額 1 時最終得到 12。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single house returns its value. | 案例一：單一房屋回自身金額。 | Edge test |
| Case two: two houses returns max of both. | 案例二：兩間房回兩者較大。 | Edge test |
| Case three: all zeros returns zero. | 案例三：全為 0 應回 0。 | Edge test |
| Case four: alternating high-low values. | 案例四：高低交錯金額。 | Edge test |
| Case five: strictly increasing sequence. | 案例五：嚴格遞增序列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan the array once from left to right. | 我們由左到右掃描陣列一次。 | Complexity |
| Each step does constant-time max and assignment operations. | 每一步只有常數次 max 與指定。 | Complexity |
| Therefore runtime is O(n). | 因此時間是 O(n)。 | Complexity |
| We keep only prev1 prev2 and current, so space is O(1). | 僅保留 prev1/prev2/current，所以空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on decision at one house. | 我先聚焦單一房屋的決策。 | If stuck |
| I either rob this house or skip it. | 我不是搶這間就是跳過。 | If stuck |
| If I rob it, previous house must be skipped. | 若搶這間，前一間必須跳過。 | If stuck |
| If I skip it, best so far stays unchanged. | 若跳過，最佳值保持不變。 | If stuck |
| That gives current equals max(prev1, prev2 plus value). | 因此 current=max(prev1, prev2+value)。 | If stuck |
| Rolling variables are enough for this recurrence. | 這個遞推只需滾動變數。 | If stuck |
| Let me validate with [1,2,3,1]. | 我用 [1,2,3,1] 驗證。 | If stuck |
| I obtain four as expected. | 得到 4，符合預期。 | If stuck |
| So recurrence and update order are correct. | 遞推與更新順序都正確。 | If stuck |
| Great, I can conclude now. | 很好，我可以收尾。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved House Robber with rolling DP. | 我用滾動 DP 解出 House Robber。 | Wrap-up |
| Each house compares rob versus skip options. | 每間房都比較搶與不搶兩選項。 | Wrap-up |
| Adjacency constraint is handled by prev2 dependency. | 相鄰限制由 prev2 依賴處理。 | Wrap-up |
| Runtime is O(n) with O(1) extra space. | 時間 O(n)、額外空間 O(1)。 | Wrap-up |
| This is the standard interview-optimal solution. | 這是面試常見的最佳實作。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: linear DP with exclusion constraint. | 題型：帶排斥條件的線性 DP。 | Cheat sheet |
| Cannot rob adjacent houses. | 相鄰房屋不可同時搶。 | Cheat sheet |
| State uses best up to previous houses. | 狀態用前綴最佳值表示。 | Cheat sheet |
| prev1 = best up to i-1. | prev1=到 i-1 的最佳。 | Cheat sheet |
| prev2 = best up to i-2. | prev2=到 i-2 的最佳。 | Cheat sheet |
| current = max(prev1, prev2+value). | current=max(prev1,prev2+value)。 | Cheat sheet |
| Initialize prev1 and prev2 to zero. | 初始 prev1、prev2 為 0。 | Cheat sheet |
| Iterate each house value once. | 每個房屋金額只處理一次。 | Cheat sheet |
| Update shift prev2=prev1. | 更新時 prev2=prev1。 | Cheat sheet |
| Update shift prev1=current. | 更新時 prev1=current。 | Cheat sheet |
| End answer is prev1. | 結尾答案是 prev1。 | Cheat sheet |
| Single house edge returns value. | 單一房屋回自身值。 | Cheat sheet |
| Two houses edge returns max. | 兩房邊界回 max。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Works for zeros and mixed values. | 可處理 0 與混合值。 | Cheat sheet |
| Common bug: wrong update order. | 常見錯誤：更新順序錯。 | Cheat sheet |
| Common bug: using current updated prev1 too early. | 常見錯誤：過早使用更新後 prev1。 | Cheat sheet |
| House Robber II builds on this helper. | House Robber II 以此為核心。 | Cheat sheet |
| Mention recurrence clearly in interview. | 面試時清楚說遞推式。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Rolling DP max recurrence is preserved.
- No hallucinated constraints: ✅ Uses linear street and adjacency rule exactly.
- Language simplicity: ✅ Direct interview narration and concise formula lines.
