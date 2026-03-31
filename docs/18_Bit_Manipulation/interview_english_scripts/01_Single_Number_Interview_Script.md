# 01 Single Number — Interview English Script (C++)

> Source aligned with: `docs/18_Bit_Manipulation/01_Single_Number.md`

> Quick links: [Source Solution](../01_Single_Number.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Single Number. | 我先重述 Single Number。 | Restatement |
| In the array, every value appears twice except one value. | 陣列中除了某一個值，其餘都出現兩次。 | Restatement |
| We need to return that single value. | 我們要找出唯一出現一次的值。 | Restatement |
| Target complexity is linear time and constant extra space. | 目標是線性時間與常數額外空間。 | Restatement |
| I will use XOR cancellation property. | 我會用 XOR 抵消性質。 | Restatement |
| Pair duplicates cancel to zero, leaving the unique number. | 成對數字會變 0，只剩唯一值。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is there guaranteed exactly one number appearing once? | 是否保證恰好只有一個數只出現一次？ | Clarify |
| Are all other numbers guaranteed to appear exactly twice? | 其他數是否都剛好出現兩次？ | Clarify |
| Can values be negative integers as well? | 值是否可能是負整數？ | Clarify |
| Should we optimize for O(1) extra memory strictly? | 是否嚴格要求 O(1) 額外空間？ | Clarify |
| Is return type standard int? | 回傳型別是一般 int 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| A simple method counts frequency using hash map. | 簡單作法是用 HashMap 計數。 | Approach |
| Then find the key with count one. | 再找出次數為 1 的鍵。 | Approach |
| Time is O(n), but extra space is O(n). | 時間 O(n)，但空間 O(n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| XOR has properties a xor a equals zero and a xor zero equals a. | XOR 性質是 a^a=0 且 a^0=a。 | Approach |
| XOR is associative and commutative, so order does not matter. | XOR 具結合律交換律，順序不影響。 | Approach |
| XOR all numbers in one pass. | 一次遍歷把所有數做 XOR。 | Approach |
| Every duplicated pair cancels out. | 每個成對數字都會互相抵消。 | Approach |
| Remaining value is exactly the single number. | 最後剩下的就是唯一值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize result as zero. | 我先把 result 初始化為 0。 | Coding |
| I iterate through each number n in nums. | 我逐一遍歷 nums 中每個 n。 | Coding |
| I update result with result xor n. | 我把 result 更新為 result xor n。 | Coding |
| Duplicates cancel automatically during accumulation. | 在累積過程中，重複值會自動抵消。 | Coding |
| After the loop, result stores the unique value. | 迴圈結束後 result 即為唯一值。 | Coding |
| I return result. | 我回傳 result。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [4,1,2,1,2]. | 我用 [4,1,2,1,2] 手跑。 | Dry-run |
| Start result zero. | 起始 result 為 0。 | Dry-run |
| After xor four, result is four. | XOR 4 後 result 為 4。 | Dry-run |
| After xor one then xor two, result becomes seven. | 再 XOR 1、XOR 2 後 result 變 7。 | Dry-run |
| XOR one cancels previous one, result back to six. | 再 XOR 1 抵消前面的 1，result 回 6。 | Dry-run |
| XOR two cancels previous two, result becomes four. | 再 XOR 2 抵消前面的 2，result 變 4。 | Dry-run |
| Final answer is four. | 最終答案是 4。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: array size one. | 案例一：陣列長度為 1。 | Edge test |
| Case two: unique number is zero. | 案例二：唯一值是 0。 | Edge test |
| Case three: includes negative values. | 案例三：包含負數。 | Edge test |
| Case four: unique value appears at beginning or end. | 案例四：唯一值在開頭或結尾。 | Edge test |
| Case five: large array still linear scan. | 案例五：大陣列仍是線性掃描。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We make one pass through n elements. | 我們只遍歷 n 個元素一次。 | Complexity |
| Each xor operation is constant time. | 每次 xor 都是常數時間。 | Complexity |
| So runtime is O(n). | 因此時間是 O(n)。 | Complexity |
| We use one accumulator variable only, so memory is O(1). | 只用一個累積變數，空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me rely on xor identities first. | 我先依賴 xor 恆等式。 | If stuck |
| Same numbers cancel because a xor a is zero. | 相同數字可抵消因為 a xor a=0。 | If stuck |
| Zero does not change value because a xor zero is a. | 0 不改值因為 a xor 0=a。 | If stuck |
| Order does not matter due to associativity and commutativity. | 因結合律交換律，順序無關。 | If stuck |
| So I can xor all values directly. | 所以我可直接 xor 全部元素。 | If stuck |
| Pairs vanish and only unique survives. | 成對值消失，唯一值留下。 | If stuck |
| Let me test quickly with [2,2,1]. | 我快速測 [2,2,1]。 | If stuck |
| Result one confirms the rule. | 得到 1，規則成立。 | If stuck |
| This meets O(n) time and O(1) space target. | 這符合 O(n) 時間與 O(1) 空間目標。 | If stuck |
| Implementation is now a few lines. | 實作現在只要幾行。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with one-pass xor accumulation. | 我用單次 xor 累積解出此題。 | Wrap-up |
| Duplicate values cancel out naturally. | 重複值會自然互相抵消。 | Wrap-up |
| The remaining value is the unique number. | 剩下值就是唯一數字。 | Wrap-up |
| Complexity is O(n) time and O(1) extra space. | 複雜度是 O(n) 時間與 O(1) 空間。 | Wrap-up |
| This is the canonical interview solution. | 這是此題面試的經典解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: find only value appearing once. | 目標：找出唯一出現一次的值。 | Cheat sheet |
| Others appear exactly twice. | 其餘都出現兩次。 | Cheat sheet |
| Use xor accumulation. | 使用 xor 累積。 | Cheat sheet |
| Start res = 0. | 初始 res=0。 | Cheat sheet |
| For each n: res ^= n. | 對每個 n：res ^= n。 | Cheat sheet |
| Property: a^a=0. | 性質：a^a=0。 | Cheat sheet |
| Property: a^0=a. | 性質：a^0=a。 | Cheat sheet |
| Property: xor is associative. | 性質：xor 有結合律。 | Cheat sheet |
| Property: xor is commutative. | 性質：xor 有交換律。 | Cheat sheet |
| Therefore pair values cancel. | 因此成對值會抵消。 | Cheat sheet |
| Unique value remains. | 唯一值會留下。 | Cheat sheet |
| Return res. | 回傳 res。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Test [2,2,1] => 1. | 測 [2,2,1] => 1。 | Cheat sheet |
| Test [4,1,2,1,2] => 4. | 測 [4,1,2,1,2] => 4。 | Cheat sheet |
| Works with negatives too. | 負數也適用。 | Cheat sheet |
| Common bug: using sum instead of xor. | 常見錯誤：誤用加總而非 xor。 | Cheat sheet |
| Keep loop single pass. | 保持單次遍歷。 | Cheat sheet |
| Short, fast, interview-perfect. | 短小快速，面試很加分。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ XOR cancellation method.
- Constraint alignment: ✅ O(n) time, O(1) extra space.
- Language simplicity: ✅ Direct spoken style.
