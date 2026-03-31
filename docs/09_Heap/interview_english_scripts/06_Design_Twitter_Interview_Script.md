# 06 Design Twitter — Interview English Script (C++)

> Source aligned with: `docs/09_Heap/06_Design_Twitter.md`

> Quick links: [Source Solution](../06_Design_Twitter.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate this mini Twitter design problem. | 我先重述這題迷你 Twitter 設計題。 | Restatement |
| We need post, follow, unfollow, and get news feed operations. | 需要 post、follow、unfollow、getNewsFeed。 | Restatement |
| Feed includes self tweets and followed users tweets. | 動態消息包含自己與追蹤對象的推文。 | Restatement |
| Feed must be ordered by most recent first. | 動態消息必須按最新時間排序。 | Restatement |
| Each getNewsFeed returns at most ten tweet ids. | 每次 getNewsFeed 最多回傳十則 id。 | Restatement |
| I will use hash maps plus heap-based k-way merge. | 我會用雜湊表加 heap 的多路合併。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should users implicitly follow themselves? | 使用者是否預設追蹤自己？ | Clarify |
| Is unfollow self disallowed or ignored? | 取消追蹤自己是禁止還是忽略？ | Clarify |
| Is tweet timestamp strictly increasing per post call? | 每次發文時間戳是否嚴格遞增？ | Clarify |
| Do we only return tweet ids, not full tweet objects? | 只回傳 tweet id，不回完整物件嗎？ | Clarify |
| Can we create user records lazily on first operation? | 可在首次操作時延遲建立 user 資料嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force stores all tweets globally in time order. | 暴力法把全部推文放全域時間序。 | Approach |
| getNewsFeed scans backward and filters by follow set. | getNewsFeed 倒掃並依追蹤集合過濾。 | Approach |
| That becomes too slow when total tweets grows. | 總推文量大時會太慢。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Store each user tweets as a linked list newest first. | 每位使用者推文以鏈結串列頭為最新。 | Approach |
| Keep followees as a hash set per user. | 每位使用者用 hash set 存 followees。 | Approach |
| For feed, push each timeline head into a max-heap by time. | 取 feed 時，把各時間線頭推入 max-heap。 | Approach |
| Pop newest tweet, append id, then push its next older node. | 彈出最新推文，加入答案，再推其 next。 | Approach |
| Repeat until ten tweets or heap becomes empty. | 重複到十則或 heap 為空。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I maintain a global timestamp that increments on each post. | 我維護全域 timestamp，每次 post 遞增。 | Coding |
| I define Tweet node with id, time, and next pointer. | 我定義 Tweet 節點含 id、time、next。 | Coding |
| User object stores followee set and tweet head pointer. | User 物件存 followee 集合與 tweet head。 | Coding |
| getUser helper lazily creates missing user records. | getUser 輔助函式會延遲建立使用者。 | Coding |
| postTweet prepends a new tweet node to user timeline. | postTweet 以頭插法放入新推文節點。 | Coding |
| follow inserts followee id; unfollow erases unless self. | follow 插入 id；unfollow 非自己才刪除。 | Coding |
| getNewsFeed pushes all followed timelines heads into heap. | getNewsFeed 把追蹤時間線頭都推入 heap。 | Coding |
| Pop and push-next up to ten times to build answer ids. | 最多執行十次彈出並推 next 組答案。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run the standard sequence from the prompt. | 我手跑題目常見操作序列。 | Dry-run |
| User one posts tweet five, so feed of one is [5]. | 使用者 1 發 5，1 的 feed 是 [5]。 | Dry-run |
| User one follows user two. | 使用者 1 追蹤使用者 2。 | Dry-run |
| User two posts tweet six with newer timestamp. | 使用者 2 發 6，時間更新。 | Dry-run |
| Feed of user one merges two timelines to [6,5]. | 使用者 1 feed 合併後為 [6,5]。 | Dry-run |
| User one unfollows two, so feed returns to [5]. | 使用者 1 取消追蹤 2，feed 回到 [5]。 | Dry-run |
| This matches expected behavior exactly. | 這與預期行為完全一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: new user asks feed before posting anything. | 案例一：新用戶未發文就取 feed。 | Edge test |
| Case two: user follows self explicitly multiple times. | 案例二：使用者重複追蹤自己。 | Edge test |
| Case three: unfollow self should not remove self timeline. | 案例三：unfollow self 不應移除自己時間線。 | Edge test |
| Case four: user follows many people but feed still capped at ten. | 案例四：追蹤很多人但 feed 仍最多十則。 | Edge test |
| Case five: one followee has long timeline, others are empty. | 案例五：只有一位 followee 有長時間線。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| post, follow, and unfollow are O(1) average. | post、follow、unfollow 平均 O(1)。 | Complexity |
| getNewsFeed is O(F + 10 log F), space O(F) for heap. | getNewsFeed 是 O(F + 10logF)，heap 空間 O(F)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Hash map and hash set operations are O(1) average. | hash map 與 hash set 操作平均 O(1)。 | Complexity |
| Feed building first pushes up to F timeline heads into heap. | 建 feed 先把最多 F 個時間線頭推入 heap。 | Complexity |
| Then we extract at most ten tweets, each with heap log F cost. | 之後最多取十則，每次成本 logF。 | Complexity |
| So feed time is O(F + 10 log F), extra heap memory O(F). | 因此 feed 時間 O(F+10logF)，額外空間 O(F)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me split this design into data model and feed query. | 我先把設計拆成資料模型與查詢。 | If stuck |
| Data model stores per-user follow set and tweet timeline. | 資料模型：每位用戶 follow set 與時間線。 | If stuck |
| Feed query is just merge k sorted lists by time. | feed 查詢本質是 k 路有序合併。 | If stuck |
| Heap should hold current head tweet from each timeline. | heap 要放各時間線當前 head。 | If stuck |
| After pop, push that node next pointer. | 每次 pop 後推該節點 next。 | If stuck |
| Stop once I collected ten tweet ids. | 收集到十則就停止。 | If stuck |
| I must ensure user always follows self. | 我必須確保使用者永遠追蹤自己。 | If stuck |
| I also block unfollow self operation. | 也要阻止 unfollow self。 | If stuck |
| Let me verify with [5], then [6,5], then [5]. | 我用 [5]、[6,5]、[5] 驗證流程。 | If stuck |
| Great, design invariants now look consistent. | 很好，設計不變量已一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I designed Twitter with hash structures and heap merge. | 我用 hash 結構加 heap 合併完成 Twitter 設計。 | Wrap-up |
| Posting and follow updates stay O(1) average. | 發文與追蹤更新維持平均 O(1)。 | Wrap-up |
| News feed is generated by k-way merge of timelines. | 動態消息透過多時間線 k 路合併產生。 | Wrap-up |
| We always return at most ten most recent tweet ids. | 始終回傳最多十則最新 tweet id。 | Wrap-up |
| I can discuss memory cleanup strategy in production systems. | 若需要我可補充正式系統的記憶體回收策略。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Design APIs: post, feed, follow, unfollow. | API：post、feed、follow、unfollow。 | Cheat sheet |
| Keep global increasing timestamp. | 維護全域遞增時間戳。 | Cheat sheet |
| User has followee hash set. | User 有 followee hash set。 | Cheat sheet |
| User has tweet linked list head. | User 有 tweet 鏈表 head。 | Cheat sheet |
| Self-follow is enforced by default. | 預設強制追蹤自己。 | Cheat sheet |
| Unfollow self is ignored. | unfollow 自己時忽略。 | Cheat sheet |
| post prepends new tweet node. | post 用頭插法新增 tweet。 | Cheat sheet |
| Feed includes self and followees. | feed 包含自己與 followees。 | Cheat sheet |
| Feed query uses max-heap by timestamp. | feed 查詢用 timestamp max-heap。 | Cheat sheet |
| Push each timeline head first. | 先推每條時間線 head。 | Cheat sheet |
| Pop newest tweet id into result. | pop 最新 tweet id 進答案。 | Cheat sheet |
| Push popped node next if exists. | 若有 next 就推回 heap。 | Cheat sheet |
| Stop at ten results or empty heap. | 十則或 heap 空時停止。 | Cheat sheet |
| post average O(1). | post 平均 O(1)。 | Cheat sheet |
| follow/unfollow average O(1). | follow/unfollow 平均 O(1)。 | Cheat sheet |
| feed O(F + 10 log F). | feed 為 O(F + 10logF)。 | Cheat sheet |
| feed extra space O(F). | feed 額外空間 O(F)。 | Cheat sheet |
| Common bug: forgetting self-follow. | 常見錯誤：忘記 self-follow。 | Cheat sheet |
| Common bug: returning more than ten ids. | 常見錯誤：回傳超過十則。 | Cheat sheet |
| Mental model: merge k sorted timelines. | 心智模型：合併 k 條有序時間線。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Hash map + max-heap merge-K design is preserved.
- No hallucinated constraints: ✅ API behavior follows source examples and assumptions.
- Language simplicity: ✅ Interview-friendly narration with concrete operation flow.
