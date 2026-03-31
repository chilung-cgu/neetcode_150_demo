# 04 Coin Change II — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/04_Coin_Change_II.md`

> Quick links: [Source Solution](../04_Coin_Change_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate coin change two. | 我先重述 Coin Change II。 | Restatement |
| We are given amount and coin denominations. | 題目給目標金額與硬幣面額。 | Restatement |
| We need number of combinations to form amount. | 要求湊成 amount 的組合數量。 | Restatement |
| Each coin can be used unlimited times. | 每種硬幣都可無限使用。 | Restatement |
| Different order of same coins counts as one combination. | 同組硬幣不同順序算同一組合。 | Restatement |
| I will solve it using unbounded knapsack DP. | 我會用完全背包 DP 解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do we return count only, not the actual combinations? | 是否只回數量，不回實際組合？ | Clarify |
| Can amount be zero in this problem? | 這題 amount 可能是 0 嗎？ | Clarify |
| Are coin values positive integers? | 硬幣面額都是正整數嗎？ | Clarify |
| Should we count combinations instead of permutations? | 這裡是算組合不是排列，對嗎？ | Clarify |
| Is O(amount times coinCount) expected? | O(amount*硬幣種類數) 是否預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursively chooses take or skip per coin. | 暴力遞迴對每個硬幣做取或不取。 | Approach |
| It re-explores the same remaining amount states. | 會重複探索相同剩餘金額狀態。 | Approach |
| Complexity is exponential without memoization. | 不做記憶化會是指數時間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[a] be number of ways to make amount a. | 定義 dp[a] 為湊出金額 a 的方法數。 | Approach |
| Base case dp[0] equals one, choose nothing. | 基底 dp[0]=1，代表什麼都不選。 | Approach |
| Iterate coins in outer loop to avoid permutation overcount. | 外層遍歷硬幣，避免排列重複計數。 | Approach |
| For each coin, iterate a from coin to amount. | 每個硬幣下，a 從 coin 到 amount。 | Approach |
| Transition is dp[a] plus equals dp[a-coin]. | 轉移為 dp[a]+=dp[a-coin]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create dp array of size amount plus one with zeros. | 我建立 amount+1 的 dp 並設為 0。 | Coding |
| I set dp[0] to one as base. | 我把 dp[0] 設為 1 當基底。 | Coding |
| I loop each coin in coins first. | 我先外層遍歷每個 coin。 | Coding |
| For current coin, I loop a from coin to amount. | 對當前 coin，a 從 coin 到 amount。 | Coding |
| I add dp[a-coin] into dp[a]. | 我把 dp[a-coin] 加到 dp[a]。 | Coding |
| This represents using current coin at least once. | 這代表至少使用一次當前硬幣。 | Coding |
| After all coins, dp[amount] is total combinations. | 全部硬幣處理後，dp[amount] 即總組合數。 | Coding |
| I return dp[amount]. | 我回傳 dp[amount]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run amount five and coins [1,2,5]. | 我手跑 amount=5、coins=[1,2,5]。 | Dry-run |
| Start with dp[0]=1 and others zero. | 起始 dp[0]=1，其餘為 0。 | Dry-run |
| After coin one, every dp[a] from one to five becomes one. | coin=1 後，dp[1..5] 都變 1。 | Dry-run |
| After coin two, dp[5] becomes three via added combinations. | coin=2 後，dp[5] 變 3。 | Dry-run |
| After coin five, dp[5] increases to four. | coin=5 後，dp[5] 增為 4。 | Dry-run |
| Final answer is four combinations. | 最終答案是 4 種組合。 | Dry-run |
| That matches the sample output. | 與範例輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: amount zero should return one. | 案例一：amount=0 應回 1。 | Edge test |
| Case two: no coin can fit target amount. | 案例二：沒有任何硬幣能湊目標。 | Edge test |
| Case three: single coin exactly divides amount. | 案例三：單一硬幣可整除目標。 | Edge test |
| Case four: coin set where order should not duplicate counts. | 案例四：檢查不同順序不重複計數。 | Edge test |
| Case five: large amount with many coin types. | 案例五：大金額與多面額。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(amount times number of coins). | 時間複雜度是 O(amount*硬幣種類數)。 | Complexity |
| Space complexity is O(amount). | 空間複雜度是 O(amount)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Outer loop goes through each coin denomination once. | 外層對每種面額跑一次。 | Complexity |
| Inner loop scans amounts from coin value to target. | 內層從 coin 掃到 target。 | Complexity |
| Total operations are O(C times A). | 總操作量是 O(C*A)。 | Complexity |
| DP array length is A plus one, so memory is O(A). | dp 長度 A+1，所以記憶體 O(A)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me confirm this is combination counting. | 我先確認這題是算組合數。 | If stuck |
| So loop order matters a lot. | 所以迴圈順序非常關鍵。 | If stuck |
| Coins must be outer loop to avoid permutations. | 硬幣必須放外層避免排列重複。 | If stuck |
| dp[a] means number of ways to make a. | dp[a] 代表湊成 a 的方法數。 | If stuck |
| Base dp[0]=1 is mandatory. | 基底 dp[0]=1 必不可少。 | If stuck |
| Transition is dp[a]+=dp[a-coin]. | 轉移是 dp[a]+=dp[a-coin]。 | If stuck |
| Let me test quickly with amount three and coin two. | 我快速測 amount=3、coin=2。 | If stuck |
| dp[3] stays zero if no valid combination exists. | 若無組合，dp[3] 會維持 0。 | If stuck |
| For amount five with [1,2,5], we should get four. | amount=5、[1,2,5] 應得到 4。 | If stuck |
| Great, the recurrence is consistent. | 很好，遞推邏輯一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved coin change two with unbounded knapsack DP. | 我用完全背包 DP 解了 Coin Change II。 | Wrap-up |
| dp[a] stores number of combinations for amount a. | dp[a] 存的是金額 a 的組合數。 | Wrap-up |
| Using coins in outer loop prevents permutation overcount. | 以硬幣做外層可避免排列重複計數。 | Wrap-up |
| Complexity is O(C*A) time and O(A) space. | 複雜度是 O(C*A) 時間、O(A) 空間。 | Wrap-up |
| This aligns with interview expectations for this problem. | 這符合該題面試常見期望。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: count combinations to form amount. | 目標：計算湊成 amount 的組合數。 | Cheat sheet |
| Coins are reusable unlimited times. | 硬幣可無限使用。 | Cheat sheet |
| Order does not matter. | 順序不重要。 | Cheat sheet |
| Define dp[a] as way count for amount a. | 定義 dp[a] 為金額 a 的方法數。 | Cheat sheet |
| Initialize dp with zeros. | dp 初值設 0。 | Cheat sheet |
| Set dp[0]=1. | 設 dp[0]=1。 | Cheat sheet |
| Loop coin in outer loop. | 外層迴圈跑 coin。 | Cheat sheet |
| Loop a from coin to amount. | a 從 coin 到 amount。 | Cheat sheet |
| Transition dp[a]+=dp[a-coin]. | 轉移 dp[a]+=dp[a-coin]。 | Cheat sheet |
| Return dp[amount]. | 回傳 dp[amount]。 | Cheat sheet |
| amount=0 -> 1. | amount=0 -> 1。 | Cheat sheet |
| [1,2,5], amount 5 -> 4. | [1,2,5]、amount 5 -> 4。 | Cheat sheet |
| No fit coin -> 0. | 沒有可用面額 -> 0。 | Cheat sheet |
| Time O(C*A). | 時間 O(C*A)。 | Cheat sheet |
| Space O(A). | 空間 O(A)。 | Cheat sheet |
| Common bug: reversed loops causing permutation counts. | 常見錯誤：迴圈反了導致算到排列。 | Cheat sheet |
| Common bug: forgetting dp[0]=1. | 常見錯誤：忘記 dp[0]=1。 | Cheat sheet |
| Mention unbounded knapsack framing. | 可提完全背包框架。 | Cheat sheet |
| Explain loop order clearly in interview. | 面試要清楚解釋迴圈順序。 | Cheat sheet |
| Validate with one impossible case. | 記得加一個無解案例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Combination-count DP and loop-order rationale preserved.
- No hallucinated constraints: ✅ Unlimited coin reuse and order-insensitive counting maintained.
- Language simplicity: ✅ Interview-friendly lines emphasizing recurrence and loop semantics.
