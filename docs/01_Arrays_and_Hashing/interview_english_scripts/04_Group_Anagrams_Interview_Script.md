# 04 Group Anagrams — Interview English Script (C++)

> Source aligned with: `docs/01_Arrays_and_Hashing/04_Group_Anagrams.md`

> Quick links: [Source Solution](../04_Group_Anagrams.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the problem first. | 我先重述題目。 | Restatement |
| We need to group words that are anagrams. | 我們要把互為 anagram 的字分組。 | Restatement |
| Output order of groups does not matter. | 輸出群組順序不重要。 | Restatement |
| A sorted word can be a stable key. | 排序後字串可當穩定 key。 | Restatement |
| I will use hash map from key to list. | 我會用 hash map 由 key 對應到列表。 | Restatement |
| Then I will verify with sample grouping. | 接著我會用範例驗證分組。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume only lowercase English letters? | 可以假設只有小寫英文字母嗎？ | Clarify |
| Should I preserve original order inside each group? | 每組內要保留原順序嗎？ | Clarify |
| Is empty string possible in input? | 輸入可能含空字串嗎？ | Clarify |
| Is sorting-key approach acceptable for this round? | 這輪可接受排序 key 作法嗎？ | Clarify |
| Do you want count-key optimization discussion too? | 也需要我補充 count-key 優化嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Baseline compares each word with many others. | 基線是每個字去比很多其他字。 | Approach |
| We need repeated anagram checks across pairs. | 我們需要反覆做配對 anagram 檢查。 | Approach |
| That is too slow, around O(m^2 * n). | 這太慢，大約 O(m^2 * n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I compute one canonical key for each word. | 我為每個字計算一個標準 key。 | Approach |
| Key is the sorted version of that word. | key 就是該字排序後版本。 | Approach |
| Anagrams share the same sorted key. | anagram 會共享同一個排序 key。 | Approach |
| So I append word into map[key]. | 所以我把字加進 map[key]。 | Approach |
| Time O(m*n log n), space O(m*n). | 時間 O(m*n log n)，空間 O(m*n)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First, I create unordered_map<string, vector<string>> groups. | 先建立 groups 的 unordered_map。 | Coding |
| Then I iterate each word in strs. | 然後逐一走訪 strs 的每個 word。 | Coding |
| I copy word into key and sort key. | 我把 word 複製到 key 並排序 key。 | Coding |
| Next, I push original word into groups[key]. | 接著把原 word 推入 groups[key]。 | Coding |
| After loop, I prepare result vector. | 迴圈後我準備 result 向量。 | Coding |
| I iterate map entries and move each group. | 我走訪 map 並把每組移入結果。 | Coding |
| Finally, I return grouped anagrams. | 最後回傳分組完成的 anagrams。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run eat, tea, tan, ate, nat, bat. | 我手跑 eat, tea, tan, ate, nat, bat。 | Dry-run |
| eat gives key aet, so group aet gets eat. | eat 的 key 是 aet，放到 aet 組。 | Dry-run |
| tea also gives aet, append into same group. | tea 也是 aet，加入同組。 | Dry-run |
| tan gives ant, and nat also gives ant. | tan 是 ant，nat 也是 ant。 | Dry-run |
| bat gives abt, so it forms its own group. | bat 是 abt，所以自成一組。 | Dry-run |
| Final groups are [eat,tea,ate], [tan,nat], [bat]. | 最後分組是 [eat,tea,ate]、[tan,nat]、[bat]。 | Dry-run |
| That matches expected grouping behavior. | 這符合預期分組行為。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single word ["a"] gives one group. | 案例一：單字 ["a"] 只會有一組。 | Edge test |
| Case two: [""] should still produce one group. | 案例二：[""] 也應產生一組。 | Edge test |
| Case three: all words identical. | 案例三：全部字都相同。 | Edge test |
| Case four: no anagram pairs at all. | 案例四：完全沒有 anagram 配對。 | Edge test |
| Case five: mix of short and long words. | 案例五：混合短字與長字。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time is O(m*n log n). | 時間是 O(m*n log n)。 | Complexity |
| Space is O(m*n). | 空間是 O(m*n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We process m words total. | 我們總共處理 m 個字。 | Complexity |
| Sorting each word costs O(n log n). | 每個字排序成本是 O(n log n)。 | Complexity |
| Hash map insertion is average O(1) per word. | 每個字放 map 平均 O(1)。 | Complexity |
| Stored characters dominate space, so O(m*n). | 儲存字元主導空間，所以是 O(m*n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| May I take fifteen seconds to think? | 可以給我十五秒想一下嗎？ | If stuck |
| Let me verify the key design first. | 我先確認 key 設計。 | If stuck |
| I can start with sorted key method. | 我可以先從排序 key 講起。 | If stuck |
| Then I can mention count-key alternative. | 然後補充 count-key 替代方案。 | If stuck |
| I forgot one container syntax only. | 我只是忘了一個容器語法。 | If stuck |
| The grouping logic is still clear. | 分組邏輯仍然清楚。 | If stuck |
| Thanks, I will adjust this line. | 謝謝，我會調整這行。 | If stuck |
| I found why that group was wrong. | 我找到那組出錯原因。 | If stuck |
| Let me rerun the sample quickly. | 我快速重跑範例。 | If stuck |
| Now every key maps correctly. | 現在每個 key 都映射正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I finished the implementation. | 我完成實作了。 | Wrap-up |
| Grouping result matches expected output. | 分組結果符合預期輸出。 | Wrap-up |
| Sorted-key map approach is easy to explain. | 排序 key map 作法容易解釋。 | Wrap-up |
| Time O(m*n log n), space O(m*n). | 時間 O(m*n log n)，空間 O(m*n)。 | Wrap-up |
| I can discuss count-key optimization too. | 我也可補充 count-key 優化。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Restate grouping-anagrams goal. | 重述 anagram 分組目標。 | Cheat sheet |
| Ask if output order matters. | 詢問輸出順序是否重要。 | Cheat sheet |
| Baseline pairwise check is too slow. | 基線兩兩比較太慢。 | Cheat sheet |
| Use canonical sorted key. | 使用標準排序 key。 | Cheat sheet |
| Build map from key to words. | 建立 key 到字串列表的 map。 | Cheat sheet |
| Sort each word copy as key. | 把每個字拷貝後排序當 key。 | Cheat sheet |
| Push word into groups[key]. | 將字推入 groups[key]。 | Cheat sheet |
| Convert map values into result. | 把 map 的 value 轉成結果。 | Cheat sheet |
| Dry-run eat, tea, ate together. | 手跑 eat、tea、ate 同組。 | Cheat sheet |
| Dry-run tan, nat together. | 手跑 tan、nat 同組。 | Cheat sheet |
| Keep bat in its own group. | bat 獨立成組。 | Cheat sheet |
| Test empty-string input. | 測空字串輸入。 | Cheat sheet |
| Test all words identical. | 測全部字串相同。 | Cheat sheet |
| Test no-anagram scenario. | 測沒有 anagram 情況。 | Cheat sheet |
| Report O(m*n log n) time. | 報告 O(m*n log n) 時間。 | Cheat sheet |
| Report O(m*n) space. | 報告 O(m*n) 空間。 | Cheat sheet |
| Mention count-key as follow-up. | 補充 count-key 後續作法。 | Cheat sheet |
| Keep explanation in coding order. | 說明保持程式撰寫順序。 | Cheat sheet |
| End with trade-off summary. | 以取捨總結收尾。 | Cheat sheet |
| Invite deeper optimization discussion. | 邀請更深入優化討論。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Sorted-key grouping approach is preserved.
- No hallucinated constraints: ✅ Uncertain preferences are asked in clarification lines.
- Language simplicity: ✅ Short, spoken, interview-safe English.
