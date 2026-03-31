# 14 Binary Tree Maximum Path Sum — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/14_Binary_Tree_Maximum_Path_Sum.md`

> Quick links: [Source Solution](../14_Binary_Tree_Maximum_Path_Sum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the maximum-path-sum problem. | 我先重述最大路徑和題目。 | Restatement |
| We need the largest sum among all valid parent-child paths. | 要找所有父子連續路徑中的最大總和。 | Restatement |
| Path can start and end at any nodes, not necessarily root. | 路徑可在任意節點起終，不必經 root。 | Restatement |
| Path must contain at least one node. | 路徑至少要包含一個節點。 | Restatement |
| Values may be negative, so we must handle pruning carefully. | 節點可能為負，要小心做剪枝。 | Restatement |
| I will use bottom-up DFS with a global best value. | 我會用 bottom-up DFS 加全域最佳值。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can path start and end at arbitrary nodes in the tree? | 路徑可在樹中任意節點起終嗎？ | Clarify |
| Is at least one node always required in the path? | 路徑是否一定至少包含一節點？ | Clarify |
| Are all-negative trees possible in test cases? | 測資可能全負數嗎？ | Clarify |
| Should I use global variable to store best path sum? | 我可用全域變數記錄最佳路徑和嗎？ | Clarify |
| Is pruning negative branch gains with max(0, gain) acceptable? | 用 max(0,gain) 剪掉負分支可以嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries each node as a turning point and recomputes branch sums repeatedly. | 暴力法把每節點當轉折點並重算分支和。 | Approach |
| This duplicates subtree computations many times. | 這會大量重複子樹計算。 | Approach |
| Worst-case complexity becomes O(n^2). | 最壞複雜度會變成 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| DFS helper returns best one-branch gain upward to parent. | DFS helper 向父節點回傳最佳單邊貢獻。 | Approach |
| For each node, compute leftGain and rightGain recursively. | 每節點遞迴得到 leftGain 與 rightGain。 | Approach |
| Negative gains are replaced by zero to avoid lowering total. | 負貢獻以 0 取代，避免拉低總和。 | Approach |
| Candidate full path through node is node plus leftGain plus rightGain. | 經過該節點完整路徑是 node+leftGain+rightGain。 | Approach |
| Update global answer with candidate and return one-branch gain. | 用候選值更新全域答案，回傳單邊貢獻。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize globalMax to INT_MIN before DFS. | DFS 前先把 globalMax 設為 INT_MIN。 | Coding |
| In helper, null node returns zero gain. | helper 中 null 節點回傳 0 貢獻。 | Coding |
| I recursively compute left and right branch gains. | 我遞迴計算左右分支貢獻。 | Coding |
| I clamp each branch gain with max(0, gain). | 每個分支用 max(0,gain) 做剪枝。 | Coding |
| I compute currentPath as node value plus both gains. | currentPath = node值 + 左右貢獻。 | Coding |
| I update globalMax with currentPath if larger. | 若 currentPath 較大就更新 globalMax。 | Coding |
| I return node value plus max of two branch gains. | 回傳 node值 + max(左右貢獻)。 | Coding |
| Main function returns globalMax after DFS completes. | 主函式在 DFS 後回傳 globalMax。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [-10,9,20,null,null,15,7]. | 我手跑 root [-10,9,20,null,null,15,7]。 | Dry-run |
| Leaf 15 returns gain 15, leaf 7 returns gain 7. | 葉節點 15 回 15，葉節點 7 回 7。 | Dry-run |
| At node 20, currentPath is 20 plus 15 plus 7 equals 42. | 在節點 20，currentPath=20+15+7=42。 | Dry-run |
| globalMax updates to 42. | globalMax 更新為 42。 | Dry-run |
| Node 20 returns one-branch gain 20 plus max(15,7)=35. | 節點 20 回傳單邊 20+max(15,7)=35。 | Dry-run |
| Root -10 computes path -10 plus 9 plus 35 equals 34. | root -10 算出路徑和 -10+9+35=34。 | Dry-run |
| Final answer stays 42, matching expected output. | 最終答案維持 42，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single-node tree returns that node value. | 案例一：單節點樹回傳該節點值。 | Edge test |
| Case two: all-negative tree returns maximum single node. | 案例二：全負數樹回傳最大單節點。 | Edge test |
| Case three: path not passing root should still be considered. | 案例三：不經 root 的路徑也必須考慮。 | Edge test |
| Case four: skewed tree behaves like best contiguous chain. | 案例四：斜樹行為像最佳連續鏈。 | Edge test |
| Case five: mixed positive and negative values test pruning. | 案例五：正負混合要驗證剪枝效果。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) recursion stack. | 空間複雜度是 O(h) 遞迴堆疊。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| DFS visits each node exactly once. | DFS 對每個節點僅訪問一次。 | Complexity |
| Each visit does constant-time arithmetic and max operations. | 每次訪問只做常數時間運算與比較。 | Complexity |
| Stack depth equals tree height h. | 呼叫堆疊深度等於樹高 h。 | Complexity |
| Worst skew gives O(n) stack, balanced gives O(log n). | 最壞斜樹 O(n)，平衡樹 O(log n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate two concepts: global answer and return gain. | 我先分清兩個概念：全域答案與回傳貢獻。 | If stuck |
| Return gain can only include one branch. | 回傳貢獻只能選單邊分支。 | If stuck |
| Global answer may include both branches at current node. | 全域答案可在當前節點同時含左右分支。 | If stuck |
| I might have returned both branches to parent incorrectly. | 我可能錯把雙分支回傳給父節點。 | If stuck |
| Let me fix return to node plus max(leftGain,rightGain). | 我修正回傳為 node+max(leftGain,rightGain)。 | If stuck |
| I also keep max(0, gain) pruning for negatives. | 同時保留 max(0,gain) 負值剪枝。 | If stuck |
| I will rerun all-negative sample now. | 我現在重跑全負數範例。 | If stuck |
| It now returns largest single node correctly. | 現在可正確回傳最大單節點。 | If stuck |
| I will rerun mixed sample too. | 我也重跑正負混合範例。 | If stuck |
| Great, both global and return logic are consistent. | 很好，全域與回傳邏輯都一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed maximum-path-sum DFS with branch pruning. | 我完成了帶分支剪枝的最大路徑和 DFS。 | Wrap-up |
| The key is separating local return gain from global path candidate. | 核心是分離回傳貢獻與全域候選路徑。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h). | 空間複雜度是 O(h)。 | Wrap-up |
| I can also explain relation to diameter-of-tree pattern. | 若需要我可補充它與直徑題的關聯。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find maximum path sum in binary tree. | 求二元樹最大路徑和。 | Cheat sheet |
| Path can start and end anywhere. | 路徑可在任意點起終。 | Cheat sheet |
| Path must include at least one node. | 路徑至少含一節點。 | Cheat sheet |
| Use bottom-up DFS. | 使用 bottom-up DFS。 | Cheat sheet |
| Track globalMax for best full path. | 用 globalMax 記錄最佳完整路徑。 | Cheat sheet |
| Helper returns one-branch gain only. | helper 只回傳單邊貢獻。 | Cheat sheet |
| leftGain = max(0, dfs(left)). | leftGain = max(0, dfs(left))。 | Cheat sheet |
| rightGain = max(0, dfs(right)). | rightGain = max(0, dfs(right))。 | Cheat sheet |
| currentPath = node + leftGain + rightGain. | currentPath = node+leftGain+rightGain。 | Cheat sheet |
| Update globalMax with currentPath. | 用 currentPath 更新 globalMax。 | Cheat sheet |
| Return node + max(leftGain, rightGain). | 回傳 node+max(leftGain,rightGain)。 | Cheat sheet |
| Initialize globalMax = INT_MIN. | globalMax 初始為 INT_MIN。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(h). | 空間 O(h)。 | Cheat sheet |
| Test all-negative tree. | 測全負數樹。 | Cheat sheet |
| Test path not through root. | 測不經 root 路徑。 | Cheat sheet |
| Common bug: returning two branches upward. | 常見錯誤：把雙分支往上回傳。 | Cheat sheet |
| Common bug: forgetting negative pruning. | 常見錯誤：忘記負值剪枝。 | Cheat sheet |
| Mention diameter-like pattern relation. | 可提與直徑題模式相似。 | Cheat sheet |
| End by distinguishing global vs return values. | 收尾強調全域值與回傳值不同。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Bottom-up DFS with `max(0, gain)` pruning is preserved.
- No hallucinated constraints: ✅ Path definition and negative-value handling align with source.
- Language simplicity: ✅ Clear spoken script lines for interview use.
