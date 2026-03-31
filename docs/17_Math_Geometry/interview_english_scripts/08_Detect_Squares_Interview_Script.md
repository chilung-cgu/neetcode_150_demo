# 08 Detect Squares — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/08_Detect_Squares.md`

> Quick links: [Source Solution](../08_Detect_Squares.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Detect Squares. | 我先重述 Detect Squares。 | Restatement |
| We need a data structure supporting add and count operations. | 這題要設計支援 add 與 count 的資料結構。 | Restatement |
| Points are added on 2D grid, and duplicates are allowed. | 點會加在 2D 平面，且可重複出現。 | Restatement |
| count(query) asks how many axis-aligned squares use query as one corner. | count(query) 要求以 query 為角點可形成多少軸對齊正方形。 | Restatement |
| I will store point frequencies and iterate candidate diagonal points. | 我會存點頻率並枚舉對角候選點。 | Restatement |
| Multiplicity from duplicates is handled by multiplication of frequencies. | 重複點會用頻率乘積正確計數。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Are all squares required to be axis-aligned only? | 正方形是否限定軸對齊？ | Clarify |
| Can identical points be added multiple times and counted with multiplicity? | 相同點可重複 add 並用乘法計數嗎？ | Clarify |
| Is coordinate range bounded, for example zero to one thousand? | 座標範圍是否有上界如 0 到 1000？ | Clarify |
| Does count need to include every valid combination from duplicates? | count 是否要計入所有重複點組合？ | Clarify |
| Is O(n) count per query acceptable here? | 每次 count 為 O(n) 是否可接受？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force picks three other points and checks square geometry each query. | 暴力法每次挑三個點檢查是否成方形。 | Approach |
| That is extremely expensive combinatorially. | 其組合成本非常高。 | Approach |
| We need frequency-aware hashing with smarter enumeration. | 我們需要帶頻率的雜湊搭配更聰明枚舉。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Store every added point in a list to iterate candidates later. | 用列表保存所有加入點供後續枚舉。 | Approach |
| Also store frequency count for each coordinate pair lookup. | 另外存每個座標點的頻率以便查詢。 | Approach |
| For query qx,qy, iterate each point x,y as potential diagonal. | 對查詢 qx,qy，把每個 x,y 當可能對角點。 | Approach |
| Valid diagonal requires abs(qx minus x) equals abs(qy minus y) and x not equal qx. | 合法對角需 |qx-x|=|qy-y| 且 x!=qx。 | Approach |
| Add count of corners (x,qy) times (qx,y), summing across all candidates. | 把 (x,qy) 與 (qx,y) 的頻率乘積累加。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| In constructor, initialize frequency grid or hash map and points list. | 建構子先初始化頻率結構與 points 列表。 | Coding |
| In add(point), extract x and y. | add(point) 時先取 x、y。 | Coding |
| Increment frequency at x,y. | x,y 的頻率加一。 | Coding |
| Push point into points list preserving duplicates. | 把點放入列表，保留重複出現。 | Coding |
| In count(query), set qx,qy and answer zero. | count(query) 時設定 qx、qy 與答案 0。 | Coding |
| Iterate every stored point x,y from list. | 逐一枚舉列表中的 x,y。 | Coding |
| Skip if not a valid diagonal for axis-aligned square. | 若不符軸對齊對角條件就跳過。 | Coding |
| Otherwise add frequency(x,qy) times frequency(qx,y). | 否則加上 frequency(x,qy)*frequency(qx,y)。 | Coding |
| Return final accumulated answer. | 回傳累加後答案。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run add three-ten, add eleven-two, add three-two, then count eleven-ten. | 我手跑 add(3,10)、add(11,2)、add(3,2)，再 count(11,10)。 | Dry-run |
| Candidate diagonal three-two works because side lengths match. | 對角候選 (3,2) 可行，因為邊長相等。 | Dry-run |
| Needed corners are three-ten and eleven-two. | 需要另外兩角是 (3,10) 與 (11,2)。 | Dry-run |
| Both exist with frequency one. | 兩點都存在且頻率為 1。 | Dry-run |
| Contribution is one times one equals one. | 貢獻是 1*1=1。 | Dry-run |
| No other candidate contributes in this state. | 其他候選在此狀態無貢獻。 | Dry-run |
| Final count is one. | 最終計數為 1。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: query point has no possible diagonal. | 案例一：查詢點沒有可行對角點。 | Edge test |
| Case two: duplicate corner points increase answer multiplicatively. | 案例二：角點重複出現會乘法增加答案。 | Edge test |
| Case three: points on same x or same y as query should be skipped as diagonal. | 案例三：與 query 同 x 或同 y 的點不可當對角。 | Edge test |
| Case four: multiple distinct squares from one query. | 案例四：同一查詢可形成多個不同正方形。 | Edge test |
| Case five: minimal additions before any square is possible. | 案例五：僅少量點時應尚無方形。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| add runs in O(1). | add 的時間是 O(1)。 | Complexity |
| count runs in O(p) where p is number of stored points, with O(p) storage plus frequency structure. | count 是 O(p)，p 為已存點數；空間含 O(p) 列表與頻率結構。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| add updates frequency and appends point once, so it is constant-time. | add 只做一次頻率更新與附加，為常數時間。 | Complexity |
| count iterates all stored points as candidate diagonals. | count 需枚舉所有已存點當對角候選。 | Complexity |
| Each candidate check and frequency lookup is O(1). | 每個候選判斷與查頻率都是 O(1)。 | Complexity |
| So count is O(p), and memory is linear in stored points plus frequency table. | 故 count 為 O(p)，空間是點數線性加頻率表。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me pin down geometry for axis-aligned squares. | 我先釘清軸對齊正方形幾何條件。 | If stuck |
| Query and candidate must be diagonal with equal delta x and delta y in magnitude. | query 與候選需為對角，且 x、y 差絕對值相等。 | If stuck |
| Also delta x cannot be zero, otherwise area is zero. | 且 delta x 不能是 0，否則面積為零。 | If stuck |
| Once diagonal is fixed, other two corners are deterministic. | 對角固定後，另兩角是唯一決定的。 | If stuck |
| They are x with qy and qx with y. | 兩角即 (x,qy) 與 (qx,y)。 | If stuck |
| Multiply their frequencies for contribution count. | 把這兩點頻率相乘作為貢獻。 | If stuck |
| Duplicates are naturally handled by frequency multiplication. | 重複點會自然由頻率乘法處理。 | If stuck |
| I will verify with one duplicate scenario quickly. | 我快速驗證一個重複點場景。 | If stuck |
| If answer doubles as expected, counting logic is right. | 若答案如預期倍增，計數邏輯就正確。 | If stuck |
| Great, now implementation path is clear. | 很好，現在實作路徑清楚。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it with frequency counting plus diagonal enumeration. | 我用頻率統計加對角枚舉解題。 | Wrap-up |
| Axis-aligned geometry makes missing corners deterministic. | 軸對齊幾何讓缺失角點可被唯一推導。 | Wrap-up |
| Duplicate points are handled correctly through multiplicative counts. | 重複點可透過乘法計數正確處理。 | Wrap-up |
| add is O(1), count is O(p). | add 是 O(1)，count 是 O(p)。 | Wrap-up |
| This is the standard accepted interview design. | 這是面試常見且可接受的標準設計。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: support add and count for axis-aligned squares. | 目標：支援軸對齊方形的 add 與 count。 | Cheat sheet |
| Store points list including duplicates. | 列表儲存所有點含重複。 | Cheat sheet |
| Store frequency by coordinate. | 以座標儲存頻率。 | Cheat sheet |
| add: freq[x][y]++, push point. | add：freq[x][y]++ 並加入列表。 | Cheat sheet |
| count(query): iterate all stored points. | count(query)：枚舉全部已存點。 | Cheat sheet |
| Candidate must satisfy abs(dx)==abs(dy). | 候選需滿足 abs(dx)==abs(dy)。 | Cheat sheet |
| Also require dx!=0. | 且 dx!=0。 | Cheat sheet |
| Other corners are (x,qy) and (qx,y). | 另外兩角是 (x,qy)、(qx,y)。 | Cheat sheet |
| Contribution = freq(x,qy)*freq(qx,y). | 貢獻=freq(x,qy)*freq(qx,y)。 | Cheat sheet |
| Sum all candidate contributions. | 累加所有候選貢獻。 | Cheat sheet |
| Return total count. | 回傳總數。 | Cheat sheet |
| add complexity O(1). | add 複雜度 O(1)。 | Cheat sheet |
| count complexity O(p). | count 複雜度 O(p)。 | Cheat sheet |
| Space linear in stored points. | 空間對已存點數為線性。 | Cheat sheet |
| Duplicate points naturally multiply combinations. | 重複點會自然放大組合數。 | Cheat sheet |
| Common bug: counting same-x or same-y candidate as diagonal. | 常見錯誤：把同 x 或同 y 候選當對角。 | Cheat sheet |
| Common bug: forgetting duplicates in answer. | 常見錯誤：忘記重複點對答案影響。 | Cheat sheet |
| Verify with example returning one first. | 用初始案例回傳 1 驗證。 | Cheat sheet |
| Add duplicate point and verify count increases. | 再加重複點檢查答案上升。 | Cheat sheet |
| Explain geometry first, then coding details. | 先講幾何，再講實作，最清晰。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Diagonal-based counting with frequencies.
- Constraint alignment: ✅ Duplicate-point multiplicity handled.
- Language simplicity: ✅ Interview-ready concise structure.
