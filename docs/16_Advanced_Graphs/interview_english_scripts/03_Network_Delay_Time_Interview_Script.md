# 03 Network Delay Time — Interview English Script (C++)

> Source aligned with: `docs/16_Advanced_Graphs/03_Network_Delay_Time.md`

> Quick links: [Source Solution](../03_Network_Delay_Time.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate network delay time. | 我先重述 Network Delay Time。 | Restatement |
| We have directed weighted edges times u v w. | 題目給有向加權邊 times=(u,v,w)。 | Restatement |
| Signal starts from node k. | 訊號從節點 k 發出。 | Restatement |
| We need time when all nodes have received signal. | 要找所有節點都收到訊號的時間。 | Restatement |
| This is maximum shortest-path distance from k to every node. | 這是從 k 到各點最短路中的最大值。 | Restatement |
| I will use Dijkstra since all weights are non-negative. | 我會用 Dijkstra，因為邊權皆非負。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are nodes labeled one to n? | 節點是否編號 1 到 n？ | Clarify |
| Is graph directed for each time edge? | 每條 time 邊是否為有向？ | Clarify |
| If some node unreachable, should return minus one? | 若有節點不可達是否回 -1？ | Clarify |
| Are edge weights always positive or non-negative? | 邊權是否皆正或至少非負？ | Clarify |
| Is O(E log V) expected? | 是否預期 O(ElogV) 解法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force from k using repeated relaxations can use Bellman-Ford. | 暴力放鬆可用 Bellman-Ford 從 k 出發。 | Approach |
| It works but is slower at O(VE). | 可行但較慢，時間 O(VE)。 | Approach |
| Dijkstra is better for non-negative weights. | 非負權圖用 Dijkstra 更合適。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build adjacency list from times. | 先由 times 建立鄰接表。 | Approach |
| Min-heap stores pair currentTime and node. | 最小堆存目前時間與節點。 | Approach |
| Pop smallest time state each step. | 每步彈出最小時間狀態。 | Approach |
| First time we settle a node gives its shortest time. | 節點首次定稿時間就是最短路。 | Approach |
| Track max settled time and visited count; if count less than n at end return minus one. | 追蹤最大定稿時間與訪問數；若訪問不足 n 則回 -1。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I build adjacency list u to list of v and w. | 我建立鄰接表 u -> [(v,w)]。 | Coding |
| I initialize min-heap with pair zero and source k. | 我把 (0,k) 放入最小堆。 | Coding |
| I prepare distance or visited array to mark finalized nodes. | 我準備 dist 或 visited 來標記定稿節點。 | Coding |
| While heap not empty, pop shortest-time entry. | heap 非空時彈出最短時間項。 | Coding |
| If node already finalized, skip it. | 節點若已定稿就略過。 | Coding |
| Finalize node time and update maxTime. | 定稿節點時間並更新 maxTime。 | Coding |
| For each outgoing edge, push newTime to neighbor into heap. | 對每條出邊把新時間推入鄰居。 | Coding |
| Continue until heap ends. | 持續直到 heap 結束。 | Coding |
| If finalized node count is n, return maxTime. | 若定稿節點數為 n，回 maxTime。 | Coding |
| Otherwise return minus one. | 否則回 -1。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run times [2,1,1],[2,3,1],[3,4,1], n four, k two. | 我手跑 times=[2,1,1],[2,3,1],[3,4,1]，n=4，k=2。 | Dry-run |
| Start heap has [0,2]. | 起始 heap 為 [0,2]。 | Dry-run |
| Pop node two at time zero. | 彈出節點 2，時間 0。 | Dry-run |
| Push node one time one and node three time one. | 推入節點 1 時間 1、節點 3 時間 1。 | Dry-run |
| Pop node one and settle time one. | 彈出節點 1，定稿時間 1。 | Dry-run |
| Pop node three and push node four time two. | 彈出節點 3，再推節點 4 時間 2。 | Dry-run |
| Pop node four at time two, all nodes reached so answer is two. | 彈出節點 4 時間 2，全部到達，答案是 2。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n one and k one returns zero. | 案例一：n=1 且 k=1 回 0。 | Edge test |
| Case two: disconnected graph leaves some node unreachable and returns minus one. | 案例二：圖不連通有不可達節點，回 -1。 | Edge test |
| Case three: multiple edges between same pair with different weights. | 案例三：同對節點有不同權重多條邊。 | Edge test |
| Case four: path with many hops but lower total time. | 案例四：多跳但總時間更小的路徑。 | Edge test |
| Case five: star graph centered at source. | 案例五：以來源為中心的星狀圖。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(E log E) or O(E log V). | 時間複雜度是 O(ElogE) 或 O(ElogV)。 | Complexity |
| Space complexity is O(V plus E). | 空間複雜度是 O(V+E)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Building adjacency list costs O(E). | 建鄰接表成本是 O(E)。 | Complexity |
| Heap push and pop operations dominate with logarithmic factor. | 堆的推彈操作帶來對數成本。 | Complexity |
| Total is O(E log V) in standard Dijkstra analysis. | 依標準分析總時間是 O(ElogV)。 | Complexity |
| Adjacency plus heap plus visited structures use O(V plus E) memory. | 鄰接表、堆與 visited 共用 O(V+E) 記憶體。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me convert this to single-source shortest path. | 我先把題目轉成單源最短路。 | If stuck |
| Final answer is max shortest distance among all nodes. | 最終答案是所有最短距離的最大值。 | If stuck |
| Non-negative weights suggest Dijkstra directly. | 非負權重可直接用 Dijkstra。 | If stuck |
| Min-heap always expands currently closest unsettled node. | 最小堆會先展開目前最近未定稿節點。 | If stuck |
| First settle time is optimal for that node. | 節點首次定稿時間即最優。 | If stuck |
| Unreachable nodes cause result minus one. | 若有不可達節點，結果為 -1。 | If stuck |
| Let me test quickly with disconnected sample. | 我快速測不連通範例。 | If stuck |
| Visited count should stay below n. | visited 計數會小於 n。 | If stuck |
| That confirms minus-one branch. | 這可確認 -1 分支。 | If stuck |
| Great, now algorithm choice is justified. | 很好，現在演算法選擇有依據。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with Dijkstra shortest paths from source k. | 我用從 k 出發的 Dijkstra 最短路解題。 | Wrap-up |
| Each node settles at its minimum arrival time. | 每個節點都在最小到達時間被定稿。 | Wrap-up |
| Max settled time gives network delay result. | 最大定稿時間就是網路延遲答案。 | Wrap-up |
| If some nodes never settle, answer is minus one. | 若有節點永不定稿，答案是 -1。 | Wrap-up |
| Complexity is O(E log V) time and O(V plus E) space. | 複雜度是 O(ElogV) 時間與 O(V+E) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: time for signal from k to reach all nodes. | 目標：訊號從 k 到達全部節點所需時間。 | Cheat sheet |
| Directed weighted graph input. | 輸入是有向加權圖。 | Cheat sheet |
| Use Dijkstra from source k. | 從來源 k 使用 Dijkstra。 | Cheat sheet |
| Build adjacency list. | 建立鄰接表。 | Cheat sheet |
| Heap stores (time,node). | 堆存 (time,node)。 | Cheat sheet |
| Start with (0,k). | 從 (0,k) 起始。 | Cheat sheet |
| Pop smallest time state. | 彈出最小時間狀態。 | Cheat sheet |
| Skip if node already finalized. | 節點已定稿就略過。 | Cheat sheet |
| Finalize node time. | 定稿節點時間。 | Cheat sheet |
| Update maxTime. | 更新 maxTime。 | Cheat sheet |
| Push neighbors with time+w. | 推入鄰居時間 time+w。 | Cheat sheet |
| Continue until heap empty. | 持續直到堆空。 | Cheat sheet |
| If visited count < n return -1. | 若訪問數<n 回 -1。 | Cheat sheet |
| Else return maxTime. | 否則回 maxTime。 | Cheat sheet |
| Time O(E log V). | 時間 O(ElogV)。 | Cheat sheet |
| Space O(V+E). | 空間 O(V+E)。 | Cheat sheet |
| Common bug: treating edges as undirected. | 常見錯誤：把邊當無向。 | Cheat sheet |
| Common bug: not skipping stale heap entries. | 常見錯誤：未略過過期堆項。 | Cheat sheet |
| Bellman-Ford is slower alternative. | Bellman-Ford 是較慢替代。 | Cheat sheet |
| Explain max-of-shortest interpretation. | 強調「最短路最大值」詮釋。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Dijkstra-based shortest-time propagation preserved.
- No hallucinated constraints: ✅ Directed edges and unreachable-node handling maintained.
- Language simplicity: ✅ concise interview-safe phrasing.
