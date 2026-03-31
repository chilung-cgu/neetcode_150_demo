# 05 Same Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/05_Same_Tree.md`

> Quick links: [Source Solution](../05_Same_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the same-tree problem. | 我先重述相同樹題目。 | Restatement |
| We are given two binary trees p and q. | 題目給兩棵二元樹 p 與 q。 | Restatement |
| We need to check whether they are exactly identical. | 要判斷它們是否完全一致。 | Restatement |
| Identical means same structure and same node values. | 一致代表結構相同且節點值相同。 | Restatement |
| If one side is null while the other is not, answer is false. | 一邊為 null 另一邊非 null 就是 false。 | Restatement |
| I will use synchronized recursive DFS. | 我會使用同步遞迴 DFS。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume both roots may be null? | 我可假設兩個 root 都可能是 null 嗎？ | Clarify |
| Is exact structural equality required at every position? | 每個位置都要完全結構相等嗎？ | Clarify |
| Node values can be compared directly as integers, right? | 節點值可直接以整數比較對嗎？ | Clarify |
| Do you prefer recursive DFS as the primary solution? | 主解法偏好遞迴 DFS 嗎？ | Clarify |
| Should I mention iterative queue comparison as an alternative? | 要補充迭代 queue 比較法嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A straightforward way is traversing both trees level by level. | 直觀作法是兩樹同步層序遍歷。 | Approach |
| At each pair, compare null-state and value. | 每對節點都比 null 狀態與數值。 | Approach |
| This is valid but needs explicit queue bookkeeping. | 這可行，但要額外 queue 管理細節。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Recursive DFS is cleaner for structural matching. | 遞迴 DFS 對結構比對更乾淨。 | Approach |
| If both nodes are null, return true. | 兩節點都 null 時回傳 true。 | Approach |
| If only one is null, return false. | 只有一邊 null 就回傳 false。 | Approach |
| If values differ, return false immediately. | 值不同就立即回傳 false。 | Approach |
| Otherwise recurse on left pair and right pair with AND. | 否則左右配對遞迴並用 AND 合併。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I start helper isSameTree with nodes p and q. | 我以節點 p、q 開始 helper。 | Coding |
| If both are null, I return true. | 若兩者都 null，回傳 true。 | Coding |
| If one is null and the other is not, I return false. | 若僅一邊 null，回傳 false。 | Coding |
| If p value differs from q value, return false. | 若 p 值與 q 值不同，回傳 false。 | Coding |
| I recursively compare p left with q left. | 遞迴比較 p.left 與 q.left。 | Coding |
| I recursively compare p right with q right. | 遞迴比較 p.right 與 q.right。 | Coding |
| I return logical AND of the two subtree checks. | 回傳兩個子樹結果的 AND。 | Coding |
| This bubbles up to final true or false at roots. | 逐層回傳到 root 得到最終真假。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run p=[1,2,3] and q=[1,2,3]. | 我手跑 p=[1,2,3]、q=[1,2,3]。 | Dry-run |
| Compare roots 1 and 1, values match. | 比較根節點 1 與 1，值相同。 | Dry-run |
| Recurse left: 2 and 2, still match. | 遞迴左側：2 與 2，仍相同。 | Dry-run |
| Recurse right: 3 and 3, still match. | 遞迴右側：3 與 3，仍相同。 | Dry-run |
| Children of leaves are null on both sides. | 葉節點子節點兩邊都為 null。 | Dry-run |
| Null pairs return true all the way up. | null 配對一路回傳 true。 | Dry-run |
| Final result is true. | 最終結果為 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: both trees null should return true. | 案例一：兩棵都 null 應回傳 true。 | Edge test |
| Case two: one null and one non-null should return false. | 案例二：一棵 null 一棵非 null 應回傳 false。 | Edge test |
| Case three: same structure but one value differs. | 案例三：結構相同但某個值不同。 | Edge test |
| Case four: same values but different structure. | 案例四：值看似相同但結構不同。 | Edge test |
| Case five: deep skewed trees that are identical. | 案例五：深度斜樹但兩邊完全相同。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(h) from recursion depth. | 空間複雜度是 O(h) 遞迴深度。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We compare each corresponding node pair at most once. | 每個對應節點配對最多比較一次。 | Complexity |
| Per comparison is constant-time null and value checks. | 每次比較是常數時間 null 與值檢查。 | Complexity |
| Recursion stack depends on tree height h. | 遞迴堆疊取決於樹高 h。 | Complexity |
| Worst skew gives O(n) stack; balanced gives O(log n). | 最壞斜樹 O(n)，平衡樹 O(log n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me enforce the base-case order carefully. | 我先嚴格確認 base-case 順序。 | If stuck |
| First check both-null true condition. | 先檢查兩邊都 null 的 true。 | If stuck |
| Then check one-null false condition. | 再檢查單邊 null 的 false。 | If stuck |
| Then compare node values. | 接著比較節點值。 | If stuck |
| I might have merged null checks incorrectly. | 我可能把 null 判斷合併錯了。 | If stuck |
| Let me split them explicitly and rerun. | 我把它拆開後重跑。 | If stuck |
| I will test structure-mismatch sample now. | 我現在測結構不一致範例。 | If stuck |
| It now returns false correctly. | 現在可正確回傳 false。 | If stuck |
| I will test identical sample again. | 我再測一次完全相同範例。 | If stuck |
| Great, both outcomes are correct. | 很好，兩種結果都正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed synchronized DFS tree comparison. | 我完成同步 DFS 的樹比較。 | Wrap-up |
| The solution validates both structure and value equality. | 解法同時驗證結構與值相等。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(h). | 空間複雜度是 O(h)。 | Wrap-up |
| I can provide iterative queue version if needed. | 若需要我可補充迭代 queue 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Compare two binary trees for exact equality. | 比較兩棵樹是否完全相同。 | Cheat sheet |
| Equality needs same structure and values. | 相同需結構與值都一致。 | Cheat sheet |
| Use recursive synchronized DFS. | 使用同步遞迴 DFS。 | Cheat sheet |
| Base case: both null => true. | base case：兩邊 null => true。 | Cheat sheet |
| Base case: one null => false. | base case：單邊 null => false。 | Cheat sheet |
| Value mismatch => false. | 值不相同 => false。 | Cheat sheet |
| Recurse on left children pair. | 遞迴比左子節點配對。 | Cheat sheet |
| Recurse on right children pair. | 遞迴比右子節點配對。 | Cheat sheet |
| Return leftResult AND rightResult. | 回傳 leftResult AND rightResult。 | Cheat sheet |
| Touch each pair once. | 每組配對只處理一次。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(h). | 空間 O(h)。 | Cheat sheet |
| Test both-null case. | 測兩邊都 null。 | Cheat sheet |
| Test one-null case. | 測單邊 null。 | Cheat sheet |
| Test value mismatch case. | 測值不相同案例。 | Cheat sheet |
| Test structure mismatch case. | 測結構不一致案例。 | Cheat sheet |
| Common bug: wrong base-case order. | 常見錯誤：base-case 順序錯。 | Cheat sheet |
| Common bug: forgetting one-null check. | 常見錯誤：漏單邊 null 判斷。 | Cheat sheet |
| Mention iterative BFS alternative. | 可補充迭代 BFS 替代法。 | Cheat sheet |
| End by stating exact-match requirement. | 收尾再強調「完全匹配」要求。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Recursive exact-structure-and-value check is preserved.
- No hallucinated constraints: ✅ Matches source definition and constraints.
- Language simplicity: ✅ Short spoken lines for interview delivery.
