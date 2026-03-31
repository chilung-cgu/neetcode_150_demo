# 03 Set Matrix Zeroes — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/03_Set_Matrix_Zeroes.md`

> Quick links: [Source Solution](../03_Set_Matrix_Zeroes.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Set Matrix Zeroes. | 我先重述 Set Matrix Zeroes。 | Restatement |
| We have an m by n matrix. | 題目給一個 m x n 矩陣。 | Restatement |
| If one cell is zero, its whole row and column must become zero. | 若某格是 0，整列整欄都要設成 0。 | Restatement |
| The operation must be in place. | 操作必須是原地進行。 | Restatement |
| I will use first row and first column as marker storage. | 我會用第一列與第一欄當標記空間。 | Restatement |
| That gives O(mn) time and O(1) extra space. | 這樣可達 O(mn) 時間與 O(1) 額外空間。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is in-place O(1) extra space mandatory? | 是否必須原地且 O(1) 額外空間？ | Clarify |
| Can matrix include negative values? | 矩陣元素可包含負數嗎？ | Clarify |
| Will matrix size always be at least one by one? | 矩陣大小是否至少 1x1？ | Clarify |
| Should I mutate input directly without returning new matrix? | 是否直接修改輸入而不回傳新矩陣？ | Clarify |
| Is any order of zeroing acceptable as long as final state is correct? | 只要最終狀態正確，處理順序都可嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force uses sets to store rows and columns containing zero. | 暴力法用集合記錄要清零的列與欄。 | Approach |
| Second pass sets cell to zero if row or column is marked. | 第二輪若列或欄被標記就設 0。 | Approach |
| It is O(mn) time but O(m plus n) extra space. | 這是 O(mn) 時間、O(m+n) 空間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use matrix first row and first column as marker arrays. | 用矩陣第一列和第一欄充當標記陣列。 | Approach |
| First detect whether row zero and column zero originally contain any zero. | 先判斷原本第一列、第一欄是否含 0。 | Approach |
| For inner cells, when matrix[i][j] is zero, mark matrix[i][0] and matrix[0][j]. | 內部若 matrix[i][j]=0，就標記 matrix[i][0] 和 matrix[0][j]。 | Approach |
| Zero inner cells based on markers, then handle first column and first row last. | 依標記清內部，最後再處理第一欄與第一列。 | Approach |
| This preserves markers correctly and stays O(1) extra space. | 這可保留標記正確且維持 O(1) 額外空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I get rows and cols from matrix dimensions. | 我先取 rows 和 cols。 | Coding |
| I define booleans rowZero and colZero. | 我定義 rowZero 與 colZero。 | Coding |
| I scan first row to set rowZero. | 我先掃第一列設定 rowZero。 | Coding |
| I scan first column to set colZero. | 我再掃第一欄設定 colZero。 | Coding |
| I traverse inner cells from one-one onward. | 接著走內部格子從 (1,1) 開始。 | Coding |
| If an inner cell is zero, I mark its row head and column head zero. | 若內部是 0，就把對應列首欄首標成 0。 | Coding |
| I run second inner pass and zero by row or column marker. | 第二輪內部依列首或欄首標記清零。 | Coding |
| If colZero is true, I zero entire first column. | 若 colZero 為真，第一欄全清零。 | Coding |
| If rowZero is true, I zero entire first row. | 若 rowZero 為真，第一列全清零。 | Coding |
| Then function ends with matrix modified in place. | 最後函式結束，矩陣已原地更新。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [[1,1,1],[1,0,1],[1,1,1]]. | 我用 [[1,1,1],[1,0,1],[1,1,1]] 手跑。 | Dry-run |
| First row and first column initially have no zero. | 第一列與第一欄一開始都沒有 0。 | Dry-run |
| Inner scan finds zero at row one col one, so mark row one head and col one head. | 內部掃到 (1,1)=0，標記列首與欄首。 | Dry-run |
| Second inner pass zeros cells in marked row or column. | 第二輪把被標記列欄的內部格清零。 | Dry-run |
| rowZero and colZero are false, so first row and column stay as is unless marked cells require. | rowZero、colZero 皆 false，首列首欄不額外全清。 | Dry-run |
| Final matrix is [[1,0,1],[0,0,0],[1,0,1]]. | 最終矩陣是 [[1,0,1],[0,0,0],[1,0,1]]。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: zero appears in first row. | 案例一：0 出現在第一列。 | Edge test |
| Case two: zero appears in first column. | 案例二：0 出現在第一欄。 | Edge test |
| Case three: one-by-one matrix with zero. | 案例三：1x1 且值為 0。 | Edge test |
| Case four: one-by-one matrix without zero. | 案例四：1x1 且值非 0。 | Edge test |
| Case five: multiple zeros in different rows and columns. | 案例五：多個 0 分散在不同列欄。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan first row, first column, and inner matrix with constant work each cell. | 我們掃首列、首欄與內部，每格做常數工作。 | Complexity |
| Total processed cells are proportional to m times n. | 總處理格數與 m*n 成正比。 | Complexity |
| So runtime is O(m times n). | 因此時間是 O(m*n)。 | Complexity |
| Marker storage reuses input matrix plus two booleans, so extra memory is O(1). | 標記重用輸入矩陣外加兩個布林，額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate marker phase and write phase. | 我先把標記階段和寫回階段分開。 | If stuck |
| First row and first column can store row and column flags. | 第一列與第一欄可存列欄旗標。 | If stuck |
| I must track original first row and first column zeros separately. | 我必須另外記錄首列首欄原始是否有 0。 | If stuck |
| Otherwise marker information gets overwritten. | 否則標記資訊會互相覆蓋。 | If stuck |
| Inner scan starts at index one to avoid touching flag row and col too early. | 內部掃描從索引 1 開始，避免太早破壞旗標。 | If stuck |
| After marking, inner write pass follows markers only. | 標記完後，內部寫回只看旗標。 | If stuck |
| First column and first row are handled last. | 第一欄與第一列最後處理。 | If stuck |
| Let me test a case where first row has zero. | 我測一個首列有 0 的案例。 | If stuck |
| Then test a case where first column has zero. | 再測首欄有 0 的案例。 | If stuck |
| Great, now corner behavior is correct. | 很好，角落情況現在正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with first-row and first-column markers. | 我用首列首欄標記法解題。 | Wrap-up |
| The two-phase flow keeps in-place correctness. | 兩階段流程可維持原地正確性。 | Wrap-up |
| Separate booleans protect first row and column edge cases. | 額外布林可保護首列首欄邊界情況。 | Wrap-up |
| Complexity is O(mn) time and O(1) extra space. | 複雜度為 O(mn) 時間、O(1) 額外空間。 | Wrap-up |
| This is the standard interview-optimal solution. | 這是面試中標準且最佳的解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: zero full row and column when a cell is zero. | 目標：遇到 0 就清該列與該欄。 | Cheat sheet |
| Must do it in place. | 必須原地完成。 | Cheat sheet |
| Use first row and first column as markers. | 用首列首欄當標記。 | Cheat sheet |
| Track rowZero and colZero separately. | 另外追蹤 rowZero、colZero。 | Cheat sheet |
| Scan first row for rowZero. | 掃首列決定 rowZero。 | Cheat sheet |
| Scan first column for colZero. | 掃首欄決定 colZero。 | Cheat sheet |
| Mark inner zeros into row and column heads. | 內部遇 0 就標記列首欄首。 | Cheat sheet |
| Second pass zero inner cells by markers. | 第二輪依標記清內部。 | Cheat sheet |
| Handle first column if colZero true. | 若 colZero=true，清首欄。 | Cheat sheet |
| Handle first row if rowZero true. | 若 rowZero=true，清首列。 | Cheat sheet |
| Done in O(mn) time. | 時間 O(mn)。 | Cheat sheet |
| Extra space O(1). | 額外空間 O(1)。 | Cheat sheet |
| Common bug: forgetting separate first-row state. | 常見錯誤：忘記首列需獨立狀態。 | Cheat sheet |
| Common bug: updating first row/col too early. | 常見錯誤：太早改動首列首欄。 | Cheat sheet |
| Start inner loops from index one. | 內部迴圈從 1 開始。 | Cheat sheet |
| Test first-row-zero case. | 測首列含 0 案例。 | Cheat sheet |
| Test first-column-zero case. | 測首欄含 0 案例。 | Cheat sheet |
| Test single-cell matrices. | 測單格矩陣。 | Cheat sheet |
| Speak marker/write phases clearly. | 口述時清楚分標記與寫回。 | Cheat sheet |
| Interview-safe and deterministic. | 面試表達穩定且可驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ First row/column marker strategy.
- Constraint alignment: ✅ In-place and O(1) extra memory.
- Language simplicity: ✅ Clear and concise interview phrasing.
