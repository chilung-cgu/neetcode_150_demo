# 03 Two Sum — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/03_Two_Sum.md`

> Quick links: [Source Solution](../03_Two_Sum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We have nums and a target value. | 我們有 nums 和 target。 | Restatement |
| We need two different indices. | 我們要找兩個不同索引。 | Restatement |
| Their values must sum to target. | 這兩個位置的值相加要等於 target。 | Restatement |
| I will use one-pass hash map. | 我會用一次遍歷 hash map。 | Restatement |
| Then I will test edge cases. | 然後我會測邊界案例。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume exactly one valid answer? | 可以假設剛好一組解嗎？ | Clarify |
| Can nums contain duplicate values? | nums 會有重複值嗎？ | Clarify |
| Can numbers be negative? | 數字可能是負數嗎？ | Clarify |
| Does return order of indices matter? | 回傳索引順序有要求嗎？ | Clarify |
| If no solution exists, return empty list? | 如果無解，回傳空陣列嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline checks every pair i and j. | 基線是檢查每一對 i 與 j。 | Approach |
| If nums[i] plus nums[j] equals target, return them. | 若兩者和等於 target 就回傳。 | Approach |
| Time O(n^2), space O(1). | 時間 O(n^2)、空間 O(1)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I store value to index in a hash map. | 我用 hash map 存值到索引。 | Approach |
| For each value, need equals target minus value. | 每個值對應的 need 是 target 減它。 | Approach |
| If need already exists, I return two indices. | 若 need 已存在，就回傳兩個索引。 | Approach |
| Otherwise I store current value and index. | 否則先存目前值與索引。 | Approach |
| Average time O(n), extra space O(n). | 平均時間 O(n)，額外空間 O(n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create unordered_map<int,int> seen. | 先建立 unordered_map<int,int> seen。 | Coding |
| Then I loop i from zero to nums size. | 然後 i 從 0 走到 nums 長度。 | Coding |
| Current is nums[i], and need is target minus current. | current 是 nums[i]，need 是 target-current。 | Coding |
| I check whether need exists in seen. | 我檢查 seen 裡是否有 need。 | Coding |
| If found, I return seen[need] and i. | 若找到，就回傳 seen[need] 和 i。 | Coding |
| If not found, I store seen[current] equals i. | 若找不到，就存 seen[current]=i。 | Coding |
| This keeps one pass and correct index order. | 這樣維持一次遍歷與正確索引。 | Coding |
| At end, return empty as defensive fallback. | 最後回傳空陣列作保底。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums two, seven, eleven, fifteen. | 我手跑 nums = 2,7,11,15。 | Dry-run |
| Target is nine. | target 是 9。 | Dry-run |
| i zero: current two, need seven, not found. | i=0：current=2，need=7，未找到。 | Dry-run |
| Store value two at index zero. | 儲存數值 2 在索引 0。 | Dry-run |
| i one: current seven, need two, found. | i=1：current=7，need=2，已找到。 | Dry-run |
| Return indices zero and one. | 回傳索引 0 和 1。 | Dry-run |
| Output matches expected answer. | 輸出符合預期答案。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: [3,3], target 6, expect [0,1]. | 案例一：[3,3], target 6，預期 [0,1]。 | Edge test |
| Case two: [0,4,3,0], target 0, expect [0,3]. | 案例二：[0,4,3,0], target 0，預期 [0,3]。 | Edge test |
| Case three: negatives like [-1,-2,-3,-4], target -6. | 案例三：負數如 [-1,-2,-3,-4], target -6。 | Edge test |
| Case four: ensure same index is never reused. | 案例四：確認不會重用同一索引。 | Edge test |
| Case five: if no-solution allowed, return empty. | 案例五：若允許無解，回傳空陣列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Average time is O(n). | 平均時間是 O(n)。 | Complexity |
| Space is O(n) for stored values. | 空間是 O(n)，用來存已看過值。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We iterate through nums exactly one time. | 我們剛好把 nums 走訪一次。 | Complexity |
| Each map lookup and insert is average O(1). | 每次 map 查找與插入平均 O(1)。 | Complexity |
| So total average time is O(n). | 所以總平均時間是 O(n)。 | Complexity |
| Map can hold up to n elements, so space O(n). | map 最多存 n 個元素，所以空間 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me confirm one requirement first. | 我先確認一個需求。 | If stuck |
| I can explain brute force quickly. | 我可以快速說明暴力法。 | If stuck |
| Then I will optimize to hash map. | 然後我會優化成 hash map。 | If stuck |
| I forgot one syntax detail only. | 我只是一時忘了語法細節。 | If stuck |
| The core logic is still correct. | 但核心邏輯仍是正確的。 | If stuck |
| Thanks for the hint, I will adjust. | 謝謝提示，我會調整。 | If stuck |
| I found the bug and fixed it. | 我找到 bug 並修好了。 | If stuck |
| Let me rerun the sample now. | 我現在重跑範例。 | If stuck |
| The result is consistent now. | 現在結果一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified both normal and edge cases. | 我驗證了正常與邊界案例。 | Wrap-up |
| One-pass hash map gives O(n) average time. | 一次遍歷 hash map 可達 O(n) 平均時間。 | Wrap-up |
| Space is O(n), which is acceptable here. | 空間是 O(n)，在這題可接受。 | Wrap-up |
| I can discuss sorted-array variant if needed. | 若需要我可補充排序陣列變體。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate nums, target, and index output. | 重述 nums、target 與索引輸出。 | Cheat sheet |
| Ask if exactly one answer exists. | 問是否保證唯一解。 | Cheat sheet |
| Mention brute force O(n^2). | 提到暴力法 O(n^2)。 | Cheat sheet |
| Introduce one-pass hash map. | 引入一次遍歷 hash map。 | Cheat sheet |
| Store value to index mapping. | 儲存數值到索引映射。 | Cheat sheet |
| Need equals target minus current. | need = target - current。 | Cheat sheet |
| Check need before storing current. | 先檢查 need 再儲存 current。 | Cheat sheet |
| Found need, return two indices. | 找到 need 就回傳兩索引。 | Cheat sheet |
| Never reuse same index. | 絕不重用同一索引。 | Cheat sheet |
| Dry-run [2,7,11,15], target 9. | 手跑 [2,7,11,15], target 9。 | Cheat sheet |
| Verify duplicate value case [3,3]. | 驗證重複值案例 [3,3]。 | Cheat sheet |
| Verify zero case [0,4,3,0]. | 驗證含零案例 [0,4,3,0]。 | Cheat sheet |
| Verify negative-number case. | 驗證負數案例。 | Cheat sheet |
| Average lookup is O(1). | 平均查找是 O(1)。 | Cheat sheet |
| Total average time is O(n). | 總平均時間是 O(n)。 | Cheat sheet |
| Space usage is O(n). | 空間使用是 O(n)。 | Cheat sheet |
| If stuck, restate invariant. | 卡住就重述不變量。 | Cheat sheet |
| If needed, explain fallback return. | 需要時說明保底回傳。 | Cheat sheet |
| End with complexity summary. | 以複雜度總結收尾。 | Cheat sheet |
| Offer follow-up discussion. | 主動提供後續討論。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ One-pass hash map logic is preserved.
- No hallucinated constraints: ✅ Uncertain behaviors are asked in clarification lines.
- Language simplicity: ✅ Short, spoken, interview-safe lines.
