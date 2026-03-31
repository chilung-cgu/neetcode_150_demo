# 03 3Sum — Interview English Script (C++)

> Source aligned with: `docs/02_Two_Pointers/03_3Sum.md`

> Quick links: [Source Solution](../03_3Sum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We need unique triplets summing to zero. | 我們要找和為零的不重複三元組。 | Restatement |
| Indices must be different for each triplet. | 每組三元組的索引都要不同。 | Restatement |
| Duplicate triplets are not allowed in output. | 輸出不能有重複三元組。 | Restatement |
| I will use sorting plus two pointers. | 我會用排序加雙指標。 | Restatement |
| Then I will focus on dedup rules. | 接著我會重點說明去重規則。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I reorder input by sorting in place? | 我可以原地排序輸入嗎？ | Clarify |
| Should output triplet order matter? | 輸出三元組順序有要求嗎？ | Clarify |
| Do we require strict uniqueness of triplets? | 是否要求三元組嚴格唯一？ | Clarify |
| Can nums include many duplicates and negatives? | nums 可含大量重複與負數嗎？ | Clarify |
| Is O(n^2) expected target complexity? | 預期目標複雜度是 O(n^2) 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline uses three nested loops. | 基線是三層迴圈。 | Approach |
| Check every i, j, k combination for sum zero. | 檢查每個 i,j,k 組合是否和為零。 | Approach |
| Time O(n^3), which is too slow. | 時間 O(n^3)，明顯過慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First sort nums to enable two-pointer scan. | 先排序 nums，才能做雙指標掃描。 | Approach |
| Fix i, then solve two-sum on the right side. | 固定 i，再在右側解 two-sum。 | Approach |
| If nums[i] is positive, we can break early. | 若 nums[i] 已為正，可提早結束。 | Approach |
| Skip duplicate i and duplicate left values. | 跳過重複的 i 與重複 left 值。 | Approach |
| Total time O(n^2), extra space mainly sort overhead. | 總時間 O(n^2)，額外空間主要是排序開銷。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I sort the array in non-decreasing order. | 先把陣列做非遞減排序。 | Coding |
| Then I loop i from zero to n minus one. | 然後 i 從 0 走到 n-1。 | Coding |
| If i is duplicate, I continue to next i. | 若 i 重複，我直接 continue。 | Coding |
| I set left to i plus one and right to end. | 我把 left 設 i+1，right 設尾端。 | Coding |
| Compute sum equals nums[i] plus nums[left] plus nums[right]. | 計算 sum = nums[i]+nums[left]+nums[right]。 | Coding |
| If sum too small, move left rightward. | sum 太小就 left 往右。 | Coding |
| If sum too large, move right leftward. | sum 太大就 right 往左。 | Coding |
| If sum is zero, record triplet and move both. | sum 為零就記錄並移動雙指標。 | Coding |
| After match, skip duplicate left values. | 命中後要跳過重複 left 值。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run minus one, zero, one, two, minus one, minus four. | 我手跑 -1,0,1,2,-1,-4。 | Dry-run |
| After sorting, array is minus four, minus one, minus one, zero, one, two. | 排序後是 -4,-1,-1,0,1,2。 | Dry-run |
| Fix i at minus one, target two-sum is plus one. | 固定 i=-1，two-sum 目標是 +1。 | Dry-run |
| left at minus one and right at two gives zero sum triplet. | left=-1、right=2 時可湊出零和三元組。 | Dry-run |
| Record minus one, minus one, two. | 記錄 -1,-1,2。 | Dry-run |
| Move pointers and find minus one, zero, one. | 移動指標後找到 -1,0,1。 | Dry-run |
| Dedup rules prevent repeated triplets. | 去重規則可避免重複三元組。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: all zeros like [0,0,0,0]. | 案例一：全零如 [0,0,0,0]。 | Edge test |
| Case two: no solution like [1,2,-2,-1]. | 案例二：無解如 [1,2,-2,-1]。 | Edge test |
| Case three: heavy duplicates around same value. | 案例三：同值附近大量重複。 | Edge test |
| Case four: exactly one triplet exists. | 案例四：只有一組三元組。 | Edge test |
| Case five: mixed large positive and negative numbers. | 案例五：大正負值混合。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n^2). | 時間是 O(n^2)。 | Complexity |
| Extra space is O(1) besides sort stack and output. | 除排序堆疊與輸出外，額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting costs O(n log n) first. | 排序先花 O(n log n)。 | Complexity |
| Outer loop is O(n) and inner scan is O(n). | 外層 O(n)，內層掃描 O(n)。 | Complexity |
| So dominant runtime is O(n^2). | 所以主導時間是 O(n^2)。 | Complexity |
| Dedup checks do not change big-O complexity. | 去重檢查不改變 big-O 複雜度。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me recheck dedup conditions first. | 我先重檢去重條件。 | If stuck |
| I can explain brute force baseline quickly. | 我可先快速說明暴力基線。 | If stuck |
| Then I switch to sorted two pointers. | 然後切到排序雙指標。 | If stuck |
| I forgot one duplicate-skip line. | 我一時忘了一行去重。 | If stuck |
| Core triplet logic is still clear. | 核心三元組邏輯仍清楚。 | If stuck |
| Thanks, I will adjust this pointer move. | 謝謝，我會調整這次指標移動。 | If stuck |
| I found why duplicate triplets appeared. | 我找到重複三元組出現原因。 | If stuck |
| Let me rerun one sample quickly. | 我快速重跑一個範例。 | If stuck |
| Now unique output is correct. | 現在唯一輸出正確了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| Sorting and two pointers handle efficiency well. | 排序加雙指標可有效提升效率。 | Wrap-up |
| Dedup logic keeps output unique. | 去重邏輯能確保輸出唯一。 | Wrap-up |
| Time is O(n^2), with low extra memory. | 時間 O(n^2)，額外記憶體很低。 | Wrap-up |
| I can discuss 4Sum extension if needed. | 若需要我可延伸到 4Sum。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate unique-triplet sum-zero goal. | 重述唯一三元組和為零目標。 | Cheat sheet |
| Mention duplicates are the hard part. | 提到重複去除是難點。 | Cheat sheet |
| Baseline O(n^3) is too slow. | 基線 O(n^3) 太慢。 | Cheat sheet |
| Sort array first. | 先做陣列排序。 | Cheat sheet |
| Fix i, run two pointers on suffix. | 固定 i，在後綴跑雙指標。 | Cheat sheet |
| Skip duplicate i values. | 跳過重複的 i。 | Cheat sheet |
| Break early when nums[i] > 0. | nums[i] > 0 時提早結束。 | Cheat sheet |
| Move left or right by sum sign. | 依 sum 正負移動左右指標。 | Cheat sheet |
| On match, record triplet. | 命中時記錄三元組。 | Cheat sheet |
| After match, skip duplicate left values. | 命中後跳過重複 left。 | Cheat sheet |
| Dry-run [-1,0,1,2,-1,-4]. | 手跑 [-1,0,1,2,-1,-4]。 | Cheat sheet |
| Verify all-zero input case. | 驗證全零輸入案例。 | Cheat sheet |
| Verify no-solution input case. | 驗證無解輸入案例。 | Cheat sheet |
| Report O(n^2) runtime. | 報告 O(n^2) 時間。 | Cheat sheet |
| Mention sorting overhead O(n log n). | 提及排序開銷 O(n log n)。 | Cheat sheet |
| Explain dedup invariant clearly. | 清楚解釋去重不變量。 | Cheat sheet |
| If stuck, restate pointer roles. | 卡住時重述指標角色。 | Cheat sheet |
| Keep output unique and sorted-friendly. | 保持輸出唯一且符合排序邏輯。 | Cheat sheet |
| End with complexity summary. | 以複雜度總結收尾。 | Cheat sheet |
| Offer follow-up on 3Sum variants. | 提供 3Sum 變體延伸。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sorting + two-pointer with dedup is preserved.
- No hallucinated constraints: ✅ Uncertain requirements are handled in clarification lines.
- Language simplicity: ✅ Short spoken lines for interview delivery.
