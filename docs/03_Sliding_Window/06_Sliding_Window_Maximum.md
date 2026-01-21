# Sliding Window Maximum (滑動窗口最大值) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

> 📌 **LeetCode #239** — [題目連結](https://leetcode.com/problems/sliding-window-maximum/) | [NeetCode 解說](https://neetcode.io/problems/sliding-window-maximum)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `nums`，以及一個窗口大小 `k`。
這個窗口從最左邊移動到最右邊，每次只移動一步。
我們只能看到窗口內的 `k` 個數字。
請回傳 **每一個位置時窗口內的最大值**。

- **Input**: `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **Output**: `[3,3,5,5,6,7]`
  - `[1,3,-1]`, -3, 5, 3, 6, 7 -> max: 3
  - 1, `[3,-1,-3]`, 5, 3, 6, 7 -> max: 3
  - 1, 3, `[-1,-3,5]`, 3, 6, 7 -> max: 5
  - ...
- **Constraints**:
  - $1 <= k <= nums.length <= 10^5$.
  - 題目要求 $O(n)$ 的解法。

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一個窗口，遍歷這 `k` 個元素找最大值。

- **Time**: $O(n \cdot k)$。
- **Result**: 當 `k` 很大時 (例如 $k \approx n/2$)，會變成 $O(n^2)$ -> TLE。

---

## 3. 💡 The "Aha!" Moment (優化)

我們需要一個這要在 $O(1)$ 時間內取得最大值，同時支援 $O(1)$ 的「加入」與「移除」操作。
Heap? 移除任意元素需要 $O(k)$ 或 tricky $O(\log k)$ mapping。
BST? $O(\log k)$。

這題的最佳解是 **Monotonically Decreasing Deque (單調遞減雙端佇列)**。

**核心邏輯**:
Deque 裡存的一定是 **候選的最大值** 的 Index。
並且我們保持 Deque 裡的元素對應的數值是 **單調遞減** 的。

- `deque.front()` 永遠是當前窗口的最大值。
- 當新元素 `nums[i]` 進來時：
  1.  **Pop Small Elements**: 如果 `nums[i]` 比 `deque.back()` 還大，那 `deque.back()` 裡的那個數字這輩子都不可能成為最大值了（因為 `nums[i]` 比它晚進來，還比它大，會壓死它）。直接踢掉 `pop_back()`。重複直到 Deque 單調或空。
  2.  **Add New Element**: 把 `i` 加進 `push_back()`。
  3.  **Pop Outdated Elements**: 如果 `deque.front()` 的 index 已經超出窗口範圍 (`i - k`)，就踢掉 `pop_front()`。
  4.  **Record Result**: 只要 `i >= k-1` (窗口成形後)，`deque.front()` 就是當前答案。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../sliding_maximum_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../sliding_maximum_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Monotonic Deque

```cpp
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // Deque 存的是 index，不是 value
        deque<int> dq;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            // 1. 移除過期元素 (超出窗口左界)
            if (!dq.empty() && dq.front() == i - k) {
                dq.pop_front();
            }

            // 2. 維護單調性 (移除比當前元素小的所有候選人)
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }

            // 3. 加入新元素
            dq.push_back(i);

            // 4. 記錄答案 (當窗口填滿 k 個後開始記錄)
            if (i >= k - 1) {
                res.push_back(nums[dq.front()]);
            }
        }

        return res;
    }
};
```

### Python Reference

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)

            if dq[0] == i - k:
                dq.popleft()

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // 使用 Deque (Double Ended Queue)
        // 裡面存的是 Index。
        // 性質：對應的 nums[index] 是單調嚴格遞減的。
        // 例如: deque裡是 [5, 2] (假設是 indices)，這代表 nums[5] > nums[2]。
        // 且 nums[5] 是目前窗口最大值。
        deque<int> dq;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            // Step 1: Remove Out-of-bound indices
            // 窗口範圍是 [i-k+1, i]。如果 front 是 i-k，說明它過期了。
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }

            // Step 2: Remove smaller elements from back
            // 如果新來的 nums[i] 很大，那它前面那些比它小的「老元素」就沒用了。
            // 因為 nums[i] 比它們晚過期，數值又比它們大，所以它們永遠沒機會翻身。
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }

            // Step 3: Add current index
            dq.push_back(i);

            // Step 4: Add to result
            // 當我們至少有 k 個元素 (i >= k-1) 時，front 就是最大值
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - 每個元素被 push 進 Deque 一次。
  - 每個元素被 pop 出 Deque 最多一次。
  - 總操作次數是 $2n$，所以是線性時間。
- **Space Complexity**: $O(k)$
  - Deque 最多同時儲存 $k$ 個元素 (在 Input 是 Strictly Decreasing `[5,4,3,2,1]` 的最差情況下)。
  - Output space $O(n-k+1)$ 不算在 auxiliary space 中。
