# 01 Maximum Subarray — Interview English Script (C++)

> Source aligned with: `docs/13_Greedy/01_Maximum_Subarray.md`

> Quick links: [Source Solution](../01_Maximum_Subarray.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate maximum subarray. | 我先重述 Maximum Subarray。 | Restatement |
| We are given an integer array nums. | 題目給整數陣列 nums。 | Restatement |
| We need the largest sum among all non-empty contiguous subarrays. | 要找所有非空連續子陣列中的最大總和。 | Restatement |
| The subarray must be contiguous, not arbitrary picks. | 子陣列必須連續，不能任選元素。 | Restatement |
| We return only the maximum sum value. | 只需要回最大總和值。 | Restatement |
| I will solve it with Kadane greedy approach. | 我會用 Kadane 貪心法解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is nums guaranteed non-empty? | nums 是否保證非空？ | Clarify |
| Can numbers be negative and positive mixed? | 數字可能正負混合嗎？ | Clarify |
| Should all-negative arrays return the largest single element? | 全負陣列是否回最大單一元素？ | Clarify |
| Do we return sum only, not start and end indices? | 是否只回總和，不回左右邊界？ | Clarify |
| Is O(n) time expected? | O(n) 時間是否為預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks every subarray range. | 暴力法檢查每個子陣列區間。 | Approach |
| Even with prefix sums, it still needs O(n squared) ranges. | 即使用前綴和仍要 O(n²) 個區間。 | Approach |
| We need linear-time optimization. | 我們需要線性時間優化。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Keep current running sum and global best sum. | 維護目前累加和與全域最佳和。 | Approach |
| If running sum becomes negative, drop it and restart from next position. | 若累加和變負，捨棄並從下一點重啟。 | Approach |
| Negative prefix only hurts any future extension. | 負前綴只會拖累後續延伸。 | Approach |
| Update global best after each element. | 每個元素都更新一次全域最佳。 | Approach |
| This is Kadane algorithm in O(n) time. | 這就是 O(n) 的 Kadane 演算法。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize maxSub with nums[0] to handle all-negative cases. | 我用 nums[0] 初始化 maxSub，以處理全負情況。 | Coding |
| I initialize curSum as zero. | 我把 curSum 初值設為 0。 | Coding |
| For each number n, if curSum is negative I reset it to zero first. | 對每個 n，若 curSum 為負先重設成 0。 | Coding |
| Then I add n into curSum. | 接著把 n 加進 curSum。 | Coding |
| I update maxSub as max(maxSub, curSum). | 我用 max(maxSub,curSum) 更新 maxSub。 | Coding |
| This keeps best contiguous sum seen so far. | 這可維持目前看過的最佳連續和。 | Coding |
| Loop continues through all elements once. | 迴圈一次掃完所有元素。 | Coding |
| Return maxSub as final answer. | 回傳 maxSub 作最終答案。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [-2,1,-3,4,-1,2,1,-5,4]. | 我手跑 nums=[-2,1,-3,4,-1,2,1,-5,4]。 | Dry-run |
| Start with maxSub minus two and curSum zero. | 初始 maxSub=-2、curSum=0。 | Dry-run |
| At value one, curSum becomes one and maxSub updates to one. | 遇到 1 時 curSum=1，maxSub 更新為 1。 | Dry-run |
| At value four, sequence restarts and curSum becomes four. | 到 4 時序列重啟，curSum 變 4。 | Dry-run |
| Then adding minus one plus two plus one reaches six. | 再加 -1、+2、+1 後達到 6。 | Dry-run |
| maxSub stays six through the remaining scan. | 後續掃描中 maxSub 維持 6。 | Dry-run |
| Final answer is six. | 最終答案是 6。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element array. | 案例一：單元素陣列。 | Edge test |
| Case two: all negative numbers. | 案例二：全為負數。 | Edge test |
| Case three: all positive numbers. | 案例三：全為正數。 | Edge test |
| Case four: alternating small gains and losses. | 案例四：小幅正負交替。 | Edge test |
| Case five: best subarray appears at the end. | 案例五：最佳子陣列在尾端。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan the array exactly once. | 我們只掃描陣列一次。 | Complexity |
| Each step performs constant-time updates. | 每一步都只做常數時間更新。 | Complexity |
| Therefore runtime is linear O(n). | 因此時間是線性的 O(n)。 | Complexity |
| Only two scalar variables are used, so memory is O(1). | 只用兩個純量變數，所以空間是 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Kadane intuition first. | 我先重述 Kadane 直覺。 | If stuck |
| A negative running sum should be dropped. | 負的累加和應該被捨棄。 | If stuck |
| Keeping a negative prefix never helps future sum. | 保留負前綴不會幫助未來總和。 | If stuck |
| I track curSum and maxSub only. | 我只追蹤 curSum 與 maxSub。 | If stuck |
| maxSub must start from nums[0], not zero. | maxSub 必須從 nums[0] 開始，不是 0。 | If stuck |
| That handles all-negative arrays correctly. | 這能正確處理全負陣列。 | If stuck |
| Let me test quickly with [-3,-2,-5]. | 我快速測 [-3,-2,-5]。 | If stuck |
| The answer should be minus two. | 答案應該是 -2。 | If stuck |
| Good, initialization is validated. | 好，初始化已驗證。 | If stuck |
| Now coding flow is straightforward. | 現在實作流程就很直觀。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved maximum subarray with Kadane greedy algorithm. | 我用 Kadane 貪心演算法解了 Maximum Subarray。 | Wrap-up |
| The key is resetting negative running sums. | 關鍵是把負累加和重設。 | Wrap-up |
| We update global best at each position. | 在每個位置更新全域最佳。 | Wrap-up |
| Complexity is O(n) time and O(1) space. | 複雜度是 O(n) 時間、O(1) 空間。 | Wrap-up |
| This is the standard interview-optimal solution. | 這是面試標準且最優的解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: max sum of non-empty contiguous subarray. | 目標：非空連續子陣列最大和。 | Cheat sheet |
| Use Kadane greedy. | 使用 Kadane 貪心。 | Cheat sheet |
| Track curSum and maxSub. | 追蹤 curSum 與 maxSub。 | Cheat sheet |
| Initialize maxSub=nums[0]. | 初始化 maxSub=nums[0]。 | Cheat sheet |
| Initialize curSum=0. | 初始化 curSum=0。 | Cheat sheet |
| If curSum<0, reset curSum=0. | 若 curSum<0，重設 curSum=0。 | Cheat sheet |
| Add current number to curSum. | 把當前數字加到 curSum。 | Cheat sheet |
| Update maxSub=max(maxSub,curSum). | 更新 maxSub=max(maxSub,curSum)。 | Cheat sheet |
| Single pass through array. | 陣列單次掃描。 | Cheat sheet |
| Return maxSub. | 回傳 maxSub。 | Cheat sheet |
| All negative case still works. | 全負情況仍可正確運作。 | Cheat sheet |
| Example [-2,1,-3,4,-1,2,1,-5,4] -> 6. | 例 [-2,1,-3,4,-1,2,1,-5,4] -> 6。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: init maxSub=0. | 常見錯誤：maxSub 初始化成 0。 | Cheat sheet |
| Common bug: reset after update in wrong order. | 常見錯誤：更新順序寫反。 | Cheat sheet |
| Contiguous is mandatory. | 必須強調連續性。 | Cheat sheet |
| Mention divide-and-conquer as follow-up. | 可補充分治法當追問。 | Cheat sheet |
| Validate with all-negative sample. | 記得用全負樣例驗證。 | Cheat sheet |
| Keep explanation concise and confident. | 說明時保持簡潔有力。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Kadane reset logic and initialization preserved.
- No hallucinated constraints: ✅ Non-empty contiguous semantics maintained.
- Language simplicity: ✅ Interview-ready concise narration.
