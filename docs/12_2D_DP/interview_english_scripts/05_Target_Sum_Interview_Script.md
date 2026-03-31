# 05 Target Sum — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/05_Target_Sum.md`

> Quick links: [Source Solution](../05_Target_Sum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the target sum problem. | 我先重述 Target Sum 題目。 | Restatement |
| We are given nums and an integer target. | 題目給 nums 與整數 target。 | Restatement |
| For each number, we choose plus or minus sign. | 每個數字前都可選加號或減號。 | Restatement |
| We need the number of sign assignments reaching target. | 要求可達 target 的指派方式數量。 | Restatement |
| This is counting ways, not checking existence only. | 這是計算方法數，不只是判定可不可達。 | Restatement |
| I will convert it to a subset-sum counting DP. | 我會轉成子集合和計數 DP。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are all nums non-negative as in constraints? | nums 是否皆為非負整數？ | Clarify |
| Do we return number of ways as integer count? | 是否回傳方法數的整數？ | Clarify |
| Can target be negative? | target 可以是負數嗎？ | Clarify |
| Is answer guaranteed to fit 32-bit integer? | 答案是否保證在 32 位整數內？ | Clarify |
| Is O(n times sum) DP acceptable here? | O(n*sum) DP 是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force explores two choices plus or minus per index. | 暴力法每個索引都分成加或減兩分支。 | Approach |
| It forms a full binary recursion tree. | 會形成完整的二元遞迴樹。 | Approach |
| Complexity is O(2 power n) without memoization. | 不記憶化時複雜度是 O(2^n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let total be sum of all numbers. | 先令 total 為所有數字總和。 | Approach |
| If P is positive subset and N is negative subset, then P minus N equals target. | 若 P 為正子集、N 為負子集，則 P-N=target。 | Approach |
| Also P plus N equals total, so P equals (target plus total) divided by two. | 又有 P+N=total，因此 P=(target+total)/2。 | Approach |
| We count subsets whose sum equals that derived value. | 接著計算和等於該值的子集數量。 | Approach |
| Use 0/1 knapsack counting with backward loop. | 使用 0/1 背包計數並反向迴圈。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I compute total sum of nums first. | 我先計算 nums 的 total sum。 | Coding |
| If target is outside plus minus total range, return zero. | 若 target 超出 ±total 範圍，回 0。 | Coding |
| If target plus total is odd, return zero. | 若 target+total 為奇數，回 0。 | Coding |
| I set subsetSum to (target plus total) divided by two. | 我令 subsetSum=(target+total)/2。 | Coding |
| I create dp array of size subsetSum plus one with zeros. | 建立大小 subsetSum+1 的 dp，初值 0。 | Coding |
| Base case dp[0] equals one. | 基底 dp[0]=1。 | Coding |
| For each num, loop j from subsetSum down to num. | 對每個 num，j 從 subsetSum 反向到 num。 | Coding |
| Update dp[j] by adding dp[j-num], then return dp[subsetSum]. | 更新 dp[j]+=dp[j-num]，最後回 dp[subsetSum]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [1,1,1,1,1] and target three. | 我手跑 nums=[1,1,1,1,1]、target=3。 | Dry-run |
| Total is five, so subsetSum is four. | total=5，因此 subsetSum=4。 | Dry-run |
| Initialize dp[0]=1 and others zero. | 初始 dp[0]=1，其餘 0。 | Dry-run |
| After processing all five ones, dp[4] becomes five. | 五個 1 都處理後，dp[4] 變成 5。 | Dry-run |
| That means five valid sign assignments. | 代表有 5 種有效正負指派。 | Dry-run |
| Final answer is five. | 最終答案是 5。 | Dry-run |
| It matches sample output. | 與範例輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: target outside reachable range should return zero. | 案例一：target 超可達範圍應回 0。 | Edge test |
| Case two: target plus total odd should return zero. | 案例二：target+total 奇數應回 0。 | Edge test |
| Case three: many zeros increase counting multiplicity. | 案例三：多個 0 會增加計數倍數。 | Edge test |
| Case four: single number equal to target. | 案例四：單一數字剛好等於 target。 | Edge test |
| Case five: negative target with valid assignments. | 案例五：負 target 但仍可達。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n times subsetSum). | 時間複雜度是 O(n*subsetSum)。 | Complexity |
| Space complexity is O(subsetSum). | 空間複雜度是 O(subsetSum)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We iterate all n numbers once. | 我們會遍歷 n 個數字一次。 | Complexity |
| For each number, we scan subset sums backward. | 每個數字下反向掃描子集合和。 | Complexity |
| Therefore runtime is O(n times subsetSum). | 因此時間是 O(n*subsetSum)。 | Complexity |
| DP array size is subsetSum plus one, giving O(subsetSum) memory. | dp 大小為 subsetSum+1，故空間 O(subsetSum)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me convert sign assignment to subset equation first. | 我先把正負指派轉成子集方程。 | If stuck |
| Define P as positives and N as negatives. | 定義 P 為正集合、N 為負集合。 | If stuck |
| P minus N equals target and P plus N equals total. | P-N=target 且 P+N=total。 | If stuck |
| So P equals target plus total over two. | 所以 P=(target+total)/2。 | If stuck |
| If this value is not integer, answer is zero. | 若不是整數，答案就是 0。 | If stuck |
| Then it becomes counting subset-sum ways. | 接著就變成子集合和計數問題。 | If stuck |
| I should use backward loop for 0/1 usage. | 我應該用反向迴圈維持 0/1 使用。 | If stuck |
| dp[0]=1 represents empty subset baseline. | dp[0]=1 代表空集合基底。 | If stuck |
| Let me test sample to verify count five. | 我用範例測得 5 來驗證。 | If stuck |
| Great, conversion and DP are correct. | 很好，轉換與 DP 都正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved target sum by reducing it to subset-sum counting. | 我把 Target Sum 轉成子集合和計數來解。 | Wrap-up |
| Key formula is subsetSum equals target plus total over two. | 關鍵公式是 subsetSum=(target+total)/2。 | Wrap-up |
| Invalid parity or range gives immediate zero. | 奇偶或範圍不合法可立即回 0。 | Wrap-up |
| DP uses 0/1 knapsack counting with backward iteration. | DP 使用 0/1 背包計數與反向迭代。 | Wrap-up |
| Complexity is O(n*subsetSum) time and O(subsetSum) space. | 複雜度為 O(n*subsetSum) 時間、O(subsetSum) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: count sign assignments reaching target. | 目標：計算達成 target 的正負指派數。 | Cheat sheet |
| Let total=sum(nums). | 設 total=sum(nums)。 | Cheat sheet |
| Equation: P-N=target. | 方程：P-N=target。 | Cheat sheet |
| Equation: P+N=total. | 方程：P+N=total。 | Cheat sheet |
| Derive P=(target+total)/2. | 推得 P=(target+total)/2。 | Cheat sheet |
| If out of range, return 0. | 若超出範圍回 0。 | Cheat sheet |
| If parity invalid, return 0. | 若奇偶不合法回 0。 | Cheat sheet |
| Now count subsets summing to P. | 接著計算和為 P 的子集數。 | Cheat sheet |
| dp[j] = ways to form sum j. | dp[j] 代表湊出 j 的方法數。 | Cheat sheet |
| Initialize dp[0]=1. | 初始化 dp[0]=1。 | Cheat sheet |
| For each num, loop j backward. | 每個 num 下 j 反向迴圈。 | Cheat sheet |
| Update dp[j]+=dp[j-num]. | 更新 dp[j]+=dp[j-num]。 | Cheat sheet |
| Return dp[P]. | 回傳 dp[P]。 | Cheat sheet |
| Example [1,1,1,1,1],3 -> 5. | 範例 [1,1,1,1,1],3 -> 5。 | Cheat sheet |
| Zero values can double counts. | 0 值可能讓計數倍增。 | Cheat sheet |
| Time O(n*P). | 時間 O(n*P)。 | Cheat sheet |
| Space O(P). | 空間 O(P)。 | Cheat sheet |
| Common bug: forget parity check. | 常見錯誤：忘記奇偶檢查。 | Cheat sheet |
| Common bug: forward loop causing reuse bug. | 常見錯誤：正向迴圈導致重複使用。 | Cheat sheet |
| Explain algebra transformation clearly first. | 先清楚講代數轉換。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Algebraic reduction and 0/1 counting DP preserved.
- No hallucinated constraints: ✅ Proper range/parity guards and count semantics maintained.
- Language simplicity: ✅ Clear interview phrasing for transformation and loop direction.
