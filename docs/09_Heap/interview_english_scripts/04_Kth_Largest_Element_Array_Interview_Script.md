# 04 Kth Largest Element in an Array — Interview English Script (C++)

> Source aligned with: `docs/09_Heap/04_Kth_Largest_Element_Array.md`

> Quick links: [Source Solution](../04_Kth_Largest_Element_Array.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the kth-largest-in-array problem. | 我先重述陣列第 k 大問題。 | Restatement |
| We are given an unsorted integer array and k. | 題目給未排序整數陣列與 k。 | Restatement |
| We need the k-th largest value, counting duplicates normally. | 要找第 k 大值，重複值照常計算。 | Restatement |
| This is selection, not full sorting requirement. | 這是選擇問題，不是一定要全排序。 | Restatement |
| We can solve with quick select or heap. | 可以用 quick select 或 heap。 | Restatement |
| I will present quick select as primary optimized approach. | 我會以 quick select 作主要優化法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are duplicates counted as separate positions? | 重複值是否分別計算名次？ | Clarify |
| Is in-place modification of nums allowed? | 可以原地修改 nums 嗎？ | Clarify |
| Do we always have one less than or equal k less than or equal n? | 是否保證 1 <= k <= n？ | Clarify |
| Do you prefer average O(n) quick select discussion? | 你希望強調平均 O(n) quick select 嗎？ | Clarify |
| Should I also mention heap O(n log k) alternative? | 是否也要提 heap O(n log k) 替代法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force sorts full array in ascending order. | 暴力法把整個陣列升序排序。 | Approach |
| Then answer is at index n minus k. | 接著答案在索引 n-k。 | Approach |
| Runtime is O(n log n), which is not optimal. | 時間 O(n log n)，不是最佳。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Optimized approach uses quick select partition idea. | 優化法用 quick select 的 partition 概念。 | Approach |
| We can transform to finding index k minus one in descending order. | 轉成降序下找索引 k-1。 | Approach |
| Each partition puts pivot near its final relative position. | 每次 partition 會把 pivot 放到相對正確區域。 | Approach |
| We recurse or iterate only on one relevant side. | 只在有機會含答案的一側繼續。 | Approach |
| Average runtime is O(n), worst case O(n squared). | 平均 O(n)，最壞 O(n²)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I call nth_element with comparator greater for descending logic. | 我用 greater 比較器呼叫 nth_element。 | Coding |
| Target iterator is nums begin plus k minus one. | 目標迭代器是 nums.begin()+k-1。 | Coding |
| nth_element ensures that position has the correct element. | nth_element 會保證該位置元素正確。 | Coding |
| Elements before target are not smaller than target by comparator. | 目標前元素依比較器不小於目標。 | Coding |
| Elements after target are not larger than target by comparator. | 目標後元素依比較器不大於目標。 | Coding |
| I then return nums at index k minus one. | 然後回傳 nums[k-1]。 | Coding |
| This avoids full sorting overhead. | 這可避免完整排序成本。 | Coding |
| I can mention heap variant if interviewer asks. | 若面試官問，我可補充 heap 版本。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [3,2,1,5,6,4] with k equals 2. | 我手跑 nums [3,2,1,5,6,4]、k=2。 | Dry-run |
| Target in descending index one should become second largest. | 降序索引 1 應成為第二大。 | Dry-run |
| After nth_element, nums[1] is guaranteed to be correct answer. | 執行後 nums[1] 保證是正確答案。 | Dry-run |
| For this sample, that value is five. | 這個範例該值是 5。 | Dry-run |
| We do not care about full order of other positions. | 其他位置不需完全排序。 | Dry-run |
| Returned result is five, matching expected output. | 回傳 5，與預期一致。 | Dry-run |
| Duplicate handling stays natural in this formulation. | 這種作法對重複值處理自然。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: k equals one returns global maximum. | 案例一：k=1 回傳全域最大值。 | Edge test |
| Case two: k equals n returns global minimum. | 案例二：k=n 回傳全域最小值。 | Edge test |
| Case three: all numbers equal should return that value. | 案例三：全部相等應回同一值。 | Edge test |
| Case four: duplicates around boundary rank. | 案例四：邊界名次附近有重複值。 | Edge test |
| Case five: negative and positive mixed values. | 案例五：正負數混合情況。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Average time complexity is O(n), worst case O(n squared). | 平均時間 O(n)，最壞 O(n²)。 | Complexity |
| Extra space is O(1) excluding recursion stack internals. | 額外空間 O(1)（不含內部遞迴堆疊）。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Quick select partitions array and only explores one side each step. | quick select 每步 partition 並只往一側繼續。 | Complexity |
| Expected remaining size shrinks geometrically on average. | 平均下剩餘規模呈幾何縮小。 | Complexity |
| So average runtime is O(n), but worst partition pattern can hit O(n squared). | 所以平均 O(n)，最壞切分會到 O(n²)。 | Complexity |
| In-place rearrangement keeps auxiliary memory near O(1). | 原地重排讓輔助記憶體約 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate: I need one rank, not full sorted array. | 我先重述：只要一個名次，不要全排序。 | If stuck |
| That suggests selection algorithm immediately. | 這立刻指向 selection 演算法。 | If stuck |
| I can still mention sorting as baseline. | 我仍可先提排序作基線。 | If stuck |
| Then I pivot to quick select for better average time. | 然後切到 quick select 取得較佳平均時間。 | If stuck |
| I should be careful with k index conversion. | 我要小心 k 的索引轉換。 | If stuck |
| With descending comparator, target is index k minus one. | 用降序比較器時目標是 k-1。 | If stuck |
| Let me validate with sample where answer is five. | 我用答案為 5 的範例驗證。 | If stuck |
| Result matches, so index mapping is correct. | 結果吻合，索引映射正確。 | If stuck |
| If interviewer prefers, I can offer min-heap version. | 若面試官偏好，我可提供 min-heap 版本。 | If stuck |
| Great, I am ready to finalize complexity and trade-offs. | 很好，我可收尾複雜度與取捨。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with quick select style nth_element. | 我用 quick select 風格的 nth_element 解題。 | Wrap-up |
| This targets kth largest directly without full sort. | 這能直接定位第 k 大，不用全排序。 | Wrap-up |
| Average complexity is O(n), with worst-case O(n squared). | 平均複雜度 O(n)，最壞 O(n²)。 | Wrap-up |
| Space overhead is minimal due to in-place partitioning. | 因原地切分，空間額外開銷很小。 | Wrap-up |
| I can also provide heap alternative O(n log k). | 我也可提供 heap 替代法 O(n log k)。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: selection by rank. | 題型：按名次做 selection。 | Cheat sheet |
| Need kth largest with duplicates counted. | 要找第 k 大，重複照算。 | Cheat sheet |
| Baseline: sort then pick n-k. | 基線：排序後取 n-k。 | Cheat sheet |
| Baseline runtime O(n log n). | 基線時間 O(n log n)。 | Cheat sheet |
| Optimized: quick select partition. | 優化：quick select partition。 | Cheat sheet |
| Use nth_element in C++. | C++ 可用 nth_element。 | Cheat sheet |
| Comparator greater gives descending relation. | greater 比較器代表降序關係。 | Cheat sheet |
| Target index is k minus one. | 目標索引是 k-1。 | Cheat sheet |
| Return nums at target index. | 回傳目標索引元素。 | Cheat sheet |
| Full array order is unnecessary. | 不需要整體完全有序。 | Cheat sheet |
| Average runtime O(n). | 平均時間 O(n)。 | Cheat sheet |
| Worst runtime O(n squared). | 最壞時間 O(n²)。 | Cheat sheet |
| Aux space about O(1). | 輔助空間約 O(1)。 | Cheat sheet |
| Edge: k equals one. | 邊界：k=1。 | Cheat sheet |
| Edge: k equals n. | 邊界：k=n。 | Cheat sheet |
| Handle duplicates naturally. | 重複值自然處理。 | Cheat sheet |
| Handle negative values too. | 負數也可處理。 | Cheat sheet |
| Common bug: wrong k index conversion. | 常見錯誤：k 索引轉換錯。 | Cheat sheet |
| Alternative: min-heap size k. | 替代法：size-k min-heap。 | Cheat sheet |
| Heap complexity O(n log k). | heap 複雜度 O(n log k)。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Quick select / `nth_element` primary approach preserved.
- No hallucinated constraints: ✅ Uses source-defined semantics and duplicate handling.
- Language simplicity: ✅ Natural interview phrasing with precise technical terms.
