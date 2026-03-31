# 02 Clone Graph — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/02_Clone_Graph.md`

> Quick links: [Source Solution](../02_Clone_Graph.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate clone graph. | 我先重述 Clone Graph。 | Restatement |
| We are given one node in an undirected connected graph. | 題目給無向連通圖中的一個節點。 | Restatement |
| We need to return a deep copy of the whole graph. | 我們要回傳整張圖的深拷貝。 | Restatement |
| Deep copy means new nodes, not shared old pointers. | 深拷貝代表新節點，不能共用舊指標。 | Restatement |
| Graph may contain cycles, so revisits must be handled. | 圖中可能有環，需正確處理重訪。 | Restatement |
| I will use DFS with old-to-new hash map. | 我會用 DFS 配舊到新節點的雜湊表。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can input node be null? | 輸入節點是否可能為空？ | Clarify |
| Is graph guaranteed connected from the given node? | 給定節點是否可到達整張圖？ | Clarify |
| Are node values unique? | 節點值是否唯一？ | Clarify |
| Should neighbor ordering be preserved as in traversal? | 鄰居順序是否需維持原遍歷順序？ | Clarify |
| Is either DFS or BFS cloning acceptable? | DFS 或 BFS 複製都可接受嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A naive recursive copy without memo will loop forever on cycles. | 沒有記錄表的遞迴拷貝遇環會無限循環。 | Approach |
| It can also create duplicate cloned nodes for one original node. | 也可能把同一原節點重複複製多次。 | Approach |
| So memoization mapping is mandatory. | 因此映射記錄是必要條件。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use hash map from original node pointer to cloned node pointer. | 用雜湊表記錄原節點指標到新節點指標。 | Approach |
| DFS on a node returns its cloned counterpart. | DFS 對一節點回傳其複製節點。 | Approach |
| If node already exists in map, return mapped clone directly. | 若節點已在 map，就直接回傳對應複製。 | Approach |
| Otherwise create clone, store mapping first, then clone neighbors recursively. | 否則先建立 clone、先存映射，再遞迴複製鄰居。 | Approach |
| This handles cycles and shared neighbors correctly. | 這可正確處理環與共享鄰居。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If input node is null, return null. | 若輸入節點為空，回傳空指標。 | Coding |
| I keep unordered_map oldNode to newNode. | 我維護 unordered_map oldNode->newNode。 | Coding |
| In clone function, first check map contains node. | 在 clone 函式先檢查 map 是否已有此節點。 | Coding |
| If yes, return existing cloned node. | 若有，直接回傳既有 clone。 | Coding |
| If no, create new node with same value. | 若無，建立同值新節點。 | Coding |
| Store mapping before exploring neighbors. | 在展開鄰居前先存映射。 | Coding |
| Loop original neighbors and clone each recursively. | 迴圈原鄰居並遞迴複製。 | Coding |
| Push cloned neighbors into new node neighbor list. | 把複製鄰居加入新節點 neighbor 列表。 | Coding |
| Return newly built clone node. | 回傳建好的複製節點。 | Coding |
| Entry call starts from given node. | 入口呼叫從給定節點開始。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run a four-node cycle graph. | 我手跑一個四節點環圖。 | Dry-run |
| Start cloning node one, map is empty so create clone one. | 先複製節點 1，map 空，因此建立 clone1。 | Dry-run |
| Visit neighbor two, create clone two and map it. | 走到鄰居 2，建立 clone2 並記錄。 | Dry-run |
| From two visit one again, map hit returns clone one directly. | 從 2 回訪 1，map 命中直接回 clone1。 | Dry-run |
| Continue for neighbors three and four similarly. | 鄰居 3、4 也同樣流程。 | Dry-run |
| No infinite recursion happens due to map short-circuit. | 因 map 截斷，不會無限遞迴。 | Dry-run |
| Final cloned graph keeps structure but uses new nodes. | 最終結構相同，但全部是新節點。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: null input returns null. | 案例一：空輸入回空。 | Edge test |
| Case two: single node with no neighbors. | 案例二：單節點且無鄰居。 | Edge test |
| Case three: two nodes with one undirected edge. | 案例三：兩節點一條無向邊。 | Edge test |
| Case four: cycle graph to verify no infinite loop. | 案例四：有環圖，確認不會無限循環。 | Edge test |
| Case five: node with multiple neighbors shared by paths. | 案例五：多路徑共享鄰居的節點。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(V plus E). | 時間複雜度是 O(V+E)。 | Complexity |
| Space complexity is O(V) for map plus recursion stack. | 空間複雜度是 O(V)，來自 map 與遞迴堆疊。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each vertex is cloned exactly once. | 每個頂點只會被複製一次。 | Complexity |
| Each edge is traversed through neighbor lists once per adjacency representation. | 每條邊會在鄰接表遍歷時被處理。 | Complexity |
| So total traversal cost is O(V plus E). | 因此總遍歷成本是 O(V+E)。 | Complexity |
| Hash map and recursive call stack are both O(V) worst case. | 雜湊表與遞迴堆疊最壞都為 O(V)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on cycle handling first. | 我先聚焦在處理環。 | If stuck |
| Without map, recursion may never stop. | 沒有 map，遞迴可能不會停止。 | If stuck |
| Map key is old pointer, value is new pointer. | map 的 key 是舊指標，value 是新指標。 | If stuck |
| I must save mapping before cloning neighbors. | 我必須在克隆鄰居前先存映射。 | If stuck |
| That breaks cyclic recursion safely. | 這樣能安全切斷環狀遞迴。 | If stuck |
| Let me test quickly with two nodes pointing each other. | 我快速測兩節點互相連線。 | If stuck |
| Second visit should return from map immediately. | 第二次訪問應立刻從 map 返回。 | If stuck |
| Then neighbor links are still built correctly. | 同時鄰居連線仍會建立正確。 | If stuck |
| This guarantees deep copy and structure preservation. | 這可保證深拷貝與結構保留。 | If stuck |
| Great, now implementation order is clear. | 很好，現在實作順序清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved clone graph with DFS plus memo map. | 我用 DFS 加記憶映射解了 Clone Graph。 | Wrap-up |
| Memo map prevents duplicate clones and cycle loops. | 映射可避免重複複製與環狀死循環。 | Wrap-up |
| Creating map entry before recursion is the key step. | 遞迴前先寫 map 是關鍵步驟。 | Wrap-up |
| Complexity is O(V plus E) time and O(V) extra space. | 複雜度是 O(V+E) 時間與 O(V) 額外空間。 | Wrap-up |
| This is the standard interview-safe deep-copy pattern for graphs. | 這是圖深拷貝的標準面試安全寫法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: deep copy an undirected graph. | 目標：深拷貝無向圖。 | Cheat sheet |
| Input may contain cycles. | 輸入可能含環。 | Cheat sheet |
| Use DFS or BFS with hash map. | 用 DFS/BFS 搭配雜湊表。 | Cheat sheet |
| Map old node pointer to new node pointer. | map 舊指標到新指標。 | Cheat sheet |
| Null input returns null. | 空輸入回空。 | Cheat sheet |
| If node in map, return mapped clone. | 節點在 map 就直接回 clone。 | Cheat sheet |
| Else create new clone node. | 否則建立新 clone 節點。 | Cheat sheet |
| Store mapping immediately. | 立即存入映射。 | Cheat sheet |
| Then clone each neighbor recursively. | 再遞迴複製每個鄰居。 | Cheat sheet |
| Append cloned neighbors to clone list. | 把 clone 鄰居加入列表。 | Cheat sheet |
| Return clone node. | 回傳 clone 節點。 | Cheat sheet |
| Entry is clone(start node). | 入口是 clone(起始節點)。 | Cheat sheet |
| Prevents infinite recursion on cycles. | 可防止環造成無限遞迴。 | Cheat sheet |
| Preserves original graph structure. | 保留原圖拓樸結構。 | Cheat sheet |
| Uses brand-new nodes only. | 全程使用新節點物件。 | Cheat sheet |
| Time O(V+E). | 時間 O(V+E)。 | Cheat sheet |
| Space O(V). | 空間 O(V)。 | Cheat sheet |
| Common bug: mapping too late. | 常見錯誤：太晚才寫映射。 | Cheat sheet |
| Common bug: shallow copy neighbors. | 常見錯誤：鄰居做成淺拷貝。 | Cheat sheet |
| Validate with a cycle example. | 用環狀範例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS + old-to-new map cloning preserved.
- No hallucinated constraints: ✅ Graph-cycle and deep-copy semantics respected.
- Language simplicity: ✅ Clear short interview narration.
