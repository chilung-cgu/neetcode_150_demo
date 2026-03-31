# 15 Serialize and Deserialize Binary Tree — Interview English Script (C++)

> Source aligned with: `docs/07_Trees/15_Serialize_Deserialize_Binary_Tree.md`

> Quick links: [Source Solution](../15_Serialize_Deserialize_Binary_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the serialize-deserialize problem. | 我先重述序列化與反序列化題目。 | Restatement |
| We need two functions: serialize tree to string, and deserialize back. | 要實作兩個函式：樹轉字串、字串還原樹。 | Restatement |
| The exact text format is flexible as long as reconstruction is lossless. | 格式可自訂，但必須可無損還原。 | Restatement |
| Null children must be encoded explicitly. | null 子節點一定要明確編碼。 | Restatement |
| Deserialized tree should match original structure and values. | 還原後結構與值都要與原樹一致。 | Restatement |
| I will use preorder DFS with delimiter and null marker. | 我會用 preorder DFS + 分隔符 + null 標記。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is custom format acceptable if encode and decode are consistent? | 只要 encode/decode 一致，自訂格式可以嗎？ | Clarify |
| Can I use comma as delimiter and N as null marker? | 我可用逗號分隔、N 表示 null 嗎？ | Clarify |
| Should empty tree serialize to just N? | 空樹序列化成單一 N 可以嗎？ | Clarify |
| Is recursion depth acceptable under given node constraints? | 目前節點限制下遞迴深度可接受嗎？ | Clarify |
| Do you want BFS-format discussion as alternative? | 需要補充 BFS 格式替代法嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A naive format without null markers cannot uniquely recover structure. | 沒有 null 標記的簡單格式無法唯一還原結構。 | Approach |
| Different trees may produce same value order. | 不同樹可能產生相同值序列。 | Approach |
| So explicit null encoding is mandatory. | 因此必須明確編碼 null。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Serialize by preorder: node, left subtree, right subtree. | 以 preorder 序列化：節點、左子樹、右子樹。 | Approach |
| Append node value tokens and use N token for null nodes. | 非 null 存值 token，null 存 N token。 | Approach |
| Join tokens by comma into one string. | 以逗號串接成單一字串。 | Approach |
| For deserialize, split tokens and consume them in order with DFS. | 反序列化時切 token 並依序 DFS 消耗。 | Approach |
| Encountering N returns null; otherwise create node and recurse children. | 讀到 N 回 null；否則建節點並遞迴子節點。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| In serialize, if root is null, return N. | serialize 中若 root 為 null，回傳 N。 | Coding |
| Otherwise append root value, then serialize left and right recursively. | 否則先寫 root 值，再遞迴序列化左右。 | Coding |
| I separate each token by comma delimiter. | 每個 token 以逗號分隔。 | Coding |
| In deserialize, I split string into token queue. | deserialize 時先把字串切成 token queue。 | Coding |
| Helper pops one token each call. | helper 每次呼叫彈出一個 token。 | Coding |
| If token is N, return null immediately. | 若 token 是 N，立即回傳 null。 | Coding |
| Else create node from token value. | 否則由 token 值建立節點。 | Coding |
| Recurse to build left child then right child, then return node. | 依序建左再建右，最後回傳節點。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run tree [1,2,3,null,null,4,5]. | 我手跑樹 [1,2,3,null,null,4,5]。 | Dry-run |
| Preorder serialization yields tokens 1,2,N,N,3,4,N,N,5,N,N. | preorder 序列化得到 token：1,2,N,N,3,4,N,N,5,N,N。 | Dry-run |
| During deserialize, first token 1 becomes root node. | 反序列化時第一個 token 1 建成 root。 | Dry-run |
| Next token 2 builds left child, followed by two N leaves. | 下一個 token 2 建左子，後面兩個 N 補空葉。 | Dry-run |
| Token 3 builds right child of root. | token 3 建 root 的右子。 | Dry-run |
| Then 4 and 5 are built as children of node 3. | 接著 4、5 建成節點 3 的左右子。 | Dry-run |
| Reconstructed tree matches original structure exactly. | 重建樹與原始結構完全一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty tree serializes and deserializes correctly. | 案例一：空樹序列化與反序列化都正確。 | Edge test |
| Case two: single-node tree round-trip stays identical. | 案例二：單節點樹 round-trip 後保持一致。 | Edge test |
| Case three: skewed tree preserves null positions exactly. | 案例三：斜樹要精準保留 null 位置。 | Edge test |
| Case four: tree with negative values parses correctly. | 案例四：含負值節點要可正確解析。 | Edge test |
| Case five: mixed sparse tree validates token consumption order. | 案例五：稀疏樹驗證 token 消耗順序正確。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n) for both serialize and deserialize. | 序列化與反序列化時間都為 O(n)。 | Complexity |
| Space complexity is O(n) for tokens plus recursion. | token 儲存與遞迴整體空間為 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each real node and null marker is processed once. | 每個實節點與 null 標記都只處理一次。 | Complexity |
| Serialization visits all nodes in DFS order, O(n). | 序列化 DFS 走訪全部節點，為 O(n)。 | Complexity |
| Deserialization consumes each token once, also O(n). | 反序列化每個 token 只消耗一次，也是 O(n)。 | Complexity |
| Extra memory comes from token storage and recursion depth. | 額外記憶體來自 token 儲存與遞迴深度。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me verify format symmetry between serialize and deserialize. | 我先確認 encode/decode 格式完全對稱。 | If stuck |
| Token order must be exactly preorder in both directions. | token 順序在雙向都必須是 preorder。 | If stuck |
| I might have omitted null marker for missing child. | 我可能漏掉了缺子節點的 null 標記。 | If stuck |
| Missing null markers break unique reconstruction. | 少 null 標記會導致無法唯一還原。 | If stuck |
| Let me add explicit N markers and rerun. | 我補上明確 N 標記後重跑。 | If stuck |
| I will test sparse tree with many nulls now. | 我現在測試含大量 null 的稀疏樹。 | If stuck |
| Reconstruction now matches expected shape. | 還原出的形狀現在正確。 | If stuck |
| I also test empty tree serialization. | 我也測空樹序列化。 | If stuck |
| Empty tree round-trip works with token N. | 空樹用 token N 可正確往返。 | If stuck |
| Great, encode-decode contract is stable. | 很好，編解碼契約已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed preorder-based tree serialization and deserialization. | 我完成了基於 preorder 的序列化與反序列化。 | Wrap-up |
| Explicit null markers ensure lossless structure recovery. | 明確 null 標記可保證結構無損還原。 | Wrap-up |
| Time is O(n) for both operations. | 兩個操作時間皆為 O(n)。 | Wrap-up |
| Space is O(n) due to tokens and recursion. | 因 token 與遞迴，空間是 O(n)。 | Wrap-up |
| I can also compare this with BFS-based codec if needed. | 若需要我也可比較 BFS 版本 codec。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Implement serialize and deserialize for binary tree. | 實作二元樹 serialize / deserialize。 | Cheat sheet |
| Use preorder DFS format. | 使用 preorder DFS 格式。 | Cheat sheet |
| Use comma delimiter between tokens. | token 間用逗號分隔。 | Cheat sheet |
| Use N token for null nodes. | null 節點用 N token。 | Cheat sheet |
| Serialize null => N. | serialize null => N。 | Cheat sheet |
| Serialize node => val,left,right. | serialize 節點 => val,left,right。 | Cheat sheet |
| Deserialize by token queue/stream. | deserialize 用 token 佇列/串流。 | Cheat sheet |
| Pop token each recursive step. | 每次遞迴先彈一個 token。 | Cheat sheet |
| Token N => return null. | token N => 回 null。 | Cheat sheet |
| Else create node from value token. | 否則以值 token 建節點。 | Cheat sheet |
| Build left subtree recursively. | 遞迴建立左子樹。 | Cheat sheet |
| Build right subtree recursively. | 遞迴建立右子樹。 | Cheat sheet |
| Return reconstructed node. | 回傳重建節點。 | Cheat sheet |
| Round-trip should preserve exact shape. | round-trip 要保留完整形狀。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Test empty tree. | 測空樹。 | Cheat sheet |
| Test sparse tree with many nulls. | 測大量 null 的稀疏樹。 | Cheat sheet |
| Common bug: forgetting null marker. | 常見錯誤：漏 null 標記。 | Cheat sheet |
| Mention BFS codec as alternative. | 可提 BFS codec 替代法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Preorder DFS with null marker is preserved.
- No hallucinated constraints: ✅ Round-trip requirement and complexity align with source.
- Language simplicity: ✅ Concise spoken-style lines for interviews.
