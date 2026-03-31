# 06 Cheapest Flights Within K Stops — Interview English Script (C++)

> Source aligned with: `docs/16_Advanced_Graphs/06_Cheapest_Flights_K_Stops.md`

> Quick links: [Source Solution](../06_Cheapest_Flights_K_Stops.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate cheapest flights within k stops. | 我先重述 Cheapest Flights Within K Stops。 | Restatement |
| We have directed flights with prices between cities. | 題目給城市間有向航班與價格。 | Restatement |
| We need minimum price from src to dst. | 要找 src 到 dst 的最低價格。 | Restatement |
| Route can use at most k stops, so at most k plus one edges. | 路線最多 k 次中轉，也就是最多 k+1 條邊。 | Restatement |
| If no such route exists, return minus one. | 若無可行路線，回 -1。 | Restatement |
| I will use Bellman-Ford style relaxation for exactly stop-bounded shortest path. | 我會用 Bellman-Ford 變形做有中轉上限最短路。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are flights directed edges? | 航班邊是否為有向？ | Clarify |
| Is k counting intermediate nodes only, not edges? | k 是否只計中轉點，不是邊數？ | Clarify |
| If dst is unreachable within k stops, return minus one right? | 若在 k 中轉內不可達，是否回 -1？ | Clarify |
| Can there be multiple edges between same two cities? | 同兩城市間是否可能有多條不同價格邊？ | Clarify |
| Is O(k times flights) expected? | 是否預期 O(k*航班數) 解法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| DFS over all paths with stop pruning can still explode. | DFS 即使加中轉剪枝仍可能爆炸。 | Approach |
| Priority-queue search with stops dimension is possible but trickier to reason. | 帶 stops 維度的 PQ 搜尋可行但推理較複雜。 | Approach |
| Bellman-Ford iterations map directly to edge-count limit. | Bellman-Ford 迭代次數可直接對應邊數上限。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Initialize prices array with infinity and prices[src]=0. | prices 先設無限大，prices[src]=0。 | Approach |
| Repeat relaxation k plus one rounds. | 做 k+1 輪放鬆。 | Approach |
| In each round, relax all flights using previous-round prices snapshot. | 每輪用上一輪快照 prices 去放鬆所有航班。 | Approach |
| Snapshot prevents chaining more than one edge in same round. | 快照可避免同輪連鎖走超過一條邊。 | Approach |
| After rounds, return prices[dst] or minus one if still infinity. | 輪次後回 prices[dst]，仍無限大就回 -1。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create prices array size n and set all to INF. | 我建立大小 n 的 prices，全部設 INF。 | Coding |
| Set prices[src] to zero. | 把 prices[src] 設為 0。 | Coding |
| Loop i from zero to k inclusive for k plus one rounds. | i 從 0 到 k，共做 k+1 輪。 | Coding |
| Copy current prices into tmp array at round start. | 每輪開始先複製目前 prices 到 tmp。 | Coding |
| For each flight u v w, if prices[u] is reachable, try relax tmp[v]. | 對每航班 u,v,w，若 prices[u] 可達就嘗試放鬆 tmp[v]。 | Coding |
| Relax rule is tmp[v] = min(tmp[v], prices[u] plus w). | 放鬆規則：tmp[v]=min(tmp[v],prices[u]+w)。 | Coding |
| After processing all flights, assign prices = tmp. | 所有航班處理後，令 prices=tmp。 | Coding |
| Continue until all rounds done. | 重複直到輪次結束。 | Coding |
| If prices[dst] is INF, return minus one. | 若 prices[dst] 仍 INF，回 -1。 | Coding |
| Else return prices[dst]. | 否則回 prices[dst]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n three, flights 0-1 100, 1-2 100, 0-2 500, k one. | 我手跑 n=3，航班 0-1:100、1-2:100、0-2:500，k=1。 | Dry-run |
| Round zero allows one edge paths from src. | 第 0 輪允許最多一條邊路徑。 | Dry-run |
| Prices to one becomes one hundred, to two can be five hundred directly. | 到 1 變 100，到 2 可先是直飛 500。 | Dry-run |
| Round one allows up to two edges. | 第 1 輪允許最多兩條邊。 | Dry-run |
| Using previous snapshot, path 0 to 1 to 2 gives two hundred. | 用前輪快照，0->1->2 得到 200。 | Dry-run |
| Min with existing five hundred updates dst to two hundred. | 和原本 500 取最小後，dst 更新為 200。 | Dry-run |
| Final answer is two hundred. | 最終答案是 200。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: src equals dst should return zero. | 案例一：src=dst 應回 0。 | Edge test |
| Case two: k zero means direct flights only. | 案例二：k=0 只允許直飛。 | Edge test |
| Case three: path exists but requires more than k stops so return minus one. | 案例三：路徑存在但超過 k 中轉，回 -1。 | Edge test |
| Case four: multiple flights same route with different prices. | 案例四：同路線多價格航班。 | Edge test |
| Case five: disconnected destination unreachable in any round. | 案例五：目的地完全不連通。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O((k plus one) times E). | 時間複雜度是 O((k+1)*E)。 | Complexity |
| Space complexity is O(N). | 空間複雜度是 O(N)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We run exactly k plus one relaxation rounds. | 我們固定執行 k+1 輪放鬆。 | Complexity |
| Each round scans all E flights once. | 每輪都完整掃描 E 條航班。 | Complexity |
| So total runtime is O((k plus one) times E). | 因此總時間是 O((k+1)*E)。 | Complexity |
| Two arrays of size N are maintained, giving O(N) memory. | 只維護兩個大小 N 的陣列，空間 O(N)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me map stops limit to edge count limit. | 我先把中轉限制映射成邊數限制。 | If stuck |
| K stops means at most k plus one edges. | k 次中轉代表最多 k+1 條邊。 | If stuck |
| Bellman-Ford iteration i gives best cost using up to i plus one edges. | Bellman-Ford 第 i 輪可得最多 i+1 邊最佳成本。 | If stuck |
| Snapshot array is crucial to enforce round boundary. | 快照陣列是維持輪次邊界的關鍵。 | If stuck |
| Without snapshot, one round may chain too many edges. | 沒快照同輪可能串太多邊。 | If stuck |
| Let me test quickly when k equals zero. | 我快速測 k=0 情況。 | If stuck |
| Only direct edge from src should matter. | 這時只應考慮 src 直飛邊。 | If stuck |
| This confirms round interpretation. | 這可驗證輪次詮釋。 | If stuck |
| After rounds, INF means unreachable under limit. | 輪次後若仍 INF 代表在限制內不可達。 | If stuck |
| Great, now implementation is deterministic. | 很好，現在實作邏輯是確定的。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with stop-bounded Bellman-Ford relaxation. | 我用有中轉上限的 Bellman-Ford 放鬆法解題。 | Wrap-up |
| k plus one rounds correspond to allowed edge count. | k+1 輪正好對應允許邊數。 | Wrap-up |
| Snapshot per round keeps stop constraint correct. | 每輪快照可正確維持中轉限制。 | Wrap-up |
| Complexity is O((k plus one) times E) time and O(N) space. | 複雜度是 O((k+1)*E) 時間與 O(N) 空間。 | Wrap-up |
| This is the cleanest interview explanation for this constrainted shortest path variant. | 這是此類受限最短路最乾淨的面試說法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: cheapest src to dst within k stops. | 目標：k 中轉內 src 到 dst 最低價。 | Cheat sheet |
| Directed weighted graph flights. | 輸入是有向加權航班圖。 | Cheat sheet |
| K stops => max k+1 edges. | k 中轉 => 最多 k+1 邊。 | Cheat sheet |
| Use Bellman-Ford style rounds. | 用 Bellman-Ford 輪次法。 | Cheat sheet |
| prices initialized INF, prices[src]=0. | prices 初始 INF，src 為 0。 | Cheat sheet |
| Repeat k+1 rounds. | 重複 k+1 輪。 | Cheat sheet |
| Copy prices to tmp each round. | 每輪先複製 prices 到 tmp。 | Cheat sheet |
| Relax all flights on tmp using prices. | 用 prices 放鬆所有航班到 tmp。 | Cheat sheet |
| Rule: tmp[v]=min(tmp[v],prices[u]+w). | 規則：tmp[v]=min(tmp[v],prices[u]+w)。 | Cheat sheet |
| Assign prices=tmp after round. | 輪末更新 prices=tmp。 | Cheat sheet |
| End rounds then check prices[dst]. | 輪次結束檢查 prices[dst]。 | Cheat sheet |
| INF means unreachable => -1. | INF 代表不可達 => -1。 | Cheat sheet |
| Else return prices[dst]. | 否則回 prices[dst]。 | Cheat sheet |
| k=0 means direct flight only. | k=0 只看直飛。 | Cheat sheet |
| Time O((k+1)E). | 時間 O((k+1)E)。 | Cheat sheet |
| Space O(N). | 空間 O(N)。 | Cheat sheet |
| Common bug: no tmp snapshot. | 常見錯誤：沒用 tmp 快照。 | Cheat sheet |
| Common bug: wrong interpretation of stops. | 常見錯誤：中轉定義解讀錯。 | Cheat sheet |
| Dijkstra-with-stops is alternative but trickier. | 帶 stops 的 Dijkstra 是替代但較難。 | Cheat sheet |
| Explain rounds as edge-budget growth. | 用「可用邊數逐輪增加」解釋最直觀。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Bellman-Ford with per-round snapshot preserved.
- No hallucinated constraints: ✅ stop limit semantics and -1 condition maintained.
- Language simplicity: ✅ concise interview-ready narration.
