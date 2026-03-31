# 13 Word Ladder — Interview English Script (C++)

> Source aligned with: `docs/15_Graphs/13_Word_Ladder.md`

> Quick links: [Source Solution](../13_Word_Ladder.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate word ladder. | 我先重述 Word Ladder。 | Restatement |
| We have beginWord endWord and a dictionary list. | 題目給 beginWord、endWord 與字典 wordList。 | Restatement |
| One step changes exactly one character. | 每一步只能改一個字元。 | Restatement |
| Every intermediate word must exist in dictionary. | 每個中間字都必須在字典中。 | Restatement |
| We need shortest transformation sequence length. | 我們要最短轉換序列的長度。 | Restatement |
| I will use BFS because it gives shortest path in unweighted graph. | 我會用 BFS，因為它能找無權圖最短路。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| If endWord is absent from dictionary, should answer be zero? | 若 endWord 不在字典中，答案是否為 0？ | Clarify |
| Are all words the same length? | 所有單字長度是否相同？ | Clarify |
| Are letters lowercase English only? | 字元是否僅小寫英文字母？ | Clarify |
| Does length count include beginWord itself? | 回傳長度是否包含 beginWord 本身？ | Clarify |
| Can wordList contain duplicates? | wordList 是否可能有重複字？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force over all transformation paths explodes combinatorially. | 對所有轉換路徑暴力搜尋會組合爆炸。 | Approach |
| We need shortest path method with pruning. | 我們需要可剪枝的最短路方法。 | Approach |
| BFS with visited control is the right base. | 用 BFS 搭配 visited 控制是正確基礎。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Put wordList into hash set for O one lookup. | 把 wordList 放進 hash set 取得 O(1) 查找。 | Approach |
| Start BFS queue from beginWord with level one. | 以 beginWord 作為 BFS 起點，層級從 1。 | Approach |
| For each popped word, try replacing each position with a to z. | 對每個出隊字，逐位置嘗試替換 a~z。 | Approach |
| Valid transformed words in set are enqueued and erased from set. | 在 set 內的合法新字就入隊並從 set 刪除。 | Approach |
| First time reaching endWord gives shortest length. | 首次到達 endWord 就是最短長度。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I build unordered_set from wordList. | 我先用 wordList 建立 unordered_set。 | Coding |
| If endWord is not in set, return zero. | 若 endWord 不在 set，直接回 0。 | Coding |
| I push beginWord into queue and set level to one. | 我把 beginWord 入隊，level 設 1。 | Coding |
| While queue not empty, process one full level. | queue 非空時處理一整層。 | Coding |
| Pop current word. If it equals endWord, return level. | 彈出 current，若等於 endWord 就回 level。 | Coding |
| For each index j in word, save original char. | 對字中每個位置 j，先存原字元。 | Coding |
| Try chars from a to z except original. | 嘗試 a 到 z（排除原字元）。 | Coding |
| If transformed word exists in set, enqueue and erase it. | 若變換字存在 set，入隊並刪除。 | Coding |
| Restore original char before next position. | 進下一位置前還原原字元。 | Coding |
| After finishing this layer, level plus plus. | 本層結束後 level++。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run hit to cog with hot dot dog lot log cog. | 我手跑 hit 到 cog，字典為 hot dot dog lot log cog。 | Dry-run |
| Level one queue has hit. | 第 1 層 queue 只有 hit。 | Dry-run |
| From hit we can form hot in dictionary. | 從 hit 可形成字典內的 hot。 | Dry-run |
| Level two processes hot and reaches dot and lot. | 第 2 層處理 hot，可到 dot 與 lot。 | Dry-run |
| Next level reaches dog and log. | 下一層可到 dog 與 log。 | Dry-run |
| Then from dog or log we reach cog. | 接著由 dog 或 log 到達 cog。 | Dry-run |
| Returned length is five. | 回傳長度為 5。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: endWord missing returns zero immediately. | 案例一：endWord 缺失時立即回 0。 | Edge test |
| Case two: beginWord already equals endWord, answer should be one under this level definition. | 案例二：beginWord=endWord 時，此定義下答案應為 1。 | Edge test |
| Case three: no possible path despite endWord present returns zero. | 案例三：即使有 endWord 但無路徑時回 0。 | Edge test |
| Case four: duplicate words in list should not break set-based logic. | 案例四：wordList 重複字不應破壞 set 邏輯。 | Edge test |
| Case five: very short one-letter words. | 案例五：極短一字母單字。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(M times L times 26). | 時間複雜度是 O(M*L*26)。 | Complexity |
| Space complexity is O(M times L) for queue and set storage of words. | 空間複雜度約 O(M*L)，主要是 queue 與 set 儲字。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each word is visited at most once because we erase it after enqueue. | 每個字最多訪問一次，因為入隊後就刪除。 | Complexity |
| For each visited word, we try L positions and 26 letters. | 每個訪問字會嘗試 L 個位置與 26 種字元。 | Complexity |
| So runtime is O(M times L times 26). | 因此時間是 O(M*L*26)。 | Complexity |
| Set plus queue hold up to M words, each length L. | set 與 queue 最多存 M 個長度 L 的字。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me model each word as a graph node. | 我把每個單字看成圖節點。 | If stuck |
| Edges connect words differing by one character. | 相差一字元的單字之間有邊。 | If stuck |
| We need shortest path length, so BFS is natural. | 我們要最短路長度，所以 BFS 最自然。 | If stuck |
| Level number directly maps to transformation length. | BFS 層數可直接對應轉換長度。 | If stuck |
| Erasing visited words prevents revisits and loops. | 刪除已訪字可避免重訪與循環。 | If stuck |
| Missing endWord means impossible at once. | endWord 缺失代表立即不可能。 | If stuck |
| Let me test quickly with hit to cog sample. | 我快速測 hit 到 cog 範例。 | If stuck |
| We should reach cog at level five. | 我們應在第 5 層到達 cog。 | If stuck |
| This confirms shortest-path behavior. | 這可驗證最短路特性。 | If stuck |
| Great, now implementation is clear. | 很好，現在實作很清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with BFS on implicit word graph. | 我用隱式單字圖的 BFS 解題。 | Wrap-up |
| One-level expansion equals one transformation step. | 每擴一層就多一步轉換。 | Wrap-up |
| Set lookup and erase keep traversal efficient. | set 查找與刪除讓遍歷高效。 | Wrap-up |
| Complexity is O(M times L times 26) time. | 時間複雜度是 O(M*L*26)。 | Wrap-up |
| This is the standard shortest-word-transform pattern. | 這是單字最短轉換題的標準模式。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: shortest transformation length from begin to end. | 目標：begin 到 end 的最短轉換長度。 | Cheat sheet |
| Must change one char each step. | 每步只能改一個字元。 | Cheat sheet |
| Intermediate words must be in dictionary. | 中間字必須在字典內。 | Cheat sheet |
| If end missing, return zero. | end 不在字典就回 0。 | Cheat sheet |
| Put dictionary into hash set. | 字典放入 hash set。 | Cheat sheet |
| Queue starts with beginWord. | queue 從 beginWord 開始。 | Cheat sheet |
| Level starts at one. | level 從 1 起算。 | Cheat sheet |
| BFS level order traversal. | BFS 逐層遍歷。 | Cheat sheet |
| Pop current word each step. | 每步先彈出 current。 | Cheat sheet |
| If current==end, return level. | 若 current=end，回 level。 | Cheat sheet |
| For each position try a..z replacements. | 每個位置嘗試 a..z 替換。 | Cheat sheet |
| If transformed in set, enqueue it. | 變換字在 set 就入隊。 | Cheat sheet |
| Erase transformed from set immediately. | 立刻從 set 刪除該字。 | Cheat sheet |
| After layer done, level++. | 一層完成後 level++。 | Cheat sheet |
| Queue exhausted means no path. | queue 耗盡表示無路徑。 | Cheat sheet |
| Return zero in no-path case. | 無路徑時回 0。 | Cheat sheet |
| Time O(M*L*26). | 時間 O(M*L*26)。 | Cheat sheet |
| Space about O(M*L). | 空間約 O(M*L)。 | Cheat sheet |
| Common bug: forgetting erase visited words. | 常見錯誤：忘記刪除已訪字。 | Cheat sheet |
| Explain why BFS gives shortest path. | 說明 BFS 為何保證最短路。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ BFS with dynamic neighbor generation and set pruning.
- No hallucinated constraints: ✅ End-word check and shortest-length semantics preserved.
- Language simplicity: ✅ concise interview-ready speaking lines.
