# 09 N-Queens — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/09_N_Queens.md`

> Quick links: [Source Solution](../09_N_Queens.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the N-Queens problem. | 我先重述 N-Queens。 | Restatement |
| We need to place n queens on an n by n board. | 要在 n*n 棋盤放 n 個皇后。 | Restatement |
| No two queens can attack each other. | 任兩皇后都不能互相攻擊。 | Restatement |
| That means no shared column or diagonal conflicts. | 也就是不能同欄或同對角線。 | Restatement |
| We must return all valid board configurations. | 要回傳所有合法棋盤配置。 | Restatement |
| I will place queens row by row with backtracking. | 我會逐行放皇后並用回溯搜尋。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do we return actual board strings, not just number of solutions? | 是否要回傳棋盤字串，而非只回數量？ | Clarify |
| Is one queen per row guaranteed by our construction? | 我們可否用每行放一顆的建構方式？ | Clarify |
| Should we optimize conflict check to O(1) with sets or arrays? | 衝突檢查是否建議 O(1) 集合法？ | Clarify |
| Is any order of valid boards acceptable? | 合法棋盤輸出順序是否可任意？ | Clarify |
| May I use diagonal indices r plus c and r minus c with offset? | 可用 r+c 與 r-c+offset 當對角線索引嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force chooses any n cells and checks all conflicts. | 暴力法任選 n 格再檢查衝突。 | Approach |
| Search space is huge and quickly impractical. | 搜尋空間巨大，很快不可行。 | Approach |
| We need constrained row-wise backtracking instead. | 需要改用受限的逐行回溯。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Place exactly one queen per row recursively. | 遞迴時每行只放一顆皇后。 | Approach |
| Track occupied columns with a boolean set or array. | 用布林集合追蹤已用欄位。 | Approach |
| Track positive diagonal by r plus c. | 用 r+c 追蹤正斜對角線。 | Approach |
| Track negative diagonal by r minus c plus n offset. | 用 r-c+n 追蹤反斜對角線。 | Approach |
| If position is safe, place queen, recurse, then backtrack. | 位置安全就放置、遞迴、再回溯。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize board with dots and empty occupancy trackers. | 我先用點初始化棋盤與佔用追蹤。 | Coding |
| I call dfs starting from row zero. | 我從第 0 列呼叫 dfs。 | Coding |
| Base case is row equals n, then record board snapshot. | 基底是 row==n，記錄棋盤快照。 | Coding |
| For each column c in current row, I test conflicts. | 目前列中對每個欄 c 檢查衝突。 | Coding |
| Conflict means used column or used diagonal index. | 衝突代表欄位或對角線已被占用。 | Coding |
| If safe, mark trackers and place Q on board. | 若安全就標記追蹤並放 Q。 | Coding |
| Recurse to next row, then undo all marks and board cell. | 遞迴到下一列後還原所有標記與棋盤。 | Coding |
| This ensures complete search with clean state restoration. | 這可完整搜尋且保持狀態乾淨。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n equals four briefly. | 我簡短手跑 n=4。 | Dry-run |
| Row zero choose column one as first queen. | 第 0 列先選第 1 欄。 | Dry-run |
| Row one safe choice becomes column three. | 第 1 列安全選擇是第 3 欄。 | Dry-run |
| Row two then chooses column zero. | 第 2 列接著選第 0 欄。 | Dry-run |
| Row three can place at column two and complete one board. | 第 3 列可放第 2 欄完成一解。 | Dry-run |
| Backtracking explores another branch to get second board. | 回溯後探索另一分支得到第二解。 | Dry-run |
| Final count for n four is two configurations. | n=4 最終共有兩種配置。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals one should return single queen board. | 案例一：n=1 應回單皇后棋盤。 | Edge test |
| Case two: n equals two should return no solution. | 案例二：n=2 應無解。 | Edge test |
| Case three: n equals three should return no solution. | 案例三：n=3 也應無解。 | Edge test |
| Case four: n equals four should return exactly two solutions. | 案例四：n=4 應回兩組解。 | Edge test |
| Case five: verify each returned board has one queen per row. | 案例五：確認每個解每列只有一顆皇后。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Worst-case runtime is often described as O(n factorial). | 最壞時間常描述為 O(n!)。 | Complexity |
| Recursion depth is O(n), excluding board output storage. | 不含輸出時遞迴深度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We place one queen per row, trying available columns recursively. | 我們逐行放皇后並遞迴嘗試可行欄位。 | Complexity |
| Branching shrinks with constraints, but worst upper bound is near n factorial. | 分支因約束縮小，但最壞上界近似 n!。 | Complexity |
| O(1) conflict check from trackers is essential for speed. | 以追蹤器做 O(1) 衝突檢查是關鍵。 | Complexity |
| Stack depth is n, while storing all boards dominates memory. | 堆疊深度 n，而儲存所有棋盤主導記憶體。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me enforce one queen per row first. | 我先強制每列只放一顆皇后。 | If stuck |
| Then I only need to choose a column each row. | 這樣每列只需選欄位。 | If stuck |
| Conflict checks should be O(1), not scanning whole board. | 衝突檢查應 O(1)，不要掃全盤。 | If stuck |
| I will track columns and two diagonal sets. | 我會追蹤欄位與兩種對角線集合。 | If stuck |
| Positive diagonal key is r plus c. | 正斜線 key 是 r+c。 | If stuck |
| Negative diagonal key is r minus c plus offset. | 反斜線 key 是 r-c+偏移。 | If stuck |
| Place, recurse, and always undo on return. | 放置、遞迴、回來一定還原。 | If stuck |
| Let me sanity check with n equals four. | 我用 n=4 做快速 sanity check。 | If stuck |
| I can produce exactly two boards, so flow is right. | 可產出兩組解，流程正確。 | If stuck |
| Great, backtracking invariants are stable now. | 很好，回溯不變量已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved N-Queens with row-based backtracking. | 我以逐行回溯解出 N-Queens。 | Wrap-up |
| O(1) conflict checks use column and diagonal trackers. | O(1) 衝突檢查靠欄位與對角線追蹤。 | Wrap-up |
| Each valid full placement is captured as one board output. | 每個完整合法放置都記錄為一張棋盤。 | Wrap-up |
| Backtracking restore keeps search state correct. | 回溯還原確保搜尋狀態正確。 | Wrap-up |
| I can also derive the counting-only N-Queens II variant. | 我也可延伸到只計數的 N-Queens II。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: constrained board backtracking. | 題型：受限棋盤回溯。 | Cheat sheet |
| Place n queens on n by n board. | 在 n*n 棋盤放 n 皇后。 | Cheat sheet |
| No same column conflicts. | 不可同欄衝突。 | Cheat sheet |
| No diagonal conflicts. | 不可對角線衝突。 | Cheat sheet |
| Place one queen per row. | 每列放一顆皇后。 | Cheat sheet |
| DFS state: current row. | DFS 狀態：當前列。 | Cheat sheet |
| Track used columns. | 追蹤已用欄位。 | Cheat sheet |
| Track pos diagonal r+c. | 追蹤正斜線 r+c。 | Cheat sheet |
| Track neg diagonal r-c+offset. | 追蹤反斜線 r-c+偏移。 | Cheat sheet |
| If row == n, record board. | row==n 時記錄棋盤。 | Cheat sheet |
| For each column test safety. | 對每欄檢查安全性。 | Cheat sheet |
| If safe, place queen and mark sets. | 安全就放皇后並標記集合。 | Cheat sheet |
| Recurse to next row. | 遞迴到下一列。 | Cheat sheet |
| Undo placement and marks afterward. | 回來後還原放置與標記。 | Cheat sheet |
| n=1 has one solution. | n=1 有一解。 | Cheat sheet |
| n=2 and n=3 have no solution. | n=2、n=3 無解。 | Cheat sheet |
| n=4 has two solutions. | n=4 有兩解。 | Cheat sheet |
| Worst runtime near O(n!). | 最壞時間近 O(n!)。 | Cheat sheet |
| Stack depth O(n). | 堆疊深度 O(n)。 | Cheat sheet |
| Output storage can be large. | 輸出儲存可能很大。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Row-wise DFS with column/diagonal trackers preserved.
- No hallucinated constraints: ✅ Uses exact N-Queens attack rules and output form.
- Language simplicity: ✅ Concise spoken interview flow with concrete invariants.
