# 06 Interleaving String — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/06_Interleaving_String.md`

> Quick links: [Source Solution](../06_Interleaving_String.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate interleaving string. | 我先重述 Interleaving String。 | Restatement |
| We are given s1, s2, and s3. | 題目給 s1、s2、s3 三字串。 | Restatement |
| We need to decide whether s3 can be formed by interleaving s1 and s2. | 要判斷 s3 是否可由 s1 與 s2 交錯形成。 | Restatement |
| Relative order inside s1 and inside s2 must be preserved. | s1 與 s2 各自內部順序都必須保留。 | Restatement |
| We must use all characters from both strings exactly once. | 兩字串字元都要完整使用一次。 | Restatement |
| I will solve this with two-dimensional DP. | 我會用二維 DP 解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do we return boolean only? | 是否只回傳布林值？ | Clarify |
| Can s1 or s2 be empty? | s1 或 s2 可以是空字串嗎？ | Clarify |
| Is length mismatch immediate false? | 長度不符是否可直接回 false？ | Clarify |
| Are characters case-sensitive in matching? | 比對是否區分大小寫？ | Clarify |
| Is O(m times n) DP expected? | O(m*n) DP 是否為預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursively chooses next char from s1 or s2. | 暴力遞迴每步選 s1 或 s2 下一字元。 | Approach |
| Overlapping states appear for same i and j positions. | 相同 i、j 位置會重複出現狀態。 | Approach |
| Complexity becomes exponential without memoization. | 不記憶化會是指數級時間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[i][j] mean first i of s1 and first j of s2 can form first i+j of s3. | 定義 dp[i][j]：s1 前 i 與 s2 前 j 可形成 s3 前 i+j。 | Approach |
| Base case dp[0][0] is true. | 基底 dp[0][0]=true。 | Approach |
| If s1[i-1] matches s3[i+j-1], we can come from dp[i-1][j]. | 若 s1[i-1] 匹配，可由 dp[i-1][j] 轉移。 | Approach |
| If s2[j-1] matches s3[i+j-1], we can come from dp[i][j-1]. | 若 s2[j-1] 匹配，可由 dp[i][j-1] 轉移。 | Approach |
| Final answer is dp[m][n]. | 最終答案是 dp[m][n]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I check m plus n equals length of s3, otherwise false. | 先檢查 m+n 是否等於 |s3|，否則 false。 | Coding |
| I allocate boolean dp table sized m plus one by n plus one. | 建立大小 (m+1)*(n+1) 的布林 dp 表。 | Coding |
| I set dp[0][0] to true. | 設 dp[0][0]=true。 | Coding |
| I initialize first column using only s1 matches against s3. | 用 s1 與 s3 比對初始化第一欄。 | Coding |
| I initialize first row using only s2 matches against s3. | 用 s2 與 s3 比對初始化第一列。 | Coding |
| For each i and j, I test s1 transition and s2 transition. | 對每個 i,j 同時檢查 s1 與 s2 兩種轉移。 | Coding |
| I OR the valid transitions into dp[i][j]. | 把合法轉移用 OR 合併到 dp[i][j]。 | Coding |
| I return dp[m][n] at the end. | 最後回傳 dp[m][n]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s1 aabcc, s2 dbbca, s3 aadbbcbcac. | 我手跑 s1=aabcc、s2=dbbca、s3=aadbbcbcac。 | Dry-run |
| Length check passes because five plus five equals ten. | 長度檢查通過，5+5=10。 | Dry-run |
| dp[0][0] starts true and first row/column are filled by direct matches. | dp[0][0] 起始為 true，首列首欄由直接匹配填入。 | Dry-run |
| In middle cells, some states are reachable from top and some from left. | 中間格有些從上可達、有些從左可達。 | Dry-run |
| Eventually dp[5][5] becomes true. | 最後 dp[5][5] 變 true。 | Dry-run |
| So s3 is a valid interleaving. | 因此 s3 是合法交錯字串。 | Dry-run |
| This matches expected output true. | 這與預期 true 一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: both s1 and s2 empty, s3 empty. | 案例一：s1、s2、s3 全空。 | Edge test |
| Case two: one source empty and other equals s3. | 案例二：其中一個空，另一個等於 s3。 | Edge test |
| Case three: length mismatch should be immediate false. | 案例三：長度不符應立即 false。 | Edge test |
| Case four: repeated characters causing ambiguous paths. | 案例四：重複字元造成多路徑歧義。 | Edge test |
| Case five: near-match but impossible ordering. | 案例五：字元接近但順序不可能。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m times n). | 空間複雜度是 O(m*n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We fill each state in an m by n DP table once. | m*n 的每個狀態都只填一次。 | Complexity |
| Each state checks up to two constant-time transitions. | 每狀態最多檢查兩個常數時間轉移。 | Complexity |
| Therefore runtime is O(m*n). | 因此時間是 O(m*n)。 | Complexity |
| DP table stores O(m*n) booleans, with optional 1D optimization. | 表格存 O(m*n) 布林，可進一步做 1D 優化。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me check length condition first. | 我先檢查長度條件。 | If stuck |
| If lengths do not add up, answer is false directly. | 長度加總不符就直接 false。 | If stuck |
| Define state as prefix interleaving validity. | 狀態定義為前綴交錯可行性。 | If stuck |
| dp[i][j] maps to s3 index i plus j minus one. | dp[i][j] 對應 s3 索引 i+j-1。 | If stuck |
| Transition from top means taking from s1. | 從上方轉移代表取 s1 字元。 | If stuck |
| Transition from left means taking from s2. | 從左方轉移代表取 s2 字元。 | If stuck |
| Use OR because either source can make state true. | 用 OR 因為任一來源成立即可。 | If stuck |
| Let me verify with one true sample quickly. | 我快速驗證一個 true 範例。 | If stuck |
| Then test a known false ordering case. | 再測一個順序錯誤的 false 案例。 | If stuck |
| Great, transitions are now clear. | 很好，轉移邏輯清楚了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved interleaving string with two-dimensional DP. | 我用二維 DP 解了 Interleaving String。 | Wrap-up |
| State tracks whether two prefixes can form a target prefix. | 狀態追蹤兩前綴能否形成目標前綴。 | Wrap-up |
| We combine top and left transitions when characters match. | 字元匹配時合併上與左兩種轉移。 | Wrap-up |
| Complexity is O(m*n) time and O(m*n) space. | 複雜度是 O(m*n) 時間與 O(m*n) 空間。 | Wrap-up |
| I can provide 1D optimization if needed. | 若需要我可提供 1D 空間優化。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: check if s3 interleaves s1 and s2. | 目標：判斷 s3 是否由 s1、s2 交錯。 | Cheat sheet |
| Preserve internal order of each source string. | 各來源字串內部順序要保留。 | Cheat sheet |
| Length check first: m+n must equal len(s3). | 先做長度檢查：m+n 必須等於 |s3|。 | Cheat sheet |
| Define dp[i][j] on prefixes. | 在前綴上定義 dp[i][j]。 | Cheat sheet |
| dp[0][0]=true. | dp[0][0]=true。 | Cheat sheet |
| Init first column with s1-only matches. | 用僅 s1 匹配初始化第一欄。 | Cheat sheet |
| Init first row with s2-only matches. | 用僅 s2 匹配初始化第一列。 | Cheat sheet |
| For each cell, check s1 transition from top. | 每格先檢查從上方的 s1 轉移。 | Cheat sheet |
| Check s2 transition from left. | 再檢查從左方的 s2 轉移。 | Cheat sheet |
| Combine with OR. | 用 OR 合併。 | Cheat sheet |
| Return dp[m][n]. | 回傳 dp[m][n]。 | Cheat sheet |
| True sample: aadbbcbcac. | true 範例：aadbbcbcac。 | Cheat sheet |
| False sample: aadbbbaccc. | false 範例：aadbbbaccc。 | Cheat sheet |
| Time O(m*n). | 時間 O(m*n)。 | Cheat sheet |
| Space O(m*n). | 空間 O(m*n)。 | Cheat sheet |
| Common bug: wrong s3 index i+j-1. | 常見錯誤：s3 索引 i+j-1 寫錯。 | Cheat sheet |
| Common bug: missing base row/column init. | 常見錯誤：漏掉首列首欄初始化。 | Cheat sheet |
| Explain transitions with source-of-character view. | 用「字元來源」視角說明轉移。 | Cheat sheet |
| Mention optional O(n) space optimization. | 可補充 O(n) 空間優化。 | Cheat sheet |
| Validate both true and false cases. | 同時驗證 true 與 false 案例。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Prefix DP definition and dual transitions preserved.
- No hallucinated constraints: ✅ Length precheck and order-preserving semantics maintained.
- Language simplicity: ✅ Straight interview lines for state/index mapping.
