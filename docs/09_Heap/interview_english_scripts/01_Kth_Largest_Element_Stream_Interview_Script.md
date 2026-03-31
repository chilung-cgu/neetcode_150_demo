# 01 Kth Largest Element in a Stream — Interview English Script (C++)

> Source aligned with: `docs/09_Heap/01_Kth_Largest_Element_Stream.md`

> Quick links: [Source Solution](../01_Kth_Largest_Element_Stream.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the stream kth-largest design problem. | 我先重述串流第 k 大設計題。 | Restatement |
| We need a class initialized with k and an initial array. | 要設計一個類別，初始給 k 與陣列。 | Restatement |
| For each add call, we insert one value into the stream. | 每次 add 都會把一個值加入串流。 | Restatement |
| Then we return the current k-th largest element. | 接著回傳目前第 k 大元素。 | Restatement |
| Duplicate numbers still count as separate elements. | 重複數值也要分別計算。 | Restatement |
| I will use a min-heap of size k. | 我會用大小固定為 k 的 min-heap。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is it guaranteed that after each add we have at least k elements? | 是否保證每次 add 後至少有 k 個元素？ | Clarify |
| Are duplicate values treated as distinct occurrences? | 重複值是否視為不同出現次數？ | Clarify |
| Can the initial nums array be empty? | 初始 nums 可以是空的嗎？ | Clarify |
| Should add return answer immediately after insertion? | add 是否要在插入後立刻回傳答案？ | Clarify |
| Is min-heap size-k approach the expected design? | 題目是否預期用 size-k 的 min-heap？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force keeps all stream values in a list. | 暴力法把串流所有值都存清單。 | Approach |
| On each add, sort the whole list and pick index length minus k. | 每次 add 後整體排序，再取倒數第 k。 | Approach |
| That costs O(n log n) per operation, too expensive. | 每次操作 O(n log n)，成本太高。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Maintain a min-heap that stores only the largest k elements. | 維護只存最大 k 個數的 min-heap。 | Approach |
| Heap top is the smallest among those k elements. | heap top 是這 k 個中的最小值。 | Approach |
| Therefore heap top is exactly the k-th largest overall. | 因此 heap top 就是整體第 k 大。 | Approach |
| For each add, push value and pop once if size exceeds k. | 每次 add 先 push，超過 k 就 pop 一次。 | Approach |
| This keeps add operation at O(log k). | 如此 add 可維持在 O(log k)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I store k as a class field. | 我先把 k 存成類別欄位。 | Coding |
| I define a min-heap using priority_queue with greater comparator. | 我用 greater 比較器定義 min-heap。 | Coding |
| In constructor, I iterate initial numbers and call add logic. | 建構子走訪初始數列並套用 add 邏輯。 | Coding |
| In add, I push the new value into heap. | 在 add 中先把新值推入 heap。 | Coding |
| If heap size is larger than k, I pop heap top. | 若 heap 大小超過 k，就 pop top。 | Coding |
| This removes values that cannot stay in top-k set. | 這會移除不屬於 top-k 的值。 | Coding |
| I return heap top as the current k-th largest. | 我回傳 heap top 作為目前第 k 大。 | Coding |
| Heap size stays bounded by k at all times. | heap 大小會始終維持在 k 以內。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run k equals 3 with nums [4,5,8,2]. | 我手跑 k=3、nums=[4,5,8,2]。 | Dry-run |
| After initialization, heap keeps top three values [4,5,8]. | 初始化後 heap 留下前 3 大 [4,5,8]。 | Dry-run |
| add 3 gives heap [4,5,8], so return 4. | add 3 後 heap 仍是 [4,5,8]，回 4。 | Dry-run |
| add 5 gives heap [5,5,8], so return 5. | add 5 後 heap 為 [5,5,8]，回 5。 | Dry-run |
| add 10 gives heap [5,8,10], so return 5. | add 10 後 heap 為 [5,8,10]，回 5。 | Dry-run |
| add 9 gives heap [8,9,10], so return 8. | add 9 後 heap 為 [8,9,10]，回 8。 | Dry-run |
| add 4 keeps return value 8, matching expected outputs. | add 4 仍回 8，與預期一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: k equals one should always return current maximum. | 案例一：k=1 應始終回傳目前最大值。 | Edge test |
| Case two: initial nums is empty and values come from add only. | 案例二：初始 nums 空，全部靠 add 進來。 | Edge test |
| Case three: all values equal should keep same answer. | 案例三：全部值相同時答案應固定。 | Edge test |
| Case four: negative numbers mixed with positives. | 案例四：負數與正數混合情況。 | Edge test |
| Case five: k equals total stream size boundary. | 案例五：k 等於串流總長邊界。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Constructor is O(n log k), and each add is O(log k). | 建構子 O(n log k)，每次 add 是 O(log k)。 | Complexity |
| Extra space is O(k). | 額外空間是 O(k)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We process each initial value with push and possible pop on size-k heap. | 初始每個值都在 size-k heap 做 push/可能 pop。 | Complexity |
| Each heap operation costs O(log k). | 每次 heap 操作成本 O(log k)。 | Complexity |
| Therefore constructor is O(n log k) and add is O(log k). | 所以建構子 O(n log k)，add 為 O(log k)。 | Complexity |
| Heap never stores more than k elements, so memory is O(k). | heap 不會超過 k 個元素，因此記憶體 O(k)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on what we truly need: only top k values. | 我先聚焦需求：只要 top k 值。 | If stuck |
| I do not need full sorted order of all stream elements. | 我不需要整個串流完整排序。 | If stuck |
| The correct heap is min-heap, not max-heap. | 這題應用 min-heap，不是 max-heap。 | If stuck |
| Min-heap top represents the k-th largest boundary. | min-heap top 就是第 k 大邊界值。 | If stuck |
| I might have forgotten to pop when size exceeds k. | 我可能漏了 size>k 時的 pop。 | If stuck |
| Let me add that guard and rerun sample. | 我補上這個條件後重跑範例。 | If stuck |
| Now add sequence returns 4,5,5,8,8 correctly. | 現在 add 序列正確回 4,5,5,8,8。 | If stuck |
| I will test k equals one quickly. | 我再快速測試 k=1。 | If stuck |
| It returns running maximum as expected. | 結果如預期回傳動態最大值。 | If stuck |
| Great, heap invariant is now stable. | 很好，heap 不變量已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed KthLargest using a size-k min-heap. | 我完成了用 size-k min-heap 的 KthLargest。 | Wrap-up |
| Heap top always gives the current k-th largest value. | heap top 會始終給出目前第 k 大。 | Wrap-up |
| Constructor cost is O(n log k). | 建構子成本為 O(n log k)。 | Wrap-up |
| Each add call is O(log k). | 每次 add 為 O(log k)。 | Wrap-up |
| I can also compare with full-sort baseline if needed. | 若需要我可再對比完整排序基線。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Design stream k-th largest structure. | 設計串流第 k 大結構。 | Cheat sheet |
| Keep only top k values. | 只保留 top k 值。 | Cheat sheet |
| Use min-heap of size k. | 使用大小 k 的 min-heap。 | Cheat sheet |
| Heap top is k-th largest. | heap top 就是第 k 大。 | Cheat sheet |
| Store k in class field. | 將 k 存成類別欄位。 | Cheat sheet |
| Constructor processes initial nums. | 建構子處理初始 nums。 | Cheat sheet |
| add pushes new value. | add 先推入新值。 | Cheat sheet |
| If size > k, pop top. | 若 size>k，彈出 top。 | Cheat sheet |
| Return heap top each add. | 每次 add 回傳 heap top。 | Cheat sheet |
| Duplicates count normally. | 重複值正常計算。 | Cheat sheet |
| k=1 returns current max. | k=1 回傳目前最大值。 | Cheat sheet |
| Empty initial nums is allowed. | 可處理初始空 nums。 | Cheat sheet |
| Constructor O(n log k). | 建構子 O(n log k)。 | Cheat sheet |
| add O(log k). | add O(log k)。 | Cheat sheet |
| Space O(k). | 空間 O(k)。 | Cheat sheet |
| Common bug: using max-heap directly. | 常見錯誤：直接用 max-heap。 | Cheat sheet |
| Common bug: forgetting size cap pop. | 常見錯誤：忘記 size 上限 pop。 | Cheat sheet |
| Validate with sample returns 4,5,5,8,8. | 用範例驗證回傳 4,5,5,8,8。 | Cheat sheet |
| Mention full-sort alternative. | 可提完整排序替代法。 | Cheat sheet |
| End with heap invariant statement. | 收尾強調 heap 不變量。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Min-heap size `k` design is preserved.
- No hallucinated constraints: ✅ Operation semantics follow source definition.
- Language simplicity: ✅ Concise spoken interview lines.
