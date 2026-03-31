# 07 Partition Labels — Interview English Script (C++)

> Source aligned with: `docs/13_Greedy/07_Partition_Labels.md`

> Quick links: [Source Solution](../07_Partition_Labels.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate partition labels. | 我先重述 Partition Labels。 | Restatement |
| We have a string s and need to split it into as many parts as possible. | 題目給字串 s，要盡可能切成多段。 | Restatement |
| Each letter must appear in at most one part. | 每個字母最多只能出現在一段中。 | Restatement |
| We should return the sizes of all parts. | 需要回傳每段的長度。 | Restatement |
| Cut points must keep all occurrences of letters inside their segment. | 切點必須確保每字母所有出現都留在同段。 | Restatement |
| I will solve it with greedy using last occurrence map. | 我會用最後出現位置的貪心法。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Is input restricted to lowercase English letters? | 輸入是否限定小寫英文字母？ | Clarify |
| Do we maximize number of partitions by default? | 是否預設要最大化分段數？ | Clarify |
| Should output be list of lengths only? | 輸出是否只要各段長度？ | Clarify |
| Is empty string case excluded by constraints? | 限制是否排除空字串？ | Clarify |
| Is O(n) expected? | O(n) 是否為預期解？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force tests many cut combinations. | 暴力法會測試很多切割組合。 | Approach |
| Validating each combination requires repeated scans. | 每組切法都要重複掃描驗證。 | Approach |
| This is unnecessarily expensive. | 這會造成不必要高成本。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| First record last index of each character. | 先記錄每個字元最後一次出現索引。 | Approach |
| Scan string and maintain current segment end as maximum last index seen so far. | 掃描時把當前段終點維持為目前看到的最大最後索引。 | Approach |
| When current index reaches end, we can safely cut. | 當索引走到 end，就能安全切段。 | Approach |
| Append segment length and start next segment. | 記錄段長後開始下一段。 | Approach |
| This greedy cut is optimal and linear. | 這種貪心切法是最優且線性。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create an array lastIndex of size twenty-six. | 我先建立大小 26 的 lastIndex 陣列。 | Coding |
| I fill lastIndex by scanning s once. | 先掃一次 s 填入每字元最後位置。 | Coding |
| I initialize start to zero and end to zero. | 初始化 start=0、end=0。 | Coding |
| I scan i from zero to s length minus one. | i 從 0 掃到字串尾。 | Coding |
| I update end as max(end, lastIndex[currentChar]). | 用當前字元最後位置更新 end。 | Coding |
| If i equals end, segment is complete. | 若 i==end，代表一段完整。 | Coding |
| I push length i-start+1 and set start=i+1. | 記錄長度 i-start+1，並把 start 設 i+1。 | Coding |
| Finally return the collected lengths. | 最後回傳所有段長。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run s ababcbacadefegdehijhklij. | 我手跑 s=ababcbacadefegdehijhklij。 | Dry-run |
| Last index map shows a ends at eight, b at five, c at seven. | 最後位置圖顯示 a 到 8、b 到 5、c 到 7。 | Dry-run |
| First segment expands until index eight, then we cut length nine. | 第一段擴張到索引 8，切出長度 9。 | Dry-run |
| Next segment from nine reaches end fifteen, length seven. | 下一段從 9 到 15，長度 7。 | Dry-run |
| Final segment from sixteen to twenty-three, length eight. | 最後一段 16 到 23，長度 8。 | Dry-run |
| Output becomes [9,7,8]. | 輸出為 [9,7,8]。 | Dry-run |
| This matches expected result. | 與預期結果一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: all unique letters should each form length one segments. | 案例一：全唯一字母應分成多個長度 1。 | Edge test |
| Case two: all same letter should be one full segment. | 案例二：全同字母應是一整段。 | Edge test |
| Case three: nested last occurrences forcing long first segment. | 案例三：最後位置巢狀導致首段很長。 | Edge test |
| Case four: two clearly separated character groups. | 案例四：兩群字元明顯分離。 | Edge test |
| Case five: shortest possible length one string. | 案例五：最短長度 1 字串。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n). | 時間複雜度是 O(n)。 | Complexity |
| Space complexity is O(1). | 空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| We scan string once to build last positions. | 先掃一遍字串建立最後位置。 | Complexity |
| We scan again to construct partitions greedily. | 再掃一遍以貪心方式切段。 | Complexity |
| Total runtime is linear O(n). | 總時間是線性 O(n)。 | Complexity |
| Auxiliary storage is fixed alphabet array, so O(1). | 額外空間是固定字母表大小，故 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me compute last occurrence first. | 我先算每字元最後出現位置。 | If stuck |
| Current segment must include that last occurrence for every seen char. | 當前段必須包含每個已見字元的最後位置。 | If stuck |
| So segment end is max of those last indices. | 因此段終點是那些最後索引的最大值。 | If stuck |
| When i reaches end, no seen char leaks to the right. | 當 i 到 end，已見字元不會再出現在右側。 | If stuck |
| That means we can cut safely. | 這代表可以安全切段。 | If stuck |
| Then restart from next index. | 然後從下一索引重啟。 | If stuck |
| Let me test quickly with eccbbbbdec. | 我快速測試 eccbbbbdec。 | If stuck |
| End keeps extending to last c and e positions. | end 會持續延到 c、e 的最後位置。 | If stuck |
| So only one segment length ten appears. | 所以只會得到一段長度 10。 | If stuck |
| Great, greedy invariant is clear. | 很好，貪心不變量已清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved partition labels using last-occurrence greedy boundaries. | 我用最後出現邊界的貪心法解了 Partition Labels。 | Wrap-up |
| Segment end tracks the farthest last index among seen characters. | 段終點追蹤已見字元中最遠最後索引。 | Wrap-up |
| Reaching that end guarantees safe cut. | 到達該終點即可安全切段。 | Wrap-up |
| Complexity is O(n) time and O(1) extra space. | 複雜度是 O(n) 時間與 O(1) 額外空間。 | Wrap-up |
| This is the canonical interview solution. | 這是面試常見經典解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: split string so each char appears in at most one part. | 目標：切字串使每字元最多出現在一段。 | Cheat sheet |
| Return partition lengths. | 回傳各段長度。 | Cheat sheet |
| Build lastIndex for each char. | 建立每字元最後位置 lastIndex。 | Cheat sheet |
| Initialize start=0, end=0. | 初始化 start=0、end=0。 | Cheat sheet |
| Scan i from 0..n-1. | i 從 0 掃到 n-1。 | Cheat sheet |
| Update end=max(end,lastIndex[s[i]]). | 更新 end=max(end,lastIndex[s[i]])。 | Cheat sheet |
| If i==end, cut segment. | 若 i==end，就切段。 | Cheat sheet |
| Segment length is i-start+1. | 段長為 i-start+1。 | Cheat sheet |
| Push length to result. | 把段長放入結果。 | Cheat sheet |
| Set start=i+1 for next segment. | start 設為 i+1 進入下一段。 | Cheat sheet |
| Example -> [9,7,8]. | 範例輸出 -> [9,7,8]。 | Cheat sheet |
| All unique letters -> many 1s. | 全唯一字母 -> 多個 1。 | Cheat sheet |
| All same letter -> one segment. | 全同字母 -> 一段。 | Cheat sheet |
| Time O(n). | 時間 O(n)。 | Cheat sheet |
| Space O(1) for fixed alphabet. | 固定字母表下空間 O(1)。 | Cheat sheet |
| Common bug: cutting before reaching farthest last index. | 常見錯誤：還沒到最遠最後索引就切。 | Cheat sheet |
| Common bug: not rebuilding end after each segment. | 常見錯誤：新段未正確重設 end。 | Cheat sheet |
| Greedy cut maximizes number of parts. | 此貪心切法可最大化分段數。 | Cheat sheet |
| Keep invariant explanation explicit. | 要明確講不變量。 | Cheat sheet |
| Validate with nested-overlap sample. | 用巢狀重疊樣例驗證。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Last-index boundary greedy preserved.
- No hallucinated constraints: ✅ Partition objective and output format maintained.
- Language simplicity: ✅ Interview-friendly explanation of invariant and cut condition.
