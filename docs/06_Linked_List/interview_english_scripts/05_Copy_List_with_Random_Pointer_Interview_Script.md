# 05 Copy List with Random Pointer — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/05_Copy_List_with_Random_Pointer.md`

> Quick links: [Source Solution](../05_Copy_List_with_Random_Pointer.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate this deep-copy linked-list problem. | 我先重述這題深拷貝串列問題。 | Restatement |
| Each node has next and random pointers. | 每個節點有 next 與 random 指標。 | Restatement |
| I need a completely new list with identical structure. | 我要建立全新但結構完全相同的串列。 | Restatement |
| New nodes must not share addresses with original nodes. | 新舊節點記憶體位址不能共享。 | Restatement |
| Random links must point to copied targets, not old targets. | random 必須指向複製節點，不是舊節點。 | Restatement |
| I will use hash map old-node to new-node mapping first. | 我先用 hash map 做舊節點到新節點映射。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can input head be null? | 輸入 head 可能是 null 嗎？ | Clarify |
| Is O(n) extra space acceptable for main solution? | 主要解法可接受 O(n) 額外空間嗎？ | Clarify |
| Should random pointer possibly be null on any node? | 任一節點的 random 可能是 null 嗎？ | Clarify |
| Do we need to preserve exact node ordering by next chain? | next 鏈的節點順序需完全保留嗎？ | Clarify |
| Should I mention O(1) interleaving alternative as follow-up? | 要不要補充 O(1) 交錯法當延伸？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline is trying to resolve random targets by repeated scans. | 基線是每次用重掃方式找 random 目標。 | Approach |
| That means for each node we may walk list again. | 代表每個節點都可能再掃一次串列。 | Approach |
| Time can degrade to O(n^2). | 時間可能退化到 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First pass creates copy nodes and map entries. | 第一趟建立複製節點與映射。 | Approach |
| Map key is original node pointer, value is copied node pointer. | map 的 key 是舊節點指標，value 是新節點指標。 | Approach |
| Second pass assigns copied next and random via map lookups. | 第二趟透過 map 查表設定 next 與 random。 | Approach |
| Null pointers are handled by mapping null to null logic. | null 指標可用查表或條件判斷處理。 | Approach |
| Overall complexity is O(n) time and O(n) space. | 整體複雜度是 O(n) 時間、O(n) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, return null immediately if head is null. | 先判斷 head 為 null 就直接回傳 null。 | Coding |
| I create an unordered_map from old node to new node. | 建立 old node 到 new node 的 unordered_map。 | Coding |
| In first pass, for each old node I create a new node copy. | 第一趟對每個舊節點建立新節點副本。 | Coding |
| I store map[old] equals new copy. | 把 map[old] 設成對應新節點。 | Coding |
| In second pass, I set copy next to map[old next]. | 第二趟設定 copy->next = map[old->next]。 | Coding |
| I also set copy random to map[old random]. | 同時設定 copy->random = map[old->random]。 | Coding |
| This links copied graph without touching original links. | 這可連好新圖且不改動舊串列。 | Coding |
| Finally return map[head] as copied list head. | 最後回傳 map[head] 作為新 head。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run sample [[7,null],[13,0],[11,4],[10,2],[1,0]]. | 我手跑範例 [[7,null],[13,0],[11,4],[10,2],[1,0]]。 | Dry-run |
| First pass creates five copied nodes and map pairs. | 第一趟建立五個複製節點與 map 配對。 | Dry-run |
| For old node 13, random points to old node 7. | 舊節點 13 的 random 指向舊節點 7。 | Dry-run |
| So copied 13 random should point to copied 7 through map. | 所以新 13 的 random 要透過 map 指向新 7。 | Dry-run |
| For old node 11, random points to old node 1. | 舊節點 11 的 random 指向舊節點 1。 | Dry-run |
| Copied 11 random becomes copied 1 similarly. | 新 11 的 random 同理會指向新 1。 | Dry-run |
| Final copied structure matches original topology exactly. | 最終新串列拓樸與原串列完全一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty list input. | 案例一：空串列輸入。 | Edge test |
| Case two: single node with random null. | 案例二：單節點且 random 為 null。 | Edge test |
| Case three: single node random points to itself. | 案例三：單節點 random 指向自己。 | Edge test |
| Case four: multiple nodes with cross random pointers. | 案例四：多節點且 random 交叉指向。 | Edge test |
| Case five: all random pointers are null. | 案例五：所有 random 都是 null。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space is O(n) for node mapping. | 節點映射需要 O(n) 額外空間。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We traverse list twice, each pass is linear. | 我們遍歷兩趟串列，每趟都是線性。 | Complexity |
| Hash map operations are average O(1) each. | hash map 每次操作平均 O(1)。 | Complexity |
| One map entry is stored for every original node. | 每個舊節點都對應一個 map 項目。 | Complexity |
| Hence runtime O(n) and extra memory O(n). | 因此時間 O(n)、額外空間 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate node creation and pointer wiring phases. | 我先分離建節點與連指標兩階段。 | If stuck |
| First phase only builds map from old to new nodes. | 第一階段只建立 old->new map。 | If stuck |
| Second phase fills next and random using that map. | 第二階段再填 next 與 random。 | If stuck |
| I should never point new random to old nodes. | 新 random 絕不能指回舊節點。 | If stuck |
| I might have missed null handling in lookups. | 我可能漏處理 null 查表。 | If stuck |
| Let me guard null before map access. | 我在查表前先處理 null。 | If stuck |
| I rerun self-random and cross-random cases. | 我重跑自指與交叉 random 案例。 | If stuck |
| Now deep-copy addresses are fully separated. | 現在深拷貝位址已完全分離。 | If stuck |
| Structure and random topology both match. | 結構與 random 拓樸都匹配。 | If stuck |
| Great, solution is correct now. | 很好，解法現在正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished deep-copy implementation with hash map. | 我完成了 hash map 深拷貝實作。 | Wrap-up |
| I validated null, self-random, and cross-random cases. | 我驗證了 null、自指、交叉 random 案例。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Extra space is O(n). | 額外空間是 O(n)。 | Wrap-up |
| I can explain O(1) interleaving optimization if needed. | 若需要我可補充 O(1) 交錯優化法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Deep-copy list with next and random pointers. | 深拷貝含 next/random 的串列。 | Cheat sheet |
| New nodes must be independent addresses. | 新節點位址必須獨立。 | Cheat sheet |
| Baseline repeated-scan can be O(n^2). | 基線重掃可能是 O(n^2)。 | Cheat sheet |
| Better use old->new hash map. | 更好是 old->new hash map。 | Cheat sheet |
| Pass one: create all copied nodes. | 第一趟：建立全部新節點。 | Cheat sheet |
| Store mapping for each original node. | 存每個舊節點對應。 | Cheat sheet |
| Pass two: assign copy->next. | 第二趟：設定 copy->next。 | Cheat sheet |
| Pass two: assign copy->random. | 第二趟：設定 copy->random。 | Cheat sheet |
| Use map lookup for target copied node. | 用 map 查表找到目標新節點。 | Cheat sheet |
| Handle null pointers safely. | 安全處理 null 指標。 | Cheat sheet |
| Return map[head]. | 回傳 map[head]。 | Cheat sheet |
| Test empty input case. | 測空輸入案例。 | Cheat sheet |
| Test self-random case. | 測 random 指向自己的案例。 | Cheat sheet |
| Test cross-random case. | 測 random 交叉指向案例。 | Cheat sheet |
| Test all-random-null case. | 測全部 random 為 null。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Bug risk: linking new node to old random. | 風險：新節點誤指舊 random。 | Cheat sheet |
| Bug risk: missing null handling. | 風險：漏掉 null 處理。 | Cheat sheet |
| Follow-up: interleaving O(1) extra space. | 延伸：交錯法可 O(1) 額外空間。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hash-map deep-copy flow is preserved.
- No hallucinated constraints: ✅ Uses source random-pointer semantics.
- Language simplicity: ✅ Natural short lines for interview speaking.
