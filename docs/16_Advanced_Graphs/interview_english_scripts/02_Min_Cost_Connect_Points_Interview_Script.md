# 02 Min Cost to Connect All Points — Interview English Script (C++)

> Source aligned with: `docs/16_Advanced_Graphs/02_Min_Cost_Connect_Points.md`

> Quick links: [Source Solution](../02_Min_Cost_Connect_Points.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate min cost to connect all points. | 我先重述 Min Cost to Connect All Points。 | Restatement |
| We have points on two-dimensional plane. | 題目給二維平面上的多個點。 | Restatement |
| Cost between two points is Manhattan distance. | 兩點連線成本是曼哈頓距離。 | Restatement |
| We need connect all points with minimum total cost. | 要以最小總成本把所有點連通。 | Restatement |
| This is minimum spanning tree problem on complete graph. | 這是完整圖上的最小生成樹問題。 | Restatement |
| I will use Prim algorithm with min-heap. | 我會用 Prim 演算法加最小堆。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is points length up to around one thousand? | points 長度是否約到一千？ | Clarify |
| Is Manhattan distance exactly abs dx plus abs dy? | 曼哈頓距離是否是 |dx|+|dy|？ | Clarify |
| We only need total cost, not actual edges list, right? | 是否只需總成本，不需回邊清單？ | Clarify |
| Can coordinates be negative values? | 座標值是否可能為負？ | Clarify |
| Is O(n squared log n) acceptable for this constraint? | 在此限制下 O(n²logn) 是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Generate all edges of complete graph and run Kruskal. | 列舉完整圖所有邊再跑 Kruskal。 | Approach |
| Edge count is O(n squared), sorting adds heavy cost. | 邊數 O(n²)，排序成本也高。 | Approach |
| Prim avoids explicit full edge list creation. | Prim 可避免顯式建立全部邊清單。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Start from any point, usually index zero. | 從任一點起跑，通常 index 0。 | Approach |
| Maintain visited set for points already in MST. | 維護已納入 MST 的 visited 集合。 | Approach |
| Min-heap stores candidate edges as cost and destination index. | 最小堆存候選邊：成本與目的節點索引。 | Approach |
| Each step picks cheapest edge reaching unvisited point. | 每一步選最便宜可達未訪點的邊。 | Approach |
| Repeat until all points are included, summing costs. | 重複直到全點納入並累加成本。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize min-heap with pair zero and node zero. | 我先把 (0,0) 放入最小堆。 | Coding |
| I prepare visited boolean array sized n. | 我準備大小 n 的 visited 布林陣列。 | Coding |
| I keep totalCost and connectedCount as zero. | 我維護 totalCost 與 connectedCount 初值 0。 | Coding |
| While connectedCount is less than n, pop heap top. | 當 connectedCount<n 時，彈出堆頂。 | Coding |
| If node already visited, skip this entry. | 若節點已訪問，就略過該項。 | Coding |
| Otherwise mark visited and add cost to totalCost. | 否則標記 visited 並把成本加到 totalCost。 | Coding |
| Increase connectedCount by one. | connectedCount 加一。 | Coding |
| For every unvisited point v, compute Manhattan distance from current node. | 對每個未訪點 v，計算到當前點的曼哈頓距離。 | Coding |
| Push distance and v into heap as candidate edge. | 把距離與 v 作為候選邊推入堆。 | Coding |
| After loop ends, return totalCost. | 迴圈結束後回傳 totalCost。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run points [0,0],[2,2],[3,10],[5,2],[7,0]. | 我手跑 points [0,0],[2,2],[3,10],[5,2],[7,0]。 | Dry-run |
| Start with point zero at cost zero. | 從點 0 成本 0 開始。 | Dry-run |
| Cheapest next edge connects to point one with cost four. | 最便宜下一邊連到點 1，成本 4。 | Dry-run |
| Continue selecting minimum edge crossing visited cut. | 持續選跨越 visited 邊界的最小邊。 | Dry-run |
| Points join in order of cheapest available Manhattan links. | 各點依最便宜曼哈頓連結順序加入。 | Dry-run |
| Total accumulated MST cost becomes twenty. | 最終 MST 累加成本為 20。 | Dry-run |
| Output is twenty. | 輸出是 20。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single point returns zero. | 案例一：單一點回 0。 | Edge test |
| Case two: two points returns their Manhattan distance. | 案例二：兩點回其曼哈頓距離。 | Edge test |
| Case three: duplicate coordinates produce zero-cost edges. | 案例三：重複座標會出現零成本邊。 | Edge test |
| Case four: points with negative coordinates. | 案例四：含負座標點集。 | Edge test |
| Case five: collinear points with multiple equal choices. | 案例五：共線且有多個等價選擇。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n squared log n). | 時間複雜度是 O(n²logn)。 | Complexity |
| Space complexity is O(n squared) in heap worst case. | 空間最壞是 O(n²)（堆中候選邊）。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For each accepted node, we may push distances to many unvisited nodes. | 每接納一個節點，可能推入多個未訪點距離。 | Complexity |
| Total pushed candidate edges can be O(n squared). | 總候選邊推入量可達 O(n²)。 | Complexity |
| Heap operations add logarithmic factor, giving O(n squared log n). | 堆操作帶對數因子，總時間 O(n²logn)。 | Complexity |
| Visited array is O(n), heap dominates memory up to O(n squared). | visited 為 O(n)，堆最壞主導為 O(n²)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me reframe this as MST problem. | 我先把它重述成 MST 問題。 | If stuck |
| We never need cycles in MST. | MST 中不需要任何環。 | If stuck |
| Prim grows one connected tree gradually. | Prim 會逐步長出一棵連通樹。 | If stuck |
| At each step choose cheapest edge to unvisited point. | 每步選到未訪點的最便宜邊。 | If stuck |
| Min-heap helps retrieve that edge quickly. | 最小堆可快速取出該邊。 | If stuck |
| Manhattan distance is computed on demand. | 曼哈頓距離可按需計算。 | If stuck |
| Let me test quickly with two-point case. | 我快速驗證兩點案例。 | If stuck |
| Result should equal direct distance. | 結果應等於直接距離。 | If stuck |
| This confirms cost accumulation logic. | 這可確認成本累加邏輯。 | If stuck |
| Great, now implementation is straightforward. | 很好，現在實作很直觀。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with Prim minimum spanning tree. | 我用 Prim 最小生成樹解題。 | Wrap-up |
| Visited set tracks nodes already connected. | visited 集合追蹤已連入節點。 | Wrap-up |
| Heap always picks cheapest edge into unvisited area. | 堆會持續挑最便宜跨界邊。 | Wrap-up |
| Complexity is O(n squared log n) time. | 時間複雜度是 O(n²logn)。 | Wrap-up |
| This is a standard MST approach for dense complete graph costs. | 這是稠密完整圖成本題的標準 MST 作法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: minimum total cost to connect all points. | 目標：最小總成本連通所有點。 | Cheat sheet |
| Cost is Manhattan distance. | 成本是曼哈頓距離。 | Cheat sheet |
| Model as MST problem. | 建模成 MST 問題。 | Cheat sheet |
| Use Prim with min-heap. | 使用 Prim + 最小堆。 | Cheat sheet |
| Start with node zero cost zero. | 從節點 0、成本 0 起跑。 | Cheat sheet |
| Maintain visited nodes. | 維護 visited 節點。 | Cheat sheet |
| Pop cheapest candidate edge. | 彈出最便宜候選邊。 | Cheat sheet |
| Skip if destination already visited. | 目的節點已訪則略過。 | Cheat sheet |
| Otherwise add cost and mark visited. | 否則加成本並標記 visited。 | Cheat sheet |
| Push distances to all unvisited nodes. | 推入到所有未訪點距離。 | Cheat sheet |
| Repeat until all n nodes connected. | 重複直到 n 點全連通。 | Cheat sheet |
| Return totalCost. | 回傳 totalCost。 | Cheat sheet |
| n=1 returns 0. | n=1 回 0。 | Cheat sheet |
| Two points return direct Manhattan cost. | 兩點回直接曼哈頓成本。 | Cheat sheet |
| Time O(n²logn). | 時間 O(n²logn)。 | Cheat sheet |
| Heap memory can reach O(n²). | 堆記憶體最壞 O(n²)。 | Cheat sheet |
| Common bug: forgetting visited skip. | 常見錯誤：忘記 visited skip。 | Cheat sheet |
| Common bug: wrong Manhattan formula. | 常見錯誤：曼哈頓公式寫錯。 | Cheat sheet |
| Kruskal is alternative but needs full edge list. | Kruskal 可行但需完整邊清單。 | Cheat sheet |
| Explain cut property briefly if asked. | 若被追問可簡述割邊性質。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Prim min-heap MST approach preserved.
- No hallucinated constraints: ✅ Manhattan-cost and full-connect target maintained.
- Language simplicity: ✅ concise interview speaking style.
