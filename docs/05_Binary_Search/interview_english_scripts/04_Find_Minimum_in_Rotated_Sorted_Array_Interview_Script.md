# 04 Find Minimum in Rotated Sorted Array — Interview English Script (C++)

> Source aligned with: `docs/05_Binary_Search/04_Find_Minimum_in_Rotated_Sorted_Array.md`

> Quick links: [Source Solution](../04_Find_Minimum_in_Rotated_Sorted_Array.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the rotated-array minimum problem. | 我先重述旋轉陣列最小值題。 | Restatement |
| The array was sorted, then rotated at an unknown pivot. | 陣列原本排序後在未知 pivot 被旋轉。 | Restatement |
| All elements are unique in this version. | 這一版元素都不重複。 | Restatement |
| I need to return the minimum value. | 我要回傳最小值本身。 | Restatement |
| Required runtime is O(log n), so linear scan is not enough. | 題目要求 O(log n)，不能用線掃。 | Restatement |
| I will use binary search against the right boundary. | 我會用與右邊界比較的二分法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume no duplicate values in the array? | 我可以假設陣列沒有重複值嗎？ | Clarify |
| Should I return value instead of pivot index? | 要回傳值而不是 pivot 索引對嗎？ | Clarify |
| Is array length always at least one? | 陣列長度是否一定至少為 1？ | Clarify |
| Do you prefer iterative binary search style? | 你偏好迭代寫法嗎？ | Clarify |
| Should I also mention how duplicates would change logic? | 需要我補充重複值版本差異嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline scans all elements and tracks smallest value. | 基線是掃描所有元素記錄最小值。 | Approach |
| It is simple and always correct. | 這做法很直觀且一定正確。 | Approach |
| But time is O(n), not meeting O(log n). | 但時間是 O(n)，不符 O(log n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Compare nums[mid] with nums[right] each iteration. | 每輪比較 nums[mid] 與 nums[right]。 | Approach |
| If nums[mid] is greater, minimum is to the right. | 若 nums[mid] 較大，最小值在右側。 | Approach |
| Otherwise minimum is at mid or to the left side. | 否則最小值在 mid 或左側。 | Approach |
| Use right equals mid, not mid minus one, to keep candidate. | right 要設 mid，不是 mid-1。 | Approach |
| End when left equals right, that index is minimum. | 當 left==right 時，該點就是最小值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize left to zero and right to n minus one. | 先設 left=0、right=n-1。 | Coding |
| I loop while left is strictly less than right. | 在 left<right 時持續迴圈。 | Coding |
| I compute mid using safe integer formula. | 我用安全公式計算 mid。 | Coding |
| If nums[mid] is greater than nums[right], move left to mid plus one. | 若 nums[mid]>nums[right]，left 移到 mid+1。 | Coding |
| Else move right to mid to keep mid as possible minimum. | 否則 right 移到 mid 保留候選。 | Coding |
| Continue shrinking until both pointers meet. | 持續收縮直到兩指標相遇。 | Coding |
| Return nums[left] as final minimum value. | 回傳 nums[left] 作為最小值。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run array [4,5,6,7,0,1,2]. | 我手跑陣列 [4,5,6,7,0,1,2]。 | Dry-run |
| left is 0, right is 6, mid is 3 with value 7. | left=0、right=6，mid=3 值為 7。 | Dry-run |
| Seven is greater than nums[right] which is 2, so move left to 4. | 7 大於 nums[right]=2，所以 left 到 4。 | Dry-run |
| Now left 4, right 6, mid 5 with value 1. | 現在 left=4、right=6，mid=5 值為 1。 | Dry-run |
| One is not greater than nums[right] 2, so move right to 5. | 1 不大於 nums[right]=2，所以 right 到 5。 | Dry-run |
| Next mid is 4, value 0, move right to 4. | 下一輪 mid=4，值 0，right 移到 4。 | Dry-run |
| Pointers meet at index 4, minimum is 0. | 指標相遇在 index 4，最小值是 0。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: array length one. | 案例一：陣列長度為 1。 | Edge test |
| Case two: already sorted, not rotated. | 案例二：本來就排序好、未旋轉。 | Edge test |
| Case three: rotated by one position. | 案例三：只旋轉一格。 | Edge test |
| Case four: minimum at last index after rotation. | 案例四：旋轉後最小值在最後一格。 | Edge test |
| Case five: minimum at first index in no-rotation case. | 案例五：未旋轉時最小值在首位。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(log n). | 時間複雜度是 O(log n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Every iteration removes about half of current interval. | 每輪都大致排除一半區間。 | Complexity |
| Therefore number of iterations is logarithmic. | 因此迭代次數是對數級。 | Complexity |
| I only keep left, right, and mid pointers. | 我只維護 left/right/mid 指標。 | Complexity |
| So extra memory remains constant. | 所以額外空間維持常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me re-check the comparison baseline first. | 我先重檢比較基準。 | If stuck |
| I compare mid with right boundary in this template. | 這個模板是 mid 與 right 比較。 | If stuck |
| If mid is bigger, minimum must be to the right. | 若 mid 較大，最小值一定在右邊。 | If stuck |
| Otherwise minimum may still be at mid. | 否則最小值仍可能是 mid。 | If stuck |
| So right should move to mid, not mid minus one. | 所以 right 要到 mid，不是 mid-1。 | If stuck |
| I will verify loop condition uses left less than right. | 我確認迴圈條件是 left<right。 | If stuck |
| This avoids skipping the final candidate index. | 這可避免漏掉最後候選點。 | If stuck |
| Let me run one sorted and one rotated sample. | 我跑一個未旋轉與一個旋轉樣本。 | If stuck |
| Both return the correct minimum now. | 兩種情況現在都回傳正確最小值。 | If stuck |
| Great, logic is consistent. | 很好，邏輯一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed the rotated minimum binary search solution. | 我完成了旋轉最小值二分解法。 | Wrap-up |
| I validated rotated and non-rotated cases. | 我驗證了旋轉與未旋轉案例。 | Wrap-up |
| Runtime is O(log n). | 時間複雜度是 O(log n)。 | Wrap-up |
| Extra memory is O(1). | 額外記憶體是 O(1)。 | Wrap-up |
| I can explain duplicate-handling variant if needed. | 若需要我可補充重複值版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find minimum in rotated sorted unique array. | 在旋轉排序唯一陣列找最小值。 | Cheat sheet |
| O(log n) required. | 題目要求 O(log n)。 | Cheat sheet |
| Baseline linear scan is O(n). | 基線線掃是 O(n)。 | Cheat sheet |
| Use binary search with right comparison. | 用與 right 比較的二分法。 | Cheat sheet |
| left = 0, right = n-1. | left=0，right=n-1。 | Cheat sheet |
| Loop while left < right. | 迴圈條件 left<right。 | Cheat sheet |
| mid = left + (right-left)/2. | mid=left+(right-left)/2。 | Cheat sheet |
| If nums[mid] > nums[right], left = mid+1. | 若 nums[mid]>nums[right]，left=mid+1。 | Cheat sheet |
| Else right = mid. | 否則 right=mid。 | Cheat sheet |
| Keep mid when it can be minimum. | mid 可能是最小值要保留。 | Cheat sheet |
| End when pointers meet. | 指標相遇時結束。 | Cheat sheet |
| Return nums[left]. | 回傳 nums[left]。 | Cheat sheet |
| Test single-element case. | 測試單元素案例。 | Cheat sheet |
| Test non-rotated sorted case. | 測試未旋轉排序案例。 | Cheat sheet |
| Test rotation by one case. | 測試旋轉一格案例。 | Cheat sheet |
| Test minimum at tail case. | 測試最小值在尾端案例。 | Cheat sheet |
| Time O(log n). | 時間 O(log n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: using right = mid-1. | 常見 bug：誤用 right=mid-1。 | Cheat sheet |
| Common bug: wrong loop condition. | 常見 bug：迴圈條件寫錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Mid-vs-right binary-search invariant is preserved.
- No hallucinated constraints: ✅ Uses source unique-elements constraint.
- Language simplicity: ✅ Natural short lines for spoken interview use.
