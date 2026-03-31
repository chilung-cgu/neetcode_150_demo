# 02 Longest Substring Without Repeating Characters — Interview English Script (C++)

> Source aligned with: `docs/03_Sliding_Window/02_Longest_Substring_Without_Repeating.md`

> Quick links: [Source Solution](../02_Longest_Substring_Without_Repeating.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We need the longest substring with unique characters. | 我們要找無重複字元的最長子字串。 | Restatement |
| Substring means characters must be contiguous. | substring 代表字元必須連續。 | Restatement |
| We return the maximum length, not the string. | 我們回傳最大長度，不是字串本體。 | Restatement |
| I will use sliding window with a set. | 我會用 sliding window 搭配 set。 | Restatement |
| Then I will keep window always duplicate-free. | 然後維持視窗始終無重複。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can input include any ASCII characters? | 輸入是否可能是任意 ASCII 字元？ | Clarify |
| For empty string, should answer be zero? | 空字串是否回傳 0？ | Clarify |
| Do we only need length, not substring itself? | 只需長度，不需回傳內容對嗎？ | Clarify |
| Is O(n) expected due to large input size? | 由於輸入大，是否預期 O(n)？ | Clarify |
| Can I present set or last-index map variant? | 我可說明 set 或 last-index 版本嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline enumerates all substrings i to j. | 基線是枚舉所有 i 到 j 子字串。 | Approach |
| For each substring, check duplicate characters. | 對每個子字串檢查是否有重複字元。 | Approach |
| Time O(n^3) naively, too slow. | 天真作法時間 O(n^3)，太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Keep a window [left, right] with unique chars only. | 維護 [left,right] 視窗且只含唯一字元。 | Approach |
| Expand right by adding one character each step. | 每步向右擴張一個字元。 | Approach |
| If duplicate appears, shrink left until valid. | 若出現重複，左邊收縮到合法。 | Approach |
| Update max length after each valid expansion. | 每次合法擴張後更新最大長度。 | Approach |
| Total work is linear because each index moves once. | 因每個索引最多進出一次，總工作量線性。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize left and an empty hash set. | 先初始化 left 與空的 hash set。 | Coding |
| Then I iterate right from zero to end. | 接著 right 從 0 走到尾端。 | Coding |
| Before insertion, while s[right] exists, remove s[left]. | 加入前若 s[right] 已存在，就移除 s[left]。 | Coding |
| Move left forward until duplicate is removed. | left 持續右移直到重複消失。 | Coding |
| Insert s[right] into the set. | 把 s[right] 放進 set。 | Coding |
| Window is now valid with unique characters. | 此時視窗重新合法且無重複。 | Coding |
| Update answer with right minus left plus one. | 用 right-left+1 更新答案。 | Coding |
| Return the maximum length at the end. | 最後回傳最大長度。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the string abcabcbb. | 我手跑字串 abcabcbb。 | Dry-run |
| Add a, b, c, window length becomes three. | 加入 a,b,c 後視窗長度是 3。 | Dry-run |
| Next char is a, duplicate appears. | 下一個字元是 a，出現重複。 | Dry-run |
| Remove from left until old a is removed. | 從左側移除直到舊 a 被移出。 | Dry-run |
| Continue scanning, max length stays three. | 繼續掃描後最大長度仍是 3。 | Dry-run |
| Later repeated b shrinks window again. | 後續遇到重複 b 又會收縮視窗。 | Dry-run |
| Final answer is 3. | 最終答案是 3。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty string should return zero. | 案例一：空字串應回傳 0。 | Edge test |
| Case two: single character string returns one. | 案例二：單一字元應回傳 1。 | Edge test |
| Case three: all same like aaaa returns one. | 案例三：全相同如 aaaa 回傳 1。 | Edge test |
| Case four: all unique string returns full length. | 案例四：全唯一字串回傳整段長度。 | Edge test |
| Case five: pattern like dvdf verifies proper shrink. | 案例五：如 dvdf 驗證正確收縮。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Space is O(min(n,charset)). | 空間是 O(min(n,字元集大小))。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Right pointer visits each index once. | 右指標每個索引只造訪一次。 | Complexity |
| Left pointer also only moves forward. | 左指標也只會向前移動。 | Complexity |
| So total pointer moves are linear. | 所以總移動次數是線性。 | Complexity |
| Set stores only current unique window characters. | set 只儲存目前視窗的唯一字元。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate substring means contiguous. | 我先重述 substring 要連續。 | If stuck |
| Duplicate means window is invalid now. | 一旦重複，視窗就暫時非法。 | If stuck |
| I should shrink before expanding further. | 我應先收縮再繼續擴張。 | If stuck |
| I can show brute force first if needed. | 若需要我可先講暴力法。 | If stuck |
| Then I return to O(n) window method. | 再回到 O(n) 視窗法。 | If stuck |
| Thanks, I found missing while loop. | 謝謝，我找到缺少的 while 迴圈。 | If stuck |
| Let me rerun abcabcbb quickly. | 我快速重跑 abcabcbb。 | If stuck |
| Now duplicate handling is correct. | 現在重複處理正確。 | If stuck |
| Final max length is stable. | 最終最大長度穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Space is O(min(n,charset)). | 空間是 O(min(n,字元集大小))。 | Wrap-up |
| I can discuss last-index jump optimization if needed. | 若需要我可補充 last-index 跳躍優化。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate longest unique substring goal. | 重述最長無重複子字串目標。 | Cheat sheet |
| Emphasize substring must be contiguous. | 強調 substring 必須連續。 | Cheat sheet |
| Brute force checks all substrings. | 暴力法檢查所有子字串。 | Cheat sheet |
| Brute force is too slow. | 暴力法太慢。 | Cheat sheet |
| Use sliding window plus set. | 使用 sliding window 加 set。 | Cheat sheet |
| Expand right pointer step by step. | 逐步擴張右指標。 | Cheat sheet |
| If duplicate appears, shrink left. | 若重複出現，收縮左指標。 | Cheat sheet |
| Keep window always duplicate-free. | 保持視窗始終無重複。 | Cheat sheet |
| Update max length on valid window. | 視窗合法時更新最大長度。 | Cheat sheet |
| Dry-run abcabcbb sample. | 手跑 abcabcbb 範例。 | Cheat sheet |
| Verify answer is 3. | 驗證答案為 3。 | Cheat sheet |
| Test empty string case. | 測空字串案例。 | Cheat sheet |
| Test all-same string case. | 測全相同字串案例。 | Cheat sheet |
| Test all-unique string case. | 測全唯一字串案例。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report set space usage. | 報告 set 空間使用。 | Cheat sheet |
| Mention map jump variant as follow-up. | 提及 map 跳躍版本作延伸。 | Cheat sheet |
| If stuck, recheck shrink condition. | 卡住時重檢收縮條件。 | Cheat sheet |
| Re-run sample after fix. | 修正後重跑範例。 | Cheat sheet |
| End with concise summary. | 以精簡總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sliding window with duplicate-removal loop is preserved.
- No hallucinated constraints: ✅ Assumptions are handled in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
