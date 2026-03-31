# 07 Multiply Strings — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/07_Multiply_Strings.md`

> Quick links: [Source Solution](../07_Multiply_Strings.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Multiply Strings. | 我先重述 Multiply Strings。 | Restatement |
| We receive two non-negative integers as strings. | 題目給兩個非負整數字串。 | Restatement |
| We must return their product also as a string. | 要回傳乘積字串。 | Restatement |
| We cannot convert entire strings to built-in big integers. | 不能直接轉成大整數型別。 | Restatement |
| I will simulate grade-school multiplication with a digit array. | 我會用位數陣列模擬直式乘法。 | Restatement |
| Core idea is mapping each pair product into positions i plus j and i plus j plus one. | 核心是每對乘積映射到 i+j 與 i+j+1。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are inputs guaranteed to contain digits only? | 輸入是否保證只含數字字元？ | Clarify |
| Can either input be exactly zero? | 任一輸入是否可能為 0？ | Clarify |
| Are there no leading zeros except number zero itself? | 除了 0 本身外是否沒有前導零？ | Clarify |
| Is O(m times n) expected for lengths m and n? | 長度 m、n 預期 O(m*n) 嗎？ | Clarify |
| Is returning "0" required when any input is "0"? | 若任一輸入為 "0" 是否直接回 "0"？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Naive conversion to integer then multiply is disallowed and may overflow. | 直接轉整數再相乘不允許且會溢位。 | Approach |
| Another naive way does repeated string additions for each partial product. | 另一個暴力法是逐部分乘積做字串加法。 | Approach |
| It works but is verbose and less clean than position-array method. | 雖可行但冗長，且不如位置陣列法乾淨。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If either string is zero, return zero immediately. | 若任一字串為 0，立即回傳 0。 | Approach |
| Allocate result array of size m plus n initialized to zero. | 配置長度 m+n 的結果陣列，初始全 0。 | Approach |
| Iterate i and j from right to left, multiply corresponding digits. | i、j 從右到左遍歷並相乘位數。 | Approach |
| Add product into position p2=i+j+1, carry into p1=i+j. | 乘積加到 p2=i+j+1，進位加到 p1=i+j。 | Approach |
| Convert array to string while skipping leading zeros. | 最後轉字串並略過前導零。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I handle quick zero case first. | 我先處理快速零值案例。 | Coding |
| I set m and n as two string lengths. | 我設定 m、n 為兩字串長度。 | Coding |
| I create vector pos of size m plus n with zeros. | 我建立長度 m+n 的 pos 並填 0。 | Coding |
| For i from m minus one down to zero, loop over j similarly. | i 從 m-1 到 0，j 也同樣遞減。 | Coding |
| Compute mul from digit num1[i] times digit num2[j]. | 計算 num1[i] 與 num2[j] 的乘積 mul。 | Coding |
| Set p1=i+j and p2=i+j+1. | 設定 p1=i+j、p2=i+j+1。 | Coding |
| Sum is mul plus current pos[p2]. | sum = mul + pos[p2]。 | Coding |
| Write ones place to pos[p2] and add carry to pos[p1]. | 個位寫回 pos[p2]，進位加到 pos[p1]。 | Coding |
| After loops, build output string skipping leading zeros. | 雙迴圈後，略過前導零組出字串。 | Coding |
| Return built string, or zero fallback if empty. | 回傳結果字串，若空則回 "0"。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run num1 equals one-two-three and num2 equals four-five-six. | 我用 num1=123、num2=456 手跑。 | Dry-run |
| Result array size is six initially all zeros. | 結果陣列長度 6，初始全 0。 | Dry-run |
| Multiply three and six, put eighteen into tail positions. | 3 乘 6 得 18，放到尾端對應位置。 | Dry-run |
| Continue pair multiplications with carries merged into neighbors. | 繼續每對相乘，進位合併到左邊位置。 | Dry-run |
| After all pairs, array becomes digits of five-six-zero-eight-eight. | 全部完成後陣列成為 56088 的位數。 | Dry-run |
| Convert while skipping leading zero slots. | 轉字串時略過前導零欄位。 | Dry-run |
| Final answer is string five-six-zero-eight-eight. | 最終答案是字串 "56088"。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one digit times one digit. | 案例一：一位數乘一位數。 | Edge test |
| Case two: either input is zero. | 案例二：任一輸入為 0。 | Edge test |
| Case three: many carries like ninety-nine times ninety-nine. | 案例三：多重進位如 99*99。 | Edge test |
| Case four: uneven lengths like two-digit times six-digit. | 案例四：長度不均如 2 位乘 6 位。 | Edge test |
| Case five: large inputs near maximum allowed length. | 案例五：接近最大長度的大輸入。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m plus n). | 空間複雜度是 O(m+n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Nested loops multiply each digit pair once, totaling m times n operations. | 雙迴圈對每對位數相乘一次，共 m*n 次。 | Complexity |
| Position and carry updates are constant-time per pair. | 每對的定位與進位更新都是常數時間。 | Complexity |
| Therefore runtime is O(m times n). | 因此時間為 O(m*n)。 | Complexity |
| The output buffer has length m plus n, so memory is O(m plus n). | 輸出緩衝長度 m+n，故空間 O(m+n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me map this to grade-school multiplication first. | 我先把它映射成直式乘法。 | If stuck |
| Each digit pair contributes to two adjacent positions. | 每對位數會影響相鄰兩個位置。 | If stuck |
| p2 holds current ones place, p1 holds carry place. | p2 放個位，p1 放進位。 | If stuck |
| That is why p1=i+j and p2=i+j+1. | 所以才有 p1=i+j、p2=i+j+1。 | If stuck |
| I process from right to left to align least significant digits. | 右到左處理才會對齊最低位。 | If stuck |
| Let me verify with tiny case twelve times three. | 我先驗證小例子 12*3。 | If stuck |
| Then verify dense carry case ninety-nine times ninety-nine. | 再驗證高進位 99*99。 | If stuck |
| If output has leading zero, skip while building string. | 若結果有前導零，組字串時跳過。 | If stuck |
| Keep zero shortcut at top for clarity. | 開頭保留零值捷徑更清楚。 | If stuck |
| Great, logic now matches arithmetic exactly. | 很好，邏輯已和算術完全一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with position-array grade-school multiplication. | 我用位置陣列的直式乘法解題。 | Wrap-up |
| This avoids forbidden big-integer conversion. | 這避開了禁止的大整數轉換。 | Wrap-up |
| Carry handling is explicit and deterministic. | 進位處理明確且可驗證。 | Wrap-up |
| Complexity is O(mn) time and O(m+n) space. | 複雜度是 O(mn) 時間、O(m+n) 空間。 | Wrap-up |
| This is the standard interview answer for string multiplication. | 這是字串相乘題的標準面試解。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: multiply numeric strings without big integer cast. | 目標：不靠大整數轉型完成字串相乘。 | Cheat sheet |
| If either is "0", return "0". | 任一是 "0" 就回 "0"。 | Cheat sheet |
| Let m=len(num1), n=len(num2). | 設 m、n 為兩字串長度。 | Cheat sheet |
| Create pos array of size m+n. | 建立長度 m+n 的 pos。 | Cheat sheet |
| Loop i from right to left. | i 從右到左。 | Cheat sheet |
| Loop j from right to left. | j 從右到左。 | Cheat sheet |
| mul = digit1 * digit2. | mul=兩位數字相乘。 | Cheat sheet |
| p1=i+j, p2=i+j+1. | p1=i+j、p2=i+j+1。 | Cheat sheet |
| sum = mul + pos[p2]. | sum=mul+pos[p2]。 | Cheat sheet |
| pos[p2] = sum % 10. | pos[p2]=sum%10。 | Cheat sheet |
| pos[p1] += sum / 10. | pos[p1]+=sum/10。 | Cheat sheet |
| After loops, build string from pos. | 迴圈後由 pos 組字串。 | Cheat sheet |
| Skip leading zeros. | 略過前導零。 | Cheat sheet |
| Return built string. | 回傳組好的字串。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Space O(m+n). | 空間 O(m+n)。 | Cheat sheet |
| Common bug: wrong p1/p2 index mapping. | 常見錯誤：p1/p2 索引映射寫錯。 | Cheat sheet |
| Common bug: forgetting to accumulate existing pos[p2]. | 常見錯誤：忘了加上既有 pos[p2]。 | Cheat sheet |
| Validate with 123*456 -> 56088. | 用 123*456 -> 56088 驗證。 | Cheat sheet |
| Explain carry flow while coding. | 邊寫邊講進位流最加分。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Optimized simulation with index mapping.
- Constraint alignment: ✅ No big integer conversion used.
- Language simplicity: ✅ Natural spoken interview style.
