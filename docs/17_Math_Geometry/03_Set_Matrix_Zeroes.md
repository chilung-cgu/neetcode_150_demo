# Set Matrix Zeroes (矩陣置零) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #73** — [題目連結](https://leetcode.com/problems/set-matrix-zeroes/) | [NeetCode 解說](https://neetcode.io/problems/set-matrix-zeroes)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的矩陣。如果一個元素是 `0`，則將其所在的整行和整列都設為 `0`。
請 **原地 (in-place)** 進行操作。

-   **Input**:
    ```
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    ```

-   **Output**:
    ```
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    ```

-   **Constraints**:
    -   Space Complexity: $O(1)$ is best, $O(m+n)$ is acceptable.

---

## 2. 🐢 Brute Force Approach (暴力解)

-   創建一個副本矩陣 `copy`。
-   遍歷原矩陣，如果 `matrix[i][j] == 0`，則在 `copy` 中將第 `i` 行和第 `j` 列設為 `0`。
-   但這樣不是 in-place，或者說需要 $O(m \times n)$ 空間。

或者使用 $O(m+n)$ 空間：

-   用兩個集合 `rows` 和 `cols` 記錄哪些行/列需要變為 0。
-   再次遍歷矩陣，如果 `i` 在 `rows` 或 `j` 在 `cols` 中，設為 0。

---

## 3. 💡 The "Aha!" Moment (優化)

**Using First Row/Col as Flags (O(1) Space)**:
我們可以用矩陣的 **第一行** 和 **第一列** 來替代上面的 `rows` 和 `cols` 集合。
但要注意：`(0,0)` 位置既屬於第一行也屬於第一列，需要特殊處理。

**Algorithm**:

1.  **Flag Row0**: 檢查第一行是否有 0，設置布林變量 `rowZero`。
2.  **Flag Col0**: 檢查第一列是否有 0，設置布林變量 `colZero`。
3.  **Mark**: 遍歷剩下的矩陣 `(1..m-1, 1..n-1)`。如果 `matrix[i][j] == 0`，則將對應的行首 `matrix[i][0]` 和列首 `matrix[0][j]` 設為 `0`。
4.  **Set Zeroes**: 再次遍歷 `(1..m-1, 1..n-1)`。如果行首或列首是 0，則將 `matrix[i][j]` 設為 0。
5.  **Handle First Row/Col**:
    -   如果 `colZero` 為真，將第一列全設為 0。
    -   如果 `rowZero` 為真，將第一行全設為 0。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../set_matrix_zeroes_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../set_matrix_zeroes_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: O(1) Space

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        bool rowZero = false;
        bool colZero = false;

        // 1. Check if first row has zero
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                rowZero = true;
                break;
            }
        }

        // 2. Check if first col has zero
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                colZero = true;
                break;
            }
        }

        // 3. Mark zeroes in first row/col
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // 4. Set zeroes based on marks
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // 5. Handle first row/col
        if (colZero) {
            for (int i = 0; i < m; i++) matrix[i][0] = 0;
        }

        if (rowZero) {
            for (int j = 0; j < n; j++) matrix[0][j] = 0;
        }
    }
};
```

### Python Reference

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Fill zeroes except first row/col
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Handle first col (using matrix[0][0])
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Handle first row (using rowZero var)
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        bool rowZero = false; // 紀錄第一行原本是否包含 0
        bool colZero = false; // 紀錄第一列原本是否包含 0

        // 1. 檢查第一行
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                rowZero = true;
                break;
            }
        }

        // 2. 檢查第一列
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                colZero = true;
                break;
            }
        }

        // 3. 使用第一行和第一列作為標記空間
        // 從 (1,1) 開始遍歷內部矩陣
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0; // 將對應的行首標記為 0
                    matrix[0][j] = 0; // 將對應的列首標記為 0
                }
            }
        }

        // 4. 根據標記，將內部矩陣置零
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // 5. 最後處理第一列和第一行
        // 注意順序：雖然這裡互不影響，但邏輯上分開處理更清晰
        if (colZero) {
            for (int i = 0; i < m; i++) matrix[i][0] = 0;
        }

        if (rowZero) {
            for (int j = 0; j < n; j++) matrix[0][j] = 0;
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   We iterate through the matrix a constant number of times.
-   **Space Complexity**: $O(1)$
    -   We use the input matrix itself for storage.
