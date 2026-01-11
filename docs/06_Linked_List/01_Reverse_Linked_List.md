# Reverse Linked List (反轉鏈結串列)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 singly linked list 的 head。
請反轉這個 List，並回傳新的 head。

-   **Input**: `head = [1,2,3,4,5]`
-   **Output**: `[5,4,3,2,1]`
-   **Constraints**:
    -   number of nodes: $0 \dots 5000$.
    -   `-5000 <= Node.val <= 5000`.

---

## 2. 🐢 Brute Force Approach (暴力解)

用一個 Stack 把所有 node values 存起來，然後重建一個新的 List。

-   **Time**: $O(n)$。
-   **Space**: $O(n)$。
-   **Result**: 雖然可行，但面試官通常期望 $O(1)$ Space。

---

## 3. 💡 The "Aha!" Moment (優化)

我們可以用 **Iterative** 的方式原地 (In-place) 反轉。

我們只需要維護三個指標：

1.  `prev`: 指向「前一個」節點 (反轉後的下一個)。初始為 `nullptr`。
2.  `curr`: 指向「當前」節點。初始為 `head`。
3.  `next`: 用來暫存 `curr->next`，因為我們會切斷這個連結。

**步驟**：
當 `curr` 不為空時：

1.  `next = curr->next` (暫存下一步)
2.  `curr->next = prev` (反轉箭頭！指向前一個人)
3.  `prev = curr` (推進 prev)
4.  `curr = next` (推進 curr)

當迴圈結束時，`curr` 是 `nullptr`，而 `prev` 會停在原本的最後一個節點（也就是新的 Head）。回傳 `prev`。

**Recursive Approach (Optional)**:
遞迴解法雖然優雅，但空間複雜度是 $O(n)$ (Stack depth)。Iterative 是最佳解。

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative (O(1) Space)

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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            // 1. Save next
            ListNode* nextTemp = curr->next;

            // 2. Reverse link
            curr->next = prev;

            // 3. Move pointers
            prev = curr;
            curr = nextTemp;
        }

        return prev;
    }
};
```

### Approach: Recursive (O(n) Space)

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Base case: empty or single node
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // Recursive step
        ListNode* newHead = reverseList(head->next);

        // Reverse the link
        head->next->next = head; // 讓下一個節點指向自己
        head->next = nullptr;    // 斷開自己原本的指向

        return newHead;
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // prev 會變成新的 tail (指向 nullptr)
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            // 暫存下一個節點，因為我們等一下會切斷 curr->next
            ListNode* nextNode = curr->next;

            // 關鍵動作：將當前節點的指針「回頭」指
            curr->next = prev;

            // 往下一個節點推進
            // prev 跑到現在的位置
            prev = curr;
            // curr 跑到剛剛暫存的位置
            curr = nextNode;
        }

        // 當 curr 為 null 時，loop 結束，此時 prev 指向原本的最後一個節點
        // 也就是新的 head
        return prev;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   遍歷每個節點一次。
-   **Space Complexity**: $O(1)$
    -   只使用了 `prev`, `curr`, `next` 三個指標，沒有額外的資料結構。
