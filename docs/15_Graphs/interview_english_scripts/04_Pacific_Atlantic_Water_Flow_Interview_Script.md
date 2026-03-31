# 04 Pacific Atlantic Water Flow — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/04_Pacific_Atlantic_Water_Flow.md`

> Quick links: [Source Solution](../04_Pacific_Atlantic_Water_Flow.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate pacific atlantic water flow. | 我先重述 Pacific Atlantic Water Flow。 | Restatement |
| We have a height matrix. | 題目給一個高度矩陣。 | Restatement |
| Water can flow from higher or equal cell to lower or equal cell. | 水可由高或等高流向低或等高。 | Restatement |
| Top and left edges touch Pacific. | 上邊與左邊連到太平洋。 | Restatement |
| Bottom and right edges touch Atlantic. | 下邊與右邊連到大西洋。 | Restatement |
| We need cells that can reach both oceans. | 我們要找可同時到兩個海洋的格子。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is grid guaranteed non-empty? | grid 是否保證非空？ | Clarify |
| Is movement only four directions? | 移動是否只限四方向？ | Clarify |
| Can equal heights flow between cells? | 等高格之間是否可流動？ | Clarify |
| Should result order matter or any order is fine? | 結果順序是否重要，還是任意即可？ | Clarify |
| Are coordinates returned as row and column pairs? | 回傳格式是否為 row,col 座標對？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force starts DFS or BFS from every cell twice. | 暴力法對每格都做兩次 DFS/BFS。 | Approach |
| One search checks reachability to Pacific, another to Atlantic. | 一次檢查到太平洋，一次檢查到大西洋。 | Approach |
| This is too slow at O((mn) squared). | 這會太慢，達到 O((mn)^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Reverse the thinking: start from oceans and move inward. | 反向思考：從海洋往內陸反推。 | Approach |
| From Pacific borders, mark all cells reachable by non-decreasing heights. | 從太平洋邊界出發，標記可逆流到的格子。 | Approach |
| From Atlantic borders, do the same marking. | 從大西洋邊界同樣標記一次。 | Approach |
| A cell in both visited sets can flow to both oceans. | 同時在兩集合中的格子即可流向兩海。 | Approach |
| Complexity drops to O(m times n). | 複雜度可降到 O(m*n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create two visited matrices: pacific and atlantic. | 我建立兩個 visited 矩陣：pacific 與 atlantic。 | Coding |
| I run DFS from top row and left column for Pacific. | 我從上邊與左邊做 Pacific DFS。 | Coding |
| I run DFS from bottom row and right column for Atlantic. | 我從下邊與右邊做 Atlantic DFS。 | Coding |
| In DFS, I only move to neighbor with height greater or equal to current. | DFS 中只走到高度大於等於當前的鄰居。 | Coding |
| That models reverse water flow from ocean inward. | 這就是海洋逆流向內陸的模型。 | Coding |
| I skip out-of-bound or already visited cells. | 我跳過越界或已訪問格子。 | Coding |
| After both traversals, I scan all cells. | 兩次遍歷後我掃描全部格子。 | Coding |
| If pacific and atlantic are both true, add coordinate to result. | 若 pacific 與 atlantic 都為 true，就加入答案。 | Coding |
| Return result list. | 回傳結果座標列表。 | Coding |
| This avoids per-cell repeated searches. | 這避免每格重複搜尋。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the five by five sample grid. | 我手跑 5x5 範例網格。 | Dry-run |
| Pacific DFS starts from top and left borders. | Pacific DFS 從上邊與左邊開始。 | Dry-run |
| Atlantic DFS starts from bottom and right borders. | Atlantic DFS 從下邊與右邊開始。 | Dry-run |
| Cell [0,4] is reachable from both sides, so it qualifies. | [0,4] 可被兩邊逆流到，因此符合。 | Dry-run |
| Cell [2,2] also appears in both visited sets. | [2,2] 也同時出現在兩個 visited 集合。 | Dry-run |
| Low trapped cells may appear in only one set. | 低窪受限格常只出現在單一集合。 | Dry-run |
| Final intersection matches expected coordinates. | 最後交集會吻合預期座標。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one cell grid can reach both oceans. | 案例一：單格網格可同時到兩海。 | Edge test |
| Case two: flat grid where all heights are equal. | 案例二：全等高平面網格。 | Edge test |
| Case three: strictly increasing rows and cols. | 案例三：列行都嚴格遞增。 | Edge test |
| Case four: strictly decreasing landscape. | 案例四：嚴格遞減地形。 | Edge test |
| Case five: long narrow grid one by n. | 案例五：狹長 1xn 網格。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m times n). | 時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m times n). | 空間複雜度是 O(m*n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each cell can be visited at most once in Pacific traversal. | 每格在 Pacific 遍歷中最多訪問一次。 | Complexity |
| Each cell can be visited at most once in Atlantic traversal. | 每格在 Atlantic 遍歷中最多訪問一次。 | Complexity |
| So total traversal work is linear O(mn). | 因此總遍歷工作量是線性 O(mn)。 | Complexity |
| Two visited matrices plus recursion stack give O(mn) memory. | 兩個 visited 矩陣加遞迴堆疊為 O(mn) 記憶體。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me switch to reverse-flow viewpoint. | 我切換到逆流視角。 | If stuck |
| From ocean to cell, height must be non-decreasing. | 從海到內陸時高度必須不下降。 | If stuck |
| I should not start DFS from every cell. | 我不該從每個格子都起 DFS。 | If stuck |
| Start only from four borders of two oceans. | 只要從兩海的四條邊開始。 | If stuck |
| I maintain two visited sets separately. | 我分別維護兩個 visited 集合。 | If stuck |
| Final answer is intersection of those sets. | 最後答案是兩集合交集。 | If stuck |
| Let me test one-cell case quickly. | 我快速驗證單格案例。 | If stuck |
| It should appear in both sets. | 它應該同時在兩集合。 | If stuck |
| Equal height move must be allowed. | 等高移動必須允許。 | If stuck |
| Great, now traversal condition is clear. | 很好，現在遍歷條件清楚了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with two reverse DFS traversals from ocean borders. | 我用兩次從海岸逆推的 DFS 解題。 | Wrap-up |
| Pacific and Atlantic reachability are tracked separately. | 太平洋與大西洋可達性分開追蹤。 | Wrap-up |
| Intersection of visited sets gives final cells. | visited 交集就是最終座標。 | Wrap-up |
| Complexity is O(mn) time and O(mn) space. | 複雜度是 O(mn) 時間與 O(mn) 空間。 | Wrap-up |
| This is the standard reverse-thinking graph-grid pattern. | 這是經典反向思考的網格圖解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: cells flowing to both oceans. | 目標：可流向兩海的格子。 | Cheat sheet |
| Water flow is downhill or flat forward. | 正向水流是下坡或等高。 | Cheat sheet |
| Reverse view: move uphill or flat from ocean. | 反向看：從海往上坡或等高走。 | Cheat sheet |
| Create pacific visited matrix. | 建立 pacific visited。 | Cheat sheet |
| Create atlantic visited matrix. | 建立 atlantic visited。 | Cheat sheet |
| DFS from top and left borders for Pacific. | 從上邊左邊做 Pacific DFS。 | Cheat sheet |
| DFS from bottom and right borders for Atlantic. | 從下邊右邊做 Atlantic DFS。 | Cheat sheet |
| DFS condition: neighbor height >= current. | DFS 條件：鄰居高>=當前。 | Cheat sheet |
| Skip out of bound. | 跳過越界。 | Cheat sheet |
| Skip visited cell. | 跳過已訪問。 | Cheat sheet |
| After traversals, scan all cells. | 遍歷後掃全部格子。 | Cheat sheet |
| If both visited true, add coordinate. | 兩邊皆 true 就加入。 | Cheat sheet |
| Return result list. | 回傳結果列表。 | Cheat sheet |
| One-cell grid always qualifies. | 單格網格一定符合。 | Cheat sheet |
| Equal heights are reachable. | 等高可互達。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Space O(mn). | 空間 O(mn)。 | Cheat sheet |
| Common bug: wrong inequality direction. | 常見錯誤：不等號方向寫反。 | Cheat sheet |
| Common bug: starting from all cells. | 常見錯誤：從所有格起跑。 | Cheat sheet |
| Explain intersection concept clearly. | 清楚說明交集概念。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Reverse DFS/BFS from borders with set intersection.
- No hallucinated constraints: ✅ Ocean boundaries and height rules preserved.
- Language simplicity: ✅ Clear short interview lines.
