# 02 Merge Intervals — Interview English Script (C++)

> Source aligned with: `docs/14_Intervals/02_Merge_Intervals.md`

> Quick links: [Source Solution](../02_Merge_Intervals.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate merge intervals. | 我先重述 Merge Intervals。 | Restatement |
| We are given a list of intervals [start, end]. | 題目給一組區間 [start,end]。 | Restatement |
| Some intervals overlap and should be merged. | 有些區間重疊，需合併。 | Restatement |
| Final output should contain non-overlapping merged intervals. | 輸出要是互不重疊的合併結果。 | Restatement |
| Intervals touching at boundaries are considered overlapping here. | 本題邊界相接也視為重疊。 | Restatement |
| I will sort by start and merge in one scan. | 我會先按起點排序，再單趟合併。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is input size up to ten thousand intervals? | 輸入上限是否約一萬個區間？ | Clarify |
| Should touching intervals like [1,4] and [4,5] merge? | [1,4] 與 [4,5] 這種相接是否要合併？ | Clarify |
| Are interval bounds always valid start less than or equal to end? | 區間是否保證 start<=end？ | Clarify |
| Do we return merged list in sorted order by start? | 是否要按起點排序回傳合併結果？ | Clarify |
| Is O(n log n) expected due to sorting? | 是否預期 O(n log n)（因排序）？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force compares each interval with many others repeatedly. | 暴力法會反覆把每區間和其他區間比較。 | Approach |
| Re-merging and rescanning leads to high overhead. | 重複合併與重掃會造成高成本。 | Approach |
| Sorting-based greedy is cleaner and optimal. | 排序後貪心更乾淨且最優。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sort intervals by start value first. | 先按起點排序區間。 | Approach |
| Keep the last merged interval in result. | 在結果中維護最後一個已合併區間。 | Approach |
| If current start is less than or equal to last end, merge by updating last end. | 若當前起點 <= 最後終點，就更新終點進行合併。 | Approach |
| Otherwise push current interval as a new segment. | 否則把當前區間當新段加入。 | Approach |
| One pass after sorting produces final answer. | 排序後單次掃描即可完成。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I handle empty input by returning empty list. | 空輸入直接回空列表。 | Coding |
| I sort intervals ascending by start. | 我先把區間按起點遞增排序。 | Coding |
| I push the first interval into result. | 先把第一個區間放進 result。 | Coding |
| For each next interval, I compare with result.back(). | 對每個後續區間，和 result.back() 比較。 | Coding |
| If overlap exists, update back end to max(back end, current end). | 若重疊，更新尾端為兩者終點最大值。 | Coding |
| If no overlap, append current interval. | 若不重疊，直接附加當前區間。 | Coding |
| Continue until all intervals processed. | 持續直到所有區間處理完。 | Coding |
| Return result as merged intervals. | 回傳 result 作合併結果。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [[1,3],[2,6],[8,10],[15,18]]. | 我手跑 [[1,3],[2,6],[8,10],[15,18]]。 | Dry-run |
| After sorting, order stays the same. | 排序後順序不變。 | Dry-run |
| Start result with [1,3]. | result 先放 [1,3]。 | Dry-run |
| Next [2,6] overlaps, so merge to [1,6]. | 下一個 [2,6] 重疊，合併成 [1,6]。 | Dry-run |
| [8,10] does not overlap, append it. | [8,10] 不重疊，直接加入。 | Dry-run |
| [15,18] also does not overlap, append it. | [15,18] 也不重疊，直接加入。 | Dry-run |
| Final output is [[1,6],[8,10],[15,18]]. | 最終輸出 [[1,6],[8,10],[15,18]]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single interval only. | 案例一：只有一個區間。 | Edge test |
| Case two: all intervals already disjoint. | 案例二：所有區間本來就不重疊。 | Edge test |
| Case three: all intervals chain-overlap into one. | 案例三：全部鏈式重疊成一段。 | Edge test |
| Case four: boundary-touch intervals like [1,4] and [4,5]. | 案例四：邊界相接如 [1,4] 和 [4,5]。 | Edge test |
| Case five: unsorted input requiring proper sort first. | 案例五：未排序輸入需先排序。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log n). | 時間複雜度是 O(n log n)。 | Complexity |
| Space complexity is O(n) for output. | 空間複雜度是 O(n)，主要來自輸出。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting intervals dominates with O(n log n). | 排序成本主導，為 O(n log n)。 | Complexity |
| Merge scan afterward is linear O(n). | 之後合併掃描是線性 O(n)。 | Complexity |
| Combined complexity remains O(n log n). | 合併後總複雜度仍是 O(n log n)。 | Complexity |
| Result list stores up to n intervals in worst case. | 最壞情況結果可存 n 個區間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me ensure sorting by start happens first. | 我先確認一定先按起點排序。 | If stuck |
| I only compare current interval with last merged interval. | 我只需比較當前區間與最後已合併區間。 | If stuck |
| Overlap condition is current start less than or equal to last end. | 重疊條件是當前起點 <= 最後終點。 | If stuck |
| If overlap, update end with max value. | 若重疊，用 max 更新終點。 | If stuck |
| If not overlap, push as new merged block. | 若不重疊，就當新區塊加入。 | If stuck |
| Let me test quickly with [1,4] and [4,5]. | 我快速測 [1,4] 與 [4,5]。 | If stuck |
| They should merge into [1,5]. | 它們應合併成 [1,5]。 | If stuck |
| That confirms boundary-touch rule. | 這可確認邊界相接規則。 | If stuck |
| Keep result.back reference updated correctly. | 要確保 result.back 引用更新正確。 | If stuck |
| Great, merge flow is consistent. | 很好，合併流程一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved merge intervals by sorting then greedy merging. | 我用先排序再貪心合併解了 Merge Intervals。 | Wrap-up |
| We maintain one active merged interval in result. | 我們在結果中維護一個活躍合併區間。 | Wrap-up |
| Overlap extends end, non-overlap starts a new block. | 重疊延伸終點，不重疊開新區塊。 | Wrap-up |
| Complexity is O(n log n) time and O(n) output space. | 複雜度是 O(n log n) 時間與 O(n) 輸出空間。 | Wrap-up |
| This is the canonical interval merging pattern. | 這是區間題經典合併範式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: merge overlapping intervals. | 目標：合併所有重疊區間。 | Cheat sheet |
| Sort intervals by start first. | 先按起點排序。 | Cheat sheet |
| Initialize result with first interval. | result 先放第一段。 | Cheat sheet |
| Iterate remaining intervals. | 迭代其餘區間。 | Cheat sheet |
| Let last = result.back(). | 令 last=result.back()。 | Cheat sheet |
| Overlap if cur.start <= last.end. | 若 cur.start<=last.end 則重疊。 | Cheat sheet |
| Merge: last.end=max(last.end,cur.end). | 合併：last.end=max(last.end,cur.end)。 | Cheat sheet |
| Else append current interval. | 否則附加當前區間。 | Cheat sheet |
| Return result. | 回傳 result。 | Cheat sheet |
| [1,3],[2,6] -> [1,6]. | [1,3],[2,6] -> [1,6]。 | Cheat sheet |
| Boundary touch merges too. | 邊界相接也要合併。 | Cheat sheet |
| Single interval unchanged. | 單一區間不變。 | Cheat sheet |
| Time O(n log n). | 時間 O(n log n)。 | Cheat sheet |
| Scan part is O(n). | 掃描部分是 O(n)。 | Cheat sheet |
| Space O(n) output. | 空間 O(n)（輸出）。 | Cheat sheet |
| Common bug: wrong overlap strictness. | 常見錯誤：重疊條件嚴格號寫錯。 | Cheat sheet |
| Common bug: forgetting to sort first. | 常見錯誤：忘記先排序。 | Cheat sheet |
| Keep in-place update of last interval. | 直接更新最後區間終點。 | Cheat sheet |
| Mention relation to Insert Interval. | 可提與 Insert Interval 的關聯。 | Cheat sheet |
| Validate with chain-overlap input. | 用鏈式重疊案例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sort-and-scan merge pattern preserved.
- No hallucinated constraints: ✅ Overlap semantics including boundary-touch maintained.
- Language simplicity: ✅ Clear, interview-oriented merge narrative.
