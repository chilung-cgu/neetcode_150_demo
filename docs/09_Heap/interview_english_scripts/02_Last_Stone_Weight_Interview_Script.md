# 02 Last Stone Weight — Interview English Script (C++)

> Source aligned with: `docs/09_Heap/02_Last_Stone_Weight.md`

> Quick links: [Source Solution](../02_Last_Stone_Weight.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the last-stone-weight problem. | 我先重述最後石頭重量題。 | Restatement |
| We repeatedly smash the two heaviest stones. | 我們會反覆敲碎最重的兩顆石頭。 | Restatement |
| If weights are equal, both disappear. | 若重量相同，兩顆都消失。 | Restatement |
| If not equal, we push back their difference. | 若不同，就把差值放回集合。 | Restatement |
| Continue until zero or one stone remains. | 持續到剩零顆或一顆。 | Restatement |
| I will use max-heap for efficient heaviest extraction. | 我會用 max-heap 高效取最大值。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is returning zero correct when no stones remain? | 沒石頭時回傳 0 是正確嗎？ | Clarify |
| Do we always choose exactly the two heaviest stones each round? | 每輪都必須選最重兩顆嗎？ | Clarify |
| Is input size small enough but still expected to use heap? | 輸入雖小但仍希望用 heap 嗎？ | Clarify |
| Are stone weights always positive integers? | 石頭重量都為正整數嗎？ | Clarify |
| Can we mutate input container during processing? | 處理過程可修改輸入容器嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force sorts the list each round to get top two. | 暴力法每輪排序以取前兩大。 | Approach |
| After smashing, update list and sort again. | 敲碎後更新清單再重排一次。 | Approach |
| Repeated sorting leads to unnecessary overhead. | 反覆排序造成多餘成本。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use max-heap built from all initial stones. | 把初始石頭全建成 max-heap。 | Approach |
| While heap has at least two stones, pop two largest. | 當 heap 至少兩顆時彈出兩個最大。 | Approach |
| Compute difference between larger and smaller. | 計算大者減小者的差值。 | Approach |
| If difference is non-zero, push it back into heap. | 差值非零就推回 heap。 | Approach |
| Final answer is heap top or zero if empty. | 最後答案是 heap top，空則 0。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize priority_queue as max-heap with input stones. | 我先用輸入 stones 初始化 max-heap。 | Coding |
| Loop while heap size is greater than one. | 當 heap 大小大於 1 時進迴圈。 | Coding |
| I pop first heaviest stone y. | 我先彈出最重石頭 y。 | Coding |
| I pop second heaviest stone x. | 再彈出次重石頭 x。 | Coding |
| If y and x differ, I push y minus x. | 若 y 與 x 不同，推入 y-x。 | Coding |
| If equal, nothing is pushed back. | 若相同，就不推回任何值。 | Coding |
| Continue until one or zero stones remain. | 持續到剩一顆或零顆。 | Coding |
| Return heap top if not empty, otherwise zero. | heap 非空回 top，否則回 0。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run stones [2,7,4,1,8,1]. | 我手跑 stones [2,7,4,1,8,1]。 | Dry-run |
| Pop 8 and 7, push difference 1. | 彈 8 與 7，推回差值 1。 | Dry-run |
| Heap now effectively has [4,2,1,1,1]. | 此時 heap 等效為 [4,2,1,1,1]。 | Dry-run |
| Pop 4 and 2, push difference 2. | 彈 4 與 2，推回差值 2。 | Dry-run |
| Pop 2 and 1, push difference 1. | 彈 2 與 1，推回差值 1。 | Dry-run |
| Pop 1 and 1, both disappear. | 彈 1 與 1，兩顆都消失。 | Dry-run |
| One stone of weight 1 remains, answer is 1. | 最後剩 1，答案是 1。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single stone input returns itself. | 案例一：單顆石頭直接回自身。 | Edge test |
| Case two: two equal stones return zero. | 案例二：兩顆同重應回 0。 | Edge test |
| Case three: all stones equal and even count returns zero. | 案例三：全等且偶數顆應回 0。 | Edge test |
| Case four: all stones equal and odd count returns that weight. | 案例四：全等且奇數顆應回該重量。 | Edge test |
| Case five: strictly increasing weights stress heap extraction order. | 案例五：遞增重量測試 heap 取值順序。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log n). | 時間複雜度是 O(n log n)。 | Complexity |
| Space complexity is O(n). | 空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Building heap from n stones takes O(n). | 由 n 顆石頭建 heap 為 O(n)。 | Complexity |
| Each loop pops twice and may push once, each O(log n). | 每輪兩次 pop 可能一次 push，單次 O(log n)。 | Complexity |
| Number of rounds is at most n minus one. | 回合數最多是 n-1。 | Complexity |
| Total runtime is O(n log n), memory is heap O(n). | 總時間 O(n log n)，記憶體為 heap 的 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on operation that repeats: extract two maxima. | 我先聚焦重複操作：取兩個最大值。 | If stuck |
| This is exactly what max-heap is for. | 這正是 max-heap 的用途。 | If stuck |
| I might have used min-heap by mistake. | 我可能誤用了 min-heap。 | If stuck |
| Let me switch to priority_queue default max behavior. | 我改回 priority_queue 預設 max 行為。 | If stuck |
| I also need loop condition size greater than one. | 迴圈條件也要是 size>1。 | If stuck |
| I will rerun [2,7,4,1,8,1] sample. | 我重跑 [2,7,4,1,8,1] 範例。 | If stuck |
| It now returns one correctly. | 現在可正確回傳 1。 | If stuck |
| I test equal pair [5,5] too. | 我也測 [5,5] 相等組。 | If stuck |
| It returns zero as expected. | 會如預期回傳 0。 | If stuck |
| Great, heap loop logic is stable now. | 很好，heap 迴圈邏輯已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed stone-smash simulation with max-heap. | 我完成了以 max-heap 模擬敲石頭流程。 | Wrap-up |
| Each round extracts two largest stones efficiently. | 每輪都能高效取出兩顆最大石頭。 | Wrap-up |
| Runtime is O(n log n). | 時間複雜度是 O(n log n)。 | Wrap-up |
| Space is O(n). | 空間複雜度是 O(n)。 | Wrap-up |
| I can contrast this with repeated-sorting baseline if needed. | 若需要我可對比反覆排序基線。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Repeatedly smash two heaviest stones. | 反覆敲碎最重兩顆石頭。 | Cheat sheet |
| Use max-heap for fast largest extraction. | 用 max-heap 快速取最大。 | Cheat sheet |
| Build heap from all stones. | 先由所有 stones 建 heap。 | Cheat sheet |
| While size > 1 keep processing. | 當 size>1 持續處理。 | Cheat sheet |
| Pop y as largest. | 彈出最大 y。 | Cheat sheet |
| Pop x as second largest. | 彈出次大 x。 | Cheat sheet |
| If y != x push y-x. | 若 y!=x 推回 y-x。 | Cheat sheet |
| If y == x push nothing. | 若 y==x 不推回。 | Cheat sheet |
| End when one or zero stones left. | 剩一顆或零顆時結束。 | Cheat sheet |
| Return top or 0. | 回傳 top 或 0。 | Cheat sheet |
| Single stone returns itself. | 單顆石頭回自身。 | Cheat sheet |
| Equal pair returns 0. | 相等一對回 0。 | Cheat sheet |
| Time O(n log n). | 時間 O(n log n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Common bug: wrong heap direction. | 常見錯誤：heap 方向寫反。 | Cheat sheet |
| Common bug: wrong loop condition. | 常見錯誤：迴圈條件錯誤。 | Cheat sheet |
| Validate with [2,7,4,1,8,1]. | 用 [2,7,4,1,8,1] 驗證。 | Cheat sheet |
| Difference operation is y-x where y>=x. | 差值運算是 y-x（y>=x）。 | Cheat sheet |
| Mention sorting baseline alternative. | 可提排序基線替代法。 | Cheat sheet |
| End with heap invariant summary. | 收尾總結 heap 不變量。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Max-heap smash simulation is preserved.
- No hallucinated constraints: ✅ Rules and output behavior follow source description.
- Language simplicity: ✅ Short natural interview-spoken lines.
