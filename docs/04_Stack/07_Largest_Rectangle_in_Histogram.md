# Largest Rectangle in Histogram (直方圖中的最大矩形)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `heights`，代表直方圖中每個柱子的高度（寬度為 1）。
請找出直方圖中最大的矩形面積。

-   **Input**: `[2,1,5,6,2,3]`
-   **Output**: `10`
    -   解釋：由此圖能看到，index 2 和 3 的高度分別是 5 和 6。
    -   我們可以取出一個高度為 5、寬度為 2 的矩形（涵蓋 index 2, 3）。面積 10。
    -   或者高度為 6 的矩形（只含 index 3），面積 6。
    -   或者高度為 2 的矩形（涵蓋 index 2, 3, 4, 5），面積 2 * 4 = 8。
-   **Constraints**:
    -   $1 <= heights.length <= 10^5$.
    -   $0 <= heights[i] <= 10^4$.

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一根柱子 `i`，我們把它當作是「矩形的高度」，然後盡可能的往左和往右延伸，直到遇到比它矮的柱子為止。

-   `width = right_limit - left_limit - 1`
-   `area = heights[i] * width`
-   **Time**: $O(n^2)$。
-   **Result**: TLE。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是單調棧 (**Monotonic Stack**) 的終極應用。

**核心觀念**：
當我們遍歷柱子時，如果當前柱子 `h` 比前一個柱子 `prev_h` **高**，那麼 `prev_h` 還不能結算——因為它還可以繼續向右延伸！
但如果當前柱子 `h` 比前一個柱子 `prev_h` **矮**，那麼 `prev_h` 的延伸就到此為止了。因為 `h` 卡住了它。
這時候，我們就可以結算以 `prev_h` 為高度的矩形面積。

**演算法**：

1.  維護一個 Stack，存 `(index, height)`。保持 Stack 中的高度 **單調遞增**。
2.  遍歷每個柱子 `current_h` at `i`：
    -   while Stack 頂端的高度 `stack_h > current_h`：
        -   **Pop**: 這根柱子被當前柱子 `h` 擋住了，可以結算了。
        -   **Height**: `H = stack_h`
        -   **Width**:
            -   右邊界是 `i` (因為是 `i` 把這根柱子擋住的)。
            -   左邊界呢？是 Stack 中新的頂端元素！
            -   為什麼？因為我們是單調遞增棧，Stack 中新的 Top 一定是當初擋住 `H` 往左延伸的那個矮柱子 (或者說是 `H` 左邊第一個比它矮的)。
            -   所以 `W = i - stack.top().index - 1`。
        -   `MaxArea = max(MaxArea, H * W)`。
    -   Push `i` 入 Stack。
3.  **剩餘處理**：遍歷結束後，Stack 中可能還有殘留元素（這些柱子一直延伸到最右邊都没被挡住）。
    -   對這些元素做同樣的結算，右邊界視為 `n`。

---

## 4. 💻 Implementation (程式碼)

### Approach: Monotonic Stack

```cpp
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> s; // stores indices
        int maxArea = 0;

        for (int i = 0; i <= n; i++) {
            // 為了方便處理剩餘元素，我們假設最後有一個高度為 0 的柱子
            // 這會強迫 stack 中所有元素都被 pop 出來結算
            int currentHeight = (i == n) ? 0 : heights[i];

            while (!s.empty() && heights[s.top()] > currentHeight) {
                int h = heights[s.top()];
                s.pop();

                // 計算寬度
                // 如果 stack 空了，代表 h 是目前為止最矮的，它可以延伸到最左邊 (-1)
                // 否則，它的左邊界是 s.top()
                int w = s.empty() ? i : i - s.top() - 1;

                maxArea = max(maxArea, h * w);
            }

            s.push(i);
        }

        return maxArea;
    }
};
```

### Python Reference

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

```

**Python Note**: Python 版本用了一種稍微不同的技巧：在 Pop 的時候把當前 index `start` 往左推，意思是一樣的，但 C++ 版本用 `left boundary` 計算更為正規且易於理解。C++ 版本中 `(i == n) ? 0` 的技巧非常實用，能省去最後的 clean up loop。

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int max_area = 0;
        stack<int> indices;

        // 我們遍歷到 n (也就是比陣列大 1 的位置)
        // 並在邏輯上視為 heights[n] = 0。
        // 這個 0 會強迫單調遞增 Stack 中的所有柱子都「遇到更矮的」，從而一個個被 Pop 出來結算。
        for (int i = 0; i <= heights.size(); i++) {
            int h = (i == heights.size()) ? 0 : heights[i];

            // 當前高度 h 小於 Stack Top，破壞了單調遞增性
            // 這時候 Stack Top 那根柱子就到頭了 (被右邊的 h 擋住了)
            while (!indices.empty() && h < heights[indices.top()]) {
                // 1. 取出要結算的那根柱子的高度
                int height = heights[indices.top()];
                indices.pop();

                // 2. 計算寬度
                // Width = Right Boundary - Left Boundary - 1
                // Right Boundary = i (我們當前所在位置)
                // Left Boundary = 新的 indices.top() (因為 Stack 單調遞增，新的 Top 就是舊 Top 左邊第一個比它矮的)
                // 如果 Stack 空了，代表舊 Top 左邊沒有比它矮的了，它可以一直延伸到 index -1。
                int width = indices.empty() ? i : i - indices.top() - 1;

                max_area = max(max_area, height * width);
            }

            indices.push(i);
        }

        return max_area;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   每個柱子最多進 Stack 一次，出 Stack 一次。
-   **Space Complexity**: $O(n)$
    -   最壞情況 (單調遞增陣列)，Stack 會存所有的 indices。
