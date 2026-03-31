# 03 Jump Game II — Interview English Script (C++)

> Source aligned with: `docs/13_Greedy/03_Jump_Game_II.md`

> Quick links: [Source Solution](../03_Jump_Game_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate jump game two. | 我先重述 Jump Game II。 | Restatement |
| We start at index zero and each nums[i] gives max jump length. | 從索引 0 出發，nums[i] 給最大跳長。 | Restatement |
| We are guaranteed to reach the last index. | 題目保證一定能到終點。 | Restatement |
| We need the minimum number of jumps. | 要求最少跳躍次數。 | Restatement |
| This is shortest-level traversal in implicit graph. | 這是隱式圖上的最短層級問題。 | Restatement |
| I will use greedy BFS-window expansion. | 我會用貪心 BFS 視窗擴張法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is reachability always guaranteed in this version? | 這版是否保證一定可達？ | Clarify |
| Should we return jump count only? | 是否只回跳躍次數？ | Clarify |
| Is n at least one? | n 是否至少為 1？ | Clarify |
| Can we use greedy instead of explicit BFS queue? | 是否可用貪心取代顯式 BFS 佇列？ | Clarify |
| Is O(n) expected? | O(n) 是否為預期解？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force explores all jump choices recursively. | 暴力遞迴探索所有跳法。 | Approach |
| Dynamic programming can still be O(n squared). | 動態規劃仍可能是 O(n²)。 | Approach |
| We want linear-time level-based greedy. | 我們想要線性時間的層級貪心。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Treat current jump count as a window [l, r] of reachable indices. | 把當前跳數可達索引視為視窗 [l,r]。 | Approach |
| Scan this window to compute farthest index for next jump. | 掃描此視窗算出下一跳最遠 farthest。 | Approach |
| After scanning, move to next window [r+1, farthest]. | 掃描完後切到下一視窗 [r+1,farthest]。 | Approach |
| Each window expansion means one additional jump. | 每次視窗擴張代表多跳一次。 | Approach |
| Continue until r reaches or passes last index. | 持續直到 r 到達或超過終點。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize jumps to zero and window l equals r equals zero. | 我初始化 jumps=0，且視窗 l=r=0。 | Coding |
| While r is before last index, I compute next farthest reach. | 當 r 尚未到終點時，計算下一層最遠點。 | Coding |
| I iterate i from l to r and update farthest=max(farthest,i+nums[i]). | i 從 l 到 r，更新 farthest=max(farthest,i+nums[i])。 | Coding |
| After loop, I set l to r plus one. | 迴圈後把 l 設為 r+1。 | Coding |
| I set r to farthest. | 把 r 設為 farthest。 | Coding |
| I increment jumps by one. | jumps 加一。 | Coding |
| Repeat until window covers last index. | 重複直到視窗覆蓋終點。 | Coding |
| Return jumps as minimum count. | 回傳 jumps 作最少跳數。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [2,3,1,1,4]. | 我手跑 nums=[2,3,1,1,4]。 | Dry-run |
| Start window is [0,0], farthest becomes two. | 起始視窗 [0,0]，farthest 變 2。 | Dry-run |
| Move to next window [1,2], jumps now one. | 換到視窗 [1,2]，目前 jumps=1。 | Dry-run |
| Scan indices one and two, farthest becomes four. | 掃描索引 1、2 後 farthest 變 4。 | Dry-run |
| Move window to [3,4], jumps now two. | 視窗移到 [3,4]，jumps=2。 | Dry-run |
| r already reaches last index, stop. | r 已到終點，停止。 | Dry-run |
| Final answer is two. | 最終答案是 2。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element array should return zero jumps. | 案例一：單元素陣列應回 0 跳。 | Edge test |
| Case two: direct one jump to end. | 案例二：一次直接跳到終點。 | Edge test |
| Case three: many small steps required. | 案例三：需要多次小步前進。 | Edge test |
| Case four: zeros inside but still guaranteed reachable. | 案例四：中間有 0 但仍保證可達。 | Edge test |
| Case five: long array with late maximum extension. | 案例五：長陣列在後段才擴張最遠距離。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each index is scanned at most once within some window. | 每個索引最多在某個視窗中被掃一次。 | Complexity |
| Window boundaries only move forward. | 視窗邊界只會向前推進。 | Complexity |
| Therefore total runtime is linear O(n). | 因此總時間是線性 O(n)。 | Complexity |
| We use constant scalar variables, so memory is O(1). | 只用常數個變數，因此空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me view this as BFS by levels. | 我把它視為按層 BFS。 | If stuck |
| Current level is the reachable index window. | 當前層就是可達索引視窗。 | If stuck |
| One jump means moving to next level window. | 一次跳躍就是移到下一層視窗。 | If stuck |
| I only need farthest reach from current window. | 我只需要當前視窗的最遠可達點。 | If stuck |
| After scanning window, jump count increases by one. | 掃完視窗後跳數加一。 | If stuck |
| Then update l and r for next window. | 再更新下一視窗的 l 與 r。 | If stuck |
| Let me test quickly with [2,3,1,1,4]. | 我快速測 [2,3,1,1,4]。 | If stuck |
| It should finish in two levels. | 這會在兩層內完成。 | If stuck |
| That confirms minimum jumps equals two. | 這確認最少跳數為 2。 | If stuck |
| Great, approach is consistent. | 很好，方法一致且穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved jump game two with greedy level expansion. | 我用貪心層級擴張解了 Jump Game II。 | Wrap-up |
| Each window represents all indices reachable with current jump count. | 每個視窗代表當前跳數可達的所有索引。 | Wrap-up |
| Next farthest boundary gives optimal next jump decision. | 下一層最遠邊界給出最優跳躍決策。 | Wrap-up |
| Complexity is O(n) time and O(1) space. | 複雜度是 O(n) 時間、O(1) 空間。 | Wrap-up |
| This is the standard interview-optimal solution. | 這是面試常見最優解。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: minimum jumps to reach last index. | 目標：以最少跳數到達最後索引。 | Cheat sheet |
| Reachability is guaranteed. | 題目保證可達。 | Cheat sheet |
| Use greedy BFS-window idea. | 使用貪心 BFS 視窗思路。 | Cheat sheet |
| Track l and r for current window. | 用 l、r 追蹤當前視窗。 | Cheat sheet |
| Track farthest for next window. | 用 farthest 記錄下一層最遠點。 | Cheat sheet |
| Initialize l=r=0, jumps=0. | 初始化 l=r=0，jumps=0。 | Cheat sheet |
| While r < n-1, scan i in [l,r]. | 當 r<n-1，掃描 i in [l,r]。 | Cheat sheet |
| Update farthest=max(farthest,i+nums[i]). | 更新 farthest=max(farthest,i+nums[i])。 | Cheat sheet |
| Move window to [r+1,farthest]. | 視窗移到 [r+1,farthest]。 | Cheat sheet |
| jumps++. | jumps 加一。 | Cheat sheet |
| Stop when r reaches end. | r 到終點就停止。 | Cheat sheet |
| Return jumps. | 回傳 jumps。 | Cheat sheet |
| [2,3,1,1,4] -> 2. | [2,3,1,1,4] -> 2。 | Cheat sheet |
| Single element -> 0. | 單元素 -> 0。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: using wrong next window start. | 常見錯誤：下一視窗起點設錯。 | Cheat sheet |
| Common bug: forgetting to reset farthest each round. | 常見錯誤：每輪忘記重設 farthest。 | Cheat sheet |
| Explain level interpretation to justify optimality. | 用層級解釋可證明最優性。 | Cheat sheet |
| Keep indexing boundaries explicit. | 索引邊界要說清楚。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Greedy BFS-window expansion preserved.
- No hallucinated constraints: ✅ Guaranteed reachability and min-jump objective maintained.
- Language simplicity: ✅ Clear line-by-line interview narration.
