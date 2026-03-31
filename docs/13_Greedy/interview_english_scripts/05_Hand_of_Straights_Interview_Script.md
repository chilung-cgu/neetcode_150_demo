# 05 Hand of Straights — Interview English Script (C++)

> Source aligned with: `docs/13_Greedy/05_Hand_of_Straights.md`

> Quick links: [Source Solution](../05_Hand_of_Straights.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate hand of straights. | 我先重述 Hand of Straights。 | Restatement |
| We have card values in array hand and an integer groupSize. | 題目給手牌陣列 hand 與 groupSize。 | Restatement |
| We must split all cards into groups of equal size. | 要把所有牌分成固定大小群組。 | Restatement |
| Each group must be consecutive values. | 每組牌值必須連續。 | Restatement |
| Return true if such partition is possible. | 若可行回 true。 | Restatement |
| I will use greedy with ordered frequency map. | 我會用有序頻率表的貪心法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If hand length is not divisible by groupSize, can we return false immediately? | 若手牌數不能整除 groupSize，能否直接 false？ | Clarify |
| Are card values non-negative integers? | 牌值是否為非負整數？ | Clarify |
| Do we need exact partition of all cards with no leftovers? | 是否必須完全分組且不可剩牌？ | Clarify |
| Is sorted-map or min-heap approach both acceptable? | ordered map 或 min-heap 都可接受嗎？ | Clarify |
| Is O(n log n) expected? | O(n log n) 是否預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries many grouping combinations. | 暴力法會嘗試大量分組組合。 | Approach |
| Search space explodes with repeated values. | 重複值會讓搜尋空間爆炸。 | Approach |
| We need deterministic greedy construction. | 我們需要確定性的貪心構造。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Count frequencies with ordered map keyed by card value. | 用有序 map 依牌值統計頻率。 | Approach |
| Always start from smallest card still remaining. | 永遠從目前最小剩餘牌開始。 | Approach |
| If smallest appears count times, we must open count groups from it. | 若最小牌有 count 張，就必須開 count 組順子。 | Approach |
| For every offset up to groupSize minus one, each required card must have at least count copies. | 往後 groupSize-1 張每張都至少要有 count 張。 | Approach |
| Deduct counts in batch; any shortage means false. | 批次扣減頻率，任何不足即 false。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First I check hand size divisible by groupSize. | 先檢查手牌數可否整除 groupSize。 | Coding |
| I build ordered map counts for each card value. | 我建立每個牌值的有序頻率表。 | Coding |
| I iterate map from smallest key upward. | 我由最小 key 往上迭代 map。 | Coding |
| Let startCard and count be current key and remaining copies. | 令 startCard、count 為當前牌值與剩餘張數。 | Coding |
| If count is zero, this key was already consumed. | 若 count 為 0，表示已被前面組消耗。 | Coding |
| Otherwise for i from zero to groupSize minus one, I check counts[startCard+i] >= count. | 否則對每個偏移 i，檢查 counts[startCard+i] 是否至少 count。 | Coding |
| I subtract count from each required consecutive card. | 我把每張必需連續牌都扣掉 count。 | Coding |
| If loop completes, return true. | 若整輪完成，回傳 true。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run hand [1,2,3,6,2,3,4,7,8] and groupSize three. | 我手跑 hand=[1,2,3,6,2,3,4,7,8]、groupSize=3。 | Dry-run |
| Sorted counts start with one card one. | 排序後頻率從牌 1 開始。 | Dry-run |
| From startCard one and count one, consume one two three. | 以 1 為起點 count=1，扣掉 1、2、3。 | Dry-run |
| Next remaining smallest is two, consume two three four. | 下一個最小剩餘是 2，再扣 2、3、4。 | Dry-run |
| Next remaining smallest is six, consume six seven eight. | 再來最小剩餘是 6，扣 6、7、8。 | Dry-run |
| All counts become zero without shortage. | 所有頻率都可扣到 0，無短缺。 | Dry-run |
| Final answer is true. | 最終答案為 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: hand size not divisible by groupSize. | 案例一：手牌數無法整除 groupSize。 | Edge test |
| Case two: missing middle card in required sequence. | 案例二：連續序列中間缺牌。 | Edge test |
| Case three: groupSize equals one should always be true. | 案例三：groupSize=1 應永遠 true。 | Edge test |
| Case four: high duplicates requiring batch subtraction. | 案例四：大量重複值需批次扣減。 | Edge test |
| Case five: very large card values with sparse gaps. | 案例五：牌值很大且分布稀疏。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n log n). | 時間複雜度是 O(n log n)。 | Complexity |
| Space complexity is O(n). | 空間複雜度是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Building ordered frequency map costs O(n log n). | 建立有序頻率表成本為 O(n log n)。 | Complexity |
| Each card count is deducted a bounded number of times. | 每張牌頻率只會被有限次扣減。 | Complexity |
| Overall runtime remains O(n log n). | 整體時間維持 O(n log n)。 | Complexity |
| Frequency map storage is O(n) in worst case unique cards. | 最壞唯一牌值數量下 map 空間為 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me use smallest-card-first greedy rule. | 我先用最小牌優先的貪心規則。 | If stuck |
| Smallest remaining card must be a group start. | 最小剩餘牌一定是某組起點。 | If stuck |
| I should process its full remaining count in batch. | 我應一次處理它全部剩餘 count。 | If stuck |
| For each offset, required card count must be enough. | 每個偏移位置的牌數都必須足夠。 | If stuck |
| If any required count is short, return false immediately. | 任一需求短缺就立即 false。 | If stuck |
| Otherwise subtract batch count from each consecutive value. | 否則對連續值都扣掉 batch count。 | If stuck |
| Let me test quickly with [1,2,3,4,5] and group four. | 我快速測 [1,2,3,4,5]、group=4。 | If stuck |
| Size check fails first, so false is correct. | 先過不了整除檢查，false 正確。 | If stuck |
| Batch deduction avoids repeated tiny operations. | 批次扣減可避免重複小操作。 | If stuck |
| Great, greedy proof and implementation align. | 很好，貪心證明與實作一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved hand of straights with ordered-frequency greedy. | 我用有序頻率貪心解了 Hand of Straights。 | Wrap-up |
| The smallest remaining card always starts new groups. | 最小剩餘牌必定是新順子的起點。 | Wrap-up |
| Batch subtraction enforces all required consecutive cards. | 批次扣減可強制檢查所有必要連續牌。 | Wrap-up |
| Complexity is O(n log n) time and O(n) space. | 複雜度是 O(n log n) 時間、O(n) 空間。 | Wrap-up |
| This is the standard interview-grade solution. | 這是面試常用標準解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: split all cards into consecutive groups of groupSize. | 目標：把所有牌分成長度 groupSize 的連續組。 | Cheat sheet |
| If n % groupSize != 0 -> false. | 若 n % groupSize != 0 -> false。 | Cheat sheet |
| Build ordered frequency map. | 建立有序頻率表。 | Cheat sheet |
| Iterate keys from smallest upward. | 由小到大遍歷 key。 | Cheat sheet |
| Let count = remaining freq at startCard. | 令 count 為 startCard 剩餘頻率。 | Cheat sheet |
| If count==0, continue. | 若 count==0 則略過。 | Cheat sheet |
| Need cards startCard ... startCard+groupSize-1. | 需要 startCard 到 startCard+groupSize-1。 | Cheat sheet |
| Each required freq must be >= count. | 每張需求牌頻率都要 >= count。 | Cheat sheet |
| If any shortage -> false. | 任一不足 -> false。 | Cheat sheet |
| Deduct count from each required card. | 對每張需求牌扣 count。 | Cheat sheet |
| Finish all keys -> true. | 全部完成 -> true。 | Cheat sheet |
| Example [1,2,3,6,2,3,4,7,8],3 -> true. | 範例 [1,2,3,6,2,3,4,7,8],3 -> true。 | Cheat sheet |
| Example [1,2,3,4,5],4 -> false. | 範例 [1,2,3,4,5],4 -> false。 | Cheat sheet |
| Time O(n log n). | 時間 O(n log n)。 | Cheat sheet |
| Space O(n). | 空間 O(n)。 | Cheat sheet |
| Common bug: subtract one-by-one not by batch count. | 常見錯誤：逐張扣而非批次扣 count。 | Cheat sheet |
| Common bug: forgetting divisibility precheck. | 常見錯誤：忘記整除前置檢查。 | Cheat sheet |
| Keep smallest-first invariant explicit. | 清楚說明最小牌優先不變量。 | Cheat sheet |
| Ordered map simplifies correctness reasoning. | 有序 map 可簡化正確性推理。 | Cheat sheet |
| Validate with duplicated-card cases. | 要用重複牌案例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Ordered-map greedy with batch count deduction preserved.
- No hallucinated constraints: ✅ Exact partition and consecutive-group semantics maintained.
- Language simplicity: ✅ Clear interview explanation for invariant and failure condition.
