# 05 Longest Palindromic Substring — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/05_Longest_Palindromic_Substring.md`

> Quick links: [Source Solution](../05_Longest_Palindromic_Substring.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate longest palindromic substring. | 我先重述最長回文字串題。 | Restatement |
| We are given a string s. | 題目給一個字串 s。 | Restatement |
| We need the longest contiguous substring that is palindrome. | 要找最長且連續的回文子字串。 | Restatement |
| If multiple answers have same max length, any one is fine. | 若最長有多個，回任一個即可。 | Restatement |
| Substring means contiguous, not subsequence. | 子字串必須連續，不是子序列。 | Restatement |
| I will use expand-around-center in O(n squared) time. | 我會用中心擴展法，時間 O(n²)。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is returning either bab or aba acceptable for babad? | babad 回 bab 或 aba 都可嗎？ | Clarify |
| Do we need the substring itself, not just length? | 是否要回傳字串本身，不只長度？ | Clarify |
| Is case sensitivity standard character comparison? | 字元比較是否區分大小寫？ | Clarify |
| Can I prefer center expansion over O(n squared) DP table? | 可否優先中心擴展而非 DP 表？ | Clarify |
| Is empty string possible input? | 輸入是否可能是空字串？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks every substring and tests palindrome each time. | 暴力法枚舉每個子字串並逐一驗回文。 | Approach |
| There are O(n squared) substrings and each check can be O(n). | 子字串數 O(n²)，每次檢查可達 O(n)。 | Approach |
| Total becomes O(n cubed), too slow for n up to one thousand. | 總計 O(n³)，對 n=1000 太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Every palindrome has a center we can expand from. | 每個回文都可由某個中心向外擴展。 | Approach |
| We handle odd centers at i,i and even centers at i,i+1. | 處理奇中心 i,i 與偶中心 i,i+1。 | Approach |
| Expand while bounds valid and characters match. | 在邊界合法且字元相同時持續擴展。 | Approach |
| Track best start and max length whenever longer palindrome appears. | 遇到更長回文時更新起點與長度。 | Approach |
| This runs in O(n squared) time and O(1) space. | 這樣可達 O(n²) 時間、O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize start zero and maxLen zero. | 我先初始化 start=0、maxLen=0。 | Coding |
| I iterate i from zero to s length minus one. | i 從 0 迭代到字串結尾。 | Coding |
| I compute len1 by expanding around i,i for odd length. | 以 i,i 擴展算 len1（奇長）。 | Coding |
| I compute len2 by expanding around i,i+1 for even length. | 以 i,i+1 擴展算 len2（偶長）。 | Coding |
| len is max of len1 and len2. | len 取 len1 與 len2 較大。 | Coding |
| If len greater than maxLen, I update maxLen. | 若 len>maxLen 就更新 maxLen。 | Coding |
| I update start by i minus (len minus one) divided by two. | start 更新為 i-(len-1)/2。 | Coding |
| Finally I return s.substr(start, maxLen). | 最後回傳 s.substr(start,maxLen)。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s equals cbbd. | 我手跑 s="cbbd"。 | Dry-run |
| At i zero, odd center gives c length one. | i=0 時奇中心得到 c，長度 1。 | Dry-run |
| At i one, even center one-two expands to bb length two. | i=1 時偶中心 1,2 可擴展成 bb 長度 2。 | Dry-run |
| maxLen updates to two and start becomes one. | maxLen 更新為 2，start 為 1。 | Dry-run |
| Later centers do not exceed length two. | 後續中心都無法超過長度 2。 | Dry-run |
| Return substring from one of length two. | 回傳從索引 1 長度 2 的子字串。 | Dry-run |
| Final answer is bb, matching expected output. | 最終答案 bb，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single character string returns itself. | 案例一：單字元字串回自身。 | Edge test |
| Case two: all same chars like aaaa returns whole string. | 案例二：全同字元如 aaaa 回整串。 | Edge test |
| Case three: no length-two palindrome like abc returns any one char. | 案例三：如 abc 無長回文時回任一單字元。 | Edge test |
| Case four: even-length max palindrome like abba. | 案例四：偶數長最長回文如 abba。 | Edge test |
| Case five: odd-length max palindrome like racecar. | 案例五：奇數長最長回文如 racecar。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n squared). | 時間複雜度是 O(n²)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We consider two centers per index, about two n centers total. | 每個索引考慮兩種中心，約 2n 個中心。 | Complexity |
| Each center expansion can move up to O(n) in worst case. | 每個中心最壞可擴展 O(n)。 | Complexity |
| Multiplying gives O(n squared) total runtime. | 合併後總時間是 O(n²)。 | Complexity |
| We only track indices and lengths, so extra memory is O(1). | 只追蹤索引與長度，額外記憶體 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me remember every palindrome has a center. | 我先記得每個回文都有中心。 | If stuck |
| I must check both odd and even centers. | 我必須同時檢查奇中心與偶中心。 | If stuck |
| Expansion continues while left and right match. | 左右字元相同就繼續擴展。 | If stuck |
| I should update best answer only when length increases. | 只有更長時才更新最佳答案。 | If stuck |
| Start index formula is i minus len minus one over two. | 起點公式是 i-(len-1)/2。 | If stuck |
| Let me verify formula with len three and center one. | 我用 len=3、center=1 驗證公式。 | If stuck |
| It gives start zero, which is correct. | 得到 start=0，正確。 | If stuck |
| For len two and center zero, start is zero too. | len=2、center=0 時 start 也是 0。 | If stuck |
| Good, index math is consistent. | 很好，索引計算一致。 | If stuck |
| I can now finalize confidently. | 我可以有把握收尾。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved longest palindrome using center expansion. | 我用中心擴展解最長回文字串。 | Wrap-up |
| I evaluate odd and even centers at every index. | 我在每個索引評估奇偶兩種中心。 | Wrap-up |
| Best start and length are updated on longer matches. | 更長匹配時更新最佳起點與長度。 | Wrap-up |
| Runtime is O(n squared), space is O(1). | 時間 O(n²)，空間 O(1)。 | Wrap-up |
| This is practical and interview-friendly for n up to 1000. | 對 n<=1000 此法實用且面試友善。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem asks longest palindromic substring. | 題目要最長回文子字串。 | Cheat sheet |
| Substring must be contiguous. | 子字串必須連續。 | Cheat sheet |
| Any max answer is acceptable. | 任一最長答案都可。 | Cheat sheet |
| Use expand-around-center. | 使用中心擴展法。 | Cheat sheet |
| Check odd center i,i. | 檢查奇中心 i,i。 | Cheat sheet |
| Check even center i,i+1. | 檢查偶中心 i,i+1。 | Cheat sheet |
| Expand while chars match. | 字元相同就擴展。 | Cheat sheet |
| Get len1 and len2. | 取得 len1、len2。 | Cheat sheet |
| len = max(len1,len2). | len 取兩者較大。 | Cheat sheet |
| If len>maxLen update answer. | len>maxLen 時更新答案。 | Cheat sheet |
| start = i-(len-1)/2. | start=i-(len-1)/2。 | Cheat sheet |
| Return s.substr(start,maxLen). | 回傳 s.substr(start,maxLen)。 | Cheat sheet |
| Handles odd and even palindromes. | 可同時處理奇偶回文。 | Cheat sheet |
| Time O(n^2). | 時間 O(n²)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Sample cbbd -> bb. | 範例 cbbd -> bb。 | Cheat sheet |
| Sample babad -> bab or aba. | 範例 babad -> bab 或 aba。 | Cheat sheet |
| Common bug: only checking odd centers. | 常見錯誤：只檢查奇中心。 | Cheat sheet |
| Common bug: wrong start formula. | 常見錯誤：start 公式錯。 | Cheat sheet |
| Alternative: DP table O(n^2) space. | 替代法：DP 表需 O(n²) 空間。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Expand-around-center implementation preserved.
- No hallucinated constraints: ✅ Matches substring and output semantics.
- Language simplicity: ✅ Concise interview lines with correct index math.
