# 05 Missing Number — Interview English Script (C++)

> Source aligned with: `docs/18_Bit_Manipulation/05_Missing_Number.md`

> Quick links: [Source Solution](../05_Missing_Number.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Missing Number. | 我先重述 Missing Number。 | Restatement |
| Array nums contains n distinct numbers from range zero to n. | nums 含 n 個互異數，範圍是 0 到 n。 | Restatement |
| Exactly one number in that range is missing. | 該範圍中剛好少了一個數。 | Restatement |
| We need to return the missing value. | 我們要找出缺失值。 | Restatement |
| I will use XOR to avoid overflow concerns. | 我會用 XOR 來避免溢位顧慮。 | Restatement |
| This satisfies O(n) time and O(1) extra space. | 這可滿足 O(n) 時間與 O(1) 空間。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are numbers guaranteed unique with no duplicates? | 數字是否保證互異無重複？ | Clarify |
| Is range exactly inclusive zero through n? | 範圍是否確定為含端點的 0 到 n？ | Clarify |
| Can I assume one and only one missing number? | 是否可假設且僅有一個缺失值？ | Clarify |
| Is O(1) extra space required? | 是否要求 O(1) 額外空間？ | Clarify |
| Should I discuss both sum and xor methods briefly? | 是否要簡述 sum 與 xor 兩種方法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Sorting then scanning index mismatch finds answer. | 排序後找索引不匹配可找到答案。 | Approach |
| But sorting costs O(n log n). | 但排序需 O(n log n)。 | Approach |
| Hash set gives O(n) time but O(n) space. | HashSet 可 O(n) 時間但要 O(n) 空間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| XOR all indices and all values together. | 把所有索引與數值一起做 XOR。 | Approach |
| Matching numbers cancel due to xor properties. | 配對數字會因 xor 性質互相抵消。 | Approach |
| Initialize result with n because indices only go zero to n minus one. | result 先設 n，因索引只到 n-1。 | Approach |
| For each i, do result xor i xor nums[i]. | 每個 i 執行 result^=i^nums[i]。 | Approach |
| Remaining result is missing number. | 剩下的 result 就是缺失值。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I set n as nums size. | 我先設定 n=nums.size()。 | Coding |
| I initialize res to n. | 我初始化 res=n。 | Coding |
| I loop i from zero to n minus one. | i 從 0 到 n-1 迴圈。 | Coding |
| In each step, res xor equals i. | 每步先做 res ^= i。 | Coding |
| Then res xor equals nums[i]. | 再做 res ^= nums[i]。 | Coding |
| After loop, all matched values are canceled. | 迴圈後所有配對值都已抵消。 | Coding |
| I return res as missing number. | 回傳 res 作為缺失數。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums equals [3,0,1]. | 我用 nums=[3,0,1] 手跑。 | Dry-run |
| n is three, so res starts at three. | n=3，所以 res 起始為 3。 | Dry-run |
| i zero: res xor zero xor three keeps zero. | i=0：res^0^3 變成 0。 | Dry-run |
| i one: res xor one xor zero becomes one. | i=1：res^1^0 變成 1。 | Dry-run |
| i two: res xor two xor one becomes two. | i=2：res^2^1 變成 2。 | Dry-run |
| Final res is two. | 最終 res=2。 | Dry-run |
| That matches expected answer. | 這和預期答案一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: missing zero. | 案例一：缺失值是 0。 | Edge test |
| Case two: missing n itself. | 案例二：缺失值是 n。 | Edge test |
| Case three: smallest size n equals one. | 案例三：最小長度 n=1。 | Edge test |
| Case four: larger shuffled array. | 案例四：較大且打亂順序陣列。 | Edge test |
| Case five: random tests compared with sum method. | 案例五：與 sum 法做隨機對照。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan the array once with constant work per index. | 我們單次掃描陣列，每個索引做常數操作。 | Complexity |
| XOR operations are O(1). | XOR 操作是 O(1)。 | Complexity |
| Therefore runtime is linear O(n). | 因此時間是線性 O(n)。 | Complexity |
| Only n, i, and res scalars are used, so memory is O(1). | 只用 n、i、res 等純量，空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me pair complete range zero..n against nums values. | 我先把完整範圍 0..n 與 nums 做配對。 | If stuck |
| Every present number appears once on each side and cancels. | 存在的數在兩側各出現一次會抵消。 | If stuck |
| Only missing number has no partner and remains. | 只有缺失值沒有配對會留下。 | If stuck |
| I use res initialized to n to include upper bound. | res 初始設 n 以納入上界。 | If stuck |
| Then iterate i and nums[i] together. | 然後同時處理 i 與 nums[i]。 | If stuck |
| Perform res ^= i ^= nums[i] logically as two xors. | 以兩次 xor 完成 res 對 i 與 nums[i] 的更新。 | If stuck |
| Let me verify with [0,1] quickly. | 我快速驗證 [0,1]。 | If stuck |
| Result should become two. | 結果應為 2。 | If stuck |
| That confirms missing upper bound case. | 這驗證了缺失上界案例。 | If stuck |
| Great, xor solution is stable. | 很好，xor 解法穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with one-pass xor cancellation. | 我用單次 xor 抵消法解題。 | Wrap-up |
| It avoids sorting and extra hash memory. | 這避免了排序與額外雜湊空間。 | Wrap-up |
| The method is overflow-safe compared to arithmetic sum in extreme scenarios. | 相較加總法，這在極端情況更無溢位顧慮。 | Wrap-up |
| Complexity is O(n) time and O(1) extra space. | 複雜度是 O(n) 時間與 O(1) 空間。 | Wrap-up |
| This is a common interview-preferred implementation. | 這是面試常見偏好的實作。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: find missing value from range 0..n. | 目標：找出 0..n 中缺失值。 | Cheat sheet |
| nums size is n. | nums 長度是 n。 | Cheat sheet |
| Init res = n. | 初始化 res=n。 | Cheat sheet |
| Loop i from 0 to n-1. | i 從 0 到 n-1。 | Cheat sheet |
| res ^= i. | res ^= i。 | Cheat sheet |
| res ^= nums[i]. | res ^= nums[i]。 | Cheat sheet |
| Matching values cancel out. | 配對值會互相抵消。 | Cheat sheet |
| Missing value remains in res. | 缺失值會留在 res。 | Cheat sheet |
| Return res. | 回傳 res。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Test missing 0 case. | 測缺失 0。 | Cheat sheet |
| Test missing n case. | 測缺失 n。 | Cheat sheet |
| Test small array [3,0,1] => 2. | 測 [3,0,1] => 2。 | Cheat sheet |
| Common bug: forget initial res=n. | 常見錯誤：忘記初始 res=n。 | Cheat sheet |
| Common bug: using addition with overflow risk. | 常見錯誤：用加總可能有溢位風險。 | Cheat sheet |
| XOR order does not matter. | XOR 順序不影響。 | Cheat sheet |
| Distinctness assumption is important. | 元素互異假設很重要。 | Cheat sheet |
| Keep explanation with cancellation intuition. | 以抵消直覺解釋最清楚。 | Cheat sheet |
| Short and interview-robust. | 短小且面試穩健。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ XOR-based linear solution.
- Constraint alignment: ✅ Constant-space requirement met.
- Language simplicity: ✅ Interview-friendly concise wording.
