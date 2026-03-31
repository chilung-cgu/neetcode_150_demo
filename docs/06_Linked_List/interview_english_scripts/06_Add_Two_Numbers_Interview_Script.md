# 06 Add Two Numbers — Interview English Script (C++)

> Source aligned with: `docs/06_Linked_List/06_Add_Two_Numbers.md`

> Quick links: [Source Solution](../06_Add_Two_Numbers.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the add-two-numbers list problem. | 我先重述兩數相加串列題。 | Restatement |
| Each list stores digits in reverse order. | 每個串列都以反向儲存數位。 | Restatement |
| Head node is the ones place digit. | head 節點代表個位數。 | Restatement |
| I need to return a new list for the sum, also reversed. | 我需回傳同樣反向表示的總和串列。 | Restatement |
| Different lengths and carry chain must be handled. | 要處理不同長度與連續進位。 | Restatement |
| I will simulate elementary column addition iteratively. | 我會用迭代方式模擬直式加法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume node values are always between zero and nine? | 我可假設節點值一定在 0 到 9 嗎？ | Clarify |
| Are both input lists guaranteed non-empty by constraints? | 限制是否保證兩個輸入串列都非空？ | Clarify |
| Should output be a newly constructed list? | 輸出是否必須是新建立的串列？ | Clarify |
| Do we treat missing nodes as digit zero during traversal? | 掃描時缺少節點是否視為 0？ | Clarify |
| Should I include final carry node when carry remains? | 若最後還有 carry 是否要補新節點？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline tries converting lists to integers and adding directly. | 基線想先轉整數再相加。 | Approach |
| But list length can exceed native integer limits. | 但串列長度可能超過原生整數可表範圍。 | Approach |
| So arithmetic conversion is unsafe and not robust. | 所以整數轉換法不安全也不穩健。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Traverse l1 and l2 with a carry variable. | 用 carry 變數同步走訪 l1 與 l2。 | Approach |
| Current sum is digit1 plus digit2 plus carry. | 當前總和為 digit1+digit2+carry。 | Approach |
| New node digit is sum modulo ten. | 新節點數字是 sum 對 10 取餘。 | Approach |
| Updated carry is sum divided by ten. | 新 carry 是 sum 除以 10。 | Approach |
| Continue until both lists and carry are all exhausted. | 直到兩串列與 carry 都耗盡才停止。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create a dummy head and set tail to dummy. | 先建 dummy head，tail 指向 dummy。 | Coding |
| I initialize carry to zero. | carry 初始設為 0。 | Coding |
| While l1 or l2 or carry exists, I continue loop. | 只要 l1、l2、carry 其一存在就迴圈。 | Coding |
| I read digit1 and digit2, using zero when pointer is null. | 讀 digit1、digit2，空指標視為 0。 | Coding |
| I compute sum, digit, and next carry. | 計算 sum、當位 digit、下一個 carry。 | Coding |
| I append a node with digit to tail next. | 把 digit 節點接到 tail->next。 | Coding |
| I move tail and input pointers forward when available. | 推進 tail 與可前進的輸入指標。 | Coding |
| Finally I return dummy next as result head. | 最後回傳 dummy->next 當結果 head。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run l1 [2,4,3] and l2 [5,6,4]. | 我手跑 l1=[2,4,3]、l2=[5,6,4]。 | Dry-run |
| Step one: 2 plus 5 plus carry zero gives 7, carry stays zero. | 第一步 2+5+0=7，carry 仍是 0。 | Dry-run |
| Step two: 4 plus 6 plus zero gives 10, write 0 carry 1. | 第二步 4+6+0=10，寫 0、carry 變 1。 | Dry-run |
| Step three: 3 plus 4 plus carry one gives 8, carry back to zero. | 第三步 3+4+1=8，carry 回到 0。 | Dry-run |
| Both lists end and carry is zero, loop stops. | 兩串列都結束且 carry 為 0，迴圈停止。 | Dry-run |
| Built result list is [7,0,8]. | 建出的結果串列是 [7,0,8]。 | Dry-run |
| This matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: one-digit plus one-digit without carry. | 案例一：一位數加一位數且無進位。 | Edge test |
| Case two: one-digit plus one-digit with carry. | 案例二：一位數加一位數且有進位。 | Edge test |
| Case three: different list lengths. | 案例三：兩串列長度不同。 | Edge test |
| Case four: long carry chain like 999 plus 1. | 案例四：長進位鏈如 999+1。 | Edge test |
| Case five: both lists contain many zeros. | 案例五：兩串列含大量 0。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(max(m,n)). | 時間複雜度是 O(max(m,n))。 | Complexity |
| Extra space is O(max(m,n)) for output nodes. | 輸出節點帶來 O(max(m,n)) 額外空間。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Loop count is bounded by longer list length plus possible final carry. | 迴圈次數受較長串列與最終進位控制。 | Complexity |
| Each iteration does constant arithmetic and pointer updates. | 每輪只做常數次算術與指標更新。 | Complexity |
| Result list stores one node per produced digit. | 結果串列每個數位會產生一節點。 | Complexity |
| If output space excluded, algorithmic extra space is O(1). | 若不計輸出，演算法額外空間是 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me re-check carry propagation first. | 我先重檢 carry 傳遞。 | If stuck |
| Digit is sum modulo ten and carry is sum divided by ten. | digit 是 sum%10，carry 是 sum/10。 | If stuck |
| I must keep looping while carry is non-zero. | carry 非零時一定要繼續迴圈。 | If stuck |
| Missing-node digits should be treated as zero. | 缺節點時該位數視為 0。 | If stuck |
| I may have stopped loop too early. | 我可能太早結束迴圈。 | If stuck |
| Let me add carry in the while condition. | 我把 carry 加入迴圈條件。 | If stuck |
| I will rerun the 999 plus 1 case. | 我重跑 999+1 案例。 | If stuck |
| Now final extra node is appended correctly. | 現在最後補位節點正確生成。 | If stuck |
| Output order is still reversed as required. | 輸出順序也維持題目要求的反向。 | If stuck |
| Great, logic is consistent now. | 很好，邏輯現在一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed iterative digit-by-digit addition. | 我完成了逐位迭代加法實作。 | Wrap-up |
| I validated carry, length mismatch, and zero cases. | 我驗證了進位、長度差與零值案例。 | Wrap-up |
| Runtime is O(max(m,n)). | 時間複雜度是 O(max(m,n))。 | Wrap-up |
| Output space is O(max(m,n)). | 輸出空間是 O(max(m,n))。 | Wrap-up |
| I can discuss forward-order variant if needed. | 若需要我可延伸正向儲存版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Add two reversed-digit linked lists. | 相加兩個反向數位串列。 | Cheat sheet |
| Return result in same reversed format. | 以同樣反向格式回傳結果。 | Cheat sheet |
| Baseline integer-conversion is unsafe for long input. | 基線整數轉換對長輸入不安全。 | Cheat sheet |
| Use iterative column addition with carry. | 用帶 carry 的迭代直式加法。 | Cheat sheet |
| Dummy head simplifies append logic. | dummy head 可簡化追加邏輯。 | Cheat sheet |
| Loop while l1 or l2 or carry exists. | 當 l1 或 l2 或 carry 存在就迴圈。 | Cheat sheet |
| digit1 is l1 value or zero. | digit1 是 l1 值或 0。 | Cheat sheet |
| digit2 is l2 value or zero. | digit2 是 l2 值或 0。 | Cheat sheet |
| sum = digit1 + digit2 + carry. | sum=digit1+digit2+carry。 | Cheat sheet |
| write digit = sum % 10. | 寫入 digit=sum%10。 | Cheat sheet |
| update carry = sum / 10. | 更新 carry=sum/10。 | Cheat sheet |
| append new digit node. | 追加新數位節點。 | Cheat sheet |
| advance non-null pointers. | 推進非空指標。 | Cheat sheet |
| return dummy->next. | 回傳 dummy->next。 | Cheat sheet |
| test no-carry one-digit case. | 測無進位一位數案例。 | Cheat sheet |
| test long carry chain case. | 測長進位鏈案例。 | Cheat sheet |
| time O(max(m,n)). | 時間 O(max(m,n))。 | Cheat sheet |
| output space O(max(m,n)). | 輸出空間 O(max(m,n))。 | Cheat sheet |
| bug risk: forgetting final carry node. | 風險：忘記最後 carry 節點。 | Cheat sheet |
| bug risk: stopping loop too early. | 風險：迴圈過早結束。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Iterative carry-based list addition is preserved.
- No hallucinated constraints: ✅ Uses source digit constraints and reversed-order semantics.
- Language simplicity: ✅ Short interview-ready spoken lines.
