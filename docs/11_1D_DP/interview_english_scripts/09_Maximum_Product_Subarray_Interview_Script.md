# 09 Maximum Product Subarray — Interview English Script (C++)

> Source aligned with: `docs/11_1D_DP/09_Maximum_Product_Subarray.md`

> Quick links: [Source Solution](../09_Maximum_Product_Subarray.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate maximum product subarray. | 我先重述最大乘積子陣列題。 | Restatement |
| We need maximum product among contiguous subarrays. | 要找連續子陣列中的最大乘積。 | Restatement |
| Array can contain positives negatives and zeros. | 陣列可能含正數、負數與 0。 | Restatement |
| Negative numbers can flip sign behavior. | 負數會翻轉符號效果。 | Restatement |
| So tracking only max-so-far is not enough. | 因此只追蹤最大值不夠。 | Restatement |
| I will track both current max and current min products. | 我會同時追蹤當前最大與最小乘積。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Do we return product value only, not subarray indices? | 是否只回乘積值，不回索引？ | Clarify |
| Is single-element subarray allowed? | 是否允許單元素子陣列？ | Clarify |
| Should zeros reset running product consideration? | 遇到 0 是否視為重置切點？ | Clarify |
| Can result be negative if all values are negative and odd count? | 若全負且奇數，答案可為負嗎？ | Clarify |
| Is O(n) time expected as optimal? | O(n) 時間是否為最佳期望？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force checks every contiguous subarray product. | 暴力法檢查每個連續子陣列乘積。 | Approach |
| Even optimized accumulation still gives O(n squared). | 即便累乘優化仍是 O(n²)。 | Approach |
| We need linear DP-like sweep. | 我們需要線性 DP 式掃描。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| At each value n, maintain curMax and curMin ending here. | 每個值 n 維護以此結尾的 curMax 與 curMin。 | Approach |
| curMin is needed because negative times negative can become large positive. | 需要 curMin，因負負相乘可轉大正值。 | Approach |
| Transition uses three candidates: n, n times curMax, n times curMin. | 轉移候選有三個：n、n*curMax、n*curMin。 | Approach |
| Update global result with new curMax each step. | 每步用新 curMax 更新全域答案。 | Approach |
| This yields O(n) time and O(1) space. | 可達 O(n) 時間與 O(1) 空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I initialize result as first element or max element baseline. | 我先以首元素或全陣列最大值初始化 result。 | Coding |
| I set curMax and curMin to one initially. | 我先把 curMax 與 curMin 設為 1。 | Coding |
| For each number n, I store tmp as curMax times n. | 對每個 n，我先存 tmp=curMax*n。 | Coding |
| New curMax is max of n, n times old curMax, n times old curMin. | 新 curMax 取 n、n*舊curMax、n*舊curMin 的最大。 | Coding |
| New curMin is min of n, tmp, n times old curMin. | 新 curMin 取 n、tmp、n*舊curMin 的最小。 | Coding |
| I update result with max of result and curMax. | 用 max(result,curMax) 更新答案。 | Coding |
| Continue through all elements once. | 持續到所有元素處理完。 | Coding |
| Return final result. | 回傳最終 result。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums [2,3,-2,4]. | 我手跑 nums=[2,3,-2,4]。 | Dry-run |
| After two, curMax is two and result is two. | 處理 2 後 curMax=2，result=2。 | Dry-run |
| After three, curMax becomes six and result updates to six. | 處理 3 後 curMax=6，result=6。 | Dry-run |
| At minus two, curMax drops but curMin captures negative swing. | 到 -2 時 curMax 下降，但 curMin 保留負向潛力。 | Dry-run |
| At four, best ending product is four while global result stays six. | 到 4 時結尾最佳為 4，全域仍是 6。 | Dry-run |
| Final answer is six from subarray [2,3]. | 最終答案為 6，來自 [2,3]。 | Dry-run |
| This matches expected output. | 與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single negative element should return itself. | 案例一：單一負數應回自身。 | Edge test |
| Case two: array containing zero splits product segments. | 案例二：含 0 陣列會分割乘積區段。 | Edge test |
| Case three: two negatives produce positive large product. | 案例三：兩個負數可產生大正積。 | Edge test |
| Case four: all negatives with odd count. | 案例四：全負且個數為奇數。 | Edge test |
| Case five: all positives should behave like normal prefix expansion. | 案例五：全正數應像一般前綴擴展。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Extra space complexity is O(1). | 額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan array once and update constant number of variables. | 我們掃描陣列一次並更新常數個變數。 | Complexity |
| Each step computes max and min over constant candidates. | 每步在常數個候選中取 max/min。 | Complexity |
| Therefore total runtime is O(n). | 因此總時間是 O(n)。 | Complexity |
| No auxiliary arrays are needed, so extra memory is O(1). | 不需額外陣列，額外記憶體 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me remember why this is harder than max-sum Kadane. | 我先提醒自己這題比最大和 Kadane 難。 | If stuck |
| Product with negative can flip max and min roles. | 負數相乘會讓 max/min 角色互換。 | If stuck |
| So I must keep both curMax and curMin. | 所以必須同時維護 curMax 與 curMin。 | If stuck |
| Transition always checks three candidates. | 轉移一定檢查三個候選。 | If stuck |
| Candidate one starts new subarray at n. | 候選一是從 n 重新開始子陣列。 | If stuck |
| Candidate two and three extend previous chains. | 候選二與三是延伸先前鏈。 | If stuck |
| Let me test quickly with [-2,3,-4]. | 我快速測試 [-2,3,-4]。 | If stuck |
| Result should become twenty-four. | 結果應為 24。 | If stuck |
| That confirms min-tracking works. | 這證明追蹤最小值是必要且有效。 | If stuck |
| Great, I can finalize the explanation. | 很好，我可完成說明。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved maximum product subarray in one pass. | 我用單次掃描解出最大乘積子陣列。 | Wrap-up |
| The key is tracking both current max and min products. | 關鍵是同時追蹤當前最大與最小乘積。 | Wrap-up |
| Negative values can turn previous minimum into new maximum. | 負數可把先前最小值翻成新最大值。 | Wrap-up |
| Runtime is O(n) and space is O(1). | 時間 O(n)，空間 O(1)。 | Wrap-up |
| This handles zeros positives and negatives robustly. | 此法可穩健處理 0、正數與負數。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem: max product over contiguous subarrays. | 題目：連續子陣列最大乘積。 | Cheat sheet |
| Need contiguous, not subsequence. | 要連續，不是子序列。 | Cheat sheet |
| Keep global result. | 維護全域結果。 | Cheat sheet |
| Keep curMax and curMin. | 維護 curMax 與 curMin。 | Cheat sheet |
| Negative can swap their roles. | 負數會讓兩者角色翻轉。 | Cheat sheet |
| For each n, compute tmp=curMax*n. | 每個 n 先算 tmp=curMax*n。 | Cheat sheet |
| New curMax=max(n,n*oldMax,n*oldMin). | 新 curMax=max(n,n*舊Max,n*舊Min)。 | Cheat sheet |
| New curMin=min(n,tmp,n*oldMin). | 新 curMin=min(n,tmp,n*舊Min)。 | Cheat sheet |
| Update result=max(result,curMax). | 更新 result=max(result,curMax)。 | Cheat sheet |
| Single element can be answer. | 單元素也可能是答案。 | Cheat sheet |
| Zero may reset effective chain. | 0 可能重置有效鏈。 | Cheat sheet |
| Example [2,3,-2,4] -> 6. | 範例 [2,3,-2,4] -> 6。 | Cheat sheet |
| Example [-2,3,-4] -> 24. | 範例 [-2,3,-4] -> 24。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1). | 空間 O(1)。 | Cheat sheet |
| Common bug: tracking only max value. | 常見錯誤：只追蹤最大值。 | Cheat sheet |
| Common bug: overwrite old curMax too early. | 常見錯誤：過早覆寫舊 curMax。 | Cheat sheet |
| Use tmp to preserve old max product. | 用 tmp 保留舊最大乘積。 | Cheat sheet |
| Works with positive/negative/zero mix. | 適用於正負零混合。 | Cheat sheet |
| Explain sign-flip intuition in interview. | 面試中要說明符號翻轉直覺。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ curMax/curMin DP transition preserved.
- No hallucinated constraints: ✅ Correct contiguous-product semantics.
- Language simplicity: ✅ Clear spoken explanation for tricky sign behavior.
