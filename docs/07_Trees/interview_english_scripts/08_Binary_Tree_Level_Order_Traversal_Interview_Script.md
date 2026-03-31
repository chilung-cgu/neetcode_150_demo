# 08 Binary Tree Level Order Traversal — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/08_Binary_Tree_Level_Order_Traversal.md`

> Quick links: [Source Solution](../08_Binary_Tree_Level_Order_Traversal.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the level-order traversal problem. | 我先重述層序遍歷題目。 | Restatement |
| We are given binary-tree root and need level-by-level output. | 題目給 root，要逐層輸出節點值。 | Restatement |
| Each level should be listed from left to right. | 每一層都要由左到右。 | Restatement |
| Final result is a 2D array of levels. | 最後結果是二維陣列。 | Restatement |
| Empty tree should return an empty list. | 空樹應回傳空陣列。 | Restatement |
| I will use queue-based BFS, the standard level-order method. | 我會用 queue BFS，標準層序作法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For empty root, should return be an empty vector? | root 為空時要回傳空 vector 嗎？ | Clarify |
| Do we strictly preserve left-to-right order in each level? | 每層是否要嚴格維持左到右順序？ | Clarify |
| Is iterative BFS preferred over DFS-by-depth variant? | 主解是否偏好迭代 BFS 而非 DFS+depth？ | Clarify |
| Are negative node values handled normally? | 負值節點是否照常處理即可？ | Clarify |
| Is O(n) time and O(n) space expected target? | 目標是否為 O(n) 時間與 O(n) 空間？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A less direct way is DFS with depth parameter. | 較不直觀的方法是 DFS 帶 depth。 | Approach |
| We append node value into result[depth] dynamically. | 把節點值動態放進 result[depth]。 | Approach |
| It works in O(n), but queue BFS matches level order more naturally. | 雖可 O(n)，但 queue BFS 更貼近題意。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use a queue initialized with root node. | 使用 queue，初始放入 root。 | Approach |
| For each round, record current queue size as level size. | 每輪先記錄 queue 大小當作層大小。 | Approach |
| Pop exactly that many nodes to build one level list. | 彈出固定數量節點形成一層結果。 | Approach |
| Push each node's left and right children if they exist. | 存在的左右子節點再推入 queue。 | Approach |
| Append level list to result until queue is empty. | 重複直到 queue 空，逐層加入結果。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create result as vector of vector integers. | 我先建立 `vector<vector<int>> result`。 | Coding |
| If root is null, return result immediately. | 若 root 為 null，立即回傳 result。 | Coding |
| I create queue and push root first. | 建立 queue 並先推入 root。 | Coding |
| While queue is not empty, process one level. | 只要 queue 非空就處理一層。 | Coding |
| I read levelSize from current queue length. | 用當前 queue 長度當 levelSize。 | Coding |
| I loop levelSize times, pop nodes, and collect values. | 迴圈 levelSize 次，彈出節點收集值。 | Coding |
| For each node, I push non-null children into queue. | 對每節點把非 null 子節點推入 queue。 | Coding |
| After loop, append currentLevel to result. | 該層完成後把 currentLevel 加入 result。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [3,9,20,null,null,15,7]. | 我手跑 root [3,9,20,null,null,15,7]。 | Dry-run |
| Queue starts with [3]. Level size is one. | queue 起始是 [3]，層大小為 1。 | Dry-run |
| Pop 3, level becomes [3], push 9 and 20. | 彈 3，當層為 [3]，推入 9 與 20。 | Dry-run |
| Next queue is [9,20], level size is two. | 下一輪 queue 是 [9,20]，層大小 2。 | Dry-run |
| Pop 9 and 20, level is [9,20], push 15 and 7. | 彈 9、20 得 [9,20]，再推 15、7。 | Dry-run |
| Last level pops 15 and 7, level is [15,7]. | 最後一層彈 15、7，得到 [15,7]。 | Dry-run |
| Final result is [[3],[9,20],[15,7]]. | 最終結果是 [[3],[9,20],[15,7]]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty tree should return empty list. | 案例一：空樹應回傳空陣列。 | Edge test |
| Case two: single-node tree should return one level. | 案例二：單節點樹應回傳單一層。 | Edge test |
| Case three: left-skewed tree has one node per level. | 案例三：左斜樹每層一個節點。 | Edge test |
| Case four: right-skewed tree has one node per level. | 案例四：右斜樹每層一個節點。 | Edge test |
| Case five: complete tree verifies proper level grouping. | 案例五：完整樹驗證分層分組正確。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(n) in worst case. | 最壞空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Every node enters and leaves the queue exactly once. | 每個節點都恰好進出 queue 一次。 | Complexity |
| Per-node operations are constant-time pushes and pops. | 每節點僅做常數時間推入與彈出。 | Complexity |
| Queue can hold up to tree maximum width. | queue 大小可達樹的最大寬度。 | Complexity |
| In worst case width is O(n), so extra space is O(n). | 最壞寬度 O(n)，故額外空間 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate level boundary logic first. | 我先釐清層界線的處理邏輯。 | If stuck |
| I must snapshot queue size before popping this level. | 我必須先記錄本層 queue 大小。 | If stuck |
| That size prevents mixing next-level nodes too early. | 這樣才不會混入下一層節點。 | If stuck |
| I might have used dynamic queue size inside loop. | 我可能誤用迴圈中變動的 queue 大小。 | If stuck |
| Let me fix loop bound to initial levelSize. | 我改成固定使用初始 levelSize。 | If stuck |
| I will rerun sample tree now. | 我現在重跑範例樹。 | If stuck |
| Levels are now grouped correctly. | 現在層分組已正確。 | If stuck |
| I will test empty tree too. | 我也測試空樹。 | If stuck |
| Empty tree returns empty list correctly. | 空樹可正確回傳空陣列。 | If stuck |
| Great, BFS level logic is stable. | 很好，BFS 分層邏輯已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I implemented queue-based level-order traversal. | 我完成了 queue 型層序遍歷。 | Wrap-up |
| The key is fixed levelSize per BFS round. | 核心是每輪固定 levelSize。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(n) in worst-width levels. | 最壞寬度下空間是 O(n)。 | Wrap-up |
| I can also show DFS-depth variant if needed. | 若需要我也可補 DFS+depth 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Return level-order traversal as 2D list. | 回傳層序遍歷二維陣列。 | Cheat sheet |
| Use queue BFS. | 使用 queue BFS。 | Cheat sheet |
| If root null, return empty list. | root 為 null 回傳空陣列。 | Cheat sheet |
| Push root into queue first. | 先把 root 推入 queue。 | Cheat sheet |
| While queue not empty, process one level. | queue 非空就處理一層。 | Cheat sheet |
| levelSize = queue.size() before loop. | 迴圈前先取 levelSize。 | Cheat sheet |
| Loop levelSize times. | 迴圈固定跑 levelSize 次。 | Cheat sheet |
| Pop node and append value. | 彈節點並加入值。 | Cheat sheet |
| Push left child if exists. | 有左子就推入。 | Cheat sheet |
| Push right child if exists. | 有右子就推入。 | Cheat sheet |
| Append currentLevel to result. | 當層結果加入 result。 | Cheat sheet |
| Repeat until queue empty. | 重複直到 queue 為空。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Test empty tree. | 測空樹。 | Cheat sheet |
| Test single node. | 測單節點。 | Cheat sheet |
| Test skewed trees. | 測斜樹。 | Cheat sheet |
| Common bug: not fixing levelSize upfront. | 常見錯誤：沒先固定 levelSize。 | Cheat sheet |
| Common bug: mixing level boundaries. | 常見錯誤：層界線混淆。 | Cheat sheet |
| Mention DFS depth alternative. | 可提 DFS depth 替代法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Queue BFS level-by-level processing is preserved.
- No hallucinated constraints: ✅ Output shape and complexity align with source chapter.
- Language simplicity: ✅ Interview-ready concise spoken wording.
