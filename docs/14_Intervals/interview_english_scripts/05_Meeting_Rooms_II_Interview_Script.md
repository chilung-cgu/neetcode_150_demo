# 05 Meeting Rooms II — Interview English Script (C++)

> Source aligned with: `docs/14_Intervals/05_Meeting_Rooms_II.md`

> Quick links: [Source Solution](../05_Meeting_Rooms_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate meeting rooms two. | 我先重述 Meeting Rooms II。 | Restatement |
| We are given many meeting intervals. | 題目給多場會議區間。 | Restatement |
| We need the minimum number of rooms to host all meetings. | 要找容納全部會議所需的最少會議室數。 | Restatement |
| This equals the maximum number of overlapping meetings at any time. | 這等於任一時刻的最大同時重疊數。 | Restatement |
| We only need the count, not room assignments. | 只需回房間數，不需回分配細節。 | Restatement |
| I will use chronological ordering with two sorted arrays. | 我會用時間序排序法與雙陣列指標。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is intervals size up to ten thousand? | intervals 大小是否可到一萬？ | Clarify |
| Are all intervals valid with start less than end? | 區間是否都保證 start<end？ | Clarify |
| If one meeting ends exactly when another starts, can they share one room? | 若一場結束同時另一場開始，能否共用一間房？ | Clarify |
| Should I return integer room count only? | 是否只回傳整數房間數？ | Clarify |
| Is O(n log n) expected due to sorting? | 因排序而 O(n log n) 是否符合預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tracks overlaps for each meeting against many others. | 暴力法對每場會議和多場會議比較重疊。 | Approach |
| That quickly becomes O(n squared). | 這很快變成 O(n²)。 | Approach |
| We need a global timeline view instead. | 我們需要全域時間軸視角。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Split all start times and end times into two arrays. | 把所有 start 與 end 分成兩個陣列。 | Approach |
| Sort both arrays. | 兩個陣列都排序。 | Approach |
| Use pointer s for starts and e for ends with active room count. | 用 s 指 start、e 指 end，並維護 active room count。 | Approach |
| If start[s] is less than end[e], a new meeting begins before earliest end, so count increases. | 若 start[s] < end[e]，代表新會議先開始，房間數加一。 | Approach |
| Otherwise one meeting ended first, so count decreases and e moves forward. | 否則先有會議結束，房間數減一並前進 e。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If intervals is empty, return zero. | 若 intervals 為空，回傳 0。 | Coding |
| I collect all start times into starts array. | 我先收集所有開始時間到 starts。 | Coding |
| I collect all end times into ends array. | 再收集所有結束時間到 ends。 | Coding |
| I sort starts and ends separately. | 我分別排序 starts 與 ends。 | Coding |
| I initialize s and e pointers at zero. | 我把 s 和 e 初始為 0。 | Coding |
| I maintain current active count and maxRooms. | 維護目前 active count 與 maxRooms。 | Coding |
| If starts[s] is less than ends[e], I increment count and s. | 若 starts[s] < ends[e]，count++ 並 s++。 | Coding |
| Else I decrement count and move e. | 否則 count-- 並 e++。 | Coding |
| After each step, update maxRooms. | 每一步都更新 maxRooms。 | Coding |
| When s reaches n, return maxRooms. | 當 s 到 n 時回傳 maxRooms。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [[0,30],[5,10],[15,20]]. | 我手跑 [[0,30],[5,10],[15,20]]。 | Dry-run |
| starts is [0,5,15] and ends is [10,20,30]. | starts=[0,5,15]，ends=[10,20,30]。 | Dry-run |
| start zero is less than end ten, count becomes one. | start 0 < end 10，count 變 1。 | Dry-run |
| start five is less than end ten, count becomes two. | start 5 < end 10，count 變 2。 | Dry-run |
| start fifteen is not less than end ten, one meeting ends, count back to one. | start 15 不小於 end 10，先結束一場，count 回 1。 | Dry-run |
| Then start fifteen is less than end twenty, count becomes two again. | 接著 start 15 < end 20，count 又到 2。 | Dry-run |
| maxRooms observed is two, final answer is two. | 觀察到 maxRooms=2，最終答案為 2。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty intervals returns zero. | 案例一：空 intervals 回 0。 | Edge test |
| Case two: one meeting returns one. | 案例二：單一會議回 1。 | Edge test |
| Case three: non-overlapping meetings reuse one room. | 案例三：不重疊會議可重用一間房。 | Edge test |
| Case four: fully overlapping meetings need n rooms. | 案例四：完全重疊會議需要 n 間房。 | Edge test |
| Case five: boundary touch should reuse room. | 案例五：邊界相接應可重用房間。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log n). | 時間複雜度是 O(n log n)。 | Complexity |
| Space complexity is O(n). | 空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting starts and ends each takes O(n log n). | starts 與 ends 各自排序都要 O(n log n)。 | Complexity |
| The two-pointer scan is linear O(n). | 雙指標掃描是線性 O(n)。 | Complexity |
| Combined runtime remains O(n log n). | 合併後總時間仍是 O(n log n)。 | Complexity |
| Two extra arrays of size n give O(n) space. | 兩個大小 n 的陣列帶來 O(n) 空間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me switch to timeline event perspective. | 我改用時間軸事件觀點。 | If stuck |
| We only care about starts and ends ordering. | 我們只關心開始與結束的時間順序。 | If stuck |
| start before earliest end means one extra room. | 若開始早於最早結束，就需要多一間房。 | If stuck |
| end before next start means one room is freed. | 若先有結束，代表釋放一間房。 | If stuck |
| I maintain active count and global maximum. | 我維護 active 計數與全域最大值。 | If stuck |
| Let me test quickly with [7,10] and [2,4]. | 我快速測 [7,10] 與 [2,4]。 | If stuck |
| They do not overlap, so max is one room. | 它們不重疊，最大只需一間房。 | If stuck |
| This confirms boundary and ordering logic. | 這可確認排序與邊界邏輯。 | If stuck |
| Now pointer movement is clear. | 現在指標移動規則很清楚。 | If stuck |
| I can continue coding smoothly. | 我可以順利繼續實作。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with sorted starts and ends plus two pointers. | 我用排序後 starts/ends 加雙指標解題。 | Wrap-up |
| Active count tracks concurrent meetings. | active count 追蹤同時進行會議數。 | Wrap-up |
| Maximum active count is the room answer. | active 最大值就是所需會議室數。 | Wrap-up |
| Complexity is O(n log n) time and O(n) space. | 複雜度是 O(n log n) 時間、O(n) 空間。 | Wrap-up |
| This is a canonical timeline-sweep interview solution. | 這是面試常見的時間軸掃描標準解。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: minimum rooms for all meetings. | 目標：求全部會議最少房間數。 | Cheat sheet |
| Equivalent: max concurrent meetings. | 等價：最大同時會議數。 | Cheat sheet |
| Collect starts and ends arrays. | 建立 starts 與 ends。 | Cheat sheet |
| Sort both arrays. | 兩陣列都排序。 | Cheat sheet |
| s points to next start. | s 指向下一個開始。 | Cheat sheet |
| e points to earliest end. | e 指向最早結束。 | Cheat sheet |
| count tracks active rooms. | count 追蹤使用中房間。 | Cheat sheet |
| maxRooms tracks peak count. | maxRooms 追蹤峰值。 | Cheat sheet |
| If starts[s] < ends[e], count++. | 若 starts[s] < ends[e]，count++。 | Cheat sheet |
| Else count-- and e++. | 否則 count-- 並 e++。 | Cheat sheet |
| Advance s on each processed start. | 每處理一個 start 就前進 s。 | Cheat sheet |
| Update maxRooms each loop. | 每圈更新 maxRooms。 | Cheat sheet |
| Return maxRooms. | 回傳 maxRooms。 | Cheat sheet |
| Empty input returns 0. | 空輸入回 0。 | Cheat sheet |
| Boundary touch reuses room. | 邊界相接可重用房間。 | Cheat sheet |
| Time O(n log n). | 時間 O(n log n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Common bug: wrong inequality direction. | 常見錯誤：不等號方向寫錯。 | Cheat sheet |
| Common bug: forgetting maxRooms update. | 常見錯誤：忘記更新 maxRooms。 | Cheat sheet |
| Explain as sweep-line timeline. | 以掃描線時間軸方式說明。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Chronological ordering two-pointer method preserved.
- No hallucinated constraints: ✅ Reuse-at-boundary behavior aligned with source.
- Language simplicity: ✅ Interview-safe concise narration.
