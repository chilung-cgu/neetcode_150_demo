# 10 Count Good Nodes in Binary Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/10_Count_Good_Nodes.md`

> Quick links: [Source Solution](../10_Count_Good_Nodes.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the good-nodes problem. | 我先重述好節點計數題。 | Restatement |
| A node is good if no earlier node on root-to-node path is greater. | 若 root 到該點路徑上沒有更大值，該點是好節點。 | Restatement |
| So each node is compared against path maximum so far. | 所以每節點都要比對目前路徑最大值。 | Restatement |
| We need total count of such nodes. | 我們要回傳這類節點總數。 | Restatement |
| Empty tree should return zero. | 空樹應回傳 0。 | Restatement |
| I will use top-down DFS carrying maxSoFar state. | 我會用 top-down DFS 傳遞 maxSoFar。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can root be null, and should that return zero? | root 可能為 null 嗎？若是要回傳 0？ | Clarify |
| Is equality allowed, meaning node value equal to maxSoFar is still good? | 若值等於 maxSoFar 仍算 good 嗎？ | Clarify |
| Should I use recursive DFS as primary solution? | 主解法要用遞迴 DFS 嗎？ | Clarify |
| Is integer range safe for direct comparisons only? | 整數範圍只做比較就安全嗎？ | Clarify |
| Do you want discussion of iterative stack alternative? | 需要補充迭代 stack 替代法嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks each node against all ancestors on its path. | 暴力法讓每節點逐一比較所有祖先。 | Approach |
| This repeats path scans many times. | 這會重複掃描大量路徑。 | Approach |
| Worst-case skewed tree can degrade to O(n^2). | 最壞斜樹情況會退化到 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use DFS from root while carrying maxSoFar on current path. | 從 root DFS，同步攜帶路徑最大值 maxSoFar。 | Approach |
| If node value is at least maxSoFar, count it as good. | 若節點值 >= maxSoFar，就計為 good。 | Approach |
| Update path max to max(maxSoFar, node value). | 路徑最大值更新為 max(maxSoFar, node值)。 | Approach |
| Recurse left and right with updated max. | 用更新後最大值遞迴左右子樹。 | Approach |
| Sum current count plus child counts for final answer. | 當前計數加左右子樹計數即為答案。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| In goodNodes, if root is null, return zero. | 在 goodNodes 中，root 為 null 回傳 0。 | Coding |
| Otherwise call dfs with root and root value as maxSoFar. | 否則呼叫 dfs(root, root值)。 | Coding |
| In dfs, null node returns zero. | dfs 中 null 節點回傳 0。 | Coding |
| I initialize count to zero for current node. | 我先把當前節點 count 設為 0。 | Coding |
| If node value is greater than or equal to maxSoFar, count becomes one. | 若節點值 >= maxSoFar，count 變成 1。 | Coding |
| I update maxSoFar accordingly. | 接著更新 maxSoFar。 | Coding |
| I add dfs of left child and dfs of right child. | 我加上左子樹與右子樹 dfs 結果。 | Coding |
| Return total count for this subtree. | 回傳此子樹的總 good 節點數。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [3,1,4,3,null,1,5]. | 我手跑 root [3,1,4,3,null,1,5]。 | Dry-run |
| Start at root 3 with maxSoFar 3, so root is good. | 從 root 3、maxSoFar=3 開始，root 是 good。 | Dry-run |
| Go left to 1, maxSoFar remains 3, so 1 is not good. | 往左到 1，maxSoFar 仍 3，所以 1 非 good。 | Dry-run |
| Left child 3 equals maxSoFar 3, so it is good. | 左子節點 3 等於 maxSoFar 3，算 good。 | Dry-run |
| Go right to 4, 4 >= 3, so 4 is good and max becomes 4. | 往右到 4，4>=3，4 是 good 並更新 max=4。 | Dry-run |
| Node 1 under 4 is not good, node 5 is good. | 4 底下的 1 非 good，5 是 good。 | Dry-run |
| Total good nodes are 4, matching expected output. | good 節點總數為 4，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty tree should return zero. | 案例一：空樹應回傳 0。 | Edge test |
| Case two: single-node tree should return one. | 案例二：單節點樹應回傳 1。 | Edge test |
| Case three: strictly increasing root-to-leaf path makes all nodes good. | 案例三：路徑嚴格遞增時全部都是 good。 | Edge test |
| Case four: strictly decreasing path makes only root good. | 案例四：路徑嚴格遞減時通常只有 root 是 good。 | Edge test |
| Case five: repeated values equal to max should still count good. | 案例五：值等於目前最大值仍應計入 good。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) recursion stack. | 空間複雜度是 O(h) 遞迴堆疊。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| DFS visits each node exactly once. | DFS 對每節點只訪問一次。 | Complexity |
| Per node work is constant-time compare and max update. | 每節點僅做常數時間比較與 max 更新。 | Complexity |
| Stack depth equals tree height h. | 呼叫堆疊深度等於樹高 h。 | Complexity |
| Worst skew gives O(n) stack, balanced tree gives O(log n). | 最壞斜樹 O(n)，平衡樹 O(log n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on what state to carry downward. | 我先聚焦要往下傳的狀態。 | If stuck |
| The key state is maxSoFar on current path. | 核心狀態就是目前路徑最大值 maxSoFar。 | If stuck |
| I should compare current value with maxSoFar before children. | 我應先比當前值與 maxSoFar，再進子節點。 | If stuck |
| I might have updated max too late. | 我可能太晚更新 max。 | If stuck |
| Let me update max right after current-node check. | 我改成當前節點判定後立刻更新 max。 | If stuck |
| I will rerun sample [3,1,4,3,null,1,5]. | 我重跑範例 [3,1,4,3,null,1,5]。 | If stuck |
| Count now returns four correctly. | 現在計數能正確回傳 4。 | If stuck |
| I will test decreasing chain next. | 我再測遞減長鏈。 | If stuck |
| Only root counted, which is expected. | 只算到 root，符合預期。 | If stuck |
| Great, top-down state passing is fixed. | 很好，top-down 狀態傳遞已修正。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed top-down DFS good-node counting. | 我完成 top-down DFS 的 good 節點計數。 | Wrap-up |
| The path maximum is propagated as the core state. | 以路徑最大值作為核心傳遞狀態。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h). | 空間複雜度是 O(h)。 | Wrap-up |
| I can provide iterative stack version if needed. | 若需要我可補充迭代 stack 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Count nodes that are path-maximum candidates. | 計算路徑最大值候選節點數。 | Cheat sheet |
| Good means no bigger ancestor on root path. | good 代表 root 路徑上無更大祖先。 | Cheat sheet |
| Use top-down DFS. | 使用 top-down DFS。 | Cheat sheet |
| Carry maxSoFar parameter. | 傳遞 maxSoFar 參數。 | Cheat sheet |
| Null node returns 0. | null 節點回傳 0。 | Cheat sheet |
| If node.val >= maxSoFar, count current node. | 若 node.val>=maxSoFar，計入當前節點。 | Cheat sheet |
| Update maxSoFar = max(maxSoFar, node.val). | 更新 maxSoFar=max(maxSoFar,node.val)。 | Cheat sheet |
| Recurse left with updated max. | 用更新 max 遞迴左子樹。 | Cheat sheet |
| Recurse right with updated max. | 用更新 max 遞迴右子樹。 | Cheat sheet |
| Return current + left + right counts. | 回傳 current+left+right 計數。 | Cheat sheet |
| Root-only tree returns 1. | 只有 root 的樹回傳 1。 | Cheat sheet |
| Empty tree returns 0. | 空樹回傳 0。 | Cheat sheet |
| Increasing path -> many good nodes. | 遞增路徑 -> 很多 good 節點。 | Cheat sheet |
| Decreasing path -> mostly root only. | 遞減路徑 -> 多半只有 root。 | Cheat sheet |
| Equality with max still counts good. | 等於 max 仍算 good。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(h). | 空間 O(h)。 | Cheat sheet |
| Bug risk: wrong initial maxSoFar. | 風險：maxSoFar 初值錯。 | Cheat sheet |
| Bug risk: updating max after child recursion. | 風險：遞迴後才更新 max。 | Cheat sheet |
| Mention iterative DFS alternative. | 可提迭代 DFS 替代法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Top-down DFS with path maximum propagation is preserved.
- No hallucinated constraints: ✅ Matches source examples and complexity.
- Language simplicity: ✅ Spoken concise lines for interview delivery.
