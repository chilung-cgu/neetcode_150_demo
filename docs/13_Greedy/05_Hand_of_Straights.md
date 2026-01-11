# Hand of Straights (一手順子)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個整數陣列 `hand`，其中每個數字代表一張牌。還有一個整數 `groupSize`。
判斷是否能將這些牌重新排列成若干組，每組包含 `groupSize` 張牌，且這 `groupSize` 張牌是 **連續的** (consecutive)。

-   **Input**: `hand = [1,2,3,6,2,3,4,7,8], groupSize = 3`
-   **Output**: `true`
    -   [1,2,3], [2,3,4], [6,7,8]
-   **Input**: `hand = [1,2,3,4,5], groupSize = 4`
-   **Output**: `false`
    -   Hand size 5 is not divisible by 4.
-   **Constraints**:
    -   $1 <= hand.length <= 10^4$
    -   $0 <= hand[i] <= 10^9$
    -   $1 <= groupSize <= hand.length$

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試所有排列組合？太慢。
或者 Sort 後嘗試分組？
如果 Sort 後是 `[1, 2, 2, 3, 3, 4, 6, 7, 8]`

-   取最小的 `1`，需要 `2` 和 `3`.
-   剩下 `[2, 3, 4, 6, 7, 8]`.
-   取最小的 `2`，需要 `3` 和 `4`.
-   ...
這看起來不像蠻力，這其實就是 greedy。

---

## 3. 💡 The "Aha!" Moment (優化)

這題的關鍵是與 "Divide Array in Sets of K Consecutive Numbers" (LeetCode 1296) 完全相同。

**Greedy Strategy**:
1.  如果 `hand.length` 不能被 `groupSize` 整除，直接 False。
2.  使用 **Hash Map** (Frequency Count) 統計每張牌的出現次數。
3.  使用 **Min-Heap** 或者 **Sort** 讓牌有序。
    -   每次取出當前 **最小的牌** `min_val`。
    -   既然 `min_val` 存在，它必須作為某個順子的 **起點** (因為沒有比它更小的牌來接它)。
    -   檢查 `min_val, min_val + 1, ..., min_val + groupSize - 1` 是否都存在於 Map 中。
    -   如果存在，將它們的計數減 1 (或者減去 `min_val` 的 count 這麼多次，做批量處理)。
    -   如果有任何一張牌不夠，Return False。

**Ordered Map Approach**:
C++ 的 `map` 是有序的。我們可以遍歷 `map`。
但是要注意，遍歷過程中修改 map (減少 count) 會比較麻煩。
通常我們只遍歷 key。

**Sorting Approach**:
先對 `hand` 排序。
統計 `count`。
遍歷排序後的 `hand`：
如果 `count[card] > 0`，嘗試構建以 `card` 為起點的順子。
這個方法比較直觀且易於實作。

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Map + Min Heap (or Sorting)

```cpp
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize != 0) return false;

        // Use an ordered map to count frequencies and keep keys sorted
        map<int, int> counts;
        for (int card : hand) {
            counts[card]++;
        }

        // Iterate through the map
        for (auto it = counts.begin(); it != counts.end(); ++it) {
            int startCard = it->first;
            int count = it->second;

            // If count is 0, this card was already consumed by a previous sequence
            if (count > 0) {
                // We need to form 'count' number of groups starting with 'startCard'
                // Each group needs startCard, startCard+1, ..., startCard+groupSize-1
                for (int i = 0; i < groupSize; i++) {
                    int currentCard = startCard + i;
                    if (counts[currentCard] < count) {
                        return false;
                    }
                    counts[currentCard] -= count;
                }
            }
        }

        return true;
    }
};
```

### Python Reference

```python
import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False

                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False # Optimization: Must remove min element
                    heapq.heappop(min_heap)

        return True
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        // 基本檢查
        if (hand.size() % groupSize != 0) return false;

        // 使用 map (Ordered Map) 統計頻率並自動排序
        // 這樣我們可以按順序處理每張牌
        map<int, int> counts;
        for (int card : hand) {
            counts[card]++;
        }

        // 遍歷所有獨特的牌
        for (auto it = counts.begin(); it != counts.end(); ++it) {
            int startCard = it->first;
            int count = it->second;

            // 如果這張牌還有剩餘 (count > 0)
            // 由於它是目前 map 中最小的 key (因為我們依序遍歷)，
            // 它 *必須* 作為某些順子的起點。
            // 它不能作為中間或結尾，否則會有更小的牌在它前面 (但更小的牌已經被處理完了)。
            if (count > 0) {
                // 我們需要同時構建 `count` 個順子
                // 檢查接下的 groupSize-1 張牌是否足夠
                for (int i = 0; i < groupSize; i++) {
                    int nextCard = startCard + i;

                    // 如果後續的牌不夠用，或是根本不存在，則失敗
                    if (counts[nextCard] < count) {
                        return false;
                    }

                    // 扣掉相應的數量
                    counts[nextCard] -= count;
                }
            }
        }

        return true;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \log N)$ or $O(N \log M)$ (where M is unique cards)
    -   Map operations take log time. Iterating map takes linear.
    -   Sort takes $N \log N$.
-   **Space Complexity**: $O(N)$
    -   Map to store counts.
