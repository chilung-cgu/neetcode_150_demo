# Find Median from Data Stream (從數據流中尋找中位數)

## 1. 🧐 Problem Dissection (釐清問題)

題目要求設計一個 `MedianFinder` 類別：
1.  `addNum(num)`: 從數據流中加入一個整數。
2.  `findMedian()`: 回傳目前所有數字的中位數。
    -   如果數字個數為奇數，回傳中間那一個。
    -   如果數字個數為偶數，回傳中間兩個的平均值。

-   **Input**:
    ```
    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3)
    findMedian() -> 2
    ```
-   **Constraints**:
    -   $-10^5 <= num <= 10^5$
    -   At most $5 \cdot 10^4$ calls.
    -   Follow up: If 99% of numbers are in range [0, 100]? (Bucket approach)

---

## 2. 🐢 Brute Force Approach (暴力解)

維護一個 sorted array。
-   `addNum`: Insert Sort. $O(N)$.
-   `findMedian`: Access middle. $O(1)$.
-   Total Time: $O(N^2)$ if $N$ additions. Too slow.

---

## 3. 💡 The "Aha!" Moment (優化)

中位數將數據集分為兩半：**較小的一半** 和 **較大的一半**。

我們可以使用 **兩個 Heaps** 來維護這兩半數據：
1.  **Max-Heap (`small`)**: 儲存較小的那一半數字。堆頂是這一半中的最大值（即靠近中位數的左邊）。
2.  **Min-Heap (`large`)**: 儲存較大的那一半數字。堆頂是這一半中的最小值（即靠近中位數的右邊）。

**Balancing Rule**:
-   我們要保持兩個 heaps 的大小平衡：
    -   `size(small) == size(large)` (偶數個，中位數 = (small.top + large.top)/2)
    -   `size(small) == size(large) + 1` (奇數個，中位數 = small.top)
-   插入新數字時，先放 `small`，然後把 `small` 的最大值移到 `large`，再看需不需要移回來以維持上述平衡。

---

## 4. 💻 Implementation (程式碼)

### Approach: Two Heaps

```cpp
#include <queue>
#include <vector>

using namespace std;

class MedianFinder {
private:
    // small stores the smaller half of numbers (Max-Heap)
    priority_queue<int> small;
    // large stores the larger half of numbers (Min-Heap)
    priority_queue<int, vector<int>, greater<int>> large;

public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        // Step 1: Add to small heap first
        small.push(num);
        
        // Step 2: Ensure every element in small is <= every element in large
        // Move max of small to large
        large.push(small.top());
        small.pop();
        
        // Step 3: Balance sizes
        // We allow small to have at most 1 more element than large
        if (small.size() < large.size()) {
            small.push(large.top());
            large.pop();
        }
    }
    
    double findMedian() {
        if (small.size() > large.size()) {
            return small.top();
        } else {
            return (small.top() + large.top()) / 2.0;
        }
    }
};
```

### Python Reference

```python
import heapq

class MedianFinder:

    def __init__(self):
        # Python heapq is Min-Heap
        # self.small uses negative values to simulate Max-Heap
        self.small = [] 
        self.large = []

    def addNum(self, num: int) -> None:
        # Push to small (Max-Heap) first
        heapq.heappush(self.small, -1 * num)
        
        # Ensure max of small <= min of large
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes (small len approx large len)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
            
        return (-1 * self.small[0] + self.large[0]) / 2.0
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class MedianFinder {
    // Max-Heap: 存較小的一半 (e.g., 1, 2, 3) -> Top is 3
    priority_queue<int> maxHeap;
    // Min-Heap: 存較大的一半 (e.g., 4, 5, 6) -> Top is 4
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
public:
    MedianFinder() {}
    
    // O(log N)
    void addNum(int num) {
        // 先隨便選一個 heap 加進去，這裡選 maxHeap
        maxHeap.push(num);
        
        // 為了保證 maxHeap 的所有元素都在 minHeap 的左邊 (數值上)
        // 必須把 maxHeap 中最大的拿出來，放進 minHeap
        minHeap.push(maxHeap.top());
        maxHeap.pop();
        
        // 平衡大小
        // 規定 maxHeap 的大小只能等於 minHeap 或者比 minHeap 多 1
        if (maxHeap.size() < minHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    // O(1)
    double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            // 奇數個：中位數就在較大的那個 heap 的 top
            return maxHeap.top();
        } else {
            // 偶數個：平均兩個 top
            return (maxHeap.top() + minHeap.top()) / 2.0;
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**:
    -   `addNum`: $O(\log N)$ (Heap push/pop).
    -   `findMedian`: $O(1)$ (Heap top).
-   **Space Complexity**: $O(N)$
    -   To store all numbers.
