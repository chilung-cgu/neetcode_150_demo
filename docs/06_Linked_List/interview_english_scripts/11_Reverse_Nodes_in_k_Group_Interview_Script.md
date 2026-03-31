# 11 Reverse Nodes in k-Group — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/11_Reverse_Nodes_in_k_Group.md`

> Quick links: [Source Solution](../11_Reverse_Nodes_in_k_Group.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the k-group reversal problem. | 我先重述 k 組反轉題。 | Restatement |
| We reverse list nodes in groups of size k. | 我們要每 k 個節點做一組反轉。 | Restatement |
| If remaining nodes are fewer than k, keep them unchanged. | 若剩餘節點不足 k，保持原樣。 | Restatement |
| Node values stay unchanged; only links can be rewired. | 節點值不變，只能重接鏈結。 | Restatement |
| Follow-up expects O(1) extra space. | follow-up 希望 O(1) 額外空間。 | Restatement |
| I will implement iterative group-by-group pointer reversal. | 我會用逐組迭代的指標反轉實作。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is k guaranteed to be at least one? | k 是否保證至少為 1？ | Clarify |
| Should k equals one return original list immediately? | k=1 是否直接回傳原串列？ | Clarify |
| Can input list be empty? | 輸入串列可能為空嗎？ | Clarify |
| Do you prefer iterative in-place over recursive style? | 你偏好迭代原地而非遞迴嗎？ | Clarify |
| Should I mention stack-based O(k) alternative briefly? | 要不要簡述 O(k) stack 替代法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline can push each k-group into stack then pop to reverse. | 基線可把每組 k 節點放 stack 再彈出反轉。 | Approach |
| This works but uses extra stack memory per group. | 這可行但每組需要額外堆疊空間。 | Approach |
| Time O(n), space O(k). | 時間 O(n)，空間 O(k)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use dummy node and groupPrev pointer to anchor each segment. | 用 dummy 與 groupPrev 作每組錨點。 | Approach |
| Find kth node from groupPrev to ensure enough nodes. | 從 groupPrev 找 kth 以確認節點數足夠。 | Approach |
| If kth is null, stop and keep rest unchanged. | 若 kth 為 null，就停止並保留尾段。 | Approach |
| Reverse pointers within current group using groupNext boundary. | 用 groupNext 邊界反轉當前組內指標。 | Approach |
| Reconnect reversed group and advance groupPrev. | 重新接回反轉組並推進 groupPrev。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create dummy next pointing to head. | 先建立 dummy，dummy->next 指向 head。 | Coding |
| I set groupPrev to dummy as starting anchor. | groupPrev 起始設為 dummy。 | Coding |
| I find kth node by moving k steps from groupPrev. | 從 groupPrev 往前走 k 步找 kth。 | Coding |
| If kth is missing, I break because nodes are fewer than k. | 若找不到 kth，就停止反轉。 | Coding |
| I store groupNext equals kth next for boundary control. | 存下 groupNext=kth->next 當邊界。 | Coding |
| I reverse nodes from groupPrev next to kth. | 反轉 groupPrev->next 到 kth 這段。 | Coding |
| I reconnect groupPrev next to new group head. | 把 groupPrev->next 接到新組頭。 | Coding |
| I move groupPrev to old group head for next round. | groupPrev 移到舊組頭，準備下一輪。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run head [1,2,3,4,5] with k equals 2. | 我手跑 head=[1,2,3,4,5], k=2。 | Dry-run |
| First group [1,2] reverses to [2,1]. | 第一組 [1,2] 反轉為 [2,1]。 | Dry-run |
| Current list becomes [2,1,3,4,5]. | 目前串列變成 [2,1,3,4,5]。 | Dry-run |
| Second group [3,4] reverses to [4,3]. | 第二組 [3,4] 反轉為 [4,3]。 | Dry-run |
| Current list becomes [2,1,4,3,5]. | 目前串列變成 [2,1,4,3,5]。 | Dry-run |
| Last node [5] has fewer than k, so keep it. | 最後 [5] 不足 k，保持不動。 | Dry-run |
| Final output is [2,1,4,3,5]. | 最終輸出是 [2,1,4,3,5]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty list input. | 案例一：空串列輸入。 | Edge test |
| Case two: k equals one. | 案例二：k 等於 1。 | Edge test |
| Case three: list length smaller than k. | 案例三：串列長度小於 k。 | Edge test |
| Case four: list length exactly multiple of k. | 案例四：長度剛好是 k 的倍數。 | Edge test |
| Case five: list length not multiple of k. | 案例五：長度不是 k 的倍數。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Every node participates in at most one reversal operation. | 每節點至多參與一次組內反轉。 | Complexity |
| Group boundary scans and rewiring together remain linear. | 找邊界與重接總成本維持線性。 | Complexity |
| No recursion stack or auxiliary container is used. | 不使用遞迴堆疊或額外容器。 | Complexity |
| Therefore runtime is O(n) and extra memory is O(1). | 因此時間 O(n)、額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me isolate one group and verify pointer transitions. | 我先隔離一組檢查指標轉移。 | If stuck |
| groupPrev anchors before current group. | groupPrev 要錨在當前組前一個。 | If stuck |
| kth confirms this group has enough nodes. | kth 用來確認本組節點足夠。 | If stuck |
| groupNext marks the stop boundary for reversal loop. | groupNext 是反轉迴圈停止邊界。 | If stuck |
| I might have forgotten to reconnect old head to groupNext. | 我可能忘了把舊組頭接回 groupNext。 | If stuck |
| Let me patch reconnection order carefully. | 我仔細修正重接順序。 | If stuck |
| I will rerun k=2 and k=3 samples. | 我重跑 k=2 與 k=3 範例。 | If stuck |
| Remaining nodes under k are now preserved correctly. | 不足 k 的尾段現在正確保留。 | If stuck |
| No cycles appear after rewiring. | 重接後沒有形成環。 | If stuck |
| Great, implementation is now consistent. | 很好，實作現在一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed iterative k-group reversal in-place. | 我完成了原地迭代的 k 組反轉。 | Wrap-up |
| I validated divisible and non-divisible length cases. | 我驗證了可整除與不可整除長度案例。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can compare recursion or stack alternatives if needed. | 若需要我可比較遞迴或 stack 解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Reverse linked list nodes in groups of k. | 以 k 為一組反轉 linked list。 | Cheat sheet |
| Keep leftover nodes unchanged when size < k. | 剩餘不足 k 的節點保持不變。 | Cheat sheet |
| Baseline stack method uses O(k) space. | 基線 stack 法需要 O(k) 空間。 | Cheat sheet |
| Better iterative in-place pointer reversal. | 更好是迭代原地反轉指標。 | Cheat sheet |
| Create dummy before head. | 在 head 前建立 dummy。 | Cheat sheet |
| groupPrev starts at dummy. | groupPrev 起始在 dummy。 | Cheat sheet |
| Find kth node from groupPrev. | 從 groupPrev 找 kth。 | Cheat sheet |
| If kth null, stop loop. | kth 為 null 就停止。 | Cheat sheet |
| groupNext = kth->next as boundary. | groupNext=kth->next 當邊界。 | Cheat sheet |
| Reverse group pointers up to groupNext. | 反轉直到 groupNext 為止。 | Cheat sheet |
| Reconnect groupPrev to new head. | 把 groupPrev 接到新組頭。 | Cheat sheet |
| Move groupPrev to old group head. | groupPrev 移到舊組頭。 | Cheat sheet |
| Repeat for next group. | 重複處理下一組。 | Cheat sheet |
| Test k=1 case. | 測 k=1 案例。 | Cheat sheet |
| Test length<k case. | 測長度<k 案例。 | Cheat sheet |
| Test divisible/non-divisible lengths. | 測可整除/不可整除長度。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Bug risk: wrong group reconnection. | 風險：組間重接順序錯。 | Cheat sheet |
| Bug risk: boundary stop condition error. | 風險：邊界停止條件錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Iterative O(1)-space group reversal is preserved.
- No hallucinated constraints: ✅ Uses source k-group semantics and edge rules.
- Language simplicity: ✅ Interview-friendly concise lines.
