# 03 K Closest Points to Origin — Interview English Script (C++)

> Source aligned with: `docs/09_Heap/03_K_Closest_Points.md`

> Quick links: [Source Solution](../03_K_Closest_Points.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the K closest points problem. | 我先重述 K 個最近點這題。 | Restatement |
| We are given points on a 2D plane and an integer k. | 題目給 2D 點座標與整數 k。 | Restatement |
| We must return any k points closest to the origin. | 要回傳距原點最近的任意 k 點。 | Restatement |
| Distance comparison can use x squared plus y squared. | 比較距離可用 x²+y²，不必開根號。 | Restatement |
| Output order is not important for this problem. | 這題輸出順序不重要。 | Restatement |
| I will use a size-k max-heap to keep current best points. | 我會用 size-k max-heap 維護當前最佳點。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I return points in any order? | 回傳點的順序是否可任意？ | Clarify |
| Is comparing squared distance fully acceptable? | 只比距離平方是否可接受？ | Clarify |
| Are duplicate points possible and should be treated normally? | 可能有重複點且正常處理嗎？ | Clarify |
| Do we always have one less than or equal k less than or equal n? | 是否保證 1 <= k <= n？ | Clarify |
| Should I prioritize heap solution over full sorting? | 是否優先希望 heap 解法而非全排序？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force computes all distances and sorts all points. | 暴力法先算全部距離再整體排序。 | Approach |
| Then we return the first k points in sorted order. | 然後取排序後前 k 個點。 | Approach |
| This takes O(n log n), which is unnecessary when k is small. | 這要 O(n log n)，k 小時不划算。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Keep a max-heap containing at most k points. | 維持最多 k 個點的 max-heap。 | Approach |
| Heap key is squared distance to origin. | heap 鍵值是到原點的距離平方。 | Approach |
| Push each point, and if size exceeds k, pop once. | 每讀一點先 push，超過 k 就 pop。 | Approach |
| Max-heap top is the farthest among kept points. | max-heap top 是保留集合中最遠點。 | Approach |
| So after scanning all points, heap stores exactly k closest. | 掃描完成後 heap 正好是最近的 k 點。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create a max-heap of pair distance and index. | 我建立存距離與索引的 max-heap。 | Coding |
| For each point, I compute x squared plus y squared. | 對每個點計算 x²+y²。 | Coding |
| I push distance and index into heap. | 我把距離與索引推入 heap。 | Coding |
| If heap size is greater than k, I pop top. | 若 heap 大於 k，就彈出 top。 | Coding |
| This removes the farthest point among current candidates. | 這會移除目前候選中的最遠點。 | Coding |
| After loop, heap contains the k closest point indices. | 迴圈結束後 heap 留下 k 個最近點索引。 | Coding |
| I extract those indices and build answer points array. | 我取出索引並組成答案陣列。 | Coding |
| Returning in any order is acceptable by problem statement. | 題目允許任意順序回傳。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run points [[1,3],[-2,2]] with k equals 1. | 我手跑 points [[1,3],[-2,2]]、k=1。 | Dry-run |
| First point distance is ten, heap keeps it. | 第一點距離是 10，heap 先保留。 | Dry-run |
| Second point distance is eight, push into heap. | 第二點距離是 8，推入 heap。 | Dry-run |
| Heap size becomes two, so I pop the farthest distance ten. | heap 變 2，彈出最遠的 10。 | Dry-run |
| Remaining point is [-2,2], which is the answer. | 剩下 [-2,2]，即為答案。 | Dry-run |
| This matches expected output for the sample. | 與範例預期輸出一致。 | Dry-run |
| Order is trivial here since only one point is returned. | 只回傳一點時順序不影響。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: k equals one returns single nearest point. | 案例一：k=1 回傳單一最近點。 | Edge test |
| Case two: k equals n should return all points. | 案例二：k=n 時應回傳全部點。 | Edge test |
| Case three: points with same distance tie should still work. | 案例三：同距離平手情況仍要正確。 | Edge test |
| Case four: negative coordinates should behave the same. | 案例四：負座標情況行為應一致。 | Edge test |
| Case five: duplicate points should be handled naturally. | 案例五：重複點應自然被處理。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log k). | 時間複雜度是 O(n log k)。 | Complexity |
| Extra space is O(k). | 額外空間複雜度是 O(k)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan all n points once and do heap operations per point. | 我們掃描 n 個點，每點做 heap 操作。 | Complexity |
| Heap size is capped at k, so push or pop is O(log k). | heap 大小上限 k，push/pop 是 O(log k)。 | Complexity |
| Total runtime becomes O(n log k). | 總時間因此是 O(n log k)。 | Complexity |
| Heap stores at most k entries, so space is O(k). | heap 最多存 k 筆，所以空間 O(k)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me simplify: this is a top-k distance problem. | 我先簡化：這是 top-k 距離問題。 | If stuck |
| I do not need full ordering of all points. | 我不需要所有點的完整排序。 | If stuck |
| A max-heap of size k is enough. | 用 size-k max-heap 就夠了。 | If stuck |
| If size exceeds k, remove current farthest. | 若 size 超過 k，移除當前最遠。 | If stuck |
| I should compare squared distance, not sqrt distance. | 我應比較距離平方，不必算根號。 | If stuck |
| Let me rerun the two-point sample quickly. | 我快速重跑兩點範例。 | If stuck |
| Distances ten and eight leave only eight in heap. | 距離 10 與 8 最後只留 8。 | If stuck |
| So answer is [-2,2], confirmed. | 所以答案是 [-2,2]，已確認。 | If stuck |
| I will also test tie distances to confirm stability. | 我再測同距離平手確保穩定。 | If stuck |
| Great, heap invariant now looks correct. | 很好，heap 不變量看起來正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with a max-heap of fixed size k. | 我用固定 size-k 的 max-heap 解出。 | Wrap-up |
| The heap always keeps the currently best k points. | heap 會持續保留當前最佳 k 點。 | Wrap-up |
| Comparing squared distances avoids unnecessary sqrt operations. | 用距離平方比較可避免多餘根號運算。 | Wrap-up |
| Runtime is O(n log k) with O(k) space. | 時間 O(n log k)，空間 O(k)。 | Wrap-up |
| I can also discuss quick-select as an alternative. | 我也可補充 quick-select 替代法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: top-k by distance. | 題型：依距離取 top-k。 | Cheat sheet |
| Use squared distance x2 plus y2. | 用距離平方 x2+y2。 | Cheat sheet |
| Avoid sqrt for comparison. | 比較時不必開根號。 | Cheat sheet |
| Keep max-heap size exactly k. | 維持 max-heap 大小為 k。 | Cheat sheet |
| Heap stores distance and index. | heap 存距離與索引。 | Cheat sheet |
| Push each incoming point. | 每個點都先 push。 | Cheat sheet |
| If size > k, pop top. | 若 size>k，pop top。 | Cheat sheet |
| Top means farthest among kept points. | top 是保留集合中最遠點。 | Cheat sheet |
| After scan, heap is answer set. | 掃描完 heap 即答案集合。 | Cheat sheet |
| Output order can be arbitrary. | 輸出順序可任意。 | Cheat sheet |
| Brute force: full sort all points. | 暴力法：全部點排序。 | Cheat sheet |
| Brute force cost O(n log n). | 暴力成本 O(n log n)。 | Cheat sheet |
| Optimized cost O(n log k). | 優化成本 O(n log k)。 | Cheat sheet |
| Space is O(k). | 空間是 O(k)。 | Cheat sheet |
| k equals n returns all points. | k=n 會回傳全部點。 | Cheat sheet |
| Handle ties naturally. | 平手距離可自然處理。 | Cheat sheet |
| Handle negative coordinates too. | 負座標也能正常處理。 | Cheat sheet |
| Common bug: using min-heap incorrectly. | 常見錯誤：min-heap 用錯方向。 | Cheat sheet |
| Common bug: forgetting size cap pop. | 常見錯誤：忘記超量時 pop。 | Cheat sheet |
| Final invariant: heap holds k closest. | 最終不變量：heap 存 k 個最近點。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Max-heap top-k approach is preserved.
- No hallucinated constraints: ✅ Matches source assumptions and sample behavior.
- Language simplicity: ✅ Natural, interview-spoken, concise lines.
