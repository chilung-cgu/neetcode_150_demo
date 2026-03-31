# 01 01. Valid Parentheses — Interview English Script (C++)

> Source aligned with: `docs/04_Stack/01_Valid_Parentheses.md`

> Quick links: [Source Solution](../01_Valid_Parentheses.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We are given a string of bracket characters. | 我們拿到一個由括號字元組成的字串。 | Restatement |
| We must check whether it is valid. | 我們要判斷它是否有效。 | Restatement |
| Valid means correct type and correct closing order. | 有效代表類型正確且關閉順序正確。 | Restatement |
| I will use a stack for open brackets. | 我會用 stack 存左括號。 | Restatement |
| Final stack must be empty for a valid string. | 最後 stack 必須為空才算有效。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can input contain only these six bracket symbols? | 輸入是否只含六種括號符號？ | Clarify |
| Is string length at least one by constraints? | 根據限制，長度是否至少 1？ | Clarify |
| Should unmatched closing bracket return false immediately? | 遇到無對應右括號可立即 false 嗎？ | Clarify |
| Do we return only boolean, no error detail? | 是否只需回傳布林值，不要錯誤細節？ | Clarify |
| Is O(n) expected for this validation? | 這題是否預期 O(n) 驗證？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline repeatedly removes pairs like () [] {}. | 基線是不斷刪除 () [] {} 配對。 | Approach |
| If no reduction is possible and string remains, invalid. | 若無法再刪除且字串仍存在，就無效。 | Approach |
| This is roughly O(n^2) due to repeated scans. | 因反覆掃描，時間大約 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Push every opening bracket onto stack. | 每個左括號都 push 到 stack。 | Approach |
| On closing bracket, stack top must match its type. | 遇到右括號時，top 必須同類型配對。 | Approach |
| If stack is empty or mismatch, return false. | 若 stack 空或型別不合，直接 false。 | Approach |
| After full scan, stack must be empty. | 全部掃描後 stack 必須為空。 | Approach |
| This gives O(n) time and O(n) space worst-case. | 最差可達 O(n) 時間與 O(n) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create an empty stack of chars. | 先建立空的 char stack。 | Coding |
| Then I scan the string from left to right. | 然後由左到右掃描字串。 | Coding |
| If current char is opening bracket, I push it. | 若當前是左括號，就 push。 | Coding |
| Otherwise it is closing bracket, so I check stack top. | 否則是右括號，要檢查 stack top。 | Coding |
| If stack is empty, return false immediately. | 若 stack 為空，立即回傳 false。 | Coding |
| If types match, pop; else return false. | 型別匹配就 pop，不匹配就 false。 | Coding |
| Continue until all characters are processed. | 持續直到所有字元處理完。 | Coding |
| Return whether stack is empty at the end. | 最後回傳 stack 是否為空。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the sample string (). | 我手跑範例字串 ()。 | Dry-run |
| Read left parenthesis, push it to stack. | 讀到左括號，push 到 stack。 | Dry-run |
| Read right parenthesis, top is matching left one. | 讀到右括號，top 剛好是對應左括號。 | Dry-run |
| Pop that opening bracket. | 把那個左括號 pop 掉。 | Dry-run |
| End of scan with empty stack. | 掃描結束且 stack 為空。 | Dry-run |
| So the string is valid. | 因此字串有效。 | Dry-run |
| Final answer is true. | 最終答案是 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single opening bracket like (. | 案例一：只有一個左括號如 (。 | Edge test |
| Case two: single closing bracket like ). | 案例二：只有一個右括號如 )。 | Edge test |
| Case three: nested valid pattern like {[()]}. | 案例三：巢狀合法如 {[()]}。 | Edge test |
| Case four: wrong order pattern like ([)]. | 案例四：順序錯誤如 ([)]。 | Edge test |
| Case five: leftover opening brackets like (() . | 案例五：有殘留左括號如 (()。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(n) in worst case. | 最差額外空間是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each character is pushed at most once. | 每個字元最多只會被 push 一次。 | Complexity |
| Each pushed bracket is popped at most once. | 每個進 stack 的括號最多 pop 一次。 | Complexity |
| So total stack operations are linear. | 因此 stack 總操作是線性的。 | Complexity |
| Worst case all openings keeps stack size n. | 最差全是左括號時，stack 大小為 n。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate matching rule first. | 我先重述括號匹配規則。 | If stuck |
| Closing bracket must match latest opening bracket. | 右括號要配最近的左括號。 | If stuck |
| If stack is empty on closing, it is invalid. | 若遇右括號時 stack 為空，就無效。 | If stuck |
| I can show brute force idea briefly. | 我可先簡述暴力想法。 | If stuck |
| Then I switch back to stack method. | 再切回 stack 方法。 | If stuck |
| Thanks, I found my mismatch condition bug. | 謝謝，我找到型別比對 bug。 | If stuck |
| Let me rerun one invalid sample. | 我重跑一個無效範例。 | If stuck |
| Now wrong-order case fails correctly. | 現在順序錯誤案例可正確失敗。 | If stuck |
| Final logic is consistent now. | 現在整體邏輯一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(n) worst case. | 最差額外空間是 O(n)。 | Wrap-up |
| I can discuss map-based matching variant if needed. | 若需要我可補充 map 配對版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate bracket-validity goal. | 重述括號有效性目標。 | Cheat sheet |
| Mention type and order both matter. | 提到類型與順序都重要。 | Cheat sheet |
| Brute force repeatedly removes pairs. | 暴力法反覆刪配對。 | Cheat sheet |
| Better method uses stack. | 更好方法是 stack。 | Cheat sheet |
| Push opening brackets. | 左括號就 push。 | Cheat sheet |
| On closing, stack must be non-empty. | 右括號時 stack 不能空。 | Cheat sheet |
| Top type must match current closing. | top 型別要與當前右括號匹配。 | Cheat sheet |
| Match then pop, otherwise false. | 匹配就 pop，不然 false。 | Cheat sheet |
| End scan and check stack empty. | 掃描結束後檢查 stack 是否為空。 | Cheat sheet |
| Dry-run sample (). | 手跑範例 ()。 | Cheat sheet |
| Dry-run invalid sample ([)]. | 手跑無效範例 ([)]。 | Cheat sheet |
| Test single opening bracket. | 測只有左括號案例。 | Cheat sheet |
| Test single closing bracket. | 測只有右括號案例。 | Cheat sheet |
| Test nested valid case. | 測巢狀合法案例。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(n) worst-case space. | 報告 O(n) 最差空間。 | Cheat sheet |
| Mention early return on mismatch. | 提到不匹配可提前返回。 | Cheat sheet |
| If stuck, recheck match table. | 卡住時重檢配對表。 | Cheat sheet |
| Re-run dry-run after fix. | 修正後重新手跑。 | Cheat sheet |
| End with concise boolean result. | 以精簡布林結果收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Stack matching logic and empty-stack check are preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced via clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
