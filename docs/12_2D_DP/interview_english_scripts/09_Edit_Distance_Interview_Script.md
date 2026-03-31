# 09 Edit Distance — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/09_Edit_Distance.md`

> Quick links: [Source Solution](../09_Edit_Distance.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate edit distance. | 我先重述 Edit Distance。 | Restatement |
| We are given two strings word1 and word2. | 題目給兩個字串 word1 與 word2。 | Restatement |
| We need minimum operations to convert word1 into word2. | 要求把 word1 轉成 word2 的最少操作數。 | Restatement |
| Allowed operations are insert delete and replace. | 允許操作是插入、刪除、替換。 | Restatement |
| We return only the minimum count. | 只需回傳最小步數。 | Restatement |
| I will solve it with two-dimensional DP. | 我會用二維 DP 解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can either string be empty? | 其中任一字串可以為空嗎？ | Clarify |
| Are operations all unit cost one? | 三種操作成本都固定為 1 嗎？ | Clarify |
| Is matching case-sensitive? | 比對是否區分大小寫？ | Clarify |
| Do we need operation sequence or only distance value? | 需要操作序列還是只要距離值？ | Clarify |
| Is O(m times n) expected under constraints? | 在限制下 O(m*n) 是否預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force recursively tries insert delete and replace choices. | 暴力遞迴嘗試插入、刪除、替換分支。 | Approach |
| Overlapping subproblems appear for same suffix pairs. | 相同後綴對會重複出現子問題。 | Approach |
| Complexity is exponential without memoization. | 不記憶化時複雜度是指數級。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let dp[i][j] be minimum edits to convert first i chars of word1 to first j chars of word2. | 定義 dp[i][j]：word1 前 i 轉 word2 前 j 的最少編輯數。 | Approach |
| Base dp[i][0] equals i and dp[0][j] equals j. | 基底 dp[i][0]=i、dp[0][j]=j。 | Approach |
| If chars match, dp[i][j] equals dp[i-1][j-1]. | 若字元相同，dp[i][j]=dp[i-1][j-1]。 | Approach |
| Else take one plus min of delete insert replace transitions. | 否則取 1+min(刪除、插入、替換)。 | Approach |
| Final answer is dp[m][n]. | 最終答案為 dp[m][n]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I read lengths m and n for the two words. | 我先取得兩字長 m 與 n。 | Coding |
| I allocate dp table with size m plus one by n plus one. | 建立大小 (m+1)*(n+1) 的 dp 表。 | Coding |
| I initialize first column dp[i][0]=i for deletions. | 第一欄 dp[i][0]=i 代表連續刪除。 | Coding |
| I initialize first row dp[0][j]=j for insertions. | 第一列 dp[0][j]=j 代表連續插入。 | Coding |
| I iterate i from one to m and j from one to n. | i 從 1..m，j 從 1..n。 | Coding |
| If current chars equal, I copy diagonal value. | 若當前字元相等，直接取左上值。 | Coding |
| Else I set dp[i][j] to one plus min of top left and diagonal. | 否則設為 1 加上方、左方、左上三者最小。 | Coding |
| I return dp[m][n] as final edit distance. | 我回傳 dp[m][n] 作最終距離。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run word1 horse and word2 ros. | 我手跑 word1=horse、word2=ros。 | Dry-run |
| Base row and column are filled by index values. | 基底列與欄用索引值填入。 | Dry-run |
| h versus r differs, so first non-base cell is one by replace. | h 對 r 不同，第一格可由替換得到 1。 | Dry-run |
| As table fills, matching o with o reuses diagonal cost. | 表格推進時，o 對 o 會沿用左上成本。 | Dry-run |
| Final bottom-right value becomes three. | 最右下角最終值為 3。 | Dry-run |
| So minimum operations are three. | 所以最少操作是 3。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: both strings empty should return zero. | 案例一：雙空字串應回 0。 | Edge test |
| Case two: one empty string should return other length. | 案例二：單邊空字串應回另一邊長度。 | Edge test |
| Case three: identical strings should return zero. | 案例三：相同字串應回 0。 | Edge test |
| Case four: completely different same-length strings. | 案例四：同長但完全不同字串。 | Edge test |
| Case five: prefix-suffix overlap tricky case. | 案例五：前綴後綴重疊的棘手案例。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m times n). | 空間複雜度是 O(m*n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We fill every state in an m by n matrix once. | 我們把 m*n 狀態各填一次。 | Complexity |
| Each state checks at most three neighboring states. | 每個狀態最多看三個鄰接狀態。 | Complexity |
| Therefore runtime is O(m*n). | 因此時間為 O(m*n)。 | Complexity |
| Table storage is O(m*n), with optional O(min(m,n)) compression. | 表格空間 O(m*n)，可壓縮到 O(min(m,n))。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me state the DP meaning explicitly. | 我先明確說出 DP 意義。 | If stuck |
| dp[i][j] is min edits for two prefixes. | dp[i][j] 是兩前綴最小編輯數。 | If stuck |
| Base when one string empty is straightforward. | 單邊空字串的基底很直接。 | If stuck |
| Match case copies diagonal value. | 字元匹配時沿用左上值。 | If stuck |
| Mismatch case takes min of three operations plus one. | 不匹配時三操作最小值再加一。 | If stuck |
| Top means delete from word1. | 上方代表從 word1 刪除。 | If stuck |
| Left means insert into word1. | 左方代表對 word1 插入。 | If stuck |
| Diagonal means replace character. | 左上代表替換字元。 | If stuck |
| Let me verify quickly with horse to ros. | 我快速驗證 horse 到 ros。 | If stuck |
| Great, answer three confirms recurrence. | 很好，答案 3 可確認遞推。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved edit distance with classic 2D DP. | 我用經典二維 DP 解了 Edit Distance。 | Wrap-up |
| State tracks minimum edits between prefixes. | 狀態追蹤前綴間最小編輯數。 | Wrap-up |
| Match uses diagonal, mismatch uses three-operation minimum. | 匹配看左上，不匹配取三操作最小。 | Wrap-up |
| Complexity is O(m*n) time and O(m*n) space. | 複雜度是 O(m*n) 時間與 O(m*n) 空間。 | Wrap-up |
| This is the standard interview approach. | 這是面試常見標準解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: min edits to convert word1 to word2. | 目標：把 word1 轉成 word2 的最少編輯。 | Cheat sheet |
| Operations: insert delete replace. | 操作：插入、刪除、替換。 | Cheat sheet |
| Define dp[i][j] on prefixes. | 在前綴上定義 dp[i][j]。 | Cheat sheet |
| dp[i][0]=i, dp[0][j]=j. | dp[i][0]=i，dp[0][j]=j。 | Cheat sheet |
| Loop i from 1..m. | i 從 1..m。 | Cheat sheet |
| Loop j from 1..n. | j 從 1..n。 | Cheat sheet |
| If chars match: dp[i][j]=dp[i-1][j-1]. | 若字元匹配：dp[i][j]=dp[i-1][j-1]。 | Cheat sheet |
| Else: 1+min(top,left,diag). | 否則：1+min(上、左、左上)。 | Cheat sheet |
| top = delete. | 上方=刪除。 | Cheat sheet |
| left = insert. | 左方=插入。 | Cheat sheet |
| diag = replace. | 左上=替換。 | Cheat sheet |
| Return dp[m][n]. | 回傳 dp[m][n]。 | Cheat sheet |
| horse -> ros = 3. | horse -> ros = 3。 | Cheat sheet |
| Empty to abc = 3. | 空字串到 abc = 3。 | Cheat sheet |
| Same strings = 0. | 相同字串 = 0。 | Cheat sheet |
| Time O(m*n). | 時間 O(m*n)。 | Cheat sheet |
| Space O(m*n). | 空間 O(m*n)。 | Cheat sheet |
| Common bug: wrong base initialization. | 常見錯誤：基底初始化錯。 | Cheat sheet |
| Common bug: operation mapping confusion. | 常見錯誤：操作對應混淆。 | Cheat sheet |
| Explain transition meaning while coding. | 寫程式時同步解釋轉移意義。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Standard Levenshtein DP transition preserved.
- No hallucinated constraints: ✅ Operation set and output semantics maintained.
- Language simplicity: ✅ Clear interview explanation for operation mapping.
