# 03 Diameter of Binary Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/03_Diameter_of_Binary_Tree.md`

> Quick links: [Source Solution](../03_Diameter_of_Binary_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the diameter-of-binary-tree problem. | 我先重述二元樹直徑題。 | Restatement |
| We need the longest path between any two nodes. | 目標是任兩節點間最長路徑。 | Restatement |
| Diameter is counted by number of edges, not nodes. | 直徑以邊數計算，不是節點數。 | Restatement |
| This longest path may or may not pass through root. | 最長路徑不一定會經過 root。 | Restatement |
| We return one integer: the maximum edge length. | 回傳一個整數：最大邊長。 | Restatement |
| I will use one-pass bottom-up DFS. | 我會用一次遍歷的 bottom-up DFS。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Just to confirm, diameter means edge count here? | 再確認一次，直徑是算邊數嗎？ | Clarify |
| Can the longest path start and end at any nodes? | 最長路徑端點可為任意節點嗎？ | Clarify |
| Is empty tree possible, or at least one node guaranteed? | 會有空樹嗎，還是至少一個節點？ | Clarify |
| Is recursion acceptable under current constraints? | 目前限制下可用遞迴嗎？ | Clarify |
| May I keep a class-level variable for best diameter? | 我可用類別層級變數記錄最大直徑嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force treats each node as the path turning point. | 暴力法把每個節點當作路徑轉折點。 | Approach |
| For each node, compute left height and right height separately. | 對每節點分別算左右子樹高度。 | Approach |
| Recomputing heights repeatedly causes O(n^2) worst-case time. | 高度重算會造成最壞 O(n^2) 時間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use post-order DFS that returns subtree height. | 用後序 DFS 回傳子樹高度。 | Approach |
| At each node, get left and right heights once. | 每個節點只取一次左右高度。 | Approach |
| Candidate diameter through this node is left plus right. | 經過該節點的候選直徑是 left+right。 | Approach |
| Update global best diameter during traversal. | 在遍歷中即時更新全域最佳直徑。 | Approach |
| Return one plus max height upward, giving O(n) and O(h). | 向上回傳 1+max，高效達 O(n)、O(h)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize a global diameter variable to zero. | 我先把全域 diameter 初始化為 0。 | Coding |
| I write helper height function for DFS. | 我寫一個 helper height 做 DFS。 | Coding |
| Base case: null node returns zero height. | base case：null 節點回傳高度 0。 | Coding |
| I recursively compute left subtree height. | 遞迴計算左子樹高度。 | Coding |
| I recursively compute right subtree height. | 遞迴計算右子樹高度。 | Coding |
| I update diameter with leftHeight plus rightHeight. | 用 leftHeight+rightHeight 更新直徑。 | Coding |
| I return one plus max of both heights. | 回傳 1+max(左右高度)。 | Coding |
| Main function runs helper on root and returns diameter. | 主函式呼叫 helper 後回傳 diameter。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run tree [1,2,3,4,5]. | 我手跑樹 [1,2,3,4,5]。 | Dry-run |
| Node 4 and node 5 are leaves, each height is one. | 節點 4 與 5 為葉節點，高度都為 1。 | Dry-run |
| At node 2, left and right heights are one and one. | 到節點 2，左右高度分別為 1 與 1。 | Dry-run |
| So candidate diameter at node 2 is two edges. | 所以節點 2 的候選直徑是 2 條邊。 | Dry-run |
| Node 3 is leaf, height one. | 節點 3 是葉節點，高度為 1。 | Dry-run |
| At node 1, heights are two and one, candidate is three. | 在節點 1，高度是 2 與 1，候選為 3。 | Dry-run |
| Final diameter is three edges, matching expected output. | 最終直徑是 3 條邊，符合預期。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single-node tree should return zero. | 案例一：單節點樹應回傳 0。 | Edge test |
| Case two: root with one child should return one. | 案例二：root 只有一個子節點回傳 1。 | Edge test |
| Case three: skewed chain of n nodes returns n minus one. | 案例三：長鏈 n 節點回傳 n-1。 | Edge test |
| Case four: perfect binary tree checks cross-root path. | 案例四：完美樹要驗證跨 root 路徑。 | Edge test |
| Case five: irregular tree where max path avoids root. | 案例五：最長路徑不經 root 的不規則樹。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) for recursion stack. | 空間複雜度是 O(h) 遞迴堆疊。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each node is visited once in post-order DFS. | 後序 DFS 對每個節點只訪問一次。 | Complexity |
| Per node work is constant: two heights and one max update. | 每節點工作是常數：兩高度與一次更新。 | Complexity |
| Stack depth equals tree height h. | 堆疊深度等於樹高 h。 | Complexity |
| Worst skew is O(n) stack, balanced tree is O(log n). | 最壞斜樹 O(n)，平衡樹 O(log n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me verify the metric first: edges, not nodes. | 我先確認度量：算邊不是算節點。 | If stuck |
| I should separate height from diameter conceptually. | 我應把高度與直徑概念分開。 | If stuck |
| Height is what helper returns to parent. | 高度是 helper 回給父節點的值。 | If stuck |
| Diameter is global best from left plus right. | 直徑是全域 left+right 的最大值。 | If stuck |
| I may have forgotten global update at each node. | 我可能漏掉每節點更新全域值。 | If stuck |
| Let me add that update before returning height. | 我先補上更新，再回傳高度。 | If stuck |
| I will rerun sample [1,2,3,4,5]. | 我重跑範例 [1,2,3,4,5]。 | If stuck |
| Now I get diameter three correctly. | 現在正確得到直徑 3。 | If stuck |
| I will also test single-node returning zero. | 我再測單節點回傳 0。 | If stuck |
| Great, logic is now consistent. | 很好，邏輯現在一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished one-pass DFS diameter solution. | 我完成一次遍歷 DFS 直徑解法。 | Wrap-up |
| I validated root-crossing and non-root-crossing paths. | 我驗證了經過與不經過 root 的路徑情境。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h) from recursion stack. | 空間是 O(h) 來自遞迴堆疊。 | Wrap-up |
| I can provide iterative discussion if you want. | 若需要我可補充迭代思路比較。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Diameter means longest path between any two nodes. | 直徑是任兩節點最長路徑。 | Cheat sheet |
| Count diameter in edges. | 直徑以邊數計。 | Cheat sheet |
| Path may not pass root. | 路徑不一定經過 root。 | Cheat sheet |
| Brute force recomputes height repeatedly. | 暴力法會重算高度。 | Cheat sheet |
| Brute force worst time O(n^2). | 暴力最壞時間 O(n^2)。 | Cheat sheet |
| Use post-order DFS helper for height. | 用後序 DFS helper 算高度。 | Cheat sheet |
| Base case null returns 0. | base case：null 回傳 0。 | Cheat sheet |
| left = dfs(node->left). | left = dfs(node->left)。 | Cheat sheet |
| right = dfs(node->right). | right = dfs(node->right)。 | Cheat sheet |
| Update best with left + right. | 用 left+right 更新最佳值。 | Cheat sheet |
| Return 1 + max(left, right). | 回傳 1+max(left,right)。 | Cheat sheet |
| Initialize diameter to 0. | diameter 初始值設 0。 | Cheat sheet |
| Run helper on root. | 對 root 執行 helper。 | Cheat sheet |
| Return diameter at end. | 最後回傳 diameter。 | Cheat sheet |
| Test single-node tree => 0. | 測單節點 => 0。 | Cheat sheet |
| Test two-node tree => 1. | 測兩節點 => 1。 | Cheat sheet |
| Test skewed tree chain. | 測斜樹長鏈。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(h). | 空間 O(h)。 | Cheat sheet |
| Common bug: mixing edge count and node count. | 常見錯誤：邊數與節點數混淆。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Bottom-up DFS + global diameter update is preserved.
- No hallucinated constraints: ✅ Uses source definition (edge-based diameter).
- Language simplicity: ✅ Spoken and concise interview-ready lines.
