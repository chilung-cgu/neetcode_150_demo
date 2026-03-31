# 03 Reorder List — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/03_Reorder_List.md`

> Quick links: [Source Solution](../03_Reorder_List.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the reorder-list task. | 我先重述重排串列題。 | Restatement |
| We have list order L0 to Ln and need L0, Ln, L1, Ln-1 pattern. | 原順序是 L0 到 Ln，目標是 L0,Ln,L1,Ln-1 交錯。 | Restatement |
| Node values cannot be modified. | 不能改節點值。 | Restatement |
| We must only rewire next pointers. | 只能重接 next 指標。 | Restatement |
| I will do this in-place with O(1) extra space. | 我會用原地 O(1) 額外空間完成。 | Restatement |
| Plan is find middle, reverse second half, then merge alternately. | 計畫是找中點、反轉後半、再交錯合併。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is list length at least one by constraints? | 根據限制，串列長度至少一嗎？ | Clarify |
| Should function return void with in-place mutation? | 函式是 in-place 修改且回傳 void 嗎？ | Clarify |
| Can I split list exactly at middle for odd length? | 奇數長度可以在正中間切分嗎？ | Clarify |
| Is O(n) time and O(1) extra space expected? | 預期是 O(n) 時間與 O(1) 空間嗎？ | Clarify |
| Do you want safety note about restoring original list not required? | 需要註明不用還原原始順序嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline copies nodes into an array. | 基線是把節點存進陣列。 | Approach |
| Then reconnect from both ends inward. | 再由兩端往中間重接。 | Approach |
| Time O(n), extra space O(n). | 時間 O(n)，額外空間 O(n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Step one: find middle by fast and slow pointers. | 第一步：快慢指標找中點。 | Approach |
| Step two: reverse the second half list. | 第二步：反轉後半串列。 | Approach |
| Step three: merge first half and reversed half alternately. | 第三步：前半與反轉後半交錯合併。 | Approach |
| Cut at middle to avoid cycle during merge. | 在中點斷開，避免合併時成環。 | Approach |
| Total time O(n), extra space O(1). | 總時間 O(n)，額外空間 O(1)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I use slow and fast to find the middle node. | 先用 slow/fast 找中間節點。 | Coding |
| I split list into two parts at middle. | 在中點把串列切成兩段。 | Coding |
| I reverse the second half iteratively. | 以迭代方式反轉後半段。 | Coding |
| I set p1 to first half and p2 to reversed half. | p1 指前半，p2 指反轉後半。 | Coding |
| While p2 exists, I save next pointers from both sides. | 當 p2 存在時，先存兩側 next。 | Coding |
| I connect p1 to p2, then p2 to saved p1-next. | 先接 p1 到 p2，再接 p2 到原 p1-next。 | Coding |
| I advance p1 and p2 to saved next nodes. | 再把 p1/p2 前進到剛保存的位置。 | Coding |
| This finishes in-place reorder without extra array. | 這樣可原地重排且不需額外陣列。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run head [1,2,3,4,5]. | 我手跑 head=[1,2,3,4,5]。 | Dry-run |
| Middle is node 3, so first half is [1,2,3]. | 中點是 3，前半是 [1,2,3]。 | Dry-run |
| Second half [4,5] is reversed to [5,4]. | 後半 [4,5] 反轉成 [5,4]。 | Dry-run |
| Merge step one gives 1 -> 5 -> 2. | 第一步合併得到 1->5->2。 | Dry-run |
| Merge step two gives 2 -> 4 -> 3 continuation. | 第二步合併得到 2->4->3 延續。 | Dry-run |
| Final list becomes [1,5,2,4,3]. | 最終串列是 [1,5,2,4,3]。 | Dry-run |
| Output matches required pattern. | 輸出符合題目要求的交錯模式。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one node only. | 案例一：只有一個節點。 | Edge test |
| Case two: two nodes only. | 案例二：只有兩個節點。 | Edge test |
| Case three: even-length list like [1,2,3,4]. | 案例三：偶數長度如 [1,2,3,4]。 | Edge test |
| Case four: odd-length list like [1,2,3,4,5]. | 案例四：奇數長度如 [1,2,3,4,5]。 | Edge test |
| Case five: long list to validate no cycle introduced. | 案例五：長串列確認不會形成環。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We traverse list for middle, reverse, and merge phases. | 我們會做找中點、反轉、合併三個線性階段。 | Complexity |
| Each node is visited constant times across phases. | 每節點在各階段只被常數次處理。 | Complexity |
| No array, stack, or map proportional to n is used. | 不使用與 n 成比例的陣列、堆疊或 map。 | Complexity |
| So total runtime is linear with constant extra memory. | 因此總時間線性、額外空間常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me split the process into three phases again. | 我再把流程拆成三階段。 | If stuck |
| Phase one is finding middle with slow and fast. | 第一階段是快慢指標找中點。 | If stuck |
| Phase two is reversing second half safely. | 第二階段是安全反轉後半。 | If stuck |
| Phase three is alternate merge with saved next pointers. | 第三階段是保存 next 後交錯合併。 | If stuck |
| I might have forgotten to cut middle next to null. | 我可能忘了把 middle->next 斷開。 | If stuck |
| That can create cycles during merge. | 這會在合併時造成環。 | If stuck |
| I will fix the split and rerun sample. | 我修正切分後重跑範例。 | If stuck |
| Now reorder pattern looks correct. | 現在重排模式正確。 | If stuck |
| I also checked tail ends with null. | 我也確認尾端正確指向 null。 | If stuck |
| Great, implementation is stable. | 很好，實作已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished in-place reorder list implementation. | 我完成了原地重排串列實作。 | Wrap-up |
| I validated odd, even, and short-list cases. | 我驗證了奇偶長度與短串列案例。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can discuss deque-based alternative if needed. | 若需要我可補充 deque 替代解。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Reorder as L0, Ln, L1, Ln-1 pattern. | 重排成 L0,Ln,L1,Ln-1 模式。 | Cheat sheet |
| Do not change node values. | 不能改節點值。 | Cheat sheet |
| Baseline array method uses O(n) space. | 基線陣列法需 O(n) 空間。 | Cheat sheet |
| Better in-place three-phase method. | 更好是原地三階段法。 | Cheat sheet |
| Phase 1: find middle by slow-fast. | 第一階段：快慢指標找中點。 | Cheat sheet |
| Cut list at middle. | 在中點斷開串列。 | Cheat sheet |
| Phase 2: reverse second half. | 第二階段：反轉後半段。 | Cheat sheet |
| Phase 3: merge two halves alternately. | 第三階段：兩半交錯合併。 | Cheat sheet |
| Save next pointers before rewiring. | 重接前先保存 next 指標。 | Cheat sheet |
| Connect p1->p2 then p2->next1. | 連接 p1->p2 再 p2->next1。 | Cheat sheet |
| Advance both pointers. | 兩側指標同步前進。 | Cheat sheet |
| Stop when second half is exhausted. | 後半耗盡即停止。 | Cheat sheet |
| Test one-node case. | 測單節點案例。 | Cheat sheet |
| Test two-node case. | 測雙節點案例。 | Cheat sheet |
| Test odd/even lengths. | 測奇偶長度。 | Cheat sheet |
| Confirm no cycle after merge. | 確認合併後沒有環。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: not cutting middle. | 常見 bug：沒在中點斷開。 | Cheat sheet |
| Common bug: lost next pointer on merge. | 常見 bug：合併時遺失 next。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Mid + reverse + merge pipeline is preserved.
- No hallucinated constraints: ✅ Follows source reorder semantics and examples.
- Language simplicity: ✅ Compact spoken lines for interview flow.
