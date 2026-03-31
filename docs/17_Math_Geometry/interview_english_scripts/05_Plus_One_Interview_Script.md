# 05 Plus One — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/05_Plus_One.md`

> Quick links: [Source Solution](../05_Plus_One.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Plus One. | 我先重述 Plus One。 | Restatement |
| Digits array represents a non-negative integer, most significant digit first. | digits 陣列代表非負整數，最高位在前。 | Restatement |
| We need to add one and return resulting digits. | 我們要加一並回傳結果陣列。 | Restatement |
| The key difficulty is carry propagation. | 核心難點是進位傳遞。 | Restatement |
| I will iterate from right to left. | 我會從右到左處理。 | Restatement |
| If all digits are nine, we prepend one. | 若全部是 9，就在前面補 1。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are there no leading zeros except number zero itself? | 除了 0 本身外是否沒有前導零？ | Clarify |
| Is input always non-empty? | 輸入陣列是否保證非空？ | Clarify |
| Can I modify the input vector directly and return it? | 我可以直接改輸入 vector 後回傳嗎？ | Clarify |
| Are digits guaranteed between zero and nine? | 每位是否保證都在 0 到 9？ | Clarify |
| Is O(n) time and O(1) extra space expected? | 是否預期 O(n) 時間與 O(1) 額外空間？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A naive idea is converting digits to an integer, add one, then split again. | 直覺法是轉整數、加一、再拆回位數。 | Approach |
| That fails for very large length due to overflow. | 位數很大時會溢位失敗。 | Approach |
| So we should stay in digit-array arithmetic. | 所以應直接做位數陣列運算。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Traverse from last index toward zero. | 從最後一位往前走。 | Approach |
| If current digit is less than nine, increment and return immediately. | 若當前位小於 9，+1 後可立刻回傳。 | Approach |
| If current digit is nine, set it to zero and continue carry. | 若是 9，設為 0 並繼續進位。 | Approach |
| If loop finishes, all digits were nine. | 若整輪跑完，代表全部都是 9。 | Approach |
| Insert one at front, result naturally becomes one followed by zeros. | 前面插入 1，結果自然是一後面全 0。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I get n as digits size. | 我先取 n 為 digits 長度。 | Coding |
| I loop i from n minus one down to zero. | i 從 n-1 往 0 遞減。 | Coding |
| If digits[i] is less than nine, I increment it. | 若 digits[i] < 9，我就將它加一。 | Coding |
| Then I return digits because carry stops. | 然後直接回傳，因為進位結束。 | Coding |
| Otherwise digits[i] is nine, so I set it to zero. | 否則該位是 9，設為 0。 | Coding |
| Continue loop to propagate carry leftward. | 繼續迴圈把進位往左傳。 | Coding |
| If loop ends, all digits became zero. | 若迴圈結束，代表每位都變成 0。 | Coding |
| I insert one at beginning. | 我在最前面插入 1。 | Coding |
| Return the updated digits vector. | 回傳更新後的 digits。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run digits equals [9,9]. | 我用 digits=[9,9] 手跑。 | Dry-run |
| Start from rightmost nine, set to zero. | 從最右邊 9 開始，設成 0。 | Dry-run |
| Move left, again nine, set to zero. | 往左還是 9，再設成 0。 | Dry-run |
| Loop finishes without early return. | 迴圈結束仍未提早回傳。 | Dry-run |
| Insert one at front. | 在最前面插入 1。 | Dry-run |
| Result becomes [1,0,0]. | 結果變為 [1,0,0]。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single digit zero. | 案例一：單位數 0。 | Edge test |
| Case two: single digit nine. | 案例二：單位數 9。 | Edge test |
| Case three: no carry case like [1,2,3]. | 案例三：無進位如 [1,2,3]。 | Edge test |
| Case four: partial carry like [1,2,9]. | 案例四：部分進位如 [1,2,9]。 | Edge test |
| Case five: all nines like [9,9,9]. | 案例五：全 9 如 [9,9,9]。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n) in the worst case. | 最壞時間複雜度是 O(n)。 | Complexity |
| Extra space is O(1), excluding possible output growth by one digit. | 額外空間是 O(1)，不含輸出可能多一位。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan from right to left once. | 我們從右到左至多掃一遍。 | Complexity |
| Best case returns after one step when last digit is not nine. | 最佳情況末位非 9，一步就回傳。 | Complexity |
| Worst case all digits are nine, touching every position. | 最壞情況全是 9，要碰每一位。 | Complexity |
| We use constant helper variables, so extra memory is O(1). | 只用常數變數，故額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on carry behavior only. | 我先只聚焦進位行為。 | If stuck |
| Adding one affects suffix of trailing nines. | 加一只會影響尾端連續的 9。 | If stuck |
| If digit is below nine, increment and stop. | 若某位小於 9，+1 後即可停止。 | If stuck |
| If digit is nine, set to zero and continue left. | 若是 9，設為 0 並往左繼續。 | If stuck |
| So right-to-left scan is the natural order. | 所以右到左掃描是自然順序。 | If stuck |
| All-nine case is the only case needing length growth. | 只有全 9 情況才要長度增加。 | If stuck |
| Then prepend one at index zero. | 此時在索引 0 前插入 1。 | If stuck |
| Let me verify with [9] and [1,9,9]. | 我用 [9] 與 [1,9,9] 驗證。 | If stuck |
| Both confirm the carry chain logic. | 兩者都驗證了進位鏈邏輯。 | If stuck |
| Great, implementation is straightforward now. | 很好，現在實作就很直接。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with a single right-to-left carry scan. | 我用單次右到左進位掃描解題。 | Wrap-up |
| It handles normal, partial-carry, and all-nine cases cleanly. | 一般、部分進位、全 9 都可乾淨處理。 | Wrap-up |
| The logic is short and interview-friendly. | 邏輯短且面試表達友善。 | Wrap-up |
| Complexity is O(n) time and O(1) extra space. | 複雜度是 O(n) 時間、O(1) 額外空間。 | Wrap-up |
| I can also discuss immutable-array variant if needed. | 若需要我也可補充不可變陣列版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: add one to integer represented by digits array. | 目標：對 digits 表示的整數加一。 | Cheat sheet |
| Work from rightmost digit. | 從最右位開始。 | Cheat sheet |
| If digit < 9, increment and return. | 若位數 < 9，+1 後回傳。 | Cheat sheet |
| If digit == 9, set to 0 and continue. | 若位數 == 9，設 0 並繼續。 | Cheat sheet |
| This propagates carry leftward. | 這樣把進位往左傳。 | Cheat sheet |
| If loop completes, all were nines. | 若迴圈跑完，代表全是 9。 | Cheat sheet |
| Prepend one at front. | 前面補一個 1。 | Cheat sheet |
| Return updated digits. | 回傳更新後 digits。 | Cheat sheet |
| Example [1,2,3] => [1,2,4]. | 範例 [1,2,3] => [1,2,4]。 | Cheat sheet |
| Example [1,2,9] => [1,3,0]. | 範例 [1,2,9] => [1,3,0]。 | Cheat sheet |
| Example [9] => [1,0]. | 範例 [9] => [1,0]。 | Cheat sheet |
| Example [9,9] => [1,0,0]. | 範例 [9,9] => [1,0,0]。 | Cheat sheet |
| Time O(n) worst case. | 最壞時間 O(n)。 | Cheat sheet |
| Extra space O(1). | 額外空間 O(1)。 | Cheat sheet |
| Common bug: forgetting all-nine growth. | 常見錯誤：忘了全 9 需增長位數。 | Cheat sheet |
| Common bug: scanning from left to right. | 常見錯誤：從左往右掃描。 | Cheat sheet |
| Early return makes code concise. | 提早回傳可讓程式簡潔。 | Cheat sheet |
| Carry chain ends at first non-nine. | 進位鏈會在第一個非 9 處停止。 | Cheat sheet |
| Keep mutation in-place when allowed. | 可原地修改時保持 in-place。 | Cheat sheet |
| Easy question, but explain carry clearly. | 題目簡單，但進位要講清楚。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Right-to-left carry handling.
- Constraint alignment: ✅ Works without integer conversion overflow risks.
- Language simplicity: ✅ Crisp and interview-practical lines.
