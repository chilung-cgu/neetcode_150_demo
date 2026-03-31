# 06 Minimum Interval to Include Each Query — Interview English Script (C++)

> Source aligned with: `docs/14_Intervals/06_Minimum_Interval.md`

> Quick links: [Source Solution](../06_Minimum_Interval.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate minimum interval for each query. | 我先重述每個查詢的最小區間問題。 | Restatement |
| We have many intervals and many query values. | 題目給很多區間與很多查詢值。 | Restatement |
| For each query q, we need the shortest interval that contains q. | 對每個 q，要找包含 q 的最短區間。 | Restatement |
| Interval length is right minus left plus one. | 區間長度定義為 right-left+1。 | Restatement |
| If no interval covers q, answer is minus one. | 若沒有區間覆蓋 q，答案是 -1。 | Restatement |
| I will use sorting plus a min-heap sweep line. | 我會用排序加最小堆掃描線。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can intervals and queries each be as large as one hundred thousand? | intervals 與 queries 是否都可到十萬？ | Clarify |
| Are interval bounds inclusive on both sides? | 區間左右邊界是否都包含？ | Clarify |
| Should duplicate query values reuse same computed answer? | 重複查詢值是否可重用同一答案？ | Clarify |
| Must output keep original query order? | 輸出是否必須保持原始 query 順序？ | Clarify |
| Is O((n plus q) log n) style solution expected? | 是否預期 O((n+q)logn) 等級解法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks every interval for every query. | 暴力法對每個 query 檢查所有區間。 | Approach |
| Keep minimum valid length per query. | 每個 query 保留最小合法長度。 | Approach |
| This is O(n times q), too slow. | 這是 O(n*q)，太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sort intervals by left endpoint. | 先按左端點排序 intervals。 | Approach |
| Sort queries by value, but store original indices. | queries 依值排序，但保留原索引。 | Approach |
| Sweep queries from small to large; push intervals with left less than or equal to q into min-heap. | 由小到大掃 query，把 left<=q 的區間推進最小堆。 | Approach |
| Heap stores pair of interval length and interval right endpoint. | 堆中存 (區間長度, 區間右端點)。 | Approach |
| Before answering q, pop heap entries with right less than q; heap top then gives shortest valid interval. | 回答 q 前先彈出 right<q 的過期項，堆頂即最短合法區間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I build sorted query pairs as value and original index. | 我先建立排序後 query 配對：值與原索引。 | Coding |
| I sort intervals by left boundary. | 把 intervals 依 left 排序。 | Coding |
| I initialize a min-heap of length and right. | 初始化最小堆，元素是長度與 right。 | Coding |
| I keep interval pointer i starting at zero. | 維護 interval 指標 i 從 0 開始。 | Coding |
| For each sorted query q, push all intervals whose left is less than or equal to q. | 對每個排序後 q，把 left<=q 的區間都推入堆。 | Coding |
| While heap top right is less than q, pop invalid intervals. | 當堆頂 right<q 時，彈出失效區間。 | Coding |
| If heap is not empty, top length is answer for this query. | 若堆非空，堆頂長度即此 query 答案。 | Coding |
| Write answer into result at original query index. | 把答案寫回原 query 索引位置。 | Coding |
| If heap is empty, keep default minus one. | 若堆為空就保留預設 -1。 | Coding |
| Return result array after processing all queries. | 全部處理完後回傳 result。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run intervals [[1,4],[2,4],[3,6],[4,4]] and queries [2,3,4,5]. | 我手跑 intervals [[1,4],[2,4],[3,6],[4,4]] 與 queries [2,3,4,5]。 | Dry-run |
| For query two, push intervals starting at one and two, shortest valid length is three. | q=2 時推入起點 1 與 2 的區間，最短合法長度是 3。 | Dry-run |
| For query three, add interval [3,6], shortest valid still three. | q=3 時再加 [3,6]，最短仍是 3。 | Dry-run |
| For query four, add [4,4], shortest becomes one. | q=4 時加入 [4,4]，最短變 1。 | Dry-run |
| For query five, pop expired intervals ending before five. | q=5 時先彈出所有 right<5 的過期區間。 | Dry-run |
| Remaining valid interval is [3,6] with length four. | 剩下有效區間是 [3,6]，長度 4。 | Dry-run |
| Final output is [3,3,1,4]. | 最終輸出是 [3,3,1,4]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: query not covered by any interval returns minus one. | 案例一：query 無任何覆蓋時回 -1。 | Edge test |
| Case two: single interval and many queries. | 案例二：單一區間配多個 queries。 | Edge test |
| Case three: many duplicate queries. | 案例三：大量重複 query 值。 | Edge test |
| Case four: interval of length one should be selected when valid. | 案例四：長度 1 區間若合法應被選中。 | Edge test |
| Case five: large non-overlapping gaps between intervals. | 案例五：區間彼此間隔很大。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log n plus q log q plus (n plus q) log n). | 時間複雜度是 O(nlogn + qlogq + (n+q)logn)。 | Complexity |
| Space complexity is O(n plus q). | 空間複雜度是 O(n+q)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting intervals takes O(n log n), and sorting queries takes O(q log q). | intervals 排序 O(n log n)，queries 排序 O(q log q)。 | Complexity |
| Each interval is pushed to heap at most once. | 每個 interval 最多只進堆一次。 | Complexity |
| Each pushed interval can be popped at most once, and each heap operation costs log n. | 每個進堆項最多彈出一次，堆操作成本是 log n。 | Complexity |
| Result array plus heap plus sorted query pairs use O(n plus q) memory. | result、堆與排序 query 配對共用 O(n+q) 記憶體。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me convert this to offline sorted queries. | 我先把題目轉成離線排序查詢。 | If stuck |
| We answer queries in increasing order. | 由小到大回答 queries。 | If stuck |
| Add intervals when left boundary is now eligible. | 當 left 合法時把區間加入堆。 | If stuck |
| Remove intervals that already ended before q. | 把在 q 前已結束的區間移除。 | If stuck |
| Heap top gives shortest valid length at this moment. | 當下堆頂就是最短合法長度。 | If stuck |
| I must store original query index for final order. | 我必須保留 query 原索引以回填順序。 | If stuck |
| Let me test quickly with one uncovered query. | 我快速測一個無覆蓋 query。 | If stuck |
| Heap becomes empty and answer should be minus one. | 堆會變空，答案應是 -1。 | If stuck |
| Good, invalid-pop condition is right less than q. | 好，失效彈出條件是 right<q。 | If stuck |
| Now the sweep line flow is clear. | 現在掃描線流程很清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with sorted queries and a min-heap sweep. | 我用排序 queries + 最小堆掃描解了這題。 | Wrap-up |
| Heap tracks candidate intervals by shortest length first. | 堆以最短長度優先追蹤候選區間。 | Wrap-up |
| Expired intervals are lazily removed before each query answer. | 每次回答前懶惰移除已過期區間。 | Wrap-up |
| Complexity is near O((n plus q) log n) after sorting. | 排序後核心複雜度近似 O((n+q)logn)。 | Wrap-up |
| This is the standard hard-level interval-query pattern. | 這是 hard 級區間查詢的標準解法模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: shortest interval covering each query. | 目標：每個 query 的最短覆蓋區間。 | Cheat sheet |
| If none covers, answer is minus one. | 若無覆蓋，答案是 -1。 | Cheat sheet |
| Sort intervals by left. | intervals 依 left 排序。 | Cheat sheet |
| Build query pairs (value,index). | 建 query 配對 (值,索引)。 | Cheat sheet |
| Sort query pairs by value. | query 配對依值排序。 | Cheat sheet |
| Use min-heap of (length,right). | 用最小堆存 (長度,right)。 | Cheat sheet |
| Pointer i scans intervals once. | 指標 i 單次掃 intervals。 | Cheat sheet |
| While left<=q, push interval. | 當 left<=q 時推入區間。 | Cheat sheet |
| While right<q, pop expired interval. | 當 right<q 時彈出過期區間。 | Cheat sheet |
| Heap top length is best answer. | 堆頂長度就是最佳答案。 | Cheat sheet |
| Write answer to original index. | 把答案寫回原索引。 | Cheat sheet |
| Keep default -1 if heap empty. | 堆空則保留預設 -1。 | Cheat sheet |
| Each interval push at most once. | 每個區間最多推入一次。 | Cheat sheet |
| Each interval pop at most once. | 每個區間最多彈出一次。 | Cheat sheet |
| Sorting dominates front cost. | 前段成本由排序主導。 | Cheat sheet |
| Time roughly O(nlogn+qlogq+(n+q)logn). | 時間約 O(nlogn+qlogq+(n+q)logn)。 | Cheat sheet |
| Space O(n+q). | 空間 O(n+q)。 | Cheat sheet |
| Common bug: forgetting original query order. | 常見錯誤：忘記回填原 query 順序。 | Cheat sheet |
| Common bug: wrong invalid condition sign. | 常見錯誤：失效條件符號寫錯。 | Cheat sheet |
| Explain as offline query plus sweep line. | 用離線查詢加掃描線來說明。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sort + min-heap + offline query indexing preserved.
- No hallucinated constraints: ✅ Inclusive boundaries and -1 fallback respected.
- Language simplicity: ✅ Stepwise interview-ready explanations.
