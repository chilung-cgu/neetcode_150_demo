# 01 Implement Trie (Prefix Tree) — Interview English Script (C++)

> Source aligned with: `docs/08_Tries/01_Implement_Trie_Prefix_Tree.md`

> Quick links: [Source Solution](../01_Implement_Trie_Prefix_Tree.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the implement-trie problem. | 我先重述 Trie 實作題目。 | Restatement |
| We need to design a Trie with insert, search, and startsWith. | 要設計含 insert、search、startsWith 的 Trie。 | Restatement |
| Input words contain lowercase letters only. | 輸入字串只含小寫字母。 | Restatement |
| search should match full word, not just prefix. | search 要比對完整單字，不是前綴。 | Restatement |
| startsWith only checks whether a prefix path exists. | startsWith 只確認前綴路徑是否存在。 | Restatement |
| I will use trie nodes with 26 child pointers and end flag. | 我會用 26 子指標與結尾旗標的 trie node。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume all characters are lowercase a to z? | 我可假設字元都在 a 到 z 嗎？ | Clarify |
| Should duplicate inserts keep behavior unchanged? | 重複 insert 是否維持相同行為即可？ | Clarify |
| For search, must whole word end at terminal flag? | search 是否一定要落在結尾旗標？ | Clarify |
| Is fixed array children preferred over hashmap here? | 此題是否偏好固定陣列而非 hashmap？ | Clarify |
| Do we need to implement delete operation? | 需要實作刪除操作嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force stores all words in a hash set. | 暴力法把所有字存進 hash set。 | Approach |
| insert and exact search are okay, but startsWith scans many words. | insert 與完整搜尋還行，但 startsWith 需掃大量字。 | Approach |
| That can degrade to O(n times L) per prefix query. | 前綴查詢會退化成 O(n*L)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use Trie where each edge corresponds to one character. | 使用 Trie，邊代表單一字元。 | Approach |
| insert walks through characters and creates missing nodes. | insert 沿字元走訪並建立缺節點。 | Approach |
| search walks path and checks terminal flag at end. | search 走完路徑後看結尾旗標。 | Approach |
| startsWith only needs path existence, no terminal check. | startsWith 只需路徑存在，不看結尾旗標。 | Approach |
| Each operation runs in O(L) where L is string length. | 每個操作皆為 O(L)。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I define TrieNode with children array of size twenty-six. | 我定義含 26 子指標陣列的 TrieNode。 | Coding |
| I also keep boolean isEndOfWord on each node. | 每節點再保留 isEndOfWord 旗標。 | Coding |
| In constructor, I create root node. | 在建構子中建立 root。 | Coding |
| For insert, I iterate each character and move pointer. | insert 逐字元迭代並移動指標。 | Coding |
| If child does not exist, I allocate new TrieNode. | 若子節點不存在就新建 TrieNode。 | Coding |
| After processing all characters, I mark end flag true. | 字串走完後把結尾旗標設 true。 | Coding |
| For search, I traverse path and return false on missing edge. | search 走訪路徑，邊不存在就回 false。 | Coding |
| After traversal, I return current node end flag. | 走完後回傳當前節點結尾旗標。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run: insert apple, search apple, search app, startsWith app. | 我手跑：insert apple、search apple、search app、startsWith app。 | Dry-run |
| Insert creates path a to p to p to l to e. | insert 會建立 a->p->p->l->e 路徑。 | Dry-run |
| Node e is marked as end of word. | 節點 e 會被標為結尾。 | Dry-run |
| search apple follows full path and ends at true flag. | search apple 走完整路徑且落在 true 旗標。 | Dry-run |
| search app follows path but end flag is false now. | search app 雖有路徑，但目前結尾旗標是 false。 | Dry-run |
| startsWith app returns true because path exists. | startsWith app 因路徑存在而回 true。 | Dry-run |
| After insert app, search app becomes true. | 再 insert app 後，search app 變 true。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: insert single character word. | 案例一：插入單字元單字。 | Edge test |
| Case two: search word never inserted should return false. | 案例二：搜尋未插入單字應回 false。 | Edge test |
| Case three: inserted long word but searching its prefix only. | 案例三：已插長字，搜尋其前綴完整字應分辨。 | Edge test |
| Case four: repeated insert of same word should stay stable. | 案例四：重複插入同字應維持穩定。 | Edge test |
| Case five: startsWith on non-existing first character returns false. | 案例五：不存在首字前綴應回 false。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each operation runs in O(L) time. | 每個操作時間皆為 O(L)。 | Complexity |
| Trie storage is O(total inserted characters). | Trie 儲存空間為 O(總插入字元數)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| insert, search, and startsWith scan one character per step. | insert、search、startsWith 每步處理一字元。 | Complexity |
| So per-operation runtime is O(L) with no full-dictionary scan. | 所以單次操作 O(L)，不需掃整個字典。 | Complexity |
| Space grows with number of created trie nodes. | 空間隨建立的 trie 節點數增長。 | Complexity |
| Using fixed 26-array trades memory for fast child access. | 固定 26 陣列是用空間換取快速存取。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me separate full-word and prefix semantics first. | 我先分清完整字與前綴語意。 | If stuck |
| search needs end flag true at final node. | search 需最終節點 end flag 為 true。 | If stuck |
| startsWith only needs path existence. | startsWith 只需路徑存在。 | If stuck |
| I might have returned true too early in search. | 我可能在 search 太早回 true。 | If stuck |
| Let me move true-return to after full traversal. | 我把 true 回傳移到完整走訪後。 | If stuck |
| I will retest apple versus app behavior. | 我重測 apple 與 app 的差異行為。 | If stuck |
| Now search app is false before insert app. | 現在 insert app 前 search app 為 false。 | If stuck |
| And startsWith app remains true. | 且 startsWith app 維持 true。 | If stuck |
| After insert app, search app is true. | insert app 後 search app 變 true。 | If stuck |
| Great, semantics are now correct. | 很好，語意現在正確。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I completed Trie with insert, search, and startsWith. | 我完成了含 insert/search/startsWith 的 Trie。 | Wrap-up |
| The key distinction is terminal flag for full-word search. | 核心差異是完整搜尋要看結尾旗標。 | Wrap-up |
| Runtime per call is O(L). | 每次呼叫時間是 O(L)。 | Wrap-up |
| Space depends on total created trie nodes. | 空間取決於建立的 trie 節點總量。 | Wrap-up |
| I can also discuss hashmap-children variant if needed. | 若需要我可補充 hashmap 子節點版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Build Trie data structure. | 建立 Trie 資料結構。 | Cheat sheet |
| Trie node has 26 children pointers. | Trie 節點有 26 子指標。 | Cheat sheet |
| Trie node has end-of-word flag. | Trie 節點有結尾旗標。 | Cheat sheet |
| Constructor creates root node. | 建構子建立 root。 | Cheat sheet |
| insert walks each character. | insert 逐字元走訪。 | Cheat sheet |
| create missing child nodes. | 缺節點時動態建立。 | Cheat sheet |
| mark end flag at last node. | 最後節點設結尾旗標。 | Cheat sheet |
| search traverses full word path. | search 走完整字路徑。 | Cheat sheet |
| missing edge => false. | 邊不存在 => false。 | Cheat sheet |
| final end flag decides true or false. | 最終以結尾旗標判定。 | Cheat sheet |
| startsWith traverses prefix path only. | startsWith 只走前綴路徑。 | Cheat sheet |
| no end flag check for startsWith. | startsWith 不檢查結尾旗標。 | Cheat sheet |
| per operation time O(L). | 單操作時間 O(L)。 | Cheat sheet |
| storage proportional to created nodes. | 儲存量與建立節點數成正比。 | Cheat sheet |
| test full word versus prefix. | 測完整字與前綴差異。 | Cheat sheet |
| test repeated insert stability. | 測重複插入穩定性。 | Cheat sheet |
| common bug: search returns true on prefix. | 常見錯誤：search 對前綴誤回 true。 | Cheat sheet |
| common bug: forgetting node initialization. | 常見錯誤：忘記節點初始化。 | Cheat sheet |
| mention hashmap children alternative. | 可提 hashmap 子節點替代。 | Cheat sheet |
| finish with complexity summary. | 最後總結複雜度。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Trie node array + end flag operations are preserved.
- No hallucinated constraints: ✅ Operation semantics and constraints align with source.
- Language simplicity: ✅ Spoken concise interview-ready lines.
