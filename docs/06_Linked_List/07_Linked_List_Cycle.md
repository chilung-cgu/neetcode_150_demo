---
title: "Linked List Cycle (鏈結串列中的環)"
description: "題目給一個 Linked List 的 head。 判斷這個 Linked List 是否有 **Cycle (環)**。 所謂有環，就是你可以透過不斷地 `next` 指標走下去，永遠走不到 `null`，且會重複經過某些節點。"
tags:
  - Linked List
difficulty: Easy
---

# Linked List Cycle (鏈結串列中的環) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #141** — [題目連結](https://leetcode.com/problems/linked-list-cycle/) | [NeetCode 解說](https://neetcode.io/problems/linked-list-cycle-detection)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Linked List 的 head。
判斷這個 Linked List 是否有 **Cycle (環)**。
所謂有環，就是你可以透過不斷地 `next` 指標走下去，永遠走不到 `null`，且會重複經過某些節點。

-   **Input**: `head = [3,2,0,-4], pos = 1` (tail connects to node index 1)
-   **Output**: `true`
-   **Input**: `head = [1], pos = -1` (no cycle)
-   **Output**: `false`
-   **Constraints**:
    -   $0 <= nodes <= 10^4$
    -   Space: Can you solve it using $O(1)$ (i.e. constant) memory?

---

## 2. 🐢 Brute Force Approach (暴力解)

用一個 `HashSet` 存所有走過的節點地址。
每次走到新節點，檢查是否在 Set 中。

-   如果存在：有環 (True)。
-   如果走到 null：無環 (False)。
-   **Time**: $O(n)$。
-   **Space**: $O(n)$。
-   **Result**: 有效，但不是 $O(1)$ space。

---

## 3. 💡 The "Aha!" Moment (優化)

使用 **Floyd's Cycle-Finding Algorithm (龜兔賽跑演算法)**。

維護兩個指標：

1.  **Slow** (烏龜)：一次走一步。
2.  **Fast** (兔子)：一次走兩步。

**原理**：

-   如果沒有環，Fast 指標一定會先到達終點 (`nullptr`)。
-   如果有環，Fast 指標進入環後，會一直在裡面繞圈圈。Slow 指標隨後也會進入環。
-   因為 Fast 比 Slow 快，他們在環裡面一定會 **相遇** (Fast 套圈 Slow)。

**為什麼一定會相遇？**
假設 Slow 進環時，Fast 已經在環裡了。
每次移動，Fast 和 Slow 的距離會縮短 1 (`2 - 1 = 1`)。
所以不管他們距離多遠，Fast 總會追上 Slow。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../linked_list_cycle_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../linked_list_cycle_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Fast & Slow Pointers (Floyd's Algorithm)

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head) return false;

        ListNode *slow = head;
        ListNode *fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;

            // 如果相遇，代表有環
            if (slow == fast) {
                return true;
            }
        }

        // 如果 fast 走到了盡頭，代表無環
        return false;
    }
};
```

### Python Reference

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        // Floyd's Cycle Detection Algorithm

        ListNode* slow = head;
        ListNode* fast = head;

        // 當 Fast 還能繼續走時 (防止 NullPointer Exception)
        // 只需要檢查 fast 和 fast->next，因為 fast 走得快
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;          // 走 1 步
            fast = fast->next->next;    // 走 2 步

            // 檢查是否相遇
            if (slow == fast) {
                return true;
            }
        }

        // 迴圈結束，代表 Fast 抵達終點 -> 無環
        return false;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   如果無環，走 $n/2$ 步結束。
    -   如果有環，設環外長度 $A$，環長 $B$。Slow 走 $A$ 步進環時，Fast 已經在環裡。他們最多再走 $B$ 步就會相遇。總步數 $\approx A + B = O(n)$。
-   **Space Complexity**: $O(1)$
    -   只用了兩個指標。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 找環起點？
- 環的長度？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 快指標步進邏輯錯誤
- ⚠️ 沒有處理空鏈表

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 Floyd's Cycle Detection
- 💎 數學證明理解

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Find the Duplicate Number (尋找重複的數字)](08_Find_the_Duplicate_Number.md)

### 進階挑戰
- [Linked List Cycle Ii](https://leetcode.com/problems/linked-list-cycle-ii/) — LeetCode
