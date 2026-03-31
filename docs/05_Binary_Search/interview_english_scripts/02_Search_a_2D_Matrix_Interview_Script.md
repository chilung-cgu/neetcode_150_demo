# 02 Search a 2D Matrix — Interview English Script (C++)

> Source aligned with: `docs/05_Binary_Search/02_Search_a_2D_Matrix.md`

> Quick links: [Source Solution](../02_Search_a_2D_Matrix.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the matrix search problem. | 我先重述矩陣搜尋題。 | Restatement |
| Each row is sorted from left to right. | 每一列都由左到右遞增。 | Restatement |
| First value of each row is larger than previous row end. | 每列首值都大於上一列末值。 | Restatement |
| So the whole matrix is like one sorted 1D array. | 所以整體可視為一個排序 1D 陣列。 | Restatement |
| I only need to return true or false for target existence. | 我只要回傳 target 是否存在。 | Restatement |
| I will use binary search with index mapping. | 我會用二分搜尋加索引映射。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume matrix dimensions are both at least one? | 我可以假設矩陣列數與行數都至少 1 嗎？ | Clarify |
| Is target always an integer in valid range? | target 是否一定是合法整數？ | Clarify |
| Should I avoid extra matrix flattening space? | 是否希望我避免額外展平空間？ | Clarify |
| Is O(log(m*n)) the target complexity expectation? | 預期複雜度是 O(log(m*n)) 嗎？ | Clarify |
| Are duplicate numbers impossible by matrix property? | 依題目性質可視為不會跨列重複嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline scans every element in all rows. | 基線作法是掃描所有元素。 | Approach |
| Compare each cell with target directly. | 逐格與 target 比較。 | Approach |
| Time is O(m*n), space is O(1). | 時間 O(m*n)，空間 O(1)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Treat index range as 0 to m*n minus one. | 把索引範圍視為 0 到 m*n-1。 | Approach |
| Mid index maps to row equals mid divided by n. | mid 對應列是 mid/n。 | Approach |
| Column maps to mid modulo n. | 欄位對應是 mid%n。 | Approach |
| Compare mapped value and shrink search interval normally. | 比較映射值後正常收縮區間。 | Approach |
| This gives O(log(m*n)) time and O(1) space. | 可達 O(log(m*n)) 時間與 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I read row count m and column count n. | 先讀出列數 m 與欄數 n。 | Coding |
| I set left to zero and right to m times n minus one. | left 設 0，right 設 m*n-1。 | Coding |
| I loop while left is less than or equal to right. | 當 left<=right 持續迴圈。 | Coding |
| I compute mid with overflow-safe formula. | 用防溢位公式計算 mid。 | Coding |
| I map mid to row and column indices. | 把 mid 映射成 row 與 col。 | Coding |
| I read matrix[row][col] and compare with target. | 讀取 matrix[row][col] 與 target 比較。 | Coding |
| I move left or right just like standard binary search. | 像標準二分一樣更新 left/right。 | Coding |
| If found return true, otherwise return false after loop. | 找到回傳 true，否則回傳 false。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run matrix [[1,3,5,7],[10,11,16,20],[23,30,34,60]] with target 3. | 我手跑 matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]、target=3。 | Dry-run |
| m is 3, n is 4, so right starts at 11. | m=3、n=4，所以 right 起始為 11。 | Dry-run |
| First mid is 5, mapped value is 11, too large. | 第一次 mid=5，映射值 11，太大。 | Dry-run |
| Move right to 4, then mid is 2, mapped value is 5. | right 移到 4，接著 mid=2，值是 5。 | Dry-run |
| Five is still too large, move right to 1. | 5 還是太大，right 移到 1。 | Dry-run |
| Mid becomes 0 then 1, and value at 1 is 3. | mid 變 0 再變 1，索引 1 的值是 3。 | Dry-run |
| Target found, return true. | 找到 target，回傳 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one cell matrix where value equals target. | 案例一：單格矩陣且值等於 target。 | Edge test |
| Case two: one cell matrix where value differs. | 案例二：單格矩陣且值不等於 target。 | Edge test |
| Case three: target smaller than global minimum. | 案例三：target 小於全域最小值。 | Edge test |
| Case four: target larger than global maximum. | 案例四：target 大於全域最大值。 | Edge test |
| Case five: target is first or last matrix element. | 案例五：target 是首元素或尾元素。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(log(m*n)). | 時間複雜度是 O(log(m*n))。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Search space size is exactly m times n elements. | 搜尋空間大小正好是 m*n 個元素。 | Complexity |
| Binary search halves that space each iteration. | 二分搜尋每輪都把空間砍半。 | Complexity |
| Index mapping uses only arithmetic operations. | 索引映射只用算術運算。 | Complexity |
| No extra array or hash structure is allocated. | 沒有建立額外陣列或雜湊結構。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I verify the row and column mapping formula? | 我可以先確認 row/col 映射公式嗎？ | If stuck |
| Row should be mid divided by number of columns. | row 應該是 mid 除以欄數。 | If stuck |
| Column should be mid modulo number of columns. | col 應該是 mid 對欄數取餘。 | If stuck |
| I will test mapping with one concrete mid value. | 我用一個 mid 實值測試映射。 | If stuck |
| Let me also check left and right updates. | 我再檢查 left/right 更新。 | If stuck |
| If value is smaller, I must move left to mid plus one. | 值較小時，left 必須到 mid+1。 | If stuck |
| If value is larger, I must move right to mid minus one. | 值較大時，right 必須到 mid-1。 | If stuck |
| I think I fixed the index conversion bug. | 我想我修好了索引轉換 bug。 | If stuck |
| Let me rerun the sample once. | 我再重跑一次範例。 | If stuck |
| Great, the boolean result is now correct. | 很好，布林結果現在正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed the virtual-1D binary search solution. | 我完成了虛擬 1D 二分解法。 | Wrap-up |
| I verified mapping and boundary conditions. | 我驗證了索引映射與邊界條件。 | Wrap-up |
| Runtime is O(log(m*n)). | 時間複雜度是 O(log(m*n))。 | Wrap-up |
| Extra memory is O(1). | 額外記憶體是 O(1)。 | Wrap-up |
| I can also explain two-phase row-plus-column search. | 我也可補充先找列再找欄的作法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Matrix has global sorted order by row rule. | 矩陣依規則具全域排序性。 | Cheat sheet |
| Need boolean existence for target. | 目標是回傳 target 是否存在。 | Cheat sheet |
| Brute force scans all cells O(m*n). | 暴力掃全部格子 O(m*n)。 | Cheat sheet |
| Better use binary search on virtual index. | 改用虛擬索引做二分。 | Cheat sheet |
| left = 0, right = m*n-1. | left=0，right=m*n-1。 | Cheat sheet |
| mid = left + (right-left)/2. | mid=left+(right-left)/2。 | Cheat sheet |
| row = mid / n. | row=mid/n。 | Cheat sheet |
| col = mid % n. | col=mid%n。 | Cheat sheet |
| value = matrix[row][col]. | value=matrix[row][col]。 | Cheat sheet |
| If equal, return true. | 相等就回傳 true。 | Cheat sheet |
| If value < target, move left. | value<target 就移動 left。 | Cheat sheet |
| Else move right. | 否則移動 right。 | Cheat sheet |
| End loop means not found. | 迴圈結束代表沒找到。 | Cheat sheet |
| Return false then. | 那時回傳 false。 | Cheat sheet |
| Test one-cell hit and miss. | 測單格命中與未命中。 | Cheat sheet |
| Test smaller-than-min and larger-than-max. | 測小於最小與大於最大。 | Cheat sheet |
| Time O(log(m*n)). | 時間 O(log(m*n))。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: wrong row/col mapping. | 常見 bug：row/col 映射寫錯。 | Cheat sheet |
| Common bug: wrong boundary update. | 常見 bug：邊界更新寫錯。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Virtual 1D mapping binary search is preserved.
- No hallucinated constraints: ✅ Script follows source matrix properties.
- Language simplicity: ✅ Short interview-safe spoken lines.
