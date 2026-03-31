# 07 Find Median from Data Stream — Interview English Script (C++)

> Source aligned with: `docs/09_Heap/07_Find_Median_Data_Stream.md`

> Quick links: [Source Solution](../07_Find_Median_Data_Stream.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the median-from-stream design problem. | 我先重述串流中位數設計題。 | Restatement |
| We need addNum and findMedian operations. | 需要實作 addNum 與 findMedian。 | Restatement |
| Numbers arrive online, one by one. | 數字會一個接一個線上進來。 | Restatement |
| findMedian should return middle value at any time. | findMedian 要隨時回傳中位數。 | Restatement |
| For even count, median is average of two middle values. | 偶數個時中位數是中間兩值平均。 | Restatement |
| I will maintain two heaps to keep lower and upper halves. | 我會用兩個 heap 維護上下半部。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should findMedian be O(1) after each insertion? | 每次插入後 findMedian 是否期望 O(1)？ | Clarify |
| Can input numbers be negative as well? | 輸入數字是否可能為負數？ | Clarify |
| Do we assume findMedian is called only after at least one addNum? | 是否保證至少 add 一次才會呼叫 findMedian？ | Clarify |
| Is slight floating output like 1.5 expected for even count? | 偶數筆時是否預期輸出浮點如 1.5？ | Clarify |
| May I use max-heap plus min-heap standard pattern? | 可用 max-heap + min-heap 標準做法嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force keeps a sorted array after each insertion. | 暴力法每次插入後都維持排序陣列。 | Approach |
| Insertion can take O(n) due to shifting. | 插入因搬移可能要 O(n)。 | Approach |
| That is too slow for frequent stream updates. | 對高頻更新串流來說太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use max-heap small for lower half values. | 用 max-heap small 存較小一半。 | Approach |
| Use min-heap large for upper half values. | 用 min-heap large 存較大一半。 | Approach |
| Keep ordering invariant: every small top is less than or equal large top. | 維持順序不變量：small top <= large top。 | Approach |
| Keep size invariant: sizes differ by at most one. | 維持大小不變量：兩邊最多差一。 | Approach |
| Median is top of larger heap or average of both tops. | 中位數是較大 heap top 或雙 top 平均。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I define small as max-heap and large as min-heap. | 我定義 small 為 max-heap、large 為 min-heap。 | Coding |
| In addNum, I first push num into small. | addNum 先把 num 推入 small。 | Coding |
| Then I move small top to large to restore ordering relation. | 再把 small top 移到 large 以維持順序。 | Coding |
| If small has fewer elements, I move one back from large. | 若 small 較少，就從 large 移一個回來。 | Coding |
| This keeps small size equal to or one larger than large. | 這讓 small 大小等於或多 large 一個。 | Coding |
| In findMedian, odd count returns small top. | findMedian 在奇數筆時回 small top。 | Coding |
| Even count returns average of small top and large top. | 偶數筆時回 small 與 large top 平均。 | Coding |
| I cast division with 2.0 to keep floating precision. | 我用 2.0 做除法保持浮點精度。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run add one, add two, find median. | 我手跑 add 1、add 2、find median。 | Dry-run |
| After adding one, small has [1], large is empty. | 加入 1 後 small=[1]，large 為空。 | Dry-run |
| After adding two, heaps balance as small [1], large [2]. | 加入 2 後平衡為 small=[1]、large=[2]。 | Dry-run |
| Median now is one plus two over two equals one point five. | 中位數是 (1+2)/2 = 1.5。 | Dry-run |
| Add three next, and balancing gives small [2,1], large [3]. | 再加 3 後平衡成 small=[2,1]、large=[3]。 | Dry-run |
| Odd count median is small top which is two. | 奇數筆中位數是 small top，即 2。 | Dry-run |
| This matches expected outputs 1.5 then 2. | 這與預期輸出 1.5、2 一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: only one number in stream. | 案例一：串流中只有一個數字。 | Edge test |
| Case two: two numbers with average ending point five. | 案例二：兩數平均為 x.5 的情況。 | Edge test |
| Case three: many duplicate values. | 案例三：大量重複值。 | Edge test |
| Case four: negative and positive mixed stream. | 案例四：正負混合串流。 | Edge test |
| Case five: strictly increasing long sequence. | 案例五：嚴格遞增長序列。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| addNum is O(log n), and findMedian is O(1). | addNum 是 O(log n)，findMedian 是 O(1)。 | Complexity |
| Total extra space is O(n). | 額外空間總計是 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each add operation performs a constant number of heap push and pop. | 每次 add 只做常數次 heap push/pop。 | Complexity |
| Heap operation cost is O(log n) for current stream size n. | heap 單次操作在大小 n 時成本 O(log n)。 | Complexity |
| findMedian only reads heap tops and does constant arithmetic. | findMedian 只讀 top 並做常數運算。 | Complexity |
| We store all inserted numbers across two heaps, so space is O(n). | 全部數字分存兩 heap，空間是 O(n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me focus on median split into lower and upper halves. | 我先聚焦中位數的上下半部分割。 | If stuck |
| Two heaps are natural for this split. | 兩個 heap 正好對應此分割。 | If stuck |
| small is max-heap for lower half boundary. | small 作為下半部邊界的 max-heap。 | If stuck |
| large is min-heap for upper half boundary. | large 作為上半部邊界的 min-heap。 | If stuck |
| I should enforce order invariant before size balancing. | 我應先修正順序再做大小平衡。 | If stuck |
| Then keep size difference at most one. | 然後保持大小差不超過一。 | If stuck |
| Median read is immediate from heap tops. | 中位數可直接由 heap top 讀出。 | If stuck |
| Let me test sequence one, two, three quickly. | 我快速測 1、2、3 序列。 | If stuck |
| Outputs one point five then two confirm logic. | 輸出 1.5 再 2，邏輯正確。 | If stuck |
| Great, invariants and complexity are both clear now. | 很好，不變量與複雜度都清楚了。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I implemented MedianFinder with two balanced heaps. | 我用兩個平衡 heap 完成 MedianFinder。 | Wrap-up |
| addNum maintains order and size invariants each insertion. | addNum 每次都維持順序與大小不變量。 | Wrap-up |
| findMedian reads top values in constant time. | findMedian 可常數時間讀 top 求值。 | Wrap-up |
| Update cost is O(log n), query cost is O(1). | 更新成本 O(log n)，查詢成本 O(1)。 | Wrap-up |
| This is the standard robust approach for online median. | 這是串流中位數的標準穩健解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Design class for online median. | 設計線上中位數類別。 | Cheat sheet |
| APIs: addNum and findMedian. | API：addNum、findMedian。 | Cheat sheet |
| Keep two heaps. | 維護兩個 heap。 | Cheat sheet |
| small is max-heap lower half. | small 是下半部 max-heap。 | Cheat sheet |
| large is min-heap upper half. | large 是上半部 min-heap。 | Cheat sheet |
| Push into small first. | 先 push 進 small。 | Cheat sheet |
| Move small top to large. | 把 small top 移到 large。 | Cheat sheet |
| Rebalance if small size < large size. | 若 small<large 就再平衡。 | Cheat sheet |
| Keep size diff at most one. | 大小差維持至多一。 | Cheat sheet |
| Keep small top <= large top. | 維持 small top <= large top。 | Cheat sheet |
| Odd count median is small top. | 奇數筆中位數是 small top。 | Cheat sheet |
| Even count median is average of tops. | 偶數筆中位數是雙 top 平均。 | Cheat sheet |
| Use 2.0 for floating division. | 用 2.0 保持浮點除法。 | Cheat sheet |
| addNum complexity O(log n). | addNum 複雜度 O(log n)。 | Cheat sheet |
| findMedian complexity O(1). | findMedian 複雜度 O(1)。 | Cheat sheet |
| Space complexity O(n). | 空間複雜度 O(n)。 | Cheat sheet |
| Test with 1,2 gives 1.5. | 用 1、2 測得 1.5。 | Cheat sheet |
| Add 3 then median becomes 2. | 再加 3，中位數變 2。 | Cheat sheet |
| Common bug: wrong rebalance direction. | 常見錯誤：再平衡方向寫錯。 | Cheat sheet |
| Common bug: integer division in median. | 常見錯誤：中位數用整數除法。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Two-heaps design and balancing logic are preserved.
- No hallucinated constraints: ✅ Uses source operation behavior and sample flow.
- Language simplicity: ✅ Concise, interview-spoken lines with clear invariants.
