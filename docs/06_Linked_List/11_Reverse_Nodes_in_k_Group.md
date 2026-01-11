# Reverse Nodes in k-Group (k 個一組反轉鏈結串列)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Linked List 和一個整數 `k`。
請將 Linked List 每 `k` 個節點分成一組，並在每組內部進行反轉。
如果最後剩餘的節點不滿 `k` 個，則保持原樣，不反轉。
空間複雜度必須是 $O(1)$。

-   **Input**: `head = [1,2,3,4,5], k = 2`
-   **Output**: `[2,1,4,3,5]`
    -   `[1,2]` reverse -> `[2,1]`
    -   `[3,4]` reverse -> `[4,3]`
    -   `[5]` remain -> `[5]`
-   **Input**: `head = [1,2,3,4,5], k = 3`
-   **Output**: `[3,2,1,4,5]`
    -   `[1,2,3]` reverse -> `[3,2,1]`
    -   `[4,5]` remain -> `[4,5]`

---

## 2. 🐢 Brute Force Approach (暴力解)

用 Stack。每收集 k 個，就 pop 出來建成新 list。

-   **Time**: $O(n)$。
-   **Space**: $O(k)$ for stack.
-   **Result**: 題目要求 $O(1)$ space。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 Linked List 指針操作的集大成者。
我們需要反覆執行「反轉一段子鏈表」的操作。

**關鍵結構**:
我們需要维护幾個指針來進行操作：

1.  `groupPrev`: 指向當前要處理的 group 的「前一個」節點 (上一組的 tail)。
2.  `kth`: 指向當前 group 的「最後一個」節點 (這一組的 tail)。
3.  `groupNext`: 指向「下一組」的開始 (`kth->next`)。

**步驟**:
1.  從 `head` 開始遍歷。
2.  找到第 `k` 個節點 `kth`。
    -   如果找不到 (不滿 k 個)，直接結束。
3.  **Reverse** `groupPrev->next` 到 `kth` 之間的節點。
    -   這是一個標準的 reverse 操作，但需要小心邊界。
    -   原本的 `first` (groupPrev->next) 會變成 `last`。
    -   反轉後，讓 `groupPrev->next` 指向新的 head (`kth`)。
    -   讓原本的 `first` 指向 `groupNext`。
4.  更新 `groupPrev` 到下一組的起點前 (也就是剛反轉完的 tail)。
5.  重複。

**Dummy Node**:
因為 Head 也會變，所以用 Dummy Node `dummy->next = head` 很重要。`groupPrev` 初始為 `dummy`。

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* groupPrev = &dummy;

        while (true) {
            // 1. Find the kth node
            ListNode* kth = groupPrev;
            for (int i = 0; i < k && kth != nullptr; i++) {
                kth = kth->next;
            }

            if (kth == nullptr) break; // Not enough nodes left

            // 2. Remember next group
            ListNode* groupNext = kth->next;

            // 3. Reverse the group
            // Range: [groupPrev->next, kth]
            // We need to reverse pointers within this range
            // prev starts at groupNext because the first node of this group
            // will point to groupNext after reversal
            ListNode* prev = groupNext;
            ListNode* curr = groupPrev->next;

            while (curr != groupNext) {
                ListNode* tmp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = tmp;
            }

            // 4. Update connections
            // old first node (now last) is already pointing to groupNext (via initialization of prev)
            // now we need groupPrev to point to the new first node (which is 'kth', locally 'prev' after loop but technically let's trace carefully)

            // wait, inside loop:
            // 1->2->3->4, k=2. groupPrev at header. kth at 2. groupNext at 3.
            // prev = 3, curr = 1.
            // Loop 1: tmp=2, 1->3, prev=1, curr=2
            // Loop 2: tmp=3, 2->1, prev=2, curr=3 (break)
            // now prev is 2 (which is the new head of this reversed group)

            ListNode* temp = groupPrev->next; // This was the first node, now it's the tail
            groupPrev->next = prev; // Connect previous part to new head
            groupPrev = temp; // Move groupPrev to the tail of this group
        }

        return dummy.next;
    }
};
```

### Python Reference

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # Reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Link
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0);
        dummy.next = head;
        // groupPrev 指向 "上一組" 的最後一個節點 (作為這一組的 anchor)
        ListNode* groupPrev = &dummy;

        while (true) {
            // 1. 檢查剩餘節點是否足夠 k 個
            ListNode* kth = getKth(groupPrev, k);
            if (!kth) break; // 不夠就停止，保持原樣

            // groupNext 是 "下一組" 的第一個節點
            ListNode* groupNext = kth->next;

            // 2. 反轉 [groupPrev->next ... kth] 這一區間

            // prev 初始化為 groupNext
            // 這樣反轉後，原本的第一個節點 (現在的最後一個) 會自然指向下一組的頭
            ListNode* prev = groupNext;
            ListNode* curr = groupPrev->next;

            while (curr != groupNext) {
                ListNode* temp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = temp;
            }

            // 3. 修正外部連接
            // 反轉完後，prev 會指向這一組新的頭 (原本的 kth)
            // groupPrev->next (原本的第一個，現在是最後一個) 已經在上面指向了 groupNext
            // 我們只需要讓 groupPrev 指向新的頭
            ListNode* temp = groupPrev->next; // 暫存原本的第一個節點 (它變成了上一組的 groupPrev)
            groupPrev->next = kth;            // 連接新的頭
            groupPrev = temp;                 // groupPrev 移動到這一組的尾巴，為下一輪做準備
        }

        return dummy.next;
    }

    ListNode* getKth(ListNode* curr, int k) {
        while (curr && k > 0) {
            curr = curr->next;
            k--;
        }
        return curr;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   每個節點被尋訪兩次：一次是 `getKth` 確認長度，一次是反轉指針。
    -   $O(2n) = O(n)$。
-   **Space Complexity**: $O(1)$
    -   使用固定數量的指針。
