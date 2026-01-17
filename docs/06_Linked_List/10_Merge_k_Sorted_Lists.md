# Merge k Sorted Lists (合併 k 個排序鏈表)

## 1. 🧐 Problem Dissection (釐清問題)

題目給 `k` 個已經排序 (ascending order) 的 Linked Lists 陣列 `lists`。
請將這 `k` 個 Linked List 合併成 **一個** 排序 Linked List 並回傳。

- **Input**: `lists = [[1,4,5],[1,3,4],[2,6]]`
- **Output**: `[1,1,2,3,4,4,5,6]`
- **Input**: `[]`
- **Output**: `[]`
- **Constraints**:
  - $k == lists.length$
  - $0 <= k <= 10^4$
  - $0 <= lists[i].length <= 500$ (鏈表不長，但 k 很大)
  - $-10^4 <= lists[i][j] <= 10^4$
  - Sum of list lengths <= $10^4$.

---

## 2. 🐢 Brute Force Approach (暴力解)

將所有 node values 收集到一個 array，排序，然後重建 list。

- **Time**: $O(N \log N)$，其中 $N$ 是總節點數。
- **Space**: $O(N)$。
- **Result**: 有效，但沒利用到「已經是 k 個 sorted list」的特性。

---

## 3. 💡 The "Aha!" Moment (優化)

這是經典問題，有兩個主要優化方向：

**Approach 1: Min-Heap (Priority Queue)**
我們需要一直找出這 `k` 個 list 的所有 current head 中 **最小** 的那個。

1.  把 `k` 個 list 的 head 都放入 Min-Heap。
2.  Pop 最小的 node，接到我們的新 list 上。
3.  如果那個 node 有 `.next`，把 `.next` 放回 Min-Heap。
4.  重複直到 Heap 空。

- **Time**: $O(N \log k)$。因為 Heap size 最多為 `k`。
- **Space**: $O(k)$。

**Approach 2: Divide and Conquer (Merge Sort)**
兩兩合併。

- Round 1: Merge pairs (0,1), (2,3), (4,5)... -> 剩下 k/2 個 lists。
- Round 2: Merge new pairs... -> 剩下 k/4 個 lists。
- ...
- 直到剩下 1 個。
- Merge two lists 是 $O(n)$。
- 總共有 $\log k$ 輪。
- **Time**: $O(N \log k)$。
- **Space**: $O(1)$ (Iterative) or $O(\log k)$ (Recursive stack).

面試中，**Min-Heap** 比較直觀且易於解釋，而 **Divide and Conquer** 在空間複雜度上略勝一籌 (不需要額外的 heap space)。
讓我們實作 Divide and Conquer。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../merge_k_lists_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../merge_k_lists_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Divide and Conquer

```cpp
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        int k = lists.size();
        int interval = 1;

        while (interval < k) {
            for (int i = 0; i < k - interval; i += interval * 2) {
                lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }

        return lists[0];
    }

private:
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

### Approach: Min-Heap (C++)

```cpp
#include <queue>
#include <vector>

using namespace std;

class Solution {
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val; // Min-heap (smallest at top)
        }
    };
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;

        for (auto list : lists) {
            if (list) pq.push(list);
        }

        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (!pq.empty()) {
            ListNode* minNode = pq.top();
            pq.pop();

            tail->next = minNode;
            tail = tail->next;

            if (minNode->next) {
                pq.push(minNode->next);
            }
        }

        return dummy.next;
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists

        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們詳細註解 Divide and Conquer 的方法，因為它在空間上最優。

```cpp
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Edge case: empty input
        if (lists.empty()) return nullptr;

        // interval 代表我們目前要合併的 two lists 之間的距離
        // 一開始是 1 (合併相鄰的 0 & 1, 2 & 3, ...)
        // 下一輪是 2 (合併 0 & 2, 4 & 6 ...)
        // ...
        // 直到 interval 超過總長度
        int interval = 1;
        while (interval < lists.size()) {
            for (int i = 0; i < lists.size() - interval; i += interval * 2) {
                // 將 lists[i] 和 lists[i + interval] 合併
                // 結果存回 lists[i]
                lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }

        // 最後結果會匯聚在 lists[0]
        return lists[0];
    }

private:
    // Helper: Merge Two Sorted Lists (Iterative)
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (l1 && l2) {
            if (l1->val <= l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }

        if (l1) tail->next = l1;
        if (l2) tail->next = l2;

        return dummy.next;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(N \log k)$
  - $N$ 是所有節點總數。$k$ 是 lists 個數。
  - Divide and Conquer 類似 Merge Sort，樹高 $\log k$，每層處理 $N$ 個節點。
- **Space Complexity**: $O(1)$
  - 我們直接修改 `lists` array 和 nodes 的指標，沒有使用額外的 Heap 或 Recursion stack (Iterative merge)。
