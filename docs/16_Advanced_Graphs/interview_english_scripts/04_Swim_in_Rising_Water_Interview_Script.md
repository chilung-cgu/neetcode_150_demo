# 04 Swim in Rising Water — Interview English Script (C++)

> Source aligned with: `docs/16_Advanced_Graphs/04_Swim_in_Rising_Water.md`

> Quick links: [Source Solution](../04_Swim_in_Rising_Water.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate swim in rising water. | 我先重述 Swim in Rising Water。 | Restatement |
| Grid value is elevation at each cell. | 每個格子的數值是海拔高度。 | Restatement |
| At time t, we can enter cells with height at most t. | 在時間 t 時，只能進入高度 <=t 的格子。 | Restatement |
| We move four directions from top-left to bottom-right. | 我們四方向移動，從左上到右下。 | Restatement |
| We need minimum t that makes this path possible. | 要找讓路徑可行的最小 t。 | Restatement |
| I will use Dijkstra on minimax path cost. | 我會用 Dijkstra 解 minimax 路徑成本。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is grid always square n by n? | grid 是否一定是 n×n 正方形？ | Clarify |
| Is movement limited to four directions? | 移動是否只限四方向？ | Clarify |
| Are heights unique permutation from zero to n squared minus one? | 高度是否是 0 到 n²-1 的排列？ | Clarify |
| Should output be minimum time integer only? | 是否只回最小時間整數？ | Clarify |
| Is O(n squared log n) acceptable here? | O(n²logn) 在此題是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force DFS over all paths is exponential. | 對所有路徑做 DFS 暴力是指數級。 | Approach |
| Binary search plus reachability check is possible but still repeated scans. | 二分答案加可達檢查可行，但會重複掃描。 | Approach |
| Dijkstra gives direct minimax optimization elegantly. | Dijkstra 可直接優雅地做 minimax 最佳化。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Define path cost as maximum elevation seen on that path. | 定義路徑成本為路上最大海拔。 | Approach |
| We minimize this maximum cost to destination. | 我們要把這個最大值最小化。 | Approach |
| Min-heap stores state maxCostSoFar and position. | 最小堆狀態存 maxCostSoFar 與座標。 | Approach |
| Transition cost to neighbor is max(currentCost, neighborHeight). | 轉移到鄰居的成本是 max(目前成本,鄰居高度)。 | Approach |
| First time destination is popped gives optimal answer. | 目的地首次出堆即最優答案。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize min-heap with state grid zero zero and position zero zero. | 我把初始狀態 (grid[0][0],0,0) 放入最小堆。 | Coding |
| I keep visited matrix to avoid reprocessing cells. | 我用 visited 矩陣避免重複處理。 | Coding |
| While heap not empty, pop state with smallest current max cost. | heap 非空時彈出目前最大成本最小的狀態。 | Coding |
| If cell is destination, return its cost. | 若該格是終點，直接回傳成本。 | Coding |
| For each valid unvisited neighbor, mark visited. | 對每個有效且未訪鄰居，先標記 visited。 | Coding |
| Compute newCost as max(currentCost, grid neighbor). | 計算 newCost=max(currentCost,鄰居高度)。 | Coding |
| Push new state into heap. | 把新狀態推入 heap。 | Coding |
| Continue exploration by cost order. | 按成本順序持續探索。 | Coding |
| Return minus one only as safety fallback. | -1 僅作理論保底。 | Coding |
| This is Dijkstra with modified edge relaxation rule. | 這是放鬆規則改寫版 Dijkstra。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run grid [[0,2],[1,3]]. | 我手跑 grid=[[0,2],[1,3]]。 | Dry-run |
| Start state is cost zero at cell zero zero. | 起始狀態是成本 0 在 (0,0)。 | Dry-run |
| Neighbor one zero gives new cost one. | 鄰居 (1,0) 的 newCost 是 1。 | Dry-run |
| Neighbor zero one gives new cost two. | 鄰居 (0,1) 的 newCost 是 2。 | Dry-run |
| Heap pops cost one first, then reaches destination with max three. | heap 先彈成本 1，接著到終點成本成為 3。 | Dry-run |
| Destination popped with cost three. | 終點以成本 3 出堆。 | Dry-run |
| Answer is three. | 答案是 3。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n one grid returns its single value. | 案例一：n=1 時回該唯一值。 | Edge test |
| Case two: monotonic increasing path along boundary. | 案例二：沿邊界單調上升路徑。 | Edge test |
| Case three: local low cells with one unavoidable high barrier. | 案例三：低地形但有必經高障礙。 | Edge test |
| Case four: multiple routes where shortest steps is not best minimax cost. | 案例四：步數短不等於 minimax 最佳路徑。 | Edge test |
| Case five: winding path with lower maximum elevation. | 案例五：繞路但最大海拔更低。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n squared log n). | 時間複雜度是 O(n²logn)。 | Complexity |
| Space complexity is O(n squared). | 空間複雜度是 O(n²)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| There are n squared grid states. | 網格共有 n² 個狀態。 | Complexity |
| Each state may enter heap once in visited-on-push variant. | 在 push 即標記版本下，每狀態最多入堆一次。 | Complexity |
| Heap operations cost logarithmic factor, giving O(n squared log n). | 堆操作有對數因子，總時間 O(n²logn)。 | Complexity |
| Visited matrix and heap storage are O(n squared). | visited 矩陣與堆儲存量為 O(n²)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on minimax definition first. | 我先聚焦 minimax 定義。 | If stuck |
| Path cost is maximum elevation on path, not sum. | 路徑成本是最大海拔，不是總和。 | If stuck |
| Transition uses max current and neighbor height. | 轉移用 max(目前,鄰居高度)。 | If stuck |
| Dijkstra still works with this monotone cost. | 在此單調成本下 Dijkstra 仍成立。 | If stuck |
| Min-heap explores currently best possible max cost first. | 最小堆會先探索目前最有利的最大成本。 | If stuck |
| Destination first pop is optimal answer. | 終點首次出堆即最優。 | If stuck |
| Let me test quickly with two by two sample. | 我快速測 2x2 範例。 | If stuck |
| Expected answer there is three. | 該例預期答案是 3。 | If stuck |
| This confirms minimax relaxation rule. | 這可確認 minimax 放鬆規則。 | If stuck |
| Great, implementation path is clear. | 很好，實作路徑已清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with modified Dijkstra on grid states. | 我用修改版 Dijkstra 處理網格狀態解題。 | Wrap-up |
| Cost metric is path maximum elevation. | 成本度量是路徑最大海拔。 | Wrap-up |
| Heap order guarantees first destination pop is minimum feasible time. | 堆序可保證終點首次出堆即最小可行時間。 | Wrap-up |
| Complexity is O(n squared log n) time and O(n squared) space. | 複雜度是 O(n²logn) 時間與 O(n²) 空間。 | Wrap-up |
| This is a classic minimax shortest-path pattern. | 這是經典 minimax 最短路模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: minimum time to reach bottom-right. | 目標：最短時間到右下角。 | Cheat sheet |
| Time equals max elevation along chosen path. | 時間等於路徑上最大海拔。 | Cheat sheet |
| This is minimax path problem. | 這是 minimax 路徑問題。 | Cheat sheet |
| Use Dijkstra with custom cost update. | 用自訂成本更新的 Dijkstra。 | Cheat sheet |
| Heap state: (cost,r,c). | heap 狀態：(cost,r,c)。 | Cheat sheet |
| Start cost is grid[0][0]. | 起始成本是 grid[0][0]。 | Cheat sheet |
| Pop smallest cost state. | 彈出最小成本狀態。 | Cheat sheet |
| If destination popped, return cost. | 終點出堆就回成本。 | Cheat sheet |
| For each neighbor compute newCost=max(cost,height). | 鄰居新成本 newCost=max(cost,height)。 | Cheat sheet |
| Push unvisited neighbor with newCost. | 未訪鄰居以 newCost 入堆。 | Cheat sheet |
| Repeat until destination reached. | 重複直到到達終點。 | Cheat sheet |
| n=1 returns grid[0][0]. | n=1 回 grid[0][0]。 | Cheat sheet |
| Time O(n²logn). | 時間 O(n²logn)。 | Cheat sheet |
| Space O(n²). | 空間 O(n²)。 | Cheat sheet |
| Common bug: summing heights instead of max. | 常見錯誤：把高度相加而非取 max。 | Cheat sheet |
| Common bug: wrong visited timing. | 常見錯誤：visited 標記時機錯。 | Cheat sheet |
| Binary search + BFS is alternative. | 二分 + BFS 是替代方案。 | Cheat sheet |
| Explain why minimax remains monotone. | 說明 minimax 為何保持單調。 | Cheat sheet |
| Keep four-direction movement only. | 移動僅限四方向。 | Cheat sheet |
| Verify with small 2x2 sample. | 用 2x2 小樣例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Dijkstra minimax transition `max(curr, neighbor)`.
- No hallucinated constraints: ✅ grid movement and output semantics preserved.
- Language simplicity: ✅ concise interview speaking lines.
