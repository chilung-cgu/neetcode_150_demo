# 11 Number of Connected Components — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/11_Number_of_Connected_Components.md`

> Quick links: [Source Solution](../11_Number_of_Connected_Components.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate number of connected components. | 我先重述 Number of Connected Components。 | Restatement |
| We have n nodes and undirected edges. | 題目給 n 個節點與無向邊。 | Restatement |
| A connected component is a maximal set where every pair is connected by path. | 連通分量是節點彼此可達的最大集合。 | Restatement |
| We need total count of components. | 我們要回傳分量總數。 | Restatement |
| Isolated node also counts as one component. | 孤立節點也算一個分量。 | Restatement |
| I will use Union Find and decrement count on successful unions. | 我會用 Union Find，在成功合併時遞減計數。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are nodes labeled from zero to n minus one? | 節點編號是否為 0 到 n-1？ | Clarify |
| Is graph guaranteed undirected? | 圖是否保證無向？ | Clarify |
| Can there be duplicate edges? | 是否可能有重複邊？ | Clarify |
| Can n be one with empty edges? | n=1 且邊為空是否可能？ | Clarify |
| Should we return integer component count only? | 是否只回傳整數分量數？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| DFS from each unvisited node also works and counts components. | 從每個未訪節點做 DFS 也能計算分量。 | Approach |
| But we still need adjacency structure and visited tracking. | 但仍需鄰接結構與 visited 管理。 | Approach |
| Union Find is concise for dynamic merging view. | 從動態合併視角看，Union Find 更精簡。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Initialize component count as n. | 初始分量數設為 n。 | Approach |
| Parent array starts with each node as its own root. | parent 初始每節點自成根。 | Approach |
| For each edge u v, find their roots. | 對每條邊 u,v 查兩端根節點。 | Approach |
| If roots differ, union them and component count minus one. | 若根不同就合併，分量數減一。 | Approach |
| If roots same, edge is internal and count stays unchanged. | 若根相同，邊在分量內，計數不變。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize parent vector of size n with parent[i]=i. | 我先建立大小 n 的 parent，令 parent[i]=i。 | Coding |
| I set components count to n. | 我把 components 設為 n。 | Coding |
| I define find with path compression. | 我定義帶路徑壓縮的 find。 | Coding |
| I iterate each undirected edge [u,v]. | 我逐一處理每條無向邊 [u,v]。 | Coding |
| Compute ru=find(u) and rv=find(v). | 計算 ru=find(u)、rv=find(v)。 | Coding |
| If ru not equal rv, union them. | 若 ru!=rv，就把兩者合併。 | Coding |
| After successful union, components minus minus. | 成功合併後 components--。 | Coding |
| If ru equals rv, skip because already connected. | 若 ru==rv，代表已連通，直接略過。 | Coding |
| Continue through all edges. | 持續直到邊都處理完。 | Coding |
| Return components as final answer. | 回傳 components 作最終答案。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n five with edges [0,1],[1,2],[3,4]. | 我手跑 n=5，邊為 [0,1],[1,2],[3,4]。 | Dry-run |
| Start components equals five. | 一開始 components=5。 | Dry-run |
| Union zero and one, components becomes four. | 合併 0 與 1，components 變 4。 | Dry-run |
| Union one and two merges node two into same set, components becomes three. | 再合併 1 與 2，components 變 3。 | Dry-run |
| Union three and four, components becomes two. | 合併 3 與 4，components 變 2。 | Dry-run |
| No more edges left to merge. | 沒有更多邊可合併。 | Dry-run |
| Final answer is two components. | 最終答案是 2 個分量。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n one and no edges returns one. | 案例一：n=1 且無邊回 1。 | Edge test |
| Case two: n five and no edges returns five. | 案例二：n=5 無邊回 5。 | Edge test |
| Case three: fully connected chain returns one. | 案例三：全連通鏈狀圖回 1。 | Edge test |
| Case four: duplicate edge should not change count after first union. | 案例四：重複邊在首次合併後不應再改計數。 | Edge test |
| Case five: separate clusters plus isolated node. | 案例五：多個群加一個孤立點。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(E alpha N). | 時間複雜度是 O(E·α(N))。 | Complexity |
| Space complexity is O(N). | 空間複雜度是 O(N)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We process each edge once. | 每條邊只處理一次。 | Complexity |
| Each find and union is near constant with path compression. | 路徑壓縮下 find/union 近乎常數。 | Complexity |
| Therefore total runtime is O(E alpha N). | 因此總時間是 O(E·α(N))。 | Complexity |
| Parent array stores one root pointer per node, so O(N) memory. | parent 每節點一個根指標，因此空間 O(N)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me think in terms of merging groups. | 我先用群組合併角度思考。 | If stuck |
| Initially each node is its own component. | 初始每個節點都是獨立分量。 | If stuck |
| Every successful union reduces component count by one. | 每次成功 union，分量數減一。 | If stuck |
| If two nodes already share root, count should not change. | 若兩端同根，計數不應改變。 | If stuck |
| Path compression avoids deep parent chains. | 路徑壓縮可避免 parent 鏈過深。 | If stuck |
| Let me test quickly with no-edge input. | 我快速測無邊輸入。 | If stuck |
| Answer should equal n in that case. | 該情況答案應等於 n。 | If stuck |
| This confirms initialization is correct. | 這可確認初始化正確。 | If stuck |
| Then process edges one by one. | 接著就逐邊處理即可。 | If stuck |
| Great, the counting rule is clear. | 很好，計數規則已清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with Union Find component counting. | 我用 Union Find 分量計數解題。 | Wrap-up |
| Start from n components and merge by edges. | 從 n 個分量開始，沿邊合併。 | Wrap-up |
| Only successful unions reduce the answer. | 只有成功合併才會減少答案。 | Wrap-up |
| Complexity is O(E alpha N) time and O(N) space. | 複雜度是 O(E·α(N)) 時間與 O(N) 空間。 | Wrap-up |
| This is a standard connectivity-counting DSU pattern. | 這是標準 DSU 連通分量計數模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: count connected components in undirected graph. | 目標：計算無向圖連通分量數。 | Cheat sheet |
| Initialize components = n. | 初始化 components=n。 | Cheat sheet |
| parent[i]=i for all nodes. | 對所有節點設 parent[i]=i。 | Cheat sheet |
| Use find with path compression. | find 用路徑壓縮。 | Cheat sheet |
| Iterate each edge [u,v]. | 逐條處理邊 [u,v]。 | Cheat sheet |
| ru=find(u), rv=find(v). | ru=find(u), rv=find(v)。 | Cheat sheet |
| If ru!=rv, union and components--. | 若 ru!=rv，合併且 components--。 | Cheat sheet |
| If ru==rv, skip count change. | 若 ru==rv，不改計數。 | Cheat sheet |
| After all edges, return components. | 邊處理完後回 components。 | Cheat sheet |
| No edges => answer n. | 無邊 => 答案 n。 | Cheat sheet |
| Connected chain => answer one. | 連通鏈 => 答案 1。 | Cheat sheet |
| Duplicate edge should not double-decrement. | 重複邊不可重複遞減。 | Cheat sheet |
| Time O(E alpha N). | 時間 O(E·α(N))。 | Cheat sheet |
| Space O(N). | 空間 O(N)。 | Cheat sheet |
| DFS/BFS alternative also valid. | DFS/BFS 替代法也可。 | Cheat sheet |
| DSU is concise without adjacency list. | DSU 可不建鄰接表，寫法精簡。 | Cheat sheet |
| Common bug: wrong node index range. | 常見錯誤：節點索引範圍處理錯。 | Cheat sheet |
| Common bug: missing path compression. | 常見錯誤：漏掉路徑壓縮。 | Cheat sheet |
| Keep union logic deterministic. | 讓 union 邏輯保持一致。 | Cheat sheet |
| Explain count-minus-one intuition clearly. | 清楚說明「合併就減一」直覺。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Union-Find component counting preserved.
- No hallucinated constraints: ✅ Undirected connectivity semantics maintained.
- Language simplicity: ✅ Interview-focused short statements.
