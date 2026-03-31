# 08 Letter Combinations of a Phone Number — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/08_Letter_Combinations.md`

> Quick links: [Source Solution](../08_Letter_Combinations.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the phone-letter combinations problem. | 我先重述電話字母組合題。 | Restatement |
| Input is a digit string from two to nine. | 輸入是由 2 到 9 組成的字串。 | Restatement |
| Each digit maps to several letters on keypad. | 每個數字對應按鍵上的多個字母。 | Restatement |
| We need all possible letter combinations. | 我們要回傳所有可能字母組合。 | Restatement |
| If input is empty, result should be empty list. | 若輸入為空，結果應是空陣列。 | Restatement |
| I will use DFS backtracking over digit positions. | 我會用 DFS 回溯逐位展開。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume digits contain only two through nine? | 可否假設 digits 只含 2~9？ | Clarify |
| Should empty input return empty vector instead of one empty string? | 空輸入要回空陣列而非含空字串嗎？ | Clarify |
| Is output order arbitrary as long as all combinations exist? | 只要完整，輸出順序可任意嗎？ | Clarify |
| Is recursive backtracking preferred for readability? | 面試中是否偏好遞迴回溯表達？ | Clarify |
| Can I use array lookup table for digit-to-letters mapping? | 可否用陣列查表做數字到字母映射？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force concept is cartesian product of letter groups. | 暴力概念是各位字母集合的笛卡兒積。 | Approach |
| We can build iteratively or recursively. | 可用迭代或遞迴建構。 | Approach |
| Backtracking gives the cleanest interview narrative. | 回溯最適合面試口述。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Create mapping table from digit to letters. | 建立 digit 到 letters 的映射表。 | Approach |
| DFS state is index in digits and current string path. | DFS 狀態為 digits 索引與當前字串。 | Approach |
| For current digit, try each mapped letter. | 對當前數字嘗試每個對應字母。 | Approach |
| Append letter, recurse index plus one, then remove letter. | 加字母後遞迴 index+1，再移除字母。 | Approach |
| When path length equals digits length, record one result. | 當路徑長度等於 digits 長度就記錄結果。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I define keypad mapping array from zero to nine. | 我先定義 0~9 的按鍵映射陣列。 | Coding |
| If digits is empty, I return empty result immediately. | 若 digits 為空就直接回空結果。 | Coding |
| I prepare result vector and mutable current string. | 我準備結果向量與可變 current 字串。 | Coding |
| I call backtrack starting at index zero. | 我從 index=0 呼叫 backtrack。 | Coding |
| Base case is index equals digits length. | 基底條件是 index 等於 digits 長度。 | Coding |
| At base, push current string into result. | 基底時把 current 放進結果。 | Coding |
| Otherwise iterate letters mapped from current digit. | 否則迭代當前 digit 對應字母。 | Coding |
| Push char recurse pop char for backtracking. | push 字元、遞迴、再 pop 字元。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run digits twenty-three. | 我手跑 digits="23"。 | Dry-run |
| Digit two maps to a b c. | 數字 2 對應 a b c。 | Dry-run |
| For prefix a, digit three gives ad ae af. | 前綴 a 搭配 3 會得到 ad ae af。 | Dry-run |
| For prefix b, we get bd be bf. | 前綴 b 會得到 bd be bf。 | Dry-run |
| For prefix c, we get cd ce cf. | 前綴 c 會得到 cd ce cf。 | Dry-run |
| Total nine combinations are generated. | 總共生成九個組合。 | Dry-run |
| This matches expected sample output exactly. | 這與範例預期完全一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty digits should return empty list. | 案例一：空字串應回空陣列。 | Edge test |
| Case two: one digit like seven returns four letters. | 案例二：單一 7 應回四個字母。 | Edge test |
| Case three: mixed three-letter and four-letter digits. | 案例三：混合 3 字母與 4 字母按鍵。 | Edge test |
| Case four: repeated same digit like twenty-two. | 案例四：重複同數字如 "22"。 | Edge test |
| Case five: maximum length input within constraints. | 案例五：限制內最大長度輸入。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(four to the n times n) in worst case. | 最壞時間複雜度為 O(4^n*n)。 | Complexity |
| Recursion depth and auxiliary stack are O(n). | 遞迴深度與輔助堆疊是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each digit contributes up to four branches for seven or nine. | 每個 digit 最多帶來 4 個分支（7/9）。 | Complexity |
| So total combinations are bounded by four to the n. | 因此組合數上界為 4^n。 | Complexity |
| Building each output string takes O(n). | 生成每個輸出字串成本 O(n)。 | Complexity |
| Recursion stack depth is n, excluding result storage. | 不含結果儲存時遞迴深度是 n。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me map this to a decision tree per digit position. | 我先把它映射成每一位數字的決策樹。 | If stuck |
| At each level I choose one letter from current digit. | 每一層從當前 digit 選一個字母。 | If stuck |
| Path length should equal processed digit count. | 路徑長度應等於已處理位數。 | If stuck |
| Base case triggers when index reaches digits length. | index 到 digits 長度時觸發基底。 | If stuck |
| I must return empty list for empty input. | 空輸入必須回空陣列。 | If stuck |
| Mapping table avoids repeated switch statements. | 查表映射可避免重複 switch。 | If stuck |
| Let me test quickly with digits twenty-three. | 我快速用 "23" 驗證。 | If stuck |
| I see nine outputs from three times three choices. | 會得到 3*3 共九個輸出。 | If stuck |
| That confirms recursion branching is correct. | 這證明遞迴分支正確。 | If stuck |
| Great, I can summarize complexity now. | 很好，我可以收尾複雜度。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved this with DFS backtracking and keypad mapping. | 我用 DFS 回溯與按鍵映射解題。 | Wrap-up |
| Each recursion level handles one digit position. | 每層遞迴處理一個 digit 位置。 | Wrap-up |
| Push recurse pop forms the full combination tree. | push-recuse-pop 組成完整組合樹。 | Wrap-up |
| Empty input is handled explicitly as special case. | 空輸入以特例顯式處理。 | Wrap-up |
| Complexity is exponential in digit length as expected. | 複雜度如預期對位數呈指數。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: keypad cartesian product. | 題型：按鍵字母笛卡兒積。 | Cheat sheet |
| Input digits range two to nine. | 輸入數字範圍 2 到 9。 | Cheat sheet |
| Build digit-to-letter mapping first. | 先建立 digit-letter 映射。 | Cheat sheet |
| Empty input returns empty result. | 空輸入回空結果。 | Cheat sheet |
| Use DFS backtracking by index. | 用依索引 DFS 回溯。 | Cheat sheet |
| State: index and current string. | 狀態：index 與 current 字串。 | Cheat sheet |
| Base when index equals length. | index 等於長度即基底。 | Cheat sheet |
| Push current string to result at base. | 基底時把字串放入結果。 | Cheat sheet |
| Get mapped letters for digits[index]. | 取出 digits[index] 的字母群。 | Cheat sheet |
| Loop each letter choice. | 迴圈嘗試每個字母。 | Cheat sheet |
| Append letter then recurse. | 先附加字母再遞迴。 | Cheat sheet |
| Pop letter on backtrack. | 回溯時移除字母。 | Cheat sheet |
| Sample twenty-three gives nine outputs. | "23" 範例會產生九個。 | Cheat sheet |
| Worst branches up to four per level. | 每層最壞 4 分支。 | Cheat sheet |
| Runtime O(4^n * n). | 時間 O(4^n*n)。 | Cheat sheet |
| Stack O(n). | 堆疊 O(n)。 | Cheat sheet |
| Output size dominates overall memory. | 整體記憶體常由輸出主導。 | Cheat sheet |
| Common bug: return [empty string] for empty input. | 常見錯誤：空輸入回 ["" ]。 | Cheat sheet |
| Common bug: wrong mapping for seven nine. | 常見錯誤：7/9 映射寫錯。 | Cheat sheet |
| Mention iterative queue alternative if asked. | 被問可補充迭代 queue 作法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS keypad mapping approach is preserved.
- No hallucinated constraints: ✅ Uses 2-9 mapping and empty-input behavior correctly.
- Language simplicity: ✅ Interview-friendly concise lines with concrete flow.
