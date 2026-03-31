# 04 Subsets II — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/04_Subsets_II.md`

> Quick links: [Source Solution](../04_Subsets_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the Subsets Two problem. | 我先重述 Subsets II。 | Restatement |
| Input may contain duplicate numbers this time. | 這題輸入可能有重複數字。 | Restatement |
| We need all unique subsets only. | 我們只要唯一的子集結果。 | Restatement |
| Duplicate subset outputs are not allowed. | 不可出現重複子集輸出。 | Restatement |
| Empty subset is still part of the answer. | 空集合仍是答案的一部分。 | Restatement |
| I will sort first and skip duplicates within each DFS level. | 我會先排序並在同層 DFS 跳過重複。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is output order arbitrary as long as subsets are unique? | 只要唯一，輸出順序可任意嗎？ | Clarify |
| Should duplicate values in input be treated as separate positions? | 輸入重複值是否視為不同位置？ | Clarify |
| Do we need to preserve original input order? | 是否需要保留原始輸入順序？ | Clarify |
| Is sorting input acceptable for duplicate handling? | 為去重而排序是否允許？ | Clarify |
| Do you prefer loop-style DFS skip over using a set container? | 你偏好迴圈跳重而非 set 去重嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force generates all subsets then deduplicates by set. | 暴力法先生成全部子集再用 set 去重。 | Approach |
| This adds extra memory and comparison overhead. | 這會增加記憶體與比對成本。 | Approach |
| We can avoid that by preventing duplicates during DFS. | 我們可在 DFS 過程中就避免重複。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sort nums so equal values become adjacent. | 先排序讓相同值相鄰。 | Approach |
| In backtracking loop, push current path into result first. | 在迴圈 DFS 中先把路徑加入結果。 | Approach |
| When iterating i, skip if i greater than start and nums[i] equals nums[i-1]. | 迭代 i 時，若 i>start 且與前一個相同則跳過。 | Approach |
| This skip rule removes same-level duplicate branches. | 此規則能去掉同層重複分支。 | Approach |
| Then choose number, recurse to i plus one, and backtrack. | 接著選值、遞迴到 i+1、再回溯。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I sort nums before DFS. | DFS 前我先排序 nums。 | Coding |
| I define backtrack(start, currentPath). | 我定義 backtrack(start, currentPath)。 | Coding |
| On entry of each call, currentPath is a valid subset. | 每次進入函式，當前路徑都算合法子集。 | Coding |
| So I append a copy of currentPath to result. | 所以先把路徑拷貝加到結果。 | Coding |
| Then I iterate i from start to end. | 然後讓 i 從 start 走到結尾。 | Coding |
| If i greater than start and nums[i] equals previous, I continue. | 若 i>start 且 nums[i] 等於前一個就 continue。 | Coding |
| Otherwise push nums[i], recurse with i plus one, then pop. | 否則 push nums[i]，遞迴 i+1，再 pop。 | Coding |
| This guarantees uniqueness without a hash set. | 這可在不用 hash set 下保證唯一性。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [1,2,2] after sorting. | 我手跑排序後 nums=[1,2,2]。 | Dry-run |
| Start with empty path, record empty subset. | 從空路徑開始，先記錄空集合。 | Dry-run |
| Choose one, then choose first two, then second two to get [1,2,2]. | 選 1，再選第一個 2，再選第二個 2 得 [1,2,2]。 | Dry-run |
| Backtrack and include only one two to get [1,2]. | 回溯後只選一個 2 得 [1,2]。 | Dry-run |
| At same level, second two is skipped by duplicate rule. | 同層遇到第二個 2 會被跳過。 | Dry-run |
| Branch without one gives [2] and [2,2]. | 不選 1 的分支會得 [2] 與 [2,2]。 | Dry-run |
| Final unique set matches expected output. | 最終唯一集合與預期一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: all numbers identical like [2,2,2]. | 案例一：全相同數字如 [2,2,2]。 | Edge test |
| Case two: no duplicates should behave like normal subsets. | 案例二：無重複時應退化成一般 subsets。 | Edge test |
| Case three: single element input still returns two subsets. | 案例三：單元素輸入仍回兩個子集。 | Edge test |
| Case four: negative and repeated values mixed. | 案例四：負數與重複值混合。 | Edge test |
| Case five: verify duplicate subsets never appear. | 案例五：確認輸出無重複子集。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n times two to the n) in worst case. | 最壞時間複雜度是 O(n*2^n)。 | Complexity |
| Auxiliary recursion space is O(n), excluding output. | 不含輸出時輔助空間 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting costs O(n log n) before DFS starts. | DFS 前排序成本為 O(n log n)。 | Complexity |
| DFS still explores power-set scale in worst distinct-like cases. | DFS 在最壞情況仍近似冪集合規模。 | Complexity |
| Copying subsets contributes factor n, so worst runtime is O(n times two to the n). | 子集拷貝帶來 n 因子，因此最壞是 O(n*2^n)。 | Complexity |
| Recursion depth is n, while output memory can dominate. | 遞迴深度 n，而輸出記憶體可能主導。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| The key issue here is duplicate handling, not subset generation itself. | 這題核心是去重，不是生成本身。 | If stuck |
| Sorting is my first step to expose adjacent duplicates. | 排序是第一步，讓重複值相鄰。 | If stuck |
| Duplicate skip only applies within the same recursion level. | 跳重只作用在同一層遞迴。 | If stuck |
| Condition should be i greater than start and nums[i] equals nums[i-1]. | 條件要是 i>start 且 nums[i]==nums[i-1]。 | If stuck |
| If I skip too aggressively, I may lose valid subsets. | 若跳太多會漏合法子集。 | If stuck |
| If I skip too little, duplicates appear. | 若跳太少就會出現重複。 | If stuck |
| Let me test with [1,2,2] to validate skip behavior. | 我用 [1,2,2] 驗證跳重行為。 | If stuck |
| I still get [1,2,2] once and [2,2] once. | [1,2,2] 與 [2,2] 都只出現一次。 | If stuck |
| Great, same-level dedup rule is now correct. | 很好，同層去重規則已正確。 | If stuck |
| I can now finalize complexity and summary. | 我現在可收尾複雜度與總結。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved Subsets Two by sorting plus level-wise duplicate skipping. | 我以排序加同層跳重解出 Subsets II。 | Wrap-up |
| Every recursion path is recorded as one valid subset. | 每條遞迴路徑都記錄成合法子集。 | Wrap-up |
| The i greater than start rule prevents duplicate branches. | i>start 的規則可防止重複分支。 | Wrap-up |
| Worst-case runtime remains O(n times two to the n). | 最壞時間仍是 O(n*2^n)。 | Wrap-up |
| This is cleaner than post-processing with set deduplication. | 這比事後用 set 去重更乾淨。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: subsets with duplicates. | 題型：含重複值的 subsets。 | Cheat sheet |
| Need unique subsets only. | 只要唯一子集。 | Cheat sheet |
| Sort input first. | 先排序輸入。 | Cheat sheet |
| Use DFS with start index. | 使用帶 start 的 DFS。 | Cheat sheet |
| Record current path every call. | 每次呼叫都記錄當前路徑。 | Cheat sheet |
| Iterate i from start to end. | i 從 start 迭代到結尾。 | Cheat sheet |
| Duplicate skip condition is crucial. | 跳重條件是關鍵。 | Cheat sheet |
| Condition: i>start and equal previous. | 條件：i>start 且等於前值。 | Cheat sheet |
| If true, continue loop. | 成立就 continue。 | Cheat sheet |
| Else push nums[i]. | 否則 push nums[i]。 | Cheat sheet |
| Recurse with i+1. | 以 i+1 遞迴。 | Cheat sheet |
| Pop after recursion. | 遞迴後 pop。 | Cheat sheet |
| Same-level dedup only. | 只做同層去重。 | Cheat sheet |
| Preserve deeper-level valid duplicates. | 保留深層合法重複組合。 | Cheat sheet |
| Empty subset must exist. | 必含空集合。 | Cheat sheet |
| Worst time O(n*2^n). | 最壞時間 O(n*2^n)。 | Cheat sheet |
| Sort adds O(n log n). | 排序額外 O(n log n)。 | Cheat sheet |
| Stack space O(n). | 堆疊空間 O(n)。 | Cheat sheet |
| Output can be exponential. | 輸出可能是指數級。 | Cheat sheet |
| Alternative set dedup is heavier. | 替代 set 去重較笨重。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sort + same-level skip backtracking is preserved.
- No hallucinated constraints: ✅ Matches duplicate-input and unique-subset requirements.
- Language simplicity: ✅ Clear interview-oriented explanation with precise skip rule.
