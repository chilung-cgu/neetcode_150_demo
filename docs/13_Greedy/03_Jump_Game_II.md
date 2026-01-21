# Jump Game II (跳躍遊戲 II) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

給定一個非負整數陣列 `nums`。
最初位於第一個位置。
每個元素代表你可以跳躍的最大長度。
假設你 **一定可以** 到達最後一個位置 (Always possible)。
請找出到達最後一個位置所需的 **最少跳躍次數**。

-   **Input**: `nums = [2,3,1,1,4]`
-   **Output**: `2`
    -   Step 1: 0 -> 1 (Jump size 1, val 3)
    -   Step 2: 1 -> 4 (Jump size 3)
    -   Total 2 jumps.
-   **Input**: `nums = [2,3,0,1,4]`
-   **Output**: `2`
-   **Constraints**:
    -   $1 <= nums.length <= 10^4$
    -   $0 <= nums[i] <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

**BFS (Breadth First Search)**:
將陣列視為圖。每個 index 是節點，能跳到的 index 是鄰居。
求最短路徑 (Unweighted shortest path) -> BFS.

-   Layer 0: index 0
-   Layer 1: indices reachable from Layer 0
-   Layer 2: indices reachable from Layer 1...
-   **Time**: $O(N)$ (if visited optimally) or $O(N^2)$ (if traversing all edges blindly). Edges can be many.

---

## 3. 💡 The "Aha!" Moment (優化)

這其實就是 **BFS 的貪心優化版** (Implicit BFS)。
我們不用真的建立 Queue。
每一層 (Level) 的節點其實是一個 **連續區間 (Range)** `[l, r]`。

-   **第一次跳躍** 能到達的範圍是 `[0, 0]`.
-   **第二次跳躍** 能到達的範圍是 `[1, nums[0]]`. (令其為 `[l, r]`)
-   **第三次跳躍** 能到達的範圍是 `[r + 1, max(i + nums[i])]` for all `i` in `[l, r]`.

策略：

-   我們維護當前能跳到的區間 `[l, r]`。
-   計算從這個區間 `[l, r]` 出發，**最遠** 能跳到哪裡 (設為 `farthest`)。
-   當我們遍歷完 `[l, r]` 後，說明需要多跳一次，才能到達更遠的地方。
-   更新區間：`l = r + 1`, `r = farthest`.
-   步數 `res += 1`.
-   如果不夠，重複。

這種方法只遍歷陣列一次 ($O(N)$)，且空間 $O(1)$。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../jump_game_ii_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../jump_game_ii_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy BFS

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int res = 0;
        int l = 0, r = 0;

        // While current reachable window does not include the last index
        while (r < nums.size() - 1) {
            int farthest = 0;
            // Iterate through current level window to find farthest reach for next level
            for (int i = l; i <= r; i++) {
                farthest = max(farthest, i + nums[i]);
            }

            // Move to next level
            l = r + 1;
            r = farthest;
            res++;
        }

        return res;
    }
};
```

### Python Reference

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        // 結果步數
        int jumps = 0;
        // 當前跳躍次數能覆蓋的範圍 [left, right]
        int l = 0, r = 0;

        // 當覆蓋範圍還沒包含最後一個 index 時，繼續跳
        while (r < nums.size() - 1) {
            int farthest = 0;

            // 遍歷當前層的所有節點，找出下一跳能到達的最遠位置
            for (int i = l; i <= r; i++) {
                farthest = max(farthest, i + nums[i]);
            }

            // 更新範圍到下一層
            // 左邊界變成上一層右邊界 + 1
            l = r + 1;
            // 右邊界變成計算出的最遠距離
            r = farthest;

            // 跳躍次數 + 1
            jumps++;
        }

        return jumps;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   The `l` and `r` window slides forward. Each element is visited at most once.
-   **Space Complexity**: $O(1)$
    -   Constant extra space.
