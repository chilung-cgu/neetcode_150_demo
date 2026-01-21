# Jump Game (跳躍遊戲) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #55** — [題目連結](https://leetcode.com/problems/jump-game/) | [NeetCode 解說](https://neetcode.io/problems/jump-game)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個非負整數陣列 `nums`。
最初位於第一個 index (位置 0)。
陣列中的每個元素代表你在該位置可以跳躍的 **最大長度** (Maximum Jump Length)。
判斷你是否能夠到達最後一個 index。

-   **Input**: `nums = [2,3,1,1,4]`
-   **Output**: `true`
    -   Jump 1 step from 0 to 1 (val 3). Then 3 steps to last index.
-   **Input**: `nums = [3,2,1,0,4]`
-   **Output**: `false`
    -   Will always arrive at index 3 (value 0). Cannot move forward.
-   **Constraints**:
    -   $1 <= nums.length <= 10^4$
    -   $0 <= nums[i] <= 10^5$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Backtracking / Recursion**:
`canJump(i)`: 從 `i` 出發能否到達終點？

-   嘗試從 $1$ 到 $nums[i]$ 所有可能的跳躍長度 $j$。
-   如果 `canJump(i + j)` 為真，則回傳真。
-   **Time**: $O(2^N)$ (或者 $O(N^2)$ with DP memoization)。 $10^4$ 下 $N^2$ 可能會勉強通過，但有更優解。

---

## 3. 💡 The "Aha!" Moment (優化)

**Greedy**:
我們不需要知道具體怎麼跳，只需要維護一個 **「目前能到達的最遠位置」 (furthest reachable index)**。

-   遍歷陣列 `i` from `0` to `n-1`。
-   如果 `i` 超過了目前能到達的最遠位置 (`i > reachable`)，說明此路不通，Return `false`。
-   否則，更新最遠位置：`reachable = max(reachable, i + nums[i])`。
-   如果 `reachable >= n - 1`，Return `true`。

或者反過來思考 (NeetCode 喜歡這種)：
**Shift the Goal Post backward**.

-   目標是到達 `last index` (一開始 goal = n-1)。
-   從後往前遍歷 `i`。
-   如果 `i + nums[i] >= goal`，說明從 `i` 可以跳到 `goal`。
-   那麼現在的目標變成：只要能到達 `i` 即可。更新 `goal = i`。
-   最後檢查 `goal` 是否為 `0`。

這種反向 Greedy 很直觀：我們只需要問「能不能從這裡跳到目前的目標點」。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../jump_game_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../jump_game_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy (Shift Goal Post Backward)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = nums.size() - 1;

        // Iterate backwards from the second to last element
        for (int i = nums.size() - 2; i >= 0; i--) {
            // If from current position i we can reach the goal (or beyond)
            if (i + nums[i] >= goal) {
                // Shift the goal post closer to start
                goal = i;
            }
        }

        // If goal post reached the start, it means we can reach the original end
        return goal == 0;
    }
};
```

### Approach: Greedy (Forward Reachability)

```cpp
class SolutionForward {
public:
    bool canJump(vector<int>& nums) {
        int reachable = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > reachable) return false; // Cannot reach current i
            reachable = max(reachable, i + nums[i]);
            if (reachable >= nums.size() - 1) return true;
        }
        return true;
    }
};
```

### Python Reference

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們採用反向 Greedy 方法，這非常優雅。

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        // 設定目前的目標是最後一個位置
        int goal = nums.size() - 1;

        // 從倒數第二個位置往前遍歷
        for (int i = nums.size() - 2; i >= 0; i--) {
            // 如果從當前位置 i 最遠能跳到的位置 (i + nums[i])
            // 大於或等於目前的目標 goal
            // 代表從 i 跳到 goal 是可行的
            if (i + nums[i] >= goal) {
                // 那麼只要能到達 i，就能到達 goal
                // 所以把目標前移到 i
                goal = i;
            }
        }

        // 如果最後目標被移到了起點 0，代表從 0 可以一路連通到最後
        return goal == 0;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Single pass.
-   **Space Complexity**: $O(1)$
    -   No extra space.

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 你會如何處理更大的輸入？
- 有沒有更好的空間複雜度？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有考慮邊界條件
- ⚠️ 未討論複雜度

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 主動討論 trade-offs
- 💎 提供多種解法比較

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Jump Game II (跳躍遊戲 II)](03_Jump_Game_II.md)
