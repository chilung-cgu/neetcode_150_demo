# 06 Palindromic Substrings — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/06_Palindromic_Substrings.md`

> Quick links: [Source Solution](../06_Palindromic_Substrings.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate palindromic substrings counting problem. | 我先重述回文子字串計數題。 | Restatement |
| We are given a string s. | 題目給一個字串 s。 | Restatement |
| We need total number of palindromic substrings. | 要求回文子字串總數。 | Restatement |
| Same letters at different positions count separately. | 相同內容但位置不同要分開計算。 | Restatement |
| Single characters are all palindromes. | 每個單字元都算回文。 | Restatement |
| I will use expand-around-center and count every valid expansion. | 我會用中心擴展並統計每次成功擴展。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do repeated substrings at different indices count multiple times? | 不同索引的相同子字串是否重複計算？ | Clarify |
| Are we returning only count, not actual substrings? | 是否只回傳數量，不回傳內容？ | Clarify |
| Is empty string excluded by constraints? | 限制下是否不會給空字串？ | Clarify |
| Can I reuse center-expansion idea from longest palindrome? | 可否沿用最長回文的中心擴展想法？ | Clarify |
| Is O(n squared) expected and accepted? | O(n²) 是否為可接受解法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force enumerates all substrings and checks each palindrome. | 暴力法列舉所有子字串再逐一驗回文。 | Approach |
| That is O(n cubed) in worst case. | 最壞複雜度是 O(n³)。 | Approach |
| We can do better with center expansion. | 可用中心擴展做得更好。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each palindrome can be discovered from a center. | 每個回文都可由某中心找到。 | Approach |
| For each index, expand odd center i,i and even center i,i+1. | 每個索引展開奇中心 i,i 與偶中心 i,i+1。 | Approach |
| During expansion, every successful match adds one to count. | 擴展中每次匹配成功就加一。 | Approach |
| Stop expanding when boundary fails or chars differ. | 越界或不相等時停止擴展。 | Approach |
| Summing all centers gives total palindromic substrings. | 累加所有中心結果即總回文數。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize total count to zero. | 我先把總計數設為 0。 | Coding |
| I loop i from zero to s length minus one. | i 從 0 走到字串尾。 | Coding |
| I add count from odd expansion at i,i. | 加上奇中心 i,i 的擴展數。 | Coding |
| I add count from even expansion at i,i+1. | 加上偶中心 i,i+1 的擴展數。 | Coding |
| Expansion helper starts with local counter zero. | 擴展 helper 先有區域計數 0。 | Coding |
| While bounds valid and chars match, increment counter and expand. | 邊界合法且字元相同就加一並外擴。 | Coding |
| Helper returns local count to caller. | helper 回傳該中心的計數。 | Coding |
| Main function returns accumulated total count. | 主函式回傳累積總數。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s equals aaa. | 我手跑 s="aaa"。 | Dry-run |
| Center at zero gives one odd palindrome a. | 中心 0 提供一個奇回文 a。 | Dry-run |
| Even center zero-one gives one palindrome aa. | 偶中心 0,1 提供一個回文 aa。 | Dry-run |
| Center at one gives odd palindromes a and aaa. | 中心 1 的奇擴展給 a 與 aaa。 | Dry-run |
| Even center one-two gives another aa. | 偶中心 1,2 再給一個 aa。 | Dry-run |
| Center at two gives one odd palindrome a. | 中心 2 再給一個奇回文 a。 | Dry-run |
| Total count is six, matching expected result. | 總數為 6，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single character should return one. | 案例一：單字元應回 1。 | Edge test |
| Case two: all distinct chars like abc returns length count only. | 案例二：全不同如 abc 只回長度數量。 | Edge test |
| Case three: all same chars gives maximal palindrome count. | 案例三：全同字元會有最大回文數。 | Edge test |
| Case four: mixed odd and even palindromes in one string. | 案例四：同時有奇偶回文的混合字串。 | Edge test |
| Case five: long repeated pattern stress test. | 案例五：長重複模式壓力測試。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n squared). | 時間複雜度是 O(n²)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We evaluate around two centers per index. | 每個索引評估兩種中心。 | Complexity |
| In worst case each expansion can travel O(n). | 最壞每次擴展可到 O(n)。 | Complexity |
| Total runtime is therefore O(n squared). | 因此總時間為 O(n²)。 | Complexity |
| We only store counters and pointers, so extra space is O(1). | 只用計數器與指標，額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me align with longest palindrome technique first. | 我先對齊最長回文那題技巧。 | If stuck |
| The difference is we count all expansions, not only max length. | 差別是這題要數全部，不只最長。 | If stuck |
| I must include both odd and even centers. | 必須包含奇偶兩種中心。 | If stuck |
| Every successful expansion contributes one palindrome. | 每次成功擴展就貢獻一個回文。 | If stuck |
| Stop as soon as mismatch or boundary break occurs. | 一旦不匹配或越界就停止。 | If stuck |
| Let me verify quickly with abc. | 我快速用 abc 驗證。 | If stuck |
| I get three from single letters only. | 只會得到三個單字元回文。 | If stuck |
| For aaa I should get six. | 對 aaa 應得到六。 | If stuck |
| That confirms counting logic is correct. | 這證明計數邏輯正確。 | If stuck |
| Great, I can conclude confidently. | 很好，我可有把握收尾。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved palindromic substring counting with center expansion. | 我用中心擴展解回文子字串計數。 | Wrap-up |
| I sum counts from odd and even centers for each index. | 我對每個索引累加奇偶中心計數。 | Wrap-up |
| Each successful expansion directly adds one to answer. | 每次成功擴展直接讓答案加一。 | Wrap-up |
| Runtime is O(n squared) and extra space O(1). | 時間 O(n²)、額外空間 O(1)。 | Wrap-up |
| This is clean and easy to explain in interviews. | 這在面試中清楚且易解釋。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem asks count of palindromic substrings. | 題目要回文字串數量。 | Cheat sheet |
| Position-distinct substrings count separately. | 不同位置要分開計算。 | Cheat sheet |
| Use center expansion. | 使用中心擴展法。 | Cheat sheet |
| Iterate each index i. | 迭代每個索引 i。 | Cheat sheet |
| Expand odd center i,i. | 擴展奇中心 i,i。 | Cheat sheet |
| Expand even center i,i+1. | 擴展偶中心 i,i+1。 | Cheat sheet |
| Helper returns count from one center. | helper 回傳單一中心計數。 | Cheat sheet |
| While s[l]==s[r], count++. | s[l]==s[r] 時 count++。 | Cheat sheet |
| Move l-- and r++ each success. | 每次成功後 l--、r++。 | Cheat sheet |
| Stop when mismatch or out of bounds. | 不符或越界即停止。 | Cheat sheet |
| Add odd and even counts to total. | 把奇偶計數加到總數。 | Cheat sheet |
| Single characters always contribute. | 單字元一定貢獻。 | Cheat sheet |
| abc -> 3. | abc -> 3。 | Cheat sheet |
| aaa -> 6. | aaa -> 6。 | Cheat sheet |
| Time O(n^2). | 時間 O(n²)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: forgetting even centers. | 常見錯誤：漏掉偶中心。 | Cheat sheet |
| Common bug: counting only max length. | 常見錯誤：只算最長不算全部。 | Cheat sheet |
| Related to longest palindrome problem. | 與最長回文題高度相關。 | Cheat sheet |
| Great quick interview implementation. | 是快速面試實作好選擇。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Center-expansion counting approach preserved.
- No hallucinated constraints: ✅ Correct counting semantics for position-distinct substrings.
- Language simplicity: ✅ Concise, spoken, and directly actionable.
