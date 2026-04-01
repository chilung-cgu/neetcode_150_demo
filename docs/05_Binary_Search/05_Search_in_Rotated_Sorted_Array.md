---
title: "Search in Rotated Sorted Array (在旋轉排序陣列中搜尋)"
description: "題目給一個**旋轉後**的排序陣列 `nums` 和一個 `target`。 請搜尋 `target` 是否存在。如果存在回傳 index，否則回傳 -1。 **要求時間複雜度為** $O(\log n)$。"
tags:
  - Binary Search
  - Array
difficulty: Medium
---

# Search in Rotated Sorted Array (在旋轉排序陣列中搜尋) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #33** — [題目連結](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [NeetCode 解說](https://neetcode.io/problems/find-target-in-rotated-sorted-array)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個**旋轉後**的排序陣列 `nums` 和一個 `target`。
請搜尋 `target` 是否存在。如果存在回傳 index，否則回傳 -1。
**要求時間複雜度為** $O(\log n)$。

-   **Input**: `nums = [4,5,6,7,0,1,2], target = 0`
-   **Output**: `4`
-   **Input**: `nums = [4,5,6,7,0,1,2], target = 3`
-   **Output**: `-1`
-   **Constraints**:
    -   All values are unique. (這簡化了問題，不必處理 duplicates)

---

## 2. 🐢 Brute Force Approach (暴力解)

Linear scan.

-   **Time**: $O(n)$。
-   **Result**: TLE (Conceptual, as $O(\log n)$ is required).

---

## 3. 💡 The "Aha!" Moment (優化)

這題可以看作是 `Find Minimum` 的進展版。
我們依然使用 Binary Search，取 `mid`。
雖然 array 被旋轉了，但我們切一刀後，**至少有一半是 Sorted (有序) 的**。
例如 `[4,5,6,7,0,1,2]` 切在 `7` (mid)：

-   左半 `[4,5,6]` 是有序的。
-   右半 `[0,1,2]` 也是有序的。
或者 `[6,7,0,1,2,4,5]` 切在 `1` (mid)：

-   左半 `[6,7,0]` 是無序的 (包含斷崖)。
-   右半 `[2,4,5]` 是有序的。

**演算法**：

1.  Check if `nums[mid] == target`.
2.  判斷哪半邊是有序的：
    -   如果 `nums[left] <= nums[mid]`：**左半邊有序**。
        -   檢查 `target` 是否在左半邊範圍內 (`nums[left] <= target < nums[mid]`)。
            -   是：搜尋左邊 `high = mid - 1`。
            -   否：搜尋右邊 `low = mid + 1`。
    -   否則 (`nums[left] > nums[mid]`)：**右半邊有序**。
        -   檢查 `target` 是否在右半邊範圍內 (`nums[mid] < target <= nums[right]`)。
            -   是：搜尋右邊 `low = mid + 1`。
            -   否：搜尋左邊 `high = mid - 1`。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../search_rotated_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../search_rotated_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: One-pass Binary Search

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) return mid;

            // 判斷哪一部分是有序的
            if (nums[left] <= nums[mid]) {
                // 左半邊有序
                if (target >= nums[left] && target < nums[mid]) {
                    // target 在這一段有序區間內
                    right = mid - 1;
                } else {
                    // target 在另一邊 (可能是右邊的有序區間，也可能是包含斷崖的區間)
                    left = mid + 1;
                }
            } else {
                // 右半邊有序
                if (target > nums[mid] && target <= nums[right]) {
                    // target 在這一段有序區間內
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
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
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # Left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (nums[m] == target) return m;

            // 關鍵判斷：哪一邊是連續遞增的 (Sorted Portion)？
            // Case 1: nums[l] <= nums[m]
            // 例如 [4, 5, 6, 7, 0, 1, 2], m=3 (val=7). 4 <= 7.
            // 左邊 [4, 5, 6, 7] 是 Sorted 的。
            // 注意：<= 是因為 m 可能等於 l (只剩兩個元素時)
            if (nums[l] <= nums[m]) {
                // 如果 target 落在这个 Sorted 的区间内
                if (target >= nums[l] && target < nums[m]) {
                    r = m - 1; // 往左找
                } else {
                    l = m + 1; // 往右找
                }
            }
            // Case 2: nums[l] > nums[m]
            // 例如 [6, 7, 0, 1, 2, 4, 5], m=3 (val=1). 6 > 1.
            // 說明左邊有斷崖，所以右邊 [1, 2, 4, 5] 肯定是 Sorted 的。
            else {
                // 如果 target 落在这个 Sorted 的区间内
                if (target > nums[m] && target <= nums[r]) {
                    l = m + 1; // 往右找
                } else {
                    r = m - 1; // 往左找
                }
            }
        }

        return -1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log n)$
    -   即使陣列有旋轉，我們每次迭代還是排除了一半的搜尋空間。
-   **Space Complexity**: $O(1)$
    -   常數空間。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果有重複？
- Find Min + Binary Search 兩步法？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 判斷哪半邊有序的邏輯錯誤
- ⚠️ 邊界條件複雜容易出錯

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 一次 Binary Search 完成
- 💎 清晰的分類討論

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Find Minimum in Rotated Sorted Array (尋找旋轉排序陣列中的最小值)](04_Find_Minimum_in_Rotated_Sorted_Array.md)

### 進階挑戰
- [Search In Rotated Sorted Array Ii](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) — LeetCode
