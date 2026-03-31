# 08 Distinct Subsequences — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/08_Distinct_Subsequences.md`

> Quick links: [Source Solution](../08_Distinct_Subsequences.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate distinct subsequences. | 我先重述 Distinct Subsequences。 | Restatement |
| We are given source string s and target string t. | 題目給來源字串 s 與目標字串 t。 | Restatement |
| We need number of subsequences of s equal to t. | 要求 s 中等於 t 的子序列個數。 | Restatement |
| Deleting different positions counts as different ways. | 刪除位置不同就算不同方法。 | Restatement |
| We count ways, not just whether one match exists. | 這題是計數，不是單純判斷存在。 | Restatement |
| I will solve it with dynamic programming. | 我會用動態規劃解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should we return zero when t is longer than s? | 若 t 比 s 長，是否直接回 0？ | Clarify |
| Are strings made of English letters only? | 字串是否僅英文字符？ | Clarify |
| Is answer guaranteed to fit in 32-bit integer? | 答案是否保證在 32 位整數內？ | Clarify |
| Do we need count only, not actual subsequences? | 只需計數，不需輸出實際子序列？ | Clarify |
| Is O(m times n) DP expected? | O(m*n) DP 是否為預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursively choose take or skip each character in s. | 暴力遞迴對 s 每字元做取或不取。 | Approach |
| Many repeated states appear for same indices i and j. | 相同 i、j 會反覆出現重複狀態。 | Approach |
| Complexity grows exponentially without memoization. | 不記憶化會呈指數增長。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[i][j] be ways to form first j chars of t using first i chars of s. | 定義 dp[i][j]：用 s 前 i 字形成 t 前 j 字的方法數。 | Approach |
| Base case dp[i][0] equals one for all i. | 基底是所有 dp[i][0]=1。 | Approach |
| If s[i-1] equals t[j-1], we add match and skip counts. | 若字元相等，要加上匹配與跳過兩種計數。 | Approach |
| If not equal, we only inherit skip count dp[i-1][j]. | 若不等，只能繼承跳過計數 dp[i-1][j]。 | Approach |
| Final answer is dp[m][n], with optional 1D compression. | 最終答案是 dp[m][n]，也可做 1D 壓縮。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I read m as s length and n as t length. | 我先取得 s 長度 m 與 t 長度 n。 | Coding |
| I allocate dp table (m plus one) by (n plus one) initialized to zero. | 我建立 (m+1)*(n+1) 的零初始化 dp 表。 | Coding |
| I set dp[i][0] to one for all i. | 我把所有 dp[i][0] 設為 1。 | Coding |
| I loop i from one to m and j from one to n. | i 從 1..m、j 從 1..n 迭代。 | Coding |
| If s[i-1] equals t[j-1], dp[i][j]=dp[i-1][j-1]+dp[i-1][j]. | 若字元相等，dp[i][j]=dp[i-1][j-1]+dp[i-1][j]。 | Coding |
| Else dp[i][j]=dp[i-1][j]. | 否則 dp[i][j]=dp[i-1][j]。 | Coding |
| After filling table, I return dp[m][n]. | 填表完成後回傳 dp[m][n]。 | Coding |
| This exactly reflects match versus skip decisions. | 這正對應匹配與跳過決策。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s rabbbit and t rabbit. | 我手跑 s=rabbbit、t=rabbit。 | Dry-run |
| Base column dp[*][0] is all one. | 基底欄 dp[*][0] 全為 1。 | Dry-run |
| Early characters match directly and accumulate one path. | 前段字元直接匹配並累積一路徑。 | Dry-run |
| At repeated b positions, counts branch and add up. | 在重複 b 位置，計數會分支累加。 | Dry-run |
| Final dp value becomes three. | 最終 dp 值為 3。 | Dry-run |
| So there are three distinct subsequences. | 所以有 3 種不同子序列。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: t empty should return one. | 案例一：t 為空應回 1。 | Edge test |
| Case two: s empty and t non-empty should return zero. | 案例二：s 空且 t 非空應回 0。 | Edge test |
| Case three: t longer than s should return zero. | 案例三：t 長於 s 應回 0。 | Edge test |
| Case four: repeated chars causing large combinational counts. | 案例四：重複字元導致組合數較大。 | Edge test |
| Case five: no shared characters at all. | 案例五：完全無共同字元。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m times n), or O(n) optimized. | 空間複雜度是 O(m*n)，優化可到 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We fill each state in an m by n table once. | m*n 表格中的每個狀態只填一次。 | Complexity |
| Each state update uses constant-time arithmetic. | 每個狀態更新只需常數運算。 | Complexity |
| Hence total runtime is O(m*n). | 因此總時間是 O(m*n)。 | Complexity |
| Full table uses O(m*n) memory, with optional O(n) 1D variant. | 全表空間 O(m*n)，可改 1D 到 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define state in counting form. | 我先用計數形式定義狀態。 | If stuck |
| dp[i][j] is number of ways, not boolean. | dp[i][j] 是方法數，不是布林。 | If stuck |
| Base dp[i][0] equals one is crucial. | 基底 dp[i][0]=1 非常關鍵。 | If stuck |
| If chars match, combine match and skip branches. | 字元匹配時合併匹配與跳過分支。 | If stuck |
| If chars differ, only skip branch survives. | 字元不匹配時只剩跳過分支。 | If stuck |
| Let me check rabbbit to rabbit quickly. | 我快速檢查 rabbbit 到 rabbit。 | If stuck |
| Branching at b should create count three. | 在 b 的分支應產生計數 3。 | If stuck |
| Empty target should always return one. | 目標空字串永遠應回 1。 | If stuck |
| That validates base and transition logic. | 這可驗證基底與轉移邏輯。 | If stuck |
| Great, now I can finish confidently. | 很好，我可安心完成。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved distinct subsequences with counting DP. | 我用計數 DP 解了 Distinct Subsequences。 | Wrap-up |
| State tracks ways to form target prefixes from source prefixes. | 狀態追蹤用來源前綴形成目標前綴的方法數。 | Wrap-up |
| Match adds two branches, mismatch keeps skip branch. | 匹配加兩分支，不匹配保留跳過分支。 | Wrap-up |
| Complexity is O(m*n) time and O(m*n) space. | 複雜度是 O(m*n) 時間、O(m*n) 空間。 | Wrap-up |
| Space can be optimized to O(n) if needed. | 若需要可把空間優化到 O(n)。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: count subsequences of s equal to t. | 目標：計算 s 中等於 t 的子序列數。 | Cheat sheet |
| This is counting, not existence check. | 這是計數，不是存在判斷。 | Cheat sheet |
| Define dp[i][j] on prefixes. | 在前綴上定義 dp[i][j]。 | Cheat sheet |
| dp[i][j]=ways using s[0..i-1] for t[0..j-1]. | dp[i][j]=用 s 前 i 字形成 t 前 j 字的方法數。 | Cheat sheet |
| Initialize dp[i][0]=1. | 初始化 dp[i][0]=1。 | Cheat sheet |
| Initialize dp[0][j>0]=0. | 初始化 dp[0][j>0]=0。 | Cheat sheet |
| Loop i from 1..m. | i 從 1..m。 | Cheat sheet |
| Loop j from 1..n. | j 從 1..n。 | Cheat sheet |
| If char match: dp[i][j]=dp[i-1][j-1]+dp[i-1][j]. | 若字元匹配：dp[i][j]=dp[i-1][j-1]+dp[i-1][j]。 | Cheat sheet |
| Else: dp[i][j]=dp[i-1][j]. | 否則：dp[i][j]=dp[i-1][j]。 | Cheat sheet |
| Return dp[m][n]. | 回傳 dp[m][n]。 | Cheat sheet |
| rabbbit -> rabbit gives 3. | rabbbit -> rabbit 會得到 3。 | Cheat sheet |
| Empty target gives 1. | 目標空字串給 1。 | Cheat sheet |
| t longer than s gives 0. | t 比 s 長給 0。 | Cheat sheet |
| Time O(m*n). | 時間 O(m*n)。 | Cheat sheet |
| Space O(m*n). | 空間 O(m*n)。 | Cheat sheet |
| Optional 1D compression to O(n). | 可選 1D 壓縮到 O(n)。 | Cheat sheet |
| Common bug: forgetting dp[i][0]=1. | 常見錯誤：忘記 dp[i][0]=1。 | Cheat sheet |
| Common bug: treating dp as bool. | 常見錯誤：把 dp 當布林。 | Cheat sheet |
| Explain match/skip decision tree clearly. | 清楚說明匹配/跳過決策樹。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Counting recurrence and base-case semantics preserved.
- No hallucinated constraints: ✅ Distinct-subsequence counting model maintained.
- Language simplicity: ✅ Interview wording focuses on counting intuition.
