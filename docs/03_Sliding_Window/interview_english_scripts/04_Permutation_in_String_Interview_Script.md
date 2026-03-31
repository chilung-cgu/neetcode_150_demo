# 04 Permutation in String — Interview English Script (C++)

> Source aligned with: `docs/03_Sliding_Window/04_Permutation_in_String.md`

> Quick links: [Source Solution](../04_Permutation_in_String.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We check whether s2 contains a permutation of s1. | 我們檢查 s2 是否含有 s1 的排列。 | Restatement |
| That means some window has identical character counts. | 也就是某個視窗字元頻率完全相同。 | Restatement |
| Window length must equal s1 length. | 視窗長度必須等於 s1 長度。 | Restatement |
| I will use fixed-size sliding window. | 我會用固定大小 sliding window。 | Restatement |
| Frequency arrays make comparison efficient. | 用頻率陣列讓比較更有效率。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume both strings contain lowercase letters only? | 可以假設兩字串只含小寫嗎？ | Clarify |
| If s1 is longer than s2, return false directly? | 若 s1 比 s2 長，是否可直接 false？ | Clarify |
| Do we return boolean only? | 只需要回傳布林值嗎？ | Clarify |
| Is O(n) expected instead of generating permutations? | 是否預期 O(n) 而非產生所有排列？ | Clarify |
| Can I discuss both direct compare and matches-count variants? | 我可說明直接比較與 matches 版本嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline generates all permutations of s1. | 基線是產生 s1 的所有排列。 | Approach |
| Then search each permutation inside s2. | 再逐一去 s2 內搜尋。 | Approach |
| This is factorial and infeasible. | 這是階乘等級，實務上不可行。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build frequency count for s1 first. | 先建立 s1 的頻率統計。 | Approach |
| Keep a fixed-size window on s2 with same length. | 在 s2 維持同長度固定視窗。 | Approach |
| Slide one step: add right char and remove left char. | 每次滑動：加右字元、減左字元。 | Approach |
| Compare frequencies or maintain matches count. | 可全比較頻率或維護 matches 計數。 | Approach |
| This gives linear time with constant alphabet space. | 這可達線性時間與常數字母空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I handle quick fail when len(s1) > len(s2). | 先處理 len(s1)>len(s2) 的快速失敗。 | Coding |
| I build two arrays of size 26. | 我建立兩個長度 26 的陣列。 | Coding |
| Fill s1 count and initial window count. | 填好 s1 統計與初始視窗統計。 | Coding |
| If initial counts match, return true. | 若初始統計相同，直接回傳 true。 | Coding |
| Then slide window by one each iteration. | 接著每輪把視窗右移一步。 | Coding |
| Add incoming char count and remove outgoing char count. | 增加進入字元、減少移出字元。 | Coding |
| If counts match at any step, return true. | 任一步統計相同就回傳 true。 | Coding |
| If loop ends without match, return false. | 迴圈結束仍無命中就回傳 false。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s1 equals ab, s2 equals eidbaooo. | 我手跑 s1=ab、s2=eidbaooo。 | Dry-run |
| Window size is fixed at two. | 視窗大小固定是 2。 | Dry-run |
| First windows ei and id do not match counts. | 前幾個視窗 ei、id 頻率都不匹配。 | Dry-run |
| When window reaches db, still no match. | 視窗到 db 時仍不匹配。 | Dry-run |
| Next window is ba, counts equal to s1. | 下一窗 ba，頻率與 s1 相同。 | Dry-run |
| So we can return true immediately. | 因此可立即回傳 true。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: s1 longer than s2 should be false. | 案例一：s1 長於 s2 應為 false。 | Edge test |
| Case two: exact same strings should be true. | 案例二：兩字串完全相同應為 true。 | Edge test |
| Case three: repeated chars like s1 = aab. | 案例三：含重複字元如 s1=aab。 | Edge test |
| Case four: all same letters in both strings. | 案例四：兩者都為同字母重複。 | Edge test |
| Case five: no valid permutation anywhere. | 案例五：整段都沒有合法排列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Window slides across s2 once. | 視窗只需掃過 s2 一次。 | Complexity |
| Each slide updates constant number of counters. | 每次滑動只更新常數個計數器。 | Complexity |
| Alphabet size is fixed at 26. | 字母表大小固定為 26。 | Complexity |
| Therefore runtime is linear and space constant. | 因此時間線性、空間常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate fixed window size rule. | 我先重述固定視窗大小規則。 | If stuck |
| Window length must equal len(s1). | 視窗長度一定是 len(s1)。 | If stuck |
| I should add one char and remove one char. | 每步要加一個、減一個字元。 | If stuck |
| I can explain brute force quickly first. | 我可先快速說明暴力法。 | If stuck |
| Then switch to O(n) frequency window. | 再切到 O(n) 頻率視窗。 | If stuck |
| Thanks, I found a wrong index update. | 謝謝，我找到索引更新錯誤。 | If stuck |
| Let me rerun the ab/eidbaooo sample. | 我重跑 ab/eidbaooo 範例。 | If stuck |
| Now counts align at window ba. | 現在在 ba 視窗頻率已對齊。 | If stuck |
| The boolean result is stable. | 布林結果已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can discuss matches-count optimization if needed. | 若需要我可補充 matches 計數優化。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate permutation-in-string goal. | 重述字串排列包含目標。 | Cheat sheet |
| Mention fixed window size len(s1). | 提到固定視窗大小 len(s1)。 | Cheat sheet |
| Brute force permutation generation is infeasible. | 暴力排列生成不可行。 | Cheat sheet |
| Use frequency arrays for both strings. | 使用兩組頻率陣列。 | Cheat sheet |
| Initialize first window counts. | 初始化第一個視窗統計。 | Cheat sheet |
| Compare counts for initial window. | 先比較初始視窗頻率。 | Cheat sheet |
| Slide by adding right char. | 右移時加入右字元。 | Cheat sheet |
| Remove outgoing left char. | 同步移除左端字元。 | Cheat sheet |
| Compare counts each step. | 每一步比較頻率。 | Cheat sheet |
| Return true on first match. | 首次匹配就回傳 true。 | Cheat sheet |
| Return false if no window matches. | 若都不匹配就回傳 false。 | Cheat sheet |
| Dry-run ab and eidbaooo. | 手跑 ab 與 eidbaooo。 | Cheat sheet |
| Verify match window is ba. | 驗證命中視窗是 ba。 | Cheat sheet |
| Test s1 longer than s2 case. | 測 s1 長於 s2 案例。 | Cheat sheet |
| Test repeated-char target case. | 測目標含重複字元案例。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(1) extra space. | 報告 O(1) 額外空間。 | Cheat sheet |
| Mention matches-count optimization. | 提到 matches 計數優化。 | Cheat sheet |
| If stuck, recheck window update pair. | 卡住時重檢加減字元配對。 | Cheat sheet |
| End with concise boolean summary. | 以精簡布林結論收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Fixed-size frequency window logic is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
