# 08 Find the Duplicate Number — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/08_Find_the_Duplicate_Number.md`

> Quick links: [Source Solution](../08_Find_the_Duplicate_Number.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the duplicate-number problem. | 我先重述找重複數字題。 | Restatement |
| Array length is n plus one, values are in range one to n. | 陣列長度是 n+1，值域在 1 到 n。 | Restatement |
| Exactly one value repeats at least twice. | 恰有一個值重複出現至少兩次。 | Restatement |
| We cannot modify the input array. | 我們不能修改輸入陣列。 | Restatement |
| Extra space must stay O(1). | 額外空間必須是 O(1)。 | Restatement |
| I will map it to cycle detection and use Floyd algorithm. | 我會映射成環偵測並用 Floyd 演算法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume there is always at least one duplicate? | 我可假設一定至少有一個重複值嗎？ | Clarify |
| Are values guaranteed within closed interval one to n? | 值是否保證落在 1 到 n 區間？ | Clarify |
| Is input strictly read-only in interview expectation? | 面試預期是否視為唯讀輸入？ | Clarify |
| Should I avoid sorting because it mutates array? | 是否應避免排序，因為會改動陣列？ | Clarify |
| Do you want binary-search-on-value as alternative discussion? | 要不要補充值域二分替代法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline counts occurrences for each candidate value. | 基線是對每個候選值統計出現次數。 | Approach |
| That needs nested scanning over values and array. | 這需要對值域與陣列做巢狀掃描。 | Approach |
| Time O(n^2), space O(1), but too slow. | 時間 O(n^2)、空間 O(1)，但太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Treat index as node and nums[index] as next pointer. | 把索引視為節點，nums[index] 視為 next。 | Approach |
| This forms a functional graph with a cycle. | 這會形成函數圖且必有環。 | Approach |
| Repeated number corresponds to cycle entry. | 重複數字對應環入口。 | Approach |
| Phase one finds intersection of slow and fast pointers. | 第一階段找 slow 與 fast 的相遇點。 | Approach |
| Phase two finds entry, which is duplicate value. | 第二階段找入口，入口就是重複值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I initialize slow and fast to index zero. | 先把 slow 與 fast 都設在索引 0。 | Coding |
| I run do-while: slow moves one step, fast moves two steps. | 用 do-while：slow 一步、fast 兩步。 | Coding |
| Loop until slow equals fast at intersection. | 直到 slow 與 fast 在相遇點重合。 | Coding |
| Then I set a second pointer to index zero. | 接著把第二指標設回索引 0。 | Coding |
| I move both pointers one step each time. | 讓兩個指標每次都走一步。 | Coding |
| Their meeting point is cycle entry. | 再次相遇點就是環入口。 | Coding |
| That entry value is the duplicate number. | 該入口值即為重複數字。 | Coding |
| Return that value directly. | 直接回傳該值。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [1,3,4,2,2]. | 我手跑 nums=[1,3,4,2,2]。 | Dry-run |
| Start slow and fast at index zero. | 起始 slow 與 fast 在索引 0。 | Dry-run |
| Phase one eventually meets at index value 2 cycle region. | 第一階段最終會在值為 2 的環區域相遇。 | Dry-run |
| Reset second pointer to zero for phase two. | 第二階段把另一指標重設到 0。 | Dry-run |
| Move both one step each; they meet at value 2. | 兩者同步一步前進後在值 2 相遇。 | Dry-run |
| So duplicate number is 2. | 所以重複數字是 2。 | Dry-run |
| Result matches expected output. | 結果符合預期輸出。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: smallest valid n with one duplicate. | 案例一：最小合法 n 且有一個重複值。 | Edge test |
| Case two: duplicate appears many times. | 案例二：同一重複值出現多次。 | Edge test |
| Case three: duplicate equals lower bound one. | 案例三：重複值是下界 1。 | Edge test |
| Case four: duplicate equals upper bound n. | 案例四：重複值是上界 n。 | Edge test |
| Case five: duplicate appears near end positions. | 案例五：重複值出現在靠尾端位置。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Floyd phase one reaches intersection in linear steps. | Floyd 第一階段在線性步數內到達相遇點。 | Complexity |
| Phase two reaches cycle entry also in linear bound. | 第二階段也在線性上界內到達入口。 | Complexity |
| Only fixed pointers are maintained. | 全程只維護固定數量指標。 | Complexity |
| No array modification and no extra containers are needed. | 不改陣列，也不需額外容器。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me re-explain the index-to-pointer mapping first. | 我先重講索引到指標的映射。 | If stuck |
| Node i points to node nums[i]. | 節點 i 指向節點 nums[i]。 | If stuck |
| Because values are one to n, mapping is always valid. | 因值域 1 到 n，映射一定有效。 | If stuck |
| Duplicate value creates converging edges and a cycle entry. | 重複值會造成匯入邊與環入口。 | If stuck |
| I might have mixed index and value in pointer updates. | 我可能把索引與值更新混淆了。 | If stuck |
| Let me use slow = nums[slow], fast = nums[nums[fast]]. | 我改回 slow=nums[slow]、fast=nums[nums[fast]]。 | If stuck |
| Then reset second pointer to zero for phase two. | 然後第二階段把另一指標重設為 0。 | If stuck |
| Move both one step to find entry. | 兩者同速前進找入口。 | If stuck |
| Now sample returns expected duplicate. | 現在範例回傳預期重複值。 | If stuck |
| Great, logic is correct now. | 很好，邏輯現在正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed the Floyd-cycle duplicate finder. | 我完成了 Floyd 環偵測找重複值解法。 | Wrap-up |
| I validated bounds and repeated-occurrence patterns. | 我驗證了邊界與重複次數模式。 | Wrap-up |
| Runtime is O(n). | 時間複雜度是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can discuss value-domain binary search alternative if needed. | 若需要我可補充值域二分替代法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Find one duplicate in read-only array. | 在唯讀陣列找唯一重複值。 | Cheat sheet |
| Values range from 1 to n. | 值域是 1 到 n。 | Cheat sheet |
| Need O(1) extra space. | 需要 O(1) 額外空間。 | Cheat sheet |
| Baseline counting is O(n^2). | 基線計數法是 O(n^2)。 | Cheat sheet |
| Map index i to next nums[i]. | 把索引 i 映射到 nums[i]。 | Cheat sheet |
| This creates a cycle in functional graph. | 這會形成函數圖中的環。 | Cheat sheet |
| Duplicate is cycle entry. | 重複值就是環入口。 | Cheat sheet |
| Floyd phase 1 finds intersection. | Floyd 第一階段找相遇點。 | Cheat sheet |
| slow moves one step. | slow 每次一步。 | Cheat sheet |
| fast moves two steps. | fast 每次兩步。 | Cheat sheet |
| Floyd phase 2 finds entry. | Floyd 第二階段找入口。 | Cheat sheet |
| Reset pointer to zero. | 重設一個指標到 0。 | Cheat sheet |
| Move both one step until they meet. | 兩者同速前進直到相遇。 | Cheat sheet |
| Return meeting value. | 回傳相遇值。 | Cheat sheet |
| Test duplicate at lower bound. | 測重複值在下界。 | Cheat sheet |
| Test duplicate at upper bound. | 測重複值在上界。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Bug risk: wrong pointer update formula. | 風險：指標更新公式寫錯。 | Cheat sheet |
| Bug risk: mixing index and value semantics. | 風險：索引與值語意混淆。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Floyd cycle-entry mapping approach is preserved.
- No hallucinated constraints: ✅ Uses source read-only/O(1)-space requirements.
- Language simplicity: ✅ Short interview-speaking lines.
