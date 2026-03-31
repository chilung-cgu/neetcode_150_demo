# 07 Longest Increasing Path Matrix — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/07_Longest_Increasing_Path_Matrix.md`

> Quick links: [Source Solution](../07_Longest_Increasing_Path_Matrix.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate longest increasing path in a matrix. | 我先重述矩陣最長遞增路徑題。 | Restatement |
| We have a matrix and can move up down left or right. | 題目給矩陣，可上下左右移動。 | Restatement |
| We need the maximum length of a strictly increasing path. | 要求嚴格遞增路徑的最長長度。 | Restatement |
| We cannot move diagonally or go outside bounds. | 不能斜走，也不能越界。 | Restatement |
| Strict increase implies no cycles along a valid path. | 嚴格遞增代表有效路徑中不會成環。 | Restatement |
| I will use DFS with memoization for each cell. | 我會對每格做 DFS 加記憶化。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is matrix guaranteed non-empty in constraints? | 限制是否保證矩陣非空？ | Clarify |
| Are moves limited to four cardinal directions only? | 是否只允許四個正交方向？ | Clarify |
| Is path required to be strictly increasing, not non-decreasing? | 路徑是嚴格遞增，不是非遞減，對嗎？ | Clarify |
| Do we return length only, not the path itself? | 是否只回傳長度，不回路徑內容？ | Clarify |
| Is O(m times n) expected with memoization? | 加記憶化後 O(m*n) 是否預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force starts DFS from every cell without cache. | 暴力法從每格起 DFS 但不快取。 | Approach |
| Same subpaths are recomputed many times. | 相同子路徑會被反覆重算。 | Approach |
| Runtime blows up quickly on larger grids. | 在大矩陣上時間會快速爆炸。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let memo[r][c] be longest increasing path starting at cell r c. | 定義 memo[r][c] 為從 r,c 出發最長遞增路徑。 | Approach |
| DFS explores neighbors with larger values only. | DFS 只走值更大的鄰居。 | Approach |
| Transition is one plus max of valid neighbor results. | 轉移為 1 加上合法鄰居結果最大值。 | Approach |
| Cache each cell result after first computation. | 每格第一次算完就快取結果。 | Approach |
| Global answer is max memo value across all cells. | 全域答案是所有格子的 memo 最大值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I store row count and column count. | 我先記錄列數與欄數。 | Coding |
| I initialize memo table with zeros meaning not computed. | 我把 memo 初始為 0 代表未計算。 | Coding |
| I define directions array for four moves. | 我定義四方向陣列。 | Coding |
| DFS returns memo value directly if already filled. | DFS 若已有 memo 值就直接回傳。 | Coding |
| Otherwise I start best length as one for current cell. | 否則先把當前最佳長度設為 1。 | Coding |
| For each neighbor, if in bounds and larger, recurse and update best. | 對每個鄰居，若合法且更大就遞迴更新 best。 | Coding |
| I save best to memo and return it. | 我把 best 存入 memo 並回傳。 | Coding |
| Main loop calls DFS on every cell and tracks global maximum. | 主迴圈對每格呼叫 DFS 並維護全域最大。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run matrix [[9,9,4],[6,6,8],[2,1,1]]. | 我手跑矩陣 [[9,9,4],[6,6,8],[2,1,1]]。 | Dry-run |
| Starting from value one at bottom middle, we can go to two then six then nine. | 從底部中間的 1 可走到 2、再到 6、再到 9。 | Dry-run |
| That path length is four. | 這條路徑長度是 4。 | Dry-run |
| Memo stores computed lengths, so repeated calls reuse results. | memo 會存結果，重複呼叫可重用。 | Dry-run |
| Other starts cannot exceed this length in this matrix. | 本矩陣其他起點不會超過此長度。 | Dry-run |
| Final answer is four. | 最終答案為 4。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single cell matrix should return one. | 案例一：單格矩陣應回 1。 | Edge test |
| Case two: all equal values should return one. | 案例二：全相等數值應回 1。 | Edge test |
| Case three: strictly increasing snake-like path. | 案例三：蛇形嚴格遞增路徑。 | Edge test |
| Case four: strictly decreasing matrix where best is one. | 案例四：嚴格遞減矩陣最佳仍為 1。 | Edge test |
| Case five: multiple local peaks and valleys. | 案例五：多個局部高低峰。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m times n). | 空間複雜度是 O(m*n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each cell DFS is fully computed at most once due to memoization. | 因記憶化，每格 DFS 最多完整計算一次。 | Complexity |
| Each computation checks up to four neighbors. | 每次計算最多檢查四個鄰居。 | Complexity |
| So total runtime is O(m*n). | 所以總時間為 O(m*n)。 | Complexity |
| Memo table plus recursion stack uses O(m*n) in worst case. | memo 表加遞迴堆疊最壞為 O(m*n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define DFS state first. | 我先定義 DFS 狀態。 | If stuck |
| State is longest path starting from current cell. | 狀態是從當前格出發的最長路徑。 | If stuck |
| I should memoize by cell coordinates. | 我應該以座標做記憶化。 | If stuck |
| Neighbor is valid only if value is strictly larger. | 鄰居只有值更大才合法。 | If stuck |
| Base local length is always one. | 本地基礎長度永遠是 1。 | If stuck |
| Transition is one plus best neighbor result. | 轉移是 1 加最佳鄰居結果。 | If stuck |
| Let me sanity-check all-equal matrix quickly. | 我快速檢查全相等矩陣。 | If stuck |
| Every cell should return one there. | 每格在該情況都應回 1。 | If stuck |
| Then global max logic is straightforward. | 接著全域最大值邏輯就很直接。 | If stuck |
| Great, now implementation is stable. | 很好，現在實作方向穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved this using DFS plus memoization. | 我用 DFS 加記憶化解這題。 | Wrap-up |
| Each cell stores its best path length once. | 每格只需存一次最佳路徑長度。 | Wrap-up |
| Strictly increasing constraint guides valid transitions. | 嚴格遞增條件決定合法轉移。 | Wrap-up |
| Complexity is O(m*n) time and O(m*n) space. | 複雜度是 O(m*n) 時間、O(m*n) 空間。 | Wrap-up |
| This is the standard interview solution for this problem. | 這是此題面試標準解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: longest strictly increasing path in grid. | 目標：網格中的最長嚴格遞增路徑。 | Cheat sheet |
| Moves: up/down/left/right only. | 移動：僅上下左右。 | Cheat sheet |
| Use DFS from each cell. | 從每格出發做 DFS。 | Cheat sheet |
| Memoize result per cell. | 每格結果做記憶化。 | Cheat sheet |
| memo[r][c]=best length from r,c. | memo[r][c]=從 r,c 出發最佳長度。 | Cheat sheet |
| If cached, return immediately. | 若已快取就立即回傳。 | Cheat sheet |
| Base local best starts at one. | 本地基底 best 從 1 開始。 | Cheat sheet |
| Explore four neighbors. | 探索四個鄰居。 | Cheat sheet |
| Only go to larger value neighbor. | 只走向更大值鄰居。 | Cheat sheet |
| Update best=max(best,1+dfs(nei)). | 更新 best=max(best,1+dfs(nei))。 | Cheat sheet |
| Save best to memo. | 把 best 存回 memo。 | Cheat sheet |
| Global answer is max over all starts. | 全域答案是所有起點最大值。 | Cheat sheet |
| Example [[9,9,4],[6,6,8],[2,1,1]] -> 4. | 範例 [[9,9,4],[6,6,8],[2,1,1]] -> 4。 | Cheat sheet |
| Single cell -> 1. | 單格 -> 1。 | Cheat sheet |
| All equal -> 1. | 全相等 -> 1。 | Cheat sheet |
| Time O(m*n). | 時間 O(m*n)。 | Cheat sheet |
| Space O(m*n). | 空間 O(m*n)。 | Cheat sheet |
| Common bug: forgetting memo guard. | 常見錯誤：忘記 memo 快取判斷。 | Cheat sheet |
| Common bug: using non-strict comparison. | 常見錯誤：誤用非嚴格比較。 | Cheat sheet |
| Mention DAG intuition if interviewer asks why no cycles. | 若被問無環原因，可補充 DAG 直覺。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS + memo state and neighbor transition preserved.
- No hallucinated constraints: ✅ Strictly increasing, 4-direction movement semantics maintained.
- Language simplicity: ✅ Clear interview narrative for recursion and caching.
