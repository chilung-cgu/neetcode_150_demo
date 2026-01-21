---
title: "Valid Sudoku (有效的數獨)"
description: "題目給一個 $9 \times 9$ 的數獨棋盤，要求我們判斷它目前是否有效。 所謂「有效」只需滿足："
tags:
  - Array
  - Hash Table
difficulty: Medium
---

# Valid Sudoku (有效的數獨) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #36** — [題目連結](https://leetcode.com/problems/valid-sudoku/) | [NeetCode 解說](https://neetcode.io/problems/valid-sudoku)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 $9 \times 9$ 的數獨棋盤，要求我們判斷它目前是否有效。
所謂「有效」只需滿足：

1.  每一行 (Row) 必須包含 1-9 不重複。
2.  每一列 (Col) 必須包含 1-9 不重複。
3.  每一個 $3 \times 3$ 的宮格 (Sub-box) 必須包含 1-9 不重複。

- **Input**: `vector<vector<char>> board`。
- **Clarification**:
  - 棋盤可能沒填滿 (會有 `.` )。
  - **我們不需要解數獨**，只需要判斷「現有的數字」有沒有衝突。
  - 即使有效，也不代表這個數獨真的有解 (Is solvable)，這題不在乎 solvable，只在乎 valid。

---

## 2. 🐢 Brute Force Approach (暴力解)

寫三個迴圈分別檢查 Rows, Cols, Boxes。

1.  迴圈 0-8 檢查每一 Row。 -> OK.
2.  迴圈 0-8 檢查每一 Col。 -> OK.
3.  迴圈 0-8 檢查每一 Box。 -> 座標計算比較麻煩。

- **Time Complexity**: $O(9^2)$ (如果我們視 $N=9$ 為常數，則是 $O(1)$; 如果視 $N$ 為變數，則是 $O(N^2)$)。
- **問題**: 程式碼會很冗長，要寫三次類似的邏輯。

---

## 3. 💡 The "Aha!" Moment (優化)

我們可以 **只遍歷一次** 棋盤 ($9 \times 9$) 就完成所有檢查嗎？

對於棋盤上的每一個數字 `board[i][j]` (若不為空)，它同時受到三個限制：

1.  它所在的 Row `i`。
2.  它所在的 Col `j`。
3.  它所在的 Box `k`。

我們可以用 **Hash Set** (或 Boolean Array) 來即時記錄這三個維度的狀態。

- `rows[9][9]`：記錄第 `i` 行是否出現過數字 `num`。
- `cols[9][9]`：記錄第 `j` 列是否出現過數字 `num`。
- `boxes[3][3][9]`：記錄第 `r/3`, `c/3` 個 Box 是否出現過數字 `num`。

這樣我們只需要雙層迴圈遍歷 `i` 和 `j`，檢查這三個 Look-up table 即可。

**Boxes Indexing**:
也可以把 $3 \times 3$ 的 boxes 展平成 9 個 index。
`boxIndex = (i / 3) * 3 + (j / 3)`

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../valid_sudoku_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../valid_sudoku_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

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
        # 1. 初始化 Hash Maps
        # collections.defaultdict(set): 這是一種特殊的 Dictionary。
        # 當你存取一個不存在的 Key 時，它會自動呼叫 set() 創建一個空的 Hash Set。
        # C++ 類比: 類似 unordered_map<int, unordered_set<char>>，但 Python 會自動處理初始化。
        # 注意: Python 的 set 底層是 Hash Table，對應 C++ 的 std::unordered_set (O(1))，而非 std::set (Red-Black Tree, O(logN))。
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        # key 是一個 Tuple (row_idx, col_idx)，代表 3x3 的區塊座標
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # 跳過空白格
                if board[r][c] == ".":
                    continue

                # 2. 檢查衝突 (Lookup)
                # 語法 check: "val in set" 是 O(1) 操作。
                # C++ 類比: rows[r].find(val) != rows[r].end()
                # 這裡的 key (r // 3, c // 3) 利用了 Tuple 可以被 Hash 的特性
                # 在 C++ 中要用 std::pair 當 unordered_map 的 key 需要手寫 Hash Function，Python 直接支援。
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # 3. 插入記錄 (Insert)
                # set.add() 對應 C++ 的 set.insert()
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

- **Time Complexity**: $O(1)$
  - 因為棋盤大小固定是 $9 \times 9 = 81$。我們只遍歷一次。
  - 如果棋盤大小是 $N \times N$，則是 $O(N^2)$。
- **Space Complexity**: $O(1)$
  - 我們使用了固定大小的 Array (`3 * 9 * 9` booleans)。
  - 如果 $N$ 是變數，則是 $O(N^2)$。

**Bitwise Optimization (Optional)**:
可以使用一個 `int` (32 bits) 來代替 `bool array[9]`，透過 bitmask 來記錄 1-9 的出現狀況。
例如 `row[r] |= (1 << num)`。這樣可以進一步壓縮空間，但在 $9 \times 9$ 規模下差異極小。

## 7. 💻 Other Solutions

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // 優化重點：用 int (32 bits) 代替 bool array
        // 變數說明：
        // rows[i]: 第 i 列的 bitmask，第 k 個 bit 為 1 代表數字 k+1 已出現
        // cols[i]: 第 i 行的 bitmask
        // boxes[i]: 第 i 個九宮格的 bitmask
        // 空間複雜度：從 O(N^2) 降為 O(N) (雖然 N 固定為 9，但概念上更省)
        vector<int> rows(9, 0);
        vector<int> cols(9, 0);
        vector<int> boxes(9, 0);

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                // 遇到空白則跳過
                if (board[r][c] == '.') continue;

                // Step 1: 將字元 '1'-'9' 轉換為整數 0-8
                // 這是為了配合 bit shifting (位移運算)
                int val = board[r][c] - '1';

                // Step 2: 產生 Mask
                // 例如數字是 '3' (val=2)，mask = 1 << 2 = 000...0100 (binary)
                // 只有第 2 個 bit 是 1，其餘為 0
                int mask = 1 << val;

                // Step 3: 計算九宮格索引 (Box Index)
                // 公式解析：
                // (r / 3) * 3 : 決定是哪一層 (Top/Middle/Bottom)，每層跨度為 3
                // (c / 3)     : 決定是哪一列 (Left/Center/Right)
                // 結果範圍 0~8
                int boxIndex = (r / 3) * 3 + (c / 3);

                // Step 4: 衝突檢查 (Bitwise Check)
                // 使用 AND (&) 運算：若 rows[r] 的該 bit 已經是 1，結果就不會是 0
                // 只要 row, col 或 box 任一處有衝突，即回傳 false
                if ((rows[r] & mask) || (cols[c] & mask) || (boxes[boxIndex] & mask)) {
                    return false;
                }

                // Step 5: 更新狀態 (Bitwise Set)
                // 使用 OR (|) 運算：將該 bit 設定為 1，保留其他 bits 不變
                rows[r] |= mask;
                cols[c] |= mask;
                boxes[boxIndex] |= mask;
            }
        }

        return true;
    }
};

```

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如何擴展到解數獨？
- 有沒有更高效的位運算解法？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 3x3 Box 的索引計算錯誤
- ⚠️ 沒有跳過空格 '.'

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 用 bitmask 優化空間
- 💎 正確計算 box index: (r/3)*3 + c/3

---

## 📚 Related Problems (相關題目)

### 站內相關

### 進階挑戰
- [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) — LeetCode
