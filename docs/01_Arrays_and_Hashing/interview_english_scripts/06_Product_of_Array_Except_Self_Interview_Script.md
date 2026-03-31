# 06 Product of Array Except Self — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/06_Product_of_Array_Except_Self.md`

> Quick links: [Source Solution](../06_Product_of_Array_Except_Self.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| For each index, return product of all other values. | 每個索引要回傳其餘值的乘積。 | Restatement |
| We cannot use division here. | 這題不能使用除法。 | Restatement |
| We also want O(n) time. | 我們也希望時間是 O(n)。 | Restatement |
| I will use prefix and postfix products. | 我會使用 prefix 與 postfix 乘積。 | Restatement |
| Then I will test zero-related edge cases. | 然後我會測含零的邊界案例。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume output array does not count as extra space? | 可以假設輸出陣列不算額外空間嗎？ | Clarify |
| Are zeros and negative numbers allowed? | 允許零與負數嗎？ | Clarify |
| Is integer overflow out of scope here? | 整數溢位在這題可忽略嗎？ | Clarify |
| Do we require exactly O(1) extra space? | 是否要求嚴格 O(1) 額外空間？ | Clarify |
| Should I still mention division idea as contrast? | 我要先提除法法當對照嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline computes each answer by scanning all others. | 基線是每個答案都掃一次其他元素。 | Approach |
| That gives O(n^2) time. | 這會得到 O(n^2) 時間。 | Approach |
| Division idea is simpler but not allowed. | 除法法較簡單，但題目禁止。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| For index i, answer is left product times right product. | 對索引 i，答案是左乘積乘右乘積。 | Approach |
| First pass stores prefix product in result. | 第一輪把 prefix 乘積存進結果。 | Approach |
| Second pass multiplies postfix product into result. | 第二輪把 postfix 乘積乘回結果。 | Approach |
| We avoid division and keep O(n) time. | 我們避開除法且維持 O(n) 時間。 | Approach |
| Extra space is O(1) besides output array. | 除輸出陣列外，額外空間是 O(1)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create result array of size n. | 先建立大小 n 的結果陣列。 | Coding |
| I set prefix to one. | 我把 prefix 設為 1。 | Coding |
| Left to right: res[i] gets current prefix. | 從左到右：res[i] 先放當前 prefix。 | Coding |
| Then prefix multiplies nums[i]. | 接著 prefix 乘上 nums[i]。 | Coding |
| Next, I set postfix to one. | 接著我把 postfix 設為 1。 | Coding |
| Right to left: res[i] multiplies postfix. | 從右到左：res[i] 乘上 postfix。 | Coding |
| Then postfix multiplies nums[i]. | 然後 postfix 再乘上 nums[i]。 | Coding |
| Finally, return the result array. | 最後回傳結果陣列。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums one, two, three, four. | 我手跑 nums = 1,2,3,4。 | Dry-run |
| Prefix pass writes res as one, one, two, six. | prefix 後 res 會是 1,1,2,6。 | Dry-run |
| Start postfix as one from the right. | 從右側開始，postfix 初值是 1。 | Dry-run |
| i three: res becomes six, postfix becomes four. | i=3：res 變 6，postfix 變 4。 | Dry-run |
| i two: res becomes eight, postfix becomes twelve. | i=2：res 變 8，postfix 變 12。 | Dry-run |
| i one then i zero give twelve and twenty four. | i=1 與 i=0 得到 12 與 24。 | Dry-run |
| Final output is [24,12,8,6]. | 最終輸出是 [24,12,8,6]。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: [1,2] should output [2,1]. | 案例一：[1,2] 應輸出 [2,1]。 | Edge test |
| Case two: one zero, like [0,1,2,3]. | 案例二：單一零，如 [0,1,2,3]。 | Edge test |
| Case three: two zeros, like [0,0,2,3]. | 案例三：兩個零，如 [0,0,2,3]。 | Edge test |
| Case four: all negatives, like [-1,-2,-3]. | 案例四：全負數，如 [-1,-2,-3]。 | Edge test |
| Case five: repeated values, like [2,2,2]. | 案例五：重複值，如 [2,2,2]。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(n). | 時間是 O(n)。 | Complexity |
| Extra space is O(1), excluding output. | 不含輸出時，額外空間是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We do one forward pass and one backward pass. | 我們做一次正向與一次反向遍歷。 | Complexity |
| Each pass is linear in n. | 每一輪都對 n 線性。 | Complexity |
| Only prefix, postfix, and loop vars are extra. | 額外只用 prefix、postfix 與迴圈變數。 | Complexity |
| So time is O(n), extra space O(1). | 所以時間 O(n)、額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me recheck the no-division requirement. | 我先重確認不可除法要求。 | If stuck |
| I can explain prefix idea first. | 我可以先講 prefix 概念。 | If stuck |
| Then I add postfix in second pass. | 然後第二輪補上 postfix。 | If stuck |
| I forgot one index direction. | 我一時忘了索引方向。 | If stuck |
| The main formula is still clear. | 但主公式仍清楚。 | If stuck |
| Thanks, I will adjust this loop. | 謝謝，我會調整這個迴圈。 | If stuck |
| I found why zero case failed. | 我找到零案例失敗原因。 | If stuck |
| Let me rerun with zeros quickly. | 我快速用含零案例重跑。 | If stuck |
| Now results are consistent. | 現在結果一致了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| It works without using division. | 這個解法在不除法下可運作。 | Wrap-up |
| Prefix and postfix combine into correct answers. | prefix 與 postfix 能組出正確答案。 | Wrap-up |
| Time is O(n), extra space O(1). | 時間 O(n)，額外空間 O(1)。 | Wrap-up |
| I can discuss zero-case intuition if needed. | 若需要我可補充零案例直覺。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate product-except-self goal. | 重述除自身外乘積目標。 | Cheat sheet |
| Mention no-division constraint. | 提到不可除法限制。 | Cheat sheet |
| Baseline O(n^2) is too slow. | 基線 O(n^2) 太慢。 | Cheat sheet |
| Use prefix and postfix idea. | 使用 prefix 與 postfix 概念。 | Cheat sheet |
| Forward pass writes prefix into res. | 正向遍歷把 prefix 寫入 res。 | Cheat sheet |
| Backward pass multiplies postfix. | 反向遍歷把 postfix 乘回去。 | Cheat sheet |
| Keep prefix initialized to one. | prefix 初值維持為 1。 | Cheat sheet |
| Keep postfix initialized to one. | postfix 初值維持為 1。 | Cheat sheet |
| Dry-run [1,2,3,4]. | 手跑 [1,2,3,4]。 | Cheat sheet |
| Verify one-zero case. | 驗證單一零案例。 | Cheat sheet |
| Verify two-zero case. | 驗證雙零案例。 | Cheat sheet |
| Verify negative values case. | 驗證負值案例。 | Cheat sheet |
| Output array is allowed storage. | 輸出陣列可視為允許儲存。 | Cheat sheet |
| Time is O(n). | 時間是 O(n)。 | Cheat sheet |
| Extra space is O(1). | 額外空間是 O(1)。 | Cheat sheet |
| Explain why division fails with zeros. | 解釋除法遇零為何失敗。 | Cheat sheet |
| Speak each pass clearly. | 清楚口述每一輪遍歷。 | Cheat sheet |
| If stuck, restate formula. | 卡住就重述公式。 | Cheat sheet |
| End with complexity summary. | 以複雜度總結收尾。 | Cheat sheet |
| Offer extra edge-case discussion. | 提供額外邊界案例討論。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Prefix/postfix two-pass approach is preserved.
- No hallucinated constraints: ✅ Ambiguous constraints are asked as clarifications.
- Language simplicity: ✅ Short interview-safe spoken lines.
