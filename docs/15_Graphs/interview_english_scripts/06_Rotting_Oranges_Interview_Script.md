# 06 Rotting Oranges — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/06_Rotting_Oranges.md`

> Quick links: [Source Solution](../06_Rotting_Oranges.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate rotting oranges. | 我先重述 Rotting Oranges。 | Restatement |
| Grid cells can be empty, fresh, or rotten. | 格子可能是空、鮮橘子或爛橘子。 | Restatement |
| Every minute, rotten oranges infect adjacent fresh ones. | 每分鐘爛橘子會感染相鄰鮮橘子。 | Restatement |
| We need minimum minutes until all reachable fresh oranges rot. | 要求讓所有可達鮮橘子腐爛的最短分鐘數。 | Restatement |
| If some fresh orange can never rot, return minus one. | 若有鮮橘子永遠無法腐爛，回 -1。 | Restatement |
| I will use multi-source BFS by minute levels. | 我會用多源 BFS 逐分鐘擴散。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is movement only in four directions? | 傳染是否只限四方向？ | Clarify |
| If no fresh oranges initially, should answer be zero? | 一開始沒有鮮橘子是否回 0？ | Clarify |
| Can grid be empty? | grid 是否可能為空？ | Clarify |
| Are values strictly zero one two? | 值是否只會是 0、1、2？ | Clarify |
| Do we return only time, not final grid? | 是否只回時間，不回最終網格？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force repeatedly rescans grid each minute. | 暴力法每分鐘都重掃整張網格。 | Approach |
| It tracks newly rotten cells layer by layer manually. | 它要手動追蹤每輪新腐爛格。 | Approach |
| Repeated full scans are inefficient. | 重複全掃效率差。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Put all initial rotten oranges into queue first. | 先把初始爛橘子全部放入佇列。 | Approach |
| Count fresh oranges at initialization. | 初始化同時計算鮮橘子數。 | Approach |
| BFS level represents one minute of spread. | BFS 每一層代表一分鐘擴散。 | Approach |
| When a fresh neighbor is infected, decrement fresh count and push it. | 感染到鮮鄰居時，fresh-- 並入隊。 | Approach |
| At end, return minutes if fresh is zero else minus one. | 結束時 fresh 為 0 回 minutes，否則回 -1。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I scan the grid once to find rotten sources and fresh count. | 我先掃一遍網格找爛橘子來源與 fresh 計數。 | Coding |
| I push each rotten position into queue. | 每個爛橘子座標都推進佇列。 | Coding |
| If fresh count is zero, I return zero immediately. | 若 fresh 為 0，直接回 0。 | Coding |
| I set minutes to zero. | 我把 minutes 初始化為 0。 | Coding |
| While queue not empty and fresh still positive, process one BFS level. | 當 queue 非空且 fresh>0，處理一個 BFS 層。 | Coding |
| For each cell in this level, check four neighbors. | 對本層每格檢查四個鄰居。 | Coding |
| If neighbor is fresh, make it rotten, decrement fresh, and enqueue. | 鄰居是鮮橘子就腐爛它、fresh-- 並入隊。 | Coding |
| After this level, increment minutes by one. | 本層處理完 minutes 加一。 | Coding |
| After loop, if fresh is zero return minutes. | 迴圈後若 fresh 為 0，回 minutes。 | Coding |
| Otherwise return minus one. | 否則回傳 -1。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [[2,1,1],[1,1,0],[0,1,1]]. | 我手跑 [[2,1,1],[1,1,0],[0,1,1]]。 | Dry-run |
| Initial queue has one rotten at top-left and fresh count is six. | 初始 queue 有左上爛橘子，fresh=6。 | Dry-run |
| Minute one rots two adjacent fresh oranges. | 第 1 分鐘會感染兩個相鄰鮮橘子。 | Dry-run |
| Minute two continues from newly rotten oranges. | 第 2 分鐘由新爛橘子繼續擴散。 | Dry-run |
| Spread proceeds level by level until fresh becomes zero. | 擴散按層進行直到 fresh 歸零。 | Dry-run |
| Final minutes become four. | 最終分鐘數是 4。 | Dry-run |
| Output is four as expected. | 輸出為 4，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: no fresh oranges from start returns zero. | 案例一：起始無鮮橘子回 0。 | Edge test |
| Case two: fresh oranges isolated by empty cells return minus one. | 案例二：鮮橘子被空格隔離時回 -1。 | Edge test |
| Case three: one fresh next to one rotten returns one. | 案例三：一鮮一爛相鄰時回 1。 | Edge test |
| Case four: all fresh with no rotten source returns minus one. | 案例四：全鮮且無來源時回 -1。 | Edge test |
| Case five: single cell zero returns zero. | 案例五：單格 0 回 0。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(rows times cols). | 時間複雜度是 O(rows*cols)。 | Complexity |
| Space complexity is O(rows times cols) in worst case queue size. | 最壞佇列大小下空間是 O(rows*cols)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Initial scan of grid is O(mn). | 初始掃描網格是 O(mn)。 | Complexity |
| BFS visits each orange cell at most once when it becomes rotten. | BFS 中每顆橘子最多被處理一次。 | Complexity |
| Thus total runtime is O(mn). | 因此總時間是 O(mn)。 | Complexity |
| Queue can hold up to all cells in worst spread, so O(mn) space. | 最壞擴散下 queue 可達全部格子，空間 O(mn)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me model this as shortest time spread from many sources. | 我把這題建模成多源最短擴散時間。 | If stuck |
| Multi-source BFS is natural for simultaneous infection. | 同步感染最適合多源 BFS。 | If stuck |
| Queue starts with all rotten oranges. | 佇列起始放所有爛橘子。 | If stuck |
| Fresh count tells me if goal is complete. | fresh 計數可判斷是否完成目標。 | If stuck |
| One BFS level equals one minute. | 一個 BFS 層就是一分鐘。 | If stuck |
| Infecting a fresh neighbor must decrement fresh. | 感染鮮鄰居時必須 fresh--。 | If stuck |
| If fresh never reaches zero, answer is minus one. | 若 fresh 無法歸零，答案就是 -1。 | If stuck |
| Let me test no-fresh case first. | 我先測無鮮橘子案例。 | If stuck |
| That should return zero immediately. | 這應立即回傳 0。 | If stuck |
| Great, now minute accounting is clear. | 很好，現在分鐘計算很清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with multi-source BFS over time layers. | 我用多源 BFS 時間分層解題。 | Wrap-up |
| Initial rotten oranges are simultaneous start points. | 初始爛橘子是同步起點。 | Wrap-up |
| Fresh count tracks completion exactly. | fresh 計數可精確追蹤完成度。 | Wrap-up |
| Complexity is O(mn) time and O(mn) space. | 複雜度是 O(mn) 時間與 O(mn) 空間。 | Wrap-up |
| This is the standard contagion-wave interview pattern. | 這是擴散波型題目的標準面試模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: minimum minutes to rot all reachable fresh oranges. | 目標：最短分鐘數讓可達鮮橘子全腐爛。 | Cheat sheet |
| Use multi-source BFS. | 使用多源 BFS。 | Cheat sheet |
| Queue starts with all rotten cells. | queue 起始放所有爛格。 | Cheat sheet |
| Count fresh oranges initially. | 初始化統計 fresh。 | Cheat sheet |
| If fresh is zero, return zero. | 若 fresh=0，回 0。 | Cheat sheet |
| Process BFS level by level. | 逐層處理 BFS。 | Cheat sheet |
| One level equals one minute. | 一層等於一分鐘。 | Cheat sheet |
| For each rotten cell, check four neighbors. | 每個爛格檢查四鄰居。 | Cheat sheet |
| If neighbor fresh, set to rotten. | 鄰居是鮮的就改成爛。 | Cheat sheet |
| Decrement fresh and enqueue. | fresh-- 並入隊。 | Cheat sheet |
| After level, minutes++. | 每層結束 minutes++。 | Cheat sheet |
| Stop when queue empty or fresh zero. | queue 空或 fresh=0 時停止。 | Cheat sheet |
| If fresh zero, return minutes. | fresh 為 0 回 minutes。 | Cheat sheet |
| Else return minus one. | 否則回 -1。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Space O(mn). | 空間 O(mn)。 | Cheat sheet |
| Common bug: forgetting fresh decrement. | 常見錯誤：忘記遞減 fresh。 | Cheat sheet |
| Common bug: wrong minute increment placement. | 常見錯誤：minutes++ 位置錯。 | Cheat sheet |
| Test isolated fresh orange case. | 測隔離鮮橘子案例。 | Cheat sheet |
| Test no-fresh-at-start case. | 測起始無鮮橘子案例。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Multi-source BFS layer expansion preserved.
- No hallucinated constraints: ✅ Return-0 and return--1 conditions kept.
- Language simplicity: ✅ Short, clear interview flow lines.
