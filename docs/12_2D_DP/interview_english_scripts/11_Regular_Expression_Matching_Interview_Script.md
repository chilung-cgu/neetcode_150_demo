# 11 Regular Expression Matching — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/11_Regular_Expression_Matching.md`

> Quick links: [Source Solution](../11_Regular_Expression_Matching.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate regular expression matching. | 我先重述正規表示式匹配題。 | Restatement |
| We are given string s and pattern p. | 題目給字串 s 與模式 p。 | Restatement |
| Pattern supports dot and star only. | 模式只支援 `.` 與 `*`。 | Restatement |
| Dot matches any single character. | `.` 可匹配任意單一字元。 | Restatement |
| Star means zero or more of the preceding element. | `*` 代表前一元素重複零次或多次。 | Restatement |
| I will solve it using two-dimensional DP. | 我會用二維 DP 解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should the whole string match the whole pattern? | 是否要求整個字串完整匹配整個模式？ | Clarify |
| Can we assume pattern is valid, for example no leading star? | 可否假設模式合法，例如不會以 `*` 開頭？ | Clarify |
| Are there only dot and star special operators? | 特殊符號是否只有 `.` 與 `*`？ | Clarify |
| Do we return boolean only? | 是否只回傳布林值？ | Clarify |
| Is O(m times n) DP acceptable? | O(m*n) DP 是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursion branches heavily when star appears. | 暴力遞迴遇到 `*` 會大量分支。 | Approach |
| Same suffix pairs are revisited repeatedly. | 相同後綴配對會被反覆訪問。 | Approach |
| Complexity grows exponentially in worst cases. | 最壞情況複雜度呈指數成長。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[i][j] mean s prefix length i matches p prefix length j. | 定義 dp[i][j]：s 前 i 是否匹配 p 前 j。 | Approach |
| Base dp[0][0] is true. | 基底 dp[0][0]=true。 | Approach |
| If p[j-1] is normal char or dot, check char match and diagonal state. | 若 p[j-1] 是一般字元或 `.`, 看字元匹配與左上狀態。 | Approach |
| If p[j-1] is star, combine zero-occurrence and multi-occurrence transitions. | 若 p[j-1] 是 `*`, 合併零次與多次轉移。 | Approach |
| Final answer is dp[m][n]. | 最終答案是 dp[m][n]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I allocate dp table of size m plus one by n plus one initialized false. | 建立 (m+1)*(n+1) 的 false 初始化 dp 表。 | Coding |
| I set dp[0][0] to true. | 設 dp[0][0]=true。 | Coding |
| I initialize first row for patterns like a star b star matching empty string. | 初始化首列，處理像 a* b* 可匹配空字串。 | Coding |
| I iterate i from one to m and j from one to n. | i 從 1..m，j 從 1..n。 | Coding |
| If p[j-1] is not star, match char or dot then use dp[i-1][j-1]. | 若 p[j-1] 非 `*`, 字元或 `.` 匹配時看 dp[i-1][j-1]。 | Coding |
| If p[j-1] is star, zero case is dp[i][j-2]. | 若 p[j-1] 是 `*`, 零次情況看 dp[i][j-2]。 | Coding |
| For star one-plus case, s[i-1] must match p[j-2], then use dp[i-1][j]. | `*` 一次以上需 s[i-1] 匹配 p[j-2]，再看 dp[i-1][j]。 | Coding |
| I combine those cases and return dp[m][n]. | 合併兩情況後回傳 dp[m][n]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s aa and p a star. | 我手跑 s=aa、p=a*。 | Dry-run |
| dp[0][0] is true and dp[0][2] becomes true by star zero-case initialization. | dp[0][0] 為真，且首列由 `*` 零次規則讓 dp[0][2] 成真。 | Dry-run |
| At i one and j two, star one-plus case matches first a. | i=1,j=2 時 `*` 多次規則可匹配第一個 a。 | Dry-run |
| At i two and j two, same rule extends match to second a. | i=2,j=2 時同規則可延伸匹配第二個 a。 | Dry-run |
| Final dp[2][2] is true. | 最終 dp[2][2] 為 true。 | Dry-run |
| So pattern matches the string. | 所以模式可匹配字串。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty string against patterns like a star b star. | 案例一：空字串對 a*b* 類模式。 | Edge test |
| Case two: single char with dot pattern. | 案例二：單字元對 `.` 模式。 | Edge test |
| Case three: star needs to consume multiple characters. | 案例三：`*` 需要匹配多個字元。 | Edge test |
| Case four: star used as zero occurrence. | 案例四：`*` 走零次匹配路徑。 | Edge test |
| Case five: near-match but full-string mismatch at end. | 案例五：前面近似但尾端整體不匹配。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m times n). | 空間複雜度是 O(m*n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We fill each state in an m by n DP table once. | m*n 的 DP 狀態各填一次。 | Complexity |
| Each state computes constant number of checks. | 每個狀態只做常數次檢查。 | Complexity |
| Therefore runtime is O(m*n). | 因此時間是 O(m*n)。 | Complexity |
| Boolean table storage costs O(m*n) memory. | 布林表格空間成本是 O(m*n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate star and non-star cases first. | 我先把 `*` 與非 `*` 情況分開。 | If stuck |
| State dp[i][j] means prefix match status. | 狀態 dp[i][j] 表示前綴匹配狀態。 | If stuck |
| Non-star case uses diagonal when chars match. | 非 `*` 情況在字元匹配時看左上。 | If stuck |
| Star zero-case drops previous element and star. | `*` 零次情況是略過前一元素與 `*`。 | If stuck |
| Star one-plus needs char match with p[j-2]. | `*` 一次以上需與 p[j-2] 字元匹配。 | If stuck |
| Then we stay in same pattern column using dp[i-1][j]. | 接著沿同一模式欄位看 dp[i-1][j]。 | If stuck |
| I should initialize dp[0][j] for star pairs. | 我應初始化 dp[0][j] 的星號配對。 | If stuck |
| Let me verify quickly with aa and a star. | 我快速驗證 aa 對 a*。 | If stuck |
| It ends true, confirming star transitions. | 結果為 true，證明星號轉移正確。 | If stuck |
| Great, I can finalize implementation. | 很好，我可完成實作。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved regex matching using 2D DP. | 我用二維 DP 解了正規表示式匹配。 | Wrap-up |
| The core is handling star zero-case and one-plus case correctly. | 核心是正確處理 `*` 的零次與多次情況。 | Wrap-up |
| Dot is treated as single-character wildcard. | `.` 視為單字元萬用符。 | Wrap-up |
| Complexity is O(m*n) time and O(m*n) space. | 複雜度是 O(m*n) 時間、O(m*n) 空間。 | Wrap-up |
| This is the standard robust interview solution. | 這是面試常見且穩健的標準解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: full-string match with pattern containing dot and star. | 目標：以含 `.`、`*` 的模式完整匹配字串。 | Cheat sheet |
| Define dp[i][j] on prefixes. | 在前綴上定義 dp[i][j]。 | Cheat sheet |
| dp[0][0]=true. | dp[0][0]=true。 | Cheat sheet |
| Init dp[0][j] for star-skippable patterns. | 初始化 dp[0][j] 處理可被 `*` 略過的模式。 | Cheat sheet |
| If p[j-1] not star and chars match, use diag. | 若 p[j-1] 非 `*` 且字元匹配，取左上。 | Cheat sheet |
| Char match means same char or dot. | 字元匹配指相同字元或 `.`。 | Cheat sheet |
| If p[j-1] is star, zero-case uses dp[i][j-2]. | 若 p[j-1] 是 `*`，零次看 dp[i][j-2]。 | Cheat sheet |
| Star one-plus requires s[i-1] match p[j-2]. | `*` 多次需 s[i-1] 匹配 p[j-2]。 | Cheat sheet |
| Then one-plus uses dp[i-1][j]. | 然後多次情況看 dp[i-1][j]。 | Cheat sheet |
| Combine star cases with OR. | `*` 兩情況以 OR 合併。 | Cheat sheet |
| Return dp[m][n]. | 回傳 dp[m][n]。 | Cheat sheet |
| aa vs a* -> true. | aa 對 a* -> true。 | Cheat sheet |
| ab vs .* -> true. | ab 對 .* -> true。 | Cheat sheet |
| aab vs c*a*b -> true. | aab 對 c*a*b -> true。 | Cheat sheet |
| Time O(m*n). | 時間 O(m*n)。 | Cheat sheet |
| Space O(m*n). | 空間 O(m*n)。 | Cheat sheet |
| Common bug: forgetting dp[0][j] initialization. | 常見錯誤：忘記初始化 dp[0][j]。 | Cheat sheet |
| Common bug: using j-1 instead of j-2 in star zero-case. | 常見錯誤：`*` 零次誤用 j-1 非 j-2。 | Cheat sheet |
| Keep star logic separated for clarity. | 把 `*` 邏輯拆開講會更清楚。 | Cheat sheet |
| Validate both zero and multi occurrence behavior. | 記得同時驗證零次與多次行為。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Dot/star DP transitions and empty-prefix initialization preserved.
- No hallucinated constraints: ✅ Full-match semantics and operator scope kept correct.
- Language simplicity: ✅ Interview-focused wording for tricky star handling.
