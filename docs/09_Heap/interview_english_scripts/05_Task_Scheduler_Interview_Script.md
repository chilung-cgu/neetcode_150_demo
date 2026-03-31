# 05 Task Scheduler — Interview English Script (C++)

> Source aligned with: `docs/09_Heap/05_Task_Scheduler.md`

> Quick links: [Source Solution](../05_Task_Scheduler.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the task scheduler problem. | 我先重述任務排程題。 | Restatement |
| We have task letters and cooldown n between same task types. | 有任務字母，且同類任務間隔至少 n。 | Restatement |
| Each task takes one unit of CPU time. | 每個任務花 1 單位時間。 | Restatement |
| CPU may be idle if no valid task is ready. | 若無合法任務可執行，CPU 可 idle。 | Restatement |
| We need the minimum total intervals to finish all tasks. | 要求完成所有任務的最少總時間。 | Restatement |
| I will use the frequency formula based greedy approach. | 我會用頻率公式的貪婪解法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are task labels limited to uppercase English letters? | 任務標籤是否限大寫英文字母？ | Clarify |
| Is n allowed to be zero? | n 是否可能為 0？ | Clarify |
| Do we only need length, not the actual schedule sequence? | 只需回傳長度，不需回傳排程序列嗎？ | Clarify |
| Can multiple task types tie for maximum frequency? | 多種任務可能並列最大頻率嗎？ | Clarify |
| Should I present both formula and simulation intuition? | 是否要同時說公式與模擬直覺？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force simulates every interval and chooses feasible tasks. | 暴力法逐時間模擬並挑可執行任務。 | Approach |
| This often uses max-heap plus cooldown queue. | 通常會用 max-heap 搭配冷卻佇列。 | Approach |
| It works but is heavier than needed for this question. | 可行但對本題來說較笨重。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Key is the most frequent task count, call it maxFreq. | 關鍵是最高頻率，記為 maxFreq。 | Approach |
| We create maxFreq minus one full blocks of length n plus one. | 形成 maxFreq-1 個長度 n+1 的區塊。 | Approach |
| Then add number of tasks that tie at maxFreq. | 再加上並列 maxFreq 的任務數。 | Approach |
| Formula candidate is maxFreq minus one times n plus one plus ties. | 公式候選為 (maxFreq-1)*(n+1)+ties。 | Approach |
| Final answer is max of this candidate and total task count. | 最後答案是候選值與任務總數取較大。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I count frequency of each task type first. | 我先統計每種任務頻率。 | Coding |
| While counting, I track the maximum frequency value. | 統計同時追蹤最大頻率值。 | Coding |
| Next I count how many task types equal that max frequency. | 接著算有幾種任務達到最大頻率。 | Coding |
| I compute formula length with block structure. | 我用區塊結構計算公式長度。 | Coding |
| Formula is maxFreq minus one times n plus one plus tie count. | 公式為 (maxFreq-1)*(n+1)+並列數。 | Coding |
| Then I compare formula length with tasks size. | 然後把公式長度與 tasks.size() 比較。 | Coding |
| I return the larger one as minimum intervals. | 回傳較大者作為最小總時間。 | Coding |
| This handles both idle-heavy and fully packed schedules. | 這可同時涵蓋有 idle 與無 idle 情況。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run tasks A A A B B B with n equals 2. | 我手跑 tasks A A A B B B、n=2。 | Dry-run |
| Frequencies are A three and B three, so maxFreq is three. | 頻率 A=3、B=3，所以 maxFreq=3。 | Dry-run |
| Number of maxFreq task types is two. | 達最大頻率的種類數是 2。 | Dry-run |
| Formula gives three minus one times three plus two equals eight. | 公式得 (3-1)*3+2=8。 | Dry-run |
| Total tasks count is six, so answer is max of six and eight. | 任務總數是 6，答案取 max(6,8)。 | Dry-run |
| Final answer is eight intervals. | 最終答案是 8 個時間單位。 | Dry-run |
| This matches the expected sample output. | 這與範例預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals zero, answer should be tasks length. | 案例一：n=0 時答案應等於任務總數。 | Edge test |
| Case two: single task type repeated many times. | 案例二：只有一種任務重複很多次。 | Edge test |
| Case three: many task types with same maximum frequency. | 案例三：多種類並列最大頻率。 | Edge test |
| Case four: enough filler tasks so no idle is needed. | 案例四：填充任務夠多，不需 idle。 | Edge test |
| Case five: minimal input length one. | 案例五：最小輸入長度 1。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n) where n is number of tasks. | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(1) for fixed alphabet size. | 固定字母集下空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We do one linear pass to count frequencies. | 我們做一次線性掃描統計頻率。 | Complexity |
| Finding max frequency and tie count is constant over 26 letters. | 對 26 字母找最大與並列數是常數操作。 | Complexity |
| So total runtime is O(n). | 因此總時間是 O(n)。 | Complexity |
| Frequency array size is constant, so memory is O(1). | 頻率陣列大小固定，所以空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me avoid over-simulation and focus on frequency structure. | 我先避免過度模擬，聚焦頻率結構。 | If stuck |
| The bottleneck is always the most frequent task type. | 瓶頸永遠是最高頻任務。 | If stuck |
| I can build blocks around that bottleneck. | 我可用它建立區塊骨架。 | If stuck |
| Block count is maxFreq minus one. | 區塊數是 maxFreq-1。 | If stuck |
| Block width is n plus one. | 區塊寬度是 n+1。 | If stuck |
| Then I add the number of tied max-frequency tasks. | 再加上並列最大頻率種類數。 | If stuck |
| Final answer cannot be below total tasks count. | 最終答案不可能小於任務總數。 | If stuck |
| So I take max between formula and tasks length. | 所以取公式與總數的較大值。 | If stuck |
| Let me verify with A A A B B B, n equals 2. | 我用 A A A B B B、n=2 驗證。 | If stuck |
| It gives eight correctly, so formula is consistent. | 得到 8，公式一致正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it using the max-frequency block formula. | 我用最大頻率區塊公式解出此題。 | Wrap-up |
| This avoids heavy simulation while keeping correctness. | 這避免笨重模擬且保持正確性。 | Wrap-up |
| We compute candidate idle-aware length from maxFreq and ties. | 用 maxFreq 與並列數算含 idle 候選長度。 | Wrap-up |
| Final result is max of candidate and task count. | 最終結果是候選值與任務數取較大。 | Wrap-up |
| Complexity is O(n) time and O(1) space. | 複雜度為 O(n) 時間、O(1) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem asks minimum total intervals. | 題目要最小總時間區間數。 | Cheat sheet |
| Same task needs cooldown n. | 同任務間需冷卻 n。 | Cheat sheet |
| Each task takes one interval. | 每任務耗時一格。 | Cheat sheet |
| CPU can be idle if needed. | 必要時 CPU 可 idle。 | Cheat sheet |
| Count frequency of each letter. | 先統計各字母頻率。 | Cheat sheet |
| Find maxFreq. | 找出 maxFreq。 | Cheat sheet |
| Count how many tasks tie maxFreq. | 計算並列 maxFreq 數量。 | Cheat sheet |
| Build blocks: maxFreq minus one. | 建立區塊：maxFreq-1。 | Cheat sheet |
| Block width: n plus one. | 區塊寬度：n+1。 | Cheat sheet |
| Candidate length: blocks times width plus ties. | 候選長度：區塊乘寬再加並列數。 | Cheat sheet |
| Candidate formula: (maxFreq-1)*(n+1)+ties. | 候選公式：(maxFreq-1)*(n+1)+ties。 | Cheat sheet |
| Final answer is max(candidate, total tasks). | 最終答案 max(候選, 任務總數)。 | Cheat sheet |
| n equals zero gives tasks length. | n=0 時答案即任務總數。 | Cheat sheet |
| If fillers are enough, no idle needed. | 填充任務夠多就不需 idle。 | Cheat sheet |
| If one task dominates, idle appears. | 單一任務過多就會出現 idle。 | Cheat sheet |
| Baseline simulation is possible but heavier. | 基線可模擬，但較笨重。 | Cheat sheet |
| Optimized runtime O(n). | 優化時間 O(n)。 | Cheat sheet |
| Optimized space O(1). | 優化空間 O(1)。 | Cheat sheet |
| Common bug: forgetting tie count term. | 常見錯誤：漏掉並列數項。 | Cheat sheet |
| Common bug: not taking max with tasks length. | 常見錯誤：沒與任務總數取 max。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Math/greedy formula approach is preserved.
- No hallucinated constraints: ✅ Uses source-defined task model and cooldown rule.
- Language simplicity: ✅ Clear spoken lines suitable for interview narration.
