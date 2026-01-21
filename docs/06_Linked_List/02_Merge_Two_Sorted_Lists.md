# Merge Two Sorted Lists (合併兩個排序鏈表) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #21** — [題目連結](https://leetcode.com/problems/merge-two-sorted-lists/) | [NeetCode 解說](https://neetcode.io/problems/merge-two-sorted-lists)


## 1. 🧐 Problem Dissection (釐清問題)

題目給兩個已排序 (Non-decreasing) 的 Linked Lists `list1` 和 `list2`。
請將它們合併成一個 **新的** 排序 Linked List 並回傳 head。

-   **Input**: `list1 = [1,2,4], list2 = [1,3,4]`
-   **Output**: `[1,1,2,3,4,4]`
-   **Input**: `list1 = [], list2 = []`
-   **Output**: `[]`
-   **Input**: `list1 = [], list2 = [0]`
-   **Output**: `[0]`
-   **Constraints**:
    -   Nodes number: $[0, 50]$.
    -   `-100 <= Node.val <= 100`.
    -   Both lists are sorted.

---

## 2. 🐢 Brute Force Approach (暴力解)

將所有 node values 放入一個 array，然後 sort array，再重建一個新的 list。

-   **Time**: $O((n+m) \log(n+m))$。
-   **Space**: $O(n+m)$。
-   **Result**: 沒利用到「原本就是 sorted」這個特性，效率不佳。

---

## 3. 💡 The "Aha!" Moment (優化)

因為兩個輸入都已經是 Sorted 的，我們可以使用 **Merge Sort** 中的 Merge 步驟。
維護兩個指標 `l1` 和 `l2`，比較它們當前的值：

1.  如果 `l1->val <= l2->val`：選 `l1`，`l1` 前進。
2.  否則：選 `l2`，`l2` 前進。
3.  將選中的 node 接到結果 list 的後面。

**Dummy Node (哨兵節點)**：
這題的「結果 list」一開始是空的，為了避免處理 edge case (head 為 null 的情況)，我們會创建一个 **Dummy Node**。
我們讓 `tail` 一開始指向 Dummy。
每次接上新節點後，`tail = tail->next`。
最後回傳 `dummy->next`。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../merge_two_lists_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../merge_two_lists_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative with Dummy Node

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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy; // Stack allocation is enough if not returning dummy itself
        ListNode* tail = &dummy;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // 處理剩餘部分
        // 因為是 linked list，直接接上去就好，不用像 array 那樣一個個 copy
        if (list1 != nullptr) {
            tail->next = list1;
        } else if (list2 != nullptr) {
            tail->next = list2;
        }

        return dummy.next;
    }
};
```

### Approach: Recursive

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;

        if (l1->val <= l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        } else {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};
```

### Python Reference

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // 使用哨兵節點簡化代碼 (避免處理 head 為空的情況)
        ListNode dummy(0);
        ListNode* tail = &dummy;

        // 只要兩個 list 都還有節點，就比較並串接小的那個
        while (list1 && list2) {
            if (list1->val < list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            // 推進 tail
            tail = tail->next;
        }

        // 如果其中一個 list 還有剩，直接把它接在 tail 後面
        // 因為剩下的部分本身就是 sorted 的，所以不用再遍歷
        if (list1) {
            tail->next = list1;
        } else if (list2) {
            tail->next = list2;
        }

        // 回傳 dummy 的下一個，即真正的 head
        return dummy.next;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n + m)$
    -   遍歷兩個 list 各一次。
-   **Space Complexity**: $O(1)$
    -   我們只使用了幾個 pointers (`dummy`, `tail`) 重組現有的 nodes。
    -   Recursive 解法會是 $O(n+m)$ Stack Space。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- Merge K Sorted Lists?
- 原地合併？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有處理空鏈表
- ⚠️ 沒有處理剩餘節點

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 使用 dummy head 簡化
- 💎 解釋時間空間複雜度

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Merge k Sorted Lists (合併 k 個排序鏈表)](10_Merge_k_Sorted_Lists.md)
