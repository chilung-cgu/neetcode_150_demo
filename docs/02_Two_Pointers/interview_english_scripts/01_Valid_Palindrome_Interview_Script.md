# 01 Valid Palindrome — Interview English Script (C++)

> Source aligned with: `docs/02_Two_Pointers/01_Valid_Palindrome.md`

> Quick links: [Source Solution](../01_Valid_Palindrome.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We check whether a string is a palindrome. | 我們要判斷字串是否回文。 | Restatement |
| We ignore non-alphanumeric characters. | 我們忽略非英數字元。 | Restatement |
| We also ignore letter case. | 我們也忽略大小寫差異。 | Restatement |
| I will use two pointers in place. | 我會用原地雙指標。 | Restatement |
| Then I will verify edge cases. | 接著我會驗證邊界案例。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume input uses ASCII characters? | 可以假設輸入是 ASCII 嗎？ | Clarify |
| Should I ignore all punctuation and spaces? | 我應忽略所有標點與空白嗎？ | Clarify |
| Is an empty cleaned string considered palindrome? | 清洗後空字串是否算回文？ | Clarify |
| Do digits compare the same way as letters? | 數字比對規則和字母一樣嗎？ | Clarify |
| Should I optimize for O(1) extra space? | 是否要優先做到 O(1) 額外空間？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline builds a cleaned lowercase string first. | 基線是先建立清洗後小寫字串。 | Approach |
| Then compare it with its reversed copy. | 再和反轉副本比較。 | Approach |
| Time O(n), space O(n). | 時間 O(n)，空間 O(n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I place one pointer at each end. | 我把兩個指標放在頭尾。 | Approach |
| Skip non-alphanumeric characters on both sides. | 兩邊都跳過非英數字元。 | Approach |
| Compare lowercase characters when both are valid. | 兩邊有效時，比較小寫後字元。 | Approach |
| Mismatch means return false immediately. | 不相等就立即回傳 false。 | Approach |
| Finish scan means return true. | 掃描完成就回傳 true。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I set left to zero and right to n minus one. | 先把 left 設 0、right 設 n-1。 | Coding |
| While left is smaller than right, I keep scanning. | 當 left 小於 right 就持續掃描。 | Coding |
| I move left forward until it is alphanumeric. | 我讓 left 前進到英數字元。 | Coding |
| I move right backward until it is alphanumeric. | 我讓 right 後退到英數字元。 | Coding |
| Then I compare lowercase forms of both characters. | 然後比較兩邊字元的小寫形式。 | Coding |
| If they differ, I return false. | 若不同，我回傳 false。 | Coding |
| Otherwise I move both pointers inward. | 否則我讓兩邊指標往內縮。 | Coding |
| If loop ends, I return true. | 若迴圈結束，我回傳 true。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run A man, a plan, a canal Panama. | 我手跑 A man, a plan, a canal Panama。 | Dry-run |
| Left starts at A and right starts at a. | left 從 A 開始，right 從 a 開始。 | Dry-run |
| Both become lowercase and match. | 兩邊轉小寫後相同。 | Dry-run |
| Pointers skip spaces and punctuation. | 指標會跳過空白和標點。 | Dry-run |
| Next valid pairs keep matching. | 接下來有效字元配對持續相同。 | Dry-run |
| No mismatch appears before pointers cross. | 在指標交錯前都沒出現不相等。 | Dry-run |
| So the function returns true. | 所以函式回傳 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: s equals a single letter, expect true. | 案例一：單一字母，預期 true。 | Edge test |
| Case two: s equals punctuation only, expect true. | 案例二：只有標點，預期 true。 | Edge test |
| Case three: s equals race a car, expect false. | 案例三：race a car，預期 false。 | Edge test |
| Case four: mixed letters and digits still works. | 案例四：字母與數字混合仍可處理。 | Edge test |
| Case five: very long string with many symbols. | 案例五：含大量符號的長字串。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each pointer moves only toward the center. | 每個指標都只會往中心移動。 | Complexity |
| No character is processed too many times. | 沒有字元會被過度重複處理。 | Complexity |
| Therefore total work is linear in input length. | 因此總工作量對長度是線性。 | Complexity |
| We only store a few pointer variables. | 我們只儲存少量指標變數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate ignore rules first. | 我先重述忽略規則。 | If stuck |
| I will handle cleaning during pointer moves. | 我會在指標移動時完成清洗。 | If stuck |
| I can show brute force then optimize. | 我可先講基線再優化。 | If stuck |
| I forgot one helper API name. | 我一時忘了某個 helper API。 | If stuck |
| The pointer logic is still clear. | 但雙指標邏輯仍清楚。 | If stuck |
| Thanks, I will adjust this condition. | 謝謝，我會調整這個條件。 | If stuck |
| I found the mismatch check bug. | 我找到比對條件的 bug。 | If stuck |
| Let me rerun one sample quickly. | 我快速重跑一個範例。 | If stuck |
| Now the result is consistent. | 現在結果一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| It ignores non-alphanumeric and letter case correctly. | 它能正確忽略非英數與大小寫。 | Wrap-up |
| I verified both positive and negative examples. | 我驗證了正反兩種案例。 | Wrap-up |
| Time is O(n), extra space O(1). | 時間 O(n)，額外空間 O(1)。 | Wrap-up |
| I can discuss Unicode considerations if needed. | 需要的話我可補充 Unicode 考量。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate palindrome with ignore rules. | 重述含忽略規則的回文定義。 | Cheat sheet |
| Ask about character set assumption. | 詢問字元集假設。 | Cheat sheet |
| Baseline uses cleaned string and reverse. | 基線是清洗字串加反轉。 | Cheat sheet |
| Baseline space is O(n). | 基線空間是 O(n)。 | Cheat sheet |
| Optimized uses two pointers in place. | 優化用原地雙指標。 | Cheat sheet |
| Skip invalid chars on left side. | 跳過左側無效字元。 | Cheat sheet |
| Skip invalid chars on right side. | 跳過右側無效字元。 | Cheat sheet |
| Compare lowercase valid chars. | 比較小寫後有效字元。 | Cheat sheet |
| Mismatch means false immediately. | 不匹配就立即 false。 | Cheat sheet |
| Otherwise move inward. | 否則雙指標內縮。 | Cheat sheet |
| Crossed pointers means true. | 指標交錯代表 true。 | Cheat sheet |
| Dry-run Panama sample. | 手跑 Panama 範例。 | Cheat sheet |
| Test punctuation-only input. | 測試只有標點輸入。 | Cheat sheet |
| Test non-palindrome phrase. | 測試非回文字串。 | Cheat sheet |
| Mention O(n) time. | 提到 O(n) 時間。 | Cheat sheet |
| Mention O(1) extra space. | 提到 O(1) 額外空間。 | Cheat sheet |
| Keep speaking each pointer move. | 每次指標移動都口述。 | Cheat sheet |
| If stuck, restate ignore rules. | 卡住時重述忽略規則。 | Cheat sheet |
| End with concise correctness claim. | 以精簡正確性結論收尾。 | Cheat sheet |
| Invite follow-up questions. | 邀請後續提問。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ In-place two-pointer approach is preserved.
- No hallucinated constraints: ✅ Unclear assumptions are asked in clarification lines.
- Language simplicity: ✅ Short spoken English for interview use.
