# 07 Decode Ways — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/07_Decode_Ways.md`

> Quick links: [Source Solution](../07_Decode_Ways.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the decode ways problem. | 我先重述 Decode Ways。 | Restatement |
| Digits map to letters one through twenty-six. | 數字 1 到 26 映射到字母。 | Restatement |
| We need number of valid decodings for string s. | 要求字串 s 的合法解碼總數。 | Restatement |
| Zero cannot stand alone as a valid code. | 0 不能單獨作為合法代碼。 | Restatement |
| Two-digit code must be between ten and twenty-six. | 兩位數代碼需介於 10 到 26。 | Restatement |
| I will use rolling DP with one-digit and two-digit transitions. | 我會用滾動 DP 處理一位與兩位轉移。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If string starts with zero, answer is zero, correct? | 若字串以 0 開頭是否直接為 0？ | Clarify |
| Is six invalid but ten valid as two-digit decode? | 06 無效但 10 有效，對嗎？ | Clarify |
| Do we return count only, not decoded strings? | 是否只回數量，不回字串內容？ | Clarify |
| Should repeated use of same mapping be naturally allowed? | 同樣映射可重複使用是否自然允許？ | Clarify |
| Is O(n) time expected for this constraint? | 此限制下是否期待 O(n) 時間？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursively branches by taking one or two digits. | 暴力遞迴以取 1 位或 2 位分支。 | Approach |
| Many overlapping suffix subproblems appear. | 會出現大量重疊後綴子問題。 | Approach |
| Time becomes exponential without memoization. | 不記憶化時時間會是指數級。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[i] be number of ways to decode prefix length i. | 令 dp[i] 為長度 i 前綴的解碼數。 | Approach |
| If one-digit at i-1 is valid one to nine, add dp[i-1]. | 若 i-1 的一位數有效 1~9，就加 dp[i-1]。 | Approach |
| If two-digit from i-2 to i-1 is ten to twenty-six, add dp[i-2]. | 若 i-2 到 i-1 兩位數在 10~26，就加 dp[i-2]。 | Approach |
| Base is dp[0] equals one and initial zero checks. | 基底是 dp[0]=1 並先處理前導 0。 | Approach |
| Rolling two states gives O(1) extra memory. | 只需滾動兩狀態即可 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I return zero immediately if s is empty or starts with zero. | s 空或首字 0 時我立刻回 0。 | Coding |
| I initialize prev2 as dp zero equals one. | 我初始化 prev2 代表 dp[0]=1。 | Coding |
| I initialize prev1 as dp one equals one after valid first char. | 首字有效時初始化 prev1=dp[1]=1。 | Coding |
| For i from two to n, I compute current as zero first. | i 從 2 到 n，先令 current=0。 | Coding |
| If one-digit value is one to nine, current adds prev1. | 若一位值在 1~9，current 加 prev1。 | Coding |
| If two-digit value is ten to twenty-six, current adds prev2. | 若兩位值在 10~26，current 加 prev2。 | Coding |
| Then I shift prev2 to prev1 and prev1 to current. | 然後更新 prev2=prev1、prev1=current。 | Coding |
| Final answer is prev1. | 最終答案是 prev1。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s equals two-two-six. | 我手跑 s="226"。 | Dry-run |
| dp zero is one and dp one is one. | dp[0]=1，dp[1]=1。 | Dry-run |
| At i two, one-digit two valid and two-digit twenty-two valid. | i=2 時一位 2 有效，兩位 22 也有效。 | Dry-run |
| So dp two becomes two. | 所以 dp[2]=2。 | Dry-run |
| At i three, one-digit six valid and two-digit twenty-six valid. | i=3 時一位 6 有效，兩位 26 也有效。 | Dry-run |
| dp three becomes three. | dp[3] 變成 3。 | Dry-run |
| Final answer is three, matching expected output. | 最終答案 3，與預期一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: leading zero like zero-six should return zero. | 案例一：前導 0 如 06 應回 0。 | Edge test |
| Case two: ten and twenty are valid single decode each. | 案例二：10 與 20 都是有效單一解碼。 | Edge test |
| Case three: thirty is invalid as two-digit decode. | 案例三：30 作為兩位碼無效。 | Edge test |
| Case four: string one-one-one-one has Fibonacci-like growth. | 案例四：1111 會呈 Fibonacci 型成長。 | Edge test |
| Case five: single digit non-zero should return one. | 案例五：單一非零數字應回 1。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We process each character position once in a single loop. | 我們在單一迴圈中逐位處理一次。 | Complexity |
| Each step does constant-time validity checks and additions. | 每步僅做常數次合法性檢查與加總。 | Complexity |
| Therefore runtime is O(n). | 因此時間為 O(n)。 | Complexity |
| Only rolling states prev1 prev2 current are stored, so O(1) space. | 僅存 prev1/prev2/current，故空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me split transitions into one-digit and two-digit cases. | 我先把轉移拆成一位與兩位情況。 | If stuck |
| One-digit is valid only from one to nine. | 一位有效值只在 1 到 9。 | If stuck |
| Two-digit is valid only from ten to twenty-six. | 兩位有效值只在 10 到 26。 | If stuck |
| Zero is never valid alone. | 0 永遠不能單獨解碼。 | If stuck |
| Current ways is sum of valid incoming transitions. | current 是所有合法轉移的總和。 | If stuck |
| I should initialize dp zero as one for combinational base. | 我應把 dp[0] 設為 1 作為組合基底。 | If stuck |
| Let me test quickly with twelve. | 我快速測試 "12"。 | If stuck |
| It gives two: AB and L. | 會得到 2：AB 與 L。 | If stuck |
| Then test zero-six gives zero. | 再測 "06" 得 0。 | If stuck |
| Great, rules and recurrence are now consistent. | 很好，規則與遞推已一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved decode ways with rolling dynamic programming. | 我用滾動動態規劃解出 Decode Ways。 | Wrap-up |
| Each position combines valid one-digit and two-digit contributions. | 每個位置累加合法一位與兩位貢獻。 | Wrap-up |
| Leading and standalone zeros are handled explicitly. | 前導與單獨 0 都有明確處理。 | Wrap-up |
| Runtime is linear O(n). | 執行時間是線性 O(n)。 | Wrap-up |
| Extra memory is constant O(1). | 額外記憶體是常數 O(1)。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: counting decodings. | 題型：解碼方式計數。 | Cheat sheet |
| Mapping range is 1..26. | 映射範圍是 1..26。 | Cheat sheet |
| Zero cannot decode alone. | 0 不能單獨解碼。 | Cheat sheet |
| dp[i] = ways for prefix length i. | dp[i] 是長度 i 前綴方式數。 | Cheat sheet |
| Base dp[0] = 1. | 基底 dp[0]=1。 | Cheat sheet |
| Guard: if s[0]=='0' return 0. | 若首字 0 直接回 0。 | Cheat sheet |
| For each i, start current at 0. | 每個 i 先令 current=0。 | Cheat sheet |
| Check one-digit validity 1..9. | 檢查一位合法性 1..9。 | Cheat sheet |
| If valid, current += dp[i-1]. | 合法則 current+=dp[i-1]。 | Cheat sheet |
| Check two-digit validity 10..26. | 檢查兩位合法性 10..26。 | Cheat sheet |
| If valid, current += dp[i-2]. | 合法則 current+=dp[i-2]。 | Cheat sheet |
| Roll prev2 prev1 after each step. | 每步後滾動 prev2 與 prev1。 | Cheat sheet |
| Final answer is dp[n]. | 最終答案是 dp[n]。 | Cheat sheet |
| Rolling answer is prev1. | 滾動版本答案是 prev1。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Example 226 -> 3. | 例 226 -> 3。 | Cheat sheet |
| Example 12 -> 2. | 例 12 -> 2。 | Cheat sheet |
| Example 06 -> 0. | 例 06 -> 0。 | Cheat sheet |
| Common bug: accepting 06 as valid. | 常見錯誤：把 06 誤判有效。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ One-digit/two-digit DP transition preserved.
- No hallucinated constraints: ✅ Zero-handling and range rules are exact.
- Language simplicity: ✅ Interview-safe concise lines with clear recurrence.
