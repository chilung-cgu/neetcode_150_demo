# 07 Largest Rectangle in Histogram — Interview English Script (C++)

> Source aligned with: `docs/04_Stack/07_Largest_Rectangle_in_Histogram.md`

> Quick links: [Source Solution](../07_Largest_Rectangle_in_Histogram.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| heights represents histogram bar heights with width one. | heights 代表寬度為 1 的柱高。 | Restatement |
| We need the maximum rectangle area in this histogram. | 我們要找直方圖內最大矩形面積。 | Restatement |
| Any rectangle uses contiguous bars. | 矩形一定由連續柱子組成。 | Restatement |
| I will use monotonic increasing stack of indices. | 我會用遞增單調索引 stack。 | Restatement |
| Lower bar triggers area settlement for taller bars. | 較低柱會觸發較高柱的結算。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can heights include zero-valued bars? | heights 可以包含 0 高度柱子嗎？ | Clarify |
| Is n up to 1e5, so O(n^2) is too slow? | n 到 1e5，代表 O(n^2) 不可行嗎？ | Clarify |
| Do we return area only, not boundaries? | 只需回傳面積，不需左右邊界嗎？ | Clarify |
| Can I append a virtual zero height sentinel? | 可否加一個虛擬 0 高度 sentinel？ | Clarify |
| Are 32-bit integer areas guaranteed safe? | 面積是否保證在 32-bit 範圍？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline fixes each bar as rectangle height. | 基線是固定每根柱當矩形高度。 | Approach |
| Expand left and right until hitting lower bar. | 向左右擴張直到遇到更低柱。 | Approach |
| This leads to O(n^2) in worst case. | 這在最差情況會到 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Stack keeps indices with non-decreasing heights. | stack 會維持索引對應高度非遞減。 | Approach |
| When current height is smaller, pop taller bars. | 當前高度較小時，pop 掉更高柱。 | Approach |
| For each popped bar, current index is right boundary. | 被 pop 柱的右邊界就是當前索引。 | Approach |
| New stack top gives left smaller boundary. | pop 後新 top 提供左側更小邊界。 | Approach |
| Compute area height times width and update max. | 計算高度乘寬度並更新最大值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize maxArea and empty index stack. | 先初始化 maxArea 與空的索引 stack。 | Coding |
| I iterate i from zero to n inclusive. | i 會從 0 走到 n（含 n）。 | Coding |
| At i equals n, current height is virtual zero. | 當 i=n，當前高度視為虛擬 0。 | Coding |
| While stack top height is greater than current, pop. | 當 top 高度大於當前，就持續 pop。 | Coding |
| Popped height is rectangle height candidate. | 被 pop 的高度就是矩形高度候選。 | Coding |
| Width is i if stack empty, else i minus top minus one. | 寬度是空 stack 時 i，否則 i-top-1。 | Coding |
| Update maxArea with height times width. | 用高乘寬更新 maxArea。 | Coding |
| Push current index and continue until finish. | push 當前索引後繼續直到結束。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run heights [2,1,5,6,2,3]. | 我手跑 heights [2,1,5,6,2,3]。 | Dry-run |
| Push indices for heights 2 then 1 with proper pops. | 依規則 push 2、1 對應索引並做必要 pop。 | Dry-run |
| At height 2 on index 4, bars 6 and 5 get popped. | 到 index 4 高度 2 時，6 與 5 會被 pop。 | Dry-run |
| For height 5, width becomes 2 so area is 10. | 對高度 5，寬度是 2，面積為 10。 | Dry-run |
| This becomes current maximum area. | 這成為當前最大面積。 | Dry-run |
| Sentinel zero at end flushes remaining bars. | 尾端 sentinel 0 會清空剩餘柱。 | Dry-run |
| Final maximum area stays 10. | 最終最大面積維持 10。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single bar input. | 案例一：單柱輸入。 | Edge test |
| Case two: all equal heights. | 案例二：全部等高。 | Edge test |
| Case three: strictly increasing heights. | 案例三：嚴格遞增高度。 | Edge test |
| Case four: strictly decreasing heights. | 案例四：嚴格遞減高度。 | Edge test |
| Case five: includes zero-height bars. | 案例五：包含 0 高度柱子。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(n). | 額外空間是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each index is pushed once. | 每個索引只 push 一次。 | Complexity |
| Each index is popped at most once. | 每個索引最多 pop 一次。 | Complexity |
| So stack operations are linear overall. | 因此 stack 總操作量線性。 | Complexity |
| Stack size can reach n in monotonic cases. | 在單調情境下 stack 可達 n。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate width formula carefully. | 我先仔細重述寬度公式。 | If stuck |
| Width is rightBoundary minus leftBoundary minus one. | 寬度是右邊界減左邊界再減一。 | If stuck |
| Current index is right boundary when popping. | pop 時當前索引就是右邊界。 | If stuck |
| I can explain brute force baseline first. | 我可先說明暴力基線。 | If stuck |
| Then I switch back to monotonic stack. | 再切回單調 stack。 | If stuck |
| Thanks, I found a boundary bug. | 謝謝，我找到邊界 bug。 | If stuck |
| Let me rerun [2,1,5,6,2,3]. | 我重跑 [2,1,5,6,2,3]。 | If stuck |
| Now area calculations match expected. | 現在面積計算符合預期。 | If stuck |
| Final max area is consistent now. | 最終最大面積現在一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(n). | 額外空間是 O(n)。 | Wrap-up |
| I can discuss maximal-rectangle extension if needed. | 若需要我可延伸到 maximal rectangle。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate largest-histogram-rectangle goal. | 重述直方圖最大矩形目標。 | Cheat sheet |
| Mention bars have unit width. | 提到每個柱寬都是 1。 | Cheat sheet |
| Brute force expands each bar both sides. | 暴力法對每柱向兩側擴張。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法是 O(n^2)。 | Cheat sheet |
| Use monotonic increasing index stack. | 使用遞增索引單調 stack。 | Cheat sheet |
| Pop when current height is smaller. | 當前高度較小就 pop。 | Cheat sheet |
| Popped bar sets rectangle height. | 被 pop 柱決定矩形高度。 | Cheat sheet |
| Compute width from current index and new top. | 由當前索引與新 top 算寬度。 | Cheat sheet |
| Update max area each pop. | 每次 pop 都更新最大面積。 | Cheat sheet |
| Add sentinel zero at end. | 末端加 sentinel 0。 | Cheat sheet |
| Sentinel flushes remaining stack bars. | sentinel 會清空剩餘柱。 | Cheat sheet |
| Dry-run [2,1,5,6,2,3]. | 手跑 [2,1,5,6,2,3]。 | Cheat sheet |
| Verify best area equals 10. | 驗證最佳面積等於 10。 | Cheat sheet |
| Test increasing-height input. | 測遞增高度輸入。 | Cheat sheet |
| Test decreasing-height input. | 測遞減高度輸入。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(n) extra space. | 報告 O(n) 額外空間。 | Cheat sheet |
| If stuck, recheck boundary formula. | 卡住時重檢邊界公式。 | Cheat sheet |
| Re-run sample after fixes. | 修正後重跑範例。 | Cheat sheet |
| End with concise area summary. | 以精簡面積結論收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Monotonic stack boundary-settlement logic is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
