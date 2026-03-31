# 07 Median of Two Sorted Arrays — Interview English Script (C++)

> Source aligned with: `docs/05_Binary_Search/07_Median_of_Two_Sorted_Arrays.md`

> Quick links: [Source Solution](../07_Median_of_Two_Sorted_Arrays.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate this median problem. | 我先重述這題中位數問題。 | Restatement |
| We have two individually sorted arrays. | 我們有兩個各自排序好的陣列。 | Restatement |
| We need the median of their combined order. | 要找合併排序後的中位數。 | Restatement |
| A full merge is easy but too slow for requirement. | 全合併雖容易，但不符複雜度要求。 | Restatement |
| Target complexity is logarithmic in input size. | 題目要求對數級時間。 | Restatement |
| I will binary-search partition on the shorter array. | 我會在較短陣列上做 partition 二分。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can either input array be empty? | 任一輸入陣列可以是空的嗎？ | Clarify |
| Should final answer be returned as double precision? | 最終答案要用 double 回傳嗎？ | Clarify |
| Are arrays guaranteed sorted in non-decreasing order? | 陣列是否保證非遞減排序？ | Clarify |
| Do you want me to optimize to O(log(min(m,n))) specifically? | 你希望我強調 O(log(min(m,n))) 嗎？ | Clarify |
| Is discussing sentinel boundaries expected? | 是否希望我說明哨兵邊界處理？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline merges two arrays then reads middle position(s). | 基線是先合併兩陣列再取中間值。 | Approach |
| This gives correct median directly. | 這可直接得到正確中位數。 | Approach |
| But runtime is O(m+n), not logarithmic. | 但時間 O(m+n)，不符要求。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Always binary search on the shorter array A. | 固定在較短陣列 A 上做二分。 | Approach |
| Choose partition i in A, then j equals half minus i in B. | 在 A 選切點 i，B 的切點 j=half-i。 | Approach |
| Valid partition needs Aleft <= Bright and Bleft <= Aright. | 合法切點需 Aleft<=Bright 且 Bleft<=Aright。 | Approach |
| If valid, compute median from boundary values. | 合法後用邊界值直接算中位數。 | Approach |
| Else adjust i left or right and continue binary search. | 否則調整 i 左右繼續二分。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I ensure nums1 is the shorter array. | 先確保 nums1 是較短陣列。 | Coding |
| I compute total length and half size for left partition. | 計算總長與左半邊需要的數量。 | Coding |
| I binary search i from zero to length of nums1. | 在 nums1 的 [0,m] 範圍二分 i。 | Coding |
| For each i, j equals half minus i. | 每個 i 對應 j=half-i。 | Coding |
| I derive left and right boundary values using sentinels. | 用哨兵值取四個邊界元素。 | Coding |
| If cross conditions hold, partition is correct. | 若交叉條件成立，切點正確。 | Coding |
| Odd total returns max(left parts), even returns average of middle pair. | 奇數回左半最大，偶數回中間兩值平均。 | Coding |
| If Aleft too big move right down, else move left up. | 若 Aleft 太大就降 right，否則升 left。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums1 [1,3] and nums2 [2]. | 我手跑 nums1=[1,3]、nums2=[2]。 | Dry-run |
| I swap so A is [2] and B is [1,3]. | 我先交換，讓 A=[2]、B=[1,3]。 | Dry-run |
| Total is 3, half for left side is 2. | 總長 3，左半需求是 2。 | Dry-run |
| Try i equals 0, then j equals 2. | 嘗試 i=0，則 j=2。 | Dry-run |
| Boundaries violate Bleft <= Aright, so move i right. | 邊界不符 Bleft<=Aright，所以 i 右移。 | Dry-run |
| Try i equals 1, j equals 1 and both cross checks pass. | 嘗試 i=1、j=1，交叉條件都成立。 | Dry-run |
| Total is odd, answer is max(Aleft, Bleft) equals 2. | 總長奇數，答案是 max(Aleft,Bleft)=2。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one array empty, the other non-empty. | 案例一：一邊空陣列、另一邊非空。 | Edge test |
| Case two: both arrays length one. | 案例二：兩邊都只有一個元素。 | Edge test |
| Case three: total length even with two middle values. | 案例三：總長偶數需平均兩中位值。 | Edge test |
| Case four: partition touches array boundary at i equals zero or m. | 案例四：切點在 i=0 或 i=m 邊界。 | Edge test |
| Case five: values heavily imbalanced across arrays. | 案例五：兩陣列值域高度不平衡。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(log(min(m,n))). | 時間複雜度是 O(log(min(m,n)))。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Binary search range size is the shorter array length plus one. | 二分範圍是較短陣列長度加一。 | Complexity |
| Each iteration performs constant-time boundary comparisons. | 每輪只做常數次邊界比較。 | Complexity |
| So runtime is logarithmic in the shorter length. | 因此時間對較短長度是對數級。 | Complexity |
| Only a fixed number of scalar variables are used. | 僅使用固定數量標量變數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the partition condition precisely. | 我先精確重述 partition 條件。 | If stuck |
| We need Aleft <= Bright and Bleft <= Aright. | 我們需要 Aleft<=Bright 且 Bleft<=Aright。 | If stuck |
| I will verify j equals half minus i formula. | 我確認 j=half-i 公式。 | If stuck |
| I should binary search only shorter array for safe bounds. | 我應只在短陣列二分確保邊界安全。 | If stuck |
| Sentinel values handle empty-side boundaries cleanly. | 哨兵值可處理切點在邊界情況。 | If stuck |
| If Aleft is too large, I move i left. | 若 Aleft 太大，我把 i 往左移。 | If stuck |
| Otherwise I move i right. | 否則把 i 往右移。 | If stuck |
| Let me run odd and even examples again. | 我再跑一次奇數與偶數範例。 | If stuck |
| Now partition checks and median formulas are consistent. | 現在切點檢查與中位數公式一致。 | If stuck |
| Great, the final answer is stable. | 很好，最終答案穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed the partition-based median solution. | 我完成了 partition 中位數解法。 | Wrap-up |
| I verified odd and even total-length behavior. | 我驗證了奇偶總長兩種情況。 | Wrap-up |
| Runtime is O(log(min(m,n))). | 時間複雜度是 O(log(min(m,n)))。 | Wrap-up |
| Extra memory is O(1). | 額外記憶體是 O(1)。 | Wrap-up |
| I can also derive kth-element extension if needed. | 若需要我可延伸到第 k 小問題。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find median of two sorted arrays. | 找兩個排序陣列的中位數。 | Cheat sheet |
| Required time is logarithmic. | 要求時間是對數級。 | Cheat sheet |
| Brute force merge is O(m+n). | 暴力合併是 O(m+n)。 | Cheat sheet |
| Use partition binary search on shorter array. | 在短陣列做 partition 二分。 | Cheat sheet |
| Ensure A is shorter than B. | 先確保 A 比 B 短。 | Cheat sheet |
| half = (m+n+1)/2. | half=(m+n+1)/2。 | Cheat sheet |
| Choose i in A, j = half - i in B. | 在 A 選 i，B 的 j=half-i。 | Cheat sheet |
| Define Aleft/Aright with sentinels. | 用哨兵定義 Aleft/Aright。 | Cheat sheet |
| Define Bleft/Bright with sentinels. | 用哨兵定義 Bleft/Bright。 | Cheat sheet |
| Check Aleft <= Bright. | 檢查 Aleft<=Bright。 | Cheat sheet |
| Check Bleft <= Aright. | 檢查 Bleft<=Aright。 | Cheat sheet |
| If valid partition, compute median directly. | 合法切點就直接算中位數。 | Cheat sheet |
| Odd total -> max(left side). | 奇數總長 -> 左半最大值。 | Cheat sheet |
| Even total -> average of middle pair. | 偶數總長 -> 中間兩值平均。 | Cheat sheet |
| If Aleft too big, move search left. | 若 Aleft 太大，搜尋往左。 | Cheat sheet |
| Else move search right. | 否則搜尋往右。 | Cheat sheet |
| Time O(log(min(m,n))). | 時間 O(log(min(m,n)))。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: wrong j formula. | 常見 bug：j 公式寫錯。 | Cheat sheet |
| Common bug: missing sentinel boundaries. | 常見 bug：漏處理哨兵邊界。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Short-array partition binary search is preserved.
- No hallucinated constraints: ✅ Uses source constraints and median rules.
- Language simplicity: ✅ Spoken-friendly concise interview lines.
