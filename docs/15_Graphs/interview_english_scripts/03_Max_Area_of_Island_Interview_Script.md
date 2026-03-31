# 03 Max Area of Island — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/03_Max_Area_of_Island.md`

> Quick links: [Source Solution](../03_Max_Area_of_Island.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate max area of island. | 我先重述 Max Area of Island。 | Restatement |
| We have a binary grid with land one and water zero. | 題目給二元網格，1 是陸地、0 是水。 | Restatement |
| An island is four-direction connected land. | 島嶼定義為四方向連通陸地。 | Restatement |
| We need the maximum area among all islands. | 要找所有島嶼中的最大面積。 | Restatement |
| If there is no land, answer is zero. | 若完全沒有陸地，答案是 0。 | Restatement |
| I will use DFS to compute each component area. | 我會用 DFS 計算每個連通分量面積。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I modify the grid in place for visited marking? | 可以原地修改 grid 做 visited 標記嗎？ | Clarify |
| Are diagonals excluded from island connectivity? | 對角是否不算連通？ | Clarify |
| Is grid guaranteed non-empty? | grid 是否保證非空？ | Clarify |
| Are cell values strictly integers zero and one? | cell 是否只會是整數 0 與 1？ | Clarify |
| Should I return area only, not coordinates? | 是否只回面積，不需回座標？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Recomputing area from many cells without proper marking repeats work. | 若未妥善標記，從多點重算面積會重複工作。 | Approach |
| That leads to much higher cost than needed. | 這會導致不必要的高成本。 | Approach |
| We should ensure each land cell is consumed once. | 我們應確保每塊陸地只被處理一次。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Scan all cells in the grid. | 掃描網格的所有格子。 | Approach |
| When a land cell appears, run DFS to get this island area. | 遇到陸地就做 DFS 取得該島面積。 | Approach |
| DFS returns one plus areas of four neighbors. | DFS 回傳 1 加上四個鄰居面積。 | Approach |
| Mark visited land as zero to avoid recounting. | 把已訪問陸地標成 0 避免重算。 | Approach |
| Track global maximum area over all DFS results. | 對所有 DFS 結果維護全域最大值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize maxArea as zero. | 我先把 maxArea 初始化為 0。 | Coding |
| I loop through every row and column cell. | 我遍歷每一列每一行格子。 | Coding |
| If current cell is land one, I call dfs. | 若當前格為 1，我呼叫 dfs。 | Coding |
| I update maxArea with max of itself and returned area. | 我用回傳面積更新 maxArea。 | Coding |
| In dfs, out of bounds or water returns zero. | dfs 中越界或水直接回 0。 | Coding |
| Otherwise mark current cell to zero immediately. | 否則立即把當前格標成 0。 | Coding |
| Then compute area as one plus four recursive calls. | 面積計為 1 加四方向遞迴。 | Coding |
| Return computed area to caller. | 把計算面積回傳給呼叫端。 | Coding |
| Continue scan until all cells are processed. | 持續掃描直到所有格子處理完。 | Coding |
| Return maxArea at the end. | 最後回傳 maxArea。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the sample where answer is six. | 我手跑答案為 6 的範例。 | Dry-run |
| Scan finds a land component in the middle-right region. | 掃描會找到中右區的一個陸地分量。 | Dry-run |
| DFS expands through connected ones and counts cells. | DFS 會沿連通 1 擴展並累計格數。 | Dry-run |
| That component area becomes six. | 那個分量面積會得到 6。 | Dry-run |
| Other components are smaller than six. | 其他分量都小於 6。 | Dry-run |
| maxArea stays six after full scan. | 全掃描後 maxArea 維持 6。 | Dry-run |
| Final output is six. | 最終輸出為 6。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: all zeros returns zero. | 案例一：全 0 回 0。 | Edge test |
| Case two: one single land cell returns one. | 案例二：單一陸地格回 1。 | Edge test |
| Case three: all ones grid returns rows times cols. | 案例三：全 1 網格回 rows*cols。 | Edge test |
| Case four: multiple islands with same area. | 案例四：多座島且面積相同。 | Edge test |
| Case five: diagonal-only touching lands stay separate. | 案例五：僅對角接觸的陸地仍分開。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(rows times cols). | 時間複雜度是 O(rows*cols)。 | Complexity |
| Space complexity is O(rows times cols) worst case recursion depth. | 空間最壞是 O(rows*cols) 的遞迴深度。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each cell is visited at most once because visited land is turned to zero. | 每格最多訪問一次，因為訪問後會改成 0。 | Complexity |
| So total operations are linear in number of cells. | 所以總操作量對格子數是線性。 | Complexity |
| Recursive DFS stack is the main extra memory. | 遞迴 DFS 堆疊是主要額外記憶體。 | Complexity |
| In worst case one huge island, stack can reach rows times cols. | 最壞單一大島時，堆疊可達 rows*cols。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me align this with number of islands pattern. | 我先把它對齊 Number of Islands 模式。 | If stuck |
| Difference is we return largest component size. | 差別是這題回傳最大分量大小。 | If stuck |
| DFS should return area, not just mark visited. | DFS 要回面積，不只是標記。 | If stuck |
| Base case returns zero for water or boundary. | 基底情況對水或越界回 0。 | If stuck |
| Current land contributes one area unit. | 當前陸地貢獻 1 單位面積。 | If stuck |
| Add four recursive neighbor areas. | 再加上四方向遞迴面積。 | If stuck |
| Mark current cell before recursive calls. | 在遞迴前先標記當前格。 | If stuck |
| That prevents infinite revisits. | 這可避免無限重訪。 | If stuck |
| Then update global max after each DFS. | 每次 DFS 後更新全域最大值。 | If stuck |
| Great, now implementation is straightforward. | 很好，現在實作很直接。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it by DFS area computation on each island. | 我用每座島 DFS 面積計算解題。 | Wrap-up |
| In-place marking ensures each land is counted once. | 原地標記確保每塊陸地只算一次。 | Wrap-up |
| We keep the largest returned component area. | 持續保留最大分量面積。 | Wrap-up |
| Complexity is O(mn) time and O(mn) worst-case stack space. | 複雜度是 O(mn) 時間與 O(mn) 最壞堆疊空間。 | Wrap-up |
| This is the standard flood-fill maximum-component template. | 這是標準 flood-fill 最大分量模板。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: largest area among all islands. | 目標：所有島嶼中的最大面積。 | Cheat sheet |
| One is land, zero is water. | 1 是陸地，0 是水。 | Cheat sheet |
| Four-direction connectivity only. | 僅四方向連通。 | Cheat sheet |
| Scan every cell in grid. | 掃描每個格子。 | Cheat sheet |
| On land, run DFS. | 遇陸地就跑 DFS。 | Cheat sheet |
| DFS base out of bounds returns zero. | DFS 越界回 0。 | Cheat sheet |
| DFS base water returns zero. | DFS 遇水回 0。 | Cheat sheet |
| Mark land as zero when visited. | 訪問時把陸地改 0。 | Cheat sheet |
| Area = one plus four DFS calls. | 面積=1+四向 DFS。 | Cheat sheet |
| Update maxArea after each DFS. | 每次 DFS 後更新 maxArea。 | Cheat sheet |
| Return maxArea. | 回傳 maxArea。 | Cheat sheet |
| All water means answer zero. | 全水答案為 0。 | Cheat sheet |
| Single land means answer one. | 單陸地答案為 1。 | Cheat sheet |
| Full land means answer rows*cols. | 全陸地答案 rows*cols。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Stack worst O(mn). | 堆疊最壞 O(mn)。 | Cheat sheet |
| BFS variant also works. | BFS 版本也可行。 | Cheat sheet |
| Avoid diagonal connections. | 不要把對角當連通。 | Cheat sheet |
| Mark before recursive expand. | 先標記再遞迴擴展。 | Cheat sheet |
| Keep explanation centered on components. | 說明重點放在連通分量。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS recursive area sum with in-place sink.
- No hallucinated constraints: ✅ Four-direction and zero-land behavior preserved.
- Language simplicity: ✅ Concise interview-safe steps.
