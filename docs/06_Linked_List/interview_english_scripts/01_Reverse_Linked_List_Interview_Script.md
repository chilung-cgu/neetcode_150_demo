# 01 Reverse Linked List — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/01_Reverse_Linked_List.md`

> Quick links: [Source Solution](../01_Reverse_Linked_List.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We are given the head of a singly linked list. | 我們拿到單向 linked list 的 head。 | Restatement |
| I need to reverse the direction of every next pointer. | 我要把每個 next 指向完全反轉。 | Restatement |
| Then I should return the new head node. | 最後回傳新的 head。 | Restatement |
| This should run in linear time. | 這題應該用線性時間完成。 | Restatement |
| I will use iterative three-pointer reversal with O(1) extra space. | 我會用三指標迭代反轉，額外空間 O(1)。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can the input head be null? | 輸入 head 可能是 null 嗎？ | Clarify |
| Should I return null directly for empty list? | 空串列是否直接回傳 null？ | Clarify |
| Is iterative approach preferred over recursive one? | 你偏好迭代而不是遞迴嗎？ | Clarify |
| Do you want me to keep node values unchanged? | 需要保持節點值完全不變對嗎？ | Clarify |
| Should I mention recursive trade-off briefly? | 要不要順帶提遞迴版取捨？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| One baseline is storing nodes in an array first. | 一個基線是先把節點存進陣列。 | Approach |
| Then reconnect pointers from back to front. | 再由後往前重接指標。 | Approach |
| Time is O(n), extra space is O(n). | 時間 O(n)，額外空間 O(n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use three pointers: prev, curr, and nextTemp. | 用三個指標：prev、curr、nextTemp。 | Approach |
| At each node, save curr->next first. | 每步先保存 curr->next。 | Approach |
| Reverse the link by setting curr->next to prev. | 再把 curr->next 改指向 prev。 | Approach |
| Move prev and curr one step forward. | 然後 prev 和 curr 各前進一步。 | Approach |
| Finish when curr becomes null, and prev is new head. | curr 變 null 時結束，prev 就是新 head。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize prev as null and curr as head. | 先把 prev 設 null，curr 設 head。 | Coding |
| I loop while curr is not null. | 當 curr 不為 null 時持續迴圈。 | Coding |
| I store curr next node in a temp pointer. | 先用 temp 存 curr 的下一個節點。 | Coding |
| I reverse curr next to point to prev. | 將 curr 的 next 反轉指向 prev。 | Coding |
| I move prev to curr. | 把 prev 前進到 curr。 | Coding |
| I move curr to saved nextTemp. | 把 curr 前進到 nextTemp。 | Coding |
| Repeat until all pointers are reversed. | 重複直到所有指標都反轉。 | Coding |
| Return prev as the new list head. | 回傳 prev 作為新串列 head。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run head equals [1,2,3,4,5]. | 我手跑 head=[1,2,3,4,5]。 | Dry-run |
| Start with prev null and curr at node 1. | 起始 prev 是 null，curr 在節點 1。 | Dry-run |
| Save node 2, set 1 next to null, move prev to 1. | 存節點 2，讓 1 指向 null，prev 到 1。 | Dry-run |
| Curr moves to 2, then 2 next points to 1. | curr 到 2，接著 2 指向 1。 | Dry-run |
| Continue same pattern for 3, 4, and 5. | 對 3、4、5 重複同樣流程。 | Dry-run |
| At end curr is null and prev is node 5. | 結束時 curr=null，prev 在節點 5。 | Dry-run |
| Final output is [5,4,3,2,1]. | 最終輸出是 [5,4,3,2,1]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty list input. | 案例一：空串列輸入。 | Edge test |
| Case two: single node list. | 案例二：只有一個節點。 | Edge test |
| Case three: two-node list. | 案例三：兩個節點的串列。 | Edge test |
| Case four: odd-length list with middle node. | 案例四：奇數長度含中間節點。 | Edge test |
| Case five: even-length list. | 案例五：偶數長度串列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each node is visited exactly once in the loop. | 迴圈中每個節點只訪問一次。 | Complexity |
| Every iteration does constant pointer assignments. | 每輪只做常數次指標賦值。 | Complexity |
| No auxiliary array or stack is created. | 沒有建立額外陣列或堆疊。 | Complexity |
| Therefore runtime is linear and memory is constant. | 因此時間線性、空間常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me verify pointer update order first. | 我先確認指標更新順序。 | If stuck |
| I must save next before changing curr next. | 改 curr->next 前必須先存 next。 | If stuck |
| Otherwise I will lose the remaining list. | 不然會遺失後續串列。 | If stuck |
| The safe order is save, reverse, move prev, move curr. | 安全順序是存、反轉、移 prev、移 curr。 | If stuck |
| I think my bug is missing the save step. | 我的 bug 可能是漏掉保存步驟。 | If stuck |
| Let me patch that and rerun sample. | 我修正後重跑範例。 | If stuck |
| Now links are reversed without node loss. | 現在可反轉且不遺失節點。 | If stuck |
| Empty and single-node cases also pass. | 空串列與單節點也都通過。 | If stuck |
| Great, the new head is correct. | 很好，新 head 正確。 | If stuck |
| I can continue with final complexity summary. | 我可以接著做複雜度總結。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished iterative linked-list reversal. | 我完成了迭代反轉 linked list。 | Wrap-up |
| I validated empty, single, and normal cases. | 我驗證了空、單節點與一般案例。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can also provide recursive version trade-offs. | 我也可補充遞迴版取捨。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Reverse singly linked list and return new head. | 反轉單向串列並回傳新 head。 | Cheat sheet |
| Baseline can use array with O(n) space. | 基線可用陣列但要 O(n) 空間。 | Cheat sheet |
| Better use iterative three pointers. | 更好是迭代三指標。 | Cheat sheet |
| prev starts null, curr starts head. | prev 起始 null，curr 起始 head。 | Cheat sheet |
| Save nextTemp = curr->next first. | 先存 nextTemp=curr->next。 | Cheat sheet |
| Reverse curr->next = prev. | 反轉 curr->next=prev。 | Cheat sheet |
| Move prev = curr. | 移動 prev=curr。 | Cheat sheet |
| Move curr = nextTemp. | 移動 curr=nextTemp。 | Cheat sheet |
| Loop until curr is null. | 迴圈到 curr 為 null。 | Cheat sheet |
| Return prev. | 回傳 prev。 | Cheat sheet |
| Test empty list case. | 測空串列案例。 | Cheat sheet |
| Test single-node case. | 測單節點案例。 | Cheat sheet |
| Test two-node case. | 測雙節點案例。 | Cheat sheet |
| Test odd and even lengths. | 測奇數與偶數長度。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: not saving next pointer. | 常見 bug：未先保存 next。 | Cheat sheet |
| Common bug: wrong pointer update order. | 常見 bug：更新順序錯誤。 | Cheat sheet |
| Speak each pointer move while coding. | 寫程式時口述每次指標移動。 | Cheat sheet |
| End with new-head confirmation. | 收尾確認新 head。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Iterative O(1) pointer-reversal logic is preserved.
- No hallucinated constraints: ✅ Follows linked-list input/output behavior from source.
- Language simplicity: ✅ Short spoken lines suitable for interviews.
