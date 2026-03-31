# 09 Binary Tree Right Side View — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/09_Binary_Tree_Right_Side_View.md`

> Quick links: [Source Solution](../09_Binary_Tree_Right_Side_View.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the right-side-view problem. | 我先重述右視圖題目。 | Restatement |
| We need nodes visible when looking from the tree's right side. | 要找從樹右側看得到的節點。 | Restatement |
| Output should list one value per depth level from top to bottom. | 輸出要由上到下，每層一個值。 | Restatement |
| Empty tree should return an empty list. | 空樹應回傳空陣列。 | Restatement |
| A common approach is BFS by level taking last node. | 常見做法是每層 BFS 取最後節點。 | Restatement |
| I will implement that straightforward queue solution. | 我會實作這個直觀 queue 解法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For each level, do we only keep one visible node value? | 每層只保留一個可見節點值嗎？ | Clarify |
| For null root, should return be empty vector? | root 為 null 是否回傳空 vector？ | Clarify |
| Is BFS preferred as primary implementation? | 主解法偏好 BFS 嗎？ | Clarify |
| Can I mention right-first DFS as an alternative? | 我可以補充右優先 DFS 替代法嗎？ | Clarify |
| Is left-to-right queue insertion required for BFS approach? | BFS 是否要採左到右入列順序？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A naive thought is rendering tree by coordinates then picking rightmost. | 直觀暴力可先做座標渲染再挑最右。 | Approach |
| That adds unnecessary geometry-style bookkeeping. | 這會增加不必要的座標管理成本。 | Approach |
| We can directly derive right view during traversal. | 其實遍歷過程就能直接取得右視圖。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use BFS level-order traversal with a queue. | 使用 queue 做 BFS 層序遍歷。 | Approach |
| For each level, record queue size upfront. | 每層先固定該層 queue 大小。 | Approach |
| Process exactly that many nodes. | 只處理固定數量的節點。 | Approach |
| The last processed node of that level is right-side visible. | 該層最後處理節點就是右視圖可見值。 | Approach |
| Append it to answer and continue until queue is empty. | 把它加入答案，重複直到 queue 為空。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize result vector for right-side values. | 我先建立 right-side 結果向量。 | Coding |
| If root is null, I return empty result. | 若 root 為 null，回傳空結果。 | Coding |
| I create queue and push root. | 建立 queue 並推入 root。 | Coding |
| While queue not empty, I process one level. | queue 非空時逐層處理。 | Coding |
| I store levelSize as current queue length. | 我把當前 queue 長度記為 levelSize。 | Coding |
| In loop, I pop one node each iteration. | 迴圈中每次彈出一個節點。 | Coding |
| If index equals levelSize minus one, record that node value. | 若索引等於 levelSize-1，記錄該值。 | Coding |
| Push left and right children when they exist. | 子節點存在時推入左右孩子。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run root [1,2,3,null,5,null,4]. | 我手跑 root [1,2,3,null,5,null,4]。 | Dry-run |
| Level one has node 1, so record 1. | 第一層只有節點 1，記錄 1。 | Dry-run |
| Level two has nodes 2 and 3, last one is 3. | 第二層有 2、3，最後是 3。 | Dry-run |
| Level three has nodes 5 and 4, last one is 4. | 第三層有 5、4，最後是 4。 | Dry-run |
| No more nodes remain in queue. | queue 已無剩餘節點。 | Dry-run |
| Collected right-side list is [1,3,4]. | 收集到的右視圖是 [1,3,4]。 | Dry-run |
| That matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty tree returns empty list. | 案例一：空樹回傳空陣列。 | Edge test |
| Case two: single-node tree returns that node only. | 案例二：單節點只回傳該節點。 | Edge test |
| Case three: left-skewed tree still returns all levels. | 案例三：左斜樹仍會回傳每層節點。 | Edge test |
| Case four: right-skewed tree returns path itself. | 案例四：右斜樹回傳整條路徑。 | Edge test |
| Case five: mixed missing children tests level-last logic. | 案例五：缺子節點混合測試每層最後節點邏輯。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(n) in worst width. | 最壞寬度下空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| BFS visits every node exactly once. | BFS 對每個節點恰好訪問一次。 | Complexity |
| Per node operations are constant-time queue actions. | 每節點僅做常數時間 queue 操作。 | Complexity |
| Queue size can grow to maximum tree width. | queue 大小可成長到樹的最大寬度。 | Complexity |
| In a wide level, that worst-case width is O(n). | 在最寬層下，最壞寬度為 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me lock the per-level boundary first. | 我先鎖定每層邊界處理。 | If stuck |
| I should read levelSize before loop starts. | 我應在迴圈前先讀 levelSize。 | If stuck |
| Then process exactly levelSize pops. | 接著精準彈出 levelSize 次。 | If stuck |
| I might have used queue size dynamically inside loop. | 我可能在迴圈中誤用動態 queue 大小。 | If stuck |
| Let me fix that and rerun sample. | 我修正後重跑範例。 | If stuck |
| Now each level contributes one rightmost value. | 現在每層都能產生一個最右值。 | If stuck |
| I will test left-skewed tree too. | 我也測左斜樹。 | If stuck |
| It still gives one value per depth. | 仍正確每層產生一個值。 | If stuck |
| I will test empty root quickly. | 我快速測空 root。 | If stuck |
| Empty case returns empty list correctly. | 空案例可正確回傳空陣列。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed BFS right-side-view extraction. | 我完成了 BFS 右視圖擷取。 | Wrap-up |
| The key step is taking last node of each level. | 核心步驟是每層取最後節點。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Space is O(n) in worst-case width. | 最壞寬度下空間是 O(n)。 | Wrap-up |
| I can also explain right-first DFS variant if needed. | 若需要我也可解釋右優先 DFS 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Return visible nodes from right side. | 回傳從右側可見節點。 | Cheat sheet |
| One value per depth level. | 每層只留一個值。 | Cheat sheet |
| Use queue BFS. | 使用 queue BFS。 | Cheat sheet |
| Null root => empty list. | null root => 空陣列。 | Cheat sheet |
| Push root first. | 先推入 root。 | Cheat sheet |
| While queue non-empty, process level. | queue 非空就處理一層。 | Cheat sheet |
| Snapshot levelSize before loop. | 迴圈前先固定 levelSize。 | Cheat sheet |
| Pop nodes levelSize times. | 彈出節點共 levelSize 次。 | Cheat sheet |
| If i == levelSize-1, record value. | 若 i==levelSize-1 就記錄值。 | Cheat sheet |
| Push left child if exists. | 有左子就推入。 | Cheat sheet |
| Push right child if exists. | 有右子就推入。 | Cheat sheet |
| Append one value per level. | 每層附加一個值。 | Cheat sheet |
| Continue to next level. | 前進下一層。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Test empty tree. | 測空樹。 | Cheat sheet |
| Test skewed trees. | 測斜樹。 | Cheat sheet |
| Common bug: not fixing level boundary. | 常見錯誤：層邊界沒固定。 | Cheat sheet |
| Common bug: taking first not last node. | 常見錯誤：誤取第一個非最後一個。 | Cheat sheet |
| Mention DFS right-first alternative. | 可補 DFS 右優先替代法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Level-order BFS taking each level's last node is preserved.
- No hallucinated constraints: ✅ Matches source examples and complexity.
- Language simplicity: ✅ Interview-spoken concise lines.
