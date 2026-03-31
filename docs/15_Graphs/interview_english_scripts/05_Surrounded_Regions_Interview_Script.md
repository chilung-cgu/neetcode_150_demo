# 05 Surrounded Regions — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/05_Surrounded_Regions.md`

> Quick links: [Source Solution](../05_Surrounded_Regions.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate surrounded regions. | 我先重述 Surrounded Regions。 | Restatement |
| We have a board with X and O. | 題目給一個只含 X 與 O 的棋盤。 | Restatement |
| Any O fully surrounded by X should be flipped to X. | 被 X 完整包圍的 O 要翻成 X。 | Restatement |
| Border-connected O cells should stay O. | 與邊界連通的 O 要保留。 | Restatement |
| We modify the board in place. | 題目要求原地修改棋盤。 | Restatement |
| I will mark safe border regions first, then flip others. | 我會先標安全邊界區，再翻其餘格子。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is board guaranteed non-empty? | board 是否保證非空？ | Clarify |
| Is connectivity four directions only? | 連通是否只算四方向？ | Clarify |
| Should diagonal O cells be treated as disconnected? | 對角 O 是否視為不連通？ | Clarify |
| Can I use temporary marker like T for safe O? | 可以用暫存標記例如 T 嗎？ | Clarify |
| Should function return void and mutate input? | 函式是否回 void 並直接改輸入？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks every O to see if it can reach border. | 暴力法對每個 O 都檢查能否連到邊界。 | Approach |
| That repeats many searches across same regions. | 這會在相同區域重複搜尋。 | Approach |
| We need one global border-driven traversal instead. | 我們需要一次全域邊界驅動遍歷。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Reverse viewpoint: first protect O connected to border. | 反向思考：先保護連到邊界的 O。 | Approach |
| Run DFS from all border O and mark them as T. | 從所有邊界 O 做 DFS，標成 T。 | Approach |
| After marking, all remaining O are truly surrounded. | 標記後剩下的 O 就是真正被包圍。 | Approach |
| Flip remaining O to X. | 把剩餘 O 翻成 X。 | Approach |
| Convert T back to O to restore safe regions. | 最後把 T 還原為 O。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I get rows and cols from board. | 我先取得 rows 與 cols。 | Coding |
| I scan first and last rows for border O. | 我掃第一列與最後一列的邊界 O。 | Coding |
| I run DFS on each border O to mark T. | 對每個邊界 O 執行 DFS 標記 T。 | Coding |
| I scan first and last columns similarly. | 第一欄與最後一欄也同樣處理。 | Coding |
| DFS stops on out of bounds or non-O cell. | DFS 遇越界或非 O 就停止。 | Coding |
| DFS marks O as T and expands four directions. | DFS 把 O 標成 T 並向四方向擴展。 | Coding |
| After border marking, I scan whole board. | 邊界標記後我掃整張棋盤。 | Coding |
| If cell is O, flip to X. | 若格子是 O，就翻成 X。 | Coding |
| If cell is T, restore to O. | 若格子是 T，就還原成 O。 | Coding |
| Done, board now satisfies surrounded rule. | 完成後棋盤就符合包圍規則。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the classic four-by-four sample. | 我手跑經典 4x4 範例。 | Dry-run |
| Border scan finds only the O at bottom row second column. | 邊界掃描只找到底列第二欄那個 O。 | Dry-run |
| DFS marks that border-connected region as T. | DFS 把該邊界連通區標為 T。 | Dry-run |
| Inner O cells not connected to border remain O for now. | 內部未連邊界的 O 暫時保持 O。 | Dry-run |
| Full scan flips those inner O cells to X. | 全掃描時把這些內部 O 翻成 X。 | Dry-run |
| T cells are restored back to O. | T 格子最後還原成 O。 | Dry-run |
| Final board matches expected output. | 最終棋盤與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: all X board stays unchanged. | 案例一：全 X 棋盤不變。 | Edge test |
| Case two: all O board keeps border-connected region, often all remain O. | 案例二：全 O 棋盤保留邊界連通區，常全部保留。 | Edge test |
| Case three: single row board should never flip due to border contact. | 案例三：單列棋盤因都接邊界，通常不翻。 | Edge test |
| Case four: single column board same behavior. | 案例四：單欄棋盤同理。 | Edge test |
| Case five: isolated center O inside X should flip. | 案例五：被 X 包圍的中心 O 要翻。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(rows times cols). | 時間複雜度是 O(rows*cols)。 | Complexity |
| Space complexity is O(rows times cols) worst case recursion stack. | 空間最壞是 O(rows*cols) 的遞迴堆疊。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Border DFS visits each cell at most once for marking. | 邊界 DFS 對每格最多標記一次。 | Complexity |
| Final board conversion scan is linear in cell count. | 最後轉換掃描對格數是線性。 | Complexity |
| Combined runtime is O(mn). | 合併後總時間是 O(mn)。 | Complexity |
| Recursive DFS stack can reach O(mn) in worst connected case. | 最壞連通情況下遞迴堆疊可達 O(mn)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me avoid checking each O independently. | 我避免逐格獨立檢查每個 O。 | If stuck |
| Border-connected O cells are the only safe ones. | 只有邊界連通 O 是安全區。 | If stuck |
| I should mark safe cells first, not surrounded cells first. | 我應先標安全格，不是先找被包圍格。 | If stuck |
| Temporary mark T helps separate two groups. | 暫存標記 T 可清楚分群。 | If stuck |
| DFS from borders captures all safe O components. | 從邊界 DFS 可抓出全部安全 O 分量。 | If stuck |
| Then flip remaining O to X confidently. | 然後可放心把剩餘 O 翻成 X。 | If stuck |
| Restore T back to O at the end. | 最後把 T 還原成 O。 | If stuck |
| Let me test with one center O example. | 我用中心單一 O 例子快速驗證。 | If stuck |
| It should be flipped because no border path. | 它應被翻轉，因為無邊界路徑。 | If stuck |
| Great, logic is now clear and robust. | 很好，邏輯已清楚且穩健。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it using border-first DFS marking. | 我用邊界優先 DFS 標記法解題。 | Wrap-up |
| Border-connected O are preserved as safe cells. | 邊界連通 O 被保留為安全格。 | Wrap-up |
| Unmarked O are surrounded and flipped to X. | 未標記 O 即被包圍，會翻成 X。 | Wrap-up |
| Complexity is O(mn) time and O(mn) worst-case stack space. | 複雜度是 O(mn) 時間與 O(mn) 最壞堆疊空間。 | Wrap-up |
| This is the standard reverse-thinking region-capture pattern. | 這是區域捕獲題的標準反向思考模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: flip surrounded O to X. | 目標：把被包圍 O 翻成 X。 | Cheat sheet |
| Border-connected O must stay O. | 邊界連通 O 必須保留。 | Cheat sheet |
| Reverse approach: mark safe first. | 反向法：先標安全區。 | Cheat sheet |
| DFS from top and bottom borders. | 從上、下邊界做 DFS。 | Cheat sheet |
| DFS from left and right borders. | 從左、右邊界做 DFS。 | Cheat sheet |
| Only expand from O cells. | 只從 O 格擴展。 | Cheat sheet |
| Mark safe O as T. | 安全 O 標成 T。 | Cheat sheet |
| Scan entire board afterward. | 之後掃描整張棋盤。 | Cheat sheet |
| O -> X for surrounded region. | O -> X 代表被包圍區。 | Cheat sheet |
| T -> O restore safe region. | T -> O 還原安全區。 | Cheat sheet |
| Do operation in place. | 原地修改。 | Cheat sheet |
| Diagonal does not connect. | 對角不連通。 | Cheat sheet |
| All X stays same. | 全 X 不變。 | Cheat sheet |
| Single row often unchanged. | 單列通常不變。 | Cheat sheet |
| Single column often unchanged. | 單欄通常不變。 | Cheat sheet |
| Time O(mn). | 時間 O(mn)。 | Cheat sheet |
| Stack worst O(mn). | 堆疊最壞 O(mn)。 | Cheat sheet |
| Common bug: forgetting restore T. | 常見錯誤：忘記還原 T。 | Cheat sheet |
| Common bug: starting DFS from every O. | 常見錯誤：從每個 O 啟 DFS。 | Cheat sheet |
| Explain safe-versus-captured clearly. | 清楚說明安全區與被捕獲區。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Border DFS mark-then-flip strategy preserved.
- No hallucinated constraints: ✅ In-place mutation and four-direction logic kept.
- Language simplicity: ✅ Practical interview-style wording.
