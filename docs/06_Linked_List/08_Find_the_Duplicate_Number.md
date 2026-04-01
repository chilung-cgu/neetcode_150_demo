---
title: "Find the Duplicate Number (尋找重複的數字)"
description: "題目給一個包含 `n + 1` 個整數的陣列 `nums`，每個整數都在 `[1, n]` 範圍內（包含 1 和 n）。 在這個陣列中，**恰好有一個** 數字重複出現（可能出現 2 次或更多次）。 請找出這個重複的數字。"
tags:
  - Linked List
difficulty: Medium
---

# Find the Duplicate Number (尋找重複的數字) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #287** — [題目連結](https://leetcode.com/problems/find-the-duplicate-number/) | [NeetCode 解說](https://neetcode.io/problems/find-duplicate-integer)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個包含 `n + 1` 個整數的陣列 `nums`，每個整數都在 `[1, n]` 範圍內（包含 1 和 n）。
在這個陣列中，**恰好有一個** 數字重複出現（可能出現 2 次或更多次）。
請找出這個重複的數字。

**Constraints / Requirements**:

- You must not modify the array (assume the array is read-only).
- You must use only constant, $O(1)$ extra space.
- Your runtime complexity should be less than $O(n^2)$.
- $1 <= n <= 10^5$.

這題雖然給的是 Array，但它其實是 **Legacy Interview Question** 的變形，核心解法跟 Linked List 有關。

---

## 2. 🐢 Brute Force Approach (暴力解)

1.  **Count Iteration**: 對於 `1` 到 `n` 的每個數字，計算它在 array 出現幾次。
    - **Time**: $O(n^2)$。符合題目 "less than O(n^2)" 的邊緣，但不是最佳。
2.  **Sorting**: 排序後檢查相鄰元素。
    - **Time**: $O(n \log n)$。
    - **Violation**: 修改了 array。
3.  **Hash Set**:
    - **Time**: $O(n)$。
    - **Violation**: Space $O(n)$。

---

## 3. 💡 The "Aha!" Moment (優化)

這題可以轉化為 **Linked List Cycle Detection (Linked List Cycle II)** 問題。

**Mapping**:
每個 index `i` 在陣列中的值 `v = nums[i]` 可以看作是 `next` 指標，指向 index `v`。
即 `i -> nums[i]`。
因為值在 `[1, n]` 範圍內，所以這是一個 Valid 的 Pointer jumping。
如果有重複的數字（例如 `x`），那麼就有多個 index 指向 `x`。這意味著多個節點指向同一個節點，這會形成一個 **Cycle (環)**。
而且，重複的數字 `x` 就是這個環的 **入口 (Entry Point)**。

**Floyd's Algorithm (Turtle and Hare)**:

1.  **Phase 1**: 判斷是否有環（一定有）。
    - `slow = nums[slow]`, `fast = nums[nums[fast]]`。
    - 他們會相遇。
2.  **Phase 2**: 找出環的入口。
    - 將 `slow` 重置回起點 (`nums[0]` 或 `0`)。
    - `fast` 保持在相遇點。
    - 兩者同時每次走一步：`slow = nums[slow]`, `fast = nums[fast]`。
    - 他們再次相遇的點，就是環的入口，也就是重複的數字。

**為什麼 Phase 2 有效？** (數學證明略，這是經典算法性質)：
設起點到環入口距離為 `a`，環長為 `L`。相遇點距離環入口為 `b`。
Fast 走了 `2(a+b)`，Slow 走了 `a+b`。
Fast 也在 `a + b + kL` 處。
可以推導出 `a = kL - b`。這意味著從起點走 `a` 步，和從相遇點走 `a` 步 (實際上是 `kL - b`，也就是倒退 `b` 步或者往前走互補距離)，會在入口相遇。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../find_duplicate_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../find_duplicate_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Floyd's Cycle Detection

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // Phase 1: Find intersection point
        int slow = nums[0];
        int fast = nums[nums[0]];

        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }

        // Phase 2: Find entrance of cycle
        slow = 0; // 從起點開始 (題目 array 是 0-indexed，但值是 1-n，所以 index 0 永遠是安全的起點，且因為值 >=1，0 不在 cycle 內)

        // 注意：這裡我們把 Pointer 邏輯稍微調整。
        // 標準 Floyd 是從 head 開始。
        // 上面 Phase 1 我們是從 head 的 next 開始的 (slow=nums[0], fast=nums[nums[0]])
        // 所以 Phase 2 我們也要稍微對齊。

        // 修正逻辑：
        // Start from initial state: slow = 0, fast = 0
        // do-while for Phase 1

        // Better Implementation:
        slow = 0;
        fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }

        return slow;
    }
};
```

### Python Reference

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
```

Note: 初始值設為 0 是有效的，因為 index 0 的數字 `nums[0]` 指向 `next`。我們把 index 當作 node address。

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // 使用 Floyd's Cycle Detection 演算法
        // 我們將 array 視為 Linked List: i -> nums[i]

        // 1. 判斷是否有環 (Phase 1)
        // 初始時都在 index 0
        int slow = 0;
        int fast = 0;

        // 使用 do-while 確保至少走一步
        do {
            slow = nums[slow];          // 走一步
            fast = nums[nums[fast]];    // 走兩步
        } while (slow != fast);

        // 2. 尋找環的入口 (Phase 2)
        // 將 slow (或者另一個新的指針) 放回起點
        // fast 留在原地
        int slow2 = 0;

        // 兩個指針都每次走一步，它們會在環的入口 (重複的數字) 相遇
        while (slow2 != fast) {
            slow2 = nums[slow2];
            fast = nums[fast];
        }

        return slow2;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - Floyd 演算法是線性的。
- **Space Complexity**: $O(1)$
  - 沒有修改 array，沒有額外空間。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 不能修改陣列？
- O(1) 空間？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 連結方式錯誤 (nums[i] -> nums[nums[i]])
- ⚠️ 環起點計算錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 Floyd's Cycle Detection 在陣列上的應用
- 💎 二分搜尋替代解法

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Linked List Cycle (鏈結串列中的環)](07_Linked_List_Cycle.md)
