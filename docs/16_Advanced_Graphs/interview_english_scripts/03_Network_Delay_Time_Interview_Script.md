# 03 Network Delay Time — Interview English Script (C++)

> Source aligned with: `docs/16_Advanced_Graphs/03_Network_Delay_Time.md`

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem. | 我先重述題目。 | Restatement |
| We solve Network Delay Time. | 我們要解這一題。 | Restatement |
| Input and output follow the source statement. | 輸入輸出依來源敘述。 | Restatement |
| I will use Dijkstra's Algorithm as main method. | 我會用來源主方法。 | Restatement |
| I will verify edge cases before final answer. | 我會先驗證邊界案例。 | Restatement |
| Missing details are marked [CHECK]. | 缺漏細節會標記 [CHECK]。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I use source constraints directly? | 可直接採用來源限制嗎？ | Clarify |
| Do we have guaranteed valid input format? | 輸入格式是否保證合法？ | Clarify |
| Can I return early when condition is met? | 條件成立可提早回傳嗎？ | Clarify |
| Should output order matter in final answer? | 輸出順序是否有要求？ | Clarify |
| If missing, I will mark [CHECK], right? | 若缺漏我標 [CHECK] 可以嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force follows direct exhaustive checking. | 暴力法直接全面檢查。 | Approach |
| Brute time is about O(V \times E) from source. | 來源暴力時間約 O(V \times E)。 | Approach |
| Brute space is about O(V^3) from source. | 來源暴力空間約 O(V^3)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Optimized method uses Dijkstra's Algorithm. | 優化法使用來源主方法。 | Approach |
| I keep key invariant during updates. | 更新時維持關鍵不變量。 | Approach |
| I apply source transitions step by step. | 依來源規則逐步轉移。 | Approach |
| Optimized time is O(E \log E) from source. | 來源優化時間為 O(E \log E)。 | Approach |
| Optimized space is O(V + E) from source. | 來源優化空間為 O(V + E)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I build graph adjacency structure first. | 依來源步驟執行。 | Coding |
| Next, I initialize distance array and min heap. | 依來源步驟執行。 | Coding |
| Then, I use unordered_map for constant-time lookup. | 依來源步驟執行。 | Coding |
| Next, I keep heap invariant after each operation. | 依來源步驟執行。 | Coding |
| Then, I process nodes level by level with queue. | 依來源步驟執行。 | Coding |
| Next, I pop smallest distance node from heap. | 依來源步驟執行。 | Coding |
| Then, I skip stale states when needed. | 依來源步驟執行。 | Coding |
| Next, I relax outgoing edges and update distances. | 依來源步驟執行。 | Coding |
| Finally, I push improved states into heap. | 依來源步驟執行。 | Coding |
| I return final shortest-path result. | 依來源步驟執行。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let us dry-run one source sample input. | 我們手跑一組來源範例。 | Dry-run |
| Sample input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2. | 範例輸入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2。 | Dry-run |
| First, initialize required variables and structures. | 先初始化必要變數與結構。 | Dry-run |
| Next, execute first transition from source logic. | 接著執行第一個來源轉移。 | Dry-run |
| Then, continue updates until termination condition. | 然後持續更新到終止條件。 | Dry-run |
| State remains consistent with invariant. | 狀態保持符合不變量。 | Dry-run |
| Expected output: 2. | 預期輸出：2。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: smallest valid input case. | 案例一：最小合法輸入。 | Edge test |
| Case two: empty input behavior [CHECK]. | 案例二：空輸入行為 [CHECK]。 | Edge test |
| Case three: duplicated values or repeated pattern. | 案例三：重複值或重複模式。 | Edge test |
| Case four: boundary values near constraints. | 案例四：接近限制邊界值。 | Edge test |
| Case five: tricky pattern for naive solution. | 案例五：直覺解易錯模式。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(E \log E). | 時間複雜度是 O(E \log E)。 | Complexity |
| Space complexity is O(V + E). | 空間複雜度是 O(V + E)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| This follows the source optimized method. | 這是依來源優化方法。 | Complexity |
| Main runtime from source is O(E \log E). | 來源主要時間為 O(E \log E)。 | Complexity |
| Extra memory from source is O(V + E). | 來源額外空間為 O(V + E)。 | Complexity |
| Please recheck constraints if interviewer differs. | 若面試官條件不同請再確認。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 卡住時可用這句。 | If stuck |
| I will restate the core goal now. | 卡住時可用這句。 | If stuck |
| I can start from brute force first. | 卡住時可用這句。 | If stuck |
| Then I optimize with source method. | 卡住時可用這句。 | If stuck |
| I will verify one invariant quickly. | 卡住時可用這句。 | If stuck |
| Thanks, I will apply your hint. | 卡住時可用這句。 | If stuck |
| I found the likely bug position. | 卡住時可用這句。 | If stuck |
| I will patch this block first. | 卡住時可用這句。 | If stuck |
| Let me dry-run once again. | 卡住時可用這句。 | If stuck |
| Now I can continue coding clearly. | 卡住時可用這句。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed the final implementation. | 收尾時可用這句。 | Wrap-up |
| I followed the source optimized logic. | 收尾時可用這句。 | Wrap-up |
| I verified with normal and edge cases. | 收尾時可用這句。 | Wrap-up |
| Time is O(E \log E), space is O(V + E). | 收尾時可用這句。 | Wrap-up |
| I can discuss trade-offs if needed. | 收尾時可用這句。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate problem goal clearly. | 速記重點。 | Cheat sheet |
| Confirm constraints and assumptions. | 速記重點。 | Cheat sheet |
| Start from brute force baseline. | 速記重點。 | Cheat sheet |
| Explain why brute force is slower. | 速記重點。 | Cheat sheet |
| Present source optimized approach. | 速記重點。 | Cheat sheet |
| Keep one invariant during updates. | 速記重點。 | Cheat sheet |
| Use data structure from source. | 速記重點。 | Cheat sheet |
| Apply transitions in coding order. | 速記重點。 | Cheat sheet |
| Speak while writing each block. | 速記重點。 | Cheat sheet |
| Dry-run one representative sample. | 速記重點。 | Cheat sheet |
| Check smallest valid input. | 速記重點。 | Cheat sheet |
| Check empty input behavior [CHECK]. | 速記重點。 | Cheat sheet |
| Check duplicate or repeated pattern. | 速記重點。 | Cheat sheet |
| Check boundary limit values. | 速記重點。 | Cheat sheet |
| Report time complexity O(E \log E). | 速記重點。 | Cheat sheet |
| Report space complexity O(V + E). | 速記重點。 | Cheat sheet |
| State one clear trade-off point. | 速記重點。 | Cheat sheet |
| Use hint and adjust quickly. | 速記重點。 | Cheat sheet |
| Summarize final answer confidently. | 速記重點。 | Cheat sheet |
| Invite follow-up questions politely. | 速記重點。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Based on source chapter markdown.

- No hallucinated constraints: ✅ Unknown details marked `[CHECK]`.

- Language simplicity: ✅ Short A2-B1 lines for non-native speakers.