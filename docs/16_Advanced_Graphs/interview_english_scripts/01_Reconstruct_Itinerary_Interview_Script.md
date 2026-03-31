# 01 Reconstruct Itinerary — Interview English Script (C++)

> Source aligned with: `docs/16_Advanced_Graphs/01_Reconstruct_Itinerary.md`

> Quick links: [Source Solution](../01_Reconstruct_Itinerary.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate reconstruct itinerary. | 我先重述 Reconstruct Itinerary。 | Restatement |
| We are given flight tickets from airport to airport. | 題目給一組機票 from 到 to。 | Restatement |
| Trip must start at JFK and use every ticket exactly once. | 行程必須從 JFK 開始，且每張票只用一次。 | Restatement |
| If multiple valid itineraries exist, return lexicographically smallest one. | 若有多解，要回字典序最小的行程。 | Restatement |
| This is an Eulerian path style traversal on directed graph. | 這是有向圖的歐拉路徑型問題。 | Restatement |
| I will use Hierholzer DFS with min lexical next choice. | 我會用 Hierholzer DFS 搭配字典序最小下一站。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is solution guaranteed to exist? | 題目是否保證一定有解？ | Clarify |
| Should itinerary length be tickets count plus one? | 行程長度是否應為 tickets+1？ | Clarify |
| Can duplicate tickets between same airports appear? | 同機場對之間是否可能有重複機票？ | Clarify |
| Is lexical order based on normal string order? | 字典序是否採一般字串比較？ | Clarify |
| Should we return vector of airport strings? | 是否回傳機場字串向量？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Backtracking over all ticket permutations is exponential. | 暴力回溯所有機票排列是指數級。 | Approach |
| Even with pruning, worst-case branching is huge. | 即使剪枝，最壞分支仍很大。 | Approach |
| We need Euler-path-specific linear edge usage strategy. | 我們需要針對歐拉路徑的線性用邊策略。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build adjacency map from source airport to min-heap of destinations. | 建立鄰接表：source 對應目的地最小堆。 | Approach |
| DFS from JFK, always consuming smallest lexical outgoing edge first. | 從 JFK 做 DFS，總是先用字典序最小出邊。 | Approach |
| During DFS, keep walking while outgoing edges exist. | DFS 中只要還有出邊就持續往下走。 | Approach |
| Add airport to result after consuming all its outgoing edges. | 當出邊耗盡時才把機場加入結果。 | Approach |
| Reverse postorder result to get final itinerary order. | 將後序結果反轉即可得到最終行程。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create unordered_map from string to min-heap of strings. | 我建立 string 到最小堆的鄰接 map。 | Coding |
| For each ticket from to, push destination into source heap. | 對每張 from,to 機票，把 to 推入 from 的堆。 | Coding |
| I define dfs function taking current airport. | 我定義接收目前機場的 dfs 函式。 | Coding |
| While current airport heap is not empty, pop smallest next and dfs it. | 當前機場堆非空時，彈最小 next 並遞迴。 | Coding |
| This pop operation consumes one ticket exactly once. | 這個 pop 代表消耗一張票且只用一次。 | Coding |
| After no outgoing edge remains, push current airport into result. | 無出邊後把目前機場加入結果。 | Coding |
| Start dfs from JFK. | 從 JFK 啟動 dfs。 | Coding |
| Reverse result vector at the end. | 最後反轉結果向量。 | Coding |
| Return reversed result as itinerary. | 回傳反轉後結果作行程。 | Coding |
| This ensures lexical smallest valid Euler path. | 這可確保字典序最小的合法歐拉路徑。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run tickets JFK SFO, JFK ATL, SFO ATL, ATL JFK, ATL SFO. | 我手跑票組：JFK->SFO, JFK->ATL, SFO->ATL, ATL->JFK, ATL->SFO。 | Dry-run |
| From JFK, lexical smaller next is ATL before SFO. | 從 JFK 出發，字典序較小的是 ATL。 | Dry-run |
| DFS continues ATL to JFK then JFK to SFO then SFO to ATL then ATL to SFO. | DFS 路徑持續 ATL->JFK->SFO->ATL->SFO。 | Dry-run |
| Airports are appended on backtracking when no outgoing ticket remains. | 回溯時在無出邊節點依序加入機場。 | Dry-run |
| Postorder list is reversed to itinerary order. | 後序清單反轉後變成行程順序。 | Dry-run |
| Final itinerary is JFK ATL JFK SFO ATL SFO. | 最終行程是 JFK,ATL,JFK,SFO,ATL,SFO。 | Dry-run |
| It is lexicographically smallest valid one. | 這是字典序最小的合法解。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single ticket JFK to A. | 案例一：只有一張 JFK->A 機票。 | Edge test |
| Case two: duplicate identical tickets between same airports. | 案例二：同機場間重複機票。 | Edge test |
| Case three: branch choices where lexical tie-breaking matters. | 案例三：有分支選擇且字典序會影響結果。 | Edge test |
| Case four: path requiring backtracking and postorder insertion. | 案例四：需要回溯與後序插入的路徑。 | Edge test |
| Case five: long chain with no branching. | 案例五：無分支的長鏈路徑。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(E log E) due to heap push and pop over edges. | 時間複雜度是 O(E log E)，主因邊的堆操作。 | Complexity |
| Space complexity is O(V plus E). | 空間複雜度是 O(V+E)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each ticket edge is inserted once into a min-heap. | 每張機票邊會被推入最小堆一次。 | Complexity |
| Each edge is also popped once during DFS traversal. | 每條邊在 DFS 中也只會被彈出一次。 | Complexity |
| Heap operations contribute logarithmic factor, giving O(E log E) total. | 堆操作帶來對數因子，總計 O(E log E)。 | Complexity |
| Adjacency storage and recursion/result arrays use O(V plus E) memory. | 鄰接儲存與遞迴/結果共用 O(V+E) 記憶體。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me identify this as Eulerian path, not shortest path. | 我先確認這是歐拉路徑，不是最短路。 | If stuck |
| We must use every ticket exactly once. | 我們必須每張票剛好用一次。 | If stuck |
| Hierholzer adds node after exhausting outgoing edges. | Hierholzer 在出邊耗盡後才加入節點。 | If stuck |
| That is why result is collected in reverse order. | 這就是結果會先逆序收集的原因。 | If stuck |
| Lexical requirement means using min-heap neighbors. | 字典序要求代表鄰居要用最小堆。 | If stuck |
| Pop edge when traversed to avoid reuse. | 遍歷時要 pop 邊，避免重用。 | If stuck |
| Let me test quickly with two JFK choices. | 我快速測 JFK 有兩個目的地時。 | If stuck |
| Smaller lexical choice should be consumed first. | 字典序小的目的地應先被取用。 | If stuck |
| Reverse final list to get forward itinerary. | 最後把清單反轉成正向行程。 | If stuck |
| Great, flow now matches required constraints. | 很好，流程已符合題目限制。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with Hierholzer DFS on directed ticket graph. | 我用有向機票圖的 Hierholzer DFS 解題。 | Wrap-up |
| Each edge is consumed once via heap pop. | 每條邊透過堆 pop 僅消耗一次。 | Wrap-up |
| Postorder airport append plus reverse builds itinerary. | 後序加入機場並反轉可還原行程。 | Wrap-up |
| Min-heap neighbors enforce lexical smallest answer. | 最小堆鄰居可保證字典序最小解。 | Wrap-up |
| Complexity is O(E log E) time and O(V plus E) space. | 複雜度是 O(E log E) 時間與 O(V+E) 空間。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: itinerary from JFK using all tickets once. | 目標：從 JFK 出發且每票用一次。 | Cheat sheet |
| If many valid paths, choose lexical smallest. | 多解時選字典序最小。 | Cheat sheet |
| Model tickets as directed edges. | 把機票建成有向邊。 | Cheat sheet |
| Use map source -> min-heap destinations. | 使用 source->目的地最小堆。 | Cheat sheet |
| DFS starts at JFK. | DFS 從 JFK 開始。 | Cheat sheet |
| While outgoing exists, pop smallest next. | 有出邊就彈最小 next。 | Cheat sheet |
| Recurse to next airport. | 遞迴到下一機場。 | Cheat sheet |
| Edge pop means ticket consumed. | pop 邊代表機票已使用。 | Cheat sheet |
| No outgoing means append current airport. | 無出邊時加入當前機場。 | Cheat sheet |
| This is postorder recording. | 這是後序記錄。 | Cheat sheet |
| Reverse result at end. | 最後反轉結果。 | Cheat sheet |
| Return reversed list. | 回傳反轉後清單。 | Cheat sheet |
| Length should be tickets + 1. | 長度應為 tickets+1。 | Cheat sheet |
| Time O(E log E). | 時間 O(E log E)。 | Cheat sheet |
| Space O(V+E). | 空間 O(V+E)。 | Cheat sheet |
| Common bug: append before exploring children. | 常見錯誤：先加入節點再展開子節點。 | Cheat sheet |
| Common bug: forgetting reverse step. | 常見錯誤：忘記最後反轉。 | Cheat sheet |
| Common bug: not enforcing lexical order. | 常見錯誤：沒強制字典序。 | Cheat sheet |
| Mention relation to Eulerian path. | 可提與歐拉路徑關聯。 | Cheat sheet |
| Validate with branching JFK sample. | 用 JFK 分支範例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hierholzer + lexical min-heap strategy preserved.
- No hallucinated constraints: ✅ JFK start, all-ticket usage, lexical tie-break respected.
- Language simplicity: ✅ interview-safe concise lines.
