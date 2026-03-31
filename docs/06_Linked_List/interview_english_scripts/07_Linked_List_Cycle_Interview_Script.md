# 07 Linked List Cycle — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/07_Linked_List_Cycle.md`

> Quick links: [Source Solution](../07_Linked_List_Cycle.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate this cycle-detection problem. | 我先重述偵測環的題目。 | Restatement |
| We are given the head of a linked list. | 我們拿到 linked list 的 head。 | Restatement |
| We only need to return whether a cycle exists. | 我們只要回傳是否有環。 | Restatement |
| We are asked to use constant extra memory if possible. | 題目希望用常數額外空間。 | Restatement |
| I will use Floyd slow-fast pointer method. | 我會用 Floyd 快慢指標法。 | Restatement |
| If slow meets fast, the list has a cycle. | 若 slow 與 fast 相遇，就代表有環。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can the input head be null? | 輸入 head 可能是 null 嗎？ | Clarify |
| Is returning boolean enough with no extra metadata? | 只回傳布林值即可，不需其他資訊嗎？ | Clarify |
| Should I prioritize O(1) space over hash-set approach? | 我應優先 O(1) 空間解法嗎？ | Clarify |
| Are node values irrelevant to cycle detection logic? | 節點值是否與偵測邏輯無關？ | Clarify |
| Do you want follow-up discussion for finding cycle entry? | 要不要延伸討論環入口定位？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline stores visited node addresses in a hash set. | 基線是用 hash set 記錄走過的節點位址。 | Approach |
| If current node already exists in set, cycle is found. | 若當前節點已在 set 內，就有環。 | Approach |
| Time O(n), space O(n). | 時間 O(n)，空間 O(n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Slow moves one step, fast moves two steps each round. | slow 每輪走一步，fast 每輪走兩步。 | Approach |
| If no cycle exists, fast hits null first. | 無環時 fast 會先碰到 null。 | Approach |
| If cycle exists, fast eventually laps and meets slow. | 有環時 fast 會追上 slow。 | Approach |
| Meeting condition directly proves cycle existence. | 相遇條件可直接證明存在環。 | Approach |
| This gives O(n) time and O(1) extra space. | 可達 O(n) 時間與 O(1) 額外空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I return false if head is null. | 先判斷 head 為 null 就回傳 false。 | Coding |
| I initialize slow and fast to head. | 將 slow 與 fast 都設在 head。 | Coding |
| I loop while fast and fast next are not null. | 當 fast 與 fast->next 都非 null 時迴圈。 | Coding |
| I move slow by one and fast by two. | slow 前進一步，fast 前進兩步。 | Coding |
| After movement I compare slow and fast pointers. | 移動後比較 slow 與 fast 指標。 | Coding |
| If they meet, I return true immediately. | 若相遇就立即回傳 true。 | Coding |
| If loop exits, fast reached tail and no cycle exists. | 若迴圈退出，代表 fast 到尾端且無環。 | Coding |
| Finally I return false. | 最後回傳 false。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run head [3,2,0,-4] with tail linking to index one. | 我手跑 [3,2,0,-4] 且尾巴連回索引 1。 | Dry-run |
| Start slow and fast both at node 3. | 起始 slow 與 fast 都在節點 3。 | Dry-run |
| Round one: slow at 2, fast at 0. | 第一輪後 slow 在 2，fast 在 0。 | Dry-run |
| Round two: slow at 0, fast at 2. | 第二輪後 slow 在 0，fast 在 2。 | Dry-run |
| Round three: slow at -4, fast at -4. | 第三輪後 slow 在 -4，fast 也在 -4。 | Dry-run |
| Pointers meet, so cycle exists. | 指標相遇，因此存在環。 | Dry-run |
| Return true as expected. | 依預期回傳 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty list. | 案例一：空串列。 | Edge test |
| Case two: single node without self-loop. | 案例二：單節點且不自環。 | Edge test |
| Case three: single node with self-loop. | 案例三：單節點且自環。 | Edge test |
| Case four: multi-node list without cycle. | 案例四：多節點但無環。 | Edge test |
| Case five: cycle starts near tail or near head. | 案例五：環入口靠近尾端或頭端。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| In non-cycle case, fast reaches null after linear traversal. | 無環時 fast 會在線性步數內到達 null。 | Complexity |
| In cycle case, pointers meet after at most linear total steps. | 有環時兩指標也會在線性步數內相遇。 | Complexity |
| Each round only updates two pointers. | 每輪只更新兩個指標。 | Complexity |
| No hash set or extra container is allocated. | 不需要 hash set 或其他額外容器。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me check loop guards for fast pointer safety. | 我先確認 fast 的安全迴圈條件。 | If stuck |
| I must require both fast and fast next non-null. | 必須同時檢查 fast 與 fast->next 非 null。 | If stuck |
| Comparison should happen after moving pointers. | 指標移動後才做相遇比較。 | If stuck |
| If I compare before move, I may get false positive at start. | 若先比對，起點可能誤判。 | If stuck |
| I might have used fast one-step by mistake. | 我可能把 fast 寫成只走一步。 | If stuck |
| Fast must move two steps to guarantee detection logic. | fast 必須走兩步才能保證邏輯。 | If stuck |
| Let me rerun cycle and non-cycle samples. | 我重跑有環與無環樣本。 | If stuck |
| Now one returns true and the other returns false. | 現在一個回 true、另一個回 false。 | If stuck |
| Edge cases also pass. | 邊界案例也都通過。 | If stuck |
| Great, implementation is correct now. | 很好，實作現在正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished Floyd cycle-detection implementation. | 我完成了 Floyd 環偵測實作。 | Wrap-up |
| I validated empty, single-node, and cyclic cases. | 我驗證了空串列、單節點與有環案例。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can extend this to find cycle entry if needed. | 若需要我可延伸到環入口定位。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Detect whether linked list has cycle. | 判斷 linked list 是否有環。 | Cheat sheet |
| Return boolean only. | 只需回傳布林值。 | Cheat sheet |
| Baseline hash set is O(n) space. | 基線 hash set 是 O(n) 空間。 | Cheat sheet |
| Better use slow-fast pointers. | 更好是快慢指標。 | Cheat sheet |
| slow moves one step. | slow 每輪走一步。 | Cheat sheet |
| fast moves two steps. | fast 每輪走兩步。 | Cheat sheet |
| Loop guard: fast && fast->next. | 迴圈條件：fast 與 fast->next。 | Cheat sheet |
| Move pointers then compare. | 先移動再比較。 | Cheat sheet |
| Meeting means cycle exists. | 相遇代表有環。 | Cheat sheet |
| Hitting null means no cycle. | 碰到 null 代表無環。 | Cheat sheet |
| Return false after loop end. | 迴圈結束回傳 false。 | Cheat sheet |
| Test empty list. | 測空串列。 | Cheat sheet |
| Test single node no cycle. | 測單節點無環。 | Cheat sheet |
| Test single node self-cycle. | 測單節點自環。 | Cheat sheet |
| Test normal multi-node cycle. | 測一般多節點有環。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Bug risk: missing fast->next guard. | 風險：漏檢 fast->next。 | Cheat sheet |
| Bug risk: comparing before movement. | 風險：移動前先比較。 | Cheat sheet |
| Mention cycle-entry follow-up if asked. | 若被問可延伸環入口題。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Floyd fast/slow cycle detection is preserved.
- No hallucinated constraints: ✅ Uses source cycle semantics and constraints.
- Language simplicity: ✅ Short lines for smooth interview delivery.
