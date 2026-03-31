# 07 Valid Sudoku — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/07_Valid_Sudoku.md`

> Quick links: [Source Solution](../07_Valid_Sudoku.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We validate a 9x9 Sudoku board. | 我們要驗證 9x9 數獨盤面。 | Restatement |
| We only check current validity, not solvability. | 我們只查目前合法性，不解題。 | Restatement |
| Digits one to nine cannot repeat in row, column, box. | 1 到 9 不能在行、列、宮重複。 | Restatement |
| Dots mean empty cells and should be skipped. | 點號代表空格，應該跳過。 | Restatement |
| I will use one pass with fixed arrays. | 我會用一次遍歷加固定陣列。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume board size is always 9x9? | 可以假設盤面永遠是 9x9 嗎？ | Clarify |
| Do we only validate filled cells? | 我們只驗證已填入的格子嗎？ | Clarify |
| Should I return false on first conflict? | 發現第一個衝突就回傳 false 嗎？ | Clarify |
| Input chars are only dot or digits one to nine? | 輸入只會是 '.' 或 '1'~'9' 嗎？ | Clarify |
| Do you want bitmask variant discussion too? | 也需要我補充 bitmask 變體嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline checks rows, then columns, then boxes separately. | 基線是分別檢查行、列、九宮格。 | Approach |
| It works but repeats similar logic blocks. | 這能解，但會重複很多相似邏輯。 | Approach |
| We can do cleaner one-pass validation. | 我們可改成更乾淨的一次遍歷。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I maintain three trackers: rows, cols, and boxes. | 我維護三個追蹤器：rows、cols、boxes。 | Approach |
| For each digit, compute num and boxIndex. | 對每個數字，計算 num 與 boxIndex。 | Approach |
| If any tracker already marked, return false. | 任一追蹤器已標記就回傳 false。 | Approach |
| Otherwise mark all three trackers true. | 否則把三個追蹤器都標為 true。 | Approach |
| For fixed 9x9, runtime and memory are constant. | 固定 9x9 時，時間與空間皆為常數。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I declare bool rows, cols, boxes arrays. | 先宣告 bool 的 rows、cols、boxes 陣列。 | Coding |
| Then I loop r from zero to eight. | 然後 r 從 0 走到 8。 | Coding |
| Inside, I loop c from zero to eight. | 內層 c 從 0 走到 8。 | Coding |
| If board[r][c] is dot, I continue. | 若 board[r][c] 是點號，我直接 continue。 | Coding |
| I map digit to num by subtracting one char. | 我把字元減 '1' 映射成 num。 | Coding |
| boxIndex is r divided by three times three plus c divided by three. | boxIndex 是 r/3*3 + c/3。 | Coding |
| If rows or cols or boxes already true, return false. | 若 rows/cols/boxes 任何為 true 就回傳 false。 | Coding |
| Otherwise mark all three positions true. | 否則把三個位置都標成 true。 | Coding |
| After full scan, return true. | 全部掃完後回傳 true。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run one valid partial board. | 我手跑一個合法的部分盤面。 | Dry-run |
| At cell zero,zero we read digit five. | 在格子 0,0 讀到數字 5。 | Dry-run |
| Row zero, column zero, box zero are empty. | 第 0 行、第 0 列、第 0 宮都還沒標記。 | Dry-run |
| So we mark those three positions true. | 所以把三個位置都標成 true。 | Dry-run |
| Later if same digit appears in same row, conflict happens. | 之後若同列再出現同數字就衝突。 | Dry-run |
| We return false immediately on that conflict. | 出現衝突就立刻回傳 false。 | Dry-run |
| If no conflict after scan, return true. | 若掃完都無衝突就回傳 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: duplicate in one row should be false. | 案例一：同一列重複應為 false。 | Edge test |
| Case two: duplicate in one column should be false. | 案例二：同一欄重複應為 false。 | Edge test |
| Case three: duplicate in one 3x3 box should be false. | 案例三：同一九宮格重複應為 false。 | Edge test |
| Case four: all dots board should be true. | 案例四：全點號盤面應為 true。 | Edge test |
| Case five: valid mixed board should be true. | 案例五：合法混合盤面應為 true。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For fixed 9x9, time is O(1). | 固定 9x9 時，時間是 O(1)。 | Complexity |
| For fixed 9x9, space is O(1). | 固定 9x9 時，空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We visit 81 cells at most. | 我們最多只會看 81 個格子。 | Complexity |
| Each visit does constant checks and writes. | 每次造訪都只做常數次檢查與寫入。 | Complexity |
| So fixed-board runtime is constant. | 所以固定盤面的時間是常數。 | Complexity |
| Trackers are fixed-size arrays, so constant space. | 追蹤器是固定大小陣列，所以空間常數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me recheck box index formula. | 我先重檢 box 索引公式。 | If stuck |
| I can start with row and column checks. | 我可先從行列檢查講起。 | If stuck |
| Then I add 3x3 box check. | 然後補上 3x3 宮格檢查。 | If stuck |
| I forgot one index conversion. | 我一時忘了索引轉換。 | If stuck |
| The overall logic still holds. | 整體邏輯仍成立。 | If stuck |
| Thanks, I will correct this line. | 謝謝，我會修正這行。 | If stuck |
| I found the conflict condition bug. | 我找到衝突條件 bug。 | If stuck |
| Let me rerun one board quickly. | 我快速重跑一個盤面。 | If stuck |
| Now results are correct. | 現在結果正確了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| It validates rows, columns, and boxes in one scan. | 它在一次掃描內驗證行、列、宮。 | Wrap-up |
| It returns false immediately on conflict. | 一旦衝突就立即回傳 false。 | Wrap-up |
| On fixed 9x9 board, time and space are O(1). | 固定 9x9 下時間與空間都是 O(1)。 | Wrap-up |
| I can also discuss bitmask optimization. | 我也可以補充 bitmask 優化。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate validation-only goal. | 重述僅驗證合法性的目標。 | Cheat sheet |
| Skip dots as empty cells. | 跳過點號空格。 | Cheat sheet |
| Track rows, columns, and boxes. | 追蹤行、列、九宮格。 | Cheat sheet |
| Convert digit char to index 0..8. | 把字元數字轉索引 0..8。 | Cheat sheet |
| Compute box index with r/3*3+c/3. | 用 r/3*3+c/3 算 box 索引。 | Cheat sheet |
| Check conflict before marking. | 先檢查衝突再標記。 | Cheat sheet |
| Conflict means immediate false. | 發生衝突就立刻 false。 | Cheat sheet |
| No conflict after scan means true. | 掃完無衝突就是 true。 | Cheat sheet |
| Test duplicate in one row. | 測試同列重複。 | Cheat sheet |
| Test duplicate in one column. | 測試同欄重複。 | Cheat sheet |
| Test duplicate in one box. | 測試同宮重複。 | Cheat sheet |
| Test all-dots board. | 測試全點號盤面。 | Cheat sheet |
| Mention fixed-size complexity. | 提到固定尺寸複雜度。 | Cheat sheet |
| Fixed-board time O(1). | 固定盤面時間 O(1)。 | Cheat sheet |
| Fixed-board space O(1). | 固定盤面空間 O(1)。 | Cheat sheet |
| If generalized to N, use O(N^2). | 若泛化到 N，則是 O(N^2)。 | Cheat sheet |
| Keep code narration by loops. | 依迴圈順序口述程式。 | Cheat sheet |
| If stuck, recheck box formula. | 卡住時重檢 box 公式。 | Cheat sheet |
| End with early-return benefit. | 以早回傳優點收尾。 | Cheat sheet |
| Offer bitmask follow-up. | 提供 bitmask 延伸討論。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ One-pass row/col/box tracking is preserved.
- No hallucinated constraints: ✅ Ambiguous requirements are asked in clarification lines.
- Language simplicity: ✅ Short spoken lines for interview delivery.
