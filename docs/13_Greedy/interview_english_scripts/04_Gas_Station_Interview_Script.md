# 04 Gas Station — Interview English Script (C++)

> Source aligned with: `docs/13_Greedy/04_Gas_Station.md`

> Quick links: [Source Solution](../04_Gas_Station.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate gas station. | 我先重述 Gas Station。 | Restatement |
| We have circular stations with gas[i] and travel cost[i]. | 有一圈站點，每站有 gas[i] 與 cost[i]。 | Restatement |
| We need a start index to complete one full circle. | 要找一個起點能跑完整圈。 | Restatement |
| If impossible, return minus one. | 若不可能則回傳 -1。 | Restatement |
| If possible, problem guarantees a unique valid start. | 若可行，題目保證解唯一。 | Restatement |
| I will solve it with one-pass greedy plus total check. | 我會用總量檢查加單趟貪心解。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are gas and cost arrays same length n? | gas 與 cost 長度是否同為 n？ | Clarify |
| Is tank capacity effectively unlimited? | 油箱容量是否視為無上限？ | Clarify |
| Should we return minus one when total gas is insufficient? | 總油不足時是否直接回 -1？ | Clarify |
| Is uniqueness of valid start guaranteed by statement? | 合法起點唯一性是否由題目保證？ | Clarify |
| Is O(n) expected? | O(n) 是否為預期解？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries every station as start and simulates full loop. | 暴力法把每站都當起點並模擬一圈。 | Approach |
| Each simulation can scan almost n steps. | 每次模擬可能掃近 n 步。 | Approach |
| Overall complexity is O(n squared). | 整體複雜度為 O(n²)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First check if totalGas is less than totalCost; if yes return minus one. | 先檢查 totalGas<totalCost，若是就回 -1。 | Approach |
| Then scan once with currentTank and candidate start index. | 接著單趟掃描，維護 currentTank 與候選起點。 | Approach |
| Add gas[i]-cost[i] into currentTank at each station. | 每站把 gas[i]-cost[i] 加入 currentTank。 | Approach |
| If currentTank drops below zero, reset start to i plus one and tank to zero. | 若 currentTank<0，起點改 i+1 並把油量歸零。 | Approach |
| Final candidate start is the answer when total check passed. | 總量可行時，最後候選起點即答案。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I compute totalGas and totalCost in one pass. | 我先單趟算出 totalGas 與 totalCost。 | Coding |
| If totalGas is smaller, I return minus one immediately. | 若 totalGas 較小就立刻回 -1。 | Coding |
| I set start to zero and currentTank to zero. | 我設 start=0、currentTank=0。 | Coding |
| For each index i, I add gas[i]-cost[i] to currentTank. | 對每個 i，把 gas[i]-cost[i] 加到 currentTank。 | Coding |
| If currentTank becomes negative, start cannot be in current segment. | 若 currentTank 變負，當前區段都不可能是起點。 | Coding |
| So I set start to i plus one and reset currentTank to zero. | 所以把 start 改為 i+1，並重設 currentTank=0。 | Coding |
| Continue until end of array. | 持續到陣列尾端。 | Coding |
| Return start as the valid station index. | 回傳 start 作為合法起點。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run gas [1,2,3,4,5] and cost [3,4,5,1,2]. | 我手跑 gas=[1,2,3,4,5]、cost=[3,4,5,1,2]。 | Dry-run |
| Total gas equals total cost, so solution may exist. | 總油等於總耗，可能有解。 | Dry-run |
| At index zero currentTank becomes minus two, so start moves to one. | 在 0 處 currentTank=-2，起點移到 1。 | Dry-run |
| Similar failures move start to two then three. | 類似失敗再把起點移到 2、再到 3。 | Dry-run |
| From index three onward currentTank never drops below zero. | 從索引 3 往後 currentTank 不再為負。 | Dry-run |
| Final start is three. | 最後起點是 3。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: total gas less than total cost returns minus one. | 案例一：總油小於總耗應回 -1。 | Edge test |
| Case two: single station feasible case. | 案例二：單站可行案例。 | Edge test |
| Case three: single station infeasible case. | 案例三：單站不可行案例。 | Edge test |
| Case four: multiple resets before final valid start. | 案例四：最終起點前會多次重設。 | Edge test |
| Case five: exact balance with unique start. | 案例五：總量平衡且起點唯一。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We use one pass for totals and one pass for greedy scan. | 我們做一趟總量計算與一趟貪心掃描。 | Complexity |
| Each pass is linear in number of stations. | 每一趟都對站點數量線性。 | Complexity |
| So runtime is O(n). | 因此時間是 O(n)。 | Complexity |
| Only constant variables are stored, so memory is O(1). | 只用常數個變數，空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate global feasibility from local start finding. | 我先把全域可行性與局部找起點分開。 | If stuck |
| Global check is total gas versus total cost. | 全域檢查是總油量對總耗油量。 | If stuck |
| If total fails, answer must be minus one. | 若總量不夠，答案一定是 -1。 | If stuck |
| For local scan, maintain currentTank. | 局部掃描維護 currentTank。 | If stuck |
| Negative currentTank means current start segment fails. | currentTank 為負代表目前起點區段失敗。 | If stuck |
| None inside that failed segment can be valid start. | 該失敗區段中的點都不可能當起點。 | If stuck |
| So jump start to next index and reset tank. | 所以起點跳到下一格並重設油量。 | If stuck |
| Let me test quickly with [2,3,4] and [3,4,3]. | 我快速測 [2,3,4] 與 [3,4,3]。 | If stuck |
| Total is insufficient, so answer is minus one. | 總量不足，所以答案是 -1。 | If stuck |
| Great, logic is consistent. | 很好，邏輯一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved gas station with total feasibility and greedy reset scan. | 我用總量可行性加重設貪心掃描解了 Gas Station。 | Wrap-up |
| Total check quickly rejects impossible inputs. | 總量檢查可快速排除無解。 | Wrap-up |
| Negative tank points define where start must move forward. | 油量轉負的位置決定起點必須前移。 | Wrap-up |
| Complexity is O(n) time and O(1) space. | 複雜度是 O(n) 時間、O(1) 空間。 | Wrap-up |
| This is the canonical interview solution. | 這是面試常見經典解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: find start index to complete circular route. | 目標：找可繞完整圈的起點。 | Cheat sheet |
| If impossible, return -1. | 不可能就回 -1。 | Cheat sheet |
| Compute totalGas and totalCost. | 計算 totalGas 與 totalCost。 | Cheat sheet |
| If totalGas<totalCost -> -1. | 若 totalGas<totalCost -> -1。 | Cheat sheet |
| Else solution exists. | 否則一定有解。 | Cheat sheet |
| Initialize start=0, currentTank=0. | 初始化 start=0、currentTank=0。 | Cheat sheet |
| Scan i from 0 to n-1. | i 從 0 掃到 n-1。 | Cheat sheet |
| currentTank += gas[i]-cost[i]. | currentTank += gas[i]-cost[i]。 | Cheat sheet |
| If currentTank<0, start=i+1. | 若 currentTank<0，start=i+1。 | Cheat sheet |
| Reset currentTank=0. | 並重設 currentTank=0。 | Cheat sheet |
| Continue scan. | 持續掃描。 | Cheat sheet |
| Return final start. | 回傳最終 start。 | Cheat sheet |
| Example [1,2,3,4,5]/[3,4,5,1,2] -> 3. | 範例 [1,2,3,4,5]/[3,4,5,1,2] -> 3。 | Cheat sheet |
| Example [2,3,4]/[3,4,3] -> -1. | 範例 [2,3,4]/[3,4,3] -> -1。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: skip total check. | 常見錯誤：漏掉總量檢查。 | Cheat sheet |
| Common bug: not resetting tank after failure. | 常見錯誤：失敗後未重設油量。 | Cheat sheet |
| Explain why failed segment cannot contain answer. | 說清楚失敗區段不可能含答案。 | Cheat sheet |
| Mention uniqueness guaranteed by problem. | 可提題目保證解唯一。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Total-sum feasibility and greedy reset logic preserved.
- No hallucinated constraints: ✅ Circular route semantics and return contract maintained.
- Language simplicity: ✅ Clean interview wording with failure-segment intuition.
