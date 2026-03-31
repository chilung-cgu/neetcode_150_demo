# 06 Subtree of Another Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/06_Subtree_of_Another_Tree.md`

> Quick links: [Source Solution](../06_Subtree_of_Another_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the subtree problem. | 我先重述子樹判定題。 | Restatement |
| We are given root and subRoot binary trees. | 題目給 root 與 subRoot 兩棵樹。 | Restatement |
| We need to decide whether subRoot appears as a complete subtree in root. | 要判斷 subRoot 是否完整出現在 root 中。 | Restatement |
| Match must include both structure and node values. | 比對必須同時符合結構與節點值。 | Restatement |
| Partial overlap is not enough; it must be exact. | 部分重疊不算，必須完整相等。 | Restatement |
| I will combine tree traversal with same-tree checking. | 我會結合遍歷與 same-tree 檢查。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If subRoot is null, should answer be true? | 若 subRoot 為 null，答案是否為 true？ | Clarify |
| If root is null but subRoot is not, should answer be false? | 若 root 為 null 且 subRoot 非 null，是否 false？ | Clarify |
| Is recursive DFS acceptable for constraints up to two thousand nodes? | 節點到兩千時可用遞迴 DFS 嗎？ | Clarify |
| Do you want the standard O(m*n) matcher first? | 你希望先給標準 O(m*n) 解法嗎？ | Clarify |
| Should I briefly mention hashing/serialization optimization later? | 後面要簡提 hash/序列化優化嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force compares subRoot at every node in root. | 暴力法是在 root 每個節點嘗試比對 subRoot。 | Approach |
| Each comparison may scan all nodes in subRoot via isSameTree. | 每次比對可能掃完整個 subRoot。 | Approach |
| So worst-case time is O(m*n). | 所以最壞時間是 O(m*n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We still use DFS over root, but with clean early exits. | 我們仍 DFS 遍歷 root，但加上明確提早返回。 | Approach |
| Base case: empty subRoot always returns true. | base case：subRoot 為空一定 true。 | Approach |
| Base case: empty root with non-empty subRoot returns false. | base case：root 空且 subRoot 非空為 false。 | Approach |
| At each node, first run isSameTree(root, subRoot). | 每個節點先跑 isSameTree(root, subRoot)。 | Approach |
| If not matched, recurse to left or right child. | 若不匹配，再遞迴左或右子樹。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| In isSubtree, if subRoot is null, return true. | 在 isSubtree 中，subRoot 為 null 回傳 true。 | Coding |
| If root is null while subRoot exists, return false. | 若 root 為 null 但 subRoot 存在，回傳 false。 | Coding |
| I call isSameTree on current root and subRoot. | 我先對當前 root 與 subRoot 呼叫 isSameTree。 | Coding |
| If they match, return true immediately. | 若兩者匹配，立即回傳 true。 | Coding |
| Otherwise recurse on root left subtree. | 否則遞迴 root 左子樹。 | Coding |
| Also recurse on root right subtree. | 也遞迴 root 右子樹。 | Coding |
| Return logical OR of the two subtree checks. | 回傳左右結果的 OR。 | Coding |
| In isSameTree, compare null states, values, then children. | isSameTree 內依序比 null、值、子樹。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [3,4,5,1,2] and subRoot [4,1,2]. | 我手跑 root [3,4,5,1,2] 與 subRoot [4,1,2]。 | Dry-run |
| Start at node 3: isSameTree(3,4) fails by value. | 從節點 3 開始：isSameTree(3,4) 因值不同失敗。 | Dry-run |
| Recurse to left child node 4. | 遞迴到左子節點 4。 | Dry-run |
| isSameTree(4,4) checks children 1 and 2, both match. | isSameTree(4,4) 比對子節點 1、2 都匹配。 | Dry-run |
| All corresponding null children also match. | 對應的 null 子節點也都一致。 | Dry-run |
| Current call returns true and bubbles up. | 當前呼叫回傳 true 並向上傳遞。 | Dry-run |
| Final answer is true. | 最終答案為 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: subRoot is null should return true. | 案例一：subRoot 為 null 應回傳 true。 | Edge test |
| Case two: root is null and subRoot non-null should return false. | 案例二：root 為 null 且 subRoot 非 null 應回傳 false。 | Edge test |
| Case three: same values but extra child in root branch should fail. | 案例三：值相同但 root 多出子節點應失敗。 | Edge test |
| Case four: subRoot equals entire root should return true. | 案例四：subRoot 等於整棵 root 應回傳 true。 | Edge test |
| Case five: repeated values requiring strict structure matching. | 案例五：重複值場景要嚴格結構比對。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(m*n) in worst case. | 最壞時間複雜度是 O(m*n)。 | Complexity |
| Space complexity is O(m) recursion depth in worst skew. | 最壞斜樹下空間複雜度是 O(m) 遞迴深度。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Outer DFS may visit each of m nodes in root. | 外層 DFS 可能訪問 root 的 m 個節點。 | Complexity |
| For each candidate node, isSameTree may scan up to n nodes. | 每個候選點的 isSameTree 最多掃 n 節點。 | Complexity |
| Multiplying gives O(m*n) worst-case time. | 兩者相乘得最壞 O(m*n) 時間。 | Complexity |
| Recursion stack follows root height, worst-case O(m). | 遞迴堆疊隨 root 高度，最壞 O(m)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate two functions: isSubtree and isSameTree. | 我先分清兩個函式：isSubtree 與 isSameTree。 | If stuck |
| isSubtree decides where to try matching. | isSubtree 負責決定在哪裡嘗試匹配。 | If stuck |
| isSameTree decides exact equality at one candidate root. | isSameTree 負責某候選點的完全相等判定。 | If stuck |
| I might have skipped the subRoot-null base case. | 我可能漏了 subRoot-null 的 base case。 | If stuck |
| Let me add it and rerun edge tests. | 我補上後重跑邊界測試。 | If stuck |
| I will test false sample with extra node zero. | 我測 false 範例（多一個節點 0）。 | If stuck |
| It correctly returns false now. | 現在能正確回傳 false。 | If stuck |
| I will test exact-match sample again. | 我再測一次完整匹配範例。 | If stuck |
| It returns true as expected. | 結果如預期回傳 true。 | If stuck |
| Great, recursion logic is now stable. | 很好，遞迴邏輯已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed subtree detection with DFS plus exact tree matcher. | 我完成了 DFS + 完整樹比對的子樹判定。 | Wrap-up |
| The solution handles null-base cases explicitly. | 此解法明確處理了 null base cases。 | Wrap-up |
| Runtime is O(m*n) worst case. | 最壞時間是 O(m*n)。 | Wrap-up |
| Space is O(m) in skewed-tree recursion depth. | 空間在斜樹情況為 O(m)。 | Wrap-up |
| I can discuss serialization optimization if needed. | 若需要我可再談序列化優化。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Determine whether subRoot is a subtree of root. | 判斷 subRoot 是否為 root 子樹。 | Cheat sheet |
| Matching needs exact structure and values. | 匹配需結構與值完全相同。 | Cheat sheet |
| Use two helpers: isSubtree and isSameTree. | 用兩個函式：isSubtree 與 isSameTree。 | Cheat sheet |
| Base: subRoot null => true. | base：subRoot null => true。 | Cheat sheet |
| Base: root null and subRoot not null => false. | base：root null 且 subRoot 非 null => false。 | Cheat sheet |
| At each root node, run isSameTree first. | 在每個 root 節點先跑 isSameTree。 | Cheat sheet |
| If match, return true immediately. | 若匹配，立即回傳 true。 | Cheat sheet |
| Else recurse into left subtree. | 否則遞迴左子樹。 | Cheat sheet |
| Else recurse into right subtree. | 再遞迴右子樹。 | Cheat sheet |
| Return left OR right result. | 回傳 left OR right。 | Cheat sheet |
| isSameTree both null => true. | isSameTree：兩邊 null => true。 | Cheat sheet |
| isSameTree one null => false. | isSameTree：單邊 null => false。 | Cheat sheet |
| Value mismatch => false. | 值不同 => false。 | Cheat sheet |
| Recurse children with AND. | 子樹遞迴結果用 AND。 | Cheat sheet |
| Worst time O(m*n). | 最壞時間 O(m*n)。 | Cheat sheet |
| Worst space O(m). | 最壞空間 O(m)。 | Cheat sheet |
| Test case: exact subtree exists => true. | 測例：存在完整子樹 => true。 | Cheat sheet |
| Test case: extra child breaks match => false. | 測例：多子節點破壞匹配 => false。 | Cheat sheet |
| Common bug: forgetting null base cases. | 常見錯誤：漏掉 null base cases。 | Cheat sheet |
| Optional: mention hash/serialization optimization. | 可補充 hash/序列化優化。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS traversal + `isSameTree` matching is preserved.
- No hallucinated constraints: ✅ Complexity and base cases follow source chapter.
- Language simplicity: ✅ Natural interview-spoken short lines.
