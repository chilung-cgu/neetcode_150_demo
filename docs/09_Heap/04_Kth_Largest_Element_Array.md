# Kth Largest Element in an Array (陣列中的第 K 大元素)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `nums` 和一個整數 `k`。
請回傳陣列中 **第 k 大** 的元素。
注意：不需要去重，例如 `[3, 2, 3]`，第 1 大是 3，第 2 大也是 3。
題目要求你如果不使用排序 (which is $O(N \log N)$)，你能做得更好嗎？理想是 $O(N)$。

-   **Input**: `nums = [3,2,1,5,6,4], k = 2`
    -   Sorted: `[1,2,3,4,5,6]`
    -   2nd largest is 5.
-   **Output**: 5
-   **Input**: `nums = [3,2,3,1,2,4,5,5,6], k = 4`
    -   Sorted: `[1,2,2,3,3,4,5,5,6]`
    -   4th largest is 4.
-   **Output**: 4
-   **Constraints**:
    -   $1 <= k <= nums.length <= 10^5$
    -   $-10^4 <= nums[i] <= 10^4$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Sorting**:
直接排序，然後取 `nums[nums.size() - k]`。

-   **Time**: $O(N \log N)$.
-   **Space**: $O(1)$ or $O(N)$ (depending on sort implementation).

---

## 3. 💡 The "Aha!" Moment (優化)

這題是經典的 Selection Problem。

**Approach 1: Min-Heap (size K)**
維護一個大小為 $k$ 的 Min-Heap。

-   遍歷每個元素。
-   Push element。
-   如果 size > k，Pop min。
-   最後 Heap Top 就是第 k 大。
-   **Time**: $O(N \log k)$。當 $k$ 很大時，接近 $O(N \log N)$。

**Approach 2: Quick Select (Partition)**
利用 QuickSort 的 Partition 思想。
每次選一個 Pivot，將陣列分為與 Pivot 比較的三部分：`< Pivot`, `== Pivot`, `> Pivot`。
我們知道第 k 大的元素會落在哪一區。

-   如果是找第 k **小**，比較直觀。找第 k **大**，可以轉成找第 `N - k + 1` 小。
-   平均時間複雜度：$N + N/2 + N/4 + \dots = O(N)$。
-   最壞時間複雜度：$O(N^2)$ (如果 pivot 選得不好)。

在 C++ 中，`std::nth_element` 已經實作了 IntroSelect (Mix of QuickSelect and HeapSelect)，保證 $O(N)$。

---

## 4. 💻 Implementation (程式碼)

### Approach: Quick Select (Optimal)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // nth_element 將第 n 個位置的元素放到排序後的正確位置
        // 並且保證前面的都比它小，後面的都比它大 (或相反，看 comparator)
        // 這裡我們找第 k 大，相當於找「排序後 index 為 k-1 的元素」(如果用 greater 降序排)

        nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
        return nums[k - 1];
    }
};
```

### Approach: Min-Heap (Implementation Detail)

```cpp
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        return minHeap.top();
    }
};
```

### Python Reference (Quick Select Implementation)

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to index of k-th smallest
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    // 解法 1: Quick Select (面試官最愛，平均 O(N))
    int findKthLargest(vector<int>& nums, int k) {
        // nth_element 是 C++ STL 的強大函式，基於 IntroSelect 算法 (QuickSelect 的變體)
        // 它會重新排列 nums，使得 nums[k-1] 是「如果整個陣列降序排序後」位於該位置的元素
        // 且 nums[0...k-2] 都 >= nums[k-1]，nums[k...end] 都 <= nums[k-1]
        // greater<int>() 讓它變成降序邏輯
        nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());

        return nums[k - 1];
    }

    /* 解法 2: Min-Heap (O(N log k))
    int findKthLargest(vector<int>& nums, int k) {
        // 建立一個最小堆
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int num : nums) {
            minHeap.push(num);

            // 保持堆的大小為 k
            // 因為是 Min-Heap，堆頂是這 k 個數中最小的
            // 也就是目前為止第 k 大的數
            if (minHeap.size() > k) {
                minHeap.pop(); // 把不夠大的踢掉
            }
        }

        return minHeap.top();
    }
    */
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

**Quick Select (`nth_element`)**:

-   **Time Complexity**: $O(N)$ average. Worst Case $O(N^2)$ for naive QuickSelect, but `std::nth_element` uses IntroSelect which guarantees $O(N)$ by switching to Median-of-Medians logic if recursion goes too deep.
-   **Space Complexity**: $O(1)$ (In-place) or $O(\log N)$ (Recursion stack).

**Min-Heap**:

-   **Time Complexity**: $O(N \log k)$.
-   **Space Complexity**: $O(k)$.
