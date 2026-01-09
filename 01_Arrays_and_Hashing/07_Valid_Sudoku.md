# Valid Sudoku (有效的數獨)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 $9 \times 9$ 的數獨棋盤，要求我們判斷它目前是否有效。
所謂「有效」只需滿足：
1.  每一行 (Row) 必須包含 1-9 不重複。
2.  每一列 (Col) 必須包含 1-9 不重複。
3.  每一個 $3 \times 3$ 的宮格 (Sub-box) 必須包含 1-9 不重複。

-   **Input**: `vector<vector<char>> board`。
-   **Clarification**:
    -   棋盤可能沒填滿 (會有 `.` )。
    -   **我們不需要解數獨**，只需要判斷「現有的數字」有沒有衝突。
    -   即使有效，也不代表這個數獨真的有解 (Is solvable)，這題不在乎 solvable，只在乎 valid。

---

## 2. 🐢 Brute Force Approach (暴力解)

寫三個迴圈分別檢查 Rows, Cols, Boxes。

1.  迴圈 0-8 檢查每一 Row。 -> OK.
2.  迴圈 0-8 檢查每一 Col。 -> OK.
3.  迴圈 0-8 檢查每一 Box。 -> 座標計算比較麻煩。

-   **Time Complexity**: $O(9^2)$ (如果我們視 $N=9$ 為常數，則是 $O(1)$; 如果視 $N$ 為變數，則是 $O(N^2)$)。
-   **問題**: 程式碼會很冗長，要寫三次類似的邏輯。

---

## 3. 💡 The "Aha!" Moment (優化)

我們可以 **只遍歷一次** 棋盤 ($9 \times 9$) 就完成所有檢查嗎？

對於棋盤上的每一個數字 `board[i][j]` (若不為空)，它同時受到三個限制：
1.  它所在的 Row `i`。
2.  它所在的 Col `j`。
3.  它所在的 Box `k`。

我們可以用 **Hash Set** (或 Boolean Array) 來即時記錄這三個維度的狀態。
-   `rows[9][9]`：記錄第 `i` 行是否出現過數字 `num`。
-   `cols[9][9]`：記錄第 `j` 列是否出現過數字 `num`。
-   `boxes[3][3][9]`：記錄第 `r/3`, `c/3` 個 Box 是否出現過數字 `num`。

這樣我們只需要雙層迴圈遍歷 `i` 和 `j`，檢查這三個 Look-up table 即可。

**Boxes Indexing**:
也可以把 $3 \times 3$ 的 boxes 展平成 9 個 index。
`boxIndex = (i / 3) * 3 + (j / 3)`

---

## 4. 💻 Implementation (程式碼)

### Approach: One Pass with Arrays

因為數字只有 1-9，我們可以用固定大小的 Array 代替 Hash Set，速度更快。

```cpp
#include <vector>
#include <cstring> // for memset

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // 使用 boolean array 記錄有沒有出現過
        // 第一維: 哪一個 row/col/box (0-8)
        // 第二維: 哪一個數字 (0-8 代表 '1'-'9')
        bool rows[9][9] = {false};
        bool cols[9][9] = {false};
        bool boxes[9][9] = {false};
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;
                
                int num = board[r][c] - '1'; // 轉成 0-index (0-8)
                int boxIndex = (r / 3) * 3 + (c / 3);
                
                // 檢查是否衝突
                if (rows[r][num] || cols[c][num] || boxes[boxIndex][num]) {
                    return false;
                }
                
                // 標記為已出現
                rows[r][num] = true;
                cols[c][num] = true;
                boxes[boxIndex][num] = true;
            }
        }
        
        return true;
    }
};
```

### Python Reference

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Space Optimization: 使用 int bitmask 甚至可以更省，但 bool array 最清楚
        // rows[i][k] 為 true 代表第 i 行已經有數字 k+1 了
        bool useRow[9][9] = {0};
        bool useCol[9][9] = {0};
        bool useBox[9][9] = {0};

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1'; // char '1'~'9' -> int 0~8
                    
                    // Box index 計算公式
                    // i/3 決定是在 上/中/下 層 (0, 1, 2)
                    // j/3 決定是在 左/中/右 行 (0, 1, 2)
                    // 乘 3 為了把它變成 0~8 的一維 index
                    int k = (i / 3) * 3 + (j / 3);

                    if (useRow[i][num] || useCol[j][num] || useBox[k][num]) {
                        return false; 
                    }
                    
                    useRow[i][num] = true;
                    useCol[j][num] = true;
                    useBox[k][num] = true;
                }
            }
        }
        return true;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(1)$
    -   因為棋盤大小固定是 $9 \times 9 = 81$。我們只遍歷一次。
    -   如果棋盤大小是 $N \times N$，則是 $O(N^2)$。
-   **Space Complexity**: $O(1)$
    -   我們使用了固定大小的 Array (`3 * 9 * 9` booleans)。
    -   如果 $N$ 是變數，則是 $O(N^2)$。

**Bitwise Optimization (Optional)**:
可以使用一個 `int` (32 bits) 來代替 `bool array[9]`，透過 bitmask 來記錄 1-9 的出現狀況。
例如 `row[r] |= (1 << num)`。這樣可以進一步壓縮空間，但在 $9 \times 9$ 規模下差異極小。
