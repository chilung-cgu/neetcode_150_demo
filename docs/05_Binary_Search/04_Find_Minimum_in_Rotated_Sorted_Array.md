# Find Minimum in Rotated Sorted Array (尋找旋轉排序陣列中的最小值) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #153** — [題目連結](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [NeetCode 解說](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個長度為 `n` 的陣列 `nums`，它原本是升序排序的，但在某個未知的 pivot 點進行了 **旋轉 (Rotation)**。
例如 `[0,1,2,4,5,6,7]` 變成 `[4,5,6,7,0,1,2]`。
請找出這個陣列中的 **最小元素**。
**要求時間複雜度為** $O(\log n)$。

-   **Input**: `[3,4,5,1,2]`
-   **Output**: `1`
-   **Input**: `[4,5,6,7,0,1,2]`
-   **Output**: `0`
-   **Input**: `[11,13,15,17]` (沒有旋轉)
-   **Output**: `11`
-   **Constraints**:
    -   $1 <= n <= 5000$.
    -   All elements are unique.

---

## 2. 🐢 Brute Force Approach (暴力解)

遍歷陣列找最小。

-   **Time**: $O(n)$。
-   **Result**: 不符合 $O(\log n)$ 要求。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 Binary Search 的變體。
觀察旋轉陣列 `[4,5,6,7,0,1,2]`：

-   它可以被分為兩個 **Sorted Subarrays**：`[4,5,6,7]` (左半) 和 `[0,1,2]` (右半)。
-   左半邊的所有數值 **都大於** 右半邊的所有數值。
-   最小值就是右半邊的第一個元素。

我們可以用 Binary Search 來找這個「斷崖」：
取 `mid`。

1.  如果 `nums[mid] > nums[right]`：
    -   這意味著 `mid` 在 **左半邊** (數值較大的一邊)。
    -   最小值一定在 `mid` 的 **右邊**。
    -   `left = mid + 1`。
2.  如果 `nums[mid] < nums[right]`：
    -   這意味著 `mid` 在 **右半邊** (數值較小的一邊)，或者是沒有旋轉的情況。
    -   最小值可能是 `mid` 自己，也可能在 `mid` 的 **左邊**。
    -   `right = mid` (注意不是 `mid - 1`，因為 `mid` 可能是最小值)。
3.  當 `left == right` 時，我們就找到了最小值。

**為什麼比較 `nums[right]` 而不是 `nums[left]`?**
比較 `right` 比較直觀。因為如果 Array 沒有旋轉 `[1,2,3]`，`nums[mid] < nums[right]` 成立，我們往左找，正確。
如果我們比較 `left`，在 `[1,2,3]` case `nums[mid] > nums[left]`，我們會往右找，就錯了。
其實也可以比 `nums[0]` 或 `nums[n-1]`，但動態的 `left/right` 更安全。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../find_min_rotated_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../find_min_rotated_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Binary Search

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                // mid 在左半邊 (大的那一半)，最小值在右邊
                left = mid + 1;
            } else {
                // mid 在右半邊 (小的那一半)，或者是未旋轉的 array
                // 最小值可能是 mid，或在 mid 左邊
                right = mid;
            }
        }

        return nums[left];
    }
};
```

### Python Reference

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;

        // 當 l == r 時，只剩下一個元素，那就是最小值，迴圈結束
        while (l < r) {
            int m = l + (r - l) / 2;

            // 將 mid 與 right 比較
            // Case 1: [3, 4, 5, 1, 2], mid=5, right=2. 5 > 2.
            // 說明 mid 處於「被旋轉過去的高地」，也就是左半段。
            // 真正的低谷 (最小值) 一定在 mid 的右邊。
            // 且 mid 肯定不是最小值 (因為它比 right 大)。
            if (nums[m] > nums[r]) {
                l = m + 1;
            }
            // Case 2: [5, 1, 2, 3, 4], mid=2, right=4. 2 < 4.
            // 說明 mid 處於「低地」，也就是右半段。
            // 最小值可能是 mid 自己，或者在 mid 的左邊。
            // 所以我們縮小範圍到 [l, m]。
            else {
                r = m;
            }
        }

        return nums[l];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log n)$
    -   標準 Binary Search。
-   **Space Complexity**: $O(1)$
    -   常數空間。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果有重複元素？
- Find Maximum？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 比較對象選擇錯誤
- ⚠️ 邊界更新錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 解釋與 nums[-1] 比較的原因
- 💎 處理已排序的情況
