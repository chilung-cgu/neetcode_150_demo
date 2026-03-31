# 01 Best Time to Buy and Sell Stock — Interview English Script (C++)

> Source aligned with: `docs/03_Sliding_Window/01_Best_Time_to_Buy_and_Sell_Stock.md`

> Quick links: [Source Solution](../01_Best_Time_to_Buy_and_Sell_Stock.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| prices[i] is the stock price on day i. | prices[i] 是第 i 天股價。 | Restatement |
| I can buy once and sell once only. | 我只能買一次、賣一次。 | Restatement |
| Sell day must be after buy day. | 賣出日必須晚於買入日。 | Restatement |
| We want the maximum profit value. | 我們要最大利潤值。 | Restatement |
| If no profit is possible, return zero. | 如果無法獲利就回傳 0。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume exactly one transaction is allowed? | 可以假設只允許一筆交易嗎？ | Clarify |
| Are prices guaranteed to be non-negative integers? | prices 是否保證為非負整數？ | Clarify |
| Is returning profit value enough, no days needed? | 只回傳利潤值，不用回傳日期對嗎？ | Clarify |
| Should strictly decreasing prices return zero? | 嚴格遞減價格是否回傳 0？ | Clarify |
| Is O(n) expected because n can be large? | 因為 n 很大，預期 O(n) 對嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline checks every buy day and later sell day. | 基線是枚舉每個買入日與後續賣出日。 | Approach |
| Compute prices[j] minus prices[i] for all pairs. | 對所有配對計算 prices[j]-prices[i]。 | Approach |
| Time O(n^2), space O(1). | 時間 O(n^2)，空間 O(1)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Keep the minimum price seen so far. | 維護到目前為止的最低價。 | Approach |
| At each day, selling profit is current minus minPrice. | 每一天的賣出利潤是當前價減 minPrice。 | Approach |
| Update best profit with that candidate. | 用這個候選值更新最大利潤。 | Approach |
| If current price is lower, refresh minPrice. | 若當前價更低，就更新 minPrice。 | Approach |
| One pass gives O(n) time and O(1) space. | 一趟掃描可達 O(n) 時間、O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I set minPrice to a very large value. | 先把 minPrice 設成很大值。 | Coding |
| I also set maxProfit to zero. | 同時把 maxProfit 設為 0。 | Coding |
| Then I scan each price from left to right. | 然後由左到右掃描每個價格。 | Coding |
| If price is lower than minPrice, update minPrice. | 若價格低於 minPrice，就更新它。 | Coding |
| Otherwise compute price minus minPrice. | 否則計算 price-minPrice。 | Coding |
| If that profit is larger, update maxProfit. | 若利潤更大，就更新 maxProfit。 | Coding |
| This guarantees buy happens before sell. | 這可保證先買後賣。 | Coding |
| Finally return maxProfit. | 最後回傳 maxProfit。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [7,1,5,3,6,4]. | 我手跑 [7,1,5,3,6,4]。 | Dry-run |
| Start with minPrice as infinity and profit zero. | 起始 minPrice 是無限大，profit 為 0。 | Dry-run |
| See 7, minPrice becomes 7. | 看到 7，minPrice 變 7。 | Dry-run |
| See 1, minPrice becomes 1. | 看到 1，minPrice 變 1。 | Dry-run |
| See 5, candidate profit is 4, update best. | 看到 5，候選利潤 4，更新。 | Dry-run |
| See 6, candidate profit is 5, update again. | 看到 6，候選利潤 5，再更新。 | Dry-run |
| Final best profit is 5. | 最終最大利潤是 5。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single day input like [5]. | 案例一：單日輸入如 [5]。 | Edge test |
| Case two: strictly decreasing prices. | 案例二：價格嚴格遞減。 | Edge test |
| Case three: all prices equal. | 案例三：所有價格相同。 | Edge test |
| Case four: best buy appears after early highs. | 案例四：最佳買點出現在前段高價之後。 | Edge test |
| Case five: best profit occurs near array end. | 案例五：最佳利潤出現在接近尾端。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan the prices array exactly once. | 我們只完整掃過陣列一次。 | Complexity |
| Each iteration does constant-time updates. | 每輪只做常數時間更新。 | Complexity |
| No nested loops are needed. | 不需要巢狀迴圈。 | Complexity |
| Only two scalars are maintained. | 只需維護兩個標量變數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate one transaction rule. | 我先重述單筆交易規則。 | If stuck |
| Buy must be earlier than sell. | 買入必須早於賣出。 | If stuck |
| I can explain brute force first. | 我可先說明暴力法。 | If stuck |
| Then I compress to one-pass state. | 再壓縮成一趟狀態維護。 | If stuck |
| I only need minPrice and maxProfit. | 我只需要 minPrice 與 maxProfit。 | If stuck |
| Thanks, I found an update-order bug. | 謝謝，我找到更新順序錯誤。 | If stuck |
| Let me rerun the sample quickly. | 我快速重跑範例。 | If stuck |
| Now buy and sell order is correct. | 現在買賣順序正確。 | If stuck |
| The final profit is stable. | 最終利潤結果穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can discuss multi-transaction variants if needed. | 若需要我可延伸多次交易版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate one-buy-one-sell goal. | 重述單買單賣目標。 | Cheat sheet |
| Clarify sell must be later. | 釐清賣出一定要更晚。 | Cheat sheet |
| Brute force checks all day pairs. | 暴力法檢查所有日配對。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法是 O(n^2)。 | Cheat sheet |
| Optimized keeps running minPrice. | 優化法維護動態 minPrice。 | Cheat sheet |
| For each day compute candidate profit. | 每天計算候選利潤。 | Cheat sheet |
| Update maxProfit if larger. | 若更大就更新 maxProfit。 | Cheat sheet |
| Update minPrice when lower price appears. | 若出現更低價就更新 minPrice。 | Cheat sheet |
| This enforces correct time order. | 這會自動保證時間順序。 | Cheat sheet |
| Dry-run [7,1,5,3,6,4]. | 手跑 [7,1,5,3,6,4]。 | Cheat sheet |
| Verify answer is 5. | 驗證答案為 5。 | Cheat sheet |
| Test decreasing case gives 0. | 測遞減案例應為 0。 | Cheat sheet |
| Test equal-price case gives 0. | 測等價案例應為 0。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(1) extra space. | 報告 O(1) 額外空間。 | Cheat sheet |
| Mention this is one-pass greedy state. | 提到這是一趟貪心狀態法。 | Cheat sheet |
| If stuck, restate update order. | 卡住時重述更新順序。 | Cheat sheet |
| Re-run sample after fix. | 修正後重跑範例。 | Cheat sheet |
| End with concise complexity summary. | 用精簡複雜度總結收尾。 | Cheat sheet |
| Offer follow-up on Stock II/III variants. | 提供 Stock II/III 延伸討論。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ One-pass minPrice/maxProfit logic is preserved.
- No hallucinated constraints: ✅ Uncertain requirements are asked in clarification lines.
- Language simplicity: ✅ Short spoken lines suitable for interview delivery.
