# 09 LRU Cache — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/09_LRU_Cache.md`

> Quick links: [Source Solution](../09_LRU_Cache.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the LRU cache design problem. | 我先重述 LRU 快取設計題。 | Restatement |
| We need get and put operations in O(1) average time. | get 與 put 都要平均 O(1)。 | Restatement |
| get returns value and marks key as most recently used. | get 要回傳值並把 key 標為最近使用。 | Restatement |
| put inserts or updates key-value pair. | put 要插入或更新 key-value。 | Restatement |
| If capacity is full, evict least recently used item. | 容量滿時要淘汰最久未使用項目。 | Restatement |
| I will combine hash map with doubly linked list. | 我會結合 hash map 與雙向串列。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should both get and put be strict O(1) average? | get 與 put 都需嚴格平均 O(1) 嗎？ | Clarify |
| Is capacity always positive? | capacity 是否一定大於 0？ | Clarify |
| On get miss, should I return minus one only? | get miss 是否只回傳 -1？ | Clarify |
| On put existing key, should recency be refreshed? | put 已存在 key 時要刷新使用順序嗎？ | Clarify |
| Do you want cleanup notes for node memory in C++? | C++ 版本要不要提節點記憶體釋放？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline stores items in a list ordered by recency. | 基線是用 list 依使用新舊排序。 | Approach |
| get and put require linear search by key. | get/put 都要線性找 key。 | Approach |
| That gives O(n) operations and fails requirement. | 這會是 O(n) 操作，不符要求。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Hash map gives O(1) key-to-node lookup. | hash map 提供 O(1) 的 key 到 node 查找。 | Approach |
| Doubly linked list maintains recency order. | 雙向串列維護使用新舊順序。 | Approach |
| Move touched node to MRU side on get or put-update. | get 或 put 更新時把節點移到 MRU 端。 | Approach |
| Evict from LRU side when size exceeds capacity. | 超容量時從 LRU 端刪除。 | Approach |
| Dummy head and tail simplify insertion and removal. | dummy head/tail 可簡化插刪邊界。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I define Node with key, value, prev, and next fields. | 先定義含 key/value/prev/next 的 Node。 | Coding |
| I create dummy head and tail for linked-list boundaries. | 建立 dummy head 與 tail 當邊界。 | Coding |
| I keep unordered_map from key to node pointer. | 用 unordered_map 維護 key 到節點指標。 | Coding |
| Helper remove unlinks a node in O(1). | remove helper 以 O(1) 拆節點。 | Coding |
| Helper insert places a node before tail as MRU. | insert helper 把節點放 tail 前當 MRU。 | Coding |
| In get, on hit remove then insert to MRU and return value. | get 命中時先拆再插到 MRU 並回傳值。 | Coding |
| In put, update or insert, then evict head next when oversize. | put 更新或新增後，超容則淘汰 head->next。 | Coding |
| Keep map and list always synchronized after each operation. | 每次操作後保持 map 與 list 同步。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run capacity two with operations put1 put2 get1 put3 get2 put4 get1 get3 get4. | 我手跑容量 2 的經典操作序列。 | Dry-run |
| After put1 and put2, recency order is [1,2] from LRU to MRU. | put1/put2 後，新舊順序是 [1,2]。 | Dry-run |
| get1 returns one and moves key1 to MRU, order becomes [2,1]. | get1 回傳 1 並把 key1 移到 MRU，順序變 [2,1]。 | Dry-run |
| put3 evicts key2 because it is current LRU. | put3 會淘汰目前 LRU 的 key2。 | Dry-run |
| get2 now returns minus one. | 此時 get2 回傳 -1。 | Dry-run |
| put4 then evicts key1, leaving keys 3 and 4. | put4 接著淘汰 key1，剩下 key3 與 key4。 | Dry-run |
| Final gets return -1, 3, and 4 as expected. | 最後 get 依序回傳 -1、3、4。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: capacity equals one. | 案例一：capacity 為 1。 | Edge test |
| Case two: repeated put on same key. | 案例二：同一 key 連續 put。 | Edge test |
| Case three: get miss without prior insert. | 案例三：未插入前直接 get miss。 | Edge test |
| Case four: frequent alternation of get and put operations. | 案例四：頻繁交錯 get 與 put。 | Edge test |
| Case five: value update should keep key and refresh recency. | 案例五：更新值時要保留 key 並刷新新舊順序。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(1) average for get and put. | get/put 平均時間複雜度是 O(1)。 | Complexity |
| Space complexity is O(capacity). | 空間複雜度是 O(capacity)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Hash map lookup and update are average O(1). | hash map 查找與更新平均 O(1)。 | Complexity |
| Doubly linked-list insert and remove are O(1) with pointers. | 雙向串列靠指標插刪是 O(1)。 | Complexity |
| Each public operation performs constant number of such steps. | 每個公開操作只做常數次這些步驟。 | Complexity |
| We store at most capacity real nodes plus map entries. | 最多儲存 capacity 個真實節點與 map 項。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate data-structure responsibilities first. | 我先分清資料結構責任。 | If stuck |
| Map handles key lookup, list handles recency order. | map 管查找，list 管新舊順序。 | If stuck |
| Every key in map must point to a list node. | map 中每個 key 都要對應 list 節點。 | If stuck |
| On access, node must move to MRU side. | 存取後節點要移到 MRU 端。 | If stuck |
| I might have forgotten to erase map entry on eviction. | 我可能忘了淘汰時刪 map 項。 | If stuck |
| Let me fix eviction to remove from both list and map. | 我修正淘汰流程，同步刪 list 與 map。 | If stuck |
| I will rerun capacity-one and update-key tests. | 我重跑 capacity=1 與更新 key 測試。 | If stuck |
| Recency and values now both look correct. | 現在新舊順序與值都正確。 | If stuck |
| O(1) operations are preserved. | O(1) 操作目標仍被維持。 | If stuck |
| Great, implementation is stable now. | 很好，實作現在穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed LRU cache with map plus doubly linked list. | 我完成了 map + 雙向串列的 LRU 實作。 | Wrap-up |
| I validated misses, updates, and eviction behavior. | 我驗證了 miss、更新與淘汰行為。 | Wrap-up |
| get and put are O(1) average time. | get 與 put 平均時間是 O(1)。 | Wrap-up |
| Space is O(capacity). | 空間是 O(capacity)。 | Wrap-up |
| I can discuss LFU extension if you want. | 若你想要我可延伸討論 LFU。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Design LRU cache with O(1) get and put. | 設計 O(1) get/put 的 LRU。 | Cheat sheet |
| get hit returns value and refreshes recency. | get 命中回值並刷新新舊。 | Cheat sheet |
| get miss returns -1. | get miss 回傳 -1。 | Cheat sheet |
| put inserts or updates key-value. | put 插入或更新 key-value。 | Cheat sheet |
| Full cache evicts least recently used key. | 滿容量時淘汰最久未使用 key。 | Cheat sheet |
| Use map: key -> node*. | 用 map: key -> node*。 | Cheat sheet |
| Use doubly list for LRU order. | 用雙向串列維護 LRU 順序。 | Cheat sheet |
| Head side is LRU, tail side is MRU. | head 側是 LRU，tail 側是 MRU。 | Cheat sheet |
| Dummy boundaries simplify edge operations. | dummy 邊界簡化邊界操作。 | Cheat sheet |
| remove(node) unlinks in O(1). | remove(node) 可 O(1) 拆鏈。 | Cheat sheet |
| insert(node) puts node at MRU side. | insert(node) 把節點放到 MRU 端。 | Cheat sheet |
| On get hit: remove + insert + return value. | get 命中：remove+insert+回值。 | Cheat sheet |
| On put existing: update then move MRU. | put 已存在：更新並移到 MRU。 | Cheat sheet |
| On put new: insert then maybe evict LRU. | put 新 key：插入後必要時淘汰 LRU。 | Cheat sheet |
| Eviction must sync list and map deletion. | 淘汰必須同步刪 list 與 map。 | Cheat sheet |
| Time O(1) average each op. | 每操作平均時間 O(1)。 | Cheat sheet |
| Space O(capacity). | 空間 O(capacity)。 | Cheat sheet |
| Bug risk: stale map pointer after eviction. | 風險：淘汰後 map 殘留舊指標。 | Cheat sheet |
| Bug risk: wrong MRU/LRU side insertion. | 風險：MRU/LRU 方向插錯。 | Cheat sheet |
| Mention LFU as advanced follow-up. | 可提 LFU 作進階延伸。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hash map + doubly linked list LRU design is preserved.
- No hallucinated constraints: ✅ Uses source API behavior and O(1) requirement.
- Language simplicity: ✅ Clear spoken lines suitable for interviews.
