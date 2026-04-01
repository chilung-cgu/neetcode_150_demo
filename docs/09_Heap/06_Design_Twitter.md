---
title: "Design Twitter (設計推特)"
description: "題目要求設計一個簡化版的 Twitter，支援："
tags:
  - Heap
  - Priority Queue
difficulty: Medium
---

# Design Twitter (設計推特) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #355** — [題目連結](https://leetcode.com/problems/design-twitter/) | [NeetCode 解說](https://neetcode.io/problems/design-twitter-feed)


## 1. 🧐 Problem Dissection (釐清問題)

題目要求設計一個簡化版的 Twitter，支援：

1.  `postTweet(userId, tweetId)`: 使用者發布推文。
2.  `getNewsFeed(userId)`: 取得使用者的新聞牆 (News Feed)。
    -   新聞牆包含 **自己** 發的推文，以及 **關注對象 (Proposees)** 發的推文。
    -   必須按照 **時間倒序** (Most Recent) 排列。
    -   最多只取 **前 10 則**。
3.  `follow(followerId, followeeId)`: 追蹤某人。
4.  `unfollow(followerId, followeeId)`: 取消追蹤。

-   **Input**:
    ```
    twitter.postTweet(1, 5);
    twitter.getNewsFeed(1); // [5]
    twitter.follow(1, 2);
    twitter.postTweet(2, 6);
    twitter.getNewsFeed(1); // [6, 5]
    twitter.unfollow(1, 2);
    twitter.getNewsFeed(1); // [5]
    ```

-   **Constraints**:
    -   User IDs / Tweet IDs are integers.
    -   At most $3 \times 10^4$ operations.

---

## 2. 🐢 Brute Force Approach (暴力解)

-   存所有推文在一個大的 List `[(time, userId, tweetId)]`。
-   `getNewsFeed`: 遍歷大 List (從後往前)，過濾出 userId 符合 (自己或 followee) 的推文，取前 10 個。
-   **Time**: $O(TotalTweets)$. 太慢。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是經典的 **Merge K Sorted Lists** 問題的變形。

每個使用者都有一條自己的 **Tweet Timeline** (Sorted by time)。
當我們要產生 `userId` 的 News Feed 時，我們需要：

1.  拿出 `userId` 自己的 Timeline。
2.  拿出所有 `followees` 的 Timelines。
3.  從這 **$k+1$ 條已排序的鏈表** 中，合併並找出最新的 10 則推文。

我們可以使用 **Max-Heap** 來進行多路歸併 (Multi-way Merge)。

-   Heap 中存每一條 Timeline 的當前最新推文 `(time, tweetId, nextIndex/pointer)`。
-   每次 Pop 出最新的，加到結果。
-   然後從該條 Timeline 取下一個較舊的推文 Push 進 Heap。
-   重複 10 次。

**Data Structures**:

-   `Global Timestamp`: `time++` whenever tweet posted.
-   `User Map`: `userId -> User Object`.
    -   `User Object`:
        -   `followees`: Set of userIds.
        -   `tweets`: List/LinkedList of `(time, tweetId)`. Head is most recent.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../twitter_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../twitter_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Map + Max-Heap (Merge K Sorted Lists)

```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

class Twitter {
private:
    int timestamp;

    struct Tweet {
        int id;
        int time;
        Tweet* next; // Singly linked list for simple "next" logic
        Tweet(int id, int time) : id(id), time(time), next(nullptr) {}
    };

    struct User {
        int id;
        unordered_set<int> followees;
        Tweet* tweetHead;

        User(int id) : id(id), tweetHead(nullptr) {
            followees.insert(id); // Follow self implicitly
        }

        void post(int tweetId, int time) {
            Tweet* t = new Tweet(tweetId, time);
            t->next = tweetHead;
            tweetHead = t;
        }

        void follow(int id) {
            followees.insert(id);
        }

        void unfollow(int id) {
            if (id != this->id) { // Cannot unfollow self
                followees.erase(id);
            }
        }
    };

    unordered_map<int, User*> userMap;

    // Helper to ensure user exists
    User* getUser(int id) {
        if (userMap.find(id) == userMap.end()) {
            userMap[id] = new User(id);
        }
        return userMap[id];
    }

public:
    Twitter() {
        timestamp = 0;
    }

    void postTweet(int userId, int tweetId) {
        getUser(userId)->post(tweetId, timestamp++);
    }

    vector<int> getNewsFeed(int userId) {
        User* user = getUser(userId);

        // Priority Queue for merging: stores {time, Tweet*}
        // C++ PQ pairs sort by first element (time) descending by default (Max-Heap)
        priority_queue<pair<int, Tweet*>> maxHeap;

        // Push head tweets of self and all followees
        for (int followeeId : user->followees) {
            User* followee = getUser(followeeId); // Ensure followee exists
            if (followee->tweetHead) {
                maxHeap.push({followee->tweetHead->time, followee->tweetHead});
            }
        }

        vector<int> feed;
        while (!maxHeap.empty() && feed.size() < 10) {
            Tweet* t = maxHeap.top().second;
            maxHeap.pop();

            feed.push_back(t->id);

            if (t->next) {
                maxHeap.push({t->next->time, t->next});
            }
        }

        return feed;
    }

    void follow(int followerId, int followeeId) {
        getUser(followerId)->follow(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        getUser(followerId)->unfollow(followeeId);
    }
};
```

### Python Reference

```python
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Twitter {
    int time = 0; // 全域時間戳

    // Tweet 使用 Linked List 結構，方便在 Heap 中快速找到 Next
    struct Tweet {
        int id;
        int time;
        Tweet* next = nullptr;
        Tweet(int i, int t) : id(i), time(t) {}
    };

    // User 結構，包含 followees 和自己的推文列表
    struct User {
        int id;
        unordered_set<int> following;
        Tweet* head = nullptr; // 最新推文指標

        User(int i) : id(i) {
            following.insert(i); // 自己也要追蹤自己，方便 NewsFeed 統一處理
        }

        void post(int tweetId, int time) {
            Tweet* t = new Tweet(tweetId, time);
            t->next = head; // 頭插法，讓最新的在前面
            head = t;
        }
    };

    unordered_map<int, User*> users;

public:
    Twitter() {}

    void postTweet(int userId, int tweetId) {
        if (!users.count(userId)) users[userId] = new User(userId);
        users[userId]->post(tweetId, time++);
    }

    // 這是最關鍵的函式：Merge K Sorted Lists
    vector<int> getNewsFeed(int userId) {
        if (!users.count(userId)) return {};

        // Priority Queue (Max-Heap) 用於排序多個 User 的推文流
        // pair: <time, Tweet*>
        priority_queue<pair<int, Tweet*>> pq;

        // 把自己和所有追蹤對象的「最新一則推文」放入 Heap
        for (int followeeId : users[userId]->following) {
            if (users.count(followeeId) && users[followeeId]->head) {
                pq.push({users[followeeId]->head->time, users[followeeId]->head});
            }
        }

        vector<int> res;
        // 取出前 10 則
        while (!pq.empty() && res.size() < 10) {
            Tweet* t = pq.top().second;
            pq.pop();

            res.push_back(t->id);

            // 如果這個 User 還有下一則舊推文，放進 Heap 繼續比較
            if (t->next) {
                pq.push({t->next->time, t->next});
            }
        }

        return res;
    }

    void follow(int followerId, int followeeId) {
        if (!users.count(followerId)) users[followerId] = new User(followerId);
        if (!users.count(followeeId)) users[followeeId] = new User(followeeId);
        users[followerId]->following.insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        if (!users.count(followerId) || followerId == followeeId) return;
        users[followerId]->following.erase(followeeId);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**:
    -   `postTweet`: $O(1)$.
    -   `follow/unfollow`: $O(1)$.
    -   `getNewsFeed`: $O(F)$, where $F$ is number of followees.
        -   Heap init takes $O(F)$. (Building heap from $F$ items).
        -   Extracting $10$ items takes $O(10 \log F)$.
        -   So if $F$ is small, it's very fast.
-   **Space Complexity**: $O(U + T)$.
    -   $U$ is number of users.
    -   $T$ is total number of tweets.

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 你會如何處理更大的輸入？
- 有沒有更好的空間複雜度？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有考慮邊界條件
- ⚠️ 未討論複雜度

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 主動討論 trade-offs
- 💎 提供多種解法比較
