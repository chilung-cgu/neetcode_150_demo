# 02 Longest Common Subsequence — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/02_Longest_Common_Subsequence.md`

> Quick links: [Source Solution](../02_Longest_Common_Subsequence.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate longest common subsequence. | 我先重述最長公共子序列題。 | Restatement |
| We are given two strings text1 and text2. | 題目給兩個字串 text1 與 text2。 | Restatement |
| We need the length of their longest common subsequence. | 要求兩者最長公共子序列長度。 | Restatement |
| Subsequence keeps order but does not need to be contiguous. | 子序列保留順序但不需連續。 | Restatement |
| We only return length, not the actual sequence. | 只回長度，不需回序列內容。 | Restatement |
| I will solve it with classic two-dimensional DP. | 我會用經典二維 DP 解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do we need only the length of LCS? | 是否只需要 LCS 長度？ | Clarify |
| Can strings include lowercase letters only? | 字串是否僅含小寫字母？ | Clarify |
| Is O(m times n) acceptable for this problem size? | O(m*n) 在此規模可接受嗎？ | Clarify |
| Should I mention one-dimensional space optimization as follow-up? | 需要補充一維空間優化嗎？ | Clarify |
| Are empty strings possible in this version? | 這版是否可能出現空字串？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursively tries match or skip decisions. | 暴力遞迴嘗試匹配或跳過決策。 | Approach |
| This creates many overlapping suffix subproblems. | 會產生大量重疊後綴子問題。 | Approach |
| Runtime becomes exponential and impractical. | 時間會變成指數級且不實用。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[i][j] be LCS length of text1 prefix i and text2 prefix j. | 定義 dp[i][j] 為兩前綴的 LCS 長度。 | Approach |
| If current characters match, take diagonal plus one. | 當前字元相同則取左上角加一。 | Approach |
| If they differ, take max of top and left cells. | 若不同則取上方與左方最大值。 | Approach |
| Initialize row zero and column zero to zero. | 第 0 列與第 0 欄初始化為 0。 | Approach |
| Final answer is dp[m][n]. | 最終答案是 dp[m][n]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I read m and n as lengths of two strings. | 我先取得兩字串長度 m 與 n。 | Coding |
| I allocate dp table of size m plus one by n plus one with zeros. | 我配置 (m+1)*(n+1) 的零初始化 dp。 | Coding |
| I loop i from one to m. | i 從 1 迭代到 m。 | Coding |
| Inside, I loop j from one to n. | 內層 j 從 1 迭代到 n。 | Coding |
| If text1[i-1] equals text2[j-1], dp[i][j]=1+dp[i-1][j-1]. | 若字元相同，dp[i][j]=1+dp[i-1][j-1]。 | Coding |
| Else dp[i][j]=max(dp[i-1][j], dp[i][j-1]). | 否則 dp[i][j]=max(dp[i-1][j],dp[i][j-1])。 | Coding |
| After filling table, I return dp[m][n]. | 填表完成後回傳 dp[m][n]。 | Coding |
| This directly mirrors the recurrence relation. | 這與遞推關係完全對齊。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run text1 abcde and text2 ace. | 我手跑 text1=abcde、text2=ace。 | Dry-run |
| At a and a, we get a match so dp becomes one. | 在 a 對 a 時匹配，dp 變成 1。 | Dry-run |
| Character b does not match c, so we carry max from neighbors. | b 與 c 不匹配，取鄰居最大值延續。 | Dry-run |
| At c with c, diagonal plus one gives two. | c 對 c 時左上加一得到 2。 | Dry-run |
| At e with e, diagonal plus one gives three. | e 對 e 時左上加一得到 3。 | Dry-run |
| Final bottom-right value is three. | 最右下角值為 3。 | Dry-run |
| That matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: identical strings should return full length. | 案例一：相同字串應回完整長度。 | Edge test |
| Case two: no common characters should return zero. | 案例二：完全無共同字元應回 0。 | Edge test |
| Case three: one string length one. | 案例三：其中一個字串長度為 1。 | Edge test |
| Case four: repeated characters with multiple choices. | 案例四：重複字元且有多條選擇路徑。 | Edge test |
| Case five: one empty string if allowed. | 案例五：若允許，單邊空字串。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m times n). | 空間複雜度是 O(m*n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We fill an m by n DP grid once. | 我們會填滿一個 m*n 的 DP 表。 | Complexity |
| Every cell computation is constant time. | 每個格子的計算都是常數時間。 | Complexity |
| Therefore runtime is O(m*n). | 因此時間是 O(m*n)。 | Complexity |
| Grid storage uses O(m*n) memory, or O(min(m,n)) with optimization. | 表格記憶體是 O(m*n)，可優化到 O(min(m,n))。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define the state clearly first. | 我先把狀態定義清楚。 | If stuck |
| dp[i][j] is LCS length for prefixes. | dp[i][j] 是前綴的 LCS 長度。 | If stuck |
| Base row and column are zeros. | 基底列與欄都為 0。 | If stuck |
| If chars match, I must use diagonal plus one. | 字元匹配時要用左上加一。 | If stuck |
| If chars differ, I choose max of top and left. | 字元不同時取上方與左方較大者。 | If stuck |
| Let me test quickly with abc and abc. | 我快速測試 abc 對 abc。 | If stuck |
| It should produce three. | 結果應為 3。 | If stuck |
| Let me test abc and def as well. | 我再測 abc 對 def。 | If stuck |
| That should produce zero. | 該結果應為 0。 | If stuck |
| Great, recurrence is confirmed. | 很好，遞推式已確認。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved LCS with a standard two-dimensional DP table. | 我用標準二維 DP 表解了 LCS。 | Wrap-up |
| Matching characters use diagonal transition plus one. | 匹配字元用左上加一轉移。 | Wrap-up |
| Non-matching characters use top-left max competition. | 不匹配時用上方與左方最大值。 | Wrap-up |
| Complexity is O(m*n) time and O(m*n) space. | 複雜度是 O(m*n) 時間與 O(m*n) 空間。 | Wrap-up |
| I can also provide space-optimized variant if needed. | 若需要我可再給空間優化版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: LCS length between two strings. | 目標：兩字串的 LCS 長度。 | Cheat sheet |
| Subsequence keeps order, not contiguity. | 子序列保序但不連續。 | Cheat sheet |
| Define dp[i][j] on prefixes. | 用前綴定義 dp[i][j]。 | Cheat sheet |
| Base dp[0][*] and dp[*][0] are zero. | 基底 dp[0][*] 與 dp[*][0] 為 0。 | Cheat sheet |
| Loop i from 1..m. | i 從 1..m。 | Cheat sheet |
| Loop j from 1..n. | j 從 1..n。 | Cheat sheet |
| If chars match: dp[i][j]=1+dp[i-1][j-1]. | 若匹配：dp[i][j]=1+dp[i-1][j-1]。 | Cheat sheet |
| Else: dp[i][j]=max(dp[i-1][j],dp[i][j-1]). | 否則：dp[i][j]=max(dp[i-1][j],dp[i][j-1])。 | Cheat sheet |
| Return dp[m][n]. | 回傳 dp[m][n]。 | Cheat sheet |
| abcde vs ace -> 3. | abcde 對 ace -> 3。 | Cheat sheet |
| abc vs abc -> 3. | abc 對 abc -> 3。 | Cheat sheet |
| abc vs def -> 0. | abc 對 def -> 0。 | Cheat sheet |
| Time O(m*n). | 時間 O(m*n)。 | Cheat sheet |
| Space O(m*n). | 空間 O(m*n)。 | Cheat sheet |
| Can optimize space to O(min(m,n)). | 空間可優化到 O(min(m,n))。 | Cheat sheet |
| Common bug: wrong index offset i-1, j-1. | 常見錯誤：i-1、j-1 索引偏移寫錯。 | Cheat sheet |
| Common bug: confuse subsequence with substring. | 常見錯誤：把 subsequence 當 substring。 | Cheat sheet |
| Keep base cases explicit. | 基底條件要講清楚。 | Cheat sheet |
| Mention recurrence before coding. | 寫碼前先講遞推。 | Cheat sheet |
| Validate with both match and mismatch samples. | 用匹配與不匹配樣例都驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Standard LCS recurrence and table structure preserved.
- No hallucinated constraints: ✅ Uses source semantics (length output, prefix DP).
- Language simplicity: ✅ Clear interview narration for index offsets and transitions.
