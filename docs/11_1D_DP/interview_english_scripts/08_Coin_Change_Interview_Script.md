# 08 Coin Change — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/08_Coin_Change.md`

> Quick links: [Source Solution](../08_Coin_Change.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the coin change problem. | 我先重述 Coin Change。 | Restatement |
| We have coin denominations and a target amount. | 題目給硬幣面額與目標金額。 | Restatement |
| We need minimum number of coins to make that amount. | 要求湊出該金額的最少硬幣數。 | Restatement |
| We can use each coin denomination unlimited times. | 每種硬幣可無限使用。 | Restatement |
| If impossible to form amount, return minus one. | 若無法湊出就回傳 -1。 | Restatement |
| I will use bottom-up DP over amount values. | 我會用自底向上 DP 依金額推進。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is amount allowed to be zero? | amount 是否可能為 0？ | Clarify |
| Are all coin values positive integers? | 硬幣面額是否皆為正整數？ | Clarify |
| Should I return minimum count only, not actual combination? | 是否只回最少數量，不回具體組合？ | Clarify |
| Can we treat amount plus one as infinity sentinel? | 可用 amount+1 當作無限大哨兵嗎？ | Clarify |
| Is O(amount times coinTypes) acceptable? | O(amount*硬幣種類數) 是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursively tries subtracting each coin. | 暴力遞迴嘗試減去每一種硬幣。 | Approach |
| Many states like amount five are recomputed repeatedly. | 像 amount=5 的狀態會重複計算。 | Approach |
| Runtime is exponential in worst cases. | 最壞情況時間為指數級。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Define dp[a] as minimum coins to make amount a. | 定義 dp[a] 為湊成 a 的最少硬幣數。 | Approach |
| Base case dp[0] equals zero. | 基底是 dp[0]=0。 | Approach |
| Initialize others to amount plus one as impossible sentinel. | 其餘初始化為 amount+1 當不可能哨兵。 | Approach |
| Transition is dp[a] equals min(dp[a], one plus dp[a-c]). | 轉移為 dp[a]=min(dp[a],1+dp[a-c])。 | Approach |
| Final answer is dp[amount] unless still sentinel. | 最後看 dp[amount] 是否仍為哨兵。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create dp array of size amount plus one. | 我建立大小 amount+1 的 dp 陣列。 | Coding |
| I fill with amount plus one and set dp zero to zero. | 先填 amount+1，再設 dp[0]=0。 | Coding |
| I loop a from one to amount. | a 從 1 迭代到 amount。 | Coding |
| For each coin c, if a minus c is non-negative I can transition. | 對每個 coin c，若 a-c>=0 就可轉移。 | Coding |
| I update dp[a] with min of current and one plus dp[a-c]. | 用目前值與 1+dp[a-c] 取 min 更新 dp[a]。 | Coding |
| After loops, dp[amount] is optimal or impossible sentinel. | 迴圈後 dp[amount] 會是最優值或哨兵。 | Coding |
| If dp[amount] greater than amount, return minus one. | 若 dp[amount]>amount，回 -1。 | Coding |
| Otherwise return dp[amount]. | 否則回 dp[amount]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run coins [1,2,5] and amount eleven. | 我手跑 coins=[1,2,5]、amount=11。 | Dry-run |
| dp zero is zero, others start as twelve sentinel. | dp[0]=0，其餘起始為 12 哨兵。 | Dry-run |
| For amount one, best becomes one using coin one. | amount=1 時用 coin1 得最小值 1。 | Dry-run |
| Progressively dp values improve by transitions. | 隨著轉移 dp 值逐步改善。 | Dry-run |
| At amount ten, dp is two via five plus five. | 到 amount=10，dp=2（5+5）。 | Dry-run |
| At amount eleven, dp becomes three via five five one. | 到 amount=11，dp=3（5+5+1）。 | Dry-run |
| Final answer is three, matching expected output. | 最終答案 3，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: amount zero should return zero. | 案例一：amount=0 應回 0。 | Edge test |
| Case two: no combination possible like coins [2] amount three. | 案例二：如 [2],3 無解應回 -1。 | Edge test |
| Case three: single coin exactly matches amount. | 案例三：單一硬幣剛好等於 amount。 | Edge test |
| Case four: one-value coin always allows solution. | 案例四：有面額 1 時一定可解。 | Edge test |
| Case five: large amount with sparse coin set. | 案例五：大金額且面額稀疏。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(amount times number of coins). | 時間複雜度是 O(amount*硬幣種類數)。 | Complexity |
| Space complexity is O(amount). | 空間複雜度是 O(amount)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Outer loop iterates each amount from one to target. | 外層迴圈遍歷 1 到 target 各金額。 | Complexity |
| Inner loop checks every coin denomination for transition. | 內層迴圈對每種面額嘗試轉移。 | Complexity |
| Thus runtime is O(A times C), where A is amount and C is coin types. | 因此時間是 O(A*C)，A 為 amount、C 為種類數。 | Complexity |
| DP array length is A plus one, so memory is O(A). | DP 陣列長度 A+1，故記憶體 O(A)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define dp state first to avoid confusion. | 我先定義 dp 狀態避免混亂。 | If stuck |
| dp[a] means minimum coins for amount a. | dp[a] 表示湊 a 的最少硬幣數。 | If stuck |
| Base dp[0] must be zero. | 基底 dp[0] 必須是 0。 | If stuck |
| Impossible states should start from big sentinel value. | 不可能狀態先設大哨兵值。 | If stuck |
| Transition is one plus dp[a-c] if a-c is valid. | 轉移是 1+dp[a-c]（若 a-c 合法）。 | If stuck |
| We take min across all coin choices. | 對所有硬幣選擇取最小。 | If stuck |
| Let me verify quickly with amount three and coin two. | 我快速驗證 amount=3、coin=2。 | If stuck |
| dp[3] remains sentinel, so answer is minus one. | dp[3] 仍是哨兵，因此答案 -1。 | If stuck |
| For [1,2,5], eleven gives three. | 對 [1,2,5]，11 得 3。 | If stuck |
| Great, recurrence and sentinel logic are consistent. | 很好，遞推與哨兵邏輯一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved coin change with bottom-up DP. | 我用自底向上 DP 解出 Coin Change。 | Wrap-up |
| State dp[a] stores minimum coins for amount a. | 狀態 dp[a] 存金額 a 的最少硬幣數。 | Wrap-up |
| We relax transitions using every coin denomination. | 我們用每個面額做轉移鬆弛。 | Wrap-up |
| Sentinel value handles impossible states cleanly. | 哨兵值可乾淨處理無解狀態。 | Wrap-up |
| Complexity is O(A*C) time and O(A) space. | 複雜度是 O(A*C) 時間、O(A) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem: minimum coins for target amount. | 題目：湊目標金額的最少硬幣。 | Cheat sheet |
| Coins can be reused unlimited times. | 硬幣可無限重用。 | Cheat sheet |
| Return -1 if impossible. | 無解回 -1。 | Cheat sheet |
| Define dp[a] minimum coins for a. | 定義 dp[a] 為 a 的最少硬幣。 | Cheat sheet |
| Initialize dp with amount+1. | dp 初值設 amount+1。 | Cheat sheet |
| Set dp[0] = 0. | 設 dp[0]=0。 | Cheat sheet |
| Loop a from 1 to amount. | a 從 1 到 amount。 | Cheat sheet |
| For each coin c try transition. | 每個 coin c 嘗試轉移。 | Cheat sheet |
| If a-c>=0, candidate=1+dp[a-c]. | 若 a-c>=0，候選值=1+dp[a-c]。 | Cheat sheet |
| dp[a]=min(dp[a], candidate). | dp[a]=min(dp[a],候選值)。 | Cheat sheet |
| After fill, inspect dp[amount]. | 填完後檢查 dp[amount]。 | Cheat sheet |
| If > amount then impossible. | 若 > amount 代表無解。 | Cheat sheet |
| Else return dp[amount]. | 否則回 dp[amount]。 | Cheat sheet |
| amount=0 returns 0. | amount=0 回 0。 | Cheat sheet |
| [2],3 returns -1. | [2],3 回 -1。 | Cheat sheet |
| [1,2,5],11 returns 3. | [1,2,5],11 回 3。 | Cheat sheet |
| Time O(A*C). | 時間 O(A*C)。 | Cheat sheet |
| Space O(A). | 空間 O(A)。 | Cheat sheet |
| Common bug: forgetting dp[0]=0. | 常見錯誤：忘記 dp[0]=0。 | Cheat sheet |
| Common bug: using bad infinity sentinel. | 常見錯誤：無限大哨兵設錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Bottom-up DP recurrence and sentinel pattern preserved.
- No hallucinated constraints: ✅ Correct impossible handling and unlimited coin usage.
- Language simplicity: ✅ Interview-ready concise lines with explicit state meaning.
