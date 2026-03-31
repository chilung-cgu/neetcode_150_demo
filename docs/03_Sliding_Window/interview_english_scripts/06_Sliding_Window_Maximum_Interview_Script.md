# 06 Sliding Window Maximum — Interview English Script (C++)

> Source aligned with: `docs/03_Sliding_Window/06_Sliding_Window_Maximum.md`

> Quick links: [Source Solution](../06_Sliding_Window_Maximum.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We have nums and fixed window size k. | 我們有 nums 與固定視窗大小 k。 | Restatement |
| For each window position, output its maximum value. | 每個視窗位置都要輸出最大值。 | Restatement |
| Window moves one step to the right each time. | 視窗每次向右移一步。 | Restatement |
| I will use a monotonic deque of indices. | 我會用單調 deque 儲存索引。 | Restatement |
| Front of deque will always be current max. | deque 前端永遠是當前最大值。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume 1 <= k <= nums length? | 可以假設 1<=k<=nums 長度嗎？ | Clarify |
| Should output length be nums length minus k plus one? | 輸出長度是否為 n-k+1？ | Clarify |
| Are negative numbers allowed in nums? | nums 允許負數嗎？ | Clarify |
| Is O(n) expected, not O(nk)? | 是否預期 O(n)，而非 O(nk)？ | Clarify |
| Can I use deque that stores indices, not values? | 我可使用存索引的 deque 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline scans each window and finds local max. | 基線是對每個視窗線性找最大值。 | Approach |
| With n windows and size k, it is O(nk). | n 個視窗、每窗 k，時間 O(nk)。 | Approach |
| This can degrade to O(n^2). | 最差會退化到 O(n^2)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Deque keeps indices in decreasing value order. | deque 內索引對應值保持遞減。 | Approach |
| Before push, pop back while new value is larger. | push 前若新值更大就反覆 pop back。 | Approach |
| Pop front when index is out of current window. | 索引過期就 pop front。 | Approach |
| After first full window, deque front is answer. | 首個完整視窗後，front 就是答案。 | Approach |
| Every index enters and leaves deque once. | 每個索引最多進出 deque 各一次。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create empty deque and result array. | 先建立空 deque 與結果陣列。 | Coding |
| For each index i, remove outdated front indices. | 對每個 i，先移除過期 front 索引。 | Coding |
| Then pop smaller values from deque back. | 接著從 deque 尾端移除較小值索引。 | Coding |
| Push current index i to deque back. | 把當前索引 i 放到 deque 尾端。 | Coding |
| If i is at least k minus one, window is ready. | 若 i>=k-1，代表視窗已成形。 | Coding |
| Append nums[dq.front()] to result. | 把 nums[dq.front()] 加入結果。 | Coding |
| Deque front always points to max in window. | deque front 永遠指向視窗最大值。 | Coding |
| Return result after loop finishes. | 迴圈結束後回傳結果。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [1,3,-1,-3,5,3,6,7] with k=3. | 我手跑 nums=[1,3,-1,-3,5,3,6,7]，k=3。 | Dry-run |
| Build first window and deque front becomes value 3. | 建立首窗後，deque front 對應值是 3。 | Dry-run |
| Record first answer as 3. | 第一個答案記錄為 3。 | Dry-run |
| Slide right, remove outdated and smaller indices. | 視窗右移，移除過期與較小索引。 | Dry-run |
| Front updates to represent 5, then 6, then 7. | front 會依序更新到 5、6、7。 | Dry-run |
| Collected outputs become [3,3,5,5,6,7]. | 收集輸出得到 [3,3,5,5,6,7]。 | Dry-run |
| This matches expected result. | 這與預期結果一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: k equals one returns original array. | 案例一：k=1 時輸出等於原陣列。 | Edge test |
| Case two: k equals n returns single global max. | 案例二：k=n 時只回傳全域最大值。 | Edge test |
| Case three: all equal values. | 案例三：全部元素相同。 | Edge test |
| Case four: strictly increasing sequence. | 案例四：嚴格遞增序列。 | Edge test |
| Case five: strictly decreasing sequence. | 案例五：嚴格遞減序列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Auxiliary space is O(k). | 輔助空間是 O(k)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each index is pushed into deque once. | 每個索引只會被 push 一次。 | Complexity |
| Each index is popped at most once. | 每個索引最多被 pop 一次。 | Complexity |
| So total deque operations are linear. | 因此 deque 操作總量是線性。 | Complexity |
| Deque size never exceeds window size k. | deque 大小不會超過視窗大小 k。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate deque invariant quickly. | 我先快速重述 deque 不變量。 | If stuck |
| Values in deque must stay decreasing. | deque 對應值必須維持遞減。 | If stuck |
| Front index must stay inside current window. | front 索引必須留在當前視窗內。 | If stuck |
| I can explain brute force first if needed. | 若需要我可先解釋暴力法。 | If stuck |
| Then switch to O(n) monotonic deque. | 再切回 O(n) 單調 deque。 | If stuck |
| Thanks, I found an outdated-index bug. | 謝謝，我找到過期索引 bug。 | If stuck |
| Let me rerun sample step by step. | 我逐步重跑範例。 | If stuck |
| Now deque front tracks max correctly. | 現在 deque front 能正確追蹤最大值。 | If stuck |
| Output sequence is now stable. | 現在輸出序列已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Auxiliary space is O(k). | 輔助空間是 O(k)。 | Wrap-up |
| I can compare heap-based alternative if needed. | 若需要我可比較 heap 替代方案。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate sliding-window max goal. | 重述滑動視窗最大值目標。 | Cheat sheet |
| Mention fixed window size k. | 提到固定視窗大小 k。 | Cheat sheet |
| Brute force scans each window. | 暴力法逐窗掃描。 | Cheat sheet |
| Brute force is O(nk). | 暴力法是 O(nk)。 | Cheat sheet |
| Use monotonic deque of indices. | 使用索引型單調 deque。 | Cheat sheet |
| Remove outdated front indices first. | 先移除過期 front 索引。 | Cheat sheet |
| Pop back while new value is larger. | 新值較大時持續 pop back。 | Cheat sheet |
| Push current index to back. | 將當前索引 push 到尾端。 | Cheat sheet |
| Front now holds max candidate. | 此時 front 即最大候選。 | Cheat sheet |
| Start output when i >= k-1. | i>=k-1 後開始輸出。 | Cheat sheet |
| Dry-run [1,3,-1,-3,5,3,6,7], k=3. | 手跑 [1,3,-1,-3,5,3,6,7], k=3。 | Cheat sheet |
| Confirm output [3,3,5,5,6,7]. | 確認輸出 [3,3,5,5,6,7]。 | Cheat sheet |
| Test k=1 returns original nums. | 測 k=1 回傳原陣列。 | Cheat sheet |
| Test k=n returns one value. | 測 k=n 回傳單一值。 | Cheat sheet |
| Test increasing sequence. | 測遞增序列。 | Cheat sheet |
| Test decreasing sequence. | 測遞減序列。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(k) auxiliary space. | 報告 O(k) 輔助空間。 | Cheat sheet |
| If stuck, recheck deque invariants. | 卡住時重檢 deque 不變量。 | Cheat sheet |
| End with concise result summary. | 以精簡結果總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Monotonic deque index logic is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
