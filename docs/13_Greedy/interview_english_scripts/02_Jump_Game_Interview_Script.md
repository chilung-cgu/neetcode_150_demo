# 02 Jump Game — Interview English Script (C++)

> Source aligned with: `docs/13_Greedy/02_Jump_Game.md`

> Quick links: [Source Solution](../02_Jump_Game.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate jump game. | 我先重述 Jump Game。 | Restatement |
| We start at index zero in array nums. | 我們從陣列 nums 的索引 0 出發。 | Restatement |
| nums[i] is maximum jump length from i. | nums[i] 代表從 i 可跳的最遠長度。 | Restatement |
| We need to decide if last index is reachable. | 要判斷是否能到達最後一格。 | Restatement |
| Return true if reachable, otherwise false. | 可達回 true，不可達回 false。 | Restatement |
| I will use greedy goal-shifting from right to left. | 我會用由右往左的貪心目標回推。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is nums guaranteed non-empty? | nums 是否保證非空？ | Clarify |
| Are all values non-negative? | 所有值是否都是非負？ | Clarify |
| Do we only return reachability boolean? | 是否只回可達性的布林值？ | Clarify |
| Can we assume indices fit in integer arithmetic safely? | 索引運算可安全放在整數內嗎？ | Clarify |
| Is O(n) greedy expected over O(n squared) DP? | 是否期望 O(n) 貪心而非 O(n²) DP？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries all jump choices recursively. | 暴力遞迴嘗試所有跳躍選擇。 | Approach |
| Many positions are revisited across branches. | 許多位置會在不同分支重複訪問。 | Approach |
| This can degrade to exponential behavior. | 這可能退化成指數行為。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Set goal as last index initially. | 一開始把 goal 設為最後索引。 | Approach |
| Traverse i from right to left. | 從右往左掃描每個 i。 | Approach |
| If i plus nums[i] reaches goal, shift goal to i. | 若 i+nums[i] 可達 goal，就把 goal 移到 i。 | Approach |
| Intuition: now we only need to reach this new closer goal. | 直覺上只要能到新 goal 就等價可達終點。 | Approach |
| Finally, return whether goal becomes zero. | 最後看 goal 是否回推到 0。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize goal as nums.size minus one. | 我先把 goal 初始化為 nums.size-1。 | Coding |
| I loop i from second last index down to zero. | i 從倒數第二格往左到 0。 | Coding |
| For each i, I check if i plus nums[i] is at least goal. | 每個 i 檢查 i+nums[i] 是否至少到 goal。 | Coding |
| If yes, I update goal to i. | 若可達，我就把 goal 更新為 i。 | Coding |
| This means index i can reach previous goal position. | 這表示 i 可到達先前的目標位置。 | Coding |
| Loop continues until index zero. | 迴圈持續到索引 0。 | Coding |
| After loop, I return goal equals zero. | 迴圈後回傳 goal==0。 | Coding |
| That gives final reachability decision. | 這就是最終可達性判定。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [2,3,1,1,4]. | 我手跑 nums=[2,3,1,1,4]。 | Dry-run |
| Initial goal is index four. | 初始 goal 是索引 4。 | Dry-run |
| At i three, three plus one reaches four, so goal becomes three. | i=3 時 3+1 可到 4，goal 變 3。 | Dry-run |
| At i two, two plus one reaches three, so goal becomes two. | i=2 時 2+1 可到 3，goal 變 2。 | Dry-run |
| At i one, one plus three reaches four, so goal becomes one. | i=1 時 1+3 可到 4，goal 變 1。 | Dry-run |
| At i zero, zero plus two reaches two, so goal becomes zero. | i=0 時 0+2 可到 2，goal 變 0。 | Dry-run |
| Goal is zero, so answer is true. | goal 最終為 0，所以答案 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element array should be true. | 案例一：單元素陣列應為 true。 | Edge test |
| Case two: zero trap like [3,2,1,0,4] should be false. | 案例二：0 陷阱如 [3,2,1,0,4] 應 false。 | Edge test |
| Case three: first jump already reaches end. | 案例三：第一跳就能到終點。 | Edge test |
| Case four: many zeros but still reachable path. | 案例四：含多個 0 但仍有可達路徑。 | Edge test |
| Case five: long array with late failure point. | 案例五：長陣列在後段才失敗。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan the array once from right to left. | 我們由右往左只掃描一次陣列。 | Complexity |
| Each index does constant-time reachability check. | 每個索引只做常數時間判斷。 | Complexity |
| So total runtime is O(n). | 因此總時間為 O(n)。 | Complexity |
| We store only one goal variable, so memory is O(1). | 只儲存一個 goal 變數，空間為 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me switch to backward greedy perspective. | 我改用反向貪心視角。 | If stuck |
| Goal starts at the last index. | goal 一開始在最後索引。 | If stuck |
| If an index can reach goal, move goal back. | 若某索引可達 goal，就把 goal 往前移。 | If stuck |
| This compresses the problem gradually. | 這會逐步壓縮問題範圍。 | If stuck |
| I only need one pass from right to left. | 我只需要一次由右往左掃描。 | If stuck |
| Let me test quickly with [3,2,1,0,4]. | 我快速測 [3,2,1,0,4]。 | If stuck |
| Goal cannot cross index four backward to zero there. | 在該例中 goal 無法回推到 0。 | If stuck |
| So result should be false. | 因此結果應為 false。 | If stuck |
| That confirms trap-zero behavior. | 這確認了 0 陷阱的行為。 | If stuck |
| Great, logic is now solid. | 很好，邏輯已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved jump game with backward greedy goal shifting. | 我用反向目標回推貪心解了 Jump Game。 | Wrap-up |
| We keep shrinking required reachable index. | 我們持續縮小必要可達目標索引。 | Wrap-up |
| If goal reaches zero, start can reach end. | 若 goal 回到 0，代表起點可達終點。 | Wrap-up |
| Complexity is O(n) time and O(1) space. | 複雜度是 O(n) 時間與 O(1) 空間。 | Wrap-up |
| This is the standard optimal interview solution. | 這是面試常見最優解。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: decide if last index is reachable. | 目標：判斷最後索引是否可達。 | Cheat sheet |
| nums[i] is max jump from i. | nums[i] 是從 i 可跳最大步數。 | Cheat sheet |
| Use backward greedy. | 使用反向貪心。 | Cheat sheet |
| Initialize goal = n-1. | 初始化 goal=n-1。 | Cheat sheet |
| Iterate i from n-2 down to 0. | i 從 n-2 到 0。 | Cheat sheet |
| If i+nums[i] >= goal, set goal=i. | 若 i+nums[i]>=goal，設 goal=i。 | Cheat sheet |
| End condition: goal==0. | 結束條件：goal==0。 | Cheat sheet |
| Return goal==0. | 回傳 goal==0。 | Cheat sheet |
| [2,3,1,1,4] -> true. | [2,3,1,1,4] -> true。 | Cheat sheet |
| [3,2,1,0,4] -> false. | [3,2,1,0,4] -> false。 | Cheat sheet |
| Single element -> true. | 單元素 -> true。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: forward logic with wrong max handling. | 常見錯誤：前向寫法中最遠值維護錯。 | Cheat sheet |
| Common bug: off-by-one around last index. | 常見錯誤：最後索引 off-by-one。 | Cheat sheet |
| Backward view is easy to explain. | 反向視角很容易說明。 | Cheat sheet |
| You can also mention forward reachable variant. | 也可補充前向 reachable 版本。 | Cheat sheet |
| Validate with zero-trap case. | 需驗證 0 陷阱案例。 | Cheat sheet |
| Keep condition i+nums[i]>=goal clear. | 明確強調條件 i+nums[i]>=goal。 | Cheat sheet |
| Final decision is simple boolean. | 最終判定是簡單布林值。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Backward goal-post greedy preserved.
- No hallucinated constraints: ✅ Reachability boolean semantics maintained.
- Language simplicity: ✅ Short interview-safe explanation with clear condition.
