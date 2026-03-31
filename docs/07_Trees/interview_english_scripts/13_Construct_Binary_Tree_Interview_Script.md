# 13 Construct Binary Tree from Preorder and Inorder Traversal — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/13_Construct_Binary_Tree.md`

> Quick links: [Source Solution](../13_Construct_Binary_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the tree-construction problem. | 我先重述建樹題目。 | Restatement |
| We are given preorder and inorder arrays of the same tree. | 題目給同一棵樹的 preorder 與 inorder。 | Restatement |
| We need to reconstruct and return the binary-tree root. | 我們要重建並回傳該樹 root。 | Restatement |
| Preorder gives root first; inorder splits left and right subtrees. | preorder 先給 root；inorder 可切左右子樹。 | Restatement |
| Values are unique, so root index in inorder is unambiguous. | 值唯一，所以 root 在 inorder 的位置唯一。 | Restatement |
| I will use hash map plus recursion with index ranges. | 我會用 hash map 加遞迴索引範圍。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are preorder and inorder lengths always equal? | preorder 與 inorder 長度總是相等嗎？ | Clarify |
| Are all values guaranteed unique? | 所有值都保證唯一嗎？ | Clarify |
| Can I assume inputs are always valid representations? | 我可假設輸入一定可構成合法樹嗎？ | Clarify |
| Should I avoid array slicing for performance? | 是否要避免陣列切片以提升效能？ | Clarify |
| Is O(n) hashmap solution the expected target? | 目標是否是 O(n) 的 hashmap 解法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force finds root index in inorder by linear search every recursion. | 暴力法每層遞迴都線性搜尋 root 在 inorder 位置。 | Approach |
| It may also create sliced subarrays repeatedly. | 也常會反覆建立切片子陣列。 | Approach |
| This leads to O(n^2) time and extra copying overhead. | 會導致 O(n^2) 時間與拷貝成本。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build value-to-index hashmap for inorder first. | 先建立 inorder 的 value-to-index hashmap。 | Approach |
| Recursive function takes preorder start and inorder range. | 遞迴函式帶 preorder 起點與 inorder 範圍。 | Approach |
| Current preorder start gives root value directly. | 當前 preorder 起點直接就是 root 值。 | Approach |
| Inorder index gives left subtree size immediately. | 由 inorder 索引可立即得左子樹大小。 | Approach |
| Recurse left then right with adjusted indices, total O(n). | 依序遞迴左右並調整索引，總體 O(n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I first fill hashmap from inorder value to index. | 我先把 inorder 值映射到索引。 | Coding |
| I call build helper with preorder start zero and full inorder range. | 以 preorder 起點 0、完整 inorder 範圍呼叫 helper。 | Coding |
| Base case: if inorder start exceeds inorder end, return null. | base case：inStart 超過 inEnd 時回傳 null。 | Coding |
| Root value is preorder at preStart. | root 值是 preorder[preStart]。 | Coding |
| I create root node from that value. | 我用該值建立 root 節點。 | Coding |
| I find root index in inorder using hashmap. | 用 hashmap 找 root 在 inorder 的索引。 | Coding |
| Left subtree size is inIndex minus inStart. | 左子樹大小為 inIndex-inStart。 | Coding |
| I recurse left with preStart plus one and left inorder range. | 左遞迴用 preStart+1 與左側 inorder 範圍。 | Coding |
| I recurse right with shifted preStart and right inorder range. | 右遞迴用位移後 preStart 與右側 inorder 範圍。 | Coding |
| Return root after linking both subtrees. | 連接完左右子樹後回傳 root。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run preorder [3,9,20,15,7] and inorder [9,3,15,20,7]. | 我手跑 preorder [3,9,20,15,7] 與 inorder [9,3,15,20,7]。 | Dry-run |
| preStart zero gives root value 3. | preStart=0 得 root 值 3。 | Dry-run |
| Inorder index of 3 is one, so left subtree size is one. | 3 在 inorder 的索引是 1，左子樹大小為 1。 | Dry-run |
| Left call builds node 9 from preorder index one. | 左遞迴從 preorder 索引 1 建出節點 9。 | Dry-run |
| Right call starts at preorder index two and builds node 20. | 右遞迴從 preorder 索引 2 建出節點 20。 | Dry-run |
| Node 20 then builds left 15 and right 7 similarly. | 節點 20 再以同邏輯建立左 15 右 7。 | Dry-run |
| Final tree matches expected [3,9,20,null,null,15,7]. | 最終樹符合預期 [3,9,20,null,null,15,7]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single-node arrays should build one-node tree. | 案例一：單元素陣列應建出單節點樹。 | Edge test |
| Case two: all-left skewed traversal pair. | 案例二：全左斜的遍歷配對。 | Edge test |
| Case three: all-right skewed traversal pair. | 案例三：全右斜的遍歷配對。 | Edge test |
| Case four: balanced tree with both subtrees non-empty. | 案例四：左右子樹都非空的平衡樹。 | Edge test |
| Case five: maximum-size input checks recursion depth risk. | 案例五：大輸入需注意遞迴深度風險。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(n) for map plus recursion stack. | 空間複雜度是 O(n)（map+遞迴堆疊）。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We create each node once and process each value once. | 每個值只建立一次節點並處理一次。 | Complexity |
| Hashmap gives O(1) average lookup for inorder index. | hashmap 可 O(1) 平均查找 inorder 索引。 | Complexity |
| So total construction time is O(n). | 因此總建構時間為 O(n)。 | Complexity |
| Extra memory is hashmap O(n) plus recursion O(h). | 額外記憶體是 hashmap O(n) 加遞迴 O(h)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me anchor on traversal definitions first. | 我先回到遍歷定義本身。 | If stuck |
| Preorder first element of subtree is always its root. | 每棵子樹的 preorder 首值永遠是 root。 | If stuck |
| Inorder root position splits left and right regions. | inorder 的 root 位置可切左右區間。 | If stuck |
| I might have miscomputed right-subtree preStart offset. | 我可能算錯右子樹 preStart 位移。 | If stuck |
| Let me recompute it as preStart plus one plus leftSize. | 我改成 preStart+1+leftSize 重新計算。 | If stuck |
| I will rerun the [3,9,20,15,7] sample. | 我重跑 [3,9,20,15,7] 範例。 | If stuck |
| Left and right subtrees now align correctly. | 現在左右子樹切分正確。 | If stuck |
| I will also test single-node input. | 我再測單節點輸入。 | If stuck |
| Base case handling works properly. | base case 處理正常。 | If stuck |
| Great, index arithmetic is now stable. | 很好，索引運算已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed tree reconstruction from preorder and inorder. | 我完成了從 preorder/inorder 重建樹。 | Wrap-up |
| Hashmap lookup removes repeated inorder scans. | hashmap 查找消除了重複 inorder 掃描。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(n) including map and recursion stack. | 空間包含 map 與遞迴為 O(n)。 | Wrap-up |
| I can also discuss preIndex-global-pointer variant if needed. | 若需要我可補 preIndex 全域指標版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build tree from preorder and inorder. | 由 preorder/inorder 建樹。 | Cheat sheet |
| Preorder gives root first. | preorder 先給 root。 | Cheat sheet |
| Inorder splits left and right subtrees. | inorder 切分左右子樹。 | Cheat sheet |
| Precompute inorder index hashmap. | 預先建 inorder 索引 map。 | Cheat sheet |
| Use recursive helper with index ranges. | 遞迴 helper 帶索引範圍。 | Cheat sheet |
| Base: inStart > inEnd returns null. | base：inStart>inEnd 回 null。 | Cheat sheet |
| rootVal = preorder[preStart]. | rootVal = preorder[preStart]。 | Cheat sheet |
| inIndex = map[rootVal]. | inIndex = map[rootVal]。 | Cheat sheet |
| leftSize = inIndex - inStart. | leftSize = inIndex-inStart。 | Cheat sheet |
| Build left with preStart + 1. | 左子樹用 preStart+1。 | Cheat sheet |
| Build right with preStart + 1 + leftSize. | 右子樹用 preStart+1+leftSize。 | Cheat sheet |
| Link root->left and root->right. | 連接 root 左右子樹。 | Cheat sheet |
| Return root. | 回傳 root。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Test single-node arrays. | 測單節點陣列。 | Cheat sheet |
| Test skewed tree arrays. | 測斜樹陣列。 | Cheat sheet |
| Common bug: right preStart offset wrong. | 常見錯誤：右子樹 preStart 位移錯。 | Cheat sheet |
| Common bug: slicing arrays unnecessarily. | 常見錯誤：不必要陣列切片。 | Cheat sheet |
| Mention global preIndex alternative. | 可提 global preIndex 替代法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hashmap + recursive range split is preserved.
- No hallucinated constraints: ✅ Complexity and unique-value assumption align with source.
- Language simplicity: ✅ Concise interview-spoken script lines.
