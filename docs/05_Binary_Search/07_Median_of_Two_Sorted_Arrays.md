# Median of Two Sorted Arrays (兩個排序陣列的中位數)

## 1. 🧐 Problem Dissection (釐清問題)

題目給兩個大小分別為 `m` 和 `n` 的排序陣列 `nums1` 和 `nums2`。
請找出這兩個陣列合併後的中位數 (Median)。
**演算法的時間複雜度必須是** $O(\log(m+n))$。

-   **Input**: `nums1 = [1,3], nums2 = [2]`
-   **Output**: `2.00000` (merged: [1,2,3], median is 2)
-   **Input**: `nums1 = [1,2], nums2 = [3,4]`
-   **Output**: `2.50000` (merged: [1,2,3,4], median is (2+3)/2 = 2.5)
-   **Constraints**:
    -   nums1.length == m, nums2.length == n
    -   $0 <= m <= 1000, 0 <= n <= 1000$
    -   $1 <= m + n <= 2000$

---

## 2. 🐢 Brute Force Approach (暴力解)

合併兩個陣列 (Merge Sort)，然後直接找中位數。

-   **Time**: $O(m+n)$。
-   **Result**: 題目嚴格要求 $O(\log(m+n))$，所以這不合規。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 Binary Search 的高難度應用。我們需要在兩個 Sorted Arrays 中找「第 k 小」的元素，或者更具體地說，找一個 **Partition (分割線)**。

假設我們把 `A` (nums1) 和 `B` (nums2) 分別切成兩半：
`A: A_left | A_right`
`B: B_left | B_right`

我們希望找到一個切法，使得：

1.  **左邊元素的總數** 等於 **右邊元素的總數** (或者多 1 個，如果總數是奇數)。
2.  **Max(A_left, B_left) <= Min(A_right, B_right)**。這保證了左邊所有元素都小於等於右邊所有元素，也就是說，Partition 是正確的。

只要我們對較短的那個陣列 (假設是 A) 做 Binary Search 尋找切點 `i`，另一個陣列的切點 `j` 就會自動確定 (因為總左半邊數量是固定的 `(m + n + 1) / 2`)。

**Partitioning Logic**:
-   `half = (m + n + 1) / 2`
-   Binary Search on A: `i` is index in A.
-   `j = half - i` (index in B).
-   Check:
    -   `A[i-1] <= B[j]` (A_left <= B_right)
    -   `B[j-1] <= A[i]` (B_left <= A_right)
-   如果正確：找到了！計算 Median。
    -   奇數：`max(A[i-1], B[j-1])`
    -   偶數：`(max(left) + min(right)) / 2`
-   如果不正確：
    -   `A[i-1] > B[j]`: A 切太多了 (A_left 太大)，`high = i - 1`。
    -   `B[j-1] > A[i]`: A 切太少了 (B_left 太大)，`low = i + 1`。

---

## 4. 💻 Implementation (程式碼)

### Approach: Binary Search on Partition

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // 確保 nums1 是較短的陣列，這樣可以減少 Binary Search 的範圍，並避免 j 越界
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        int half = (total + 1) / 2;

        int left = 0;
        int right = m;

        while (left <= right) {
            int i = left + (right - left) / 2; // Partition index for nums1
            int j = half - i;                  // Partition index for nums2

            // 處理邊界情況 (如果 i 為 0，左邊用 -infinity；如果 i 為 m，右邊用 infinity)
            int nums1Left = (i == 0) ? INT_MIN : nums1[i - 1];
            int nums1Right = (i == m) ? INT_MAX : nums1[i];

            int nums2Left = (j == 0) ? INT_MIN : nums2[j - 1];
            int nums2Right = (j == n) ? INT_MAX : nums2[j];

            // 檢查 Partition 是否合法
            if (nums1Left <= nums2Right && nums2Left <= nums1Right) {
                // 合法！計算 Median
                if (total % 2 == 1) {
                    return max(nums1Left, nums2Left);
                } else {
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2.0;
                }
            } else if (nums1Left > nums2Right) {
                // A 的左邊太大了 -> 往左縮
                right = i - 1;
            } else {
                // B 的左邊太大了 (或者說 A 的右邊太小了) -> 往右擴 A
                left = i + 1;
            }
        }

        return 0.0;
    }
};
```

### Python Reference

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
```

**Note**: Python 的 index 處理 ( `i` vs `i+1` ) 有點 tricky。C++ 版本用 "Partition Index" (0 到 m) 來視為左邊有幾個元素，這是最清晰的思路。如果 `i=0` 代表左邊有 0 個元素。

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // 為了優化效能，我們對「較短」的那個陣列進行二分搜尋
        // 這樣複雜度是 O(log(min(m, n)))
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;

        // half 代表合併後左半邊應該有多少個元素
        // 如果 total 是奇數 (e.g. 7)，左邊要有 4 個，因為中位數就是第 4 個 (index 3)
        // 如果 total 是偶數 (e.g. 8)，左邊要有 4 個
        int half = (total + 1) / 2;

        int l = 0;
        int r = m; // right bound 是 m，代表我们可以把所有 nums1 都分到左邊

        while (l <= r) {
            // i 是 nums1 的分割點 (代表 nums1 左邊有 i 個元素)
            int i = l + (r - l) / 2;
            // j 是 nums2 的分割點 (代表 nums2 左邊有 j 個元素)
            // i + j 必須等於 half
            int j = half - i;

            // 取得分割線兩側的值，注意邊界檢查
            // A_Left, A_Right
            int left1 = (i == 0) ? INT_MIN : nums1[i - 1];
            int right1 = (i == m) ? INT_MAX : nums1[i];

            // B_Left, B_Right
            int left2 = (j == 0) ? INT_MIN : nums2[j - 1];
            int right2 = (j == n) ? INT_MAX : nums2[j];

            // 檢查交叉條件
            // 我們希望 left1 <= right2 且 left2 <= right1
            if (left1 <= right2 && left2 <= right1) {
                // 找到了完美的分割！

                if (total % 2 == 1) {
                    // 奇數個：中位數就是左半邊最大的那個
                    return max(left1, left2);
                } else {
                    // 偶數個：中位數是 (左邊最大 + 右邊最小) / 2
                    return (max(left1, left2) + min(right1, right2)) / 2.0;
                }
            } else if (left1 > right2) {
                // nums1 的左邊太大了，我們需要往左縮一點
                r = i - 1;
            } else {
                // nums2 的左邊太大了 (或者是 nums1 的左邊太小了)，我們需要 nums1 往右擴一點
                l = i + 1;
            }
        }

        return 0.0;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log(\min(m, n)))$
    -   因為我們只對較短的陣列做 Binary Search，搜尋範圍是 `min(m, n)`。
-   **Space Complexity**: $O(1)$
    -   沒有額外配置 Memory。
