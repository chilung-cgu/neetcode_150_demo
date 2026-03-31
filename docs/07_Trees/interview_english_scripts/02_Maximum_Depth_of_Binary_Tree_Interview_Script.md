# 02 Maximum Depth of Binary Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/02_Maximum_Depth_of_Binary_Tree.md`

> Quick links: [Source Solution](../02_Maximum_Depth_of_Binary_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the max-depth problem. | 我先重述最大深度題。 | Restatement |
| We need the number of nodes on the longest root-to-leaf path. | 要求 root 到最深 leaf 路徑上的節點數。 | Restatement |
| Empty tree depth is zero. | 空樹深度定義為 0。 | Restatement |
| Non-empty node depth depends on deeper subtree. | 非空節點深度取決於較深的子樹。 | Restatement |
| This is a classic DFS recursion pattern. | 這是經典 DFS 遞迴模式。 | Restatement |
| I will return one plus max of left and right depths. | 我會回傳 1+max(左深度,右深度)。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can root be null in test cases? | 測資中 root 可能為 null 嗎？ | Clarify |
| Is depth measured by node count, not edge count? | 深度是用節點數而非邊數對嗎？ | Clarify |
| Do you prefer recursive DFS as primary answer? | 主要答案偏好遞迴 DFS 嗎？ | Clarify |
| Should I also mention iterative BFS level-order method? | 要不要也提 BFS 層序法？ | Clarify |
| Is O(n) expected as optimal runtime? | 最佳時間是否就是 O(n)？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A naive thought is enumerating all root-to-leaf paths explicitly. | 直觀想法是枚舉所有 root-to-leaf 路徑。 | Approach |
| Then choose the longest path length. | 再挑最長路徑長度。 | Approach |
| It is unnecessary because DFS already captures this directly. | 但其實 DFS 可直接完成，不需額外枚舉。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use post-order DFS to get child depths first. | 用後序 DFS 先取得子樹深度。 | Approach |
| Base case null returns zero. | base case：null 回傳 0。 | Approach |
| For node, compute leftDepth and rightDepth recursively. | 對節點遞迴求 leftDepth 與 rightDepth。 | Approach |
| Current depth is one plus max of two depths. | 當前深度是 1 加上兩者較大值。 | Approach |
| Return this upward until root gives final answer. | 逐層回傳，root 即最終答案。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, if root is null, return zero. | 先判斷 root 為 null 就回傳 0。 | Coding |
| I recursively compute depth of root left subtree. | 遞迴計算 root 左子樹深度。 | Coding |
| I recursively compute depth of root right subtree. | 遞迴計算 root 右子樹深度。 | Coding |
| I compare the two depths and pick the larger one. | 比較兩側深度並取較大值。 | Coding |
| I add one for current root node level. | 為當前節點層數再加 1。 | Coding |
| I return that value to parent caller. | 把這個值回傳給上一層。 | Coding |
| Recursion unwinds until original root call completes. | 遞迴回捲直到原始 root 呼叫完成。 | Coding |
| Final returned value is maximum depth. | 最終回傳值就是最大深度。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [3,9,20,null,null,15,7]. | 我手跑 root=[3,9,20,null,null,15,7]。 | Dry-run |
| Node 9 has no children, so its depth is one. | 節點 9 無子節點，深度為 1。 | Dry-run |
| Node 15 and node 7 are leaves, each depth is one. | 節點 15 與 7 都是葉節點，深度各為 1。 | Dry-run |
| Node 20 depth becomes one plus max of one and one, so two. | 節點 20 深度是 1+max(1,1)=2。 | Dry-run |
| Root 3 depth becomes one plus max of one and two, so three. | 根節點 3 深度是 1+max(1,2)=3。 | Dry-run |
| Final answer is three. | 最終答案是 3。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty tree. | 案例一：空樹。 | Edge test |
| Case two: single-node tree. | 案例二：單節點樹。 | Edge test |
| Case three: completely skewed tree. | 案例三：完全斜樹。 | Edge test |
| Case four: perfectly balanced tree. | 案例四：完美平衡樹。 | Edge test |
| Case five: mixed null children at different levels. | 案例五：不同層級夾雜 null 子節點。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) due to recursion stack. | 空間複雜度是 O(h)（遞迴堆疊）。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Every node is visited exactly once by DFS. | DFS 對每個節點恰好訪問一次。 | Complexity |
| Per node work is constant-time max and add operations. | 每節點只做常數時間比較與加法。 | Complexity |
| Call-stack depth equals current tree height h. | 呼叫堆疊深度等於樹高 h。 | Complexity |
| Worst skew gives O(n) stack, balanced gives O(log n). | 最壞斜樹是 O(n)，平衡樹是 O(log n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me recheck the depth definition first. | 我先重檢深度定義。 | If stuck |
| Here depth counts nodes, not edges. | 這題深度是數節點，不是數邊。 | If stuck |
| Base case must return zero for null. | base case 對 null 必須回傳 0。 | If stuck |
| I might have returned one for null by mistake. | 我可能誤把 null 回傳成 1。 | If stuck |
| Let me fix that and rerun the sample. | 我修正後重跑範例。 | If stuck |
| I also verify skewed-tree output. | 我也驗證斜樹輸出。 | If stuck |
| Now recursion values propagate correctly. | 現在遞迴值傳遞正確。 | If stuck |
| Root gets the proper maximum depth. | root 能拿到正確最大深度。 | If stuck |
| Great, complexity target is still O(n). | 很好，複雜度仍是 O(n)。 | If stuck |
| I can now finalize confidently. | 我現在可放心收尾。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished recursive maximum-depth implementation. | 我完成了遞迴最大深度實作。 | Wrap-up |
| I validated empty, leaf, and skewed-tree cases. | 我驗證了空樹、葉節點與斜樹案例。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h) recursion stack. | 空間是 O(h) 遞迴堆疊。 | Wrap-up |
| I can provide BFS level-order variant if needed. | 若需要我可提供 BFS 層序版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find maximum depth of binary tree. | 求二元樹最大深度。 | Cheat sheet |
| Empty tree depth is zero. | 空樹深度是 0。 | Cheat sheet |
| Depth counts nodes on path. | 深度以路徑節點數計算。 | Cheat sheet |
| Use recursive DFS. | 使用遞迴 DFS。 | Cheat sheet |
| Base case null returns 0. | base case：null 回傳 0。 | Cheat sheet |
| leftDepth = dfs(left). | leftDepth = dfs(left)。 | Cheat sheet |
| rightDepth = dfs(right). | rightDepth = dfs(right)。 | Cheat sheet |
| return 1 + max(leftDepth, rightDepth). | 回傳 1+max(leftDepth,rightDepth)。 | Cheat sheet |
| Visit each node once. | 每個節點只訪問一次。 | Cheat sheet |
| Time is O(n). | 時間是 O(n)。 | Cheat sheet |
| Stack space is O(h). | 堆疊空間是 O(h)。 | Cheat sheet |
| Test empty-tree case. | 測空樹案例。 | Cheat sheet |
| Test single-node case. | 測單節點案例。 | Cheat sheet |
| Test skewed-tree case. | 測斜樹案例。 | Cheat sheet |
| Test balanced-tree case. | 測平衡樹案例。 | Cheat sheet |
| Bug risk: wrong base return value. | 風險：base 回傳值寫錯。 | Cheat sheet |
| Bug risk: using min instead of max. | 風險：誤用 min 而非 max。 | Cheat sheet |
| Mention BFS alternative. | 可提 BFS 替代法。 | Cheat sheet |
| Keep explanation bottom-up. | 說明採 bottom-up。 | Cheat sheet |
| End with numeric depth confirmation. | 收尾確認深度數值。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Recursive depth formula is preserved.
- No hallucinated constraints: ✅ Uses source depth definition and constraints.
- Language simplicity: ✅ Concise spoken lines for interviews.
