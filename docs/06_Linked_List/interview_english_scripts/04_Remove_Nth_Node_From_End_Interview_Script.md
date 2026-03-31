# 04 Remove Nth Node From End of List — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/04_Remove_Nth_Node_From_End.md`

> Quick links: [Source Solution](../04_Remove_Nth_Node_From_End.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate this linked-list deletion problem. | 我先重述這題刪除節點問題。 | Restatement |
| We must remove the nth node counting from the end. | 我們要刪除倒數第 n 個節點。 | Restatement |
| Return the head of the updated list. | 回傳更新後串列的 head。 | Restatement |
| A one-pass approach is expected by follow-up. | follow-up 通常希望一次掃描完成。 | Restatement |
| I will use two pointers with a dummy node. | 我會用兩指標配 dummy 節點。 | Restatement |
| This handles deleting the original head safely. | 這可安全處理刪除原本 head 的情況。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume n is always valid within list length? | 我可以假設 n 一定不超過串列長度嗎？ | Clarify |
| Should deleting head be handled in same function path? | 刪 head 是否要在同一路徑處理？ | Clarify |
| Do you prefer one-pass method over two-pass length method? | 你偏好 one-pass 而不是先算長度嗎？ | Clarify |
| Is list length at least one in constraints? | 限制是否保證串列至少一個節點？ | Clarify |
| Should node memory cleanup be mentioned in C++ context? | C++ 版本要不要口頭提到記憶體釋放？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline does two passes: first for length, second for deletion index. | 基線兩趟：先算長度，再找刪除位置。 | Approach |
| Delete at position length minus n from start. | 從頭數到 length-n 的位置執行刪除。 | Approach |
| Time O(L), space O(1), but not one-pass. | 時間 O(L)、空間 O(1)，但非一趟。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Add dummy before head, set fast and slow at dummy. | 在 head 前加 dummy，fast/slow 都在 dummy。 | Approach |
| Move fast ahead by n steps first. | 先讓 fast 前進 n 步。 | Approach |
| Move both pointers until fast reaches list tail. | 再同步移動直到 fast 到尾端。 | Approach |
| Then slow is right before target node to remove. | 此時 slow 正好在待刪節點前一個。 | Approach |
| Bypass slow next and return dummy next. | 讓 slow 跳過下一節點，回傳 dummy->next。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create a dummy node pointing to head. | 先建立指向 head 的 dummy 節點。 | Coding |
| I initialize fast and slow pointers at dummy. | fast 與 slow 都從 dummy 出發。 | Coding |
| I move fast forward by n steps. | 讓 fast 先前進 n 步。 | Coding |
| Then I move fast and slow together until fast next is null. | 再同步前進直到 fast->next 為 null。 | Coding |
| Now slow next is the node we need to delete. | 此時 slow->next 就是待刪節點。 | Coding |
| I rewire slow next to skip that node. | 重新連接 slow->next 跳過該節點。 | Coding |
| Optionally free removed node in C++ implementation. | 在 C++ 可選擇釋放被刪節點記憶體。 | Coding |
| Finally I return dummy next as new head. | 最後回傳 dummy->next 作為新 head。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run head [1,2,3,4,5] with n equals 2. | 我手跑 head=[1,2,3,4,5]、n=2。 | Dry-run |
| Fast moves two steps to node 2. | fast 先走兩步到節點 2。 | Dry-run |
| Move both pointers together until fast reaches node 5. | 接著雙指標同走直到 fast 到節點 5。 | Dry-run |
| Slow stops at node 3. | slow 最後停在節點 3。 | Dry-run |
| Slow next is node 4, which is nth from end. | slow 的 next 是節點 4，即倒數第 2 個。 | Dry-run |
| Bypass node 4, list becomes [1,2,3,5]. | 跳過節點 4 後，串列變 [1,2,3,5]。 | Dry-run |
| Return updated head from dummy next. | 從 dummy->next 回傳更新後 head。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single node with n equals 1. | 案例一：單節點且 n=1。 | Edge test |
| Case two: deleting original head in multi-node list. | 案例二：多節點中刪掉原 head。 | Edge test |
| Case three: deleting last node with n equals 1. | 案例三：n=1 刪除尾節點。 | Edge test |
| Case four: deleting middle node. | 案例四：刪除中間節點。 | Edge test |
| Case five: two-node list deleting first or second. | 案例五：雙節點刪第一或第二個。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(L). | 時間複雜度是 O(L)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Fast pointer advances at most list length steps. | fast 指標最多走過整個串列一次。 | Complexity |
| Slow pointer also advances linearly. | slow 指標同樣是線性前進。 | Complexity |
| Pointer rewiring is constant-time after traversal. | 走訪後的指標重接是常數時間。 | Complexity |
| No extra list-sized storage is used. | 不需要與串列長度同級的額外儲存。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me verify fast-gap invariant first. | 我先確認 fast 與 slow 的間距不變量。 | If stuck |
| Gap between fast and slow should stay n nodes. | fast 與 slow 應維持 n 節點間距。 | If stuck |
| I should move fast n steps before joint movement. | 共同移動前要先讓 fast 走 n 步。 | If stuck |
| Dummy node helps when deleting the original head. | dummy 節點可處理刪 head。 | If stuck |
| I may have stopped at fast null instead of fast next null. | 我可能把停止條件寫成 fast==null。 | If stuck |
| Let me correct that boundary condition. | 我修正這個邊界條件。 | If stuck |
| I rerun head-removal and tail-removal cases. | 我重跑刪 head 與刪尾案例。 | If stuck |
| Now deletion position is accurate. | 現在刪除位置正確。 | If stuck |
| Returned head is also correct. | 回傳 head 也正確。 | If stuck |
| Great, one-pass logic is stable. | 很好，一趟解法穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed one-pass remove-nth-from-end solution. | 我完成了 one-pass 刪倒數第 n 節點解法。 | Wrap-up |
| I validated head, middle, and tail deletions. | 我驗證了刪頭、刪中、刪尾三類情況。 | Wrap-up |
| Runtime is O(L). | 時間複雜度是 O(L)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can compare with two-pass approach if needed. | 若需要我可比較兩趟解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Remove nth node from end. | 刪除倒數第 n 個節點。 | Cheat sheet |
| Return updated head. | 回傳更新後 head。 | Cheat sheet |
| Baseline two-pass uses length first. | 基線兩趟先算長度。 | Cheat sheet |
| Better one-pass with two pointers. | 更好是一趟雙指標。 | Cheat sheet |
| Add dummy before head. | 在 head 前加 dummy。 | Cheat sheet |
| fast and slow start at dummy. | fast/slow 都從 dummy 出發。 | Cheat sheet |
| Move fast by n steps. | 先讓 fast 走 n 步。 | Cheat sheet |
| Move both while fast->next exists. | fast->next 存在時雙指標同走。 | Cheat sheet |
| slow->next is target node. | slow->next 就是待刪節點。 | Cheat sheet |
| Rewire slow->next = slow->next->next. | 重接 slow->next 跳過目標。 | Cheat sheet |
| Return dummy->next. | 回傳 dummy->next。 | Cheat sheet |
| Test single-node n=1. | 測單節點 n=1。 | Cheat sheet |
| Test deleting head case. | 測刪 head 案例。 | Cheat sheet |
| Test deleting tail case. | 測刪尾節點案例。 | Cheat sheet |
| Test deleting middle case. | 測刪中間節點案例。 | Cheat sheet |
| Time O(L). | 時間 O(L)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Bug risk: wrong fast stop condition. | 風險：fast 停止條件錯。 | Cheat sheet |
| Bug risk: forgetting dummy node. | 風險：忘記使用 dummy。 | Cheat sheet |
| Explain gap invariant clearly. | 口述清楚間距不變量。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ One-pass fast/slow with dummy logic is preserved.
- No hallucinated constraints: ✅ Uses source-linked-list deletion semantics.
- Language simplicity: ✅ Interview-oriented concise spoken lines.
