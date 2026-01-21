# Remove Nth Node From End of List (移除鏈結串列倒數第 N 個節點) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #19** — [題目連結](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [NeetCode 解說](https://neetcode.io/problems/remove-nth-node-from-end-of-list)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Linked List 的 `head` 和一個整數 `n`。
請刪除倒數第 `n` 個節點，並回傳新的 `head`。

- **Input**: `head = [1,2,3,4,5], n = 2`
- **Output**: `[1,2,3,5]` (移除倒數第 2 個，也就是 4)
- **Input**: `head = [1], n = 1`
- **Output**: `[]`
- **Input**: `head = [1,2], n = 1`
- **Output**: `[1]`
- **Constraints**:
  - $1 <= sz <= 30$.
  - $0 <= Node.val <= 100$.
  - $1 <= n <= sz$.
  - **Challenge**: Could you do this in one pass? (一次遍歷)

---

## 2. 🐢 Brute Force Approach (暴力解)

1.  第一次遍歷算長度 `L`。
2.  目標是刪除第 `L - n` 個節點 (0-indexed)。
3.  第二次遍歷走到前一個節點，執行刪除。

- **Time**: $O(2L) = O(L)$。
- **Result**: 雖然仍是 $O(L)$，但兩次遍歷有點多了。題目希望一次。

---

## 3. 💡 The "Aha!" Moment (優化)

使用 **Two Pointers (快慢指針)**。

讓 `fast` 指針先行 `n + 1` 步。
然後 `slow` 和 `fast` 同時前進，直到 `fast` 到達尾端 (`nullptr`)。
此時 `slow` 剛好會在「被刪除節點」的 **前一個 (prev)** 位置。
為什麼？

- 假設我們想刪除倒數第 `n` 個。
- 如果要刪除它，我們需要停在它前面的節點。
- 所以 `slow` 和 `tail` 的距離應該要是 `n + 1` (包含被刪除的那個)。
- 所以 `fast` 比 `slow` 領先 `n + 1` 步。當 `fast` 到底，`slow` 就到位了。

**Dummy Node**:
如果我们要刪除的是 **Head** (倒數第 L 個)，就需要 Dummy Node 來處理這種 edge case。`dummy->next = head`。我們讓 `slow` 從 `dummy` 開始。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../remove_nth_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../remove_nth_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: One Pass with Two Pointers

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode* first = &dummy;
        ListNode* second = &dummy;

        // 1. Advance first pointer so that the gap between first and second is n nodes apart
        // 其實我們要找的是倒數第 n 個的前一個，所以要拉開 n + 1 的距離
        for (int i = 0; i <= n; i++) {
            first = first->next;
        }

        // 2. Move first to the end, maintaining the gap
        while (first != nullptr) {
            first = first->next;
            second = second->next;
        }

        // now second is at the node BEFORE the one we want to remove
        ListNode* toDelete = second->next;
        second->next = second->next->next;

        // In real C++, we should delete toDelete to avoid memory leak
        // delete toDelete;

        return dummy.next;
    }
};
```

### Python Reference

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // 使用 dummy node，解決如果刪除的是頭節點的情況
        // 例如 [1], n=1 -> 刪除 1，變成空。
        ListNode dummy(0);
        dummy.next = head;

        ListNode* fast = &dummy;
        ListNode* slow = &dummy;

        // 讓 fast 先走 n 步
        // 這樣 fast 和 slow 之間相隔 n 個節點 (不含 slow 本身)
        // 具體來說，我們希望找到倒數第 n 個節點的「前一個」
        // 所以實際上我們希望 slow 停在 L-n-1 的位置 (0-indexed)
        // 也就是 slow 距離結尾還有 n+1 個節點
        // 所以 fast 要比 slow 快 n+1 步

        for (int i = 0; i < n + 1; i++) {
            fast = fast->next;
        }

        // 一起走，直到 fast 到底
        while (fast != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }

        // 此時 slow 的下一個就是我們要刪除的
        ListNode* toTrash = slow->next;
        slow->next = slow->next->next;

        // 釋放記憶體 (Good Practice in C++)
        // delete toTrash; (面試時可以提一下但不一定要寫，LeetCode 不需要)

        return dummy.next;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(L)$
  - 我們只遍歷了 list 一次。
- **Space Complexity**: $O(1)$
  - 只使用固定指針。
