# 03 Permutations — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/03_Permutations.md`

> Quick links: [Source Solution](../03_Permutations.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the permutations problem. | 我先重述 permutations 題目。 | Restatement |
| We are given an array of distinct integers. | 題目給一個互異整數陣列。 | Restatement |
| We need to return all possible orderings. | 要回傳所有可能排列。 | Restatement |
| Each number must appear exactly once per permutation. | 每個排列中每個數字都必須且只能出現一次。 | Restatement |
| Output order of permutations is not important. | 排列輸出順序不重要。 | Restatement |
| I will use backtracking with in-place swap. | 我會用原地 swap 的回溯解法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume all numbers are unique as stated? | 是否可依題意假設數字皆不重複？ | Clarify |
| Is returning permutations in any order acceptable? | 任意順序回傳排列是否可接受？ | Clarify |
| Do you prefer swap-based recursion over visited-array recursion? | 你偏好 swap 遞迴還是 visited 遞迴？ | Clarify |
| Is in-place modification during recursion allowed? | 遞迴過程中可原地修改陣列嗎？ | Clarify |
| Should I briefly compare both common implementations? | 是否要簡短比較兩種常見寫法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force can generate all permutations and store them. | 暴力法就是完整生成所有排列。 | Approach |
| Total count is n factorial, so growth is very fast. | 總數是 n!，成長很快。 | Approach |
| We still need systematic recursion to generate them correctly. | 仍需有系統遞迴來正確生成。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| In swap-based DFS, position start chooses one value each round. | swap DFS 中每輪決定 start 位置放誰。 | Approach |
| Swap nums[start] with nums[i] for every i from start onward. | 對 i>=start，交換 nums[start] 與 nums[i]。 | Approach |
| Recurse to start plus one to decide next position. | 遞迴到 start+1 決定下一格。 | Approach |
| After recursion, swap back to restore previous state. | 遞迴後交換回來還原狀態。 | Approach |
| This avoids extra visited array and stays memory efficient. | 這可免 visited 陣列，記憶體較省。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create result container and call backtrack with start zero. | 我建立結果容器並從 start=0 呼叫。 | Coding |
| Base case is start equals nums size. | 基底條件是 start 等於陣列長度。 | Coding |
| At base, current nums order is one full permutation. | 到基底時 nums 當前順序即一個排列。 | Coding |
| For loop iterates i from start to end. | for 迴圈讓 i 從 start 到結尾。 | Coding |
| I swap nums[start] and nums[i]. | 我交換 nums[start] 與 nums[i]。 | Coding |
| Then I recurse with start plus one. | 接著以 start+1 遞迴。 | Coding |
| After returning, I swap back for backtracking. | 回來後再 swap 回去完成回溯。 | Coding |
| Finally all permutations are collected in result. | 最終結果中會收集所有排列。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [1,2,3]. | 我手跑 nums=[1,2,3]。 | Dry-run |
| At start zero, choose one first, then recurse on [2,3]. | start=0 先選 1，遞迴處理 [2,3]。 | Dry-run |
| This branch yields [1,2,3] and [1,3,2]. | 此分支得到 [1,2,3] 與 [1,3,2]。 | Dry-run |
| Backtrack and swap two to front for next branch. | 回溯後把 2 換到前面跑下一支。 | Dry-run |
| That yields [2,1,3] and [2,3,1]. | 會得到 [2,1,3] 與 [2,3,1]。 | Dry-run |
| Final branch with three in front gives last two permutations. | 最後 3 在前會給最後兩個排列。 | Dry-run |
| Total is six permutations, equal to three factorial. | 總數為 6，等於 3!。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element should return one permutation. | 案例一：單元素應只回一個排列。 | Edge test |
| Case two: two elements should return exactly two permutations. | 案例二：兩元素應剛好回兩個排列。 | Edge test |
| Case three: negative numbers should behave the same. | 案例三：含負數時行為應一致。 | Edge test |
| Case four: verify count equals n factorial for small n. | 案例四：小 n 驗證數量等於 n!。 | Edge test |
| Case five: verify no duplicates when input is distinct. | 案例五：互異輸入時不得有重複排列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n times n factorial). | 時間複雜度是 O(n*n!)。 | Complexity |
| Auxiliary recursion space is O(n), excluding output. | 不含輸出時輔助空間為 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| There are n factorial leaves because each ordering is unique. | 因每個排列唯一，所以有 n! 個葉節點。 | Complexity |
| Copying one permutation into result costs O(n). | 每次把排列寫入結果要 O(n)。 | Complexity |
| Multiply together gives O(n times n factorial). | 合併後得到 O(n*n!)。 | Complexity |
| Recursion depth is n and swap uses constant extra storage. | 遞迴深度 n，swap 只用常數額外空間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me think in terms of fixing one position at a time. | 我先用逐格固定位置的方式思考。 | If stuck |
| At position start, I can place any remaining element. | 在 start 位置可放任一未固定元素。 | If stuck |
| Swap is the simplest way to realize that choice. | swap 是實作此選擇最簡潔方式。 | If stuck |
| After recurse, I must swap back. | 遞迴後我必須 swap 回來。 | If stuck |
| Without swap-back, later branches become incorrect. | 不 swap 回來會讓後續分支錯亂。 | If stuck |
| Base case should trigger when start reaches n. | 基底應在 start 到 n 時觸發。 | If stuck |
| Then I store current array ordering. | 然後儲存當前陣列順序。 | If stuck |
| Let me test quickly with [0,1]. | 我快速用 [0,1] 測試。 | If stuck |
| I get [0,1] and [1,0], so logic is correct. | 得到 [0,1]、[1,0]，邏輯正確。 | If stuck |
| Great, recursion invariants are now clear. | 很好，遞迴不變量已清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved permutations with swap-based backtracking. | 我用 swap 回溯解出 permutations。 | Wrap-up |
| The algorithm fixes positions from left to right. | 演算法從左到右固定位置。 | Wrap-up |
| Backtracking swap-back keeps state clean for siblings. | 回溯交換還原可保持同層狀態乾淨。 | Wrap-up |
| Runtime is O(n times n factorial). | 時間複雜度是 O(n*n!)。 | Wrap-up |
| I can also show visited-array implementation if needed. | 若需要我也可展示 visited 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: full permutation generation. | 題型：全排列生成。 | Cheat sheet |
| Input values are distinct. | 輸入值互異。 | Cheat sheet |
| Need all possible orders. | 要所有可能順序。 | Cheat sheet |
| Use swap-based DFS. | 用 swap 型 DFS。 | Cheat sheet |
| State variable is start index. | 狀態變數是 start 索引。 | Cheat sheet |
| Base when start equals n. | start==n 時觸發基底。 | Cheat sheet |
| Store nums snapshot at base. | 基底時儲存 nums 快照。 | Cheat sheet |
| Loop i from start to n-1. | i 從 start 迴圈到 n-1。 | Cheat sheet |
| Swap start with i before recurse. | 遞迴前 swap(start,i)。 | Cheat sheet |
| Recurse with start+1. | 以 start+1 遞迴。 | Cheat sheet |
| Swap back after recurse. | 遞迴後要 swap 回來。 | Cheat sheet |
| Swap-back is mandatory invariant. | 交換還原是不變量。 | Cheat sheet |
| Total results count n factorial. | 總結果數是 n!。 | Cheat sheet |
| Time O(n*n!). | 時間 O(n*n!)。 | Cheat sheet |
| Stack space O(n). | 堆疊空間 O(n)。 | Cheat sheet |
| Output space O(n*n!). | 輸出空間 O(n*n!)。 | Cheat sheet |
| Validate with [1,2,3] => 6. | [1,2,3] 驗證應得 6 筆。 | Cheat sheet |
| Validate with [0,1] => 2. | [0,1] 驗證應得 2 筆。 | Cheat sheet |
| Alternative: visited-array DFS. | 替代法：visited DFS。 | Cheat sheet |
| Mention trade-off between readability and memory. | 補充可讀性與記憶體取捨。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Swap-based backtracking flow is preserved.
- No hallucinated constraints: ✅ Uses distinct-input permutation semantics.
- Language simplicity: ✅ Direct spoken narration tied to coding order.
