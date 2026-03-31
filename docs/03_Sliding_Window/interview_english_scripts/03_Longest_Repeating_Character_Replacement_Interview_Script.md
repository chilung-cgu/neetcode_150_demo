# 03 Longest Repeating Character Replacement — Interview English Script (C++)

> Source aligned with: `docs/03_Sliding_Window/03_Longest_Repeating_Character_Replacement.md`

> Quick links: [Source Solution](../03_Longest_Repeating_Character_Replacement.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We can replace at most k characters. | 我們最多可替換 k 個字元。 | Restatement |
| Goal is longest substring of same letters after replacement. | 目標是替換後最長同字母子字串。 | Restatement |
| We only need the maximum length. | 我們只要最大長度。 | Restatement |
| I will use sliding window with frequency counts. | 我會用 sliding window 加頻率統計。 | Restatement |
| Key check is window size minus maxFreq. | 關鍵判斷是視窗長度減 maxFreq。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume uppercase English letters only? | 可以假設只含大寫英文字母嗎？ | Clarify |
| Is k allowed to be zero? | k 可以是 0 嗎？ | Clarify |
| If k is large, can answer be full string length? | 若 k 很大，答案可等於整段長度嗎？ | Clarify |
| Is O(n) expected for input up to 1e5? | 對 1e5 輸入是否要求 O(n)？ | Clarify |
| Do we return length only, not the substring? | 只回傳長度，不回傳內容對嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline enumerates all substrings. | 基線是枚舉所有子字串。 | Approach |
| For each one, find most frequent char and replacements needed. | 每段找最高頻字元與所需替換數。 | Approach |
| Time is at least O(n^2), often O(n^3). | 時間至少 O(n^2)，常見是 O(n^3)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Keep a window and count each letter frequency. | 維護視窗並統計每個字母頻率。 | Approach |
| Track maxFreq as highest count in window history. | 用 maxFreq 記錄視窗歷史最高頻率。 | Approach |
| Needed replacements are windowLen minus maxFreq. | 所需替換數是 windowLen-maxFreq。 | Approach |
| If needed replacements exceed k, shrink from left. | 若替換數超過 k，就從左側收縮。 | Approach |
| This yields O(n) time and O(1) space. | 這可達 O(n) 時間與 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize count array, left, maxFreq, and answer. | 先初始化 count、left、maxFreq、answer。 | Coding |
| Then I expand right and add s[right] to count. | 接著擴張 right，計入 s[right]。 | Coding |
| Update maxFreq with this character count. | 用該字元次數更新 maxFreq。 | Coding |
| Compute window length as right minus left plus one. | 視窗長度是 right-left+1。 | Coding |
| If windowLen minus maxFreq is greater than k, shrink left. | 若 windowLen-maxFreq>k，就收縮 left。 | Coding |
| Shrink means decrement count of s[left], then left plus one. | 收縮時先減 s[left]，再 left++。 | Coding |
| After adjustment, update best length. | 調整後更新最大長度。 | Coding |
| At end, return the best length. | 最後回傳最佳長度。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s equals ABAB and k equals 2. | 我手跑 s=ABAB，k=2。 | Dry-run |
| Expand window to include A, then AB. | 視窗先擴到 A，再到 AB。 | Dry-run |
| maxFreq becomes 1 then 1, replacements stay within k. | maxFreq 先是 1，再是 1，替換數仍在 k 內。 | Dry-run |
| After full window ABAB, maxFreq is 2. | 視窗到 ABAB 時，maxFreq 是 2。 | Dry-run |
| windowLen is 4, replacements needed is 2. | 視窗長度 4，所需替換數是 2。 | Dry-run |
| This is valid because k is 2. | 這是合法的，因為 k=2。 | Dry-run |
| Final answer is 4. | 最終答案是 4。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single letter string. | 案例一：單字元字串。 | Edge test |
| Case two: k equals zero with mixed letters. | 案例二：k=0 且字元混合。 | Edge test |
| Case three: all same letters should return full length. | 案例三：全相同字母應回傳全長。 | Edge test |
| Case four: k larger than needed replacements. | 案例四：k 大於所需替換數。 | Edge test |
| Case five: alternating letters like ABABAB. | 案例五：交錯字串如 ABABAB。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Right pointer moves across string once. | 右指標只會走過字串一遍。 | Complexity |
| Left pointer also moves forward only. | 左指標也只會向前移動。 | Complexity |
| Count array size is fixed to alphabet size. | count 陣列大小固定為字母表大小。 | Complexity |
| Therefore runtime is linear and space constant. | 因此時間線性、空間常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate replacement formula quickly. | 我先快速重述替換公式。 | If stuck |
| It is window length minus maxFreq. | 就是視窗長度減 maxFreq。 | If stuck |
| If this exceeds k, I must shrink. | 若超過 k，就必須收縮。 | If stuck |
| I can explain brute force first if needed. | 若需要我可先解釋暴力法。 | If stuck |
| Then I switch back to O(n) window. | 再切回 O(n) 視窗法。 | If stuck |
| Thanks, I found incorrect shrink condition. | 謝謝，我找到錯誤的收縮條件。 | If stuck |
| Let me rerun ABAB sample. | 我重跑 ABAB 範例。 | If stuck |
| Now window validity logic is correct. | 現在視窗合法判斷正確。 | If stuck |
| Result length is stable. | 結果長度已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can discuss why maxFreq need not decrease. | 若需要我可說明為何 maxFreq 不必遞減。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate longest repeatable substring goal. | 重述可替換後最長同字串目標。 | Cheat sheet |
| Mention at most k replacements. | 提到最多替換 k 次。 | Cheat sheet |
| Brute force checks all substrings. | 暴力法檢查所有子字串。 | Cheat sheet |
| Brute force is too slow. | 暴力法太慢。 | Cheat sheet |
| Use sliding window with count array. | 使用 sliding window 與 count 陣列。 | Cheat sheet |
| Track maxFreq in window history. | 追蹤視窗歷史 maxFreq。 | Cheat sheet |
| Compute replacements as len-maxFreq. | 以 len-maxFreq 算替換需求。 | Cheat sheet |
| If replacements exceed k, shrink left. | 若需求超過 k，就收縮 left。 | Cheat sheet |
| Update best length each step. | 每步更新最佳長度。 | Cheat sheet |
| Dry-run ABAB with k=2. | 手跑 ABAB 且 k=2。 | Cheat sheet |
| Confirm answer is 4. | 確認答案是 4。 | Cheat sheet |
| Test k=0 case. | 測 k=0 案例。 | Cheat sheet |
| Test all-same letters case. | 測全同字母案例。 | Cheat sheet |
| Test alternating letters case. | 測交錯字母案例。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(1) extra space. | 報告 O(1) 額外空間。 | Cheat sheet |
| Mention maxFreq optimization point. | 提到 maxFreq 優化重點。 | Cheat sheet |
| If stuck, restate shrink rule. | 卡住時重述收縮規則。 | Cheat sheet |
| Re-run sample after fixes. | 修正後重跑範例。 | Cheat sheet |
| End with concise summary. | 以精簡總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sliding-window validity formula is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
