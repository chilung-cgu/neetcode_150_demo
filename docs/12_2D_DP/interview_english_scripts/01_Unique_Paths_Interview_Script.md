# 01 Unique Paths — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/01_Unique_Paths.md`

> Quick links: [Source Solution](../01_Unique_Paths.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the unique paths problem. | 我先重述 Unique Paths 題目。 | Restatement |
| We have an m by n grid. | 題目給一個 m*n 的網格。 | Restatement |
| Robot starts at top-left and wants to reach bottom-right. | 機器人從左上走到右下。 | Restatement |
| It can only move right or down each step. | 每步只能往右或往下。 | Restatement |
| We need the number of different valid paths. | 要求不同有效路徑總數。 | Restatement |
| I will solve it with dynamic programming. | 我會用動態規劃解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are there any blocked cells in this version? | 這版有障礙格嗎？ | Clarify |
| Is m and n always at least one? | m 與 n 都至少是 1 嗎？ | Clarify |
| Should the answer fit in 32-bit integer as stated? | 答案可放入 32 位整數嗎？ | Clarify |
| Do we only need the count, not actual paths? | 只要數量，不需輸出路徑嗎？ | Clarify |
| Is O(m times n) expected? | O(m*n) 是否為預期解？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A brute-force DFS tries right and down at every cell. | 暴力 DFS 在每格都試右和下。 | Approach |
| It recomputes many overlapping subproblems. | 會重複計算大量重疊子問題。 | Approach |
| Runtime grows exponentially with grid dimensions. | 時間會隨網格大小呈指數成長。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[j] be ways to reach current row at column j. | 令 dp[j] 為目前列到達第 j 欄的方法數。 | Approach |
| First row is all ones because only right moves are possible. | 第一列全是 1，因為只能一路向右。 | Approach |
| For each next row, first column stays one. | 每一新列的第一欄都維持 1。 | Approach |
| Transition is dp[j] equals dp[j] plus dp[j-1]. | 轉移為 dp[j]=dp[j]+dp[j-1]。 | Approach |
| Final answer is dp[n-1]. | 最終答案是 dp[n-1]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create a one-dimensional dp array of size n and initialize with one. | 我建立大小 n 的一維 dp，初值全 1。 | Coding |
| I loop row index i from one to m minus one. | 列索引 i 從 1 到 m-1。 | Coding |
| Inside each row, I loop column j from one to n minus one. | 每列內部欄索引 j 從 1 到 n-1。 | Coding |
| I update dp[j] by adding dp[j-1]. | 我用 dp[j-1] 加到 dp[j]。 | Coding |
| dp[j] old is from top, dp[j-1] is from left. | 舊 dp[j] 代表上方，dp[j-1] 代表左方。 | Coding |
| After finishing all rows, I return dp[n-1]. | 全部列處理後回傳 dp[n-1]。 | Coding |
| This keeps logic clear and space efficient. | 這個寫法清楚且節省空間。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run m equals three and n equals seven. | 我手跑 m=3、n=7。 | Dry-run |
| Initial dp is [1,1,1,1,1,1,1]. | 初始 dp 是 [1,1,1,1,1,1,1]。 | Dry-run |
| After second row, dp becomes [1,2,3,4,5,6,7]. | 第二列後 dp 變成 [1,2,3,4,5,6,7]。 | Dry-run |
| After third row, dp becomes [1,3,6,10,15,21,28]. | 第三列後 dp 變成 [1,3,6,10,15,21,28]。 | Dry-run |
| Final value at last column is twenty-eight. | 最後一欄值是 28。 | Dry-run |
| So the answer is twenty-eight. | 所以答案是 28。 | Dry-run |
| It matches the sample output. | 與範例輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: m equals one should return one. | 案例一：m=1 應回 1。 | Edge test |
| Case two: n equals one should return one. | 案例二：n=1 應回 1。 | Edge test |
| Case three: two by two grid should return two. | 案例三：2x2 網格應回 2。 | Edge test |
| Case four: large square near bounds for overflow check. | 案例四：接近上限的大方格檢查溢位。 | Edge test |
| Case five: asymmetric grid like three by seven. | 案例五：不對稱網格如 3x7。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(n). | 空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We process each cell once with two nested loops. | 我們用雙迴圈逐格處理一次。 | Complexity |
| Each update does only constant-time arithmetic. | 每次更新只做常數時間運算。 | Complexity |
| Therefore runtime is O(m times n). | 因此時間是 O(m*n)。 | Complexity |
| One row array of length n gives O(n) extra memory. | 只用長度 n 的列陣列，所以額外空間 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define the DP meaning first. | 我先定義 DP 的意義。 | If stuck |
| dp[j] is paths to current row and column j. | dp[j] 是目前列第 j 欄路徑數。 | If stuck |
| First row and first column should stay one. | 第一列與第一欄都應維持 1。 | If stuck |
| Each cell gets paths from top plus left. | 每格來自上方加左方。 | If stuck |
| In 1D form, top is old dp[j]. | 在一維寫法，上方是舊 dp[j]。 | If stuck |
| Left is updated dp[j-1]. | 左方是已更新的 dp[j-1]。 | If stuck |
| So update rule is dp[j] plus equals dp[j-1]. | 所以更新規則是 dp[j]+=dp[j-1]。 | If stuck |
| Let me test quickly with two by two. | 我快速測 2x2。 | If stuck |
| It gives two paths, so transition is correct. | 會得到 2 條路徑，轉移正確。 | If stuck |
| Great, I can continue coding confidently. | 很好，我可以繼續實作。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved unique paths with bottom-up DP. | 我用自底向上 DP 解了 Unique Paths。 | Wrap-up |
| State transition is top plus left path count. | 狀態轉移是上方加左方路徑數。 | Wrap-up |
| One-dimensional compression keeps space small. | 一維壓縮讓空間更小。 | Wrap-up |
| Complexity is O(m*n) time and O(n) space. | 複雜度是 O(m*n) 時間、O(n) 空間。 | Wrap-up |
| I can also mention combinatorics as follow-up. | 追問時我也可補充組合數解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: count paths from top-left to bottom-right. | 目標：計算左上到右下的路徑數。 | Cheat sheet |
| Moves allowed: right or down only. | 只能往右或往下。 | Cheat sheet |
| No obstacles in this version. | 這版沒有障礙物。 | Cheat sheet |
| Use DP over grid states. | 使用網格狀態 DP。 | Cheat sheet |
| 1D dp[j] stores current-row path count. | 一維 dp[j] 存目前列路徑數。 | Cheat sheet |
| Initialize dp with all ones. | dp 初值全部設 1。 | Cheat sheet |
| Row loop from 1 to m-1. | 列迴圈從 1 到 m-1。 | Cheat sheet |
| Column loop from 1 to n-1. | 欄迴圈從 1 到 n-1。 | Cheat sheet |
| Transition: dp[j] += dp[j-1]. | 轉移：dp[j] += dp[j-1]。 | Cheat sheet |
| dp[j] old is from top. | 舊 dp[j] 代表上方。 | Cheat sheet |
| dp[j-1] is from left. | dp[j-1] 代表左方。 | Cheat sheet |
| Answer is dp[n-1]. | 答案是 dp[n-1]。 | Cheat sheet |
| Example 3x7 gives 28. | 範例 3x7 得 28。 | Cheat sheet |
| m=1 or n=1 returns 1. | m=1 或 n=1 都回 1。 | Cheat sheet |
| Time O(m*n). | 時間 O(m*n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Common bug: wrong loop direction assumptions. | 常見錯誤：迴圈方向理解錯。 | Cheat sheet |
| Common bug: forgetting first row/col base value 1. | 常見錯誤：忘記首列首欄基底為 1。 | Cheat sheet |
| Mention combinatorics as alternative solution. | 可提組合數作替代解。 | Cheat sheet |
| Keep explanation focused on transition meaning. | 說明聚焦在轉移意義。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ 1D DP transition and base handling preserved.
- No hallucinated constraints: ✅ Right/down only, count-only output, no obstacles.
- Language simplicity: ✅ Interview-safe phrasing with explicit state mapping.
