# 01 Insert Interval — Interview English Script (C++)

> Source aligned with: `docs/14_Intervals/01_Insert_Interval.md`

> Quick links: [Source Solution](../01_Insert_Interval.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate insert interval. | 我先重述 Insert Interval。 | Restatement |
| We have a list of non-overlapping intervals sorted by start. | 題目給已排序且互不重疊的區間列表。 | Restatement |
| We need to insert one new interval. | 我們要插入一個新區間。 | Restatement |
| If overlaps happen, we must merge them. | 若有重疊就要合併。 | Restatement |
| Final output must stay sorted and non-overlapping. | 最後輸出仍要保持排序且不重疊。 | Restatement |
| I will solve it in one linear pass. | 我會用一次線性掃描完成。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is the input intervals array already sorted by start? | 輸入 intervals 是否已按起點排序？ | Clarify |
| Are existing intervals guaranteed non-overlapping initially? | 原本區間是否保證不重疊？ | Clarify |
| Can intervals be empty? | intervals 是否可能為空？ | Clarify |
| Should touching boundaries be merged, like [1,4] and [4,5]? | 邊界相接是否要合併，如 [1,4] 與 [4,5]？ | Clarify |
| Do we return a new array rather than modify in place strictly? | 是否回傳新陣列，不強制原地修改？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force appends new interval, sorts all intervals, then runs merge intervals. | 暴力作法是先加入新區間、排序，再做合併。 | Approach |
| This works but costs O(n log n) due to sorting. | 雖可行，但排序成本是 O(n log n)。 | Approach |
| We can do better because input is already sorted and disjoint. | 因輸入已排序且不重疊，我們可更快。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Phase one: add all intervals completely before newInterval. | 第一階段：先加入完全在 newInterval 左側的區間。 | Approach |
| Phase two: merge all intervals overlapping with newInterval by expanding start and end. | 第二階段：把與 newInterval 重疊者全部擴張合併。 | Approach |
| Push merged newInterval once overlaps are consumed. | 重疊處理完後一次加入合併後 newInterval。 | Approach |
| Phase three: append all remaining right-side intervals. | 第三階段：把右側剩餘區間直接附加。 | Approach |
| Total runtime is O(n) with one pass pointer. | 用單指標掃描，總時間 O(n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create result array and pointer i starting at zero. | 我先建立 result，並把指標 i 設為 0。 | Coding |
| While intervals[i].end is less than new start, I push intervals[i]. | 當 intervals[i].end < newStart，就先加入 intervals[i]。 | Coding |
| Next, while intervals[i].start is less than or equal to new end, I merge into newInterval. | 接著當 intervals[i].start <= newEnd，就合併進 newInterval。 | Coding |
| Merge updates new start as min and new end as max. | 合併時 newStart 取 min，newEnd 取 max。 | Coding |
| After overlap loop, I push merged newInterval. | 重疊迴圈結束後加入合併結果。 | Coding |
| Then I append all remaining intervals on the right. | 最後把右側剩餘區間全部附加。 | Coding |
| Return result. | 回傳 result。 | Coding |
| This preserves sorted non-overlapping property. | 這可維持排序與不重疊性質。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run intervals [[1,2],[3,5],[6,7],[8,10],[12,16]] with new interval [4,8]. | 我手跑 intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]、new=[4,8]。 | Dry-run |
| First [1,2] is strictly left, so it is appended directly. | [1,2] 完全在左側，直接加入。 | Dry-run |
| [3,5] overlaps, merged interval becomes [3,8]. | [3,5] 重疊後合併成 [3,8]。 | Dry-run |
| [6,7] overlaps, merged stays [3,8]. | [6,7] 重疊，合併仍是 [3,8]。 | Dry-run |
| [8,10] touches boundary and overlaps, merged becomes [3,10]. | [8,10] 邊界相接也重疊，合併成 [3,10]。 | Dry-run |
| Append merged [3,10], then append remaining [12,16]. | 加入合併後 [3,10]，再加剩餘 [12,16]。 | Dry-run |
| Final output is [[1,2],[3,10],[12,16]]. | 最終輸出 [[1,2],[3,10],[12,16]]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty intervals list. | 案例一：intervals 為空。 | Edge test |
| Case two: new interval goes fully before all intervals. | 案例二：new 完全在最左邊。 | Edge test |
| Case three: new interval goes fully after all intervals. | 案例三：new 完全在最右邊。 | Edge test |
| Case four: new interval covers all existing intervals. | 案例四：new 蓋住所有舊區間。 | Edge test |
| Case five: exact boundary touch merge. | 案例五：邊界相接合併。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(n) for output. | 空間複雜度是 O(n)，主要是輸出。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Pointer i moves from left to right once over intervals. | 指標 i 對 intervals 只由左到右走一次。 | Complexity |
| Each interval is appended or merged at most once. | 每個區間最多被加入或合併一次。 | Complexity |
| So total runtime is linear O(n). | 所以總時間是線性 O(n)。 | Complexity |
| Extra non-output memory is O(1), but returned result uses O(n). | 非輸出額外空間 O(1)，回傳結果本身是 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me split logic into left overlap and right phases. | 我先把流程拆成左、重疊、右三階段。 | If stuck |
| Left phase condition is interval end less than new start. | 左階段條件是 interval.end < new.start。 | If stuck |
| Overlap phase condition is interval start less than or equal to new end. | 重疊階段條件是 interval.start <= new.end。 | If stuck |
| During overlap I only expand newInterval bounds. | 重疊期間只擴張 newInterval 邊界。 | If stuck |
| Push merged newInterval once after overlap loop. | 重疊迴圈後一次加入合併結果。 | If stuck |
| Then append all remaining intervals unchanged. | 最後把其餘區間原樣附加。 | If stuck |
| Let me verify quickly with [[1,3],[6,9]] and [2,5]. | 我快速驗證 [[1,3],[6,9]] 與 [2,5]。 | If stuck |
| Merged middle should become [1,5]. | 中段合併應成 [1,5]。 | If stuck |
| Output should be [[1,5],[6,9]]. | 輸出應為 [[1,5],[6,9]]。 | If stuck |
| Great, phase boundaries are now clear. | 很好，三階段邊界已清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved insert interval with one-pass three-phase greedy merge. | 我用單趟三階段貪心合併解了 Insert Interval。 | Wrap-up |
| Existing sorted non-overlap property enables linear scan. | 原本已排序且不重疊特性讓線性掃描可行。 | Wrap-up |
| Overlaps are absorbed by expanding newInterval bounds. | 重疊區間透過擴張 newInterval 邊界吸收。 | Wrap-up |
| Complexity is O(n) time and O(n) output space. | 複雜度是 O(n) 時間與 O(n) 輸出空間。 | Wrap-up |
| This is the interview-optimal implementation. | 這是面試常見最優實作。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: insert new interval into sorted disjoint intervals. | 目標：把 new 插入已排序不重疊區間。 | Cheat sheet |
| Need sorted and non-overlapping output. | 輸出仍需排序且不重疊。 | Cheat sheet |
| Use one pointer scan. | 用單指標掃描。 | Cheat sheet |
| Phase 1: append left intervals with end < newStart. | 階段1：加入 end<newStart 的左區間。 | Cheat sheet |
| Phase 2: merge overlap intervals with start <= newEnd. | 階段2：合併 start<=newEnd 的重疊區間。 | Cheat sheet |
| newStart=min(newStart,curStart). | newStart=min(newStart,curStart)。 | Cheat sheet |
| newEnd=max(newEnd,curEnd). | newEnd=max(newEnd,curEnd)。 | Cheat sheet |
| Push merged new interval once. | 合併完一次加入 new。 | Cheat sheet |
| Phase 3: append remaining right intervals. | 階段3：加入右側剩餘區間。 | Cheat sheet |
| Return result. | 回傳結果。 | Cheat sheet |
| Handles boundary-touch as overlap. | 邊界相接視為重疊。 | Cheat sheet |
| Empty input returns [newInterval]. | 空輸入回 [newInterval]。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(n) due to output. | 空間 O(n) 主要因輸出。 | Cheat sheet |
| Common bug: wrong overlap condition strictness. | 常見錯誤：重疊條件嚴格號寫錯。 | Cheat sheet |
| Common bug: forgetting to push merged interval at end. | 常見錯誤：最後忘記加入合併後區間。 | Cheat sheet |
| Pointer only moves forward. | 指標只會向前移。 | Cheat sheet |
| No re-sort needed. | 不需要重新排序。 | Cheat sheet |
| Explain three phases clearly. | 清楚說明三階段流程。 | Cheat sheet |
| Validate before-after-all and cover-all cases. | 記得驗證前插、後插、全覆蓋案例。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ One-pass three-phase merge logic preserved.
- No hallucinated constraints: ✅ Sorted/disjoint input assumptions and boundary-merge semantics maintained.
- Language simplicity: ✅ Interview-ready stepwise explanation.
