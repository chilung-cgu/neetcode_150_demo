# 01 Invert Binary Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/01_Invert_Binary_Tree.md`

> Quick links: [Source Solution](../01_Invert_Binary_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the invert-binary-tree problem. | 我先重述翻轉二元樹題目。 | Restatement |
| We need to mirror the tree around its root axis. | 我們要把整棵樹沿根軸鏡像翻轉。 | Restatement |
| For every node, left and right children are swapped. | 每個節點都要交換左右子節點。 | Restatement |
| We return the same root pointer after in-place inversion. | 反轉後回傳同一棵樹的 root 指標。 | Restatement |
| Empty tree should return null directly. | 空樹情況直接回傳 null。 | Restatement |
| I will use recursive DFS for clean implementation. | 我會用遞迴 DFS 實作，最直觀。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I mutate the original tree in place? | 我可以直接原地修改原樹嗎？ | Clarify |
| Should null root return null immediately? | root 為 null 是否立即回傳 null？ | Clarify |
| Is recursion acceptable for this tree size? | 這個節點規模可接受遞迴嗎？ | Clarify |
| Do you want iterative BFS variant after main answer? | 主解後需要我補充 BFS 版本嗎？ | Clarify |
| Is preserving node values and identities required? | 是否要保留節點值與節點身分不變？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| There is no shortcut that skips node visits here. | 這題沒有可跳過節點的捷徑。 | Approach |
| Any valid solution must touch each node at least once. | 任一正確解都至少要訪問每節點一次。 | Approach |
| So baseline lower bound is already O(n). | 所以基礎下界本來就是 O(n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For current node, swap left and right pointers first. | 對當前節點先交換 left 與 right 指標。 | Approach |
| Then recursively invert the new left subtree. | 接著遞迴翻轉新的左子樹。 | Approach |
| Then recursively invert the new right subtree. | 再遞迴翻轉新的右子樹。 | Approach |
| Base case is null node doing nothing. | base case 是 null 節點不處理。 | Approach |
| This yields O(n) time and O(h) recursion stack. | 可達 O(n) 時間與 O(h) 遞迴堆疊。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I handle null root and return null. | 先處理 null root 並回傳 null。 | Coding |
| I store root left in a temp pointer. | 用暫存指標保存 root->left。 | Coding |
| I assign root left to original right. | 把 root->left 指向原本右子樹。 | Coding |
| I assign root right to saved temp subtree. | 把 root->right 指向暫存子樹。 | Coding |
| I recurse on root left subtree now. | 接著遞迴處理 root->left。 | Coding |
| I recurse on root right subtree now. | 再遞迴處理 root->right。 | Coding |
| After both calls, current subtree is fully mirrored. | 兩側遞迴後，此子樹已完整鏡像。 | Coding |
| Finally return root pointer. | 最後回傳 root 指標。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run tree [4,2,7,1,3,6,9]. | 我手跑樹 [4,2,7,1,3,6,9]。 | Dry-run |
| At root 4, swap children 2 and 7. | 在根 4 處先交換子節點 2 與 7。 | Dry-run |
| Recurse into node 7 and swap 6 and 9. | 遞迴到節點 7，交換 6 與 9。 | Dry-run |
| Recurse into node 2 and swap 1 and 3. | 遞迴到節點 2，交換 1 與 3。 | Dry-run |
| Leaf nodes have no children, recursion returns. | 葉節點沒有子節點，遞迴直接返回。 | Dry-run |
| Final tree is [4,7,2,9,6,3,1]. | 最終樹為 [4,7,2,9,6,3,1]。 | Dry-run |
| Output matches expected mirrored tree. | 輸出與預期鏡像樹一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty tree. | 案例一：空樹。 | Edge test |
| Case two: single node tree. | 案例二：單節點樹。 | Edge test |
| Case three: only left-skewed chain. | 案例三：僅左斜鏈樹。 | Edge test |
| Case four: only right-skewed chain. | 案例四：僅右斜鏈樹。 | Edge test |
| Case five: perfect full binary tree. | 案例五：完美滿二元樹。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) recursion depth. | 空間複雜度是 O(h) 遞迴深度。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We visit each node once to perform one swap. | 我們對每個節點訪問一次並做一次交換。 | Complexity |
| Per node work is constant-time pointer reassignment. | 每個節點只做常數時間指標重設。 | Complexity |
| Recursive call stack height equals tree height h. | 遞迴呼叫堆疊高度等於樹高 h。 | Complexity |
| Worst-case skewed tree gives O(n) stack usage. | 最壞斜樹情況堆疊會到 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me verify base case first. | 我先確認 base case。 | If stuck |
| Null node should return immediately. | null 節點要立即返回。 | If stuck |
| I should swap child pointers before recursive calls. | 我應先交換子指標再遞迴。 | If stuck |
| I might have swapped values instead of pointers. | 我可能誤寫成交換值而非指標。 | If stuck |
| Let me fix to pointer-level swap. | 我改成正確的指標層交換。 | If stuck |
| I will rerun one balanced sample tree. | 我重跑一棵平衡範例樹。 | If stuck |
| I will also test skewed tree shape. | 我也測試斜樹形狀。 | If stuck |
| Both left and right skew cases now mirror correctly. | 左斜與右斜現在都能正確鏡像。 | If stuck |
| Great, recursion flow is stable. | 很好，遞迴流程已穩定。 | If stuck |
| I can now conclude with complexity. | 現在可以收斂到複雜度總結。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed recursive in-place tree inversion. | 我完成了遞迴原地翻轉樹。 | Wrap-up |
| I validated empty, single, and skewed trees. | 我驗證了空樹、單節點與斜樹。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h) from recursion stack. | 空間來自遞迴堆疊 O(h)。 | Wrap-up |
| I can also provide iterative queue version if needed. | 若需要我也可補充迭代 queue 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Mirror binary tree by swapping children. | 透過交換子節點鏡像二元樹。 | Cheat sheet |
| Return same root after in-place mutation. | 原地修改後回傳同一 root。 | Cheat sheet |
| Null root returns null. | null root 直接回傳 null。 | Cheat sheet |
| Baseline still needs visiting all nodes. | 基本上仍要訪問所有節點。 | Cheat sheet |
| Use recursive DFS. | 使用遞迴 DFS。 | Cheat sheet |
| For each node swap left and right pointers. | 每節點交換 left/right 指標。 | Cheat sheet |
| Recurse into left subtree. | 遞迴處理左子樹。 | Cheat sheet |
| Recurse into right subtree. | 遞迴處理右子樹。 | Cheat sheet |
| Leaf returns naturally. | 葉節點自然返回。 | Cheat sheet |
| Each node processed once. | 每個節點只處理一次。 | Cheat sheet |
| Test empty tree. | 測空樹。 | Cheat sheet |
| Test single-node tree. | 測單節點樹。 | Cheat sheet |
| Test left-skew tree. | 測左斜樹。 | Cheat sheet |
| Test right-skew tree. | 測右斜樹。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(h). | 空間 O(h)。 | Cheat sheet |
| Bug risk: swapping values not pointers. | 風險：誤換值不是換指標。 | Cheat sheet |
| Bug risk: missing base case. | 風險：漏寫 base case。 | Cheat sheet |
| Mention BFS iterative alternative. | 可提 BFS 迭代替代法。 | Cheat sheet |
| End with mirrored output check. | 收尾確認鏡像結果。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Recursive swap-and-recurse inversion is preserved.
- No hallucinated constraints: ✅ Uses source tree constraints and behavior.
- Language simplicity: ✅ Short spoken lines suitable for interviews.
