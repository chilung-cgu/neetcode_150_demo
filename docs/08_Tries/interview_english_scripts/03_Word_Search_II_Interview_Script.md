# 03 Word Search II — Interview English Script (C++)

> Source aligned with: `docs/08_Tries/03_Word_Search_II.md`

> Quick links: [Source Solution](../03_Word_Search_II.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the Word Search II problem. | 我先重述 Word Search II 題目。 | Restatement |
| We have a board and a list of candidate words. | 題目給字元棋盤與候選單字清單。 | Restatement |
| We need all words that can be formed by adjacent cells. | 要找所有能由相鄰格子拼出的單字。 | Restatement |
| Movement is four directions, and one cell cannot be reused in one word. | 移動限上下左右，同單字不可重用同格。 | Restatement |
| Running single-word search for every word is too expensive. | 對每個字單獨搜尋成本太高。 | Restatement |
| I will combine Trie and backtracking DFS with pruning. | 我會用 Trie + 回溯 DFS + 剪枝。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are board moves only up, down, left, and right? | 棋盤移動只限上下左右嗎？ | Clarify |
| Is diagonal movement disallowed? | 對角移動是否不允許？ | Clarify |
| Can a cell be used only once per single word path? | 同一單字路徑中格子只能用一次嗎？ | Clarify |
| Should output include each found word only once? | 輸出每個找到的字是否只出現一次？ | Clarify |
| Are all words lowercase letters and potentially duplicated in input list? | words 都是小寫，且可能重複嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force runs Word Search backtracking separately for each word. | 暴力法對每個單字各跑一次回溯搜尋。 | Approach |
| For many words, this repeats the same board exploration heavily. | 單字多時會重複探索相同棋盤路徑。 | Approach |
| Complexity becomes too large with big dictionary size. | 字典大時複雜度會過高。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build Trie from all words first. | 先把所有單字建成 Trie。 | Approach |
| Start DFS from each board cell while traversing Trie simultaneously. | 從每格起 DFS，同步在 Trie 上前進。 | Approach |
| If next character edge does not exist in Trie, prune immediately. | 若 Trie 無對應邊，立即剪枝返回。 | Approach |
| When reaching a Trie word terminal, add word and deduplicate. | 抵達單字終點就加入答案並去重。 | Approach |
| Backtrack board marks to explore other paths safely. | 回溯時還原棋盤標記，安全探索其他路徑。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I first build Trie nodes from the words list. | 我先用 words 建立 Trie。 | Coding |
| For each board cell, I call DFS with Trie root. | 對每個棋盤格子用 Trie root 啟動 DFS。 | Coding |
| In DFS, I read current board character. | DFS 先讀當前棋盤字元。 | Coding |
| If character is visited marker or missing trie child, return. | 若是已訪問標記或 Trie 無子節點就返回。 | Coding |
| I move to the matched trie child node. | 我移動到匹配後的 Trie 子節點。 | Coding |
| If this trie node stores a complete word, push answer once. | 若此節點代表完整單字，就加入答案一次。 | Coding |
| I mark board cell as visited, explore four directions. | 把格子標記已訪問，探索四方向。 | Coding |
| After recursion, I restore original character for backtracking. | 遞迴後還原字元完成回溯。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run board with words oath, pea, eat, rain. | 我手跑 board 與單字 oath、pea、eat、rain。 | Dry-run |
| Trie contains all four words as prefix paths. | Trie 先含四個單字的前綴路徑。 | Dry-run |
| Starting at o in top-left, DFS can follow o-a-t-h and find oath. | 從左上角 o 出發可走 o-a-t-h 找到 oath。 | Dry-run |
| Starting near e in second row, DFS can find eat. | 從第二列 e 附近出發可找到 eat。 | Dry-run |
| For pea and rain, traversal hits trie dead-ends early and prunes. | pea 與 rain 會很快撞到 Trie 死路而被剪枝。 | Dry-run |
| Found words are collected without duplicates. | 找到的字會避免重複加入。 | Dry-run |
| Final result is eat and oath, matching expected output. | 最終結果為 eat、oath，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty board or empty words list. | 案例一：空棋盤或空單字列表。 | Edge test |
| Case two: one-cell board with one matching word. | 案例二：單格棋盤且剛好匹配一字。 | Edge test |
| Case three: many words sharing long common prefixes. | 案例三：大量共享長前綴的單字。 | Edge test |
| Case four: duplicated words in input should output once. | 案例四：輸入重複單字輸出應去重。 | Edge test |
| Case five: dense board causing many paths should rely on trie pruning. | 案例五：高分支棋盤需依賴 trie 剪枝。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Trie build is O(total word characters). | 建 Trie 是 O(所有單字字元總數)。 | Complexity |
| DFS is pruned by Trie; worst-case can still be exponential by path length. | DFS 受 Trie 剪枝，最壞仍可能隨路徑長度指數成長。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Building Trie takes O(sum of word lengths). | 建 Trie 時間為 O(單字長度總和)。 | Complexity |
| Board DFS starts from each cell, but dead branches are cut early via Trie. | DFS 從每格起跑，但 Trie 會提早剪掉死路。 | Complexity |
| In worst case with weak pruning, branch exploration can be large. | 若剪枝效果差，最壞分支探索仍可能很大。 | Complexity |
| Space includes Trie nodes, recursion stack, and output list. | 空間包含 Trie、遞迴堆疊與輸出集合。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me combine board DFS and trie traversal in one state. | 我先把棋盤 DFS 與 Trie 走訪整合成單一狀態。 | If stuck |
| Pruning should happen before exploring neighbors. | 剪枝必須在展開鄰居前先做。 | If stuck |
| If trie child is missing, return immediately. | 若 Trie 子節點不存在就立刻返回。 | If stuck |
| I might have forgotten to restore board cell on backtrack. | 我可能忘了回溯時還原棋盤格。 | If stuck |
| Let me restore the character after recursive calls. | 我在遞迴後補上字元還原。 | If stuck |
| I also nullify found-word marker to avoid duplicates. | 我也把已找到單字標記清掉避免重複。 | If stuck |
| I will rerun sample oath and eat now. | 我重跑 oath 與 eat 範例。 | If stuck |
| Both words are found exactly once. | 兩個字都正確且只找到一次。 | If stuck |
| Unmatched words are pruned quickly now. | 未匹配單字現在也能快速剪掉。 | If stuck |
| Great, DFS and pruning are now consistent. | 很好，DFS 與剪枝邏輯已一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed Word Search II using Trie plus backtracking DFS. | 我完成 Trie + 回溯 DFS 的 Word Search II。 | Wrap-up |
| The key optimization is prefix pruning against Trie structure. | 核心優化是利用 Trie 前綴結構剪枝。 | Wrap-up |
| This avoids re-running full search for each word separately. | 這避免了對每個字重跑完整搜尋。 | Wrap-up |
| Space is mainly Trie plus recursion stack. | 空間主要來自 Trie 與遞迴堆疊。 | Wrap-up |
| I can discuss trie-node deletion pruning if needed. | 若需要我可補充 trie 節點刪除剪枝。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find all dictionary words on board. | 在棋盤上找出所有字典單字。 | Cheat sheet |
| Use Trie for all words. | 對所有 words 建 Trie。 | Cheat sheet |
| Start DFS from every board cell. | 從每個格子啟動 DFS。 | Cheat sheet |
| Track trie node with board position. | 同步追蹤 trie 節點與棋盤位置。 | Cheat sheet |
| Missing trie edge => prune immediately. | Trie 無邊 => 立即剪枝。 | Cheat sheet |
| Mark board cell visited during path. | 路徑中標記格子為已訪問。 | Cheat sheet |
| Explore four directions only. | 只探索四方向。 | Cheat sheet |
| Restore cell on backtrack. | 回溯時還原格子。 | Cheat sheet |
| Trie terminal word => collect answer. | Trie 終點單字 => 收集答案。 | Cheat sheet |
| Deduplicate found words. | 對找到單字去重。 | Cheat sheet |
| Build Trie in O(total word length). | 建 Trie：O(總字長)。 | Cheat sheet |
| DFS is heavily pruning-dependent. | DFS 效率高度依賴剪枝。 | Cheat sheet |
| Worst-case branch growth can be large. | 最壞分支成長可能很大。 | Cheat sheet |
| Space includes Trie + recursion. | 空間含 Trie + 遞迴。 | Cheat sheet |
| Test empty board/words. | 測空棋盤或空字典。 | Cheat sheet |
| Test shared-prefix dictionary. | 測共享前綴字典。 | Cheat sheet |
| Common bug: forgetting backtrack restore. | 常見錯誤：忘記回溯還原。 | Cheat sheet |
| Common bug: duplicate result insertion. | 常見錯誤：重複加入結果。 | Cheat sheet |
| Mention optional trie-leaf pruning. | 可提可選的 trie 葉節點剪枝。 | Cheat sheet |
| End with prefix-pruning advantage. | 收尾強調前綴剪枝優勢。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Trie + board backtracking with pruning is preserved.
- No hallucinated constraints: ✅ Movement rules and dedup behavior align with source.
- Language simplicity: ✅ Short spoken lines for interview delivery.
