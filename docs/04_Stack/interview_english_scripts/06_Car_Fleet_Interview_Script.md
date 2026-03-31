# 06 Car Fleet — Interview English Script (C++)

> Source aligned with: `docs/04_Stack/06_Car_Fleet.md`

> Quick links: [Source Solution](../06_Car_Fleet.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| Cars move toward the same target on one lane. | 多台車在單車道往同一終點前進。 | Restatement |
| Faster rear cars can catch front cars but cannot pass. | 後車可追上前車但不能超車。 | Restatement |
| Caught cars form one fleet with same effective speed. | 追上後會形成同速車隊。 | Restatement |
| We need final number of fleets reaching target. | 我們要算到達終點的車隊數。 | Restatement |
| I will sort by position and scan from front to back. | 我會先按位置排序，再由前往後掃描。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume no two cars start at same position? | 可以假設起始位置互不相同嗎？ | Clarify |
| Is passing forbidden strictly, as in one lane? | 是否嚴格禁止超車（單車道）？ | Clarify |
| Do cars merge even if catch-up happens exactly at target? | 若剛好在終點追上，也算同車隊嗎？ | Clarify |
| Should I use floating time-to-target values? | 我應使用浮點的到達時間嗎？ | Clarify |
| Is O(n log n) acceptable due to sorting? | 因需排序，O(n log n) 是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline tries time-step simulation of all cars. | 基線是逐時間步模擬所有車。 | Approach |
| Detect catch-ups continuously during simulation. | 在模擬中持續偵測追上事件。 | Approach |
| This is complex and inefficient for large ranges. | 這在大範圍下複雜且低效。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Compute each car time to reach target. | 先計算每台車到終點所需時間。 | Approach |
| Sort cars by position descending (closest first). | 按位置降冪排序（離終點近的先）。 | Approach |
| Scan times in this order and track current fleet max time. | 依序掃時間並追蹤當前車隊瓶頸時間。 | Approach |
| If current time is greater, it starts a new fleet. | 若當前時間更大，代表新車隊。 | Approach |
| Otherwise it merges into fleet ahead. | 否則會併入前方車隊。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I pair each position with its speed. | 先把每個 position 與 speed 配對。 | Coding |
| For each pair, compute time as (target - pos) divided by speed. | 對每對資料算 time=(target-pos)/speed。 | Coding |
| Sort pairs by position from large to small. | 依 position 由大到小排序。 | Coding |
| Initialize fleets count to zero and prevTime to zero. | fleets 設 0，prevTime 設 0。 | Coding |
| Scan sorted cars in order. | 依排序順序掃描每台車。 | Coding |
| If time is greater than prevTime, increment fleets. | 若 time>prevTime，fleets 加一。 | Coding |
| Update prevTime to this new fleet time. | 並把 prevTime 更新為新車隊時間。 | Coding |
| Return fleets at the end. | 最後回傳 fleets。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run target 12 with sample cars. | 我手跑 target=12 的範例車列。 | Dry-run |
| Times after sorting by position are 1, 1, 7, 3, 12. | 依位置排序後時間是 1、1、7、3、12。 | Dry-run |
| First time 1 starts fleet one. | 第一個時間 1 形成第一隊。 | Dry-run |
| Next time 1 merges, so fleet count stays one. | 下一個時間 1 會併入，因此仍一隊。 | Dry-run |
| Time 7 is greater, so this starts fleet two. | 時間 7 較大，形成第二隊。 | Dry-run |
| Time 3 merges into fleet two, then time 12 starts fleet three. | 時間 3 併入第二隊，之後 12 形成第三隊。 | Dry-run |
| Final fleet count is 3. | 最終車隊數是 3。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: only one car should return one fleet. | 案例一：只有一台車應回傳一隊。 | Edge test |
| Case two: all cars already in increasing position order. | 案例二：車已在遞增位置分布。 | Edge test |
| Case three: all cars same speed. | 案例三：所有車速相同。 | Edge test |
| Case four: rear cars much faster and merge heavily. | 案例四：後車極快，產生大量併隊。 | Edge test |
| Case five: catch-up exactly at target boundary. | 案例五：剛好在終點追上的邊界情況。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n log n). | 時間是 O(n log n)。 | Complexity |
| Extra space is O(n). | 額外空間是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Computing times is linear over cars. | 計算時間值是線性。 | Complexity |
| Sorting by position dominates at O(n log n). | 位置排序主導為 O(n log n)。 | Complexity |
| Final scan is linear. | 最後掃描是線性。 | Complexity |
| We store car pairs and times in linear memory. | 需線性記憶體儲存車對與時間。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate no-overtake rule first. | 我先重述禁止超車規則。 | If stuck |
| Rear car can only merge, never pass. | 後車只能併隊，不能超車。 | If stuck |
| So scan order by position is critical. | 因此按位置掃描順序很關鍵。 | If stuck |
| I can show simulation idea briefly. | 我可先簡述模擬想法。 | If stuck |
| Then switch back to sorted time scan. | 再切回排序後時間掃描。 | If stuck |
| Thanks, I found sorting-direction bug. | 謝謝，我找到排序方向 bug。 | If stuck |
| Let me rerun the sample quickly. | 我快速重跑範例。 | If stuck |
| Now merge decisions are correct. | 現在併隊判斷正確。 | If stuck |
| Fleet count is consistent now. | 現在車隊數結果一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n log n). | 時間是 O(n log n)。 | Wrap-up |
| Space is O(n). | 空間是 O(n)。 | Wrap-up |
| I can discuss stack-time formulation if needed. | 若需要我可補充 stack-time 表述法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate car-fleet counting goal. | 重述車隊計數目標。 | Cheat sheet |
| Mention no-overtake one-lane rule. | 提到單車道不可超車。 | Cheat sheet |
| Compute each car time to target. | 計算每台車到終點時間。 | Cheat sheet |
| Sort by position descending. | 依位置做降冪排序。 | Cheat sheet |
| Scan from nearest car to farthest. | 由最近終點掃到最遠。 | Cheat sheet |
| Keep prevTime as current fleet bottleneck. | 用 prevTime 作當前車隊瓶頸。 | Cheat sheet |
| If time > prevTime, new fleet forms. | 若 time>prevTime，形成新車隊。 | Cheat sheet |
| Else it merges into previous fleet. | 否則併入前方車隊。 | Cheat sheet |
| Count fleets during scan. | 掃描時累計 fleet 數。 | Cheat sheet |
| Dry-run target 12 sample. | 手跑 target=12 範例。 | Cheat sheet |
| Verify result is 3 fleets. | 驗證結果為 3 隊。 | Cheat sheet |
| Test single-car case. | 測單車案例。 | Cheat sheet |
| Test same-speed case. | 測同速案例。 | Cheat sheet |
| Test heavy-merge case. | 測大量併隊案例。 | Cheat sheet |
| Report O(n log n) runtime. | 報告 O(n log n) 時間。 | Cheat sheet |
| Report O(n) extra space. | 報告 O(n) 額外空間。 | Cheat sheet |
| Mention sorting dominates complexity. | 提到排序主導複雜度。 | Cheat sheet |
| If stuck, recheck sorting order. | 卡住時重檢排序方向。 | Cheat sheet |
| Re-run sample after fix. | 修正後重跑範例。 | Cheat sheet |
| End with concise fleet summary. | 以精簡車隊結論收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sorted time-scan fleet merge logic is preserved.
- No hallucinated constraints: ✅ Assumptions are surfaced in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
