# 10 Merge k Sorted Lists — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/10_Merge_k_Sorted_Lists.md`

> Quick links: [Source Solution](../10_Merge_k_Sorted_Lists.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the merge-k-lists problem. | 我先重述合併 k 串列題。 | Restatement |
| We receive k individually sorted linked lists. | 我們拿到 k 個各自排序好的串列。 | Restatement |
| Need one globally sorted merged linked list. | 目標是合併成一個全域排序串列。 | Restatement |
| Total nodes can be large while k may also be large. | 總節點數可能大，k 也可能大。 | Restatement |
| A repeated pairwise merge pattern is suitable. | 反覆兩兩合併很適合這題。 | Restatement |
| I will use divide-and-conquer merge strategy. | 我會使用 divide-and-conquer 合併策略。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can lists array be empty? | lists 陣列可能是空的嗎？ | Clarify |
| Can some entries in lists be null? | lists 內個別項目可能是 null 嗎？ | Clarify |
| Do you prefer divide-and-conquer over heap for main answer? | 主要答案偏好分治還是 heap？ | Clarify |
| Is in-place node reuse acceptable? | 可接受重用原節點嗎？ | Clarify |
| Should I discuss heap trade-off briefly after main solution? | 主解後要不要簡述 heap 取捨？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline collects all node values then sorts them. | 基線是收集全部值後排序。 | Approach |
| Rebuild a new linked list from sorted values. | 再用排序值重建新串列。 | Approach |
| Time O(N log N), extra space O(N). | 時間 O(NlogN)，額外空間 O(N)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Merge lists in rounds with interval 1, 2, 4, and so on. | 以間距 1、2、4… 的輪次做兩兩合併。 | Approach |
| Each round halves the number of active lists. | 每輪都把有效串列數大致減半。 | Approach |
| Use standard merge-two-sorted-lists helper each pair. | 每對都用標準雙串列合併 helper。 | Approach |
| Repeat until one list remains at index zero. | 重複直到只剩 index 0 一條串列。 | Approach |
| Overall complexity becomes O(N log k). | 整體複雜度會是 O(Nlogk)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, if lists is empty, return null immediately. | 先判斷 lists 為空就回傳 null。 | Coding |
| I initialize interval as one. | interval 初始為 1。 | Coding |
| While interval is less than k, I merge pairs. | 當 interval 小於 k 時進行成對合併。 | Coding |
| For each i, merge lists[i] with lists[i plus interval]. | 對每個 i，把 lists[i] 與 lists[i+interval] 合併。 | Coding |
| Store merged result back into lists[i]. | 把合併結果寫回 lists[i]。 | Coding |
| After finishing one round, double interval. | 完成一輪後把 interval 乘以 2。 | Coding |
| Continue until interval reaches or exceeds k. | 持續到 interval 達到或超過 k。 | Coding |
| Return lists[0] as final merged head. | 回傳 lists[0] 作為最終 head。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run lists [[1,4,5],[1,3,4],[2,6]]. | 我手跑 lists=[[1,4,5],[1,3,4],[2,6]]。 | Dry-run |
| Interval one: merge list0 and list1 into [1,1,3,4,4,5]. | interval=1 時，list0 與 list1 合成 [1,1,3,4,4,5]。 | Dry-run |
| list2 remains unchanged in this round. | 本輪 list2 保持不變。 | Dry-run |
| Double interval to two. | interval 加倍成 2。 | Dry-run |
| Merge list0 with list2 to get [1,1,2,3,4,4,5,6]. | 將 list0 與 list2 合併得 [1,1,2,3,4,4,5,6]。 | Dry-run |
| Now interval four exceeds k, stop loop. | interval=4 已超過 k，停止。 | Dry-run |
| Return list0 as final answer. | 回傳 list0 即最終答案。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty lists array. | 案例一：lists 陣列為空。 | Edge test |
| Case two: lists contains only null entries. | 案例二：lists 全是 null。 | Edge test |
| Case three: one non-empty list only. | 案例三：只有一條非空串列。 | Edge test |
| Case four: many short lists with duplicates. | 案例四：多條短串列且有重複值。 | Edge test |
| Case five: highly imbalanced lengths among lists. | 案例五：各串列長度極不平均。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(N log k). | 時間複雜度是 O(Nlogk)。 | Complexity |
| Extra space is O(1) besides output-node links. | 除了輸出連結外，額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| There are log k merge rounds in divide-and-conquer. | 分治法共有 log k 輪合併。 | Complexity |
| In each round, all N nodes are processed once via merge operations. | 每輪透過合併操作會處理全部 N 節點一次。 | Complexity |
| Multiplying gives O(N log k) total runtime. | 相乘得到總時間 O(Nlogk)。 | Complexity |
| Iterative pointer rewiring keeps auxiliary memory constant. | 迭代指標重接讓輔助記憶體維持常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me step back to merge-two-lists helper first. | 我先退回確認 merge-two helper。 | If stuck |
| If helper is correct, divide-and-conquer layering is straightforward. | helper 正確後，分治層次就很直觀。 | If stuck |
| I might have wrong loop step for i increment. | 我可能把 i 的步長寫錯。 | If stuck |
| It should jump by interval times two each round. | 應該每次跳 interval*2。 | If stuck |
| I also need bound check i plus interval less than k. | 也要檢查 i+interval 小於 k。 | If stuck |
| Let me fix index bounds and rerun sample. | 我修正索引邊界後重跑範例。 | If stuck |
| Now every list pair is merged exactly once per round. | 現在每輪每對串列都只合併一次。 | If stuck |
| Final sorted order looks correct. | 最終排序結果正確。 | If stuck |
| Complexity target is also satisfied. | 複雜度目標也符合。 | If stuck |
| Great, solution is stable now. | 很好，解法現在穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed divide-and-conquer merge-k-lists implementation. | 我完成了分治合併 k 串列實作。 | Wrap-up |
| I validated empty, null-list, and duplicate-heavy cases. | 我驗證了空輸入、null 串列與重複值案例。 | Wrap-up |
| Runtime is O(N log k). | 時間複雜度是 O(Nlogk)。 | Wrap-up |
| Extra space is O(1) for iterative version. | 迭代版額外空間是 O(1)。 | Wrap-up |
| I can compare heap approach trade-offs if needed. | 若需要我可比較 heap 方案取捨。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Merge k sorted linked lists into one. | 把 k 條排序串列合併成一條。 | Cheat sheet |
| Baseline sort-all-values is O(NlogN). | 基線全值排序是 O(NlogN)。 | Cheat sheet |
| Better use divide-and-conquer merges. | 更好是分治兩兩合併。 | Cheat sheet |
| interval starts at 1. | interval 從 1 開始。 | Cheat sheet |
| Pair lists by i and i+interval. | 用 i 與 i+interval 成對。 | Cheat sheet |
| Merge pair with mergeTwo helper. | 用 mergeTwo helper 合併每對。 | Cheat sheet |
| Write merged head back to lists[i]. | 合併結果寫回 lists[i]。 | Cheat sheet |
| Increment i by interval*2. | i 每次加 interval*2。 | Cheat sheet |
| Double interval each round. | 每輪把 interval 加倍。 | Cheat sheet |
| Stop when interval >= k. | interval>=k 時停止。 | Cheat sheet |
| Return lists[0]. | 回傳 lists[0]。 | Cheat sheet |
| Test empty lists input. | 測空 lists 輸入。 | Cheat sheet |
| Test all-null entries input. | 測全 null 項目輸入。 | Cheat sheet |
| Test one-list input. | 測單一串列輸入。 | Cheat sheet |
| Test duplicate-heavy input. | 測重複值密集輸入。 | Cheat sheet |
| Time O(Nlogk). | 時間 O(Nlogk)。 | Cheat sheet |
| Space O(1) iterative. | 迭代空間 O(1)。 | Cheat sheet |
| Bug risk: wrong interval step. | 風險：interval 步長寫錯。 | Cheat sheet |
| Bug risk: out-of-range pair index. | 風險：成對索引越界。 | Cheat sheet |
| Mention heap as alternative O(Nlogk), O(k) space. | 可提 heap 替代：O(Nlogk)、O(k) 空間。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Divide-and-conquer merge pipeline is preserved.
- No hallucinated constraints: ✅ Uses source k/N constraints and list semantics.
- Language simplicity: ✅ Interview-ready concise spoken lines.
