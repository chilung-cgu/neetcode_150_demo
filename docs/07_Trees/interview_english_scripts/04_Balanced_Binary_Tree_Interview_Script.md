# 04 Balanced Binary Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/04_Balanced_Binary_Tree.md`

> Quick links: [Source Solution](../04_Balanced_Binary_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the balanced-binary-tree problem. | 我先重述平衡二元樹題目。 | Restatement |
| We need to decide whether the tree is height-balanced. | 我們要判斷樹是否高度平衡。 | Restatement |
| For every node, height difference of two subtrees must be at most one. | 每節點左右子樹高度差都要 ≤ 1。 | Restatement |
| If any node violates this, answer is false. | 只要有節點違反就回傳 false。 | Restatement |
| Empty tree is considered balanced. | 空樹視為平衡樹。 | Restatement |
| I will use bottom-up DFS with an early-fail flag. | 我會用 bottom-up DFS 與提早失敗旗標。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I treat empty tree as balanced true? | 空樹可視為平衡 true 嗎？ | Clarify |
| Is height difference threshold exactly one? | 高度差門檻確定是 1 嗎？ | Clarify |
| Should I optimize beyond O(n^2) brute force? | 需要優化超過 O(n^2) 暴力法嗎？ | Clarify |
| Is recursion preferred for readability here? | 此題偏好用遞迴提升可讀性嗎？ | Clarify |
| Can I return sentinel value -1 for unbalanced subtree? | 我可以用 -1 當不平衡 sentinel 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks every node and recomputes subtree heights repeatedly. | 暴力法每節點都重複計算子樹高度。 | Approach |
| For each node, we compute left and right heights, then recurse children. | 每節點算左右高度，再遞迴檢查子節點。 | Approach |
| This repeated height work leads to O(n^2) worst-case time. | 高度重算使最壞時間變 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use one bottom-up DFS that returns subtree height when balanced. | 用一次 bottom-up DFS，平衡時回傳高度。 | Approach |
| If a subtree is unbalanced, return sentinel -1 immediately. | 若子樹不平衡，立刻回傳 sentinel -1。 | Approach |
| Parent propagates -1 upward without more checks. | 父節點收到 -1 就直接往上傳。 | Approach |
| Otherwise return one plus max of child heights. | 否則回傳 1+max(左右高度)。 | Approach |
| Final answer is dfs(root) not equal to -1, with O(n) time. | 最後判斷 dfs(root)!=-1，時間 O(n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Main function returns whether dfsHeight(root) is not minus one. | 主函式回傳 dfsHeight(root) 是否不等於 -1。 | Coding |
| In helper, null node returns height zero. | helper 中 null 節點回傳高度 0。 | Coding |
| I compute leftHeight recursively. | 我先遞迴計算 leftHeight。 | Coding |
| If leftHeight is minus one, return minus one immediately. | 若 leftHeight 為 -1，立刻回傳 -1。 | Coding |
| I compute rightHeight recursively. | 接著遞迴計算 rightHeight。 | Coding |
| If rightHeight is minus one, return minus one immediately. | 若 rightHeight 為 -1，也立刻回傳 -1。 | Coding |
| If absolute height difference exceeds one, return minus one. | 若高度差絕對值 >1，回傳 -1。 | Coding |
| Otherwise return one plus max of both heights. | 否則回傳 1+max(左右高度)。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [3,9,20,null,null,15,7]. | 我手跑 [3,9,20,null,null,15,7]。 | Dry-run |
| Leaves 9, 15, and 7 each return height one. | 葉節點 9、15、7 都回傳高度 1。 | Dry-run |
| Node 20 gets left one and right one, so returns two. | 節點 20 左右都 1，所以回傳 2。 | Dry-run |
| Root 3 gets left one and right two, difference is one. | root 3 得到左 1 右 2，差值 1。 | Dry-run |
| Difference is valid, so root returns three. | 差值合法，所以 root 回傳 3。 | Dry-run |
| No minus-one appears, final answer is true. | 沒有出現 -1，最終答案是 true。 | Dry-run |
| This matches expected result. | 這與預期結果一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty tree should return true. | 案例一：空樹應回傳 true。 | Edge test |
| Case two: single-node tree should return true. | 案例二：單節點樹應回傳 true。 | Edge test |
| Case three: one-sided chain should return false after depth gap grows. | 案例三：單邊長鏈高度差拉大後應回傳 false。 | Edge test |
| Case four: complete balanced tree should return true. | 案例四：完整平衡樹應回傳 true。 | Edge test |
| Case five: unbalanced deep subtree should fail early via sentinel. | 案例五：深層不平衡子樹應透過 sentinel 提早失敗。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) from recursion stack. | 空間複雜度是 O(h)（遞迴堆疊）。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each node is processed once in bottom-up DFS. | bottom-up DFS 對每節點只處理一次。 | Complexity |
| Per node work is constant-time checks and max operation. | 每節點都是常數時間檢查與 max。 | Complexity |
| Recursion depth is tree height h. | 遞迴深度等於樹高 h。 | Complexity |
| Worst skewed tree gives O(n) stack; balanced gives O(log n). | 最壞斜樹 O(n)；平衡樹 O(log n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate height calculation from balance decision. | 我先把高度計算與平衡判定分開。 | If stuck |
| Sentinel minus one means this subtree is already unbalanced. | sentinel -1 代表該子樹已不平衡。 | If stuck |
| I should propagate minus one upward immediately. | 我應該立刻把 -1 往上傳。 | If stuck |
| I might have forgotten early return after left subtree fails. | 我可能漏了左子樹失敗後的提早返回。 | If stuck |
| Let me add that guard and rerun. | 我補上保護後再重跑。 | If stuck |
| I will test a long left chain now. | 我現在測一條很長的左鏈。 | If stuck |
| It correctly returns false without extra traversal. | 現在能正確回傳 false 且避免多餘遍歷。 | If stuck |
| I will test balanced sample again. | 我再測一次平衡範例。 | If stuck |
| It returns true as expected. | 它如預期回傳 true。 | If stuck |
| Great, the sentinel strategy is working. | 很好，sentinel 策略已正常運作。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I implemented one-pass balanced-tree checking. | 我完成了一次遍歷的平衡樹檢查。 | Wrap-up |
| The minus-one sentinel gives early pruning for failures. | -1 sentinel 可在失敗時提早剪枝。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h). | 空間複雜度是 O(h)。 | Wrap-up |
| I can also compare this with O(n^2) brute force if useful. | 若需要我可再對比 O(n^2) 暴力法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Check if binary tree is height-balanced. | 檢查二元樹是否高度平衡。 | Cheat sheet |
| Balanced means every node has diff <= 1. | 平衡代表每節點差值 <= 1。 | Cheat sheet |
| Empty tree is balanced. | 空樹視為平衡。 | Cheat sheet |
| Brute force recomputes heights repeatedly. | 暴力法會重算高度。 | Cheat sheet |
| Brute force worst time O(n^2). | 暴力最壞時間 O(n^2)。 | Cheat sheet |
| Use bottom-up DFS with sentinel -1. | 用 bottom-up DFS + sentinel -1。 | Cheat sheet |
| Null node returns 0 height. | null 節點回傳 0 高度。 | Cheat sheet |
| Compute left height first. | 先算左高度。 | Cheat sheet |
| If left is -1, return -1. | 若左為 -1，直接回傳 -1。 | Cheat sheet |
| Compute right height next. | 再算右高度。 | Cheat sheet |
| If right is -1, return -1. | 若右為 -1，直接回傳 -1。 | Cheat sheet |
| If abs diff > 1, return -1. | 若絕對差 >1，回傳 -1。 | Cheat sheet |
| Else return 1 + max(left, right). | 否則回傳 1+max(left,right)。 | Cheat sheet |
| Final check: dfs(root) != -1. | 最後判斷 dfs(root) != -1。 | Cheat sheet |
| Test empty tree => true. | 測空樹 => true。 | Cheat sheet |
| Test single node => true. | 測單節點 => true。 | Cheat sheet |
| Test skewed chain => false. | 測斜樹長鏈 => false。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(h). | 空間 O(h)。 | Cheat sheet |
| Common bug: not propagating -1 early. | 常見錯誤：沒提早傳遞 -1。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Bottom-up DFS with `-1` sentinel is preserved.
- No hallucinated constraints: ✅ Uses source balance definition and constraints.
- Language simplicity: ✅ Natural spoken lines with interview pacing.
