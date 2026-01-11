# Add Two Numbers (兩數相加)

## 1. 🧐 Problem Dissection (釐清問題)

題目給兩個 **非空** 的 Linked List，代表兩個非負整數。
這些數字是 **逆序 (Reverse Order)** 儲存的，也就是說個位數在 head。
請將這兩個數字相加，並以 Linked List 形式回傳（同樣是逆序）。

-   **Input**: `l1 = [2,4,3] (342), l2 = [5,6,4] (465)`
-   **Output**: `[7,0,8] (807)`
-   **Input**: `l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`
-   **Output**: `[8,9,9,9,0,0,0,1]`
-   **Constraints**:
    -   The number of nodes in each linked list is in the range `[1, 100]`.
    -   `0 <= Node.val <= 9`.
    -   It is guaranteed that the list represents a number that does not have leading zeros.

---

## 2. 🐢 Brute Force Approach (暴力解)

先將 Linked List 轉成整數 (int/long)，相加後，再轉回 Linked List。

-   **Issue**: List 長度可達 100，這代表數字有 100 位數。即使用 `unsigned long long` 也存不下。
-   **Result**: 必須直接在 Linked List 上做加法模擬。

---

## 3. 💡 The "Aha!" Moment (優化)

這就是標準的直式加法 (Column Addition)。
我們同時遍歷兩個 List，從 head (個位數) 開始加。
維護一個 `carry` (進位)。

-   `sum = val1 + val2 + carry`
-   `new_digit = sum % 10`
-   `new_carry = sum / 10`
-   Create node with `new_digit`.

**注意細節**:
1.  List 長度可能不同。如果一個走完了，就當作 0。
2.  最後如果還有 `carry` (例如 500 + 500 = 1000)，要多新增一個 node。

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int digit1 = (l1 != nullptr) ? l1->val : 0;
            int digit2 = (l2 != nullptr) ? l2->val : 0;

            int sum = digit1 + digit2 + carry;
            int digit = sum % 10;
            carry = sum / 10;

            ListNode* newNode = new ListNode(digit);
            tail->next = newNode;
            tail = tail->next;

            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        return dummy.next;
    }
};
```

### Python Reference

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // 使用 dummy node 簡化代碼
        ListNode dummy(0);
        ListNode* current = &dummy;
        int carry = 0;

        // 條件包含 carry != 0，這是為了處理最後還要進位的情況 (e.g., 99 + 1 = 100)
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            // 如果 list 已經走到底，則值視為 0
            int x = (l1 != nullptr) ? l1->val : 0;
            int y = (l2 != nullptr) ? l2->val : 0;

            // 計算和與進位
            int sum = x + y + carry;
            carry = sum / 10;

            // 創建新節點存個位數 (sum % 10)
            current->next = new ListNode(sum % 10);
            current = current->next;

            // 移動指針
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        return dummy.next;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\max(m, n))$
    -   遍歷較長的那個 List。
-   **Space Complexity**: $O(\max(m, n))$
    -   創建新的 Linked List 來儲存結果。
    -   (如果不算 Output Space，則是 $O(1)$ extra space)。
