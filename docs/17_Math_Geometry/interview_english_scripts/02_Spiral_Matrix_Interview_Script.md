# 02 Spiral Matrix — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/02_Spiral_Matrix.md`

> Quick links: [Source Solution](../02_Spiral_Matrix.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Spiral Matrix. | 我先重述 Spiral Matrix。 | Restatement |
| We are given an m by n matrix. | 題目給一個 m x n 矩陣。 | Restatement |
| We must output all elements in clockwise spiral order. | 要順時針螺旋順序輸出所有元素。 | Restatement |
| This is a simulation problem with boundary control. | 這是一題重邊界控制的模擬題。 | Restatement |
| I will use top, bottom, left, and right pointers. | 我會用 top、bottom、left、right 邊界。 | Restatement |
| I will shrink boundaries after each directional pass. | 每走完一個方向就收縮邊界。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can matrix be rectangular, not necessarily square? | 矩陣可長方形，不一定方陣嗎？ | Clarify |
| Should I return values in a one-dimensional list? | 是否回傳一維陣列結果？ | Clarify |
| Are empty matrices possible in input? | 輸入可能是空矩陣嗎？ | Clarify |
| If one row or one column only, same spiral rule applies? | 若只有一列或一欄，規則同樣套用嗎？ | Clarify |
| Any preference between explicit loops and recursion? | 偏好迴圈寫法還是遞迴寫法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| One brute method marks visited cells in a separate matrix. | 一種暴力法是用 visited 矩陣標記已走格子。 | Approach |
| Then we move by direction vectors and turn when blocked. | 再用方向向量移動，撞牆或已訪問就轉向。 | Approach |
| It is O(mn) time and O(mn) extra space. | 其複雜度是 O(mn) 時間、O(mn) 額外空間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use four boundaries to represent current unvisited layer. | 用四個邊界代表目前未訪問外框。 | Approach |
| Traverse top row left to right, then increment top. | 先走上邊由左到右，再 top++。 | Approach |
| Traverse right column top to bottom, then decrement right. | 再走右邊由上到下，再 right--。 | Approach |
| If still valid, traverse bottom row and left column similarly. | 若邊界仍有效，再走下邊與左邊。 | Approach |
| Each element is appended once, giving O(mn) time and O(1) extra space. | 每格只加入一次，故 O(mn) 時間、O(1) 額外空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize result vector and four boundaries. | 我先初始化答案陣列與四個邊界。 | Coding |
| While top is at most bottom and left is at most right, continue. | 當 top<=bottom 且 left<=right 就繼續。 | Coding |
| I scan the top row from left to right. | 我先由左到右掃上邊。 | Coding |
| Then I increment top to remove that row. | 接著 top++，移除已處理上邊。 | Coding |
| I scan the right column from top to bottom. | 再由上到下掃右邊。 | Coding |
| Then I decrement right to remove that column. | 接著 right--，移除已處理右邊。 | Coding |
| I check boundary crossing before bottom and left scans. | 走下邊與左邊前先檢查邊界是否交錯。 | Coding |
| If valid, I scan bottom row right to left and decrement bottom. | 若有效，我走下邊右到左並 bottom--。 | Coding |
| Then I scan left column bottom to top and increment left. | 然後走左邊下到上並 left++。 | Coding |
| Finally return the result vector. | 最後回傳答案陣列。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [[1,2,3],[4,5,6],[7,8,9]]. | 我用 [[1,2,3],[4,5,6],[7,8,9]] 手跑。 | Dry-run |
| First pass top row adds 1,2,3. | 第一段上邊加入 1,2,3。 | Dry-run |
| Right column adds 6,9. | 右邊再加入 6,9。 | Dry-run |
| Bottom row reverse adds 8,7. | 下邊反向加入 8,7。 | Dry-run |
| Left column upward adds 4. | 左邊往上加入 4。 | Dry-run |
| Next inner layer adds remaining center 5. | 下一層內圈再加入中心 5。 | Dry-run |
| Final order is 1,2,3,6,9,8,7,4,5. | 最終順序為 1,2,3,6,9,8,7,4,5。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single cell matrix. | 案例一：單一格矩陣。 | Edge test |
| Case two: one row matrix. | 案例二：只有一列的矩陣。 | Edge test |
| Case three: one column matrix. | 案例三：只有一欄的矩陣。 | Edge test |
| Case four: non-square matrix like three by four. | 案例四：非方陣如 3x4。 | Edge test |
| Case five: empty matrix if input allows. | 案例五：若允許則測空矩陣。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Extra space complexity is O(1), excluding output. | 額外空間複雜度是 O(1)，不含輸出。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Every element is visited and appended exactly once. | 每個元素都只被訪問並加入一次。 | Complexity |
| Boundary updates are constant-time per directional pass. | 每個方向的邊界更新都是常數成本。 | Complexity |
| So total runtime is O(m times n). | 因此總時間是 O(m*n)。 | Complexity |
| We only keep boundaries and loop variables, so extra memory is O(1). | 僅維護邊界與索引，故額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me switch to boundary simulation, it is cleaner. | 我改用邊界模擬會更清楚。 | If stuck |
| I keep four pointers: top, bottom, left, right. | 我維護 top、bottom、left、right 四指標。 | If stuck |
| Order is top row, right column, bottom row, left column. | 順序是上邊、右邊、下邊、左邊。 | If stuck |
| After each pass I shrink the corresponding boundary. | 每段走完收縮對應邊界。 | If stuck |
| I must check crossing before bottom and left passes. | 下邊和左邊前必須檢查是否交錯。 | If stuck |
| That prevents duplicates on single row or single column leftovers. | 這可避免單列單欄時重複加入。 | If stuck |
| I will dry-run a three by three quickly. | 我快速手跑 3x3。 | If stuck |
| If order matches expected, code is likely correct. | 若順序吻合預期，程式多半正確。 | If stuck |
| Then I verify one-row and one-column cases. | 再驗證單列與單欄案例。 | If stuck |
| Great, the control flow is now stable. | 很好，流程控制現在穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with four-boundary spiral simulation. | 我用四邊界螺旋模擬解題。 | Wrap-up |
| The approach handles square and rectangular matrices. | 這方法可處理方陣與長方陣。 | Wrap-up |
| Boundary checks avoid duplicate traversal. | 邊界檢查可避免重複遍歷。 | Wrap-up |
| Complexity is O(mn) time and O(1) extra space. | 複雜度是 O(mn) 時間、O(1) 額外空間。 | Wrap-up |
| I can also provide visited-matrix variant if needed. | 若需要我也可提供 visited 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: output matrix in clockwise spiral order. | 目標：順時針螺旋輸出矩陣。 | Cheat sheet |
| Keep top, bottom, left, right. | 維護 top、bottom、left、right。 | Cheat sheet |
| Loop while top <= bottom and left <= right. | 當 top<=bottom 且 left<=right 持續。 | Cheat sheet |
| Traverse top row left to right. | 走上邊左到右。 | Cheat sheet |
| top plus plus. | top++。 | Cheat sheet |
| Traverse right column top to bottom. | 走右邊上到下。 | Cheat sheet |
| right minus minus. | right--。 | Cheat sheet |
| Check boundary crossing. | 檢查邊界是否交錯。 | Cheat sheet |
| Traverse bottom row right to left. | 走下邊右到左。 | Cheat sheet |
| bottom minus minus. | bottom--。 | Cheat sheet |
| Traverse left column bottom to top. | 走左邊下到上。 | Cheat sheet |
| left plus plus. | left++。 | Cheat sheet |
| Each element appended once. | 每元素只加入一次。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Extra space O(1) excluding output. | 額外空間 O(1)（不含輸出）。 | Cheat sheet |
| Test one-row matrix. | 測單列矩陣。 | Cheat sheet |
| Test one-column matrix. | 測單欄矩陣。 | Cheat sheet |
| Test rectangular matrix. | 測長方矩陣。 | Cheat sheet |
| Common bug: missing boundary check. | 常見錯誤：漏掉邊界檢查。 | Cheat sheet |
| Explain layer-by-layer shrink idea. | 口述一層層收縮的核心概念。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Boundary simulation approach.
- Constraint alignment: ✅ Handles matrix shapes from source discussion.
- Language simplicity: ✅ Interview-ready concise phrasing.
