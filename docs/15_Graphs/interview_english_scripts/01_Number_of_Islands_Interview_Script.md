# 01 Number of Islands — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/01_Number_of_Islands.md`

> Quick links: [Source Solution](../01_Number_of_Islands.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate number of islands. | 我先重述 Number of Islands。 | Restatement |
| We have a grid of ones and zeros. | 題目給由 1 和 0 組成的網格。 | Restatement |
| One means land and zero means water. | 1 代表陸地，0 代表水域。 | Restatement |
| An island is connected land in four directions. | 島嶼是四方向連通的陸地群。 | Restatement |
| We need to count how many separate islands exist. | 我們要計算獨立島嶼有幾個。 | Restatement |
| I will use DFS flood fill from each unvisited land cell. | 我會從每塊未訪問陸地做 DFS 淹沒。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is grid guaranteed non-empty? | grid 是否保證非空？ | Clarify |
| Are diagonals excluded from connectivity? | 對角線是否不算連通？ | Clarify |
| Can I modify grid in place for visited marking? | 可以原地修改 grid 做 visited 標記嗎？ | Clarify |
| Are cells only characters zero and one? | cell 是否只會是字元 0 與 1？ | Clarify |
| Should I return integer count only? | 是否只回傳整數計數？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A naive way repeatedly searches connected lands without marking efficiently. | 天真作法會反覆搜尋連通陸地而不夠高效。 | Approach |
| That causes repeated work on the same island cells. | 這會對同一座島嶼重複做工。 | Approach |
| We need one-pass visitation over each cell. | 我們需要讓每格最多訪問一次。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Scan every grid cell once. | 全表每個格子掃描一次。 | Approach |
| When I see land one, I found a new island and increment count. | 遇到陸地 1 就代表找到新島，計數加一。 | Approach |
| Then DFS turns this whole island to zero to mark visited. | 接著 DFS 把整座島改成 0 表示已訪問。 | Approach |
| DFS expands to up down left and right neighbors. | DFS 擴展到上下左右鄰居。 | Approach |
| Final count is the number of DFS starts. | 最終計數就是 DFS 啟動次數。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I read rows and cols from grid size. | 我先取得 rows 與 cols。 | Coding |
| I initialize islandCount to zero. | 我把 islandCount 初始化為 0。 | Coding |
| I loop r from zero to rows minus one. | 我讓 r 從 0 走到 rows-1。 | Coding |
| Inside, I loop c from zero to cols minus one. | 內層讓 c 從 0 走到 cols-1。 | Coding |
| If grid[r][c] is one, islandCount plus plus. | 若 grid[r][c] 是 1，islandCount++。 | Coding |
| I call dfs on this cell. | 我對這格呼叫 dfs。 | Coding |
| In dfs, boundary or water returns immediately. | dfs 中遇邊界或水就立刻返回。 | Coding |
| Otherwise set current land to zero. | 否則把當前陸地改成 0。 | Coding |
| Then recurse to four directions. | 再遞迴四個方向。 | Coding |
| After loops, return islandCount. | 迴圈結束後回傳 islandCount。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the sample with three islands. | 我手跑那個答案為 3 的範例。 | Dry-run |
| Start scanning from top left. | 從左上角開始掃描。 | Dry-run |
| First block of ones triggers DFS and sinks that component. | 第一塊 1 觸發 DFS，整塊被淹沒。 | Dry-run |
| Later at middle isolated one, count increments again. | 後來掃到中間孤立 1，計數再加一。 | Dry-run |
| Finally bottom-right pair of ones forms the third island. | 最後右下角相連 1 形成第三座島。 | Dry-run |
| DFS marks each discovered island to zero. | DFS 會把發現的島全部標成 0。 | Dry-run |
| Final island count is three. | 最終島嶼數是 3。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: all water grid returns zero. | 案例一：全是水時回 0。 | Edge test |
| Case two: all land grid returns one. | 案例二：全是陸地時回 1。 | Edge test |
| Case three: single cell one returns one. | 案例三：單格 1 回 1。 | Edge test |
| Case four: single cell zero returns zero. | 案例四：單格 0 回 0。 | Edge test |
| Case five: diagonal ones only are separate islands. | 案例五：僅對角相鄰的 1 要分開計。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(rows times cols). | 時間複雜度是 O(rows*cols)。 | Complexity |
| Space complexity is O(rows times cols) worst case from recursion stack. | 空間最壞是 O(rows*cols) 來自遞迴堆疊。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Every cell is visited at most once during scan plus DFS. | 掃描加 DFS 下每格最多被訪問一次。 | Complexity |
| So total runtime is linear in grid size. | 所以總時間對網格大小是線性。 | Complexity |
| Extra memory is from recursion depth on connected land. | 額外記憶體來自連通陸地的遞迴深度。 | Complexity |
| In worst case full land, stack can reach rows times cols. | 最壞全陸地時，堆疊可達 rows*cols。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me treat each land cell as a graph node. | 我把每個陸地格當成圖節點。 | If stuck |
| Islands are just connected components. | 島嶼其實就是連通分量。 | If stuck |
| I increment count only when I start a new DFS. | 我只在啟動新 DFS 時加計數。 | If stuck |
| DFS must mark visited immediately to avoid repeats. | DFS 要立刻標記 visited 避免重複。 | If stuck |
| In-place marking can change one to zero. | 原地標記可把 1 改成 0。 | If stuck |
| Boundary checks prevent out-of-range recursion. | 邊界檢查可避免遞迴越界。 | If stuck |
| Let me verify with a one-cell land grid. | 我先用單格陸地驗證。 | If stuck |
| That should return one island. | 那應該回傳 1 座島。 | If stuck |
| Diagonal neighbors do not connect here. | 這題對角鄰居不算連通。 | If stuck |
| Great, now logic is stable. | 很好，現在邏輯穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with grid scan plus DFS flood fill. | 我用全表掃描加 DFS 淹沒法解題。 | Wrap-up |
| Each new land start means one new island. | 每次遇到新陸地起點代表一座新島。 | Wrap-up |
| DFS sinks that component to avoid double counting. | DFS 淹沒整個分量避免重複計算。 | Wrap-up |
| Complexity is O(mn) time and O(mn) worst-case stack space. | 複雜度是 O(mn) 時間、O(mn) 最壞堆疊空間。 | Wrap-up |
| This is the standard connected-component pattern on grids. | 這是網格連通分量的標準解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: count islands in a binary grid. | 目標：計算二元網格中的島嶼數。 | Cheat sheet |
| One is land, zero is water. | 1 是陸地，0 是水。 | Cheat sheet |
| Island uses four-direction connectivity. | 島嶼用四方向連通定義。 | Cheat sheet |
| Scan every cell once. | 每格掃描一次。 | Cheat sheet |
| If cell is one, count plus plus. | 若是 1，計數加一。 | Cheat sheet |
| Start DFS from that cell. | 從該格啟動 DFS。 | Cheat sheet |
| DFS base: out of bounds return. | DFS 基底：越界就返回。 | Cheat sheet |
| DFS base: water return. | DFS 基底：水就返回。 | Cheat sheet |
| Mark current land as zero. | 把當前陸地標成 0。 | Cheat sheet |
| Recurse up down left right. | 遞迴上下左右。 | Cheat sheet |
| Count equals DFS start times. | 計數等於 DFS 啟動次數。 | Cheat sheet |
| All water returns zero. | 全水回 0。 | Cheat sheet |
| All land returns one. | 全陸地回 1。 | Cheat sheet |
| Diagonal does not connect. | 對角不連通。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Stack worst O(mn). | 堆疊最壞 O(mn)。 | Cheat sheet |
| In-place mark saves visited matrix. | 原地標記可省 visited 陣列。 | Cheat sheet |
| BFS variant is also valid. | BFS 版本也可行。 | Cheat sheet |
| Avoid recounting sunk land. | 避免對已淹沒陸地重算。 | Cheat sheet |
| Return final island count. | 回傳最終島嶼數。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS/BFS connected-component counting with in-place marking.
- No hallucinated constraints: ✅ Four-direction rule and input semantics preserved.
- Language simplicity: ✅ Short, interview-friendly spoken lines.
