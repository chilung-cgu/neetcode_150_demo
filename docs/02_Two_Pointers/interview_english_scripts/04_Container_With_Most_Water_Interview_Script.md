# 04 Container With Most Water — Interview English Script (C++)

> Source aligned with: `docs/02_Two_Pointers/04_Container_With_Most_Water.md`

> Quick links: [Source Solution](../04_Container_With_Most_Water.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We have heights of vertical lines. | 我們有一排垂直線高度。 | Restatement |
| We choose two lines to form a container. | 我們選兩條線形成容器。 | Restatement |
| Area is min height times width. | 面積是短邊高度乘寬度。 | Restatement |
| We need the maximum possible area. | 我們要找最大面積。 | Restatement |
| I will use greedy two pointers. | 我會使用貪心雙指標。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are all heights non-negative integers? | 所有高度都為非負整數嗎？ | Clarify |
| Is n large enough that O(n^2) is too slow? | n 是否大到 O(n^2) 會太慢？ | Clarify |
| We only return max area, not indices, right? | 只要回傳最大面積，不要索引，對嗎？ | Clarify |
| If length is less than two, should return zero? | 若長度小於 2，是否回傳 0？ | Clarify |
| Should I mention potential integer overflow risk? | 需不需要提到整數溢位風險？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline checks every pair of lines. | 基線是檢查每一對線。 | Approach |
| Compute area for each pair and keep max. | 每對都算面積並更新最大值。 | Approach |
| Time O(n^2), space O(1). | 時間 O(n^2)，空間 O(1)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Start with left at zero and right at n minus one. | 從 left=0、right=n-1 開始。 | Approach |
| This gives the widest possible container first. | 這先給出最大寬度的容器。 | Approach |
| Move the shorter side inward each step. | 每一步都移動較短那一側。 | Approach |
| Moving taller side cannot improve current short limit. | 移動較高邊無法改善目前短板限制。 | Approach |
| So we get O(n) time and O(1) space. | 因此可達 O(n) 時間與 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize left, right, and best area. | 先初始化 left、right、best。 | Coding |
| While left is smaller than right, I compute width. | 當 left < right，我先算寬度。 | Coding |
| Then I get effective height by min of both sides. | 再用兩側較小高度當有效高度。 | Coding |
| I update best with current area. | 我用當前面積更新 best。 | Coding |
| If left height is smaller, I increment left. | 若左邊較矮，就遞增 left。 | Coding |
| Otherwise I decrement right. | 否則就遞減 right。 | Coding |
| This keeps only candidates that may beat current best. | 這只保留可能超越目前 best 的候選。 | Coding |
| Finally I return best area. | 最後回傳最大面積。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [1,8,6,2,5,4,8,3,7]. | 我手跑 [1,8,6,2,5,4,8,3,7]。 | Dry-run |
| Start left at 0 and right at 8. | 起始 left=0、right=8。 | Dry-run |
| Area is min(1,7) times 8, so 8. | 面積是 min(1,7)×8，所以是 8。 | Dry-run |
| Left side is shorter, move left to 1. | 左邊較短，left 移到 1。 | Dry-run |
| Now area is min(8,7) times 7, so 49. | 現在面積是 min(8,7)×7，也就是 49。 | Dry-run |
| Continue shrinking pointers, no area beats 49. | 繼續內縮後，沒有面積超過 49。 | Dry-run |
| Final answer is 49. | 最終答案是 49。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: minimum valid size like [1,1]. | 案例一：最小有效長度如 [1,1]。 | Edge test |
| Case two: strictly increasing heights. | 案例二：高度嚴格遞增。 | Edge test |
| Case three: strictly decreasing heights. | 案例三：高度嚴格遞減。 | Edge test |
| Case four: many equal heights like [5,5,5,5]. | 案例四：大量相同高度如 [5,5,5,5]。 | Edge test |
| Case five: includes zeros such as [0,2,0,4]. | 案例五：包含 0 的情況如 [0,2,0,4]。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each loop moves one pointer inward exactly once. | 每次迴圈都把一個指標內縮一次。 | Complexity |
| Total pointer moves are at most n minus one per side. | 指標總移動次數最多線性級別。 | Complexity |
| So runtime is linear in array length. | 因此執行時間對陣列長度是線性。 | Complexity |
| We only keep left, right, and best variables. | 我們只需 left、right、best 這些常數變數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate area formula quickly. | 我先快速重述面積公式。 | If stuck |
| Width shrinks every move, that part is fixed. | 每次移動寬度都會縮小，這點固定。 | If stuck |
| I should move the shorter side, not taller side. | 我應移動短邊，不是長邊。 | If stuck |
| I can show brute force first if needed. | 若需要我可先講暴力法。 | If stuck |
| Then I switch back to O(n) pointers. | 接著再切回 O(n) 雙指標。 | If stuck |
| Thanks, I found the wrong pointer branch. | 謝謝，我找到錯誤的指標分支。 | If stuck |
| Let me rerun the sample from both ends. | 我再從兩端重跑一次範例。 | If stuck |
| Now the update order is correct. | 現在更新順序正確。 | If stuck |
| The result is stable at maximum area. | 結果已穩定在最大面積。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can explain greedy proof if needed. | 若需要我可補充貪心正確性證明。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate max water container goal. | 重述最大盛水容器目標。 | Cheat sheet |
| Mention area equals min height times width. | 提到面積是短邊乘寬度。 | Cheat sheet |
| Brute force checks all pairs. | 暴力法檢查所有配對。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法是 O(n^2)。 | Cheat sheet |
| Optimized uses two pointers. | 優化法使用雙指標。 | Cheat sheet |
| Start from both ends for max width. | 從兩端開始以取得最大寬度。 | Cheat sheet |
| Compute area each iteration. | 每輪都計算一次面積。 | Cheat sheet |
| Update global best area. | 更新全域最大面積。 | Cheat sheet |
| Move shorter side inward. | 將短邊往內移。 | Cheat sheet |
| Do not move taller side first. | 不要優先移動長邊。 | Cheat sheet |
| Keep looping until pointers meet. | 持續迴圈直到指標相遇。 | Cheat sheet |
| Dry-run [1,8,6,2,5,4,8,3,7]. | 手跑 [1,8,6,2,5,4,8,3,7]。 | Cheat sheet |
| Confirm answer is 49. | 確認答案為 49。 | Cheat sheet |
| Test monotonic increasing case. | 測單調遞增案例。 | Cheat sheet |
| Test monotonic decreasing case. | 測單調遞減案例。 | Cheat sheet |
| Test equal-height case. | 測等高案例。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(1) extra space. | 報告 O(1) 額外空間。 | Cheat sheet |
| If stuck, restate move rule. | 卡住時重述移動規則。 | Cheat sheet |
| End with concise summary. | 用精簡總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Greedy two-pointer logic and move rule are preserved.
- No hallucinated constraints: ✅ Uncertain details are asked in clarification lines.
- Language simplicity: ✅ Short spoken lines for interview delivery.
