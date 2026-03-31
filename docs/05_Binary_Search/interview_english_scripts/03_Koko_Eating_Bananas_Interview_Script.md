# 03 Koko Eating Bananas — Interview English Script (C++)

> Source aligned with: `docs/05_Binary_Search/03_Koko_Eating_Bananas.md`

> Quick links: [Source Solution](../03_Koko_Eating_Bananas.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the Koko problem. | 我先重述 Koko 這題。 | Restatement |
| We have banana piles and h available hours. | 我們有多堆香蕉與 h 小時。 | Restatement |
| Koko eats k bananas per hour from one pile only. | Koko 每小時以速度 k 吃一堆香蕉。 | Restatement |
| I need the minimum integer k that finishes all piles in time. | 我要找能準時吃完的最小整數 k。 | Restatement |
| Feasibility is monotonic with respect to k. | 可行性對 k 具有單調性。 | Restatement |
| So I will binary search the answer space. | 所以我會對答案空間做二分。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume h is always at least number of piles? | 我可以假設 h 一定不小於堆數嗎？ | Clarify |
| Are pile sizes and h within 32-bit integer limits? | pile 與 h 是否在 32 位整數範圍內？ | Clarify |
| Should k be strictly positive integer? | k 是否必須是正整數？ | Clarify |
| Is returning the minimum feasible k the only output? | 輸出是否只要最小可行 k？ | Clarify |
| Should I use integer ceiling formula instead of floating point? | 你希望我用整數上取整公式嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline tries k from one upward until feasible. | 基線是從 k=1 一路往上試到可行。 | Approach |
| Each trial scans all piles to compute required hours. | 每次試值都要掃全部 piles 算總時數。 | Approach |
| Time is O(maxPile * n), too slow. | 時間是 O(maxPile*n)，太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Search k in range [1, maxPile]. | 在 [1,maxPile] 範圍搜尋 k。 | Approach |
| Mid speed gives required hours via sum of ceilings. | 用中速 mid 計算上取整總時數。 | Approach |
| If hours <= h, this speed works, move left for smaller k. | 若 hours<=h，代表可行，往左找更小 k。 | Approach |
| If hours > h, speed is too slow, move right side up. | 若 hours>h，速度太慢，要往右找更大 k。 | Approach |
| This yields O(n*log(maxPile)) time and O(1) space. | 可達 O(n*log(maxPile)) 時間與 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I set left to one and right to maximum pile size. | 先設 left=1，right=最大 pile。 | Coding |
| I keep an answer variable initialized as right. | 我用 answer 先初始化為 right。 | Coding |
| While left is not greater than right, I test mid speed. | 當 left<=right 時測試 mid 速度。 | Coding |
| I compute hours using (pile + mid - 1) divided by mid. | 我用 (pile+mid-1)/mid 算每堆時數。 | Coding |
| If total hours fit in h, update answer and shrink right. | 若總時數符合 h，更新答案並縮 right。 | Coding |
| Otherwise move left to mid plus one for faster speed. | 否則 left 移到 mid+1 找更快速度。 | Coding |
| Loop ends when smallest feasible speed is isolated. | 迴圈結束時最小可行速度被定位。 | Coding |
| Finally return answer. | 最後回傳 answer。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run piles [3,6,7,11] with h equals 8. | 我手跑 piles=[3,6,7,11]、h=8。 | Dry-run |
| Initial range is k from 1 to 11. | 初始 k 範圍是 1 到 11。 | Dry-run |
| Mid is 6, required hours become 6, so feasible. | mid=6，總時數為 6，可行。 | Dry-run |
| I record 6 and continue searching left half. | 我記錄 6，繼續往左半邊找。 | Dry-run |
| Mid becomes 3, required hours become 10, not feasible. | mid=3，總時數 10，不可行。 | Dry-run |
| Move left up, then test 4, hours become exactly 8. | left 上移後測 4，時數剛好 8。 | Dry-run |
| Four is minimum feasible speed, so answer is 4. | 4 是最小可行速度，所以答案是 4。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one pile and one hour. | 案例一：一堆香蕉且只有一小時。 | Edge test |
| Case two: h equals number of piles. | 案例二：h 等於 piles 數量。 | Edge test |
| Case three: very large pile values near upper bound. | 案例三：pile 值接近上限的大數。 | Edge test |
| Case four: answer equals one when hours are generous. | 案例四：時數很寬鬆時答案為 1。 | Edge test |
| Case five: answer equals maxPile in tight schedule. | 案例五：時程很緊時答案等於 maxPile。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n * log(maxPile)). | 時間複雜度是 O(n*log(maxPile))。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Binary search runs over speed range from one to maxPile. | 二分搜尋在 1 到 maxPile 速度範圍進行。 | Complexity |
| Number of trials is logarithmic in maxPile. | 試值次數是 maxPile 的對數級。 | Complexity |
| Each trial computes hours by scanning all n piles once. | 每次試值都要掃 n 堆算時數。 | Complexity |
| Only constant extra variables are used. | 只使用常數個額外變數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I confirm the monotonic property first? | 我先確認單調性可以嗎？ | If stuck |
| If speed works, any larger speed also works. | 若某速度可行，更大速度也可行。 | If stuck |
| That means binary search on answer is valid. | 代表可用答案空間二分。 | If stuck |
| I will re-check my ceiling-hours formula. | 我重檢上取整時數公式。 | If stuck |
| It should be (pile + k - 1) divided by k. | 應該是 (pile+k-1)/k。 | If stuck |
| Let me verify left and right movement again. | 我再確認 left/right 移動規則。 | If stuck |
| Feasible should move right to mid minus one. | 可行時應把 right 移到 mid-1。 | If stuck |
| Infeasible should move left to mid plus one. | 不可行時應把 left 移到 mid+1。 | If stuck |
| I will rerun the sample after fixing this. | 修正後我會重跑範例。 | If stuck |
| Great, now minimum k is stable. | 很好，最小 k 現在穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the binary-search-on-answer solution. | 我完成了答案空間二分解法。 | Wrap-up |
| I checked feasible and infeasible branch behavior. | 我檢查了可行與不可行兩分支。 | Wrap-up |
| Runtime is O(n * log(maxPile)). | 時間複雜度是 O(n*log(maxPile))。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can also discuss proof of monotonicity if needed. | 若需要我也可補充單調性證明。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Need minimum integer speed k. | 目標是最小整數速度 k。 | Cheat sheet |
| Feasibility is monotonic over k. | 可行性對 k 單調。 | Cheat sheet |
| Baseline tries every k from 1 upward. | 基線從 1 起逐個嘗試 k。 | Cheat sheet |
| Baseline cost is O(maxPile*n). | 基線成本 O(maxPile*n)。 | Cheat sheet |
| Use answer-space binary search instead. | 改用答案空間二分。 | Cheat sheet |
| left = 1, right = maxPile. | left=1，right=maxPile。 | Cheat sheet |
| mid is trial speed. | mid 是試驗速度。 | Cheat sheet |
| hours += ceil(pile/mid) each pile. | 每堆累加 ceil(pile/mid)。 | Cheat sheet |
| Integer ceil formula avoids floating point. | 用整數公式避免浮點誤差。 | Cheat sheet |
| If hours <= h, speed is feasible. | 若 hours<=h，速度可行。 | Cheat sheet |
| Record answer and move right leftward. | 記錄答案並把 right 左移。 | Cheat sheet |
| Else move left rightward. | 否則把 left 右移。 | Cheat sheet |
| End loop and return answer. | 結束迴圈回傳答案。 | Cheat sheet |
| Test one-pile case. | 測試單堆案例。 | Cheat sheet |
| Test h equals pile count case. | 測試 h=堆數案例。 | Cheat sheet |
| Test huge values case. | 測試大數案例。 | Cheat sheet |
| Time O(n*log(maxPile)). | 時間 O(n*log(maxPile))。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: wrong ceiling formula. | 常見 bug：上取整公式錯。 | Cheat sheet |
| Common bug: wrong feasible branch move. | 常見 bug：可行分支移動錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Binary search on answer with feasibility check is preserved.
- No hallucinated constraints: ✅ Uses source constraints and monotonic behavior.
- Language simplicity: ✅ Compact spoken lines for interview usage.
