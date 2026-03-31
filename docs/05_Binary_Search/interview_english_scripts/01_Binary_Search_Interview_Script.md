# 01 Binary Search — Interview English Script (C++)

> Source aligned with: `docs/05_Binary_Search/01_Binary_Search.md`

> Quick links: [Source Solution](../01_Binary_Search.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the task quickly. | 我先快速重述題目。 | Restatement |
| We have a sorted array of unique integers. | 我們有一個遞增且元素唯一的陣列。 | Restatement |
| I need to return the target index if it exists. | 若 target 存在，要回傳它的 index。 | Restatement |
| If it does not exist, I should return minus one. | 若不存在，回傳 -1。 | Restatement |
| The required runtime is O(log n). | 題目要求時間是 O(log n)。 | Restatement |
| So I will use iterative binary search. | 所以我會用迭代版二分搜尋。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume the array is always sorted in ascending order? | 我可以假設陣列一定是遞增排序嗎？ | Clarify |
| Can I also assume all values are unique? | 我也可以假設元素都不重複嗎？ | Clarify |
| Is returning any valid index enough when found? | 找到時回傳該 index 就可以嗎？ | Clarify |
| Should I prioritize iterative over recursive style? | 你偏好迭代而不是遞迴寫法嗎？ | Clarify |
| Do you want overflow-safe mid calculation explicitly? | 需要我明確用防溢位 mid 寫法嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline is scanning from left to right. | 基線作法是從左到右線性掃描。 | Approach |
| Stop when value equals target, else finish full scan. | 遇到 target 就停，否則掃完整個陣列。 | Approach |
| This is O(n) time and O(1) space. | 這是 O(n) 時間、O(1) 空間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Because array is sorted, I can discard half each step. | 因為已排序，每步都能排除一半。 | Approach |
| Keep two pointers: left and right boundaries. | 維護左右邊界 left 與 right。 | Approach |
| Compare target with nums[mid] to choose a side. | 比較 target 與 nums[mid] 決定方向。 | Approach |
| Move left or right accordingly until boundaries cross. | 更新邊界直到 left 與 right 交錯。 | Approach |
| This gives O(log n) time and O(1) space. | 這樣可達 O(log n) 時間、O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize left to zero and right to n minus one. | 先把 left 設 0、right 設 n-1。 | Coding |
| I loop while left is less than or equal to right. | 當 left <= right 時持續迴圈。 | Coding |
| I compute mid as left plus half the window size. | mid 用 left + (right-left)/2 計算。 | Coding |
| If nums[mid] equals target, I return mid immediately. | 若 nums[mid] 等於 target，立即回傳。 | Coding |
| If nums[mid] is smaller, I move left to mid plus one. | 若 nums[mid] 較小，left 移到 mid+1。 | Coding |
| Otherwise I move right to mid minus one. | 否則 right 移到 mid-1。 | Coding |
| If loop ends, target does not exist, so return minus one. | 迴圈結束代表找不到，回傳 -1。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums equals [-1,0,3,5,9,12], target equals 9. | 我手跑 nums=[-1,0,3,5,9,12], target=9。 | Dry-run |
| left is 0, right is 5, so mid is 2 and value is 3. | left=0、right=5，所以 mid=2，值是 3。 | Dry-run |
| Three is smaller than nine, so I move left to 3. | 3 小於 9，所以 left 移到 3。 | Dry-run |
| Now left is 3, right is 5, mid is 4 and value is 9. | 現在 left=3、right=5，mid=4，值是 9。 | Dry-run |
| I found the target at index 4. | 我在 index 4 找到 target。 | Dry-run |
| So the final output is 4. | 所以最終輸出是 4。 | Dry-run |
| The result matches the example. | 結果與範例一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element array where target exists. | 案例一：單一元素且 target 存在。 | Edge test |
| Case two: single element array where target is missing. | 案例二：單一元素但 target 不存在。 | Edge test |
| Case three: target is smaller than every element. | 案例三：target 比所有元素都小。 | Edge test |
| Case four: target is larger than every element. | 案例四：target 比所有元素都大。 | Edge test |
| Case five: target is exactly first or last element. | 案例五：target 剛好是首或尾元素。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(log n). | 時間複雜度是 O(log n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each iteration removes half of the search interval. | 每次迭代都砍掉一半搜尋區間。 | Complexity |
| So iteration count is logarithmic in array length. | 所以迭代次數是陣列長度的對數級。 | Complexity |
| I only store a few integer pointers and mid. | 我只維護少數整數指標與 mid。 | Complexity |
| Therefore extra memory stays constant. | 因此外加記憶體維持常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take ten seconds to re-check boundaries? | 我可以用十秒重檢邊界嗎？ | If stuck |
| I will restate the loop invariant quickly. | 我快速重述迴圈不變量。 | If stuck |
| Target, if present, must remain inside [left, right]. | 若 target 存在，必在 [left,right] 內。 | If stuck |
| I want to verify left less-equal right condition. | 我想確認 left<=right 的條件。 | If stuck |
| Let me check the mid update for each branch. | 我檢查各分支的 mid 更新。 | If stuck |
| I may have used right equals mid by mistake. | 我可能誤寫成 right=mid。 | If stuck |
| It should be right equals mid minus one here. | 這裡應該是 right=mid-1。 | If stuck |
| I will rerun the sample to confirm fix. | 我會重跑範例確認修正。 | If stuck |
| Now the loop terminates correctly. | 現在迴圈可正確終止。 | If stuck |
| Great, result is stable now. | 很好，結果現在穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the binary search implementation. | 我完成了二分搜尋實作。 | Wrap-up |
| I validated both hit and miss scenarios. | 我驗證了找到與找不到兩種情況。 | Wrap-up |
| Runtime is O(log n). | 時間複雜度是 O(log n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can also show recursive version if you want. | 若你需要，我也可補充遞迴版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorted unique array, find target index. | 排序唯一陣列，找 target index。 | Cheat sheet |
| Missing target returns minus one. | 找不到就回傳 -1。 | Cheat sheet |
| Baseline is linear scan O(n). | 基線是線性掃描 O(n)。 | Cheat sheet |
| Required solution is O(log n). | 題目要求 O(log n)。 | Cheat sheet |
| Use two pointers left and right. | 用兩個指標 left 與 right。 | Cheat sheet |
| Loop while left <= right. | 迴圈條件是 left <= right。 | Cheat sheet |
| Mid is left + (right-left)/2. | mid 用 left+(right-left)/2。 | Cheat sheet |
| If nums[mid] == target, return mid. | 若 nums[mid]==target，回傳 mid。 | Cheat sheet |
| If nums[mid] < target, left = mid + 1. | 若 nums[mid]<target，left=mid+1。 | Cheat sheet |
| Else right = mid - 1. | 否則 right=mid-1。 | Cheat sheet |
| End loop means not found. | 迴圈結束代表沒找到。 | Cheat sheet |
| Return -1 in that case. | 該情況回傳 -1。 | Cheat sheet |
| Test one-element hit case. | 測單元素命中案例。 | Cheat sheet |
| Test one-element miss case. | 測單元素未命中案例。 | Cheat sheet |
| Test smaller-than-all target case. | 測比全部小的 target。 | Cheat sheet |
| Test larger-than-all target case. | 測比全部大的 target。 | Cheat sheet |
| Time complexity O(log n). | 時間複雜度 O(log n)。 | Cheat sheet |
| Space complexity O(1). | 空間複雜度 O(1)。 | Cheat sheet |
| Common bug: wrong boundary update. | 常見錯誤：邊界更新錯。 | Cheat sheet |
| Common bug: wrong loop condition. | 常見錯誤：迴圈條件寫錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Iterative binary search logic is preserved.
- No hallucinated constraints: ✅ Script uses the source problem assumptions.
- Language simplicity: ✅ Short spoken lines for interview delivery.
