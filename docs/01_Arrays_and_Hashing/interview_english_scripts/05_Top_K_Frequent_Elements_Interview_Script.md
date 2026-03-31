# 05 Top K Frequent Elements — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/05_Top_K_Frequent_Elements.md`

> Quick links: [Source Solution](../05_Top_K_Frequent_Elements.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We need the k most frequent numbers. | 我們要找出前 k 個最高頻數字。 | Restatement |
| Input is nums and integer k. | 輸入是 nums 和整數 k。 | Restatement |
| Full sorting may be too slow here. | 全排序在這題可能太慢。 | Restatement |
| I will use frequency map plus buckets. | 我會用頻率 map 加 buckets。 | Restatement |
| Then I will verify with a sample. | 接著我會用範例驗證。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is k always between one and unique count? | k 一定介於 1 到 unique 數量嗎？ | Clarify |
| If tie happens, can I return any order? | 若頻率同分，可以任意順序嗎？ | Clarify |
| Do you want strictly better than O(n log n)? | 是否要求嚴格優於 O(n log n)？ | Clarify |
| Can nums include negative numbers? | nums 可能包含負數嗎？ | Clarify |
| Should I also mention heap alternative? | 也要補充 heap 替代法嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline counts frequency, then sorts all pairs. | 基線是先統計頻率，再排序所有 pair。 | Approach |
| We then take first k items. | 然後取前 k 個項目。 | Approach |
| Time is O(n log n), not optimal here. | 時間是 O(n log n)，這題不夠好。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I first build map from number to frequency. | 我先建立數字到頻率的 map。 | Approach |
| Frequency range is one to n. | 頻率範圍是 1 到 n。 | Approach |
| So I create buckets indexed by frequency. | 所以我建立以頻率為索引的 buckets。 | Approach |
| I scan buckets from high to low frequency. | 我從高頻往低頻掃 buckets。 | Approach |
| Stop when I collect k numbers. | 收滿 k 個數字就停止。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create unordered_map<int,int> freq. | 先建立 unordered_map<int,int> freq。 | Coding |
| Then I count each number in nums. | 然後統計 nums 每個數字。 | Coding |
| Next, I create vector buckets of size n plus one. | 接著建立大小 n+1 的 buckets。 | Coding |
| For each pair, push number into bucket[count]. | 對每個 pair，把數字放到 bucket[count]。 | Coding |
| Then I prepare result vector. | 然後準備結果向量。 | Coding |
| I scan i from n down to one. | 我讓 i 從 n 遞減到 1。 | Coding |
| Append numbers in bucket[i] into result. | 把 bucket[i] 的數字加入結果。 | Coding |
| If result size is k, return immediately. | 若結果大小等於 k，立刻回傳。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums one, one, one, two, two, three. | 我手跑 nums = 1,1,1,2,2,3。 | Dry-run |
| k is two. | k 是 2。 | Dry-run |
| Frequency map becomes one to three, two to two, three to one. | 頻率 map 變成 1:3, 2:2, 3:1。 | Dry-run |
| So bucket three has one, bucket two has two. | 所以 bucket[3] 有 1，bucket[2] 有 2。 | Dry-run |
| Scan from high frequency, pick one first. | 從高頻掃描，先拿到 1。 | Dry-run |
| Next pick two, now size reaches k. | 接著拿到 2，大小達到 k。 | Dry-run |
| Return [1,2]. | 回傳 [1,2]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: nums [1], k one, output [1]. | 案例一：nums [1], k=1，輸出 [1]。 | Edge test |
| Case two: all same values, k one. | 案例二：全部相同值，k=1。 | Edge test |
| Case three: negatives and positives mixed. | 案例三：正負值混合。 | Edge test |
| Case four: k equals number of unique values. | 案例四：k 等於 unique 數量。 | Edge test |
| Case five: tie frequencies, order can vary. | 案例五：同頻率時順序可不同。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Space is O(n). | 空間是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Counting pass is O(n). | 計數那一輪是 O(n)。 | Complexity |
| Filling buckets from map is O(n) total. | 從 map 填 bucket 合計 O(n)。 | Complexity |
| Reverse bucket scan is also O(n). | 反向掃 bucket 也是 O(n)。 | Complexity |
| Map and buckets both require linear extra space. | map 與 buckets 都需要線性額外空間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me confirm k range first. | 我先確認 k 的範圍。 | If stuck |
| I can explain sort solution first. | 我可以先講排序解法。 | If stuck |
| Then I switch to bucket solution. | 然後切到 bucket 解法。 | If stuck |
| I forgot one loop bound only. | 我只是忘了迴圈邊界。 | If stuck |
| The core idea is still clear. | 但核心概念仍清楚。 | If stuck |
| Thanks, I will adjust this part. | 謝謝，我會調整這段。 | If stuck |
| I found why k stopping failed. | 我找到 k 停止條件失敗原因。 | If stuck |
| Let me rerun the sample quickly. | 我快速重跑範例。 | If stuck |
| Now output size is exactly k. | 現在輸出大小剛好是 k。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| The bucket scan returns top k correctly. | bucket 掃描可正確回傳前 k。 | Wrap-up |
| It meets the better-than-sort requirement. | 它符合優於全排序的要求。 | Wrap-up |
| Time is O(n), space is O(n). | 時間 O(n)，空間 O(n)。 | Wrap-up |
| I can discuss heap alternative if needed. | 需要的話我可補充 heap 替代法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate top-k-frequency target. | 重述前 k 頻率目標。 | Cheat sheet |
| Ask if tie order matters. | 詢問同頻順序是否重要。 | Cheat sheet |
| Baseline sort is O(n log n). | 基線排序是 O(n log n)。 | Cheat sheet |
| Build frequency map first. | 先建立頻率 map。 | Cheat sheet |
| Create n+1 frequency buckets. | 建立 n+1 個頻率桶。 | Cheat sheet |
| Put number into bucket[count]. | 把數字放進 bucket[count]。 | Cheat sheet |
| Scan buckets from high to low. | 從高頻往低頻掃描 buckets。 | Cheat sheet |
| Stop exactly when size equals k. | 大小等於 k 就停止。 | Cheat sheet |
| Dry-run [1,1,1,2,2,3], k=2. | 手跑 [1,1,1,2,2,3], k=2。 | Cheat sheet |
| Verify single-element case. | 驗證單一元素情況。 | Cheat sheet |
| Verify k equals unique count. | 驗證 k 等於 unique 數量。 | Cheat sheet |
| Verify negative numbers case. | 驗證負數案例。 | Cheat sheet |
| Mention heap as alternative. | 提及 heap 替代方案。 | Cheat sheet |
| Counting pass is O(n). | 計數回合是 O(n)。 | Cheat sheet |
| Bucket fill and scan are O(n). | 填桶與掃桶都是 O(n)。 | Cheat sheet |
| Total time O(n). | 總時間 O(n)。 | Cheat sheet |
| Extra space O(n). | 額外空間 O(n)。 | Cheat sheet |
| Keep speaking in coding order. | 依照寫程式順序口述。 | Cheat sheet |
| End with concise complexity summary. | 以精簡複雜度總結結尾。 | Cheat sheet |
| Invite follow-up optimization discussion. | 邀請後續優化討論。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Bucket-sort main approach is preserved.
- No hallucinated constraints: ✅ Ambiguous preferences are asked in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview use.
