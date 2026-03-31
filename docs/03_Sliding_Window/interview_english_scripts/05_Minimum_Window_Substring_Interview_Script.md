# 05 Minimum Window Substring — Interview English Script (C++)

> Source aligned with: `docs/03_Sliding_Window/05_Minimum_Window_Substring.md`

> Quick links: [Source Solution](../05_Minimum_Window_Substring.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We need the shortest substring in s covering all chars in t. | 我們要找 s 中最短且覆蓋 t 的子字串。 | Restatement |
| Character multiplicity in t must be respected. | t 的重複字元數量也要滿足。 | Restatement |
| If no valid window exists, return empty string. | 若無合法視窗，回傳空字串。 | Restatement |
| I will use sliding window with frequency maps. | 我會用頻率表 sliding window。 | Restatement |
| Then I will shrink greedily when window is valid. | 視窗合法時會貪心收縮。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are strings case-sensitive in matching? | 比對時大小寫是否有區分？ | Clarify |
| Should I return empty string when t cannot be covered? | 若無法覆蓋 t，是否回傳空字串？ | Clarify |
| If multiple minimum windows exist, any one is fine? | 若有多個最短視窗，任一個都可嗎？ | Clarify |
| Is O(n) window solution expected due to large lengths? | 因長度大，是否預期 O(n) 視窗法？ | Clarify |
| Can I implement with array(ASCII) or unordered_map? | 可用 ASCII 陣列或 unordered_map 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline enumerates all substrings of s. | 基線是枚舉 s 的所有子字串。 | Approach |
| For each substring, verify it covers t counts. | 每段都檢查是否覆蓋 t 的頻率。 | Approach |
| Time is at least quadratic and too slow. | 時間至少平方級，會太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build target frequency map from t. | 先從 t 建立目標頻率表。 | Approach |
| Expand right pointer to collect required characters. | 右指標擴張以蒐集所需字元。 | Approach |
| Track have and need for satisfied unique chars. | 用 have/need 追蹤已滿足種類數。 | Approach |
| When have equals need, shrink left to minimize window. | have==need 時左縮以最小化視窗。 | Approach |
| Record best range during each valid phase. | 在每次合法區間更新最佳範圍。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I build countT and initialize window map. | 先建立 countT 並初始化 window map。 | Coding |
| I set have to zero and need to countT size. | 我把 have 設 0，need 設 countT 大小。 | Coding |
| Expand right, add s[right] to window counts. | 擴張 right，將 s[right] 加入視窗統計。 | Coding |
| If one char just meets target count, increment have. | 若某字元剛好達標，have 加一。 | Coding |
| While have equals need, current window is valid. | 當 have==need，當前視窗合法。 | Coding |
| Update best length and best boundaries. | 更新最佳長度與最佳邊界。 | Coding |
| Then remove s[left], and if requirement breaks, decrement have. | 接著移除 s[left]，若失衡則 have 減一。 | Coding |
| Move left forward and continue scanning. | left 前進，持續掃描。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s equals ADOBECODEBANC, t equals ABC. | 我手跑 s=ADOBECODEBANC，t=ABC。 | Dry-run |
| Expanding right first finds a valid window ADOBEC. | 先擴張 right，找到第一個合法窗 ADOBEC。 | Dry-run |
| Since window is valid, I shrink left to reduce size. | 視窗合法後，開始左縮減少長度。 | Dry-run |
| Later another valid region appears near BANC. | 後段會出現另一個合法區域接近 BANC。 | Dry-run |
| Shrinking there gives exactly BANC. | 在那段收縮後得到 BANC。 | Dry-run |
| Its length is four, smaller than previous candidates. | 長度 4，比先前候選更短。 | Dry-run |
| Final answer is BANC. | 最終答案是 BANC。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: t longer than s should return empty. | 案例一：t 比 s 長應回傳空字串。 | Edge test |
| Case two: exact match s equals t. | 案例二：s 與 t 完全相同。 | Edge test |
| Case three: repeated target chars like t = AABC. | 案例三：目標有重複字元如 t=AABC。 | Edge test |
| Case four: no overlap between s and t. | 案例四：s 與 t 完全無交集。 | Edge test |
| Case five: multiple valid windows with same min length. | 案例五：多個同長最短合法視窗。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n + m). | 時間是 O(n + m)。 | Complexity |
| Extra space is O(k) for distinct needed chars. | 額外空間是 O(k)，k 為需要字元種類數。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Building target counts costs O(m). | 建立目標頻率需 O(m)。 | Complexity |
| Left and right pointers each move forward at most n times. | left 與 right 各自最多前進 n 次。 | Complexity |
| So total scanning work is linear in s length. | 因此掃描工作量對 s 是線性。 | Complexity |
| Hash/array maps store only required character states. | map/array 只儲存所需字元狀態。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate have versus need logic. | 我先重述 have 與 need 邏輯。 | If stuck |
| Window is valid only when have equals need. | 只有 have==need 視窗才合法。 | If stuck |
| I should update answer before popping left char. | 移除左字元前要先更新答案。 | If stuck |
| I can explain brute force baseline quickly. | 我可先快速講暴力基線。 | If stuck |
| Then I switch to linear sliding window. | 再切回線性 sliding window。 | If stuck |
| Thanks, I found count decrement bug. | 謝謝，我找到 count 遞減錯誤。 | If stuck |
| Let me rerun ADOBECODEBANC example. | 我重跑 ADOBECODEBANC 範例。 | If stuck |
| Now shortest window updates correctly. | 現在最短視窗更新正確。 | If stuck |
| Final output is stable at BANC. | 最終輸出穩定為 BANC。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n + m). | 時間是 O(n + m)。 | Wrap-up |
| Extra space is O(k). | 額外空間是 O(k)。 | Wrap-up |
| I can compare array and hashmap implementations if needed. | 若需要我可比較 array 與 hashmap 實作。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate minimum covering window goal. | 重述最小覆蓋視窗目標。 | Cheat sheet |
| Mention multiplicity in t matters. | 提到 t 的重複數量也重要。 | Cheat sheet |
| Brute force checks all substrings. | 暴力法檢查所有子字串。 | Cheat sheet |
| Brute force is too slow. | 暴力法太慢。 | Cheat sheet |
| Build target frequency map. | 建立目標頻率表。 | Cheat sheet |
| Use have and need counters. | 使用 have 與 need 計數。 | Cheat sheet |
| Expand right to satisfy requirements. | 擴張 right 以滿足需求。 | Cheat sheet |
| When valid, shrink left greedily. | 合法後貪心左縮。 | Cheat sheet |
| Update best range before breaking validity. | 破壞合法前更新最佳範圍。 | Cheat sheet |
| Dry-run ADOBECODEBANC with ABC. | 手跑 ADOBECODEBANC 與 ABC。 | Cheat sheet |
| Confirm best answer is BANC. | 確認最佳答案是 BANC。 | Cheat sheet |
| Test impossible case returns empty. | 測無解時回傳空字串。 | Cheat sheet |
| Test repeated target chars case. | 測目標有重複字元案例。 | Cheat sheet |
| Test exact-match case. | 測完全相等案例。 | Cheat sheet |
| Report O(n+m) runtime. | 報告 O(n+m) 時間。 | Cheat sheet |
| Report O(k) extra space. | 報告 O(k) 額外空間。 | Cheat sheet |
| Mention ASCII-array alternative. | 提到 ASCII 陣列替代作法。 | Cheat sheet |
| If stuck, recheck have/need updates. | 卡住時重檢 have/need 更新。 | Cheat sheet |
| Re-run sample after fixes. | 修正後重跑範例。 | Cheat sheet |
| End with concise result summary. | 以精簡結果總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ have/need sliding-window logic is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
