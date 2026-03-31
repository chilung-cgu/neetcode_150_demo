# 02 Valid Anagram — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/02_Valid_Anagram.md`

> Quick links: [Source Solution](../02_Valid_Anagram.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate this problem first. | 我先重述題目。 | Restatement |
| We need to check if s and t are anagrams. | 我們要判斷 s 和 t 是否為 anagram。 | Restatement |
| They must have same letters and same counts. | 它們要有相同字母與相同次數。 | Restatement |
| If lengths differ, the answer is false. | 若長度不同，答案一定是 false。 | Restatement |
| I will use one frequency array of size 26. | 我會用一個大小 26 的頻率陣列。 | Restatement |
| Then I will run quick edge checks. | 然後我會快速做邊界測試。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume lowercase English letters only? | 可以假設只有小寫英文字母嗎？ | Clarify |
| Do I need to support Unicode characters? | 需要支援 Unicode 字元嗎？ | Clarify |
| Are empty strings valid input here? | 空字串是合法輸入嗎？ | Clarify |
| Should uppercase and lowercase be different? | 大寫與小寫要視為不同嗎？ | Clarify |
| Is sorting acceptable, or do you want O(n)? | 排序可接受嗎，還是要 O(n)？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A baseline is sorting both strings. | 基線作法是把兩個字串都排序。 | Approach |
| If sorted strings match, they are anagrams. | 排序後相同就代表是 anagram。 | Approach |
| Time is O(n log n), plus sort space cost. | 時間是 O(n log n)，還有排序空間成本。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Better approach uses one count array. | 更好的方法是用一個計數陣列。 | Approach |
| For each i, I add s[i] and subtract t[i]. | 每個 i，我對 s[i] 加一、t[i] 減一。 | Approach |
| After one pass, all counts must be zero. | 一次遍歷後，所有計數都必須是零。 | Approach |
| Time is O(n), because each char is processed once. | 時間是 O(n)，因為每個字元只處理一次。 | Approach |
| Space is O(1) with fixed alphabet size 26. | 固定 26 字母時，空間是 O(1)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I compare lengths of s and t. | 先比較 s 與 t 的長度。 | Coding |
| If lengths differ, I return false immediately. | 長度不同就立刻回傳 false。 | Coding |
| Next, I create int count array of size 26. | 接著建立大小 26 的 count 陣列。 | Coding |
| Then, I loop i from zero to n minus one. | 然後 i 從 0 跑到 n-1。 | Coding |
| I do count[s[i]-'a'] plus plus. | 我做 count[s[i]-'a']++。 | Coding |
| I do count[t[i]-'a'] minus minus. | 我做 count[t[i]-'a']--。 | Coding |
| After loop, I scan all 26 counts. | 迴圈後，我掃描 26 個計數。 | Coding |
| If any count is not zero, return false. | 若有任何非零就回傳 false。 | Coding |
| Finally, all zero means return true. | 最後全為零就回傳 true。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s equals aab, t equals baa. | 我手跑 s = aab，t = baa。 | Dry-run |
| Lengths are equal, so we continue. | 長度相同，所以繼續。 | Dry-run |
| i zero: add a, subtract b. | i=0：a 加一，b 減一。 | Dry-run |
| i one: add a, subtract a. | i=1：a 加一，a 減一。 | Dry-run |
| i two: add b, subtract a. | i=2：b 加一，a 減一。 | Dry-run |
| Final counts all become zero. | 最後所有計數都變成零。 | Dry-run |
| So the function returns true. | 所以函式回傳 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: s empty, t empty, expect true. | 案例一：s 空、t 空，預期 true。 | Edge test |
| Case two: s is a, t empty, expect false. | 案例二：s 是 a、t 空，預期 false。 | Edge test |
| Case three: s rat, t car, expect false. | 案例三：s=rat、t=car，預期 false。 | Edge test |
| Case four: s anagram, t nagaram, expect true. | 案例四：anagram 與 nagaram，預期 true。 | Edge test |
| Case five: mixed case behavior must be confirmed. | 案例五：大小寫行為需先確認。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Space is O(1) with 26 letters. | 在 26 字母下空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We iterate through both strings in one pass. | 我們一次遍歷兩個字串。 | Complexity |
| Each step does constant work on the array. | 每一步都只做常數量陣列操作。 | Complexity |
| The count array size is fixed to 26. | 計數陣列大小固定為 26。 | Complexity |
| For Unicode, switch to hash map with larger space. | 若是 Unicode，要改 hash map 並用更多空間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me recheck the alphabet assumption. | 我先重確認字母集假設。 | If stuck |
| I can start with sorting first. | 我可以先用排序法起步。 | If stuck |
| Then I will optimize to counting array. | 接著我會優化到計數陣列。 | If stuck |
| I forgot a syntax, not the logic. | 我忘了語法，不是邏輯。 | If stuck |
| I will finish logic, then polish syntax. | 我先完成邏輯，再修語法。 | If stuck |
| Could you confirm Unicode requirement? | 可以確認是否要支援 Unicode 嗎？ | If stuck |
| Thanks, I will adjust the data structure. | 謝謝，我會調整資料結構。 | If stuck |
| I found the mismatch and fixed it. | 我找到不一致並修好了。 | If stuck |
| Let me rerun one quick sample. | 我再快速跑一個範例。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test cases. | 我驗證了常規與邊界案例。 | Wrap-up |
| Length precheck avoids unnecessary work. | 長度預檢可避免多餘運算。 | Wrap-up |
| Time is O(n), space is O(1) here. | 這裡時間 O(n)、空間 O(1)。 | Wrap-up |
| I can discuss Unicode variant if needed. | 需要的話我可補充 Unicode 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate: compare letter frequencies. | 重述：比較字母頻率。 | Cheat sheet |
| Ask if input is lowercase only. | 詢問是否只限小寫。 | Cheat sheet |
| Check lengths before all logic. | 所有邏輯前先檢查長度。 | Cheat sheet |
| Sorting is baseline, O(n log n). | 排序是基線，O(n log n)。 | Cheat sheet |
| Counting array is optimized. | 計數陣列是優化解。 | Cheat sheet |
| Use one array of size 26. | 使用一個 26 大小陣列。 | Cheat sheet |
| Add for s, subtract for t. | s 做加法，t 做減法。 | Cheat sheet |
| One pass over characters. | 對字元做一次遍歷。 | Cheat sheet |
| Scan 26 counts at the end. | 最後掃描 26 個計數。 | Cheat sheet |
| Any nonzero means false. | 任一非零就是 false。 | Cheat sheet |
| All zero means true. | 全為零就是 true。 | Cheat sheet |
| Dry-run with s=aab, t=baa. | 用 s=aab、t=baa 手跑。 | Cheat sheet |
| Test empty-string pair. | 測試空字串配對。 | Cheat sheet |
| Test unequal lengths. | 測試長度不等。 | Cheat sheet |
| Test clear mismatch words. | 測試明顯不匹配字串。 | Cheat sheet |
| Report time O(n). | 報告時間 O(n)。 | Cheat sheet |
| Report space O(1) for 26 chars. | 報告空間 O(1)（26 字母）。 | Cheat sheet |
| Mention Unicode fallback map. | 提及 Unicode 需改 map。 | Cheat sheet |
| Keep speaking while coding. | 邊寫邊口述重點。 | Cheat sheet |
| End with concise summary. | 以精簡結論收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Frequency-array main approach and length precheck are preserved.
- No hallucinated constraints: ✅ Uncertain parts are asked in clarification lines.
- Language simplicity: ✅ Short A2-B1 interview-safe spoken lines.
