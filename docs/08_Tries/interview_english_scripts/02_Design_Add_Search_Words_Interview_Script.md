# 02 Design Add and Search Words Data Structure — Interview English Script (C++)

> Source aligned with: `docs/08_Tries/02_Design_Add_Search_Words.md`

> Quick links: [Source Solution](../02_Design_Add_Search_Words.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the word-dictionary design problem. | 我先重述 WordDictionary 設計題。 | Restatement |
| We need addWord and search operations. | 要實作 addWord 與 search。 | Restatement |
| search may contain dot wildcard matching any one character. | search 可能含 `.`，可匹配任一單字元。 | Restatement |
| Exact letters must still follow trie edges normally. | 一般字母仍要依 trie 邊精確匹配。 | Restatement |
| Wildcard may branch into multiple children paths. | wildcard 會分支到多個子路徑。 | Restatement |
| I will use Trie plus DFS for wildcard matching. | 我會用 Trie 加 DFS 處理 wildcard。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are addWord inputs always lowercase letters only? | addWord 輸入是否都只有小寫字母？ | Clarify |
| Does search input allow only lowercase and dot? | search 是否只允許小寫與 `.`？ | Clarify |
| Dot wildcard matches exactly one character, correct? | `.` 是匹配「一個」字元，對嗎？ | Clarify |
| Should I return false when path ends before word length? | 路徑提前結束時應回傳 false 嗎？ | Clarify |
| Is trie-based approach expected over hash-set scan? | 是否預期用 trie 而非 hash-set 全掃？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force stores words in a set and scans candidates on wildcard search. | 暴力法把字存 set，遇 wildcard 就掃候選。 | Approach |
| For each candidate, compare character by character. | 每個候選字都要逐字比對。 | Approach |
| Worst-case cost becomes O(number of words times length). | 最壞成本變 O(字數*字長)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build Trie to share prefixes among words. | 用 Trie 共享多單字前綴。 | Approach |
| addWord is standard trie insertion in O(L). | addWord 是標準 trie 插入，O(L)。 | Approach |
| For search, DFS from current node by index. | search 以索引在目前節點做 DFS。 | Approach |
| Normal letter takes one edge, dot explores all non-null children. | 一般字母走單邊，`.` 探索所有非空子節點。 | Approach |
| Return true once any wildcard branch reaches terminal word end. | 任一分支到達合法結尾即回 true。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I define TrieNode with children array and end flag. | 我先定義含 children 陣列與 end 旗標的 TrieNode。 | Coding |
| Constructor initializes all children pointers to null. | 建構子把所有子指標初始化為 null。 | Coding |
| addWord walks characters and creates missing nodes. | addWord 逐字走訪並建立缺少節點。 | Coding |
| At final node, I set end flag true. | 到最後節點時把 end 旗標設 true。 | Coding |
| search calls DFS helper with index zero and root node. | search 以 index=0、root 呼叫 DFS helper。 | Coding |
| If current char is dot, I recurse through all children. | 若當前字元是 `.`，就遞迴所有子節點。 | Coding |
| If current char is letter, I recurse one matching child. | 若是一般字母，只遞迴對應子節點。 | Coding |
| Base case returns node end flag when index reaches length. | base case 在 index 到尾時回傳節點 end 旗標。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run add bad, dad, mad; then search pad, bad, .ad, b.. | 我手跑加入 bad、dad、mad；再查 pad、bad、.ad、b.. | Dry-run |
| search pad fails at first character p path. | search pad 在首字 p 路徑就失敗。 | Dry-run |
| search bad follows b-a-d and ends at terminal true. | search bad 走 b-a-d 並落在結尾 true。 | Dry-run |
| search .ad explores b, d, and m branches. | search .ad 會探索 b、d、m 三個分支。 | Dry-run |
| Branch b-a-d reaches terminal, so return true. | b-a-d 分支到達結尾，故回 true。 | Dry-run |
| search b.. explores two wildcard levels under b. | search b.. 在 b 下面做兩層 wildcard 展開。 | Dry-run |
| Path b-a-d exists and terminal true, so result is true. | b-a-d 路徑存在且結尾 true，所以結果 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: searching empty or shorter-than-inserted pattern boundaries. | 案例一：空字串或長度邊界查詢。 | Edge test |
| Case two: wildcard-only query like three dots. | 案例二：全 wildcard 查詢如 `...`。 | Edge test |
| Case three: query longer than any inserted word. | 案例三：查詢長度大於所有已插單字。 | Edge test |
| Case four: repeated addWord on same word should remain valid. | 案例四：重複 addWord 同字應維持正確。 | Edge test |
| Case five: wildcard branch exists but does not end as word. | 案例五：wildcard 有路但未落在單字結尾。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| addWord is O(L), exact-letter search is O(L). | addWord 為 O(L)，純字母 search 也是 O(L)。 | Complexity |
| Wildcard search worst-case is exponential in pattern length. | wildcard 搜尋最壞會對字長呈指數展開。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| addWord processes each character once, so O(L). | addWord 每字元處理一次，故 O(L)。 | Complexity |
| search without dots also follows one path, O(L). | 不含 dot 的 search 走單一路徑，O(L)。 | Complexity |
| search with many dots may branch up to 26 per level. | 含多個 dot 時每層最多分支到 26。 | Complexity |
| Trie storage depends on total created nodes across all words. | Trie 儲存量取決於全部建立節點總數。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me treat wildcard logic separately from normal character logic. | 我先把 wildcard 與一般字母邏輯分開。 | If stuck |
| Normal character should recurse only one child. | 一般字母只該遞迴一個子節點。 | If stuck |
| Dot should iterate all existing children. | dot 則要遍歷所有存在子節點。 | If stuck |
| I might have returned false too early in dot loop. | 我可能在 dot 迴圈中太早回 false。 | If stuck |
| Let me return false only after all branches fail. | 我改成全部分支都失敗後才回 false。 | If stuck |
| I will retest pattern .ad now. | 我現在重測 .ad。 | If stuck |
| It now returns true correctly. | 現在能正確回傳 true。 | If stuck |
| I will test b.. and ..z as contrast. | 我再測 b.. 與 ..z 做對照。 | If stuck |
| b.. passes while ..z fails as expected. | b.. 通過而 ..z 失敗，符合預期。 | If stuck |
| Great, wildcard DFS behavior is now correct. | 很好，wildcard DFS 行為已正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed WordDictionary using Trie and DFS wildcard search. | 我完成了 Trie + DFS wildcard 的 WordDictionary。 | Wrap-up |
| addWord is linear, while wildcard search explores necessary branches. | addWord 線性，wildcard 搜尋展開必要分支。 | Wrap-up |
| Exact search path is O(L). | 精確搜尋路徑是 O(L)。 | Wrap-up |
| Wildcard worst-case is branching exponential by depth. | wildcard 最壞是隨深度分支指數成長。 | Wrap-up |
| I can also discuss pruning heuristics if needed. | 若需要我可補充剪枝策略。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Design WordDictionary with addWord and search. | 設計含 addWord/search 的 WordDictionary。 | Cheat sheet |
| search supports dot wildcard. | search 支援 dot wildcard。 | Cheat sheet |
| Use Trie nodes with 26 children. | 使用 26 子節點 Trie。 | Cheat sheet |
| Node stores end-of-word flag. | 節點保存結尾旗標。 | Cheat sheet |
| addWord inserts characters sequentially. | addWord 逐字插入。 | Cheat sheet |
| mark terminal node at end. | 最後節點標記終點。 | Cheat sheet |
| search calls DFS(node, index). | search 呼叫 DFS(node,index)。 | Cheat sheet |
| Base index==len => return end flag. | index 到尾就回 end 旗標。 | Cheat sheet |
| Normal char => follow one edge. | 一般字母走單邊。 | Cheat sheet |
| Dot => try all non-null children. | dot 嘗試全部非空子節點。 | Cheat sheet |
| Any successful branch returns true. | 任一成功分支即回 true。 | Cheat sheet |
| All branches fail => false. | 全分支失敗才回 false。 | Cheat sheet |
| addWord time O(L). | addWord 時間 O(L)。 | Cheat sheet |
| search no dot O(L). | search 無 dot 為 O(L)。 | Cheat sheet |
| search many dots worst-case exponential. | 多 dot 最壞指數展開。 | Cheat sheet |
| Trie memory grows with created nodes. | Trie 記憶體隨節點數增長。 | Cheat sheet |
| Test exact match cases. | 測精確匹配案例。 | Cheat sheet |
| Test wildcard mixed cases. | 測 wildcard 混合案例。 | Cheat sheet |
| Common bug: early false in dot loop. | 常見錯誤：dot 迴圈過早 false。 | Cheat sheet |
| End with complexity trade-off summary. | 收尾總結複雜度取捨。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Trie insertion + DFS wildcard branching is preserved.
- No hallucinated constraints: ✅ Dot semantics and complexity follow source chapter.
- Language simplicity: ✅ Concise spoken lines for interview delivery.
