# 02 Two Sum II - Input Array Is Sorted — Interview English Script (C++)

> Source aligned with: `docs/02_Two_Pointers/02_Two_Sum_II.md`

> Quick links: [Source Solution](../02_Two_Sum_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We have a sorted array called numbers. | 我們有一個已排序陣列 numbers。 | Restatement |
| We need two values summing to target. | 我們要找兩個值加總等於 target。 | Restatement |
| Return their one-based indices. | 回傳它們的一基索引。 | Restatement |
| I will use two pointers from both ends. | 我會用頭尾雙指標。 | Restatement |
| Then I will verify index format carefully. | 然後我會仔細驗證索引格式。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume exactly one valid solution exists? | 可以假設恰好一組解嗎？ | Clarify |
| Should returned indices be one-based always? | 回傳索引是否固定一基？ | Clarify |
| Can values be negative in this sorted array? | 這個排序陣列允許負數嗎？ | Clarify |
| Is extra memory restricted to O(1)? | 額外記憶體是否限制 O(1)？ | Clarify |
| Can I return early once pair is found? | 找到配對後可立即回傳嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline checks all pairs i and j. | 基線是檢查所有 i,j 配對。 | Approach |
| If sum matches target, return indices. | 若加總符合 target 就回傳索引。 | Approach |
| Time O(n^2), space O(1). | 時間 O(n^2)，空間 O(1)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Since array is sorted, two pointers are natural. | 因為已排序，雙指標很自然。 | Approach |
| Left starts at zero, right starts at n minus one. | left 從 0，right 從 n-1 開始。 | Approach |
| If sum is too big, move right leftward. | 若總和過大，right 往左移。 | Approach |
| If sum is too small, move left rightward. | 若總和過小，left 往右移。 | Approach |
| Match means return left+1 and right+1. | 相等時回傳 left+1、right+1。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I set left to zero and right to n minus one. | 先把 left 設 0、right 設 n-1。 | Coding |
| While left is smaller than right, I compute sum. | 當 left 小於 right，就計算 sum。 | Coding |
| If sum is greater than target, I decrement right. | 若 sum 大於 target，我遞減 right。 | Coding |
| If sum is less than target, I increment left. | 若 sum 小於 target，我遞增 left。 | Coding |
| If equal, I return one-based indices. | 若相等，我回傳一基索引。 | Coding |
| I do not need extra hash map here. | 這裡不需要額外 hash map。 | Coding |
| Sorted property drives each pointer decision. | 每次指標決策都靠已排序特性。 | Coding |
| Fallback return can be empty if required. | 若需要可用空陣列做保底回傳。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run numbers two, seven, eleven, fifteen. | 我手跑 numbers = 2,7,11,15。 | Dry-run |
| Target is nine. | target 是 9。 | Dry-run |
| left zero and right three gives sum seventeen. | left=0、right=3 時 sum 是 17。 | Dry-run |
| Sum too large, so move right to index two. | 總和太大，所以 right 移到 2。 | Dry-run |
| Sum is now thirteen, still too large. | 現在總和 13，仍過大。 | Dry-run |
| Move right to index one, sum becomes nine. | right 移到 1，總和變 9。 | Dry-run |
| Return [1,2] in one-based indexing. | 以一基索引回傳 [1,2]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: smallest length two with direct match. | 案例一：最小長度 2 且直接匹配。 | Edge test |
| Case two: negative and positive mixed values. | 案例二：正負值混合。 | Edge test |
| Case three: duplicated values near target. | 案例三：接近 target 的重複值。 | Edge test |
| Case four: verify one-based output indexing. | 案例四：驗證一基索引輸出。 | Edge test |
| Case five: if no-solution allowed, return empty. | 案例五：若允許無解，回傳空陣列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each loop step moves one pointer inward. | 每次迴圈都會把其中一個指標內縮。 | Complexity |
| Neither pointer moves backward. | 兩個指標都不會回頭。 | Complexity |
| So total pointer moves are linear. | 因此總移動次數是線性的。 | Complexity |
| We only keep a few integer variables. | 我們只維持少數整數變數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me recheck the sorted-array assumption. | 我先重確認已排序假設。 | If stuck |
| I can explain brute force first. | 我可先解釋暴力法。 | If stuck |
| Then I switch to two pointers. | 然後我切到雙指標。 | If stuck |
| I forgot one-based return detail. | 我一時忘了一基回傳細節。 | If stuck |
| Core pointer movement is still clear. | 核心指標移動仍清楚。 | If stuck |
| Thanks, I will adjust this branch. | 謝謝，我會調整這個分支。 | If stuck |
| I found why target compare failed. | 我找到 target 比較失敗原因。 | If stuck |
| Let me rerun one sample quickly. | 我快速重跑一個範例。 | If stuck |
| Now output format is correct. | 現在輸出格式正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| It uses sorted property effectively. | 它有效利用了已排序特性。 | Wrap-up |
| It returns one-based indices correctly. | 它可正確回傳一基索引。 | Wrap-up |
| Time is O(n), extra space O(1). | 時間 O(n)，額外空間 O(1)。 | Wrap-up |
| I can compare with hash-map variant if needed. | 若需要我可比較 hash map 變體。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate sorted-array two-sum target. | 重述排序陣列 two-sum 目標。 | Cheat sheet |
| Ask if one solution is guaranteed. | 詢問是否保證唯一解。 | Cheat sheet |
| Mention one-based index requirement. | 提到一基索引要求。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法是 O(n^2)。 | Cheat sheet |
| Two pointers give O(n). | 雙指標可達 O(n)。 | Cheat sheet |
| Start from both ends. | 從陣列兩端開始。 | Cheat sheet |
| If sum too large, move right. | 和過大就移動右指標。 | Cheat sheet |
| If sum too small, move left. | 和過小就移動左指標。 | Cheat sheet |
| Equal sum means return indices. | 和相等就回傳索引。 | Cheat sheet |
| Convert to one-based output. | 轉成一基索引輸出。 | Cheat sheet |
| Dry-run [2,7,11,15], target 9. | 手跑 [2,7,11,15], target 9。 | Cheat sheet |
| Verify negative values case. | 驗證負值案例。 | Cheat sheet |
| Verify duplicate values case. | 驗證重複值案例。 | Cheat sheet |
| Mention O(1) extra space. | 提到 O(1) 額外空間。 | Cheat sheet |
| Keep pointer invariants explicit. | 清楚說明指標不變量。 | Cheat sheet |
| If stuck, restate move rule. | 卡住時重述移動規則。 | Cheat sheet |
| Recheck output indexing before finish. | 收尾前重檢輸出索引。 | Cheat sheet |
| Summarize complexity briefly. | 簡短總結複雜度。 | Cheat sheet |
| Offer alternative discussion. | 提供替代方案討論。 | Cheat sheet |
| End confidently and clearly. | 清楚自信地收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sorted two-pointer solution and 1-based output are preserved.
- No hallucinated constraints: ✅ Uncertain assumptions are asked in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
