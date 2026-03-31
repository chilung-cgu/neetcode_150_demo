# 12 Kth Smallest Element in a BST — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/12_Kth_Smallest_Element_BST.md`

> Quick links: [Source Solution](../12_Kth_Smallest_Element_BST.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the kth-smallest-in-BST problem. | 我先重述 BST 第 k 小題目。 | Restatement |
| We are given BST root and integer k. | 題目給 BST root 與整數 k。 | Restatement |
| We need the k-th smallest value in sorted BST order. | 要找 BST 排序後第 k 小的值。 | Restatement |
| In-order traversal of BST is naturally sorted ascending. | BST 的中序遍歷天然是遞增序。 | Restatement |
| So we can stop once we visit k nodes. | 因此走到第 k 個節點即可停止。 | Restatement |
| I will implement iterative in-order with a stack. | 我會用 stack 實作迭代中序。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is k guaranteed between one and total node count? | k 是否保證在 1 到節點總數內？ | Clarify |
| Are BST values unique in this problem setting? | 此題 BST 值是否唯一？ | Clarify |
| Should I prioritize early-stop iterative traversal? | 是否優先用可提早停止的迭代遍歷？ | Clarify |
| Is returning as soon as k reaches zero acceptable? | k 歸零就立即回傳可接受嗎？ | Clarify |
| Do you want recursive in-order as secondary mention? | 需要補充遞迴中序當備選嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force collects all node values and sorts them. | 暴力法先收集所有節點值再排序。 | Approach |
| Then answer is values[k minus one]. | 再取 values[k-1] 作答案。 | Approach |
| This wastes work because BST already provides sorted traversal. | 這很浪費，因為 BST 本身就可產生排序序列。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use iterative in-order traversal with explicit stack. | 用顯式 stack 做迭代中序遍歷。 | Approach |
| Keep moving left while pushing nodes. | 持續往左走並把節點推入 stack。 | Approach |
| Pop one node, this is next smallest value. | 每次彈出節點就是下一個最小值。 | Approach |
| Decrement k after each pop and stop at zero. | 每彈一次就 k--，k=0 時停止。 | Approach |
| Then move to right subtree and continue if needed. | 然後轉向右子樹，必要時繼續。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize an empty stack and current pointer at root. | 我先初始化空 stack 與 current=root。 | Coding |
| While current exists, I push it and move left. | 當 current 存在時，推入並往左走。 | Coding |
| When left chain ends, I pop stack top. | 左鏈到底後，彈出 stack 頂端。 | Coding |
| This popped node is current next-smallest element. | 彈出的節點就是當前下一小元素。 | Coding |
| I decrement k and check whether it is zero. | 我把 k 減一並檢查是否為 0。 | Coding |
| If zero, I return current node value immediately. | 若為 0，立即回傳當前節點值。 | Coding |
| Otherwise I move current to popped node right child. | 否則 current 轉到該節點右子樹。 | Coding |
| Loop continues until answer is found. | 迴圈持續直到找到答案。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [5,3,6,2,4,1] with k equals three. | 我手跑 root [5,3,6,2,4,1]，k=3。 | Dry-run |
| Push left chain 5,3,2,1. | 先推入左鏈 5、3、2、1。 | Dry-run |
| Pop 1, now k becomes two. | 彈出 1，k 變 2。 | Dry-run |
| Pop 2, now k becomes one. | 彈出 2，k 變 1。 | Dry-run |
| Next pop is 3, now k becomes zero. | 下一次彈出 3，k 變 0。 | Dry-run |
| Return 3 immediately as third smallest. | 立即回傳 3 作為第 3 小。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: k equals one should return global minimum. | 案例一：k=1 應回傳全域最小值。 | Edge test |
| Case two: k equals n should return global maximum. | 案例二：k=n 應回傳全域最大值。 | Edge test |
| Case three: single-node tree with k one. | 案例三：單節點且 k=1。 | Edge test |
| Case four: skewed BST checks stack depth behavior. | 案例四：斜 BST 測試 stack 深度。 | Edge test |
| Case five: balanced BST verifies early-stop after k pops. | 案例五：平衡 BST 驗證 k 次彈出後提早停止。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(H plus k), worst-case O(n). | 時間複雜度是 O(H+k)，最壞 O(n)。 | Complexity |
| Space complexity is O(H) for stack height. | 空間複雜度是 O(H)（stack 高度）。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We may descend left path of height H before first pop. | 首次彈出前可能先走高為 H 的左路徑。 | Complexity |
| Then we perform k pop steps to reach k-th smallest. | 接著執行 k 次彈出走到第 k 小。 | Complexity |
| So total work is O(H+k), bounded by O(n). | 總工作量 O(H+k)，上界為 O(n)。 | Complexity |
| Stack stores at most one root-to-leaf path, O(H) space. | stack 最多存一條 root-to-leaf 路徑，空間 O(H)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me rely on BST in-order sorted property. | 我先回到 BST 中序遞增性質。 | If stuck |
| I should not sort all values unnecessarily. | 我不應該多做全量排序。 | If stuck |
| Push-left phase and pop phase must alternate correctly. | 推左階段與彈出階段要正確交替。 | If stuck |
| I might have forgotten moving to right child after pop. | 我可能漏了彈出後要去右子樹。 | If stuck |
| Let me add current equals current right transition. | 我補上 current = current->right。 | If stuck |
| I will rerun sample with k equals one. | 我重跑 k=1 範例。 | If stuck |
| It now returns smallest value correctly. | 現在能正確回傳最小值。 | If stuck |
| I will rerun sample with k equals n. | 我再跑 k=n 範例。 | If stuck |
| It now returns largest value correctly. | 現在也能正確回傳最大值。 | If stuck |
| Great, traversal state machine is stable now. | 很好，遍歷狀態機已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed iterative in-order k-th smallest search. | 我完成了迭代中序的第 k 小搜尋。 | Wrap-up |
| The algorithm stops early once k reaches zero. | 演算法在 k 歸零時可提早停止。 | Wrap-up |
| Runtime is O(H+k), worst-case O(n). | 時間是 O(H+k)，最壞 O(n)。 | Wrap-up |
| Space is O(H). | 空間是 O(H)。 | Wrap-up |
| I can also provide recursive in-order variant if needed. | 若需要我也可提供遞迴中序版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find k-th smallest value in BST. | 找 BST 的第 k 小值。 | Cheat sheet |
| In-order traversal is sorted ascending. | 中序遍歷為遞增序。 | Cheat sheet |
| Use iterative stack traversal. | 使用迭代 stack 遍歷。 | Cheat sheet |
| current starts at root. | current 從 root 開始。 | Cheat sheet |
| Push current and move left repeatedly. | 持續推入 current 並往左。 | Cheat sheet |
| Pop stack for next smallest. | 彈出 stack 取得下一小。 | Cheat sheet |
| Decrement k after each pop. | 每次彈出後 k--。 | Cheat sheet |
| If k equals zero, return value. | 若 k=0，立即回傳。 | Cheat sheet |
| Move current to right child. | current 轉到右子樹。 | Cheat sheet |
| Continue while stack or current exists. | 當 stack 或 current 存在就繼續。 | Cheat sheet |
| Time O(H+k). | 時間 O(H+k)。 | Cheat sheet |
| Worst-case time O(n). | 最壞時間 O(n)。 | Cheat sheet |
| Space O(H). | 空間 O(H)。 | Cheat sheet |
| Test k=1 for minimum. | 測 k=1 拿最小值。 | Cheat sheet |
| Test k=n for maximum. | 測 k=n 拿最大值。 | Cheat sheet |
| Test single-node tree. | 測單節點樹。 | Cheat sheet |
| Common bug: forgetting right-child transition. | 常見錯誤：漏右子樹轉移。 | Cheat sheet |
| Common bug: decrementing k in wrong place. | 常見錯誤：k-- 位置錯誤。 | Cheat sheet |
| Mention recursive alternative briefly. | 可簡提遞迴替代法。 | Cheat sheet |
| End by stressing early-stop advantage. | 收尾強調提早停止優勢。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Iterative in-order with early stop is preserved.
- No hallucinated constraints: ✅ Complexity uses source `O(H+k)` framing.
- Language simplicity: ✅ Clear short spoken interview lines.
