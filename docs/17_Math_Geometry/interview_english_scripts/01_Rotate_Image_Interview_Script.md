# 01 Rotate Image — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/01_Rotate_Image.md`

> Quick links: [Source Solution](../01_Rotate_Image.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Rotate Image. | 我先重述 Rotate Image。 | Restatement |
| We are given an n by n matrix. | 題目給一個 n x n 矩陣。 | Restatement |
| We need to rotate it ninety degrees clockwise. | 要把它順時針旋轉 90 度。 | Restatement |
| We must do it in place with no extra matrix. | 必須原地做，不能開新矩陣。 | Restatement |
| My plan is transpose first, then reverse each row. | 我的做法是先轉置，再反轉每一列。 | Restatement |
| I will explain why this exactly gives clockwise rotation. | 我會解釋這樣為何剛好是順時針旋轉。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume the matrix is always square? | 我可以假設矩陣一定是方陣嗎？ | Clarify |
| Is in-place strictly required with O(1) extra space? | 是否嚴格要求 O(1) 額外空間？ | Clarify |
| Are values unrestricted, including negatives? | 元素是否可為任意整數含負數？ | Clarify |
| For n equals one, should we just return unchanged? | n=1 是否直接原樣回傳？ | Clarify |
| Do you want clockwise only, not counterclockwise? | 只需要順時針，不是逆時針嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A direct method is building another n by n matrix. | 直覺法是新建一個 n x n 矩陣。 | Approach |
| Put old[i][j] into new[j][n minus one minus i]. | 將 old[i][j] 放到 new[j][n-1-i]。 | Approach |
| It is O(n squared) time and O(n squared) space, so not in place. | 這是 O(n²) 時間、O(n²) 空間，不符原地要求。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First transpose the matrix across the main diagonal. | 先沿主對角線做轉置。 | Approach |
| That swaps matrix[i][j] with matrix[j][i] for j greater than i. | 對 j>i 交換 matrix[i][j] 和 matrix[j][i]。 | Approach |
| Then reverse every row in place. | 接著原地反轉每一列。 | Approach |
| Transpose turns rows into columns, row reverse fixes clockwise direction. | 轉置把行變列，反轉列可修正成順時針方向。 | Approach |
| Complexity is O(n squared) time and O(1) extra space. | 複雜度是 O(n²) 時間、O(1) 額外空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I read n as matrix size. | 我先取 n 為矩陣大小。 | Coding |
| I loop i from zero to n minus one. | i 從 0 迴圈到 n-1。 | Coding |
| For each i, I loop j from i plus one to n minus one. | 每個 i 之下，j 從 i+1 到 n-1。 | Coding |
| I swap matrix[i][j] and matrix[j][i] to transpose. | 我交換 matrix[i][j] 與 matrix[j][i] 完成轉置。 | Coding |
| After transpose, I iterate each row. | 轉置後我逐列處理。 | Coding |
| I reverse the row with two pointers or std::reverse. | 我用雙指標或 std::reverse 反轉該列。 | Coding |
| All operations mutate the same matrix, no extra grid allocated. | 全程都改原矩陣，沒開新二維陣列。 | Coding |
| Then I return or finish since function is in-place. | 最後結束函式，因為是原地修改。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run with [[1,2,3],[4,5,6],[7,8,9]]. | 我用 [[1,2,3],[4,5,6],[7,8,9]] 手跑。 | Dry-run |
| After transpose, matrix becomes [[1,4,7],[2,5,8],[3,6,9]]. | 轉置後變成 [[1,4,7],[2,5,8],[3,6,9]]。 | Dry-run |
| Now reverse first row to get [7,4,1]. | 反轉第一列得到 [7,4,1]。 | Dry-run |
| Reverse second row to get [8,5,2]. | 反轉第二列得到 [8,5,2]。 | Dry-run |
| Reverse third row to get [9,6,3]. | 反轉第三列得到 [9,6,3]。 | Dry-run |
| Final matrix is [[7,4,1],[8,5,2],[9,6,3]]. | 最終矩陣是 [[7,4,1],[8,5,2],[9,6,3]]。 | Dry-run |
| This matches expected clockwise rotation. | 這和預期順時針旋轉結果一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals one should stay unchanged. | 案例一：n=1 應維持不變。 | Edge test |
| Case two: n equals two validates smallest non-trivial swap. | 案例二：n=2 可驗證最小非平凡交換。 | Edge test |
| Case three: matrix with negative numbers. | 案例三：包含負數元素的矩陣。 | Edge test |
| Case four: matrix with duplicate values. | 案例四：有重複值的矩陣。 | Edge test |
| Case five: larger n to confirm every layer rotates correctly. | 案例五：較大 n 確認各層旋轉皆正確。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n squared). | 時間複雜度是 O(n²)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Transpose touches roughly half of n squared pairs. | 轉置大約處理 n²/2 組交換。 | Complexity |
| Row reversals together touch all n squared cells once more. | 全部列反轉再處理一次 n² 個元素。 | Complexity |
| Constants differ, but asymptotically it is O(n squared). | 常數不同但漸進仍是 O(n²)。 | Complexity |
| We only use loop indices and swaps, so extra space is O(1). | 只用索引與交換，因此額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me map rotation into two simpler transforms. | 我先把旋轉拆成兩個簡單轉換。 | If stuck |
| A clockwise ninety rotation can be transpose plus row reverse. | 順時針 90 度可拆成轉置加列反轉。 | If stuck |
| I will prove with one coordinate mapping quickly. | 我快速用座標映射證明一次。 | If stuck |
| old i j goes to j n minus one minus i. | old(i,j) 會到 (j,n-1-i)。 | If stuck |
| Transpose gives j i, row reverse gives j n minus one minus i. | 轉置得 (j,i)，列反轉後得 (j,n-1-i)。 | If stuck |
| So the transform is exact, not heuristic. | 所以這是精確轉換，不是猜測。 | If stuck |
| I will now code transpose with j starting at i plus one. | 接著我用 j=i+1 開始寫轉置。 | If stuck |
| Then I reverse each row in place. | 然後把每列原地反轉。 | If stuck |
| Let me test n equals two quickly. | 我快速測一下 n=2。 | If stuck |
| Great, the mapping and code both align. | 很好，映射與程式一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with transpose followed by row reversal. | 我用轉置再列反轉解出此題。 | Wrap-up |
| The method is fully in place and deterministic. | 這個方法完全原地且流程明確。 | Wrap-up |
| It satisfies the in-place requirement cleanly. | 它乾淨地滿足原地限制。 | Wrap-up |
| Complexity is O(n squared) time and O(1) extra space. | 複雜度為 O(n²) 時間、O(1) 額外空間。 | Wrap-up |
| I can also explain the counterclockwise variant if needed. | 若需要我也可補充逆時針版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: rotate n by n matrix clockwise by ninety. | 目標：n x n 矩陣順時針轉 90 度。 | Cheat sheet |
| Must be in place, no extra matrix. | 必須原地，不可開新矩陣。 | Cheat sheet |
| Key formula target is j, n minus one minus i. | 關鍵目標座標是 (j,n-1-i)。 | Cheat sheet |
| Use transpose on main diagonal first. | 先沿主對角線轉置。 | Cheat sheet |
| Swap only when j is greater than i. | 只在 j>i 時交換。 | Cheat sheet |
| Then reverse every row. | 然後反轉每一列。 | Cheat sheet |
| Done, that equals clockwise rotation. | 完成後即為順時針旋轉。 | Cheat sheet |
| n equals one is unchanged. | n=1 不變。 | Cheat sheet |
| n equals two is a good quick sanity test. | n=2 是快速驗證好例子。 | Cheat sheet |
| Duplicates do not affect correctness. | 重複值不影響正確性。 | Cheat sheet |
| Negative values also work identically. | 負數同樣適用。 | Cheat sheet |
| Time is O(n squared). | 時間 O(n²)。 | Cheat sheet |
| Extra space is O(1). | 額外空間 O(1)。 | Cheat sheet |
| Common bug: transposing whole matrix twice by wrong loops. | 常見錯誤：迴圈寫錯導致重複交換。 | Cheat sheet |
| Common bug: reversing columns instead of rows. | 常見錯誤：反轉成欄而非列。 | Cheat sheet |
| Keep loop bounds precise. | 迴圈邊界要精準。 | Cheat sheet |
| Speak mapping while coding. | 寫程式時口述座標映射。 | Cheat sheet |
| Verify with 3 by 3 sample. | 用 3x3 範例驗證。 | Cheat sheet |
| Return after in-place mutation. | 原地修改後即可結束。 | Cheat sheet |
| Clean, interview-friendly explanation. | 這是乾淨的面試友善說法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Transpose + reverse row approach.
- Constraint alignment: ✅ In-place mutation preserved.
- Language simplicity: ✅ Short spoken lines for interview use.
