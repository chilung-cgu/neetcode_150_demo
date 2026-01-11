# Reorder List (重新排序鏈結串列)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 singly linked list `L`: $L_0 \rightarrow L_1 \rightarrow \dots \rightarrow L_{n-1} \rightarrow L_n$.
請將其重新排列為：$L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \rightarrow L_2 \rightarrow L_{n-2} \rightarrow \dots$

簡單來說，就是把後半段反轉，然後像「拉鍊」一樣跟前半段交叉合併。
**要求**：In-place modify，不能改變 node values，必須移動 nodes 本身。

-   **Input**: `head = [1,2,3,4]`
-   **Output**: `[1,4,2,3]`
-   **Input**: `head = [1,2,3,4,5]`
-   **Output**: `[1,5,2,4,3]`
-   **Constraints**:
    -   $1 <= n <= 5 \cdot 10^4$.
    -   $1 <= Node.val <= 1000$.

---

## 2. 🐢 Brute Force Approach (暴力解)

用一個 `deque` (Double-ended queue) 存所有的 nodes。
然後交替從 `front` 和 `back` 取出 node 串接。

-   **Time**: $O(n)$。
-   **Space**: $O(n)$ (因為存了 pointers)。
-   **Result**: 雖然可以過，但是題目通常期望 $O(1)$ Space。

---

## 3. 💡 The "Aha!" Moment (優化)

這題可以拆解成三個標準的 Linked List 子問題：

1.  **Find Middle**: 使用 **Slow & Fast Pointers** 找到鏈表的中點。
    -   `1->2->3->4->5` 中的 `3`。
2.  **Reverse Second Half**: 將中點之後的鏈表反轉。
    -   `3->4->5` 變成 `3<-4<-5` (或者 `3->null`, `5->4->null`)。
    -   通常我們斷開連結：`1->2->3` 和 `5->4`。
3.  **Merge Two Lists**: 將前半段 (`1->2->3`) 和反轉後的後半段 (`5->4`) 交替合併。
    -   `1->5->2->4->3`。

**步驟細節**：
-   **Find Mid**: `slow` 走一步，`fast` 走兩步。
-   **Split**: `mid = slow->next`; `slow->next = nullptr`.
-   **Reverse**: 標準 reverse linked list。
-   **Merge**: `temp1 = l1->next`, `temp2 = l2->next`, `l1->next = l2`, `l2->next = temp1`...

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

-   **Time Complexity**: $O(n)$
    -   Find Mid: $O(n/2)$.
    -   Reverse: $O(n/2)$.
    -   Merge: $O(n/2)$.
    -   Total: $O(n)$.
-   **Space Complexity**: $O(1)$
    -   In-place operation，只用了指標變數。
