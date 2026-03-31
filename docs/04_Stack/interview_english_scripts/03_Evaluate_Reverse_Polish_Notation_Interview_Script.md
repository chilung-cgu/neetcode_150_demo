# 03 Evaluate Reverse Polish Notation — Interview English Script (C++)

> Source aligned with: `docs/04_Stack/03_Evaluate_Reverse_Polish_Notation.md`

> Quick links: [Source Solution](../03_Evaluate_Reverse_Polish_Notation.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| Input is an RPN expression token list. | 輸入是一個 RPN token 串列。 | Restatement |
| Operators appear after their operands. | 運算子會出現在運算元之後。 | Restatement |
| We must evaluate and return final integer result. | 我們要計算並回傳最終整數結果。 | Restatement |
| I will use stack to simulate evaluation order. | 我會用 stack 模擬計算順序。 | Restatement |
| I will pay attention to operand order for minus and divide. | 我會注意減法與除法的操作元順序。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume expression is always valid as stated? | 可否假設題目保證表達式合法？ | Clarify |
| Is integer division truncated toward zero? | 整數除法是否朝零截斷？ | Clarify |
| Are all intermediate values within 32-bit int range? | 中間值是否都在 32-bit 範圍內？ | Clarify |
| Do tokens include negative integer literals? | token 會包含負整數字面值嗎？ | Clarify |
| Should I return a single integer result only? | 是否只需回傳單一整數結果？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline idea is convert RPN back to infix and parse. | 基線想法是先轉回中序再解析。 | Approach |
| That adds unnecessary parsing complexity. | 這會增加不必要的解析複雜度。 | Approach |
| Direct stack simulation is cleaner and faster. | 直接用 stack 模擬會更乾淨更快。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Scan tokens left to right once. | token 由左到右掃描一次。 | Approach |
| Push numbers onto stack. | 數字 token 直接 push 進 stack。 | Approach |
| On operator, pop right operand then left operand. | 遇運算子先 pop 右操作元，再 pop 左操作元。 | Approach |
| Compute left op right and push result back. | 計算 left op right，再把結果 push 回去。 | Approach |
| After scan, stack top is final answer. | 掃描完成後，stack top 就是最終答案。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize an empty integer stack. | 先初始化空的整數 stack。 | Coding |
| Then I iterate each token in order. | 然後依序處理每個 token。 | Coding |
| If token is number, parse and push it. | 若 token 是數字，就轉型後 push。 | Coding |
| If token is operator, pop two operands. | 若 token 是運算子，就 pop 兩個操作元。 | Coding |
| Remember first pop is right operand. | 記住第一次 pop 出來是右操作元。 | Coding |
| Compute left plus/minus/multiply/divide right. | 計算 left 與 right 的對應運算。 | Coding |
| Push computed result back to stack. | 把計算結果 push 回 stack。 | Coding |
| Return stack top after all tokens. | 處理完全部 token 後回傳 stack top。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run tokens 2, 1, plus, 3, multiply. | 我手跑 token：2、1、+、3、*。 | Dry-run |
| Push 2, then push 1. | 先 push 2，再 push 1。 | Dry-run |
| On plus, pop 1 and 2, compute 2+1=3, push 3. | 遇 + 時 pop 1 與 2，算 2+1=3，再 push 3。 | Dry-run |
| Next token 3 is pushed. | 下一個 token 3 直接 push。 | Dry-run |
| On multiply, pop 3 and 3, compute 3*3=9. | 遇 * 時 pop 3 與 3，算 3*3=9。 | Dry-run |
| Push 9, and stack top is final result. | push 9，stack top 即最終結果。 | Dry-run |
| Final answer is 9. | 最終答案是 9。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single number token only. | 案例一：只有單一數字 token。 | Edge test |
| Case two: negative numbers with division. | 案例二：含負數與除法。 | Edge test |
| Case three: subtraction order sensitivity. | 案例三：減法順序敏感案例。 | Edge test |
| Case four: long expression chain. | 案例四：較長的運算鏈。 | Edge test |
| Case five: mixed all four operators. | 案例五：四種運算子混合。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(n) worst case. | 最差額外空間是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each token is processed exactly once. | 每個 token 只會被處理一次。 | Complexity |
| Number token does one push. | 數字 token 只做一次 push。 | Complexity |
| Operator token does two pops and one push. | 運算子 token 做兩次 pop 與一次 push。 | Complexity |
| Stack may hold O(n) values in worst layout. | 最差情況下 stack 可能保留 O(n) 值。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate RPN pop order. | 我先重述 RPN 的 pop 順序。 | If stuck |
| First pop is right, second pop is left. | 第一次 pop 是右值，第二次是左值。 | If stuck |
| This matters for minus and division. | 這對減法與除法特別重要。 | If stuck |
| I can explain stack simulation again. | 我可以再說一次 stack 模擬。 | If stuck |
| Then I will rerun a subtraction sample. | 然後我會重跑減法範例。 | If stuck |
| Thanks, I found operand-order bug. | 謝謝，我找到操作元順序 bug。 | If stuck |
| Let me rerun one divide sample. | 我再跑一次除法範例。 | If stuck |
| Now truncation and order are correct. | 現在截斷規則與順序都正確。 | If stuck |
| Final result is consistent now. | 最終結果現在一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Space is O(n) worst case. | 最差空間是 O(n)。 | Wrap-up |
| I can discuss infix conversion follow-up if needed. | 若需要我可補充轉中序延伸。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate RPN evaluation goal. | 重述 RPN 求值目標。 | Cheat sheet |
| Mention operators come after operands. | 提到運算子在運算元之後。 | Cheat sheet |
| Use integer stack. | 使用整數 stack。 | Cheat sheet |
| Number token means push. | 數字 token 就 push。 | Cheat sheet |
| Operator token means pop two operands. | 運算子 token 就 pop 兩個值。 | Cheat sheet |
| First pop is right operand. | 第一次 pop 是右操作元。 | Cheat sheet |
| Compute left op right. | 計算 left op right。 | Cheat sheet |
| Push result back. | 把結果 push 回去。 | Cheat sheet |
| Repeat until tokens end. | 重複直到 token 結束。 | Cheat sheet |
| Return stack top. | 回傳 stack top。 | Cheat sheet |
| Dry-run 2 1 + 3 *. | 手跑 2 1 + 3 *。 | Cheat sheet |
| Verify output is 9. | 驗證輸出為 9。 | Cheat sheet |
| Test subtraction order case. | 測減法順序案例。 | Cheat sheet |
| Test negative division case. | 測負數除法案例。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(n) worst-case stack space. | 報告 O(n) 最差 stack 空間。 | Cheat sheet |
| Mention truncate-toward-zero rule. | 提到朝零截斷規則。 | Cheat sheet |
| If stuck, recheck pop order. | 卡住時重檢 pop 順序。 | Cheat sheet |
| Re-run sample after fixes. | 修正後重跑範例。 | Cheat sheet |
| End with concise numeric result. | 以精簡數值結果收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Stack-based operand-order evaluation is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
