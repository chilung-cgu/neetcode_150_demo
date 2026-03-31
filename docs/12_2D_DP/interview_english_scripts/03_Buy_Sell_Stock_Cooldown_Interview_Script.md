# 03 Buy Sell Stock Cooldown — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/03_Buy_Sell_Stock_Cooldown.md`

> Quick links: [Source Solution](../03_Buy_Sell_Stock_Cooldown.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate stock trading with cooldown. | 我先重述冷凍期股票交易題。 | Restatement |
| We are given daily prices and can trade multiple times. | 題目給每日股價，可多次交易。 | Restatement |
| We can hold at most one stock at a time. | 同一時間最多持有一股。 | Restatement |
| After selling, we must cooldown for one day before buying again. | 賣出後必須冷凍一天才能再買。 | Restatement |
| We need the maximum achievable profit. | 目標是最大總利潤。 | Restatement |
| I will model it with state-machine DP. | 我會用狀態機 DP 建模。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do we start with no stock and zero profit? | 初始是否為空手且利潤 0？ | Clarify |
| Is transaction fee absent in this variant? | 這版沒有手續費對嗎？ | Clarify |
| Can we buy and sell on the same day? | 是否允許同一天買又賣？ | Clarify |
| Is one-day cooldown exactly after each sell? | 冷凍期是否固定只一天？ | Clarify |
| Is O(n) time and O(1) space expected? | O(n) 時間 O(1) 空間是否預期？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries buy, sell, or wait decisions recursively. | 暴力遞迴嘗試買、賣、等待。 | Approach |
| Cooldown introduces branching with day jumps. | 冷凍期讓分支與日期跳躍更複雜。 | Approach |
| Without memoization, complexity is exponential. | 不做記憶化時複雜度是指數級。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I track three states per day: hold, sold, rest. | 我每天追蹤 hold、sold、rest 三狀態。 | Approach |
| hold means we currently own a stock. | hold 表示目前持股。 | Approach |
| sold means we sold today. | sold 表示今天剛賣出。 | Approach |
| rest means no stock and not sold today. | rest 表示空手且今天沒賣。 | Approach |
| Transition rules give O(n) time and O(1) memory. | 轉移規則可達 O(n) 時間與 O(1) 記憶體。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize hold to negative infinity, sold to zero, rest to zero. | 我初始化 hold=-無限大、sold=0、rest=0。 | Coding |
| For each price, I store previous hold sold rest first. | 每個 price 先暫存前一日三狀態。 | Coding |
| New hold is max of keeping hold or buying from rest. | 新 hold 取續抱或從 rest 買入的最大值。 | Coding |
| New sold equals previous hold plus current price. | 新 sold 等於前一日 hold 加今日價。 | Coding |
| New rest is max of previous rest and previous sold. | 新 rest 是前一日 rest 與 sold 的最大。 | Coding |
| This enforces cooldown because buy uses previous rest only. | 買入只從舊 rest 轉移，因此自動滿足冷凍期。 | Coding |
| After loop, answer is max of sold and rest. | 迴圈後答案是 max(sold,rest)。 | Coding |
| Ending in hold is not optimal realized profit. | 以 hold 結束不代表實現利潤。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run prices [1,2,3,0,2]. | 我手跑 prices=[1,2,3,0,2]。 | Dry-run |
| Day zero sets hold to minus one after optional buy. | 第 0 天選買後 hold 變 -1。 | Dry-run |
| Day one can sell, so sold becomes one. | 第 1 天可賣，sold 變 1。 | Dry-run |
| Day two sold can reach two, while rest becomes one. | 第 2 天 sold 可到 2，rest 變 1。 | Dry-run |
| Day three buying from rest gives hold one at price zero. | 第 3 天從 rest 買入，hold 變 1（價 0）。 | Dry-run |
| Day four sell makes sold three. | 第 4 天賣出讓 sold 變 3。 | Dry-run |
| Final max of sold and rest is three. | 最終 max(sold,rest)=3。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single day should return zero. | 案例一：只有一天應回 0。 | Edge test |
| Case two: strictly decreasing prices should return zero. | 案例二：持續下跌應回 0。 | Edge test |
| Case three: alternating peaks validates cooldown handling. | 案例三：高低交替可驗證冷凍期處理。 | Edge test |
| Case four: long flat prices should produce zero profit. | 案例四：長期平盤應為 0 利潤。 | Edge test |
| Case five: immediate re-buy temptation after sell. | 案例五：賣後隔天想再買的情境。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan prices array once from left to right. | 我們對價格陣列做一次線性掃描。 | Complexity |
| Each day updates only three scalar states. | 每天只更新三個純量狀態。 | Complexity |
| Therefore runtime is linear O(n). | 因此總時間是線性 O(n)。 | Complexity |
| No DP table is used, so extra memory is O(1). | 不需要 DP 表，額外記憶體是 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me switch to state-machine thinking. | 我改用狀態機思考。 | If stuck |
| I need three states: hold sold rest. | 我需要三個狀態：hold、sold、rest。 | If stuck |
| hold means I have stock at day end. | hold 是收盤時手上有股。 | If stuck |
| sold means I sold today. | sold 是今天剛賣。 | If stuck |
| rest means no stock and no sell today. | rest 是空手且今天沒賣。 | If stuck |
| Buying must come from previous rest only. | 買入只能從前一天 rest 來。 | If stuck |
| That is exactly how cooldown is enforced. | 這正是冷凍期約束。 | If stuck |
| Let me test [1,2,3,0,2] quickly. | 我快速測 [1,2,3,0,2]。 | If stuck |
| It gives three profit as expected. | 會得到預期利潤 3。 | If stuck |
| Great, transitions are validated. | 很好，轉移已驗證。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved this with constant-space state DP. | 我用常數空間狀態 DP 解此題。 | Wrap-up |
| The three states are hold sold and rest. | 三個狀態是 hold、sold、rest。 | Wrap-up |
| Cooldown is naturally encoded in transition rules. | 冷凍期已自然內建於轉移規則。 | Wrap-up |
| Complexity is O(n) time and O(1) space. | 複雜度是 O(n) 時間、O(1) 空間。 | Wrap-up |
| This is concise and interview-friendly to explain. | 這解法簡潔且面試易說明。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: maximize stock profit with one-day cooldown. | 目標：含一天冷凍期下最大化利潤。 | Cheat sheet |
| One stock at most can be held. | 最多持有一股。 | Cheat sheet |
| Define states hold sold rest. | 定義狀態 hold、sold、rest。 | Cheat sheet |
| hold: own stock at end of day. | hold：收盤時持股。 | Cheat sheet |
| sold: sold today. | sold：今天賣出。 | Cheat sheet |
| rest: no stock and no sell today. | rest：空手且今天沒賣。 | Cheat sheet |
| Initialize hold=-inf sold=0 rest=0. | 初始化 hold=-inf、sold=0、rest=0。 | Cheat sheet |
| Save previous states each iteration. | 每輪先保存前一日狀態。 | Cheat sheet |
| hold=max(prevHold, prevRest-price). | hold=max(prevHold,prevRest-price)。 | Cheat sheet |
| sold=prevHold+price. | sold=prevHold+price。 | Cheat sheet |
| rest=max(prevRest, prevSold). | rest=max(prevRest,prevSold)。 | Cheat sheet |
| Answer=max(sold, rest). | 答案=max(sold,rest)。 | Cheat sheet |
| Example [1,2,3,0,2] -> 3. | 範例 [1,2,3,0,2] -> 3。 | Cheat sheet |
| Single day -> 0. | 單日 -> 0。 | Cheat sheet |
| Decreasing prices -> 0. | 遞減價格 -> 0。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: buying from prevSold (invalid). | 常見錯誤：從 prevSold 買入（不合法）。 | Cheat sheet |
| Common bug: overwriting states without temp vars. | 常見錯誤：未用暫存導致覆寫錯誤。 | Cheat sheet |
| Explain cooldown through transition source. | 用轉移來源解釋冷凍期。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ hold/sold/rest transitions and cooldown semantics preserved.
- No hallucinated constraints: ✅ One-share constraint and one-day cooldown correctly captured.
- Language simplicity: ✅ State-machine explanation is concise and interview-ready.
