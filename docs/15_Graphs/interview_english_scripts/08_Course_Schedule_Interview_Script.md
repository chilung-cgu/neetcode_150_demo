# 08 Course Schedule — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/08_Course_Schedule.md`

> Quick links: [Source Solution](../08_Course_Schedule.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate course schedule. | 我先重述 Course Schedule。 | Restatement |
| We have numCourses and prerequisite pairs. | 題目給 numCourses 與先修課配對。 | Restatement |
| Pair [a,b] means we must finish b before a. | [a,b] 代表先修 b 才能修 a。 | Restatement |
| We need to decide whether all courses can be completed. | 要判斷能否完成所有課程。 | Restatement |
| This is equivalent to checking cycle in a directed graph. | 這等價於檢查有向圖是否有環。 | Restatement |
| I will use DFS with three-state coloring. | 我會用 DFS 三色標記法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are course labels from zero to numCourses minus one? | 課號是否從 0 到 numCourses-1？ | Clarify |
| Can prerequisites list be empty? | prerequisites 是否可能為空？ | Clarify |
| Is returning boolean enough? | 是否只要回傳布林值？ | Clarify |
| Should duplicate prerequisite edges be considered possible? | 先修邊是否可能重複？ | Clarify |
| Is either DFS cycle detection or Kahn BFS acceptable? | DFS 判環與 Kahn BFS 都可嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force permutation of course orders is factorial and impossible. | 暴力排列所有修課順序是階乘級不可行。 | Approach |
| We need graph-based cycle detection. | 我們需要用圖論做環檢測。 | Approach |
| If cycle exists, schedule is impossible. | 有環就不可能完成課程。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build adjacency list from prerequisite edges. | 先由先修邊建立鄰接表。 | Approach |
| Track each node state: zero unvisited, one visiting, two visited. | 每節點狀態：0 未訪、1 訪問中、2 已完成。 | Approach |
| DFS entering visiting node again means cycle. | DFS 再次碰到訪問中節點即代表有環。 | Approach |
| If DFS on all nodes finds no cycle, all courses are finishable. | 若全節點 DFS 都無環，就可完成全部課程。 | Approach |
| Complexity is linear in vertices plus edges. | 複雜度線性於頂點加邊數。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create adjacency list with numCourses vectors. | 我建立 numCourses 大小的鄰接表。 | Coding |
| For each pair [a,b], add edge b to a. | 對每個 [a,b]，加入 b->a 邊。 | Coding |
| I initialize state array with zeros. | 我把 state 陣列初始化為 0。 | Coding |
| Loop all courses, run DFS when state is zero. | 迴圈所有課程，state=0 時啟 DFS。 | Coding |
| In DFS, if state is one, return true cycle found. | DFS 中若 state=1，回 true 表示有環。 | Coding |
| If state is two, return false because already safe. | 若 state=2，回 false 因為已驗證安全。 | Coding |
| Set current state to one before exploring neighbors. | 展開鄰居前先把當前設為 1。 | Coding |
| Recurse neighbors, and if any has cycle propagate true. | 遞迴鄰居，若任何有環就往上回 true。 | Coding |
| After neighbors done, set state to two and return false. | 鄰居結束後設為 2，回 false。 | Coding |
| If any start DFS detects cycle, return false else true. | 任何起點偵測到環就回 false，否則 true。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run numCourses two with prerequisites [[1,0],[0,1]]. | 我手跑 numCourses=2，prerequisites=[[1,0],[0,1]]。 | Dry-run |
| Build edges zero to one and one to zero. | 建立 0->1 與 1->0。 | Dry-run |
| DFS starts at course zero and marks it visiting. | 從課程 0 開始 DFS，標為訪問中。 | Dry-run |
| DFS goes to course one and marks it visiting. | DFS 走到課程 1，也標為訪問中。 | Dry-run |
| From one we see neighbor zero already visiting. | 從 1 又看到鄰居 0 仍在訪問中。 | Dry-run |
| That is a back edge, so cycle exists. | 這是回邊，因此有環。 | Dry-run |
| Function returns false. | 函式回傳 false。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: no prerequisites returns true. | 案例一：無先修課回 true。 | Edge test |
| Case two: simple chain dependencies should return true. | 案例二：單鏈先修應回 true。 | Edge test |
| Case three: self dependency edge creates immediate cycle. | 案例三：自我依賴邊會立即成環。 | Edge test |
| Case four: disconnected graph with one cyclic component returns false. | 案例四：非連通圖只要有一個環分量就回 false。 | Edge test |
| Case five: multiple valid acyclic components returns true. | 案例五：多個無環分量應回 true。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(V plus E). | 時間複雜度是 O(V+E)。 | Complexity |
| Space complexity is O(V plus E). | 空間複雜度是 O(V+E)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Building adjacency list costs O(E). | 建鄰接表成本是 O(E)。 | Complexity |
| DFS visits each node and edge at most once in aggregate. | 整體 DFS 下每節點與每邊最多訪問一次。 | Complexity |
| So total runtime is O(V plus E). | 所以總時間是 O(V+E)。 | Complexity |
| Adjacency list plus state array plus recursion stack are O(V plus E). | 鄰接表、state、遞迴堆疊總計為 O(V+E)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me map courses to directed graph first. | 我先把課程轉成有向圖。 | If stuck |
| Completion is possible only when graph is acyclic. | 只有圖無環時才可能完成。 | If stuck |
| I will use three states to detect back edges. | 我用三狀態檢測回邊。 | If stuck |
| State one means node is on current DFS path. | 狀態 1 表示節點在當前遞迴路徑上。 | If stuck |
| Revisiting state one means cycle immediately. | 再訪 state 1 就是立即成環。 | If stuck |
| State two nodes are already validated safe. | state 2 節點是已驗證安全。 | If stuck |
| Let me test quickly with [1,0] and [0,1]. | 我快速測 [1,0] 與 [0,1]。 | If stuck |
| It should fail due to two-node cycle. | 它應因雙節點環而失敗。 | If stuck |
| This confirms DFS state transitions. | 這可確認 DFS 狀態轉移。 | If stuck |
| Great, I can continue coding now. | 很好，現在可以繼續實作。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it by cycle detection in directed graph. | 我用有向圖環檢測解了這題。 | Wrap-up |
| Three-state DFS catches back edges cleanly. | 三色 DFS 可清楚抓到回邊。 | Wrap-up |
| Any cycle means impossible schedule. | 只要有環就無法完成排課。 | Wrap-up |
| Complexity is O(V plus E) time and O(V plus E) space. | 複雜度是 O(V+E) 時間與 O(V+E) 空間。 | Wrap-up |
| This is a canonical topological-validity pattern. | 這是拓撲可行性題的經典模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: can all courses be finished. | 目標：是否能修完所有課。 | Cheat sheet |
| Build directed graph from prerequisites. | 由先修條件建立有向圖。 | Cheat sheet |
| Edge b to a for pair [a,b]. | 配對 [a,b] 轉為 b->a。 | Cheat sheet |
| Use state array with 0 1 2. | 使用狀態陣列 0/1/2。 | Cheat sheet |
| 0 means unvisited. | 0 代表未訪問。 | Cheat sheet |
| 1 means visiting in current path. | 1 代表目前遞迴路徑中。 | Cheat sheet |
| 2 means fully processed safe node. | 2 代表已完成且安全。 | Cheat sheet |
| DFS on each unvisited node. | 對每個未訪節點做 DFS。 | Cheat sheet |
| Entering state 1 again => cycle. | 再遇到 state 1 即成環。 | Cheat sheet |
| Cycle found => return false. | 發現環就回 false。 | Cheat sheet |
| Finish node => mark state 2. | 節點完成後標為 2。 | Cheat sheet |
| No cycle anywhere => return true. | 全圖無環就回 true。 | Cheat sheet |
| Empty prerequisite list => true. | 無先修清單 => true。 | Cheat sheet |
| Self-loop prerequisite => false. | 自迴圈先修 => false。 | Cheat sheet |
| Time O(V+E). | 時間 O(V+E)。 | Cheat sheet |
| Space O(V+E). | 空間 O(V+E)。 | Cheat sheet |
| Kahn BFS is valid alternative. | Kahn BFS 也是合法替代。 | Cheat sheet |
| Common bug: wrong edge direction. | 常見錯誤：邊方向寫反。 | Cheat sheet |
| Common bug: missing state reset to 2. | 常見錯誤：忘記將狀態設為 2。 | Cheat sheet |
| Explain with small cycle sample. | 用小環案例解釋最直觀。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS 3-state cycle detection aligned.
- No hallucinated constraints: ✅ Directed-edge semantics and feasibility logic preserved.
- Language simplicity: ✅ Clear, short interview phrasing.
