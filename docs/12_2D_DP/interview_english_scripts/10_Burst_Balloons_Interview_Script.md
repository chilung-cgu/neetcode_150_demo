# 10 Burst Balloons — Interview English Script (C++)

> Source aligned with: `docs/12_2D_DP/10_Burst_Balloons.md`

> Quick links: [Source Solution](../10_Burst_Balloons.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate burst balloons. | 我先重述 Burst Balloons。 | Restatement |
| We have an array where bursting balloon i gives left times i times right coins. | 戳破第 i 顆可得左*中*右硬幣數。 | Restatement |
| After bursting, neighbors become adjacent dynamically. | 戳破後相鄰關係會動態改變。 | Restatement |
| We need the maximum coins after bursting all balloons. | 目標是戳完全部後的最大硬幣數。 | Restatement |
| Virtual boundaries outside array are value one. | 陣列外邊界視為 1。 | Restatement |
| I will use interval DP with reverse thinking. | 我會用反向思考的區間 DP。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are boundary virtual balloons fixed as one? | 邊界虛擬氣球固定為 1 嗎？ | Clarify |
| Can nums contain zero values? | nums 可能包含 0 嗎？ | Clarify |
| Do we return maximum coins only? | 是否只回最大硬幣數？ | Clarify |
| Is n up to three hundred as constraints state? | 限制是否 n 最多 300？ | Clarify |
| Is O(n cubed) interval DP acceptable? | O(n³) 區間 DP 可接受嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tries every bursting order permutation. | 暴力法會嘗試所有戳破順序排列。 | Approach |
| Neighbor changes make subproblems unstable in forward view. | 前向視角下鄰居變動使子問題不穩定。 | Approach |
| Complexity is factorial-like and infeasible. | 複雜度接近階乘，無法實用。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Key trick is to pick the last balloon burst in an interval. | 關鍵是改想「區間內最後戳哪顆」。 | Approach |
| Add one at both ends to simplify boundary handling. | 首尾各補 1 以簡化邊界。 | Approach |
| Let dp[left][right] be best coins in open interval left right. | 定義 dp[left][right] 為開區間最佳收益。 | Approach |
| Try each k between left and right as last burst. | 枚舉區間內每個 k 當最後戳破。 | Approach |
| Transition combines left part right part and boundary product. | 轉移為左區間+右區間+邊界乘積。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I build new array arr by padding one on both sides. | 我先建立首尾補 1 的 arr。 | Coding |
| I create dp table sized n plus two by n plus two initialized zero. | 建立 (n+2)*(n+2) 的零初始化 dp。 | Coding |
| I iterate interval length len from one to n. | 區間長度 len 從 1 到 n。 | Coding |
| For each left boundary, right equals left plus len plus one. | 對每個 left，right=left+len+1。 | Coding |
| I enumerate k in open interval as last burst balloon. | 我枚舉開區間內 k 當最後戳破點。 | Coding |
| Candidate equals dp[left][k] plus dp[k][right] plus arr[left]*arr[k]*arr[right]. | 候選值是左子區間+右子區間+邊界乘積。 | Coding |
| I maximize dp[left][right] with each candidate. | 用每個候選更新 dp[left][right] 最大值。 | Coding |
| Final answer is dp[0][n+1]. | 最後答案是 dp[0][n+1]。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [3,1,5,8]. | 我手跑 nums=[3,1,5,8]。 | Dry-run |
| After padding, arr becomes [1,3,1,5,8,1]. | 補邊界後 arr 為 [1,3,1,5,8,1]。 | Dry-run |
| Length-one intervals are filled first as base transitions. | 先填長度 1 區間當基礎。 | Dry-run |
| Larger intervals use previously solved smaller intervals. | 更大區間利用已解的小區間。 | Dry-run |
| Eventually full interval dp[0][5] reaches one hundred sixty-seven. | 最終完整區間 dp[0][5] 會到 167。 | Dry-run |
| So maximum coins are one hundred sixty-seven. | 因此最大硬幣數是 167。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single balloon value x should return x. | 案例一：單顆氣球 x 應回 x。 | Edge test |
| Case two: containing zeros where some bursts yield zero product. | 案例二：含 0 時部分乘積為 0。 | Edge test |
| Case three: all ones should equal number of balloons. | 案例三：全 1 應等於氣球數量。 | Edge test |
| Case four: repeated values with multiple optimal choices. | 案例四：重複值且有多個最優選擇。 | Edge test |
| Case five: near-upper n for performance sanity. | 案例五：接近上限 n 的效能檢查。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n cubed). | 時間複雜度是 O(n³)。 | Complexity |
| Space complexity is O(n squared). | 空間複雜度是 O(n²)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We have interval length loop, left boundary loop, and k split loop. | 演算法包含區間長度、左邊界、k 切點三層迴圈。 | Complexity |
| That yields O(n cubed) total transitions. | 因而總轉移數為 O(n³)。 | Complexity |
| DP table size is proportional to n squared. | DP 表格大小與 n² 成正比。 | Complexity |
| So memory usage is O(n²). | 所以記憶體是 O(n²)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me switch to last-burst perspective. | 我改用最後戳破的視角。 | If stuck |
| Forward first-burst thinking causes unstable neighbors. | 先戳誰的前向想法會讓鄰居不穩定。 | If stuck |
| Interval DP works because boundaries stay fixed. | 區間 DP 可行因邊界在子問題中固定。 | If stuck |
| dp[left][right] means open interval result. | dp[left][right] 代表開區間結果。 | If stuck |
| k is the last balloon inside interval. | k 是區間內最後戳破氣球。 | If stuck |
| Candidate uses left part right part and boundary product. | 候選值由左區間、右區間與邊界乘積組成。 | If stuck |
| Fill intervals from short to long. | 區間填表順序要由短到長。 | If stuck |
| Let me test single balloon quickly. | 我快速測單顆氣球案例。 | If stuck |
| It confirms base transition behavior. | 這能確認基礎轉移行為。 | If stuck |
| Great, now recurrence is solid. | 很好，遞推已穩定。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved burst balloons with interval DP. | 我用區間 DP 解了 Burst Balloons。 | Wrap-up |
| Core trick is choosing the last burst balloon per interval. | 核心技巧是每區間選最後戳破者。 | Wrap-up |
| Padding boundaries with ones simplifies formula and edges. | 邊界補 1 可簡化公式與邊界處理。 | Wrap-up |
| Complexity is O(n³) time and O(n²) space. | 複雜度為 O(n³) 時間、O(n²) 空間。 | Wrap-up |
| This is the canonical interview solution. | 這是該題經典面試解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: maximize total coins after bursting all balloons. | 目標：戳完所有氣球後硬幣總和最大。 | Cheat sheet |
| Add boundary ones at both ends. | 首尾各補一個 1。 | Cheat sheet |
| Use interval DP on open intervals. | 對開區間使用區間 DP。 | Cheat sheet |
| dp[l][r]=best in (l,r). | dp[l][r]=開區間 (l,r) 最佳值。 | Cheat sheet |
| Enumerate interval lengths from short to long. | 區間長度由短到長枚舉。 | Cheat sheet |
| For each interval, try every k as last burst. | 每個區間都試每個 k 當最後戳破。 | Cheat sheet |
| Candidate=dp[l][k]+dp[k][r]+arr[l]*arr[k]*arr[r]. | 候選=dp[l][k]+dp[k][r]+arr[l]*arr[k]*arr[r]。 | Cheat sheet |
| Take max over all k. | 對所有 k 取最大。 | Cheat sheet |
| Answer is dp[0][n+1]. | 答案是 dp[0][n+1]。 | Cheat sheet |
| Single balloon x -> x. | 單顆氣球 x -> x。 | Cheat sheet |
| Example [3,1,5,8] -> 167. | 範例 [3,1,5,8] -> 167。 | Cheat sheet |
| Time O(n³). | 時間 O(n³)。 | Cheat sheet |
| Space O(n²). | 空間 O(n²)。 | Cheat sheet |
| Common bug: wrong interval boundary definition. | 常見錯誤：區間邊界定義錯。 | Cheat sheet |
| Common bug: forgetting padding ones. | 常見錯誤：忘記補邊界 1。 | Cheat sheet |
| Common bug: filling long intervals too early. | 常見錯誤：過早填長區間。 | Cheat sheet |
| Explain last-burst intuition explicitly. | 要明確解釋最後戳破直覺。 | Cheat sheet |
| Mention why forward view is hard. | 可補充前向思考為何困難。 | Cheat sheet |
| Validate with small arrays first. | 先用小陣列驗證。 | Cheat sheet |
| Then trust interval build order. | 再依序擴展區間長度。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Reverse-thinking interval recurrence preserved.
- No hallucinated constraints: ✅ Boundary handling and score formula match source.
- Language simplicity: ✅ Interview-oriented explanation of the hard intuition.
