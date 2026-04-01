---
title: "Kth Largest Element in a Stream (數據流中的第 K 大元素)"
description: "題目要求設計一個類別 `KthLargest`，它可以："
tags:
  - Heap
  - Priority Queue
difficulty: Easy
---

# Kth Largest Element in a Stream (數據流中的第 K 大元素) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #703** — [題目連結](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [NeetCode 解說](https://neetcode.io/problems/kth-largest-integer-in-a-stream)


## 1. 🧐 Problem Dissection (釐清問題)

題目要求設計一個類別 `KthLargest`，它可以：

1.  **Initialize**: 接收一個整數 `k` 和一個整數陣列 `nums`。
2.  **Add**: 接收一個整數 `val`，並回傳「當前數據流中」第 `k` 大的元素。
    -   注意：是第 `k` 大，不是第 `k` 個不同元素。

-   **Input**:
    ```
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // nums = [2, 3, 4, 5, 8], 3rd largest is 4. Return 4.
    kthLargest.add(5);   // nums = [2, 3, 4, 5, 5, 8], 3rd largest is 5. Return 5.
    kthLargest.add(10);  // nums = [2, 3, 4, 5, 5, 8, 10], 3rd largest is 5. Return 5.
    kthLargest.add(9);   // nums = ..., 3rd largest is 8. Return 8.
    kthLargest.add(4);   // nums = ..., 3rd largest is 8. Return 8.
    ```

-   **Constraints**:
    -   $1 <= k <= 10^4$
    -   $0 <= nums.length <= 10^4$
    -   $-10^4 <= val <= 10^4$
    -   At most $10^4$ calls to add.
    -   It is guaranteed that there will be at least k elements in the array when you search for the kth element.

---

## 2. 🐢 Brute Force Approach (暴力解)

每次 `add` 時，將所有數字排序，然後取 index `len - k`。

-   **Initialize**: $O(N \log N)$.
-   **Add**: $O(N \log N)$ per call.
-   **Result**: 效率太差，尤其是當 `add` 被呼叫很多次時。

或者維護一個 Sorted List / Insert Sort。

-   **Add**: $O(N)$.
-   仍然不夠高效。

---

## 3. 💡 The "Aha!" Moment (優化)

我們只關心 **第 K 大** 的元素。比第 K 大還小的元素，我們其實不關心。
這種「Top K」問題，最適合用 **Min-Heap (最小堆)** 來解決。

維護一個大小為 `k` 的 **Min-Heap**。
這個 Heap 裡存放的是「目前為止最大的 k 個數」。
Heap 的 **頂端 (Top)** 就是這 k 個數中最小的那個，也就是 **第 k 大** 的數。

**Algorithm**:

-   **Init**:
    1.  建立一個 Min-Heap。
    2.  遍歷 `nums`，將每個數 push 進 heap。
    3.  如果 heap size > k，就 pop (移除最小的，因為它不可能成為前 k 大)。
-   **Add(val)**:
    1.  Push `val` 進 heap。
    2.  如果 heap size > k，Pop。
    3.  Return Heap Top。

**Complexity**:

-   **Init**: $O(N \log k)$。
-   **Add**: $O(\log k)$。 (Queue size is limited to k+1)
-   這非常高效，因為 $k$ 反映了記憶窗口的大小，與操作次數 $M$ 無關。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../kth_largest_stream_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../kth_largest_stream_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Min-Heap

```cpp
#include <vector>
#include <queue>
#include <functional>

using namespace std;

class KthLargest {
private:
    // Min-Heap of size k
    // Stores the k largest elements seen so far
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        minHeap.push(val);

        if (minHeap.size() > k) {
            minHeap.pop();
        }

        return minHeap.top();
    }
};

/**

 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
```

### Python Reference

```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class KthLargest {
    // 使用 STL 的 priority_queue，預設是 Max-Heap
    // 要改成 Min-Heap，需要指定比較器 greater<int>
    priority_queue<int, vector<int>, greater<int>> pq;
    int K;

public:
    KthLargest(int k, vector<int>& nums) {
        K = k;
        // 初始化時，直接呼叫 add 邏輯，保持代碼一致
        for (int x : nums) {
            add(x);
        }
    }

    int add(int val) {
        // 先把新元素放進去
        pq.push(val);

        // 如果超過 K 個元素，把最小的那個踢掉
        // 因為我們要找的是「前 K 大」，所以最小的那個 (Heap Top) 只要超過個數就沒資格留下來
        if (pq.size() > K) {
            pq.pop();
        }

        // 此時 Heap Top 就是第 K 大的元素
        // (Heap 裡存的是 Top 1 到 Top K，其中最小的就是 Top K)
        return pq.top();
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**:
    -   **Constructor**: $O(N \log k)$。
    -   **Add**: $O(\log k)$。
-   **Space Complexity**: $O(k)$。
    -   Heap 只需要存 k 個元素。

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
- [Kth Largest Element in an Array (陣列中的第 K 大元素)](04_Kth_Largest_Element_Array.md)
