# 07 Walls and Gates — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/07_Walls_and_Gates.md`

> Quick links: [Source Solution](../07_Walls_and_Gates.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate walls and gates. | 我先重述 Walls and Gates。 | Restatement |
| Grid cells can be wall minus one, gate zero, or empty room INF. | 格子可能是牆 -1、門 0、或空房 INF。 | Restatement |
| For each empty room, we need distance to nearest gate. | 每個空房要填入到最近門的距離。 | Restatement |
| Unreachable rooms should stay INF. | 無法到達門的房間保持 INF。 | Restatement |
| We must update the grid in place. | 題目要求原地更新網格。 | Restatement |
| I will use multi-source BFS from all gates. | 我會從所有門做多源 BFS。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is INF represented by INT_MAX? | INF 是否以 INT_MAX 表示？ | Clarify |
| Is movement limited to four directions? | 移動是否只限四方向？ | Clarify |
| Should walls always remain minus one? | 牆是否永遠保持 -1？ | Clarify |
| Can there be zero gates in the grid? | 網格中是否可能沒有門？ | Clarify |
| Function should return void and mutate input only, right? | 函式是否回 void 並只改輸入？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force runs BFS from every empty room to nearest gate. | 暴力法從每個空房各跑一次 BFS 找最近門。 | Approach |
| This repeats huge traversal many times. | 這會大量重複遍歷。 | Approach |
| Worst case is near O((mn) squared). | 最壞接近 O((mn)^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Reverse search direction: start from all gates together. | 反向搜尋：從所有門同時出發。 | Approach |
| Push all gate cells into queue initially. | 初始把所有門座標推入 queue。 | Approach |
| BFS level expands shortest distance naturally. | BFS 分層天然對應最短距離。 | Approach |
| When we first reach an INF room, assign current distance plus one. | 首次到達 INF 房時，填目前距離加一。 | Approach |
| Since first visit is shortest, no further update is needed. | 首訪即最短，不需要再更新。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I scan grid and enqueue every gate position. | 我先掃網格，把每個門加入 queue。 | Coding |
| I keep four direction vectors. | 我準備四方向向量。 | Coding |
| While queue is not empty, pop one position. | queue 非空時彈出一個位置。 | Coding |
| For each neighbor, check boundary first. | 對每個鄰居先做邊界檢查。 | Coding |
| If neighbor is not INF, skip it. | 鄰居若不是 INF 就跳過。 | Coding |
| If neighbor is INF, set rooms[nr][nc] to rooms[r][c] plus one. | 鄰居若是 INF，就設為 rooms[r][c]+1。 | Coding |
| Then enqueue this updated room. | 再把這個已更新房間入隊。 | Coding |
| Continue until queue is empty. | 持續直到 queue 清空。 | Coding |
| Walls and original gates remain unchanged. | 牆與原門都不會被改動。 | Coding |
| End function with in-place updated grid. | 函式結束時網格已原地更新。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the classic four by four sample. | 我手跑經典 4x4 範例。 | Dry-run |
| Queue starts with both gate positions. | queue 初始含兩個門的位置。 | Dry-run |
| First BFS layer fills adjacent INF rooms with one. | 第一層 BFS 先把相鄰 INF 填成 1。 | Dry-run |
| Next layer fills reachable rooms with two. | 下一層把可達房間填成 2。 | Dry-run |
| Walls block expansion and unreachable rooms stay INF. | 牆會阻擋擴散，不可達房間維持 INF。 | Dry-run |
| Distances propagate outward level by level. | 距離會一層一層向外擴散。 | Dry-run |
| Final grid matches expected shortest distances. | 最終網格符合預期最短距離。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: no gate at all, grid stays same. | 案例一：沒有門時網格維持原樣。 | Edge test |
| Case two: all walls only, grid unchanged. | 案例二：全是牆，網格不變。 | Edge test |
| Case three: all gates only, all zeros remain. | 案例三：全是門，0 全保留。 | Edge test |
| Case four: one gate with straight open corridor. | 案例四：單門加直通走廊。 | Edge test |
| Case five: isolated room behind walls remains INF. | 案例五：被牆隔離房間維持 INF。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(rows times cols). | 時間複雜度是 O(rows*cols)。 | Complexity |
| Space complexity is O(rows times cols) worst case queue. | 空間最壞是 O(rows*cols) 的 queue。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each cell can enter queue at most once when first assigned shortest distance. | 每格在首次賦值最短距離時最多入隊一次。 | Complexity |
| Neighbor checks are constant work per pop. | 每次出隊只做常數次鄰居檢查。 | Complexity |
| Therefore runtime is linear O(mn). | 因此總時間是線性 O(mn)。 | Complexity |
| Queue can hold many cells at once, up to O(mn) in worst case. | queue 最壞可同時容納 O(mn) 個格子。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me connect this to rotting oranges pattern. | 我把它對應到 Rotting Oranges 模式。 | If stuck |
| It is also multi-source BFS from all gates. | 它同樣是從所有門出發的多源 BFS。 | If stuck |
| First reach to a room means shortest path. | 房間第一次被到達就是最短路。 | If stuck |
| So each INF room should be assigned once. | 所以每個 INF 房只要賦值一次。 | If stuck |
| We skip walls and already assigned rooms. | 跳過牆與已賦值房間。 | If stuck |
| Distance transition is parent plus one. | 距離轉移是父節點加一。 | If stuck |
| Let me test an isolated INF behind walls. | 我測一個被牆隔離的 INF。 | If stuck |
| It should remain INF forever. | 它應永遠保持 INF。 | If stuck |
| This confirms skip condition is correct. | 這可確認跳過條件正確。 | If stuck |
| Great, now code flow is clear. | 很好，現在程式流程很清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with multi-source BFS from all gates. | 我用從所有門出發的多源 BFS 解題。 | Wrap-up |
| BFS levels naturally encode shortest room distance. | BFS 分層自然對應最短房間距離。 | Wrap-up |
| INF rooms are updated once on first reach. | INF 房間在首訪時更新一次。 | Wrap-up |
| Complexity is O(mn) time and O(mn) space. | 複雜度是 O(mn) 時間與 O(mn) 空間。 | Wrap-up |
| This is the canonical nearest-source grid pattern. | 這是網格最近來源題的典型模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: fill each INF with nearest gate distance. | 目標：每個 INF 填最近門距離。 | Cheat sheet |
| Values: wall -1, gate 0, room INF. | 值定義：牆 -1、門 0、房 INF。 | Cheat sheet |
| Use multi-source BFS. | 使用多源 BFS。 | Cheat sheet |
| Enqueue all gates first. | 先把所有門入隊。 | Cheat sheet |
| Keep four direction moves. | 使用四方向移動。 | Cheat sheet |
| Pop one cell from queue. | 每次彈出一格。 | Cheat sheet |
| Check each neighbor bounds. | 檢查鄰居邊界。 | Cheat sheet |
| Process only INF neighbors. | 只處理 INF 鄰居。 | Cheat sheet |
| Set neighbor = current + 1. | 鄰居值設為 current+1。 | Cheat sheet |
| Enqueue updated neighbor. | 把更新後鄰居入隊。 | Cheat sheet |
| Skip walls and non-INF cells. | 跳過牆與非 INF。 | Cheat sheet |
| First update is shortest distance. | 首次更新即最短距離。 | Cheat sheet |
| No gate means no changes. | 無門時不會變化。 | Cheat sheet |
| Isolated INF stays INF. | 隔離 INF 保持 INF。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Queue space O(mn). | queue 空間 O(mn)。 | Cheat sheet |
| In-place update required. | 需要原地更新。 | Cheat sheet |
| Common bug: running BFS from each room. | 常見錯誤：從每個房間分別跑 BFS。 | Cheat sheet |
| Common bug: updating non-INF cell. | 常見錯誤：錯更新非 INF 格。 | Cheat sheet |
| Mention relation to rotting oranges. | 可提與 Rotting Oranges 的關聯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Multi-source BFS from all gates with INF-only expansion.
- No hallucinated constraints: ✅ In-place mutation and value semantics preserved.
- Language simplicity: ✅ Practical short interview lines.
