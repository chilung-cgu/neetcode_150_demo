---
title: "Copy List with Random Pointer (複製含隨機指標的鏈結串列)"
description: "題目給一個 Linked List，每個節點除了 `next` 指標外，還有一個 `random` 指標，可能指向 list 中的任意節點或 null。 請 **Deep Copy** 這個 List。"
tags:
  - Linked List
difficulty: Medium
---

# Copy List with Random Pointer (複製含隨機指標的鏈結串列) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #138** — [題目連結](https://leetcode.com/problems/copy-list-with-random-pointer/) | [NeetCode 解說](https://neetcode.io/problems/copy-linked-list-with-random-pointer)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Linked List，每個節點除了 `next` 指標外，還有一個 `random` 指標，可能指向 list 中的任意節點或 null。
請 **Deep Copy** 這個 List。

- **Deep Copy**:
  - 所有新節點必須是新創建的 (new operator)。
  - 如果是 `val` 相同但 address 相同的節點，不算是 deep copy。
  - 新節點的 `next` 和 `random` 必須指向**新的**對應節點。

- **Input**: `[[7,null],[13,0],[11,4],[10,2],[1,0]]` (val, random_index)
- **Output**: same structure, new addresses.
- **Constraints**:
  - $0 <= n <= 1000$.
  - $-10000 <= Node.val <= 10000$.

---

## 2. 🐢 Brute Force Approach (暴力解)

先創建所有新節點，暫時不管 pointers。
然後對於每個節點，遍歷整個 list 找 random 指向誰。

- **Time**: $O(n^2)$。
- **Result**: 太慢。

---

## 3. 💡 The "Aha!" Moment (優化)

**Approach 1: Hash Map** (最直觀)
用一個 `HashMap<OldNode*, NewNode*>` 來建立舊節點與新節點的對應關係。

1.  第一遍遍歷：創建所有 New Node，並存入 Map。`map[old] = new Node(old->val)`。
2.  第二遍遍歷：設置 pointers。
    - `map[old]->next = map[old->next]`
    - `map[old]->random = map[old->random]`

- **Time**: $O(n)$。
- **Space**: $O(n)$ (Hash Map)。

**Approach 2: Interleaving (交錯串接)** (進階，省空間)
如果我們不能用 Hash Map 呢？

1.  **Interleave**: 在每個舊節點後面插入它的複製節點。
    - `A -> B -> C` 變成 `A -> A' -> B -> B' -> C -> C'`。
2.  **Set Random**: `A->next->random = A->random->next`。
    - 因為 `A'` 是 `A->next`，`A'` 的 `random` 是 `A->random` 的複製版 (也就是 `A->random->next`)。
3.  **Separate**: 拆開成兩個 lists。
    - `A->next = A->next->next` (A 連到 B)。
    - `A'->next = A'->next->next` (A' 連到 B')。

- **Time**: $O(n)$。
- **Space**: $O(1)$ (不計算 Output space)。

面試時，HashMap 解法通常就夠了，除非面試官要求 $O(1)$ space。我們先寫 HashMap 版本，因為實作簡單且不易出錯。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../copy_random_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../copy_random_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Map `O(n)` Space

```cpp
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        unordered_map<Node*, Node*> oldToNew;

        // 1. Create all nodes
        Node* curr = head;
        while (curr) {
            oldToNew[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // 2. Link pointer
        curr = head;
        while (curr) {
            oldToNew[curr]->next = oldToNew[curr->next];
            oldToNew[curr]->random = oldToNew[curr->random];
            curr = curr->next;
        }

        return oldToNew[head];
    }
};
```

### Approach: Interleaving `O(1)` Space

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        // 1. Interleave: A -> A' -> B -> B'
        Node* curr = head;
        while (curr) {
            Node* newNode = new Node(curr->val);
            newNode->next = curr->next;
            curr->next = newNode;
            curr = newNode->next;
        }

        // 2. Set Random
        curr = head;
        while (curr) {
            if (curr->random) {
                // curr->next 是 A'
                // curr->random 是 randomTarget
                // curr->random->next 是 randomTarget'
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next; // Move to next old node
        }

        // 3. Separate
        Node* oldHead = head;
        Node* newHead = head->next;
        Node* currOld = oldHead;
        Node* currNew = newHead;

        while (currOld) {
            currOld->next = currOld->next->next;
            // 檢查是否還有下一個 new node
            if (currNew->next) {
                currNew->next = currNew->next->next;
            }

            currOld = currOld->next;
            currNew = currNew->next;
        }

        return newHead;
    }
};
```

### Python Reference

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

這邊採用 Hash Map 方法，直觀且足夠面試。

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;

        // Map: 原節點地址 -> 新節點地址
        unordered_map<Node*, Node*> map;

        // Loop 1: 建立所有新節點，並存入 Map
        Node* curr = head;
        while (curr != nullptr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Loop 2: 根據原節點的關係，連接新節點
        curr = head;
        while (curr != nullptr) {
            // map[curr] 是當前的新節點
            // map[curr]->next 應該指向 「curr->next 對應的新節點」
            map[curr]->next = map[curr->next];

            // 同理，random 指向 「curr->random 對應的新節點」
            map[curr]->random = map[curr->random];

            curr = curr->next;
        }

        return map[head];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - 兩次遍歷 list。
- **Space Complexity**: $O(n)$
  - Hash Map 存了 n 個 entry。
  - 如果用 Interleaving method 可以優化到 $O(1)$ extra space。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- O(1) 空間解法？
- Clone Graph?

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ Hash Map 對應關係錯誤
- ⚠️ random 指標處理錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 Interleaving 解法 O(1) 空間
- 💎 兩種解法的 trade-off

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Clone Graph (複製圖)](../15_Graphs/02_Clone_Graph.md)
