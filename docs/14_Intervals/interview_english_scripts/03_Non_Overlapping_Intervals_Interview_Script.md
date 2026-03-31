# 03 Non-overlapping Intervals — Interview English Script (C++)

> Source aligned with: `docs/14_Intervals/03_Non_Overlapping_Intervals.md`

> Quick links: [Source Solution](../03_Non_Overlapping_Intervals.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate non-overlapping intervals. | 我先重述 Non-overlapping Intervals。 | Restatement |
| We are given intervals with start and end times. | 題目給一組有起訖時間的區間。 | Restatement |
| We want to remove the minimum number of intervals. | 我們要移除最少數量的區間。 | Restatement |
| After removals, remaining intervals must be non-overlapping. | 移除後剩餘區間必須互不重疊。 | Restatement |
| Equivalent view is maximizing how many intervals we keep. | 等價目標是盡量保留最多區間。 | Restatement |
| I will solve it with greedy after sorting. | 我會用排序後的貪心法解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are intervals represented as closed ranges [start, end]? | 區間是否以閉區間 [start,end] 表示？ | Clarify |
| Is touching boundary non-overlap, like [1,2] and [2,3]? | 邊界相接是否算不重疊，如 [1,2] 與 [2,3]？ | Clarify |
| Is input size up to one hundred thousand? | 輸入大小是否可到十萬？ | Clarify |
| Can starts and ends be negative values? | 起訖值是否可能為負？ | Clarify |
| Should we return count only, not the kept intervals list? | 是否只回移除數量，不需回保留清單？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries many removal combinations. | 暴力法會嘗試多種移除組合。 | Approach |
| That is exponential and infeasible for large n. | 這是指數級，對大 n 不可行。 | Approach |
| We need a greedy scheduling strategy. | 我們需要區間排程型貪心策略。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sort intervals by start time. | 先按起點排序區間。 | Approach |
| Track prevEnd of the interval we decide to keep. | 追蹤目前保留區間的 prevEnd。 | Approach |
| If current start is less than prevEnd, overlap occurs and we remove one. | 若 current.start < prevEnd，表示重疊，要移除一個。 | Approach |
| Greedy choice keeps the interval with smaller end using prevEnd = min(prevEnd, currentEnd). | 貪心上保留終點較小者：prevEnd=min(prevEnd,currentEnd)。 | Approach |
| This maximizes room for future intervals and minimizes removals. | 這可留給後續更多空間，達成最少移除。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I sort intervals by start ascending. | 我先把 intervals 按起點遞增排序。 | Coding |
| I initialize removal count as zero. | 移除計數初始化為 0。 | Coding |
| I set prevEnd to the first interval end. | 我把 prevEnd 設成第一段的終點。 | Coding |
| For each next interval, I compare current start with prevEnd. | 對每個後續區間，比較 current.start 與 prevEnd。 | Coding |
| If overlap exists, increment removal count. | 若重疊，移除計數加一。 | Coding |
| On overlap, keep smaller end by updating prevEnd with min. | 發生重疊時，用 min 更新 prevEnd 保留較小終點。 | Coding |
| If no overlap, move prevEnd to current end. | 若不重疊，就把 prevEnd 更新為 current.end。 | Coding |
| After scan, return removal count. | 掃描結束後回傳移除數。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [[1,2],[2,3],[3,4],[1,3]]. | 我手跑 [[1,2],[2,3],[3,4],[1,3]]。 | Dry-run |
| Sorted order is [[1,2],[1,3],[2,3],[3,4]]. | 排序後是 [[1,2],[1,3],[2,3],[3,4]]。 | Dry-run |
| Start with prevEnd two and removals zero. | 初始 prevEnd=2、removals=0。 | Dry-run |
| [1,3] overlaps because one is less than two, removals becomes one, prevEnd stays two. | [1,3] 因 1<2 重疊，removals=1，prevEnd 保持 2。 | Dry-run |
| [2,3] does not overlap because two is not less than two, set prevEnd three. | [2,3] 因 2 不小於 2 不重疊，prevEnd 變 3。 | Dry-run |
| [3,4] also does not overlap, set prevEnd four. | [3,4] 也不重疊，prevEnd 變 4。 | Dry-run |
| Final answer is one removal. | 最終答案是移除 1 個。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single interval returns zero. | 案例一：單一區間回 0。 | Edge test |
| Case two: all intervals already non-overlapping. | 案例二：全部本來就不重疊。 | Edge test |
| Case three: all intervals identical, remove n minus one. | 案例三：全部相同區間，需移除 n-1。 | Edge test |
| Case four: chain overlap requires repeated greedy min-end updates. | 案例四：鏈式重疊需多次使用最小終點更新。 | Edge test |
| Case five: boundary touch like [1,2] and [2,3] should be allowed together. | 案例五：邊界相接如 [1,2] 與 [2,3] 可同時保留。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log n). | 時間複雜度是 O(n log n)。 | Complexity |
| Space complexity is O(1) extra excluding sort stack details. | 額外空間複雜度約 O(1)，不含排序堆疊細節。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting dominates runtime with O(n log n). | 排序主導時間，為 O(n log n)。 | Complexity |
| The single pass after sorting is O(n). | 排序後單次掃描是 O(n)。 | Complexity |
| Total complexity remains O(n log n). | 總複雜度仍為 O(n log n)。 | Complexity |
| Extra variables are constant, so additional memory is O(1). | 額外變數是常數，因此附加空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me reframe as keep maximum non-overlapping intervals. | 我改用「保留最多不重疊區間」來思考。 | If stuck |
| Remove minimum equals total minus kept maximum. | 最少移除等於總數減最多保留。 | If stuck |
| Overlap condition is current start less than prevEnd. | 重疊條件是 current.start < prevEnd。 | If stuck |
| On overlap, I must remove one interval. | 發生重疊時，必須移除其中一段。 | If stuck |
| Greedy keeps the interval ending earlier. | 貪心策略是保留結束更早的區間。 | If stuck |
| That means prevEnd becomes min of two ends. | 所以 prevEnd 取兩者終點的最小值。 | If stuck |
| Let me verify quickly with [1,2],[1,3]. | 我快速驗證 [1,2],[1,3]。 | If stuck |
| Keeping [1,2] is better for future intervals. | 保留 [1,2] 對後續更有利。 | If stuck |
| This confirms the greedy choice. | 這驗證了貪心選擇正確。 | If stuck |
| Now I can code confidently. | 現在可以有把握地實作。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with sorting plus greedy end control. | 我用排序加貪心終點控制解題。 | Wrap-up |
| Each overlap forces one removal decision. | 每次重疊都迫使一次移除決策。 | Wrap-up |
| Keeping smaller end is the key local optimum. | 保留較小終點是關鍵局部最優。 | Wrap-up |
| Complexity is O(n log n) time and O(1) extra space. | 複雜度是 O(n log n) 時間、O(1) 額外空間。 | Wrap-up |
| This is the interview-standard greedy proof pattern. | 這是面試常見的貪心證明模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: remove minimum intervals to avoid overlap. | 目標：最少移除使區間不重疊。 | Cheat sheet |
| Equivalent: keep maximum non-overlapping intervals. | 等價：保留最多不重疊區間。 | Cheat sheet |
| Sort by start ascending. | 先按起點排序。 | Cheat sheet |
| removals = 0. | removals 初值 0。 | Cheat sheet |
| prevEnd = first interval end. | prevEnd 設為第一段終點。 | Cheat sheet |
| For each interval from second onward. | 從第二段開始逐一掃描。 | Cheat sheet |
| If start < prevEnd, overlap. | 若 start < prevEnd，即重疊。 | Cheat sheet |
| On overlap: removals++. | 重疊時：removals++。 | Cheat sheet |
| Keep smaller end: prevEnd=min(prevEnd,end). | 保留較小終點：prevEnd=min(prevEnd,end)。 | Cheat sheet |
| Else set prevEnd=end. | 否則 prevEnd=end。 | Cheat sheet |
| Return removals. | 回傳 removals。 | Cheat sheet |
| Touching boundary is non-overlap. | 邊界相接視為不重疊。 | Cheat sheet |
| Example [[1,2],[1,3]] remove one. | 例 [[1,2],[1,3]] 要移除一個。 | Cheat sheet |
| Time O(n log n). | 時間 O(n log n)。 | Cheat sheet |
| Scan part O(n). | 掃描部分 O(n)。 | Cheat sheet |
| Extra space O(1). | 額外空間 O(1)。 | Cheat sheet |
| Common bug: wrong overlap strictness. | 常見錯誤：重疊條件嚴格號寫錯。 | Cheat sheet |
| Common bug: keeping larger end by mistake. | 常見錯誤：誤保留較大終點。 | Cheat sheet |
| Explain greedy reason clearly. | 清楚說明貪心理由。 | Cheat sheet |
| Validate with chain-overlap case. | 用鏈式重疊案例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sort-by-start + min-end greedy preserved.
- No hallucinated constraints: ✅ Boundary-touch non-overlap rule respected.
- Language simplicity: ✅ Clear interview-ready progression.
