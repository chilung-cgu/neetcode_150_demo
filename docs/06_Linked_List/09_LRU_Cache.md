---
title: "LRU Cache (最近少使用緩存)"
description: "設計一個 **LRU (Least Recently Used)** Cache 機制。 支援以下操作："
tags:
  - Linked List
difficulty: Medium
---

# LRU Cache (最近少使用緩存) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #146** — [題目連結](https://leetcode.com/problems/lru-cache/) | [NeetCode 解說](https://neetcode.io/problems/lru-cache)


## 1. 🧐 Problem Dissection (釐清問題)

設計一個 **LRU (Least Recently Used)** Cache 機制。
支援以下操作：

1.  `LRUCache(int capacity)`: 初始化，設定容量。
2.  `int get(int key)`: 如果 key 存在回傳 value，否則回傳 -1。
    -   注意：這算是一次 "use"，該 key 會變成最近剛使用過 (Most Recently Used)。
3.  `void put(int key, int value)`: 更新或插入 key-value。
    -   如果 key 已存在，更新 value，並標記為 "use"。
    -   如果 key 不存在，插入新的。如果容量已滿，必須 **移除** 最久沒被使用的那個項目 (LRU)，然後再插入。

**Constraints**:

-   $O(1)$ Time Complexity for both `get` and `put`.
-   Capacity ranges from 1 to 3000.

---

## 2. 🐢 Brute Force Approach (暴力解)

用 Array 或 List 存 `(key, value)` pairs。可以依使用時間排序。

-   `get`: 遍歷找 key -> $O(n)$. 移動到最前面 -> $O(n)$.
-   `put`: 插入或更新 -> $O(n)$。
-   **Result**: 效率太差，要求 $O(1)$。

---

## 3. 💡 The "Aha!" Moment (優化)

必須同時滿足：

1.  **快速查找 (Random Access)** -> 需要 **Hash Map**。 `map[key] = node`.
2.  **快速插入/刪除/移動順序 (Ordered Operations)** -> 需要 **Doubly Linked List**。

**架構 (Hash Map + Doubly Linked List)**:

-   **Doubly Linked List**:
    -   維護一個 ordered list，由 **LRU** (Head) 到 **MRU** (Tail)。
    -   或者反過來，Head 是 MRU，Tail 是 LRU。
    -   使用 Dummy Head 和 Dummy Tail 可以避免檢查 null，簡化代碼。
-   **Hash Map**:
    -   Key: Input Key
    -   Value: 指向 Linked List 節點的 Pointer (`Node*`)。

**操作邏輯**:

-   `get(key)`:
    -   Check Map。沒找到 -> -1。
    -   找到了 -> 取出 Node。
    -   **Move to MRU**: 從 List 斷開這個 Node，把它接在 MRU 端 (最前面或最後面)。
    -   回傳 value。
-   `put(key, value)`:
    -   如果 key 存在: 更新 value，**Move to MRU**。
    -   如果 key 不存在:
        -   Create new Node。
        -   Insert to MRU。
        -   Add to Map。
        -   檢查 Size > Capacity?
            -   是：**Remove LRU Node** (從 List 另一端移除，並從 Map 移除)。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../lru_cache_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../lru_cache_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Map + Doubly Linked List

```cpp
#include <unordered_map>

using namespace std;

class LRUCache {
private:
    struct Node {
        int key;
        int val;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
    };

    int capacity;
    unordered_map<int, Node*> map;
    Node* head; // Dummy Head (LRU side)
    Node* tail; // Dummy Tail (MRU side)

    // Helper: Remove node from list
    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    // Helper: Insert node at right (MRU)
    void insert(Node* node) {
        Node* prev = tail->prev;
        Node* next = tail;

        prev->next = node;
        next->prev = node;

        node->prev = prev;
        node->next = next;
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (map.find(key) == map.end()) {
            return -1;
        }
        Node* node = map[key];
        remove(node);
        insert(node);
        return node->val;
    }

    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            Node* node = map[key];
            node->val = value; // 1. 更新值
            remove(node);      // 2. 從目前位置拔除
            insert(node);      // 3. 放到 MRU 位置 (Tail 之前)
            return;            // 直接結束
        }

        Node* newNode = new Node(key, value);
        map[key] = newNode;
        insert(newNode);

        if (map.size() > capacity) {
            // Remove LRU (node after head)
            Node* lru = head->next;
            remove(lru);
            map.erase(lru->key);
            delete lru; // Remember to free memory
        }
    }

    // Destructor to clean up memory (Optional for LeetCode but good practice)
    ~LRUCache() {
        Node* curr = head;
        while (curr) {
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }
};
```

### Python Reference

```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # Left (LRU), Right (MRU)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): # Remove from list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node): # Insert at right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

这里解釋一下為什麼要兩個 Dummy Node (`head`, `tail`)。

-   如果我們不使用 Dummy Node，當 List 為空插入第一個元素，或者刪除最後一個元素時，都要檢查指標是否為 `nullptr`。
-   有了 Head (左邊界) 和 Tail (右邊界)，我們永遠是在「兩個節點中間」插入或刪除，邏輯會變成單純的指標交換，完全不需要 `if-else` 判斷邊界。

我們定義：

-   `head`: 指向 LRU 側 (Least Recently Used)。 `head->next` 是真正的 LRU。
-   `tail`: 指向 MRU 側 (Most Recently Used)。 `tail->prev` 是真正的 MRU。

```cpp
class LRUCache {
    // 內部節點結構
    struct Node {
        int key, val;
        Node *prev, *next;
        Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
    };

    int capacity;
    // Map: key -> Node*
    unordered_map<int, Node*> cache;
    // Dummy pointers
    Node *left, *right;

    // 從鏈表中移除節點
    void remove(Node* node) {
        Node* p = node->prev;
        Node* n = node->next;
        p->next = n;
        n->prev = p;
    }

    // 將節點插入到最右邊 (MRU)
    void insert(Node* node) {
        Node* p = right->prev; // 原本的最後一個
        Node* n = right;       // Dummy Tail

        p->next = node;
        node->prev = p;

        node->next = n;
        n->prev = node;
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        left = new Node(0, 0);  // LRU side dummy
        right = new Node(0, 0); // MRU side dummy
        left->next = right;
        right->prev = left;
    }

    int get(int key) {
        if (cache.find(key) != cache.end()) {
            // 找到了，更新它到 MRU
            remove(cache[key]);
            insert(cache[key]);
            return cache[key]->val;
        }
        return -1;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // 如果已經存在，先移除舊的 (為了更新順序和值)
            // 注意：這裡可以直接更新值然後 move，也可以刪掉重建，這裡選擇刪掉重建流程較統一
            remove(cache[key]);
        }

        // 建立新節點
        cache[key] = new Node(key, value);
        insert(cache[key]);

        // 檢查是否超容
        if (cache.size() > capacity) {
            // 移除 LRU (left->next)
            Node* lru = left->next;
            remove(lru);
            cache.erase(lru->key); // 別忘了從 map 移除
            // 因為 remove 沒有 delete memory (只是 unlink)，如果是 C++ 需要手動 delete
            // 不過在這個流程裡 lru pointer 還在所以可以 delete
            // *注意*：上一行 erase map 時 lru 指標可能已經失效嗎？不，指標本身還是有效的。
            // 比較安全的寫法是先存 int k = lru->key; cache.erase(k); delete lru;
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(1)$ for both `get` and `put`.
    -   Hash Map 操作平均 $O(1)$。
    -   Linked List 操作 (有了 pointer) 是 $O(1)$。
-   **Space Complexity**: $O(capacity)$
    -   存了 capacity 個節點。

---

## 7. 💼 Interview Tips (面試技巧) ⭐ 高頻題

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- LFU Cache?
- 分佈式 LRU？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 雙向鏈表操作錯誤
- ⚠️ Hash Map 更新不同步

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 O(1) 時間複雜度
- 💎 清晰的資料結構設計

---

## 📚 Related Problems (相關題目)

### 站內相關

### 進階挑戰
- [Lfu Cache](https://leetcode.com/problems/lfu-cache/) — LeetCode
