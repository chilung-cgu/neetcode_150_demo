# 10 Word Break — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/10_Word_Break.md`

> Quick links: [Source Solution](../10_Word_Break.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the word break problem. | 我先重述 Word Break 題目。 | Restatement |
| We are given a string s and a dictionary of words. | 題目給字串 s 與字典 wordDict。 | Restatement |
| We need to decide whether s can be segmented fully. | 要判斷 s 是否可被完整切分。 | Restatement |
| Each segment must be a word from the dictionary. | 每個片段都必須在字典中。 | Restatement |
| Words can be reused multiple times. | 同一單字可重複使用。 | Restatement |
| I will use bottom-up DP on string indices. | 我會用索引上的自底向上 DP。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do we return boolean only, not one valid segmentation? | 是否只回布林，不需回切分方案？ | Clarify |
| Can dictionary words be reused unlimited times? | 字典單字是否可無限重用？ | Clarify |
| Is matching case-sensitive? | 字串比對是否區分大小寫？ | Clarify |
| Are there only lowercase English letters in input? | 輸入是否僅含小寫英文字母？ | Clarify |
| Is O(n times wordCount times avgWordLen) acceptable? | O(n*字典數*平均字長) 可接受嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries every split position recursively. | 暴力法遞迴嘗試每個切點。 | Approach |
| Many suffixes get recomputed repeatedly. | 很多後綴會被重複計算。 | Approach |
| Worst-case runtime is exponential. | 最壞時間會是指數級。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Define dp[i] as whether suffix s[i:] is segmentable. | 定義 dp[i] 為後綴 s[i:] 是否可切分。 | Approach |
| Base case dp[n] is true for empty suffix. | 基底 dp[n]=true，代表空後綴可行。 | Approach |
| Iterate i from n-1 down to 0. | i 從 n-1 反向走到 0。 | Approach |
| For each word w, if s at i starts with w and dp[i+len] is true, set dp[i] true. | 對每個 w，若 i 位置可匹配且 dp[i+len] 為真，設 dp[i]=true。 | Approach |
| Final answer is dp[0]. | 最終答案是 dp[0]。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I get n as s length and create boolean dp of size n plus one. | 我先取 n=s 長度，建立 n+1 的布林 dp。 | Coding |
| I set dp[n] to true as base case. | 設 dp[n]=true 當基底。 | Coding |
| I iterate i from n minus one down to zero. | i 從 n-1 迭代到 0。 | Coding |
| For each dictionary word w, I check bounds i plus len(w) <= n. | 對每個字 w，先檢查 i+len(w)<=n。 | Coding |
| If substring s[i, len] equals w, I can use dp[i+len]. | 若 s 的該段等於 w，可參考 dp[i+len]。 | Coding |
| I set dp[i] to dp[i+len] when matched. | 匹配後把 dp[i] 設為 dp[i+len]。 | Coding |
| If dp[i] becomes true, I break inner loop early. | 若 dp[i] 成真，內層可提早 break。 | Coding |
| After loops, I return dp[0]. | 迴圈結束回傳 dp[0]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s equals leetcode and dict [leet, code]. | 我手跑 s=leetcode、dict=[leet,code]。 | Dry-run |
| n is eight, so dp[8] starts as true. | n=8，所以 dp[8] 初始為 true。 | Dry-run |
| At i equals four, word code matches and dp[8] is true, so dp[4] becomes true. | i=4 時 code 匹配且 dp[8] 為真，故 dp[4]=true。 | Dry-run |
| At i equals zero, word leet matches and dp[4] is true, so dp[0] becomes true. | i=0 時 leet 匹配且 dp[4] 為真，故 dp[0]=true。 | Dry-run |
| Other positions may remain false, that is fine. | 其他位置可為 false，這沒問題。 | Dry-run |
| Final answer is true. | 最終答案為 true。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: s is a single dictionary word. | 案例一：s 本身就是字典單字。 | Edge test |
| Case two: impossible split like catsandog example. | 案例二：像 catsandog 無法切分。 | Edge test |
| Case three: repeated-word usage like applepenapple. | 案例三：重複用詞如 applepenapple。 | Edge test |
| Case four: overlapping choices such as car, ca, rs. | 案例四：重疊選擇如 car、ca、rs。 | Edge test |
| Case five: long string with no valid suffix transition. | 案例五：長字串但沒有合法後綴轉移。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n times m times L). | 時間複雜度是 O(n*m*L)。 | Complexity |
| Space complexity is O(n). | 空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We evaluate n positions in the string. | 我們會評估字串的 n 個位置。 | Complexity |
| At each position we may try m words in dictionary. | 每個位置最多嘗試 m 個字典單字。 | Complexity |
| Matching each word costs up to its length L. | 每次匹配成本最多是字長 L。 | Complexity |
| So runtime is O(n*m*L), and dp array uses O(n) memory. | 因此時間 O(n*m*L)，dp 記憶體 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me define the DP state first. | 我先定義 DP 狀態。 | If stuck |
| dp[i] means whether suffix starting at i is breakable. | dp[i] 代表從 i 開始後綴能否切分。 | If stuck |
| Base case is dp[n] equals true. | 基底是 dp[n]=true。 | If stuck |
| I should iterate from right to left. | 迭代方向應該由右往左。 | If stuck |
| For each index, I test every dictionary word. | 每個索引都測試所有字典單字。 | If stuck |
| Only when prefix matches I consult dp[i+len]. | 只有前綴匹配才看 dp[i+len]。 | If stuck |
| If any word makes dp[i] true, I can break early. | 只要有字讓 dp[i] 為真就可提早停止。 | If stuck |
| Let me sanity-check with leetcode quickly. | 我快速用 leetcode 做健全檢查。 | If stuck |
| dp[4] and dp[0] become true in that example. | 該例中 dp[4] 與 dp[0] 會成真。 | If stuck |
| Great, recurrence and direction are consistent. | 很好，遞推與方向都一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved word break using bottom-up DP on indices. | 我用索引自底向上 DP 解出 Word Break。 | Wrap-up |
| State dp[i] represents segmentability of suffix s[i:]. | 狀態 dp[i] 代表後綴 s[i:] 的可切分性。 | Wrap-up |
| We use dp[n] as base and fill from right to left. | 以 dp[n] 為基底，從右到左填表。 | Wrap-up |
| Complexity is O(n*m*L) time and O(n) space. | 複雜度為 O(n*m*L) 時間、O(n) 空間。 | Wrap-up |
| This handles repeated words and impossible cases cleanly. | 可乾淨處理重複單字與無解情況。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: can s be fully segmented by dictionary words. | 目標：s 能否被字典單字完整切分。 | Cheat sheet |
| Return boolean only. | 只回傳布林值。 | Cheat sheet |
| Words may be reused. | 單字可重複使用。 | Cheat sheet |
| Define dp[i] for suffix s[i:]. | 定義 dp[i] 對應後綴 s[i:]。 | Cheat sheet |
| Base dp[n]=true. | 基底 dp[n]=true。 | Cheat sheet |
| Iterate i from n-1 down to 0. | i 從 n-1 走到 0。 | Cheat sheet |
| For each word w, check boundary first. | 對每個 w 先做邊界檢查。 | Cheat sheet |
| If substring matches w, use dp[i+len(w)]. | 若子字串匹配 w，使用 dp[i+len(w)]。 | Cheat sheet |
| Set dp[i]=true when any valid word found. | 找到任一合法字就設 dp[i]=true。 | Cheat sheet |
| Break inner loop after success. | 成功後可提前離開內層。 | Cheat sheet |
| Final answer is dp[0]. | 最終答案是 dp[0]。 | Cheat sheet |
| Example leetcode -> true. | 範例 leetcode -> true。 | Cheat sheet |
| Example catsandog -> false. | 範例 catsandog -> false。 | Cheat sheet |
| Time O(n*m*L). | 時間 O(n*m*L)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Common bug: wrong DP direction. | 常見錯誤：DP 方向寫反。 | Cheat sheet |
| Common bug: forgetting boundary i+len<=n. | 常見錯誤：忘記邊界 i+len<=n。 | Cheat sheet |
| Common bug: not breaking after dp[i] true. | 常見錯誤：dp[i] 成真後未提前停止。 | Cheat sheet |
| Recheck state meaning if confused. | 若混亂先重申狀態定義。 | Cheat sheet |
| Keep explanation tied to suffix transitions. | 說明時聚焦後綴轉移邏輯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Suffix DP recurrence and right-to-left traversal preserved.
- No hallucinated constraints: ✅ Uses source semantics (boolean decision, reusable words).
- Language simplicity: ✅ Clean interview lines with explicit state and transition wording.
