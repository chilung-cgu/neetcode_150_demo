# 04 Happy Number — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/04_Happy_Number.md`

> Quick links: [Source Solution](../04_Happy_Number.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Happy Number. | 我先重述 Happy Number。 | Restatement |
| Starting from n, we repeatedly replace it by sum of squared digits. | 從 n 開始，反覆改成各位平方和。 | Restatement |
| If the process reaches one, it is happy. | 若最後到 1，就是快樂數。 | Restatement |
| If it enters a cycle not containing one, it is not happy. | 若進入不含 1 的循環，就不是快樂數。 | Restatement |
| I will detect the cycle using fast and slow pointers. | 我會用快慢指標偵測循環。 | Restatement |
| This avoids hash set and keeps O(1) extra space. | 這可避免 HashSet，維持 O(1) 額外空間。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is input guaranteed to be a positive integer? | 輸入是否保證為正整數？ | Clarify |
| Should n equals one return true immediately? | n=1 是否應立即回 true？ | Clarify |
| Do you prefer Floyd cycle detection over hash set? | 你偏好 Floyd 檢測而非 HashSet 嗎？ | Clarify |
| Any constraints that affect integer overflow here? | 這題是否有整數溢位顧慮？ | Clarify |
| Is helper function for digit-square-sum acceptable? | 可以用輔助函式算各位平方和嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force uses a hash set to record seen numbers. | 暴力法用 HashSet 記錄已出現數字。 | Approach |
| If we hit one, return true; if number repeats, return false. | 若到 1 回 true，若重複則回 false。 | Approach |
| Time is acceptable, but space is O(k) for visited states. | 時間可接受，但空間要 O(k) 儲存狀態。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Model each value as a node pointing to next sum-of-squares value. | 把每個值視為節點，連到下一個平方和。 | Approach |
| Then the process is a linked-list style walk with possible cycle. | 於是流程像鏈結串列，可能有環。 | Approach |
| Use slow pointer moving one step and fast pointer moving two steps. | slow 每次一步，fast 每次兩步。 | Approach |
| If fast reaches one, it is happy; if slow meets fast, there is a non-one cycle. | fast 到 1 則快樂；slow 與 fast 相遇則是非 1 循環。 | Approach |
| Complexity is O(log n) per step work with O(1) extra space overall. | 每步計算約 O(log n)，整體額外空間 O(1)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I write helper sumOfSquares that processes digits by modulo and division. | 我先寫 sumOfSquares，用取餘與除法處理每位。 | Coding |
| In main function, set slow to n. | 主函式先令 slow=n。 | Coding |
| Set fast to sumOfSquares of n. | 令 fast=sumOfSquares(n)。 | Coding |
| While fast is not one and slow is not fast, continue loop. | 當 fast!=1 且 slow!=fast 持續迴圈。 | Coding |
| Move slow by one application of sumOfSquares. | slow 每輪走一步 sumOfSquares。 | Coding |
| Move fast by two applications of sumOfSquares. | fast 每輪走兩步 sumOfSquares。 | Coding |
| Loop ends either by reaching one or by cycle collision. | 迴圈結束要嘛到 1，要嘛碰撞成環。 | Coding |
| Return whether fast equals one. | 回傳 fast 是否等於 1。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run n equals nineteen. | 我用 n=19 手跑。 | Dry-run |
| Nineteen goes to eighty-two, then sixty-eight, then one hundred, then one. | 19 會到 82，再到 68，再到 100，再到 1。 | Dry-run |
| Fast pointer reaches one during iterations. | fast 指標在迭代中到達 1。 | Dry-run |
| So loop exits with success condition. | 因此以成功條件離開迴圈。 | Dry-run |
| Return true for nineteen. | 19 回傳 true。 | Dry-run |
| For n equals two, pointers eventually meet in cycle without one. | 若 n=2，指標會在不含 1 的循環中相遇。 | Dry-run |
| That correctly returns false. | 這會正確回傳 false。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals one should return true. | 案例一：n=1 應回 true。 | Edge test |
| Case two: n equals two should return false. | 案例二：n=2 應回 false。 | Edge test |
| Case three: numbers with many digits. | 案例三：位數很多的整數。 | Edge test |
| Case four: known happy number like seven. | 案例四：已知快樂數如 7。 | Edge test |
| Case five: known unhappy cycle members like four. | 案例五：已知不快樂循環成員如 4。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is effectively O(log n) per transition with bounded cycle behavior. | 時間可視為每次轉移 O(log n)，且循環範圍有界。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Computing next value scans decimal digits, which is O(log n). | 計算下一值需掃十進位位數，為 O(log n)。 | Complexity |
| The sequence quickly falls into a small bounded range. | 序列很快會落到一個小且有界的範圍。 | Complexity |
| Floyd cycle detection uses constant number of integers. | Floyd 檢測只用固定數量整數變數。 | Complexity |
| So memory is O(1) and practical runtime is very small. | 因此記憶體 O(1)，實務時間也很小。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me treat each number as a node in a functional graph. | 我把每個數字視為函數圖節點。 | If stuck |
| Next state is sum of squared digits. | 下一狀態是各位平方和。 | If stuck |
| This is cycle detection, so Floyd fits naturally. | 這本質是找環，所以 Floyd 很適合。 | If stuck |
| Slow moves one step, fast moves two steps. | slow 一步、fast 兩步。 | If stuck |
| If fast reaches one, we are done with true. | 若 fast 到 1，就回 true。 | If stuck |
| If slow meets fast before one, we found unhappy cycle. | 若先相遇，表示是不快樂循環。 | If stuck |
| I will write helper first to avoid arithmetic mistakes. | 我先寫輔助函式避免算術錯誤。 | If stuck |
| Let me verify with nineteen and two quickly. | 我快速驗證 19 與 2。 | If stuck |
| Both examples validate opposite outcomes clearly. | 兩例可清楚驗證正反結果。 | If stuck |
| Great, the logic is stable now. | 很好，邏輯現在穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it by Floyd cycle detection on digit-square transitions. | 我用 Floyd 在平方和轉移上做循環檢測。 | Wrap-up |
| This removes need for extra visited set memory. | 這不需要額外 visited 集合空間。 | Wrap-up |
| Helper function keeps digit processing clear and testable. | 輔助函式讓位數處理更清楚可測。 | Wrap-up |
| Complexity is O(1) extra space with small practical runtime. | 複雜度是 O(1) 額外空間，實務速度很快。 | Wrap-up |
| I can also show the hash-set variant for comparison. | 若需要我也可補充 HashSet 對照版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: decide if repeated digit-square process reaches one. | 目標：判斷反覆平方和是否到 1。 | Cheat sheet |
| Happy if reaches one. | 到 1 就是快樂數。 | Cheat sheet |
| Unhappy if falls into non-one cycle. | 掉進非 1 循環就不是。 | Cheat sheet |
| Helper: sum of squares of digits. | 輔助：計算各位平方和。 | Cheat sheet |
| Build with n%10 and n/=10 loop. | 用 n%10 與 n/=10 迴圈實作。 | Cheat sheet |
| Use Floyd cycle detection. | 使用 Floyd 快慢指標。 | Cheat sheet |
| slow = n, fast = next(n). | slow=n，fast=next(n)。 | Cheat sheet |
| slow moves one step each round. | slow 每輪走一步。 | Cheat sheet |
| fast moves two steps each round. | fast 每輪走兩步。 | Cheat sheet |
| Stop if fast == 1. | fast==1 即停止。 | Cheat sheet |
| Stop if slow == fast before one. | 若先 slow==fast 也停止。 | Cheat sheet |
| Return fast == 1. | 回傳 fast==1。 | Cheat sheet |
| Test n=19 should be true. | 測 n=19 應為 true。 | Cheat sheet |
| Test n=2 should be false. | 測 n=2 應為 false。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Per transition digit work is O(log n). | 每次轉移位數運算 O(log n)。 | Cheat sheet |
| Common bug: forgetting fast starts one step ahead. | 常見錯誤：忘記 fast 先走一步。 | Cheat sheet |
| Common bug: wrong digit-square helper. | 常見錯誤：輔助函式位數平方算錯。 | Cheat sheet |
| Keep loop condition fast!=1 and slow!=fast. | 迴圈條件維持 fast!=1 且 slow!=fast。 | Cheat sheet |
| Clear, interview-ready cycle framing. | 用循環檢測框架講解很面試友善。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Floyd fast/slow method.
- Constraint alignment: ✅ O(1) extra space maintained.
- Language simplicity: ✅ Compact and spoken-interview oriented.
