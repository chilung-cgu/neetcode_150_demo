# 09 Longest Consecutive Sequence — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/09_Longest_Consecutive_Sequence.md`

> Quick links: [Source Solution](../09_Longest_Consecutive_Sequence.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We need the longest consecutive sequence length. | 我們要找最長連續序列長度。 | Restatement |
| Input array is unsorted. | 輸入陣列是未排序的。 | Restatement |
| Sequence means x, x+1, x+2, and so on. | 連續指的是 x、x+1、x+2 這樣。 | Restatement |
| I will use hash set with start detection. | 我會用 hash set 加起點判斷。 | Restatement |
| Then I will verify duplicates and empty case. | 然後我會驗證重複與空陣列。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is O(n log n) sorting solution acceptable, or must be O(n)? | 可接受 O(n log n) 排序嗎，還是必須 O(n)？ | Clarify |
| Can input contain duplicate numbers? | 輸入可以有重複數字嗎？ | Clarify |
| Can input be empty? | 輸入可以是空陣列嗎？ | Clarify |
| Can numbers be negative or very large? | 數字可為負或很大嗎？ | Clarify |
| Should I return zero for empty input? | 空輸入是否回傳 0？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline sorts numbers, then scans consecutive runs. | 基線是先排序，再掃描連續區段。 | Approach |
| That gives O(n log n) time. | 這樣時間是 O(n log n)。 | Approach |
| But the target here is linear time. | 但這題目標是線性時間。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Put all numbers into unordered_set first. | 先把所有數字放入 unordered_set。 | Approach |
| Only start counting when num minus one is absent. | 只有 num-1 不存在時才開始計數。 | Approach |
| That num is a sequence start. | 這個 num 就是序列起點。 | Approach |
| Expand forward while num plus length exists. | 只要 num+length 存在就持續往前擴展。 | Approach |
| Keep maximum length as answer. | 持續更新最大長度當答案。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I build unordered_set from nums. | 先從 nums 建立 unordered_set。 | Coding |
| I initialize longest as zero. | 我把 longest 初始化為 0。 | Coding |
| Then I iterate each num in the set. | 然後走訪 set 裡每個 num。 | Coding |
| If num minus one exists, skip this num. | 若 num-1 存在，就跳過這個 num。 | Coding |
| Otherwise this num starts a new sequence. | 否則這個 num 是新序列起點。 | Coding |
| I set length to one. | 我把 length 設為 1。 | Coding |
| While num plus length exists, length plus plus. | 只要 num+length 存在就 length++。 | Coding |
| Update longest with max(longest, length). | 用 max(longest, length) 更新 longest。 | Coding |
| Finally, return longest. | 最後回傳 longest。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums one hundred, four, two hundred, one, three, two. | 我手跑 100,4,200,1,3,2。 | Dry-run |
| Set contains all six numbers. | set 內含這六個數。 | Dry-run |
| Number one is a start, because zero is absent. | 數字 1 是起點，因為 0 不存在。 | Dry-run |
| Expand to two, three, four, then stop. | 擴展到 2、3、4 後停止。 | Dry-run |
| This sequence length is four. | 這段序列長度是 4。 | Dry-run |
| Numbers two, three, four are skipped as non-starts. | 2、3、4 因非起點而被跳過。 | Dry-run |
| Final answer is four. | 最終答案是 4。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty input should return zero. | 案例一：空輸入應回傳 0。 | Edge test |
| Case two: single number returns one. | 案例二：單一數字回傳 1。 | Edge test |
| Case three: all duplicates like [2,2,2]. | 案例三：全重複如 [2,2,2]。 | Edge test |
| Case four: mixed negatives like [-2,-1,0,1]. | 案例四：含負數混合如 [-2,-1,0,1]。 | Edge test |
| Case five: separated blocks pick the longest block. | 案例五：多區段時取最長那段。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Average time is O(n). | 平均時間是 O(n)。 | Complexity |
| Space is O(n) for hash set. | 空間是 O(n)，用在 hash set。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Set construction is O(n). | 建 set 是 O(n)。 | Complexity |
| Each number is expanded only from sequence starts. | 每個數字只會在起點擴展時被計入。 | Complexity |
| Total expansion work is linear overall. | 總擴展工作量整體是線性。 | Complexity |
| Therefore average runtime O(n), space O(n). | 因此平均時間 O(n)、空間 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me recheck start condition first. | 我先重檢起點條件。 | If stuck |
| I can explain sorting baseline quickly. | 我可先快速講排序基線。 | If stuck |
| Then I switch to hash-set start trick. | 然後切到 hash set 起點技巧。 | If stuck |
| I forgot one boundary case only. | 我只是一時忘了邊界案例。 | If stuck |
| Core sequence logic is still correct. | 核心序列邏輯仍正確。 | If stuck |
| Thanks, I will adjust this branch. | 謝謝，我會調整這個分支。 | If stuck |
| I found why duplicates broke counting. | 我找到重複值破壞計數原因。 | If stuck |
| Let me rerun the sample now. | 我現在再跑一次範例。 | If stuck |
| The max length is correct now. | 現在最長長度正確了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| Start-detection avoids redundant sequence scans. | 起點判斷可避免重複掃序列。 | Wrap-up |
| It handles duplicates naturally through set. | 透過 set 可自然處理重複值。 | Wrap-up |
| Average time is O(n), space O(n). | 平均時間 O(n)，空間 O(n)。 | Wrap-up |
| I can discuss sorting comparison if needed. | 若需要我可補充與排序法比較。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate longest-consecutive goal. | 重述最長連續序列目標。 | Cheat sheet |
| Mention unsorted input constraint. | 提到輸入未排序限制。 | Cheat sheet |
| Sorting baseline is O(n log n). | 排序基線是 O(n log n)。 | Cheat sheet |
| Build hash set from nums. | 從 nums 建立 hash set。 | Cheat sheet |
| Only count from sequence starts. | 只從序列起點開始計數。 | Cheat sheet |
| Start means num-1 is absent. | 起點定義是 num-1 不存在。 | Cheat sheet |
| Expand with while num+len exists. | 用 while 檢查 num+len 是否存在。 | Cheat sheet |
| Update longest each sequence. | 每段序列都更新 longest。 | Cheat sheet |
| Dry-run [100,4,200,1,3,2]. | 手跑 [100,4,200,1,3,2]。 | Cheat sheet |
| Verify empty input returns zero. | 驗證空輸入回傳 0。 | Cheat sheet |
| Verify duplicate-heavy input. | 驗證大量重複輸入。 | Cheat sheet |
| Verify negative chain case. | 驗證負數連續鏈案例。 | Cheat sheet |
| Explain why work is linear overall. | 解釋為何整體工作量線性。 | Cheat sheet |
| Average time O(n). | 平均時間 O(n)。 | Cheat sheet |
| Space O(n) for set. | set 需要 O(n) 空間。 | Cheat sheet |
| If stuck, restate start condition. | 卡住時重述起點條件。 | Cheat sheet |
| Keep loop narration explicit. | 清楚口述迴圈流程。 | Cheat sheet |
| Summarize key invariant at end. | 收尾重述關鍵不變量。 | Cheat sheet |
| Mention sorting trade-off briefly. | 簡短提排序取捨。 | Cheat sheet |
| Offer follow-up discussion. | 主動提供延伸討論。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hash-set start-detection approach is preserved.
- No hallucinated constraints: ✅ Ambiguous constraints are asked in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview flow.
