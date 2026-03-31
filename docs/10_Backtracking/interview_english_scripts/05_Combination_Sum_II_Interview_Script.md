# 05 Combination Sum II — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/05_Combination_Sum_II.md`

> Quick links: [Source Solution](../05_Combination_Sum_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the Combination Sum Two problem. | 我先重述 Combination Sum II。 | Restatement |
| Input candidates may contain duplicate numbers. | 輸入 candidates 可能有重複值。 | Restatement |
| We need unique combinations summing to target. | 我們要找和為 target 的唯一組合。 | Restatement |
| Each candidate index can be used at most once. | 每個候選位置最多使用一次。 | Restatement |
| Output must not contain duplicate combinations. | 輸出不可有重複組合。 | Restatement |
| I will use sorted backtracking with pruning and duplicate skip. | 我會用排序回溯搭配剪枝與跳重。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is each element usable only once per combination? | 每個元素在單一組合中是否只能用一次？ | Clarify |
| Can I sort the array to simplify deduplication? | 可否先排序以簡化去重？ | Clarify |
| Is output order of combinations irrelevant? | 輸出組合順序是否不重要？ | Clarify |
| Should [1,7] generated from different duplicate ones count once? | 由不同重複 1 產生的 [1,7] 是否只算一次？ | Clarify |
| Is early break valid when candidates[i] exceeds remaining target? | 當 candidates[i] 大於剩餘值可直接 break 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force explores all subsets and then filters by sum. | 暴力法先列舉全部子集再過濾總和。 | Approach |
| Then it deduplicates combinations with a set. | 接著再用 set 去重組合。 | Approach |
| This is correct but wastes work and memory. | 這雖正確但浪費運算與記憶體。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sort candidates so duplicates are adjacent. | 先排序讓重複值相鄰。 | Approach |
| DFS loop starts from current index and moves forward only. | DFS 迴圈從當前 index 往後走。 | Approach |
| Skip duplicates with condition i greater than start and equal previous. | 用 i>start 且等於前值來跳過重複。 | Approach |
| If candidates[i] is greater than remaining target, break for pruning. | 若 candidates[i] 大於剩餘 target 就 break 剪枝。 | Approach |
| Recurse with i plus one since each element is one-time use. | 因元素一次性使用，遞迴到 i+1。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I sort candidates at the beginning. | 一開始先排序 candidates。 | Coding |
| I define backtrack(start, remaining, currentPath). | 我定義 backtrack(start, remaining, path)。 | Coding |
| If remaining is zero, I record currentPath. | 若 remaining 為 0，就記錄路徑。 | Coding |
| I iterate i from start to candidates size minus one. | i 從 start 迭代到結尾。 | Coding |
| If i greater than start and same as previous, I continue. | 若 i>start 且與前值相同就 continue。 | Coding |
| If candidates[i] exceeds remaining, I break loop. | 若 candidates[i] 大於 remaining 就 break。 | Coding |
| Otherwise push candidates[i], recurse with i plus one, then pop. | 否則 push 後以 i+1 遞迴，再 pop。 | Coding |
| This gives unique combinations without post-processing dedup. | 這可直接得到唯一組合，不需事後去重。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run sorted candidates [1,1,2,5,6,7,10], target eight. | 我手跑排序後 [1,1,2,5,6,7,10]、target=8。 | Dry-run |
| Pick first one, then second one, then six to reach eight. | 先選第一個 1，再選第二個 1，再選 6 得 8。 | Dry-run |
| Backtrack and try one plus two plus five to get another solution. | 回溯後試 1+2+5 得另一解。 | Dry-run |
| One plus seven also works. | 1+7 也可行。 | Dry-run |
| Starting from two, combination two plus six works too. | 從 2 開始時，2+6 也成立。 | Dry-run |
| At same depth, second leading one is skipped to avoid duplicates. | 同層第二個起始 1 會被跳過避免重複。 | Dry-run |
| Final result is [1,1,6], [1,2,5], [1,7], [2,6]. | 最終答案為 [1,1,6]、[1,2,5]、[1,7]、[2,6]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: all candidates larger than target returns empty. | 案例一：所有候選都大於 target，回空。 | Edge test |
| Case two: many duplicates but only one unique combination. | 案例二：重複很多但只有一個唯一解。 | Edge test |
| Case three: target reached by single element. | 案例三：target 可由單一元素達成。 | Edge test |
| Case four: no valid combination at all. | 案例四：完全無可行組合。 | Edge test |
| Case five: verify duplicate paths do not duplicate outputs. | 案例五：確認重複路徑不會重複輸出。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Worst-case runtime is exponential, commonly O(two to the n). | 最壞時間為指數級，常寫 O(2^n)。 | Complexity |
| Recursion stack space is O(n), excluding output. | 不含輸出時堆疊空間 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting costs O(n log n) before DFS. | DFS 前排序成本為 O(n log n)。 | Complexity |
| DFS explores subset-like branches in worst case. | DFS 在最壞情況探索近似子集樹。 | Complexity |
| Pruning and duplicate skip reduce actual search significantly. | 剪枝與跳重可大幅降低實際搜尋量。 | Complexity |
| Auxiliary recursion memory is O(n), while output can be larger. | 輔助遞迴記憶體 O(n)，輸出可能更大。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I need to separate this from Combination Sum One. | 我要先與 Combination Sum I 區分。 | If stuck |
| Here each element can be used only once. | 這題每個元素只能用一次。 | If stuck |
| So recurse with i plus one, not i. | 所以遞迴要用 i+1，不是 i。 | If stuck |
| Sorting is essential for dedup and pruning. | 排序對去重與剪枝都關鍵。 | If stuck |
| Duplicate skip must be same-level only. | 跳重必須限定在同層。 | If stuck |
| Condition is i greater than start and equal previous. | 條件是 i>start 且與前值相同。 | If stuck |
| If value exceeds remaining target, break immediately. | 值超過 remaining 就立刻 break。 | If stuck |
| Let me verify with [10,1,2,7,6,1,5], target eight. | 我用 [10,1,2,7,6,1,5]、target=8 驗證。 | If stuck |
| I get four unique combinations exactly once. | 我得到四組唯一解且各只出現一次。 | If stuck |
| Great, dedup and one-time usage are both correct. | 很好，去重與一次性使用都正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved Combination Sum Two with sorted DFS backtracking. | 我以排序 DFS 回溯解出 Combination Sum II。 | Wrap-up |
| The key differences are one-time usage and same-level dedup. | 關鍵差異是一次性使用與同層去重。 | Wrap-up |
| Pruning by remaining target improves efficiency. | 以剩餘 target 剪枝可提升效率。 | Wrap-up |
| We recurse with i plus one to avoid reusing same element index. | 遞迴到 i+1 以避免重用同一位置。 | Wrap-up |
| I can also contrast it with Combination Sum One if needed. | 若需要我也可對比 Combination Sum I。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: combination sum with duplicates in input. | 題型：輸入可重複的組合總和。 | Cheat sheet |
| Need unique combinations only. | 只要唯一組合。 | Cheat sheet |
| Each element index used at most once. | 每個位置最多用一次。 | Cheat sheet |
| Sort candidates first. | 先排序 candidates。 | Cheat sheet |
| DFS state: start, remaining, path. | DFS 狀態：start、remaining、path。 | Cheat sheet |
| Success when remaining is zero. | remaining=0 為成功。 | Cheat sheet |
| Loop i from start. | i 從 start 開始迴圈。 | Cheat sheet |
| Same-level dedup: i>start and same previous. | 同層去重：i>start 且同前值。 | Cheat sheet |
| If dedup condition true, continue. | 去重成立就 continue。 | Cheat sheet |
| Prune when value > remaining. | value>remaining 時剪枝。 | Cheat sheet |
| Because sorted, pruning can break loop. | 因已排序，剪枝可直接 break。 | Cheat sheet |
| Choose value by push. | push 當前值做選擇。 | Cheat sheet |
| Recurse with i+1. | 以 i+1 遞迴。 | Cheat sheet |
| Backtrack by pop. | pop 完成回溯。 | Cheat sheet |
| Avoid set-based post dedup. | 避免事後 set 去重。 | Cheat sheet |
| Output order is arbitrary. | 輸出順序可任意。 | Cheat sheet |
| Worst time is exponential. | 最壞時間為指數級。 | Cheat sheet |
| Stack space O(n). | 堆疊空間 O(n)。 | Cheat sheet |
| Sample gives four combinations. | 範例可得四組解。 | Cheat sheet |
| Compare with Combination Sum One if asked. | 被問到可對比 Combination Sum I。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sorted DFS + same-level dedup + pruning preserved.
- No hallucinated constraints: ✅ One-time usage and unique-output semantics are respected.
- Language simplicity: ✅ Interview-ready, concise, and problem-specific narration.
