# 04 Meeting Rooms — Interview English Script (C++)

> Source aligned with: `docs/14_Intervals/04_Meeting_Rooms.md`

> Quick links: [Source Solution](../04_Meeting_Rooms.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate meeting rooms. | 我先重述 Meeting Rooms。 | Restatement |
| We are given meeting intervals with start and end times. | 題目給會議區間的開始與結束時間。 | Restatement |
| We need to check if one person can attend all meetings. | 要判斷一個人是否可參加全部會議。 | Restatement |
| That means no two meetings can overlap in time. | 也就是任兩場會議不能時間重疊。 | Restatement |
| If any overlap exists, answer is false. | 只要有重疊，答案就是 false。 | Restatement |
| I will sort by start and scan neighbors. | 我會先按起點排序，再掃相鄰區間。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is intervals length possibly zero? | intervals 長度是否可能為 0？ | Clarify |
| Are intervals guaranteed valid with start less than end? | 區間是否保證 start 小於 end？ | Clarify |
| Is boundary touch allowed, like end equals next start? | 邊界相接是否可接受，如 end==nextStart？ | Clarify |
| Should I return boolean only, not conflict pair indices? | 是否只回布林值，不需回衝突索引？ | Clarify |
| Is O(n log n) sorting approach acceptable? | O(n log n) 排序法是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks every pair of meetings. | 暴力法比較每一對會議。 | Approach |
| If any pair overlaps, return false. | 若任一對重疊就回 false。 | Approach |
| This costs O(n squared). | 此作法成本是 O(n²)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sort intervals by start time. | 先按起始時間排序。 | Approach |
| Then only adjacent intervals can create first visible conflict in order. | 排序後只需看相鄰區間是否衝突。 | Approach |
| For each i, if intervals[i].end is greater than intervals[i+1].start, overlap exists. | 對每個 i，若 end[i] > start[i+1] 則重疊。 | Approach |
| In that case return false immediately. | 發生時可立即回 false。 | Approach |
| If scan completes, return true. | 掃描完沒有衝突就回 true。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If intervals is empty, I return true. | 若 intervals 為空，我回傳 true。 | Coding |
| I sort intervals in ascending order by start. | 我先把 intervals 依起點遞增排序。 | Coding |
| I loop i from zero to size minus two. | 我讓 i 從 0 走到 size-2。 | Coding |
| I compare current end with next start. | 比較目前區間終點與下一段起點。 | Coding |
| If current end is greater, meetings overlap. | 若目前終點較大，表示會議重疊。 | Coding |
| I return false as soon as overlap appears. | 一旦重疊立刻回傳 false。 | Coding |
| Otherwise continue checking next pair. | 否則繼續檢查下一對。 | Coding |
| After loop, I return true. | 迴圈結束後回傳 true。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [[0,30],[5,10],[15,20]]. | 我手跑 [[0,30],[5,10],[15,20]]。 | Dry-run |
| Sorted order is unchanged. | 排序後順序不變。 | Dry-run |
| Compare [0,30] and [5,10]. | 先比 [0,30] 與 [5,10]。 | Dry-run |
| Since thirty is greater than five, overlap exists. | 因為 30 > 5，出現重疊。 | Dry-run |
| So function returns false immediately. | 因此函式立即回傳 false。 | Dry-run |
| We do not need to check further pairs. | 後面配對就不必再檢查。 | Dry-run |
| Final answer is false. | 最終答案是 false。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty intervals returns true. | 案例一：空 intervals 回 true。 | Edge test |
| Case two: single meeting always returns true. | 案例二：單一會議必為 true。 | Edge test |
| Case three: boundary touch [2,4] then [4,7] should return true. | 案例三：邊界相接 [2,4]、[4,7] 應回 true。 | Edge test |
| Case four: exact overlap should return false. | 案例四：明顯重疊應回 false。 | Edge test |
| Case five: unsorted input still works after sorting. | 案例五：未排序輸入經排序後仍正確。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log n). | 時間複雜度是 O(n log n)。 | Complexity |
| Space complexity is O(1) extra excluding sort stack details. | 額外空間約 O(1)，不含排序堆疊細節。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting by start dominates at O(n log n). | 依起點排序主導成本，為 O(n log n)。 | Complexity |
| Neighbor scan is linear O(n). | 相鄰掃描為線性 O(n)。 | Complexity |
| Total runtime is O(n log n). | 總時間複雜度是 O(n log n)。 | Complexity |
| Additional variables are constant space. | 附加變數為常數空間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me simplify to overlap detection after sorting. | 我先簡化成排序後的重疊檢測。 | If stuck |
| I only need to compare adjacent meetings. | 我只要比較相鄰會議。 | If stuck |
| Overlap condition is prev end greater than next start. | 重疊條件是前段 end > 後段 start。 | If stuck |
| If overlap occurs, answer is immediately false. | 一旦重疊，答案立即是 false。 | If stuck |
| If no pair overlaps, answer is true. | 若沒有任何重疊配對，答案是 true。 | If stuck |
| Let me validate with [7,10] and [2,4]. | 我用 [7,10] 與 [2,4] 快速驗證。 | If stuck |
| After sorting, [2,4] then [7,10] has no overlap. | 排序後 [2,4] 再 [7,10]，沒有重疊。 | If stuck |
| So that case returns true. | 所以該案例回 true。 | If stuck |
| Boundary touch should also be okay. | 邊界相接也應視為可排。 | If stuck |
| Great, logic is stable now. | 很好，邏輯已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it by sorting and checking adjacent overlaps. | 我用排序加相鄰重疊檢查解題。 | Wrap-up |
| Early return false handles conflicts efficiently. | 提早回 false 可高效處理衝突。 | Wrap-up |
| If no conflict appears, return true. | 若未出現衝突，就回 true。 | Wrap-up |
| Complexity is O(n log n) time and O(1) extra space. | 複雜度是 O(n log n) 時間、O(1) 額外空間。 | Wrap-up |
| This is the standard interview solution. | 這是面試的標準解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: check if one person can attend all meetings. | 目標：判斷是否可參加所有會議。 | Cheat sheet |
| Input is intervals [start,end]. | 輸入是區間 [start,end]。 | Cheat sheet |
| Need no overlaps. | 需要不存在重疊。 | Cheat sheet |
| Sort by start time first. | 先依起點排序。 | Cheat sheet |
| Scan adjacent pairs. | 掃描相鄰配對。 | Cheat sheet |
| Overlap if end[i] > start[i+1]. | 若 end[i] > start[i+1] 即重疊。 | Cheat sheet |
| On overlap return false. | 有重疊就回 false。 | Cheat sheet |
| If scan ends return true. | 掃描結束就回 true。 | Cheat sheet |
| Empty input returns true. | 空輸入回 true。 | Cheat sheet |
| Single interval returns true. | 單一區間回 true。 | Cheat sheet |
| Boundary touch is allowed. | 邊界相接可接受。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法是 O(n²)。 | Cheat sheet |
| Optimized is O(n log n). | 優化法是 O(n log n)。 | Cheat sheet |
| Neighbor scan is O(n). | 相鄰掃描是 O(n)。 | Cheat sheet |
| Extra space O(1). | 額外空間 O(1)。 | Cheat sheet |
| Common bug: using >= instead of >. | 常見錯誤：把 > 寫成 >=。 | Cheat sheet |
| Common bug: forgetting to sort first. | 常見錯誤：忘記先排序。 | Cheat sheet |
| Example [0,30],[5,10] conflicts. | 例 [0,30],[5,10] 有衝突。 | Cheat sheet |
| Return type is boolean. | 回傳型別是布林值。 | Cheat sheet |
| Explain with one quick dry run. | 用一個快手跑說明。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sort + adjacent conflict scan preserved.
- No hallucinated constraints: ✅ Boundary-touch interpretation follows source.
- Language simplicity: ✅ Concise interview-safe wording.
