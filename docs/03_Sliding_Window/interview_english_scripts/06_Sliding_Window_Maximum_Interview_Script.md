# 06 Sliding Window Maximum — Interview English Script (C++)

> Source aligned with: `docs/03_Sliding_Window/06_Sliding_Window_Maximum.md`

> Quick links: [Source Solution](../06_Sliding_Window_Maximum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem. | 我先重述題目。 | Restatement |
| We solve Sliding Window Maximum. | 我們要解這一題。 | Restatement |
| Input and output follow the source statement. | 輸入輸出依來源敘述。 | Restatement |
| I will use Monotonic Deque as main method. | 我會用來源主方法。 | Restatement |
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
| Brute time is about O(n \cdot k) from source. | 來源暴力時間約 O(n \cdot k)。 | Approach |
| Brute space is about O(n^2) from source. | 來源暴力空間約 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Optimized method uses Monotonic Deque. | 優化法使用來源主方法。 | Approach |
| I keep key invariant during updates. | 更新時維持關鍵不變量。 | Approach |
| I apply source transitions step by step. | 依來源規則逐步轉移。 | Approach |
| Optimized time is O(n) from source. | 來源優化時間為 O(n)。 | Approach |
| Optimized space is O(k) from source. | 來源優化空間為 O(k)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize left pointer and window state. | 依來源步驟執行。 | Coding |
| Next, I expand window by moving right pointer. | 依來源步驟執行。 | Coding |
| Then, I update counts or score for new item. | 依來源步驟執行。 | Coding |
| Next, I shrink window when condition is invalid. | 依來源步驟執行。 | Coding |
| Then, I update best answer during valid window. | 依來源步驟執行。 | Coding |
| Next, I continue until right reaches end. | 依來源步驟執行。 | Coding |
| Then, I return the best recorded answer. | 依來源步驟執行。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let us dry-run one source sample input. | 我們手跑一組來源範例。 | Dry-run |
| Sample input: nums = [1,3,-1,-3,5,3,6,7], k = 3. | 範例輸入：nums = [1,3,-1,-3,5,3,6,7], k = 3。 | Dry-run |
| First, initialize required variables and structures. | 先初始化必要變數與結構。 | Dry-run |
| Next, execute first transition from source logic. | 接著執行第一個來源轉移。 | Dry-run |
| Then, continue updates until termination condition. | 然後持續更新到終止條件。 | Dry-run |
| State remains consistent with invariant. | 狀態保持符合不變量。 | Dry-run |
| Expected output: [3,3,5,5,6,7]. | 預期輸出：[3,3,5,5,6,7]。 | Dry-run |

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
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(k). | 空間複雜度是 O(k)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| This follows the source optimized method. | 這是依來源優化方法。 | Complexity |
| Main runtime from source is O(n). | 來源主要時間為 O(n)。 | Complexity |
| Extra memory from source is O(k). | 來源額外空間為 O(k)。 | Complexity |
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
| Time is O(n), space is O(k). | 收尾時可用這句。 | Wrap-up |
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
| Report time complexity O(n). | 速記重點。 | Cheat sheet |
| Report space complexity O(k). | 速記重點。 | Cheat sheet |
| State one clear trade-off point. | 速記重點。 | Cheat sheet |
| Use hint and adjust quickly. | 速記重點。 | Cheat sheet |
| Summarize final answer confidently. | 速記重點。 | Cheat sheet |
| Invite follow-up questions politely. | 速記重點。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Based on source chapter markdown.

- No hallucinated constraints: ✅ Unknown details marked `[CHECK]`.

- Language simplicity: ✅ Short A2-B1 lines for non-native speakers.
