# 06 Time Based Key-Value Store — Interview English Script (C++)

> Source aligned with: `docs/05_Binary_Search/06_Time_Based_Key_Value_Store.md`

> Quick links: [Source Solution](../06_Time_Based_Key_Value_Store.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the TimeMap design task. | 我先重述 TimeMap 設計題。 | Restatement |
| We need set and get operations with timestamps. | 我們要支援帶 timestamp 的 set/get。 | Restatement |
| set stores value at an increasing timestamp for a key. | set 會為 key 以遞增時間存值。 | Restatement |
| get should return the latest value with time less-equal query time. | get 要回傳不超過查詢時間的最新值。 | Restatement |
| If no such value exists, return empty string. | 若不存在，回傳空字串。 | Restatement |
| I will use hash map plus binary search per key history. | 我會用 hash map 加每個 key 的二分查找。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I rely on strictly increasing timestamps for each set call globally? | 我可依賴 set 的時間戳嚴格遞增嗎？ | Clarify |
| Should get return empty string when key does not exist? | key 不存在時 get 應回傳空字串嗎？ | Clarify |
| Is key lookup expected average O(1) via hash map? | key 查找預期是 hash map 平均 O(1) 嗎？ | Clarify |
| Do we need thread safety in this interview version? | 這題是否需要考慮執行緒安全？ | Clarify |
| Is memory optimization discussion a follow-up only? | 記憶體優化是 follow-up 再談即可嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline stores all pairs and linearly scans on every get. | 基線是存所有 pair，get 時線性掃描。 | Approach |
| For each get, pick maximum timestamp not exceeding query. | 每次 get 挑出不超過 query 的最大 timestamp。 | Approach |
| That makes get O(N) per key history length. | 這讓 get 對該 key 變成 O(N)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For each key, maintain vector of (timestamp, value). | 每個 key 維護 (timestamp,value) 向量。 | Approach |
| Because timestamps increase, each vector is naturally sorted. | 因 timestamp 遞增，所以向量天然有序。 | Approach |
| On get, binary search latest timestamp <= query time. | get 時二分找 <= query 的最新 timestamp。 | Approach |
| Keep best candidate and continue to the right. | 保留候選值並繼續往右找更近者。 | Approach |
| set is O(1) append; get is O(log N). | set 是 O(1) append；get 是 O(log N)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create a hash map from key to history vector. | 先建立 key 到歷史向量的 hash map。 | Coding |
| In set, I append {timestamp, value} to that key list. | set 時把 {timestamp,value} 追加進列表。 | Coding |
| In get, I return empty string if key does not exist. | get 時若 key 不存在就回傳空字串。 | Coding |
| Otherwise I binary search that key history vector. | 否則對該 key 的歷史向量做二分。 | Coding |
| If history[mid].time <= query, record value and move left bound up. | 若 mid 時間 <= query，記錄值並提升 left。 | Coding |
| Else move right bound down. | 否則降低 right。 | Coding |
| After loop, return recorded value candidate. | 迴圈結束回傳記錄的候選值。 | Coding |
| This guarantees nearest timestamp from the left side. | 這可保證拿到左側最近 timestamp。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run operations set foo bar 1, get foo 1, get foo 3, set foo bar2 4, get foo 4, get foo 5. | 我手跑 set/get 範例序列。 | Dry-run |
| After first set, history for foo is [(1, bar)]. | 第一次 set 後，foo 歷史是 [(1,bar)]。 | Dry-run |
| get at time 1 returns bar directly. | time=1 的 get 直接回傳 bar。 | Dry-run |
| get at time 3 still returns bar as latest <=3. | time=3 的 get 仍回傳 bar。 | Dry-run |
| After second set, history is [(1, bar), (4, bar2)]. | 第二次 set 後歷史變 [(1,bar),(4,bar2)]。 | Dry-run |
| get at 4 returns bar2, and get at 5 also returns bar2. | get(4) 回 bar2，get(5) 也回 bar2。 | Dry-run |
| Outputs match expected behavior. | 輸出符合預期行為。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: get on missing key. | 案例一：對不存在 key 做 get。 | Edge test |
| Case two: query timestamp before first set timestamp. | 案例二：查詢時間早於第一筆 set。 | Edge test |
| Case three: query timestamp exactly equals a stored timestamp. | 案例三：查詢時間剛好命中某筆。 | Edge test |
| Case four: query timestamp between two stored timestamps. | 案例四：查詢時間落在兩筆中間。 | Edge test |
| Case five: many sets on one key and late query. | 案例五：單 key 多筆 set 且晚時間查詢。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| set is O(1) average, get is O(log N) for one key history. | set 平均 O(1)，get 對單 key 是 O(log N)。 | Complexity |
| Overall extra space is O(total set calls). | 整體額外空間是 O(所有 set 次數)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Hash map lookup is average O(1) per operation. | hash map 查找每次平均 O(1)。 | Complexity |
| set only appends to tail because timestamps are increasing. | set 因時間遞增只需尾端追加。 | Complexity |
| get performs binary search on that key-specific timeline. | get 在該 key 時間線上做二分。 | Complexity |
| Stored entries are linear in total number of sets. | 儲存量與 set 總次數線性相關。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me confirm why binary search is valid here. | 我先確認為何這裡可用二分。 | If stuck |
| It works because timestamps are strictly increasing. | 因為 timestamps 嚴格遞增。 | If stuck |
| I am searching for rightmost time <= query. | 我在找最右邊 <= query 的時間。 | If stuck |
| I should keep a candidate whenever condition holds. | 條件成立時要保留候選值。 | If stuck |
| Then move left bound to mid plus one. | 然後把 left 移到 mid+1。 | If stuck |
| If timestamp is too large, move right to mid minus one. | 若時間太大，right 移到 mid-1。 | If stuck |
| Let me recheck missing-key and empty-string behavior. | 我重檢缺 key 與空字串回傳。 | If stuck |
| I found an off-by-one in bounds update. | 我找到一個邊界 off-by-one。 | If stuck |
| I fixed it and reran the sample sequence. | 我修好後重跑範例序列。 | If stuck |
| Now all get outputs are correct. | 現在所有 get 輸出都正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed the TimeMap design and implementation. | 我完成 TimeMap 設計與實作。 | Wrap-up |
| I verified exact-hit and nearest-left retrieval behavior. | 我驗證了精準命中與左側最近值行為。 | Wrap-up |
| set is O(1) average and get is O(log N). | set 平均 O(1)，get 是 O(log N)。 | Wrap-up |
| Space is linear in total stored entries. | 空間與儲存總筆數線性成長。 | Wrap-up |
| I can discuss upper_bound library version as well. | 我也可補充 upper_bound 寫法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Design TimeMap with set/get by time. | 設計含時間的 TimeMap set/get。 | Cheat sheet |
| get needs latest timestamp <= query. | get 要最新且 <= query 的值。 | Cheat sheet |
| Missing key returns empty string. | key 不存在回空字串。 | Cheat sheet |
| Baseline get scans all entries O(N). | 基線 get 線掃 O(N)。 | Cheat sheet |
| Use hash map from key to timeline vector. | 用 key 到時間線向量的 hash map。 | Cheat sheet |
| Timeline stores (timestamp, value). | 時間線元素為 (timestamp,value)。 | Cheat sheet |
| set appends because timestamps increase. | set 因遞增時間可直接 append。 | Cheat sheet |
| get uses binary search on timeline. | get 在時間線上做二分。 | Cheat sheet |
| Track best candidate when time <= query. | time<=query 時更新候選值。 | Cheat sheet |
| Move left = mid + 1 then. | 然後 left=mid+1。 | Cheat sheet |
| Else move right = mid - 1. | 否則 right=mid-1。 | Cheat sheet |
| Return candidate after loop. | 迴圈後回傳候選值。 | Cheat sheet |
| set average O(1). | set 平均 O(1)。 | Cheat sheet |
| get O(log N) per key history. | get 對單 key 是 O(log N)。 | Cheat sheet |
| Space O(total set calls). | 空間 O(set 總次數)。 | Cheat sheet |
| Test missing-key get case. | 測缺 key 的 get。 | Cheat sheet |
| Test query before first timestamp. | 測查詢早於第一筆時間。 | Cheat sheet |
| Test exact timestamp hit. | 測精準時間命中。 | Cheat sheet |
| Test between-two-timestamps case. | 測兩時間點之間查詢。 | Cheat sheet |
| Common bug: off-by-one in binary search. | 常見 bug：二分邊界 off-by-one。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hash map + binary search timeline design is preserved.
- No hallucinated constraints: ✅ Uses strict-increasing timestamp property from source.
- Language simplicity: ✅ Interview-friendly short spoken lines.
