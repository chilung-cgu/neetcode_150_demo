# 02 Combination Sum — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/02_Combination_Sum.md`

> Quick links: [Source Solution](../02_Combination_Sum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the combination sum problem. | 我先重述 combination sum 題目。 | Restatement |
| We are given unique candidates and a target value. | 題目給互異 candidates 與 target。 | Restatement |
| We need all unique combinations summing to target. | 要找和為 target 的所有唯一組合。 | Restatement |
| Each candidate can be used unlimited times. | 每個 candidate 可以重複使用。 | Restatement |
| Combination order does not matter in output. | 輸出中組合的順序不重要。 | Restatement |
| I will use DFS backtracking with include or skip branching. | 我會用 DFS 回溯做選取或跳過分支。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are all candidate values positive integers? | candidates 是否皆為正整數？ | Clarify |
| Can I assume candidates have no duplicates? | 可否假設 candidates 無重複？ | Clarify |
| Is output order of combinations irrelevant? | 輸出組合順序是否無要求？ | Clarify |
| Should I avoid duplicate permutations like two-three and three-two? | 是否要避免 [2,3] 與 [3,2] 這種重複？ | Clarify |
| Is recursive DFS acceptable under given constraints? | 在此限制下可用遞迴 DFS 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries all multisets and checks their sums. | 暴力法嘗試所有多重集合再檢查和。 | Approach |
| This quickly explodes due to unlimited reuse of numbers. | 因可無限重複，組合數會快速爆炸。 | Approach |
| We need pruning with recursion state to stay practical. | 需要有狀態與剪枝的遞迴。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use dfs with parameters index and remaining target. | 用 dfs，參數是 index 與剩餘 target。 | Approach |
| Include branch keeps same index because reuse is allowed. | 選取分支維持同 index，因可重複使用。 | Approach |
| Exclude branch moves to next index to avoid permutations. | 跳過分支移到下一 index 以避免排列重複。 | Approach |
| Stop branch when remaining target is zero or negative. | 剩餘 target 為 0 或負時停止分支。 | Approach |
| Sorting can help pruning, but core logic works either way. | 排序可輔助剪枝，但核心邏輯不變。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize result list and current combination path. | 我先初始化結果與當前組合路徑。 | Coding |
| I optionally sort candidates for better pruning. | 我可先排序 candidates 以利剪枝。 | Coding |
| I define dfs(index, remaining) recursion. | 我定義 dfs(index, remaining) 遞迴。 | Coding |
| If remaining equals zero, I record current path. | remaining 為 0 時記錄當前路徑。 | Coding |
| If remaining is negative or index out of range, I return. | remaining 為負或 index 越界就返回。 | Coding |
| Include branch pushes candidates[index] and recurses with same index. | 選取分支 push 當前值並用同 index 遞迴。 | Coding |
| After that I pop and run skip branch with index plus one. | 然後 pop，再跑 index+1 的跳過分支。 | Coding |
| This guarantees unique combinations without order duplicates. | 這可保證組合唯一且不產生排列重複。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run candidates [2,3,6,7] and target seven. | 我手跑 candidates [2,3,6,7]、target=7。 | Dry-run |
| Start at index zero with remaining seven and empty path. | 從 index=0、remaining=7、空路徑開始。 | Dry-run |
| Include two repeatedly gives path [2,2,2], remaining one, then fails. | 連續選 2 到 [2,2,2]，remaining=1，之後失敗。 | Dry-run |
| Backtrack one step and try three to get [2,2,3]. | 回溯一步改試 3，得到 [2,2,3]。 | Dry-run |
| Remaining becomes zero, so record [2,2,3]. | 剩餘變 0，記錄 [2,2,3]。 | Dry-run |
| Skip to candidate seven path also reaches exact zero. | 跳到 candidate 7 的路徑也可剛好湊滿。 | Dry-run |
| Final results are [2,2,3] and [7]. | 最終答案是 [2,2,3] 與 [7]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: target smaller than every candidate returns empty list. | 案例一：target 小於所有候選值應回空。 | Edge test |
| Case two: one candidate exactly equals target. | 案例二：某個候選值剛好等於 target。 | Edge test |
| Case three: only one candidate reused many times. | 案例三：單一候選值需重複使用多次。 | Edge test |
| Case four: no combination can reach target. | 案例四：任何組合都無法達到 target。 | Edge test |
| Case five: multiple valid combinations with shared prefixes. | 案例五：多組合法共享前綴路徑。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is exponential in search tree size, often written as O(n power t over m). | 時間是指數級，常寫作 O(n^(t/m))。 | Complexity |
| Recursion depth is bounded by target over minimum candidate. | 遞迴深度上限約為 target/最小候選值。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| The branching factor depends on candidate count and pruning. | 分支係數取決於候選數與剪枝效果。 | Complexity |
| Depth can grow to roughly target divided by smallest value. | 深度大約可到 target/最小值。 | Complexity |
| So runtime is exponential in worst case, often bounded by O(n power t over m). | 最壞時間為指數級，常以上界 O(n^(t/m)) 描述。 | Complexity |
| Extra recursion stack space is O(t over m), excluding output. | 不含輸出時遞迴堆疊空間約 O(t/m)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate this into include and skip decisions. | 我先拆成選取與跳過兩種決策。 | If stuck |
| Include should keep index because reuse is allowed. | 選取分支要維持 index，因可重複。 | If stuck |
| Skip should move to index plus one. | 跳過分支要移到 index+1。 | If stuck |
| That prevents duplicate permutations automatically. | 這會自動避免排列重複。 | If stuck |
| I should stop when remaining target is below zero. | remaining 小於 0 時要立刻停止。 | If stuck |
| I should record path when remaining is exactly zero. | remaining 等於 0 時要記錄答案。 | If stuck |
| Let me test with target seven sample. | 我用 target=7 範例驗證。 | If stuck |
| I get [2,2,3] and [7], which is correct. | 得到 [2,2,3] 與 [7]，正確。 | If stuck |
| So branch transitions are now consistent. | 目前分支轉移已一致。 | If stuck |
| Great, I can finalize with complexity trade-off. | 很好，我可收尾複雜度與取捨。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved combination sum using DFS backtracking. | 我用 DFS 回溯解出 combination sum。 | Wrap-up |
| The key is same-index include and next-index skip. | 關鍵是同索引選取與下一索引跳過。 | Wrap-up |
| This avoids order-duplicate combinations naturally. | 這可自然避免順序重複組合。 | Wrap-up |
| We stop early on invalid negative remaining sums. | 對 remaining 為負會提前停止。 | Wrap-up |
| I can also discuss sorting-based pruning improvements. | 我也可補充排序剪枝優化。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: unbounded combination sum. | 題型：可重複取用的組合總和。 | Cheat sheet |
| Candidates are unique. | candidates 互異。 | Cheat sheet |
| Need sum exactly target. | 需剛好湊到 target。 | Cheat sheet |
| Combination order does not matter. | 組合順序不重要。 | Cheat sheet |
| Use DFS with index and remaining. | DFS 狀態為 index 與 remaining。 | Cheat sheet |
| Base success when remaining is zero. | remaining=0 為成功。 | Cheat sheet |
| Base fail when remaining < 0. | remaining<0 為失敗。 | Cheat sheet |
| Base fail when index out of range. | index 越界為失敗。 | Cheat sheet |
| Include branch keeps same index. | 選取分支維持同 index。 | Cheat sheet |
| Skip branch moves to index+1. | 跳過分支移到 index+1。 | Cheat sheet |
| Push before include recursion. | include 前先 push。 | Cheat sheet |
| Pop after include recursion. | include 後記得 pop。 | Cheat sheet |
| Record path copy at success. | 成功時記錄路徑拷貝。 | Cheat sheet |
| Prevent permutations by index order. | 以索引順序避免排列重複。 | Cheat sheet |
| Optional sort for pruning. | 可選排序提升剪枝。 | Cheat sheet |
| Typical example gives [2,2,3], [7]. | 典型範例答案 [2,2,3]、[7]。 | Cheat sheet |
| Runtime is exponential worst case. | 最壞時間為指數級。 | Cheat sheet |
| Stack depth about target/minVal. | 堆疊深度約 target/最小值。 | Cheat sheet |
| Output size can dominate cost. | 輸出規模可能主導成本。 | Cheat sheet |
| Mention trade-off clearly in interview. | 面試時清楚說明取捨。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS include/skip with same-index reuse is preserved.
- No hallucinated constraints: ✅ Matches unique-candidate and unlimited-use semantics.
- Language simplicity: ✅ Straightforward interview narration with explicit branch logic.
