# 11 Longest Increasing Subsequence — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/11_Longest_Increasing_Subsequence.md`

> Quick links: [Source Solution](../11_Longest_Increasing_Subsequence.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate longest increasing subsequence. | 我先重述最長遞增子序列題。 | Restatement |
| We need the length of the longest strictly increasing subsequence. | 我們要最長嚴格遞增子序列的長度。 | Restatement |
| Subsequence means elements keep order but need not be contiguous. | 子序列保持順序但不需連續。 | Restatement |
| We only return the length, not the sequence itself. | 只需回傳長度，不必回序列。 | Restatement |
| A classic DP solution is O(n squared). | 經典 DP 解法是 O(n²)。 | Restatement |
| There is also an O(n log n) binary-search optimization. | 另有 O(n log n) 的二分優化。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do you want only the length of LIS? | 是否只需要 LIS 長度？ | Clarify |
| Is strictly increasing required, not non-decreasing? | 要嚴格遞增，不是非遞減，對嗎？ | Clarify |
| Are duplicate values allowed in input? | 輸入是否允許重複值？ | Clarify |
| Should I present O(n squared) first for clarity? | 我先講 O(n²) 版本可以嗎？ | Clarify |
| Then I can mention O(n log n) follow-up. | 之後我可補充 O(n log n) 追問解。 | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries include or exclude at each index. | 暴力法在每個索引做選或不選。 | Approach |
| It explores many overlapping subsequence states. | 會探索大量重疊狀態。 | Approach |
| Worst-case runtime is exponential. | 最壞時間是指數級。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| In O(n squared) DP, dp[i] is LIS length ending at i. | O(n²) DP 中，dp[i] 是以 i 結尾的 LIS 長度。 | Approach |
| Transition checks all j less than i with nums[j] less than nums[i]. | 轉移檢查 j<i 且 nums[j]<nums[i]。 | Approach |
| Update dp[i] as max of itself and one plus dp[j]. | dp[i] 更新為自身與 1+dp[j] 的最大。 | Approach |
| Global answer is max value in dp. | 全域答案是 dp 的最大值。 | Approach |
| Follow-up optimization uses greedy tails with binary search to O(n log n). | 追問可用 tails+二分優化到 O(n log n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I handle empty input by returning zero. | 空輸入直接回傳 0。 | Coding |
| I create dp array of size n and initialize all to one. | 建立長度 n 的 dp，初值全設 1。 | Coding |
| I keep maxLen initialized to one. | 設 maxLen 初值為 1。 | Coding |
| For each i from one to n minus one, I scan j from zero to i minus one. | i 從 1 到 n-1，j 從 0 到 i-1。 | Coding |
| If nums[i] greater than nums[j], I can extend sequence ending at j. | 若 nums[i]>nums[j]，可延伸 j 的序列。 | Coding |
| I set dp[i] to max(dp[i], one plus dp[j]). | 更新 dp[i]=max(dp[i],1+dp[j])。 | Coding |
| After finishing j loop, I update maxLen with dp[i]. | 完成 j 迴圈後用 dp[i] 更新 maxLen。 | Coding |
| Return maxLen as final LIS length. | 回傳 maxLen 作為最終 LIS 長度。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [10,9,2,5,3,7,101,18]. | 我手跑 nums=[10,9,2,5,3,7,101,18]。 | Dry-run |
| Initialize all dp values to one. | 先把所有 dp 值設為 1。 | Dry-run |
| At value five, it can extend from two, so dp there becomes two. | 到 5 時可接在 2 後面，該處 dp 變 2。 | Dry-run |
| At value seven, it extends best previous chain to length three. | 到 7 時可延伸最佳前鏈到長度 3。 | Dry-run |
| At value one-zero-one, it extends to length four. | 到 101 時可延伸到長度 4。 | Dry-run |
| Later eighteen also reaches length four but not higher. | 後面的 18 也可到 4，但不會更高。 | Dry-run |
| Final answer is four. | 最終答案是 4。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element array should return one. | 案例一：單元素陣列應回 1。 | Edge test |
| Case two: strictly decreasing array should return one. | 案例二：嚴格遞減陣列應回 1。 | Edge test |
| Case three: all equal numbers should return one. | 案例三：全相等數字應回 1。 | Edge test |
| Case four: already increasing array should return n. | 案例四：已遞增陣列應回 n。 | Edge test |
| Case five: mixed negatives and positives. | 案例五：正負混合數值。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| DP solution runs in O(n squared) time. | DP 解法時間為 O(n²)。 | Complexity |
| Space complexity is O(n). | 空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For each i, we scan all previous j indices. | 對每個 i，都掃描先前所有 j。 | Complexity |
| That nested loop contributes O(n squared) runtime. | 這個雙層迴圈產生 O(n²) 時間。 | Complexity |
| DP array stores one value per index. | DP 陣列每個索引存一個值。 | Complexity |
| So memory usage is O(n). | 所以記憶體用量是 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define state precisely before coding. | 我先精確定義狀態再寫。 | If stuck |
| dp[i] is LIS length ending exactly at i. | dp[i] 是「以 i 結尾」的 LIS 長度。 | If stuck |
| Base length is one for every index. | 每個位置的基礎長度都是 1。 | If stuck |
| Transition only allowed when nums[j] is smaller than nums[i]. | 只有 nums[j]<nums[i] 才能轉移。 | If stuck |
| I should maximize one plus dp[j]. | 我應該取最大的 1+dp[j]。 | If stuck |
| Global answer is max over all dp[i]. | 全域答案是所有 dp[i] 的最大。 | If stuck |
| Let me verify with decreasing input quickly. | 我快速驗證遞減輸入。 | If stuck |
| All dp values stay one there. | 那種情況所有 dp 都會是 1。 | If stuck |
| That matches strict-increase requirement. | 這符合嚴格遞增的要求。 | If stuck |
| Great, logic is consistent now. | 很好，邏輯現在一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved LIS using dynamic programming. | 我用動態規劃解了 LIS。 | Wrap-up |
| State dp[i] tracks best increasing subsequence ending at i. | 狀態 dp[i] 追蹤以 i 結尾的最佳遞增長度。 | Wrap-up |
| Transition checks all previous smaller numbers. | 轉移會檢查所有更小的前項。 | Wrap-up |
| Complexity is O(n squared) time and O(n) space. | 複雜度是 O(n²) 時間、O(n) 空間。 | Wrap-up |
| Follow-up can be improved to O(n log n). | 追問版本可優化為 O(n log n)。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: longest strictly increasing subsequence length. | 目標：最長嚴格遞增子序列長度。 | Cheat sheet |
| Subsequence is not required to be contiguous. | 子序列不要求連續。 | Cheat sheet |
| Return length only. | 只回傳長度。 | Cheat sheet |
| Define dp[i] as LIS ending at i. | 定義 dp[i] 為以 i 結尾的 LIS。 | Cheat sheet |
| Initialize all dp values to one. | 所有 dp 初值設為 1。 | Cheat sheet |
| For each i, scan all j<i. | 對每個 i，掃描所有 j<i。 | Cheat sheet |
| Require nums[j] < nums[i] to extend. | 要 nums[j]<nums[i] 才可延伸。 | Cheat sheet |
| Update dp[i]=max(dp[i],1+dp[j]). | 更新 dp[i]=max(dp[i],1+dp[j])。 | Cheat sheet |
| Track global maxLen. | 追蹤全域 maxLen。 | Cheat sheet |
| Answer is maxLen. | 答案是 maxLen。 | Cheat sheet |
| Example [10,9,2,5,3,7,101,18] -> 4. | 例 [10,9,2,5,3,7,101,18] -> 4。 | Cheat sheet |
| Decreasing array -> 1. | 遞減陣列 -> 1。 | Cheat sheet |
| Equal values -> 1 due to strictness. | 相等值因嚴格遞增故為 1。 | Cheat sheet |
| Time O(n squared). | 時間 O(n²)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Common bug: confuse subsequence with subarray. | 常見錯誤：把 subsequence 當 subarray。 | Cheat sheet |
| Common bug: allow non-decreasing transition. | 常見錯誤：誤用非遞減轉移。 | Cheat sheet |
| State must be “ending at i”. | 狀態必須是「以 i 結尾」。 | Cheat sheet |
| Mention O(n log n) follow-up briefly. | 可簡短提及 O(n log n) 追問。 | Cheat sheet |
| Keep recurrence explanation crisp. | 遞推說明要精準簡潔。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ O(n²) DP recurrence aligned, with O(n log n) follow-up mention.
- No hallucinated constraints: ✅ Strictly increasing and subsequence semantics preserved.
- Language simplicity: ✅ Clear interview phrasing for state, transition, and edge behavior.
