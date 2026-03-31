# 05 Alien Dictionary — Interview English Script (C++)

> Source aligned with: `docs/16_Advanced_Graphs/05_Alien_Dictionary.md`

> Quick links: [Source Solution](../05_Alien_Dictionary.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate alien dictionary. | 我先重述 Alien Dictionary。 | Restatement |
| We are given words already sorted in alien language order. | 題目給外星語已排序好的單字列表。 | Restatement |
| We need recover one valid character order. | 我們要推導一個合法字母順序。 | Restatement |
| If input is invalid or has cycle constraints, return empty string. | 若輸入不合法或約束成環，要回空字串。 | Restatement |
| First differing chars between adjacent words create precedence edges. | 相鄰單字首個不同字元會產生先後邊。 | Restatement |
| I will build graph then run topological BFS. | 我會建圖後跑拓撲 BFS。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should every distinct character in words appear in output? | words 裡所有出現字元都要出現在輸出嗎？ | Clarify |
| If multiple valid orders exist, any one is acceptable? | 若有多個合法順序，任意一個可接受嗎？ | Clarify |
| Prefix invalid case like abc before ab should return empty, right? | 前綴違規如 abc 在 ab 前是否要回空？ | Clarify |
| Are letters limited to lowercase English? | 字元是否限定小寫英文？ | Clarify |
| Is output empty when cycle is detected in precedence graph? | 若先後圖有環是否輸出空字串？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force trying all permutations of letters is infeasible. | 暴力試所有字母排列不可行。 | Approach |
| We need graph constraints extracted from sorted words. | 我們要先從排序字串抽圖約束。 | Approach |
| Then solve with topological ordering. | 再用拓撲排序求解。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Initialize indegree for all unique characters to zero. | 先把所有唯一字元 indegree 初始化為 0。 | Approach |
| Compare each adjacent word pair and find first differing character. | 比較每組相鄰單字，找第一個差異字元。 | Approach |
| Add directed edge c1 to c2 if not already added. | 若邊尚未存在，加入 c1->c2。 | Approach |
| Use queue with indegree-zero chars for Kahn BFS topological sort. | 用 indegree=0 字元 queue 做 Kahn BFS 拓撲排序。 | Approach |
| If result length less than unique chars count, cycle exists so return empty. | 若結果長度小於唯一字元數，代表有環回空字串。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I create adjacency map char to set of neighbors. | 我建立 char 到鄰居集合的 adjacency map。 | Coding |
| I create indegree map and add all characters with zero. | 我建立 indegree map 並把所有字元設為 0。 | Coding |
| For each adjacent words w1 and w2, check prefix invalid case first. | 對每組相鄰 w1,w2，先檢查前綴違規。 | Coding |
| If w1 longer and starts with w2, return empty string. | 若 w1 較長且前綴等於 w2，直接回空字串。 | Coding |
| Then scan characters until first mismatch. | 接著掃描字元直到第一個不相同。 | Coding |
| On mismatch c1 and c2, add edge c1 to c2 if new and indegree[c2]++. | 差異 c1,c2 時，若新邊就加 c1->c2 並 indegree[c2]++。 | Coding |
| Break after first mismatch only. | 第一個差異後就停止該對比較。 | Coding |
| Initialize queue with all chars whose indegree is zero. | 把所有 indegree=0 字元加入 queue。 | Coding |
| BFS pop char, append to result, decrease neighbors indegree. | BFS 出隊字元加到結果，再遞減鄰居 indegree。 | Coding |
| If final result size differs from unique char count, return empty else return result. | 若最終長度不等於唯一字元數回空，否則回結果。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run words wrt wrf er ett rftt. | 我手跑 words: wrt, wrf, er, ett, rftt。 | Dry-run |
| Compare wrt and wrf gives edge t to f. | 比較 wrt 與 wrf 得到邊 t->f。 | Dry-run |
| Compare wrf and er gives edge w to e. | 比較 wrf 與 er 得到邊 w->e。 | Dry-run |
| Compare er and ett gives edge r to t. | 比較 er 與 ett 得到邊 r->t。 | Dry-run |
| Compare ett and rftt gives edge e to r. | 比較 ett 與 rftt 得到邊 e->r。 | Dry-run |
| Topological BFS produces one order w e r t f. | 拓撲 BFS 會得到一種順序 w e r t f。 | Dry-run |
| Output string can be wertf. | 輸出字串可為 wertf。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single word, output all its unique chars. | 案例一：單字輸入，輸出其唯一字元。 | Edge test |
| Case two: invalid prefix order abc then ab returns empty. | 案例二：前綴違規 abc 在 ab 前時回空。 | Edge test |
| Case three: cycle constraints like z before x and x before z returns empty. | 案例三：z<x 且 x<z 成環時回空。 | Edge test |
| Case four: disconnected character groups still appear in output. | 案例四：不連通字元群也要出現在輸出。 | Edge test |
| Case five: duplicate edge inference should not double-increase indegree. | 案例五：重複推導同邊不能重複加 indegree。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(C) plus topological part O(V plus E). | 時間是 O(C)+拓撲 O(V+E)。 | Complexity |
| Space complexity is O(V plus E). | 空間複雜度是 O(V+E)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let C be total characters across all words. | 設 C 為所有單字總字元數。 | Complexity |
| Building constraints from adjacent pairs is linear in compared characters. | 從相鄰字對建約束，成本與比較字元數線性相關。 | Complexity |
| Topological BFS over character graph costs O(V plus E). | 字元圖拓撲 BFS 成本是 O(V+E)。 | Complexity |
| Adjacency sets and indegree maps store O(V plus E) information. | 鄰接集合與 indegree map 儲存 O(V+E) 資訊。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me derive constraints only from first mismatch. | 我只從第一個不匹配字元推導約束。 | If stuck |
| Later mismatches in same pair are irrelevant. | 同一對單字後續差異都不重要。 | If stuck |
| Prefix invalid case must be checked before edge extraction. | 取邊前必須先檢查前綴違規。 | If stuck |
| Graph nodes are all unique letters, even isolated ones. | 圖節點是所有唯一字母，含孤立字母。 | If stuck |
| Kahn BFS handles ordering and cycle detection together. | Kahn BFS 可同時做排序與環檢測。 | If stuck |
| If result misses nodes, cycle exists. | 若結果缺節點，代表有環。 | If stuck |
| Let me test quickly with z x z. | 我快速測 z, x, z。 | If stuck |
| Constraints become z before x and x before z. | 約束會變成 z<x 與 x<z。 | If stuck |
| That should return empty string. | 該情況應回空字串。 | If stuck |
| Great, now failure conditions are clear. | 很好，失敗條件已清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it by building precedence graph then topological sorting. | 我先建字元先後圖，再做拓撲排序解題。 | Wrap-up |
| First mismatch between adjacent words gives valid directed constraint. | 相鄰單字首個差異給出有效有向約束。 | Wrap-up |
| Prefix invalid case is handled explicitly. | 前綴違規情況有明確處理。 | Wrap-up |
| Cycle or contradiction returns empty string. | 有環或矛盾時回空字串。 | Wrap-up |
| Complexity is linear in input parsing plus graph topo cost. | 複雜度是輸入解析線性加圖拓撲成本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: infer alien letter order from sorted words. | 目標：從排序單字推導外星字母順序。 | Cheat sheet |
| Build nodes from all unique letters. | 用所有唯一字母建節點。 | Cheat sheet |
| Compare adjacent words only. | 只比較相鄰單字。 | Cheat sheet |
| Check invalid prefix first. | 先檢查前綴違規。 | Cheat sheet |
| If longer word before its prefix => empty. | 長字在其前綴前面 => 回空。 | Cheat sheet |
| Find first mismatch c1 c2. | 找第一個差異 c1,c2。 | Cheat sheet |
| Add edge c1 -> c2 once. | 只加一次邊 c1->c2。 | Cheat sheet |
| Increase indegree of c2 when new edge added. | 新邊加入時遞增 c2 indegree。 | Cheat sheet |
| Kahn queue starts with indegree zero chars. | Kahn queue 從 indegree 0 字元開始。 | Cheat sheet |
| Pop char, append to result. | 出隊字元並加入結果。 | Cheat sheet |
| Decrease indegree of neighbors. | 遞減鄰居 indegree。 | Cheat sheet |
| Push neighbor when indegree reaches zero. | 鄰居 indegree 到 0 就入隊。 | Cheat sheet |
| End with result length check. | 最後檢查結果長度。 | Cheat sheet |
| If length != unique count => cycle => empty. | 長度不符唯一數 => 有環 => 空字串。 | Cheat sheet |
| Return result string otherwise. | 否則回傳結果字串。 | Cheat sheet |
| Time parse O(C) plus topo O(V+E). | 時間 O(C)+O(V+E)。 | Cheat sheet |
| Space O(V+E). | 空間 O(V+E)。 | Cheat sheet |
| Common bug: using second mismatch edge. | 常見錯誤：誤用第二個差異建邊。 | Cheat sheet |
| Common bug: forgetting isolated letters. | 常見錯誤：漏掉孤立字母。 | Cheat sheet |
| Explain with wrt wrf er ett rftt sample. | 用 wrt/wrf/er/ett/rftt 範例說明。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ first-difference edge extraction + Kahn topo preserved.
- No hallucinated constraints: ✅ prefix-invalid and cycle-empty semantics maintained.
- Language simplicity: ✅ concise interview speaking style.
