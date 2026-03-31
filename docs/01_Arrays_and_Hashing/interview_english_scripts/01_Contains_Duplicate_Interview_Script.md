# 01 Contains Duplicate — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/01_Contains_Duplicate.md`

> Quick links: [Source Solution](../01_Contains_Duplicate.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We get an integer array, nums. | 我們有一個整數陣列 nums。 | Restatement |
| Return true if any value appears twice. | 只要有重複值就回傳 true。 | Restatement |
| Return false if all values are unique. | 全部唯一就回傳 false。 | Restatement |
| I will use a one-pass hash set. | 我會用一次遍歷的 hash set。 | Restatement |
| Then I will verify edge cases. | 接著我會驗證邊界案例。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I assume length can be up to one hundred thousand? | 可以假設長度上限十萬嗎？ | Clarify |
| Can values be negative? | 數值可能是負數嗎？ | Clarify |
| Can I return right after first duplicate? | 找到第一個重複就能回傳嗎？ | Clarify |
| Can I use extra memory for speed? | 可以用額外記憶體換速度嗎？ | Clarify |
| If empty input appears, should it return false? | 若出現空輸入，是否回傳 false？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force compares every pair with two loops. | 暴力法用雙迴圈比較每一對。 | Approach |
| If one pair matches, return true. | 只要一對相同就回傳 true。 | Approach |
| Time is O(n^2), space is O(1). | 時間 O(n^2)，空間 O(1)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I use an unordered_set called seen. | 我用一個叫 seen 的 unordered_set。 | Approach |
| I scan nums from left to right once. | 我從左到右掃過 nums 一次。 | Approach |
| If num is already in seen, return true. | 若 num 已在 seen，直接回傳 true。 | Approach |
| Otherwise I insert num into seen. | 否則把 num 放進 seen。 | Approach |
| Average time is O(n), extra space O(n). | 平均時間 O(n)，額外空間 O(n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create unordered_set seen. | 先建立 unordered_set seen。 | Coding |
| Next, I reserve nums size for fewer rehashes. | 接著用 nums 大小預留空間。 | Coding |
| Then, I loop through each num in nums. | 然後逐一走訪 nums 的每個 num。 | Coding |
| I check whether seen already contains num. | 我先檢查 seen 是否已有 num。 | Coding |
| If yes, I return true immediately. | 若有，立刻回傳 true。 | Coding |
| If no, I insert num into seen. | 若沒有，就把 num 插入 seen。 | Coding |
| I continue until the loop ends. | 我持續直到迴圈結束。 | Coding |
| Finally, I return false. | 最後回傳 false。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums equals one, two, three, one. | 我手跑 nums = 1,2,3,1。 | Dry-run |
| Start with seen equals empty set. | 一開始 seen 是空集合。 | Dry-run |
| Read one, not found, so insert one. | 讀到 1，未出現，插入 1。 | Dry-run |
| Read two, not found, so insert two. | 讀到 2，未出現，插入 2。 | Dry-run |
| Read three, not found, so insert three. | 讀到 3，未出現，插入 3。 | Dry-run |
| Read one again, found in seen, return true. | 再讀到 1，已存在，回傳 true。 | Dry-run |
| Output true matches expectation. | 輸出 true，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: nums equals [7], output false. | 案例一：[7]，輸出 false。 | Edge test |
| Case two: nums equals [1,1], output true. | 案例二：[1,1]，輸出 true。 | Edge test |
| Case three: nums equals [-1,0,-1], output true. | 案例三：[-1,0,-1]，輸出 true。 | Edge test |
| Case four: nums equals [1,2,3,4], output false. | 案例四：[1,2,3,4]，輸出 false。 | Edge test |
| Case five: if empty is allowed, output false. | 案例五：若允許空陣列，輸出 false。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Average time is O(n), worst case O(n^2). | 平均 O(n)，最差 O(n^2)。 | Complexity |
| Space is O(n) for the set. | 空間是 O(n)，用在集合。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan n elements exactly once. | 我們剛好掃描 n 個元素一次。 | Complexity |
| Each set lookup is average O(1). | 每次集合查找平均 O(1)。 | Complexity |
| Heavy hash collisions can degrade to O(n^2). | 大量碰撞時可能退化到 O(n^2)。 | Complexity |
| In worst case, set stores n unique values. | 最差情況下集合存 n 個唯一值。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒整理想法嗎？ | If stuck |
| Let me restate the goal first. | 我先重述目標。 | If stuck |
| I will verify one assumption quickly. | 我快速確認一個假設。 | If stuck |
| I see two options now. | 我現在看到兩個選項。 | If stuck |
| First I explain brute force. | 我先講暴力法。 | If stuck |
| Then I switch to hash set. | 再切到 hash set。 | If stuck |
| Thanks, I will adjust here. | 謝謝，我會在這裡調整。 | If stuck |
| I found the bug location. | 我找到 bug 的位置了。 | If stuck |
| Let me run this sample again. | 我再跑一次這個範例。 | If stuck |
| Now the logic is consistent. | 現在邏輯一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I tested normal and edge cases. | 我測了正常與邊界案例。 | Wrap-up |
| It returns early on duplicates. | 發現重複時會提前回傳。 | Wrap-up |
| Average time O(n), space O(n). | 平均時間 O(n)，空間 O(n)。 | Wrap-up |
| I can discuss sorting trade-offs too. | 我也可以補充排序取捨。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate duplicate-check goal. | 重述「檢查重複」目標。 | Cheat sheet |
| Ask input size range. | 詢問輸入大小範圍。 | Cheat sheet |
| Ask whether negatives exist. | 詢問是否有負數。 | Cheat sheet |
| Start from brute force. | 先從暴力法開始。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法是 O(n^2)。 | Cheat sheet |
| Introduce unordered_set solution. | 引出 unordered_set 解法。 | Cheat sheet |
| Scan array once. | 陣列掃描一次。 | Cheat sheet |
| Check before insert. | 先檢查再插入。 | Cheat sheet |
| Found duplicate, return true. | 找到重複就回傳 true。 | Cheat sheet |
| Loop ends, return false. | 迴圈結束回傳 false。 | Cheat sheet |
| Dry-run one simple sample. | 手跑一個簡單範例。 | Cheat sheet |
| Test single-element input. | 測試單一元素輸入。 | Cheat sheet |
| Test all-unique input. | 測試全唯一輸入。 | Cheat sheet |
| Test immediate duplicate input. | 測試立即重複輸入。 | Cheat sheet |
| Test negative-number input. | 測試含負數輸入。 | Cheat sheet |
| Mention early-return behavior. | 說明提前回傳行為。 | Cheat sheet |
| Average lookup is O(1). | 平均查找是 O(1)。 | Cheat sheet |
| Worst collisions may degrade. | 最差碰撞可能退化。 | Cheat sheet |
| Space grows with unique values. | 空間隨唯一值數量增加。 | Cheat sheet |
| Offer memory-saving alternative. | 可補充省記憶體替代法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hash set one-pass flow is preserved.
- No hallucinated constraints: ✅ Unknown behavior is asked in clarification lines.
- Language simplicity: ✅ Short, spoken, interview-safe English.
