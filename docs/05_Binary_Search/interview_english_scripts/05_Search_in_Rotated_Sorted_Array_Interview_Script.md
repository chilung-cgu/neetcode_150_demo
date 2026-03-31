# 05 Search in Rotated Sorted Array — Interview English Script (C++)

> Source aligned with: `docs/05_Binary_Search/05_Search_in_Rotated_Sorted_Array.md`

> Quick links: [Source Solution](../05_Search_in_Rotated_Sorted_Array.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the rotated search problem. | 我先重述旋轉搜尋題。 | Restatement |
| The original sorted array is rotated at some pivot. | 原本排序陣列在某個 pivot 旋轉。 | Restatement |
| All values are unique in this version. | 這一版數值都不重複。 | Restatement |
| I need to return target index, or minus one if absent. | 我要回傳 target index，找不到就 -1。 | Restatement |
| Required runtime is O(log n). | 題目要求時間 O(log n)。 | Restatement |
| I will do one-pass binary search with sorted-half checks. | 我會用一次二分加有序半邊判斷。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume there are no duplicate values? | 我可以假設沒有重複值嗎？ | Clarify |
| Do you want index only, not boolean existence? | 你要的是索引，不是布林值對嗎？ | Clarify |
| Is returning any index impossible issue since values are unique? | 因為值唯一，不會有多個索引問題對嗎？ | Clarify |
| Should I keep iterative style for clarity? | 我用迭代寫法可以嗎？ | Clarify |
| Do you want me to mention duplicate-value variant briefly? | 需要我簡述重複值變體嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline scans array linearly for target. | 基線是線性掃描找 target。 | Approach |
| Return index when matched, otherwise minus one. | 匹配就回傳索引，否則回傳 -1。 | Approach |
| Time is O(n), not enough for requirement. | 時間 O(n)，不符合要求。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| At each mid, one side must be sorted. | 每個 mid 至少有一側一定有序。 | Approach |
| If left side is sorted, check whether target lies in that range. | 若左側有序，就判斷 target 是否在範圍內。 | Approach |
| If yes, move right inward; otherwise move left outward. | 在範圍內縮 right，否則推進 left。 | Approach |
| If right side is sorted, do symmetric range check. | 若右側有序，做對稱範圍判斷。 | Approach |
| This keeps O(log n) time and O(1) space. | 這可維持 O(log n) 時間與 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I set left to zero and right to n minus one. | 先設 left=0、right=n-1。 | Coding |
| I loop while left is less than or equal to right. | 當 left<=right 時持續迴圈。 | Coding |
| I compute mid and check direct hit first. | 先算 mid 並先檢查是否直接命中。 | Coding |
| If left half is sorted, I test target within [left, mid). | 若左半有序，判斷 target 是否在 [left,mid)。 | Coding |
| If inside, move right to mid minus one; otherwise move left up. | 在範圍內就 right=mid-1，否則提升 left。 | Coding |
| Else right half is sorted, test target within (mid, right]. | 否則右半有序，判斷 target 是否在 (mid,right]。 | Coding |
| If inside, move left to mid plus one; else move right down. | 在範圍內就 left=mid+1，否則降低 right。 | Coding |
| End loop and return minus one when not found. | 迴圈結束仍未找到就回傳 -1。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [4,5,6,7,0,1,2] and target 0. | 我手跑 nums=[4,5,6,7,0,1,2]、target=0。 | Dry-run |
| left 0, right 6, mid 3 gives value 7. | left=0、right=6、mid=3，值是 7。 | Dry-run |
| Left half [4,5,6,7] is sorted, target not in it. | 左半 [4,5,6,7] 有序，但 target 不在裡面。 | Dry-run |
| So move left to 4. | 所以 left 移到 4。 | Dry-run |
| Now left 4, right 6, mid 5 gives value 1. | 現在 left=4、right=6、mid=5，值是 1。 | Dry-run |
| Left half [0,1] is sorted and target is inside, move right to 4. | 左半 [0,1] 有序且 target 在內，right 移到 4。 | Dry-run |
| Mid becomes 4, value is 0, return index 4. | mid 變成 4，值是 0，回傳索引 4。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element hit. | 案例一：單元素命中。 | Edge test |
| Case two: single element miss. | 案例二：單元素未命中。 | Edge test |
| Case three: no rotation, behaves like normal binary search. | 案例三：未旋轉，等同一般二分。 | Edge test |
| Case four: target at pivot position minimum value. | 案例四：target 在 pivot 最小值位置。 | Edge test |
| Case five: target absent between value gaps. | 案例五：target 落在值間隙且不存在。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(log n). | 時間複雜度是 O(log n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each iteration discards one half of current search interval. | 每輪都會捨棄當前區間的一半。 | Complexity |
| Sorted-half detection keeps decision deterministic. | 有序半邊判斷讓決策保持確定性。 | Complexity |
| Pointer updates are constant-time operations. | 指標更新是常數時間操作。 | Complexity |
| No extra containers are needed. | 不需要任何額外容器。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me identify which half is sorted first. | 我先判斷哪一半有序。 | If stuck |
| I compare nums[left] and nums[mid] for that. | 我用 nums[left] 與 nums[mid] 比較。 | If stuck |
| If left half is sorted, I do range check there. | 若左半有序，就先做左半範圍檢查。 | If stuck |
| Otherwise I switch to right-half range check. | 否則切到右半範圍檢查。 | If stuck |
| I should use strict and non-strict bounds carefully. | 我要小心使用嚴格/非嚴格邊界。 | If stuck |
| Mid equality case is already handled at top. | mid 相等情況已在前面先處理。 | If stuck |
| Let me rerun sample after fixing boundary signs. | 我修正邊界號號後重跑範例。 | If stuck |
| Now pivot-side decisions are consistent. | 現在 pivot 側判斷一致。 | If stuck |
| The loop converges correctly. | 迴圈能正確收斂。 | If stuck |
| Great, final index is correct now. | 很好，最終索引正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed one-pass rotated binary search. | 我完成了一次旋轉二分搜尋。 | Wrap-up |
| I validated pivot and non-pivot scenarios. | 我驗證了含 pivot 與無 pivot 情況。 | Wrap-up |
| Runtime is O(log n). | 時間複雜度是 O(log n)。 | Wrap-up |
| Extra memory is O(1). | 額外記憶體是 O(1)。 | Wrap-up |
| I can also explain duplicate version trade-offs. | 我也可補充重複值版本取捨。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Search target in rotated sorted unique array. | 在旋轉排序唯一陣列找 target。 | Cheat sheet |
| Need index or -1. | 需要回傳 index 或 -1。 | Cheat sheet |
| Baseline linear scan O(n). | 基線線掃 O(n)。 | Cheat sheet |
| Required method O(log n). | 要求方法 O(log n)。 | Cheat sheet |
| Use binary search with sorted-half detection. | 用二分加有序半邊判斷。 | Cheat sheet |
| left=0, right=n-1. | left=0，right=n-1。 | Cheat sheet |
| Loop while left<=right. | 迴圈條件 left<=right。 | Cheat sheet |
| Check nums[mid]==target first. | 先檢查 nums[mid]==target。 | Cheat sheet |
| If nums[left]<=nums[mid], left half sorted. | 若 nums[left]<=nums[mid]，左半有序。 | Cheat sheet |
| Range-hit then move right, else move left. | 範圍命中移 right，否則移 left。 | Cheat sheet |
| Else right half is sorted. | 否則右半有序。 | Cheat sheet |
| Range-hit then move left, else move right. | 範圍命中移 left，否則移 right。 | Cheat sheet |
| End loop means not found. | 迴圈結束表示找不到。 | Cheat sheet |
| Return -1 then. | 此時回傳 -1。 | Cheat sheet |
| Test single-element hit/miss. | 測單元素命中/未命中。 | Cheat sheet |
| Test non-rotated normal case. | 測未旋轉一般情況。 | Cheat sheet |
| Test pivot-target case. | 測 pivot 目標案例。 | Cheat sheet |
| Time O(log n). | 時間 O(log n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: wrong inequality boundaries. | 常見 bug：不等號邊界寫錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ One-pass sorted-half binary search is preserved.
- No hallucinated constraints: ✅ Uses source unique-elements assumption.
- Language simplicity: ✅ Concise spoken lines suitable for interview delivery.
