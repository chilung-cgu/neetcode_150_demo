# 02 Merge Two Sorted Lists — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/02_Merge_Two_Sorted_Lists.md`

> Quick links: [Source Solution](../02_Merge_Two_Sorted_Lists.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the merge-lists problem. | 我先重述合併串列題。 | Restatement |
| We are given two sorted linked lists. | 我們有兩個已排序 linked list。 | Restatement |
| I need one merged sorted list as output. | 我要輸出一個合併後仍排序的串列。 | Restatement |
| I can reuse existing nodes, no value copying required. | 可重用原節點，不必複製值。 | Restatement |
| I will use a dummy head and one tail pointer. | 我會用 dummy head 與 tail 指標。 | Restatement |
| This should run in linear time over both lists. | 這題應該是兩串列總長的線性時間。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can either list be empty? | 任一串列可能是空的嗎？ | Clarify |
| Should equal values preserve relative order from inputs? | 相等值是否要維持輸入相對順序？ | Clarify |
| Is node reuse preferred over creating new nodes? | 是否偏好重用節點而非新建節點？ | Clarify |
| Do you want iterative solution first? | 你希望先給迭代解法嗎？ | Clarify |
| Should I mention recursive variant as follow-up? | 要不要補充遞迴版本當延伸？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline can copy all values into an array and sort it. | 基線可把值拷到陣列後排序。 | Approach |
| Then rebuild a new linked list from sorted values. | 再用排序結果重建新串列。 | Approach |
| Time is O((m+n)log(m+n)), extra space is O(m+n). | 時間 O((m+n)log(m+n))，空間 O(m+n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use two pointers over list1 and list2 heads. | 以兩指標分別掃 list1 與 list2。 | Approach |
| Tail always points to last node in merged list. | tail 永遠指向合併串列最後節點。 | Approach |
| Compare current node values and append smaller one. | 比較當前值，接上較小節點。 | Approach |
| Move the pointer of the appended node forward. | 被接上的那一側指標往前移。 | Approach |
| Attach remaining list once one side is exhausted. | 任一側耗盡後直接接上另一側剩餘。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create a dummy node and set tail to dummy. | 先建 dummy 節點，tail 指向它。 | Coding |
| I set p1 to list1 head and p2 to list2 head. | p1 指向 list1，p2 指向 list2。 | Coding |
| While both pointers are non-null, I compare values. | 當兩者都非空時持續比較值。 | Coding |
| I connect tail next to the smaller node. | 把 tail->next 接到較小節點。 | Coding |
| I move that list pointer forward by one node. | 該側指標往前一個節點。 | Coding |
| I advance tail to tail next. | tail 前進到 tail->next。 | Coding |
| After loop, I connect tail next to non-null remainder. | 迴圈後把 tail 接到尚未空的一側。 | Coding |
| Finally I return dummy next as merged head. | 最後回傳 dummy->next 作為答案。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run list1 [1,2,4] and list2 [1,3,4]. | 我手跑 list1=[1,2,4], list2=[1,3,4]。 | Dry-run |
| Compare 1 and 1, choose list1 node first. | 比較 1 與 1，先接 list1 的 1。 | Dry-run |
| Next compare 2 and 1, choose list2 node 1. | 接著比較 2 與 1，接 list2 的 1。 | Dry-run |
| Then 2 beats 3, so append 2. | 然後 2 小於 3，接上 2。 | Dry-run |
| Compare 4 and 3, append 3 next. | 比較 4 與 3，下一個接 3。 | Dry-run |
| Remaining nodes are 4 and 4, append in order. | 剩下 4 與 4，依序接上。 | Dry-run |
| Final merged list is [1,1,2,3,4,4]. | 最終合併結果是 [1,1,2,3,4,4]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: both lists are empty. | 案例一：兩個串列都空。 | Edge test |
| Case two: one list empty, one non-empty. | 案例二：一空一非空。 | Edge test |
| Case three: all values in list1 are smaller than list2. | 案例三：list1 全部都比 list2 小。 | Edge test |
| Case four: heavy duplicates across both lists. | 案例四：兩側都有大量重複值。 | Edge test |
| Case five: one list has exactly one node. | 案例五：其中一側只有單節點。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m+n). | 時間複雜度是 O(m+n)。 | Complexity |
| Extra space is O(1) for iterative node-reuse version. | 迭代重用節點版額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each node from both lists is processed once. | 兩串列每個節點都只處理一次。 | Complexity |
| Per node we do constant pointer operations. | 每個節點只做常數次指標操作。 | Complexity |
| No auxiliary structure scales with input size. | 不需隨輸入成長的額外結構。 | Complexity |
| Hence runtime is linear and extra memory is constant. | 所以時間線性、額外空間常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me check my loop condition first. | 我先檢查迴圈條件。 | If stuck |
| It should continue only while both pointers exist. | 應該是兩個指標都存在才迴圈。 | If stuck |
| Tail must always point to merged list end. | tail 必須永遠指向合併尾端。 | If stuck |
| I should advance tail after every attachment. | 每次接節點後都要推進 tail。 | If stuck |
| I may have forgotten to append the remainder list. | 我可能忘了接上剩餘串列。 | If stuck |
| Let me add that after the loop. | 我把那段補在迴圈後。 | If stuck |
| I will rerun empty-list and duplicate tests. | 我重跑空串列與重複值測試。 | If stuck |
| Now all links are connected correctly. | 現在所有連結都正確。 | If stuck |
| The merged order stays sorted. | 合併後順序保持排序。 | If stuck |
| Great, solution is stable now. | 很好，解法現在穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the iterative merge implementation. | 我完成了迭代合併實作。 | Wrap-up |
| I verified empty, duplicate, and uneven-length cases. | 我驗證了空、重複與不等長案例。 | Wrap-up |
| Runtime is O(m+n). | 時間複雜度是 O(m+n)。 | Wrap-up |
| Extra memory is O(1) with node reuse. | 重用節點時額外空間是 O(1)。 | Wrap-up |
| I can also provide recursive solution comparison. | 我也可補充遞迴版本比較。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Merge two sorted linked lists. | 合併兩個排序 linked list。 | Cheat sheet |
| Return merged sorted head. | 回傳合併後排序 head。 | Cheat sheet |
| Baseline sort-all-values is expensive. | 基線全值排序成本較高。 | Cheat sheet |
| Better use two pointers plus dummy. | 更好是雙指標加 dummy。 | Cheat sheet |
| tail starts at dummy. | tail 起始在 dummy。 | Cheat sheet |
| Compare p1 and p2 values. | 比較 p1 與 p2 的值。 | Cheat sheet |
| Append smaller node to tail. | 把較小節點接到 tail。 | Cheat sheet |
| Advance that source pointer. | 推進該來源指標。 | Cheat sheet |
| Advance tail every step. | 每步都推進 tail。 | Cheat sheet |
| Loop while both pointers exist. | 兩指標都存在時持續迴圈。 | Cheat sheet |
| Attach remaining list once loop ends. | 結束後接上剩餘串列。 | Cheat sheet |
| Return dummy->next. | 回傳 dummy->next。 | Cheat sheet |
| Test both-empty case. | 測雙空案例。 | Cheat sheet |
| Test one-empty case. | 測一空一非空案例。 | Cheat sheet |
| Test duplicate-heavy case. | 測大量重複值案例。 | Cheat sheet |
| Test uneven lengths. | 測不等長案例。 | Cheat sheet |
| Time O(m+n). | 時間 O(m+n)。 | Cheat sheet |
| Space O(1) iterative reuse. | 迭代重用版空間 O(1)。 | Cheat sheet |
| Bug risk: forget remainder attachment. | 風險：忘記接剩餘串列。 | Cheat sheet |
| Bug risk: not moving tail pointer. | 風險：忘記推進 tail。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Dummy-node iterative merge logic is preserved.
- No hallucinated constraints: ✅ Script follows source list semantics and examples.
- Language simplicity: ✅ Short lines optimized for interview speaking flow.
