# 12 Partition Equal Subset Sum — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/12_Partition_Equal_Subset_Sum.md`

> Quick links: [Source Solution](../12_Partition_Equal_Subset_Sum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate partition equal subset sum. | 我先重述分割等和子集題。 | Restatement |
| We have a non-empty array of positive integers. | 題目給一個非空正整數陣列。 | Restatement |
| We need to decide whether it can be split into two subsets with equal sum. | 要判斷能否切成兩個和相等子集。 | Restatement |
| Equivalent form is finding subset sum equal to total divided by two. | 等價於找子集和等於總和的一半。 | Restatement |
| If total sum is odd, answer is immediately false. | 若總和為奇數，答案立即是 false。 | Restatement |
| I will use one-dimensional 0/1 knapsack DP. | 我會用一維 0/1 背包 DP。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are all numbers guaranteed positive? | 是否保證所有數字皆為正？ | Clarify |
| Do we return boolean only? | 是否只回傳布林值？ | Clarify |
| Is constructing actual subsets unnecessary? | 不需要輸出實際子集，對嗎？ | Clarify |
| Should I present set-based DP first or knapsack DP first? | 要先講 set DP 還是背包 DP？ | Clarify |
| Is O(n times target) acceptable for constraints? | O(n*target) 在限制下可接受嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force assigns each number to left or right subset. | 暴力法把每個數字分配到左右子集。 | Approach |
| That explores two choices per element recursively. | 每個元素遞迴都有兩種選擇。 | Approach |
| Worst-case runtime is O(2 power n). | 最壞時間是 O(2^n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First compute total sum and reject odd sum early. | 先算總和，奇數可提前拒絕。 | Approach |
| Target becomes total divided by two. | 目標值是 total/2。 | Approach |
| Define dp[t] as whether sum t is achievable. | 定義 dp[t] 表示和 t 是否可達。 | Approach |
| For each number num, iterate t backward from target to num. | 每個 num 讓 t 從 target 反向到 num。 | Approach |
| Update dp[t] with dp[t] or dp[t-num], final answer dp[target]. | 轉移 dp[t]=dp[t]或dp[t-num]，最終看 dp[target]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I compute totalSum using accumulation. | 我先用累加得到 totalSum。 | Coding |
| If totalSum is odd, I return false immediately. | 若 totalSum 為奇數，立即回 false。 | Coding |
| I set target to totalSum divided by two. | 設 target=totalSum/2。 | Coding |
| I create dp boolean array of size target plus one. | 建立大小 target+1 的布林 dp。 | Coding |
| Base case dp[0] is true. | 基底 dp[0]=true。 | Coding |
| For each num in nums, I iterate t from target down to num. | 對每個 num，t 從 target 反向到 num。 | Coding |
| I update dp[t] as dp[t] OR dp[t-num]. | 更新 dp[t]=dp[t] OR dp[t-num]。 | Coding |
| After processing all numbers, I return dp[target]. | 處理完所有數字後回 dp[target]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [1,5,11,5]. | 我手跑 nums=[1,5,11,5]。 | Dry-run |
| Total sum is twenty-two, so target is eleven. | 總和 22，所以 target=11。 | Dry-run |
| Start with dp[0] true, others false. | 起始 dp[0]=true，其餘 false。 | Dry-run |
| After processing one and five, sums one six become reachable. | 處理 1 與 5 後，和 1、6 可達。 | Dry-run |
| When processing eleven, dp[11] becomes true directly. | 處理 11 時，dp[11] 直接成真。 | Dry-run |
| Remaining processing keeps dp[11] true. | 後續處理維持 dp[11] 為真。 | Dry-run |
| Final answer is true. | 最終答案是 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: odd total like [1,2,3,5] should return false quickly. | 案例一：總和奇數如 [1,2,3,5] 應快速回 false。 | Edge test |
| Case two: single element cannot split equally. | 案例二：單一元素無法等分。 | Edge test |
| Case three: exact single-number hit to target. | 案例三：有單一數字剛好命中 target。 | Edge test |
| Case four: duplicates requiring correct backward iteration. | 案例四：含重複值，需正確反向迭代。 | Edge test |
| Case five: large values near constraint boundary. | 案例五：接近限制邊界的大數值。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n times target). | 時間複雜度是 O(n*target)。 | Complexity |
| Space complexity is O(target). | 空間複雜度是 O(target)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We run one loop over n numbers. | 我們會對 n 個數字跑一層迴圈。 | Complexity |
| For each number we sweep target down to num. | 每個數字都從 target 反向掃到 num。 | Complexity |
| Thus runtime is O(n times target). | 因此時間是 O(n*target)。 | Complexity |
| DP table has target plus one booleans, so memory is O(target). | DP 只有 target+1 個布林值，故空間 O(target)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me convert this to subset-sum form first. | 我先把題目轉成 subset-sum 形式。 | If stuck |
| Equal partition means target is total divided by two. | 等分代表 target 是 total/2。 | If stuck |
| Odd total immediately means impossible. | 總和奇數立即不可能。 | If stuck |
| dp[t] tracks whether sum t can be formed. | dp[t] 追蹤和 t 是否可形成。 | If stuck |
| Base dp[0] equals true. | 基底 dp[0]=true。 | If stuck |
| I must iterate backward to keep 0/1 usage. | 必須反向迭代以維持 0/1 使用。 | If stuck |
| Forward iteration would reuse same number multiple times. | 正向迭代會重複使用同一數字。 | If stuck |
| Let me test odd-total case quickly. | 我快速測試奇數總和案例。 | If stuck |
| It returns false before DP, which is correct. | 在 DP 前回 false，這是正確的。 | If stuck |
| Great, transition and direction are now clear. | 很好，轉移與方向都清楚了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved this as a 0/1 subset-sum DP problem. | 我把這題當 0/1 subset-sum DP 解。 | Wrap-up |
| Odd total is a fast impossible check. | 總和奇數是快速無解判斷。 | Wrap-up |
| One-dimensional boolean DP tracks reachable sums. | 一維布林 DP 追蹤可達和。 | Wrap-up |
| Backward iteration enforces each number used at most once. | 反向迭代確保每個數最多用一次。 | Wrap-up |
| Complexity is O(n*target) time and O(target) space. | 複雜度為 O(n*target) 時間、O(target) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: split array into two equal-sum subsets. | 目標：把陣列分成兩個等和子集。 | Cheat sheet |
| Equivalent target is total/2 subset sum. | 等價目標是找 total/2 的子集和。 | Cheat sheet |
| If total is odd, return false. | 若總和是奇數，回 false。 | Cheat sheet |
| Define dp[t] as reachable sum t. | 定義 dp[t] 為和 t 是否可達。 | Cheat sheet |
| Initialize dp[0]=true. | 初始化 dp[0]=true。 | Cheat sheet |
| Set target=total/2. | 設 target=total/2。 | Cheat sheet |
| For each num, iterate t from target down to num. | 對每個 num，t 從 target 反向到 num。 | Cheat sheet |
| Update dp[t]=dp[t] or dp[t-num]. | 更新 dp[t]=dp[t] 或 dp[t-num]。 | Cheat sheet |
| Backward loop prevents reuse in same round. | 反向迴圈避免同輪重複使用。 | Cheat sheet |
| Final answer is dp[target]. | 最終答案看 dp[target]。 | Cheat sheet |
| Example [1,5,11,5] -> true. | 範例 [1,5,11,5] -> true。 | Cheat sheet |
| Example [1,2,3,5] -> false. | 範例 [1,2,3,5] -> false。 | Cheat sheet |
| Single element usually false. | 單元素通常為 false。 | Cheat sheet |
| Time O(n*target). | 時間 O(n*target)。 | Cheat sheet |
| Space O(target). | 空間 O(target)。 | Cheat sheet |
| Common bug: forget odd-sum shortcut. | 常見錯誤：忘記奇數總和捷徑。 | Cheat sheet |
| Common bug: iterate t forward. | 常見錯誤：t 用正向迭代。 | Cheat sheet |
| Forward iteration breaks 0/1 rule. | 正向會破壞 0/1 規則。 | Cheat sheet |
| Keep state meaning simple and explicit. | 狀態定義保持簡潔明確。 | Cheat sheet |
| Explain why backward order is mandatory. | 面試時說清楚為何必須反向。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Odd-sum precheck and 1D knapsack transition preserved.
- No hallucinated constraints: ✅ Positive integers and boolean decision semantics maintained.
- Language simplicity: ✅ Interview-ready lines focused on subset-sum framing and loop direction.
