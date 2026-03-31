# 11 Validate Binary Search Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/11_Validate_BST.md`

> Quick links: [Source Solution](../11_Validate_BST.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the validate-BST problem. | 我先重述驗證 BST 題目。 | Restatement |
| We need to check whether a binary tree satisfies strict BST rules. | 要判斷二元樹是否符合嚴格 BST 規則。 | Restatement |
| Left subtree values must be smaller than node value. | 左子樹值都必須小於當前節點。 | Restatement |
| Right subtree values must be larger than node value. | 右子樹值都必須大於當前節點。 | Restatement |
| This condition must hold for every subtree globally, not only parent-child. | 這是全域條件，不只看父子關係。 | Restatement |
| I will use top-down DFS with valid value range. | 我會用 top-down DFS 帶範圍限制。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are duplicate values considered invalid for BST here? | 此題重複值是否視為無效 BST？ | Clarify |
| Should inequalities be strict, not less-or-equal? | 比較是否必須嚴格不等式？ | Clarify |
| Can node values reach INT_MIN and INT_MAX boundaries? | 節點值會到 INT_MIN/INT_MAX 邊界嗎？ | Clarify |
| Is recursive range-check solution preferred? | 是否偏好遞迴範圍檢查解法？ | Clarify |
| Should I mention in-order monotonic alternative too? | 要補充中序遞增檢查替代法嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks each node by scanning subtree min and max repeatedly. | 暴力法對每節點重複掃描子樹最小與最大值。 | Approach |
| That causes repeated traversal across overlapping subtrees. | 這會在重疊子樹上反覆遍歷。 | Approach |
| Worst-case complexity becomes O(n^2). | 最壞情況複雜度變成 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use DFS with dynamic range (minVal, maxVal) for each node. | 每節點用動態範圍 (minVal,maxVal) 做 DFS。 | Approach |
| Root starts with range negative infinity to positive infinity. | root 初始範圍是負無限到正無限。 | Approach |
| Left child narrows upper bound to parent value. | 左子樹把上界收斂到父節點值。 | Approach |
| Right child narrows lower bound to parent value. | 右子樹把下界收斂到父節點值。 | Approach |
| Any value outside range fails immediately in O(n) total time. | 只要超出範圍就立刻失敗，總時間 O(n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I call validate helper with root and long-range bounds. | 我用長整數邊界呼叫 validate helper。 | Coding |
| Base case: null node returns true. | base case：null 節點回傳 true。 | Coding |
| If node value is not in open interval, return false. | 若節點值不在開區間內則回傳 false。 | Coding |
| I recurse left with same min and node value as max. | 遞迴左側時 max 改為當前節點值。 | Coding |
| I recurse right with node value as min and same max. | 遞迴右側時 min 改為當前節點值。 | Coding |
| I combine two recursive results with logical AND. | 兩側遞迴結果用 AND 合併。 | Coding |
| Any false propagates up immediately. | 任一 false 會立即向上傳遞。 | Coding |
| Final helper result is the tree validity answer. | helper 最終結果就是整棵樹是否合法。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [5,1,4,null,null,3,6]. | 我手跑 root [5,1,4,null,null,3,6]。 | Dry-run |
| Root 5 is within initial range, so continue. | root 5 在初始範圍內，繼續。 | Dry-run |
| Left child 1 must be in (-inf,5), valid. | 左子 1 應在 (-inf,5)，合法。 | Dry-run |
| Right child 4 must be in (5,+inf), but 4 violates this. | 右子 4 應在 (5,+inf)，但 4 違反。 | Dry-run |
| We return false immediately. | 我們立刻回傳 false。 | Dry-run |
| This catches global constraint, not just local parent checks. | 這抓到的是全域限制，不只是局部父子。 | Dry-run |
| Output false matches expected result. | 輸出 false 與預期一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single-node tree should be valid. | 案例一：單節點樹應合法。 | Edge test |
| Case two: duplicate value in subtree should be invalid. | 案例二：子樹有重複值應不合法。 | Edge test |
| Case three: deep violation in right subtree but value less than root. | 案例三：右子樹深處值小於 root 的違規情況。 | Edge test |
| Case four: values at integer limits require safe bound types. | 案例四：整數極值需要安全邊界型別。 | Edge test |
| Case five: perfectly valid skewed BST should pass. | 案例五：合法斜 BST 應通過。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) recursion depth. | 空間複雜度是 O(h) 遞迴深度。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each node is validated exactly once with range bounds. | 每個節點只會用範圍驗證一次。 | Complexity |
| Per node operations are constant-time comparisons. | 每節點僅做常數時間比較。 | Complexity |
| Recursion stack depth equals tree height h. | 遞迴堆疊深度等於樹高 h。 | Complexity |
| Worst skew gives O(n) stack, balanced gives O(log n). | 最壞斜樹 O(n)，平衡樹 O(log n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me avoid local-only parent-child comparison trap. | 我先避開只比父子的常見陷阱。 | If stuck |
| I need global range constraints per subtree. | 每棵子樹都要帶全域範圍限制。 | If stuck |
| Left recursion updates upper bound. | 左遞迴要更新上界。 | If stuck |
| Right recursion updates lower bound. | 右遞迴要更新下界。 | If stuck |
| I might have used closed interval accidentally. | 我可能誤用了閉區間。 | If stuck |
| Let me switch back to strict open interval checks. | 我改回嚴格開區間檢查。 | If stuck |
| I will rerun invalid sample with node 4 under right subtree. | 我重跑右子樹含 4 的無效範例。 | If stuck |
| Now it correctly returns false. | 現在能正確回傳 false。 | If stuck |
| I will test valid sample [2,1,3] again. | 我再測合法範例 [2,1,3]。 | If stuck |
| Great, now both pass and fail cases look correct. | 很好，合法與不合法案例都正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed BST validation with range-propagation DFS. | 我完成了範圍傳遞 DFS 的 BST 驗證。 | Wrap-up |
| This correctly enforces global ordering constraints. | 這可正確強制全域排序限制。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h). | 空間複雜度是 O(h)。 | Wrap-up |
| I can also explain in-order monotonic approach if needed. | 若需要我也可說明中序遞增解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Validate whether tree satisfies strict BST rules. | 驗證樹是否符合嚴格 BST 規則。 | Cheat sheet |
| Do not only compare parent and child. | 不能只比父子。 | Cheat sheet |
| Use DFS with value range bounds. | 用帶範圍的 DFS。 | Cheat sheet |
| Root range is (-inf, +inf). | root 範圍是 (-inf,+inf)。 | Cheat sheet |
| Null node returns true. | null 節點回傳 true。 | Cheat sheet |
| Value must satisfy min < val < max. | 值必須滿足 min < val < max。 | Cheat sheet |
| Left subtree max becomes node value. | 左子樹上界改為 node 值。 | Cheat sheet |
| Right subtree min becomes node value. | 右子樹下界改為 node 值。 | Cheat sheet |
| Return leftValid AND rightValid. | 回傳 leftValid AND rightValid。 | Cheat sheet |
| Any violation returns false immediately. | 任一違規立即回傳 false。 | Cheat sheet |
| Use long bounds for INT edge safety. | 用 long 邊界避免整數極值問題。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(h). | 空間 O(h)。 | Cheat sheet |
| Test valid [2,1,3]. | 測合法 [2,1,3]。 | Cheat sheet |
| Test invalid [5,1,4,null,null,3,6]. | 測無效 [5,1,4,null,null,3,6]。 | Cheat sheet |
| Test duplicate values. | 測重複值。 | Cheat sheet |
| Common bug: closed-interval check. | 常見錯誤：用成閉區間。 | Cheat sheet |
| Common bug: no global bounds propagation. | 常見錯誤：沒傳遞全域範圍。 | Cheat sheet |
| Mention in-order increasing alternative. | 可提中序遞增替代法。 | Cheat sheet |
| End by stressing global BST invariant. | 收尾強調全域 BST 不變量。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Top-down range-validation DFS is preserved.
- No hallucinated constraints: ✅ Strict inequality and boundary handling align with source.
- Language simplicity: ✅ Natural concise interview-spoken lines.
