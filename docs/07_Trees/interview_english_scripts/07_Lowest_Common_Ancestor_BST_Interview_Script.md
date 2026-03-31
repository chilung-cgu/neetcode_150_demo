# 07 Lowest Common Ancestor of a BST — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/07_Lowest_Common_Ancestor_BST.md`

> Quick links: [Source Solution](../07_Lowest_Common_Ancestor_BST.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the LCA-in-BST problem. | 我先重述 BST LCA 題目。 | Restatement |
| We are given a BST root and two nodes p and q. | 題目給 BST root 與兩個節點 p、q。 | Restatement |
| We need the lowest node that is ancestor of both. | 要找同時是兩者祖先的最低節點。 | Restatement |
| BST ordering lets us decide direction at each step. | BST 排序性可讓每步都決定方向。 | Restatement |
| If p and q split around current node, we found answer. | 若 p、q 在當前節點兩側，答案就在這裡。 | Restatement |
| I will implement iterative O(1)-space traversal. | 我會實作迭代 O(1) 空間解法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume p and q always exist in the BST? | 我可假設 p、q 一定存在於 BST 嗎？ | Clarify |
| Are all BST values unique in this problem? | 這題 BST 值都唯一嗎？ | Clarify |
| If one node equals current root, is root valid LCA? | 若其中一點等於當前 root，root 算有效 LCA 嗎？ | Clarify |
| Should I prioritize iterative over recursive version? | 是否優先寫迭代而非遞迴版？ | Clarify |
| Is balanced-vs-skewed complexity discussion expected? | 需要說明平衡與斜樹複雜度差異嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Generic binary-tree LCA DFS can solve this in O(n). | 一般二元樹 LCA DFS 可用 O(n) 解。 | Approach |
| It explores both subtrees and merges return signals. | 它會探索雙子樹並合併回傳訊號。 | Approach |
| But it ignores BST ordering information. | 但這會浪費 BST 的排序資訊。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Start from root and inspect p and q values. | 從 root 開始觀察 p、q 的值。 | Approach |
| If both are smaller than current, move left. | 若兩者都小於當前節點，就往左。 | Approach |
| If both are larger than current, move right. | 若兩者都大於當前節點，就往右。 | Approach |
| Otherwise current node is split point and LCA. | 否則當前節點就是分叉點與 LCA。 | Approach |
| This takes O(h) time and O(1) extra space iteratively. | 迭代版時間 O(h)、額外空間 O(1)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I set current pointer to root. | 我先把 current 指向 root。 | Coding |
| While current is not null, I keep searching. | 只要 current 非 null 就持續搜尋。 | Coding |
| If p and q are both less than current, go left. | 若 p、q 都小於 current，就往左。 | Coding |
| Else if both are greater than current, go right. | 否則若都大於 current，就往右。 | Coding |
| Else we reached split point, return current. | 否則到分叉點，回傳 current。 | Coding |
| This else also covers current equals p or q. | 這個 else 也涵蓋 current 等於 p 或 q。 | Coding |
| If loop ends unexpectedly, return null safeguard. | 若迴圈意外結束，回傳 null 保護值。 | Coding |
| Under valid constraints, answer is found before null. | 在有效限制下通常會先找到答案。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [6,2,8,0,4,7,9,3,5], p=2, q=8. | 我手跑 root [6,2,8,0,4,7,9,3,5]，p=2，q=8。 | Dry-run |
| Start at current 6. | 從 current=6 開始。 | Dry-run |
| p is smaller than 6, q is larger than 6. | p 小於 6，q 大於 6。 | Dry-run |
| They split around current, so 6 is LCA. | 兩者分居兩側，所以 6 是 LCA。 | Dry-run |
| No further traversal is needed. | 不需要再往下走。 | Dry-run |
| Return node 6. | 回傳節點 6。 | Dry-run |
| Output matches expected answer. | 輸出與預期一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: p is ancestor of q, answer should be p. | 案例一：p 是 q 祖先，答案應是 p。 | Edge test |
| Case two: q is ancestor of p, answer should be q. | 案例二：q 是 p 祖先，答案應是 q。 | Edge test |
| Case three: p and q on opposite sides of root. | 案例三：p、q 分別在 root 兩側。 | Edge test |
| Case four: both deep in left subtree. | 案例四：兩者都在左子樹深處。 | Edge test |
| Case five: skewed BST still follows one-way traversal. | 案例五：斜 BST 仍是單向遍歷。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(h). | 時間複雜度是 O(h)。 | Complexity |
| Space complexity is O(1) for iterative solution. | 迭代解法空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We move down one BST path without backtracking. | 我們沿 BST 單一路徑往下，不會回頭。 | Complexity |
| Number of visited nodes is bounded by tree height h. | 造訪節點數受樹高 h 限制。 | Complexity |
| Balanced BST gives O(log n) time. | 平衡 BST 時間是 O(log n)。 | Complexity |
| Worst skewed BST gives O(n) time, still O(1) extra space. | 最壞斜樹時間 O(n)，額外空間仍 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me rely on BST ordering first. | 我先回到 BST 排序性。 | If stuck |
| I only need three direction cases at each node. | 每個節點只要處理三種方向情況。 | If stuck |
| Both smaller means move left. | 都比較小就往左。 | If stuck |
| Both larger means move right. | 都比較大就往右。 | If stuck |
| Otherwise this node is the split point. | 否則此節點就是分叉點。 | If stuck |
| I might have used strict comparisons incorrectly. | 我可能把比較條件寫錯了。 | If stuck |
| Let me ensure equals case returns current immediately. | 我確保相等情況立即回傳 current。 | If stuck |
| I will rerun sample p=2 and q=4. | 我重跑 p=2、q=4 範例。 | If stuck |
| It now returns node 2 correctly. | 現在可正確回傳節點 2。 | If stuck |
| Great, branching logic is fixed. | 很好，分支邏輯已修正。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished iterative LCA search using BST properties. | 我完成利用 BST 性質的迭代 LCA 搜尋。 | Wrap-up |
| The key is stopping at the first split point. | 核心是停在第一個分叉點。 | Wrap-up |
| Runtime is O(h), O(log n) on balanced trees. | 時間 O(h)，平衡樹為 O(log n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can also provide recursive variant if needed. | 若需要我也可提供遞迴版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find LCA of two nodes in BST. | 找 BST 兩節點的 LCA。 | Cheat sheet |
| Use BST ordering property. | 利用 BST 排序性。 | Cheat sheet |
| Start current at root. | current 從 root 開始。 | Cheat sheet |
| If both target values smaller, go left. | 若兩值都較小，往左。 | Cheat sheet |
| If both target values larger, go right. | 若兩值都較大，往右。 | Cheat sheet |
| Otherwise current is LCA. | 否則 current 就是 LCA。 | Cheat sheet |
| Equals case also returns current. | 相等情況也回傳 current。 | Cheat sheet |
| Iterative loop avoids recursion stack. | 迭代迴圈避免遞迴堆疊。 | Cheat sheet |
| Generic tree DFS is O(n). | 一般樹 DFS 是 O(n)。 | Cheat sheet |
| BST-guided search is O(h). | BST 導引搜尋是 O(h)。 | Cheat sheet |
| Balanced BST gives O(log n). | 平衡 BST 為 O(log n)。 | Cheat sheet |
| Skewed BST gives O(n). | 斜 BST 為 O(n)。 | Cheat sheet |
| Iterative extra space O(1). | 迭代額外空間 O(1)。 | Cheat sheet |
| Test when p is ancestor of q. | 測 p 為 q 祖先。 | Cheat sheet |
| Test when q is ancestor of p. | 測 q 為 p 祖先。 | Cheat sheet |
| Test opposite-side split at root. | 測 root 兩側分叉情況。 | Cheat sheet |
| Test deep-left subtree case. | 測深左子樹情況。 | Cheat sheet |
| Common bug: missing equals branch. | 常見錯誤：漏相等分支。 | Cheat sheet |
| Common bug: wrong comparison direction. | 常見錯誤：比較方向寫反。 | Cheat sheet |
| End by stating split-point invariant. | 收尾強調分叉點不變量。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Iterative BST split-point traversal is preserved.
- No hallucinated constraints: ✅ Complexity and assumptions align with source chapter.
- Language simplicity: ✅ Interview-ready concise spoken lines.
