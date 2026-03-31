# 09 Course Schedule II — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/09_Course_Schedule_II.md`

> Quick links: [Source Solution](../09_Course_Schedule_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate course schedule two. | 我先重述 Course Schedule II。 | Restatement |
| We have course count and prerequisite pairs. | 題目給課程數與先修配對。 | Restatement |
| Pair [a,b] means b must be done before a. | [a,b] 表示先修 b 才能修 a。 | Restatement |
| Now we need one valid course order, not just true or false. | 這題要回一個合法修課順序，不只是布林。 | Restatement |
| If impossible because of cycle, return empty list. | 若因為有環不可行，就回空陣列。 | Restatement |
| I will use Kahn topological BFS with indegree. | 我會用 Kahn 拓撲 BFS 加 indegree。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Any valid topological order is acceptable, right? | 任意合法拓撲序都可接受嗎？ | Clarify |
| Should I return empty vector when cycle exists? | 若有環是否回空 vector？ | Clarify |
| Are courses labeled from zero to n minus one? | 課號是否為 0 到 n-1？ | Clarify |
| Can prerequisites list be empty? | prerequisites 是否可能為空？ | Clarify |
| Is BFS topological sort preferred over DFS reverse-postorder? | BFS 拓撲是否比 DFS 後序反轉更偏好？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries all permutations of courses. | 暴力法會嘗試所有課程排列。 | Approach |
| Validation per permutation is expensive. | 每個排列還要額外驗證，成本很高。 | Approach |
| This is factorial and impractical. | 這是階乘級，完全不實際。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build adjacency list and indegree array. | 建立鄰接表與 indegree 陣列。 | Approach |
| Push all courses with indegree zero into queue. | 把 indegree 為 0 的課程先入 queue。 | Approach |
| Pop queue, append to result order, and decrement indegree of neighbors. | 逐一出隊加入結果，並遞減鄰居 indegree。 | Approach |
| Whenever neighbor indegree becomes zero, push it. | 鄰居 indegree 變 0 就入隊。 | Approach |
| If result size equals n, return order; otherwise cycle exists so return empty. | 若結果長度等於 n 回順序，否則有環回空。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create graph adjacency list for numCourses nodes. | 我先建立 numCourses 節點的鄰接表。 | Coding |
| I initialize indegree array with zeros. | 我把 indegree 陣列初始化為 0。 | Coding |
| For each prerequisite [a,b], add edge b to a and indegree[a]++. | 對每個 [a,b] 加 b->a，並 indegree[a]++。 | Coding |
| I enqueue every node with indegree zero. | 我把所有 indegree=0 的節點入隊。 | Coding |
| I maintain result vector order. | 我維護結果向量 order。 | Coding |
| While queue not empty, pop course cur. | queue 非空時彈出課程 cur。 | Coding |
| Append cur to result order. | 把 cur 加入結果順序。 | Coding |
| For each neighbor, decrement indegree. | 對每個鄰居遞減 indegree。 | Coding |
| If indegree hits zero, enqueue neighbor. | 若 indegree 變 0，就把鄰居入隊。 | Coding |
| After BFS, return result if size equals numCourses else empty. | BFS 後若長度等於 numCourses 回結果，否則回空。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n four with prerequisites [[1,0],[2,0],[3,1],[3,2]]. | 我手跑 n=4，先修為 [[1,0],[2,0],[3,1],[3,2]]。 | Dry-run |
| Initial indegree is zero for course zero only. | 初始只有課程 0 的 indegree 為 0。 | Dry-run |
| Queue starts with zero, result becomes [0]. | queue 起始 [0]，結果先成 [0]。 | Dry-run |
| Decrement indegree of one and two, both become zero and enter queue. | 遞減 1 與 2 的 indegree，兩者變 0 並入隊。 | Dry-run |
| Pop one then two, each decrements indegree of three. | 依序出 1、2，各自遞減 3 的 indegree。 | Dry-run |
| Three becomes zero and is appended last. | 3 變 0 後最後加入結果。 | Dry-run |
| Final valid order is [0,1,2,3] or [0,2,1,3]. | 最終合法順序可為 [0,1,2,3] 或 [0,2,1,3]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: no prerequisites returns all courses in any order. | 案例一：無先修時可回任意全課程順序。 | Edge test |
| Case two: simple cycle like zero to one and one to zero returns empty. | 案例二：0->1->0 的小環應回空。 | Edge test |
| Case three: disconnected DAG components should both appear in result. | 案例三：非連通 DAG 分量都要出現在結果。 | Edge test |
| Case four: single course n one returns [0]. | 案例四：單課 n=1 回 [0]。 | Edge test |
| Case five: duplicate edges may inflate indegree and should be treated consistently. | 案例五：重複邊會影響 indegree，需一致處理。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(V plus E). | 時間複雜度是 O(V+E)。 | Complexity |
| Space complexity is O(V plus E). | 空間複雜度是 O(V+E)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Building adjacency and indegree uses O(E). | 建鄰接表與 indegree 的成本是 O(E)。 | Complexity |
| Each node enters and leaves queue at most once. | 每個節點最多入隊出隊各一次。 | Complexity |
| Each edge is processed once when decreasing indegree. | 每條邊在遞減 indegree 時處理一次。 | Complexity |
| So overall complexity is O(V plus E) time and O(V plus E) memory. | 整體即 O(V+E) 時間與 O(V+E) 記憶體。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate feasibility from ordering output. | 我先把可行性與輸出順序分開看。 | If stuck |
| Kahn BFS gives both in one pass. | Kahn BFS 一次就能同時處理兩者。 | If stuck |
| indegree zero means course has no remaining prerequisites. | indegree 為 0 代表沒有剩餘先修。 | If stuck |
| Queue stores courses ready to take now. | queue 存目前可修的課。 | If stuck |
| Popping one course unlocks its outgoing neighbors. | 出隊一門課會解鎖其後繼鄰居。 | If stuck |
| If queue becomes empty too early, a cycle blocks progress. | 若 queue 太早清空，表示有環卡住。 | If stuck |
| Result size check is the final cycle test. | 結果長度檢查就是最後環判定。 | If stuck |
| Let me test quickly with two-node cycle. | 我快速測雙節點環。 | If stuck |
| Size will be smaller than n, so return empty. | 結果長度會小於 n，因此回空。 | If stuck |
| Great, now the flow is consistent. | 很好，流程一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with Kahn topological BFS. | 我用 Kahn 拓撲 BFS 解題。 | Wrap-up |
| Queue starts from all indegree-zero courses. | queue 從所有 indegree=0 課程起跑。 | Wrap-up |
| We build a valid order while reducing indegrees. | 我們在遞減 indegree 同時建立合法順序。 | Wrap-up |
| If not all nodes are processed, cycle exists and result is empty. | 若非全部節點被處理，代表有環，結果為空。 | Wrap-up |
| Complexity is O(V plus E) time and O(V plus E) space. | 複雜度是 O(V+E) 時間與 O(V+E) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: return one valid course order. | 目標：回傳一個合法修課順序。 | Cheat sheet |
| If impossible, return empty list. | 不可行時回空陣列。 | Cheat sheet |
| Build directed graph b->a for [a,b]. | [a,b] 轉成有向邊 b->a。 | Cheat sheet |
| Compute indegree for each node. | 計算每節點 indegree。 | Cheat sheet |
| Enqueue all indegree-zero courses. | 把 indegree=0 課程入隊。 | Cheat sheet |
| Result vector starts empty. | 結果向量初始為空。 | Cheat sheet |
| Pop queue front course. | 彈出隊首課程。 | Cheat sheet |
| Append it to result. | 把它加入結果。 | Cheat sheet |
| For each outgoing neighbor indegree--. | 對每個後繼鄰居做 indegree--。 | Cheat sheet |
| If neighbor indegree becomes zero enqueue it. | 鄰居 indegree 變 0 就入隊。 | Cheat sheet |
| Continue until queue empty. | 持續直到 queue 清空。 | Cheat sheet |
| If result size == n return result. | 若結果長度==n，回結果。 | Cheat sheet |
| Else return empty due to cycle. | 否則因有環回空。 | Cheat sheet |
| Time O(V+E). | 時間 O(V+E)。 | Cheat sheet |
| Space O(V+E). | 空間 O(V+E)。 | Cheat sheet |
| Any valid topological order works. | 任一合法拓撲序都可。 | Cheat sheet |
| Common bug: edge direction reversed. | 常見錯誤：邊方向反了。 | Cheat sheet |
| Common bug: forgetting size check at end. | 常見錯誤：忘記最後長度檢查。 | Cheat sheet |
| Mention DFS postorder as alternative. | 可補充 DFS 後序反轉替代法。 | Cheat sheet |
| Validate with a cycle sample. | 用有環範例做驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Kahn BFS indegree topological ordering preserved.
- No hallucinated constraints: ✅ Return-empty-on-cycle behavior maintained.
- Language simplicity: ✅ Interview-ready concise narration.
