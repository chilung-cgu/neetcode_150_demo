# 04 Generate Parentheses — Interview English Script (C++)

> Source aligned with: `docs/04_Stack/04_Generate_Parentheses.md`

> Quick links: [Source Solution](../04_Generate_Parentheses.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| Input n means n pairs of parentheses. | 輸入 n 代表 n 對括號。 | Restatement |
| We must generate all well-formed combinations. | 我們要產生所有合法括號組合。 | Restatement |
| Order of output can be any valid order. | 輸出順序可為任意合法順序。 | Restatement |
| I will use backtracking with pruning rules. | 我會用回溯搭配剪枝規則。 | Restatement |
| The state is openCount and closeCount. | 狀態是 openCount 與 closeCount。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume n is at least one? | 可以假設 n 至少為 1 嗎？ | Clarify |
| Do we return all combinations as strings list? | 是否回傳字串陣列包含所有組合？ | Clarify |
| Is any ordering of valid results acceptable? | 合法結果的順序是否不限？ | Clarify |
| Should we avoid generating invalid prefixes? | 是否要避免產生非法前綴？ | Clarify |
| Can I discuss Catalan-count complexity briefly? | 我可簡述 Catalan 數量複雜度嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline generates all binary strings of length two n. | 基線是產生長度 2n 的所有二元字串。 | Approach |
| Then validate each string as parentheses sequence. | 再逐一驗證每個字串是否合法。 | Approach |
| This explores many invalid paths and is inefficient. | 這會探索大量無效路徑，效率差。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Add opening parenthesis only when openCount < n. | 只有 openCount<n 才能加左括號。 | Approach |
| Add closing parenthesis only when closeCount < openCount. | 只有 closeCount<openCount 才能加右括號。 | Approach |
| This guarantees every prefix remains valid. | 這可保證每個前綴都合法。 | Approach |
| When length reaches 2n, record current string. | 長度到 2n 時就記錄結果。 | Approach |
| Backtracking explores only feasible branches. | 回溯只探索可行分支。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I define dfs with openCount, closeCount, and path. | 先定義 dfs，帶 openCount、closeCount、path。 | Coding |
| Base case is path length equals 2 times n. | 基底是 path 長度等於 2n。 | Coding |
| On base case, append current path to result. | 到基底就把 path 加入結果。 | Coding |
| If openCount is less than n, choose open bracket. | 若 openCount<n，就可選左括號。 | Coding |
| Recurse, then undo choice by pop back. | 遞迴後要 pop back 還原。 | Coding |
| If closeCount is less than openCount, choose close bracket. | 若 closeCount<openCount，就可選右括號。 | Coding |
| Recurse again and backtrack similarly. | 再遞迴並以同樣方式回溯。 | Coding |
| Return final result list after DFS completes. | DFS 完成後回傳結果列表。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n equals 3. | 我手跑 n=3。 | Dry-run |
| Start with empty path and counts zero zero. | 起始 path 空，計數是 0 與 0。 | Dry-run |
| Add open until reaching three opens. | 先加左括號直到三個。 | Dry-run |
| Then add closes where rule allows, forming ((())). | 再依規則加右括號，形成 ((()))。 | Dry-run |
| Backtrack to explore sibling branches. | 回溯後探索同層其他分支。 | Dry-run |
| This produces (()()), (())(), ()(()), and ()()(). | 會再得到 (()())、(())()、()(())、()()()。 | Dry-run |
| Total five valid strings are returned. | 最終回傳五個合法字串。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals one returns only (). | 案例一：n=1 僅回傳 ()。 | Edge test |
| Case two: n equals two returns two combinations. | 案例二：n=2 回傳兩種組合。 | Edge test |
| Case three: check no duplicates in output. | 案例三：確認輸出無重複。 | Edge test |
| Case four: verify every result length is 2n. | 案例四：確認每筆長度皆為 2n。 | Edge test |
| Case five: larger n still keeps prefix validity. | 案例五：較大 n 仍保持前綴合法。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is proportional to number of valid outputs. | 時間與合法輸出數量成正比。 | Complexity |
| Auxiliary space is O(n) for recursion path depth. | 輔助空間是 O(n)，來自遞迴深度。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Valid count is Catalan number Cn. | 合法數量是 Catalan 數 Cn。 | Complexity |
| Approximate growth is O(4^n / sqrt(n)). | 近似成長為 O(4^n/sqrt(n))。 | Complexity |
| We cannot do better than output size lower bound. | 由輸出下界限制，無法優於輸出量。 | Complexity |
| Recursion stack and path buffer need O(n). | 遞迴堆疊與 path 緩衝需要 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate pruning rules first. | 我先重述剪枝規則。 | If stuck |
| closeCount must never exceed openCount. | closeCount 絕不能超過 openCount。 | If stuck |
| openCount must not exceed n. | openCount 不能超過 n。 | If stuck |
| I can explain brute force briefly. | 我可先簡述暴力法。 | If stuck |
| Then I switch back to pruned DFS. | 再切回有剪枝的 DFS。 | If stuck |
| Thanks, I found missing backtrack pop. | 謝謝，我找到漏掉的回溯 pop。 | If stuck |
| Let me rerun n equals three quickly. | 我快速重跑 n=3。 | If stuck |
| Now all outputs are valid and complete. | 現在輸出完整且都合法。 | If stuck |
| The recursion flow is consistent now. | 現在遞迴流程一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time follows Catalan output growth. | 時間複雜度遵循 Catalan 成長。 | Wrap-up |
| Auxiliary space is O(n). | 輔助空間是 O(n)。 | Wrap-up |
| I can discuss iterative stack generation if needed. | 若需要我可補充迭代 stack 生成法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate generate-parentheses goal. | 重述產生合法括號目標。 | Cheat sheet |
| Mention n pairs requirement. | 提到 n 對括號限制。 | Cheat sheet |
| Brute force builds all 2^(2n) strings. | 暴力法生成 2^(2n) 字串。 | Cheat sheet |
| Better approach is backtracking. | 更好方法是回溯。 | Cheat sheet |
| Track openCount and closeCount. | 追蹤 openCount 與 closeCount。 | Cheat sheet |
| Add open when openCount < n. | openCount<n 時可加左括號。 | Cheat sheet |
| Add close when closeCount < openCount. | closeCount<openCount 時可加右括號。 | Cheat sheet |
| This keeps prefix always valid. | 這可保證前綴永遠合法。 | Cheat sheet |
| Record when path length is 2n. | path 長度到 2n 就記錄。 | Cheat sheet |
| Backtrack with pop after recursion. | 遞迴後記得 pop 回溯。 | Cheat sheet |
| Dry-run n=3. | 手跑 n=3。 | Cheat sheet |
| Verify total five outputs. | 驗證共有五個輸出。 | Cheat sheet |
| Test n=1 base case. | 測 n=1 基礎案例。 | Cheat sheet |
| Check output lengths all equal 2n. | 檢查輸出長度皆為 2n。 | Cheat sheet |
| Mention Catalan growth. | 提到 Catalan 成長。 | Cheat sheet |
| Report O(n) auxiliary space. | 報告 O(n) 輔助空間。 | Cheat sheet |
| No invalid strings are generated. | 不會生成非法字串。 | Cheat sheet |
| If stuck, recheck pruning rules. | 卡住時重檢剪枝規則。 | Cheat sheet |
| Re-run sample after fixes. | 修正後重跑範例。 | Cheat sheet |
| End with concise summary. | 以精簡總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Backtracking with open/close pruning is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
