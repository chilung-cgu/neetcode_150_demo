# 05 Trapping Rain Water — Interview English Script (C++)

> Source aligned with: `docs/02_Two_Pointers/05_Trapping_Rain_Water.md`

> Quick links: [Source Solution](../05_Trapping_Rain_Water.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| The array represents bar heights of width one. | 陣列代表寬度為一的柱狀高度。 | Restatement |
| Rain water can be trapped between higher bars. | 雨水會被較高柱子夾住。 | Restatement |
| We need total trapped water units. | 我們要算總接水量。 | Restatement |
| I will use two pointers with leftMax and rightMax. | 我會用雙指標搭配 leftMax、rightMax。 | Restatement |
| Then I will justify why local side is decidable. | 接著我會說明為何可局部決策。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume height values are non-negative? | 可以假設高度都非負嗎？ | Clarify |
| For length below three, should result be zero? | 長度小於 3 時結果是否為 0？ | Clarify |
| Is O(n) time and O(1) space expected? | 預期要做到 O(n) 時間與 O(1) 空間嗎？ | Clarify |
| Should I also mention DP or stack alternatives? | 需要順帶提 DP 或 stack 解法嗎？ | Clarify |
| Can answer fit in 32-bit int under constraints? | 在限制下答案可放 32-bit int 嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline handles each index independently. | 基線是逐一處理每個位置。 | Approach |
| For each i, scan left max and right max. | 對每個 i，掃左側最高與右側最高。 | Approach |
| Time O(n^2), space O(1). | 時間 O(n^2)，空間 O(1)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Keep two pointers at both ends. | 兩個指標放在陣列兩端。 | Approach |
| Track leftMax and rightMax as current walls. | 用 leftMax、rightMax 追蹤目前牆高。 | Approach |
| If leftMax is smaller, left side water is decidable. | 若 leftMax 較小，左側可直接決定水量。 | Approach |
| Otherwise right side water is decidable. | 否則可直接決定右側水量。 | Approach |
| This gives O(n) time and O(1) extra space. | 這樣可達 O(n) 時間與 O(1) 額外空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I set left to zero and right to n minus one. | 先設 left=0、right=n-1。 | Coding |
| I initialize leftMax and rightMax from boundary bars. | 用邊界柱初始化 leftMax、rightMax。 | Coding |
| While left is smaller than right, I compare both maxima. | 當 left<right，我比較兩側最大值。 | Coding |
| If leftMax is smaller, move left one step. | 若 leftMax 較小，就把 left 右移一步。 | Coding |
| Update leftMax and add leftMax minus height[left]. | 更新 leftMax，累加 leftMax-height[left]。 | Coding |
| Else move right, update rightMax, add trapped water. | 否則左移 right，更新 rightMax 並累加水量。 | Coding |
| Each step finalizes one index without revisiting. | 每一步都能定案一個索引，不需回頭。 | Coding |
| At the end, return total water. | 最後回傳總接水量。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run [0,1,0,2,1,0,1,3,2,1,2,1]. | 我手跑 [0,1,0,2,1,0,1,3,2,1,2,1]。 | Dry-run |
| Start with left at 0, right at 11. | 起始 left=0、right=11。 | Dry-run |
| leftMax is 0 and rightMax is 1, so process left side. | leftMax=0、rightMax=1，先處理左側。 | Dry-run |
| Moving left, trapped water appears at low valleys. | 左指標右移時，低谷位置會累積水量。 | Dry-run |
| Later when rightMax becomes limiting, process right side. | 後續若 rightMax 成瓶頸，就處理右側。 | Dry-run |
| Summing all finalized positions gives 6. | 全部定案位置加總得到 6。 | Dry-run |
| Final answer is 6. | 最終答案是 6。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: empty or very short array returns zero. | 案例一：空陣列或過短輸入回傳 0。 | Edge test |
| Case two: monotonic increasing bars trap zero water. | 案例二：單調遞增柱高接不到水。 | Edge test |
| Case three: monotonic decreasing bars also trap zero. | 案例三：單調遞減也接不到水。 | Edge test |
| Case four: classic valley like [3,0,2,0,4]. | 案例四：經典低谷如 [3,0,2,0,4]。 | Edge test |
| Case five: flat plateau segments mixed with pits. | 案例五：平臺區段混合凹槽。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1). | 額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each pointer moves inward at most n times total. | 每個指標向內最多移動線性次數。 | Complexity |
| No index is processed more than once. | 每個索引都只會被定案一次。 | Complexity |
| So runtime is linear. | 因此執行時間是線性。 | Complexity |
| We only keep four integers and one accumulator. | 我們只需四個整數與一個累加器。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me restate water formula at one index. | 我先重述單點水量公式。 | If stuck |
| I compare leftMax and rightMax, not raw heights. | 我比較的是 leftMax/rightMax，不是原始高度。 | If stuck |
| Smaller max side can be finalized now. | 較小 max 那一側可立即定案。 | If stuck |
| I can explain DP arrays first if needed. | 若需要我可先講 DP 陣列版。 | If stuck |
| Then I compress it into O(1) pointers. | 再壓縮成 O(1) 雙指標。 | If stuck |
| Thanks, I found the update-order bug. | 謝謝，我找到更新順序錯誤。 | If stuck |
| Let me rerun the valley example quickly. | 我快速重跑低谷範例。 | If stuck |
| Now trapped-water accumulation is correct. | 現在接水量累加正確。 | If stuck |
| The final total matches expected output. | 最終總量符合預期輸出。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| I verified normal and edge test patterns. | 我驗證了常見與邊界測試型態。 | Wrap-up |
| Time is O(n). | 時間是 O(n)。 | Wrap-up |
| Extra space is O(1). | 額外空間是 O(1)。 | Wrap-up |
| I can compare DP and stack alternatives if needed. | 若需要我可比較 DP 與 stack 方案。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate total trapped-water goal. | 重述總接水量目標。 | Cheat sheet |
| Mention unit width bars. | 提到每個柱子寬度為 1。 | Cheat sheet |
| Brute force scans left and right per index. | 暴力法每點都掃左右最高。 | Cheat sheet |
| Brute force is O(n^2). | 暴力法是 O(n^2)。 | Cheat sheet |
| Optimized keeps two pointers. | 優化法保留雙指標。 | Cheat sheet |
| Track leftMax and rightMax. | 追蹤 leftMax 與 rightMax。 | Cheat sheet |
| Compare maxima, not current heights only. | 比較兩側 max，不只看當前高度。 | Cheat sheet |
| Finalize smaller-max side immediately. | 較小 max 那側可立即定案。 | Cheat sheet |
| Add max minus current height. | 累加 max 減目前高度。 | Cheat sheet |
| Move that pointer inward. | 移動該側指標往內。 | Cheat sheet |
| Repeat until pointers meet. | 重複直到指標相遇。 | Cheat sheet |
| Dry-run [0,1,0,2,1,0,1,3,2,1,2,1]. | 手跑 [0,1,0,2,1,0,1,3,2,1,2,1]。 | Cheat sheet |
| Confirm result equals 6. | 確認結果是 6。 | Cheat sheet |
| Test monotonic increasing case. | 測單調遞增案例。 | Cheat sheet |
| Test monotonic decreasing case. | 測單調遞減案例。 | Cheat sheet |
| Test valley-rich case. | 測多低谷案例。 | Cheat sheet |
| Report O(n) runtime. | 報告 O(n) 時間。 | Cheat sheet |
| Report O(1) extra space. | 報告 O(1) 額外空間。 | Cheat sheet |
| If stuck, restate finalize rule. | 卡住時重述定案規則。 | Cheat sheet |
| End with concise summary. | 用精簡總結收尾。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Two-pointer with leftMax/rightMax logic is preserved.
- No hallucinated constraints: ✅ Uncertain details are handled via clarification questions.
- Language simplicity: ✅ Short spoken lines for interview delivery.
