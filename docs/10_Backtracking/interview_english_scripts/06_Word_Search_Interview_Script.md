# 06 Word Search — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/06_Word_Search.md`

> Quick links: [Source Solution](../06_Word_Search.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the word search problem. | 我先重述 Word Search。 | Restatement |
| We have a 2D board of characters and a target word. | 題目給字元網格與目標單字。 | Restatement |
| We need to check whether the word exists in the board. | 需要判斷單字是否存在於網格中。 | Restatement |
| Movement is four directions only: up down left right. | 只可上下左右四方向移動。 | Restatement |
| One cell cannot be reused in the same path. | 同一路徑中同一格不能重複使用。 | Restatement |
| I will run DFS backtracking from each possible start cell. | 我會從每個起點做 DFS 回溯。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are diagonal moves disallowed? | 是否明確禁止對角線移動？ | Clarify |
| Can I mutate board temporarily for visited marking? | 可否暫時改動 board 做 visited 標記？ | Clarify |
| Is returning boolean only enough, no path required? | 只需回傳布林值，不需回傳路徑嗎？ | Clarify |
| Should search stop immediately after first successful path? | 找到第一條成功路徑就可立即停止嗎？ | Clarify |
| Do constraints allow DFS from every cell safely? | 題目限制下可安全從每格做 DFS 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries every path of matching length blindly. | 暴力法盲目嘗試所有對應長度路徑。 | Approach |
| That explodes combinatorially and repeats many invalid states. | 這會組合爆炸且重複大量無效狀態。 | Approach |
| We need early mismatch checks and backtracking pruning. | 需要提早 mismatch 檢查與回溯剪枝。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Iterate every cell as a potential first character. | 遍歷每格當作第一字元起點。 | Approach |
| DFS state is row, col, and current word index. | DFS 狀態是 row、col、字元索引。 | Approach |
| Reject branch when out of bounds or char mismatch. | 越界或字元不符時立即拒絕分支。 | Approach |
| Mark cell visited temporarily, explore four directions, then restore. | 暫標記已訪問，走四方向後再還原。 | Approach |
| If index reaches word length, we return true immediately. | 當索引到 word 長度就立刻回 true。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I loop through all board cells as possible starts. | 我先遍歷所有格子做可能起點。 | Coding |
| I call dfs only when first character matches. | 只有首字匹配才呼叫 dfs。 | Coding |
| In dfs, first base case is index equals word length. | dfs 第一個基底是 index 到 word 長度。 | Coding |
| Then I check boundary and character mismatch guard. | 接著檢查邊界與字元不符守衛。 | Coding |
| I store current char and mark board cell as visited marker. | 我先存原字元並標記該格為已訪問。 | Coding |
| I recurse in four directions with index plus one. | 我對四方向以 index+1 遞迴。 | Coding |
| After recursion I restore original board character. | 遞迴後我還原原始字元。 | Coding |
| I return true if any direction succeeds. | 任何方向成功就回 true。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run word ABCCED on the sample board. | 我手跑範例板上的 ABCCED。 | Dry-run |
| Start at A on row zero col zero. | 從第 0 列第 0 欄的 A 開始。 | Dry-run |
| Move right to B then right to C. | 先向右到 B，再向右到 C。 | Dry-run |
| Next move down to second C. | 再往下到第二個 C。 | Dry-run |
| Then move down to E and left to D. | 接著往下到 E，再往左到 D。 | Dry-run |
| Index reaches word end, so path is successful. | 索引到字尾，路徑成功。 | Dry-run |
| Function returns true immediately. | 函式立刻回傳 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one-cell board with matching one-letter word. | 案例一：單格板且單字一字且匹配。 | Edge test |
| Case two: one-cell board with non-matching letter. | 案例二：單格板但字元不匹配。 | Edge test |
| Case three: word requires revisiting same cell and should fail. | 案例三：需要重訪同格時應失敗。 | Edge test |
| Case four: word longer than board cell count should fail quickly. | 案例四：word 長於格子總數應快速失敗。 | Edge test |
| Case five: multiple possible starts but only one valid path. | 案例五：多個起點中僅一條有效路徑。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n times four to the L). | 時間複雜度是 O(m*n*4^L)。 | Complexity |
| Recursion stack space is O(L). | 遞迴堆疊空間是 O(L)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We may start DFS from every cell in m by n board. | m*n 個格子都可能成為 DFS 起點。 | Complexity |
| DFS depth is L, the word length. | DFS 深度為單字長度 L。 | Complexity |
| Each step can branch up to four directions in worst case. | 最壞每步最多分支四方向。 | Complexity |
| So worst runtime is O(m*n*4^L), and stack is O(L). | 最壞時間 O(m*n*4^L)，堆疊 O(L)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me treat this as DFS path search on a grid. | 我把這題視為網格 DFS 路徑搜尋。 | If stuck |
| State needs row col and matched index. | 狀態需要 row、col、匹配索引。 | If stuck |
| I should reject out of bounds and mismatch immediately. | 越界與不匹配要立即拒絕。 | If stuck |
| Reuse is disallowed, so I must mark visited. | 不能重用格子，所以必須標記 visited。 | If stuck |
| In-place mark then restore is simplest. | 就地標記再還原最簡潔。 | If stuck |
| I explore exactly four directions per step. | 每步只探索四個方向。 | If stuck |
| Success condition is index equals word length. | 成功條件是 index 等於 word 長度。 | If stuck |
| Let me verify quickly with ABCCED sample path. | 我用 ABCCED 範例路徑快速驗證。 | If stuck |
| Path reaches end without reusing cells, so true. | 路徑到終點且未重用格子，故為 true。 | If stuck |
| Great, DFS and backtracking rules are consistent. | 很好，DFS 與回溯規則已一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved Word Search with grid DFS backtracking. | 我用網格 DFS 回溯解出 Word Search。 | Wrap-up |
| Each path tracks index and avoids cell reuse. | 每條路徑追蹤索引並避免重用格子。 | Wrap-up |
| In-place visit marking keeps implementation compact. | 就地標記 visited 讓實作精簡。 | Wrap-up |
| Runtime is O(m*n*4^L) in worst case. | 最壞時間為 O(m*n*4^L)。 | Wrap-up |
| I can also mention pre-check pruning ideas if needed. | 若需要我可補充預檢剪枝想法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: grid path existence. | 題型：網格路徑存在性。 | Cheat sheet |
| Need boolean answer only. | 只需布林答案。 | Cheat sheet |
| Move directions: up down left right. | 方向：上、下、左、右。 | Cheat sheet |
| Cannot reuse same cell in path. | 路徑中不可重用同格。 | Cheat sheet |
| Start DFS from each cell. | 從每格啟動 DFS。 | Cheat sheet |
| DFS state: row col index. | DFS 狀態：row、col、index。 | Cheat sheet |
| Success when index == word length. | index==word 長度時成功。 | Cheat sheet |
| Guard: out of bounds fails. | 守衛：越界失敗。 | Cheat sheet |
| Guard: char mismatch fails. | 守衛：字元不符失敗。 | Cheat sheet |
| Mark current cell visited. | 標記當前格為 visited。 | Cheat sheet |
| Recurse four directions. | 遞迴四個方向。 | Cheat sheet |
| Restore cell after recursion. | 遞迴後還原該格。 | Cheat sheet |
| Return true if any branch true. | 任一分支 true 即回 true。 | Cheat sheet |
| Loop all starts until found. | 掃所有起點直到找到。 | Cheat sheet |
| Worst time O(m*n*4^L). | 最壞時間 O(m*n*4^L)。 | Cheat sheet |
| Stack space O(L). | 堆疊空間 O(L)。 | Cheat sheet |
| Test ABCCED should pass. | ABCCED 測試應通過。 | Cheat sheet |
| Test ABCB should fail. | ABCB 測試應失敗。 | Cheat sheet |
| Common bug: forget restore step. | 常見錯誤：忘記還原。 | Cheat sheet |
| Common bug: allowing diagonal moves. | 常見錯誤：誤允許對角線。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS + in-place visited backtracking preserved.
- No hallucinated constraints: ✅ Uses four-direction and no-reuse rules exactly.
- Language simplicity: ✅ Clear interview flow with explicit success/guard logic.
