# Binary Search (二分搜尋) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #704** — [題目連結](https://leetcode.com/problems/binary-search/) | [NeetCode 解說](https://neetcode.io/problems/binary-search)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個**已排序 (Sorted)** 的整數陣列 `nums` 和一個目標值 `target`。
請寫一個函式來尋找 `target` 在 `nums` 中的 index。
如果找不到，回傳 `-1`。
**演算法的時間複雜度必須是** $O(\log n)$。

-   **Input**: `nums = [-1,0,3,5,9,12], target = 9`
-   **Output**: `4` (9 出現在 nums[4])
-   **Input**: `nums = [-1,0,3,5,9,12], target = 2`
-   **Output**: `-1` (找不到)
-   **Constraints**:
    -   $1 <= nums.length <= 10^4$.
    -   `nums` 中的元素都是唯一的。
    -   `nums` 是非遞減排序 (Ascending sort)。

---

## 2. 🐢 Brute Force Approach (暴力解)

遍歷整個陣列。

-   **Time**: $O(n)$。
-   **Result**: 題目明確要求 $O(\log n)$，所以這不合規。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 **Binary Search** 的教科書定義。
因為陣列是 **Sorted** 的，我們不需要檢查每個元素。

我們每次都檢查 **中間 (Middle)** 的元素：

1.  如果 `nums[mid] == target`，找到了！
2.  如果 `nums[mid] > target`，代表目標一定在左半邊 (因為右半邊都比 `nums[mid]` 大，肯定更比 `target` 大)。所以我們把搜尋範圍縮小到 `[left, mid - 1]`。
3.  如果 `nums[mid] < target`，代表目標一定在右半邊。所以我們把搜尋範圍縮小到 `[mid + 1, right]`。

這樣每次我們都能排除一半的可能性。

**一個常見的 Bug**:
計算 `mid` 時，如果是 `(left + right) / 2`，在 `left` 和 `right` 都很大時可能會造成 **Integer Overflow**。
雖然 Python 自動處理大數，但在 C++/Java 中這是個經典坑。
正確寫法：`mid = left + (right - left) / 2;`

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../binary_search_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../binary_search_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative Binary Search

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            // 防止 (left + right) 溢位
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
};
```

### Python Reference

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 works in Python but this is good habit
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;

        // 迴圈條件是 low <= high
        // 為什麼要有 '=' ? 因為當 low == high 時，或者是只有一個元素時，
        // 我們仍然需要檢查那最後一個位置是否是 target。
        while (low <= high) {
            // 計算中點
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] < target) {
                // 目標在右邊，移動下界
                low = mid + 1;
            } else {
                // 目標在左邊，移動上界
                // 為什麼是 mid - 1 而不是 mid?
                // 因為我們已經檢查過 nums[mid] 不是 target 了，
                // 所以下一次搜尋不需要包含它。
                high = mid - 1;
            }
        }

        return -1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log n)$
    -   每次迭代都將搜尋空間減半。
    -   $\log_2(10^4) \approx 14$ 次比較就能找到答案。
-   **Space Complexity**: $O(1)$
    -   Iterative 解法只需要常數空間。
    -   如果是 Recursive 解法，Stack Space 會是 $O(\log n)$。
