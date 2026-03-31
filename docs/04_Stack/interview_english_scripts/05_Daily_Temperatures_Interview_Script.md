# 05 Daily Temperatures — Interview English Script (C++)

> Source aligned with: `docs/04_Stack/05_Daily_Temperatures.md`

> Quick links: [Source Solution](../05_Daily_Temperatures.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| temperatures[i] is the temperature on day i. | temperatures[i] 是第 i 天溫度。 | Restatement |
| For each day, we need days until a warmer temperature. | 每一天要算等到更高溫需幾天。 | Restatement |
| If no warmer day exists, answer is zero. | 若之後無更高溫，答案是 0。 | Restatement |
| I will use a monotonic decreasing stack of indices. | 我會用遞減單調 stack 存索引。 | Restatement |
| This lets us fill waiting days in one pass. | 這能在一趟掃描填出等待天數。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can temperatures include equal values on many days? | 溫度可否在多天內相等？ | Clarify |
| Is strictly warmer required, not equal? | 是否必須「嚴格更高溫」才算？ | Clarify |
| Should output length equal input length always? | 輸出長度是否一定等於輸入長度？ | Clarify |
| Is O(n) expected due to large n? | 因 n 很大，是否預期 O(n)？ | Clarify |
| Can I store indices rather than temperatures in stack? | 我可在 stack 存索引而非溫度嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline scans forward from each day i. | 基線是從每一天 i 向後掃描。 | Approach |
| Stop when finding first day with higher temperature. | 找到第一個更高溫日就停止。 | Approach |
| Worst-case time is O(n^2). | 最差時間是 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Stack stores indices with decreasing temperatures. | stack 內索引對應溫度維持遞減。 | Approach |
| Current warmer day can resolve previous colder days. | 當前較高溫可一次解決先前較低溫日。 | Approach |
| While current temp is greater than stack top temp, pop. | 當前溫度高於 top 對應溫度就持續 pop。 | Approach |
| For each popped index j, answer is i minus j. | 每個被 pop 的 j，答案是 i-j。 | Approach |
| Push current index after resolving pops. | 完成 pop 結算後再 push 當前索引。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create result array initialized with zeros. | 先建立全為 0 的結果陣列。 | Coding |
| I also initialize an empty stack of indices. | 同時初始化空的索引 stack。 | Coding |
| Scan days from left to right. | 由左到右掃描每天。 | Coding |
| While stack not empty and temp[i] is warmer, pop index j. | 若 temp[i] 更高，持續 pop 索引 j。 | Coding |
| Set answer[j] to i minus j. | 把 answer[j] 設為 i-j。 | Coding |
| After resolving all possible pops, push i. | 完成可結算 pop 後，把 i push 進去。 | Coding |
| Remaining indices in stack keep default zero. | 最後留在 stack 的索引維持預設 0。 | Coding |
| Return the answer array. | 回傳答案陣列。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [73,74,75,71,69,72,76,73]. | 我手跑 [73,74,75,71,69,72,76,73]。 | Dry-run |
| Day 0 with 73 waits, stack keeps index 0. | 第 0 天 73 先等待，stack 放 0。 | Dry-run |
| Day 1 with 74 pops 0, so answer[0] is 1. | 第 1 天 74 會 pop 0，所以 answer[0]=1。 | Dry-run |
| Day 2 with 75 pops 1, so answer[1] is 1. | 第 2 天 75 會 pop 1，所以 answer[1]=1。 | Dry-run |
| Day 5 with 72 resolves days 4 and 3. | 第 5 天 72 會解決第 4 與第 3 天。 | Dry-run |
| Day 6 with 76 resolves 5 and 2. | 第 6 天 76 會解決第 5 與第 2 天。 | Dry-run |
| Final output is [1,1,4,2,1,1,0,0]. | 最終輸出是 [1,1,4,2,1,1,0,0]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single day should return [0]. | 案例一：單日輸入應回傳 [0]。 | Edge test |
| Case two: strictly increasing temperatures. | 案例二：溫度嚴格遞增。 | Edge test |
| Case three: strictly decreasing temperatures. | 案例三：溫度嚴格遞減。 | Edge test |
| Case four: repeated equal temperatures. | 案例四：大量相等溫度。 | Edge test |
| Case five: mixed peaks and valleys. | 案例五：高低峰混合序列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(n). | 額外空間是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each index is pushed once into stack. | 每個索引只會被 push 一次。 | Complexity |
| Each index is popped at most once. | 每個索引最多被 pop 一次。 | Complexity |
| Therefore total stack operations are linear. | 因此 stack 操作總量是線性的。 | Complexity |
| Result array and stack both use O(n) space. | 結果陣列與 stack 都是 O(n) 空間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate stack monotonic rule. | 我先重述 stack 單調規則。 | If stuck |
| Stack should keep unresolved colder days. | stack 應只保留未解決的較冷日期。 | If stuck |
| Warmer current day should pop and resolve them. | 當前較熱日要 pop 並解決它們。 | If stuck |
| I can show brute-force idea first. | 我可先講暴力想法。 | If stuck |
| Then I switch back to O(n) stack. | 再切回 O(n) stack 解法。 | If stuck |
| Thanks, I found a comparison direction bug. | 謝謝，我找到比較方向 bug。 | If stuck |
| Let me rerun the sample quickly. | 我快速重跑範例。 | If stuck |
| Now waiting-day differences are correct. | 現在等待天數差值正確。 | If stuck |
| Final answer array is consistent. | 最終答案陣列一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(n). | 額外空間是 O(n)。 | Wrap-up |
| I can discuss reverse-scan variant if needed. | 若需要我可補充反向掃描變體。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate waiting-days-for-warmer-temp goal. | 重述等待更高溫天數目標。 | Cheat sheet |
| Mention strict warmer condition. | 提到必須嚴格更高。 | Cheat sheet |
| Brute force scans forward each day. | 暴力法是每天向後掃。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法為 O(n^2)。 | Cheat sheet |
| Use monotonic decreasing stack of indices. | 使用遞減單調索引 stack。 | Cheat sheet |
| While current temp warmer, pop old day. | 當前更熱就 pop 舊日。 | Cheat sheet |
| Fill answer as current index minus popped index. | 答案填 current index 減 popped index。 | Cheat sheet |
| Push current index after pops. | pop 完後 push 當前索引。 | Cheat sheet |
| Unresolved indices remain zero by default. | 未解索引預設保持 0。 | Cheat sheet |
| Dry-run [73,74,75,71,69,72,76,73]. | 手跑 [73,74,75,71,69,72,76,73]。 | Cheat sheet |
| Verify output [1,1,4,2,1,1,0,0]. | 驗證輸出 [1,1,4,2,1,1,0,0]。 | Cheat sheet |
| Test single-day case. | 測單日案例。 | Cheat sheet |
| Test increasing sequence. | 測遞增序列。 | Cheat sheet |
| Test decreasing sequence. | 測遞減序列。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(n) extra space. | 報告 O(n) 額外空間。 | Cheat sheet |
| Mention each index pops at most once. | 提到每個索引最多 pop 一次。 | Cheat sheet |
| If stuck, check comparison direction. | 卡住時檢查比較方向。 | Cheat sheet |
| Re-run sample after fix. | 修正後重跑範例。 | Cheat sheet |
| End with concise summary. | 用精簡總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Monotonic stack resolution logic is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
