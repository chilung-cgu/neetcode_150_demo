# 02 Min Stack — Interview English Script (C++)

> Source aligned with: `docs/04_Stack/02_Min_Stack.md`

> Quick links: [Source Solution](../02_Min_Stack.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We need a stack with push, pop, top, and getMin. | 我們要實作含 push/pop/top/getMin 的 stack。 | Restatement |
| All operations should run in O(1) time. | 所有操作都要 O(1) 時間。 | Restatement |
| getMin is the key requirement here. | 核心要求是 getMin。 | Restatement |
| I will use two synchronized stacks. | 我會用兩個同步 stack。 | Restatement |
| One stores values and one stores running minimum. | 一個存值，一個存目前最小值。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume every pop and top call is valid? | 可否假設每次 pop/top 呼叫都合法？ | Clarify |
| Is getMin also guaranteed to be called on non-empty stack? | getMin 是否也保證在非空時呼叫？ | Clarify |
| Do we need class-style API exactly as prompt? | 需要完全依題目 class API 嗎？ | Clarify |
| Is O(1) worst-case required, not amortized? | 要求 O(1) 最差時間，不是均攤嗎？ | Clarify |
| Can I mention pair-stack variant as alternative? | 我可補充 pair-stack 變體嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline stores only values in one stack. | 基線是只用單一 stack 存值。 | Approach |
| For getMin, scan all elements to find minimum. | 每次 getMin 都線性掃描求最小值。 | Approach |
| This breaks O(1) requirement with O(n) query. | 這會變成 O(n) 查詢，不符要求。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Keep main stack for values. | 主 stack 存放原始值。 | Approach |
| Keep min stack for minimum at each depth. | min stack 存每層深度的最小值。 | Approach |
| On push, minStack pushes min(val, minStack.top). | push 時 minStack 推入 min(val,目前最小)。 | Approach |
| On pop, pop both stacks together. | pop 時兩個 stack 同步 pop。 | Approach |
| Then top and getMin are direct O(1) lookups. | 如此 top 與 getMin 都可 O(1) 取值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize value stack and min stack. | 先初始化 value stack 與 min stack。 | Coding |
| In push, I always push val into value stack. | push 時一定先把 val 放入 value stack。 | Coding |
| For min stack, push current minimum at this depth. | min stack 推入當前深度的最小值。 | Coding |
| In pop, remove top from both stacks together. | pop 時同步移除兩個 stack 的頂端。 | Coding |
| top simply returns valueStack.top. | top 直接回傳 valueStack.top。 | Coding |
| getMin simply returns minStack.top. | getMin 直接回傳 minStack.top。 | Coding |
| This keeps both stacks perfectly aligned in size. | 這可維持兩個 stack 大小完全對齊。 | Coding |
| So each API call stays O(1). | 因此每個 API 呼叫都維持 O(1)。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run push -2, push 0, push -3. | 我手跑 push -2、push 0、push -3。 | Dry-run |
| value stack is [-2,0,-3]. | value stack 會是 [-2,0,-3]。 | Dry-run |
| min stack is [-2,-2,-3]. | min stack 會是 [-2,-2,-3]。 | Dry-run |
| getMin returns top of min stack, so -3. | getMin 取 min stack top，所以是 -3。 | Dry-run |
| pop removes -3 from both stacks. | pop 會把兩邊的 -3 同步移除。 | Dry-run |
| top is now 0, and getMin is now -2. | 現在 top 是 0，getMin 是 -2。 | Dry-run |
| This matches expected behavior. | 這與預期行為一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single push then getMin. | 案例一：單次 push 後 getMin。 | Edge test |
| Case two: strictly decreasing pushes. | 案例二：連續遞減 push。 | Edge test |
| Case three: strictly increasing pushes. | 案例三：連續遞增 push。 | Edge test |
| Case four: repeated minimum values. | 案例四：最小值重複出現。 | Edge test |
| Case five: alternate push and pop many times. | 案例五：大量交錯 push/pop。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each operation is O(1). | 每個操作都是 O(1)。 | Complexity |
| Total extra space is O(n). | 總額外空間是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| push does constant comparisons and pushes. | push 只做常數次比較與 push。 | Complexity |
| pop, top, and getMin are direct top/pop operations. | pop/top/getMin 都是直接 top/pop 操作。 | Complexity |
| There is no traversal in any API call. | 所有 API 都不需要遍歷。 | Complexity |
| Two stacks together store linear number of entries. | 兩個 stack 合計儲存線性數量元素。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate the O(1) requirement. | 我先重述 O(1) 要求。 | If stuck |
| Single stack plus scan cannot satisfy getMin. | 單 stack 加掃描無法滿足 getMin。 | If stuck |
| I should maintain min state per depth. | 我應維護每層深度的最小值狀態。 | If stuck |
| I can explain brute-force baseline first. | 我可先說明暴力基線。 | If stuck |
| Then I switch to synchronized two stacks. | 再切回同步雙 stack。 | If stuck |
| Thanks, I found desync in pop logic. | 謝謝，我找到 pop 同步錯誤。 | If stuck |
| Let me rerun the sample operations. | 我重跑範例操作序列。 | If stuck |
| Now min stack stays aligned correctly. | 現在 min stack 對齊正確。 | If stuck |
| All API outputs are consistent now. | 現在所有 API 輸出一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(1). | 時間是 O(1)。 | Wrap-up |
| Space is O(n). | 空間是 O(n)。 | Wrap-up |
| I can discuss pair-based single-stack variant if needed. | 若需要我可補充 pair 單 stack 變體。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate MinStack API goal. | 重述 MinStack API 目標。 | Cheat sheet |
| Highlight O(1) for all operations. | 強調所有操作都要 O(1)。 | Cheat sheet |
| Baseline scan for min is too slow. | 掃描找最小值太慢。 | Cheat sheet |
| Use two synchronized stacks. | 使用兩個同步 stack。 | Cheat sheet |
| valueStack stores pushed values. | valueStack 存原始值。 | Cheat sheet |
| minStack stores running minimums. | minStack 存當前最小值。 | Cheat sheet |
| push updates both stacks. | push 會更新兩個 stack。 | Cheat sheet |
| pop removes from both stacks. | pop 會同時移除兩邊。 | Cheat sheet |
| top returns valueStack top. | top 回傳 valueStack top。 | Cheat sheet |
| getMin returns minStack top. | getMin 回傳 minStack top。 | Cheat sheet |
| Dry-run push -2,0,-3 sequence. | 手跑 push -2,0,-3 序列。 | Cheat sheet |
| Verify getMin then pop then getMin. | 驗證 getMin、pop、再 getMin。 | Cheat sheet |
| Test repeated minimum values. | 測最小值重複案例。 | Cheat sheet |
| Test increasing push sequence. | 測遞增 push 序列。 | Cheat sheet |
| Report O(1) per operation. | 報告每個操作 O(1)。 | Cheat sheet |
| Report O(n) extra space. | 報告 O(n) 額外空間。 | Cheat sheet |
| Mention pair-stack alternative. | 提及 pair-stack 替代方案。 | Cheat sheet |
| If stuck, recheck pop synchronization. | 卡住時重檢 pop 同步。 | Cheat sheet |
| Re-run sample after fix. | 修正後重跑範例。 | Cheat sheet |
| End with concise API summary. | 以精簡 API 總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Two-stack running-min design is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
