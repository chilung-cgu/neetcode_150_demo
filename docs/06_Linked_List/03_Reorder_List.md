---
title: "Reorder List (重新排序鏈結串列)"
description: "題目給一個 singly linked list `L`: $L_0 \rightarrow L_1 \rightarrow \dots \rightarrow L_{n-1} \rightarrow L_n$. 請將其重新排列為：$L_0 \rightarrow L_n \rightarrow L"
tags:
  - Linked List
difficulty: Medium
---

# Reorder List (重新排序鏈結串列) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #143** — [題目連結](https://leetcode.com/problems/reorder-list/) | [NeetCode 解說](https://neetcode.io/problems/reorder-linked-list)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 singly linked list `L`: $L_0 \rightarrow L_1 \rightarrow \dots \rightarrow L_{n-1} \rightarrow L_n$.
請將其重新排列為：$L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \rightarrow L_2 \rightarrow L_{n-2} \rightarrow \dots$

簡單來說，就是把後半段反轉，然後像「拉鍊」一樣跟前半段交叉合併。
**要求**：In-place modify，不能改變 node values，必須移動 nodes 本身。

- **Input**: `head = [1,2,3,4]`
- **Output**: `[1,4,2,3]`
- **Input**: `head = [1,2,3,4,5]`
- **Output**: `[1,5,2,4,3]`
- **Constraints**:
  - $1 <= n <= 5 \cdot 10^4$.
  - $1 <= Node.val <= 1000$.

---

## 2. 🐢 Brute Force Approach (暴力解)

用一個 `deque` (Double-ended queue) 存所有的 nodes。
然後交替從 `front` 和 `back` 取出 node 串接。

- **Time**: $O(n)$。
- **Space**: $O(n)$ (因為存了 pointers)。
- **Result**: 雖然可以過，但是題目通常期望 $O(1)$ Space。

---

## 3. 💡 The "Aha!" Moment (優化)

這題可以拆解成三個標準的 Linked List 子問題：

1.  **Find Middle**: 使用 **Slow & Fast Pointers** 找到鏈表的中點。
    - `1->2->3->4->5` 中的 `3`。
2.  **Reverse Second Half**: 將中點之後的鏈表反轉。
    - `3->4->5` 變成 `3<-4<-5` (或者 `3->null`, `5->4->null`)。
    - 通常我們斷開連結：`1->2->3` 和 `5->4`。
3.  **Merge Two Lists**: 將前半段 (`1->2->3`) 和反轉後的後半段 (`5->4`) 交替合併。
    - `1->5->2->4->3`。

**步驟細節**：

- **Find Mid**: `slow` 走一步，`fast` 走兩步。
- **Split**: `mid = slow->next`; `slow->next = nullptr`.
- **Reverse**: 標準 reverse linked list。
- **Merge**: `temp1 = l1->next`, `temp2 = l2->next`, `l1->next = l2`, `l2->next = temp1`...

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../reorder_list_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../reorder_list_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Mid + Reverse + Merge (O(1) Space)

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;

        // 1. Find the middle (Splitting the list)
        ListNode *slow = head, *fast = head;
        // fast->next and fast->next->next checked for even/odd balance
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // slow is at the end of the first half
        ListNode* second = slow->next;
        slow->next = nullptr; // Break the link

        // 2. Reverse the second half
        ListNode* prev = nullptr;
        ListNode* curr = second;
        while (curr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        second = prev; // new head of the reversed second half

        // 3. Merge two halves
        ListNode* first = head;
        while (second) { // second half is always shorter or equal
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            first->next = second;
            second->next = tmp1;

            first = tmp1;
            second = tmp2;
        }
    }
};
```

### Python Reference

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None # split

        # 2. Reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. Merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    void reorderList(ListNode* head) {
        // Base case: 如果只有 0, 1, 2 個節點，不需要 reorder
        if (!head || !head->next || !head->next->next) return;

        // --- Step 1: 找中點 ---
        // 使用快慢指針
        ListNode* slow = head;
        ListNode* fast = head;

        // 我們希望 slow 停在左半段的最後一個節點
        // 對於 [1,2,3,4,5]， slow 停在 3
        // 對於 [1,2,3,4]， slow 停在 2
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // --- Step 2: 反轉後半段 ---
        ListNode* curr = slow->next;
        // 切斷兩個 list
        slow->next = nullptr;

        ListNode* prev = nullptr; // 這是反轉後的 head
        while (curr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        // 此時：
        // first list: head -> ... -> slow -> null
        // second list: prev -> ... -> null

        // --- Step 3: 合併兩個 list ---
        ListNode* first = head;
        ListNode* second = prev;

        while (second) {
            // 暫存下一個
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            // 連結
            first->next = second;
            second->next = tmp1;

            // 移動
            first = tmp1;
            second = tmp2;
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - Find Mid: $O(n/2)$.
  - Reverse: $O(n/2)$.
  - Merge: $O(n/2)$.
  - Total: $O(n)$.
- **Space Complexity**: $O(1)$
  - In-place operation，只用了指標變數。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果需要保持原順序？
- 遞迴方式？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 找中點邏輯錯誤
- ⚠️ 合併時斷鏈

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 三步驟：找中點、反轉後半、合併
- 💎 原地操作 O(1) 空間

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Reverse Linked List (反轉鏈結串列)](01_Reverse_Linked_List.md)
