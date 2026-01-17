# Partition Labels (劃分字母區間)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個字串 `s`。
我們要把這個字串劃分成盡可能多的片段 (partitions)。
使得**同一個字母最多只出現在一個片段中**。
回傳一個列表，包含每個片段的長度。

-   **Input**: `s = "ababcbacadefegdehijhklij"`
-   **Output**: `[9,7,8]`
    -   Partitions: "ababcbaca", "defegde", "hijhklij".
    -   'a' only appears in part 1.
    -   'd' only appears in part 2.
-   **Input**: `s = "eccbbbbdec"`
-   **Output**: `[10]`
-   **Constraints**:
    -   $1 <= s.length <= 500$

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試每一個切割點。
檢查當切割點為 `i` 時，左邊所有的字符是否都沒有出現在右邊。
需要多次 scan。

---

## 3. 💡 The "Aha!" Moment (優化)

**Greedy / Merge Intervals**:

1.  首先，對於每個字符，我們需要知道它 **最後一次出現的位置 (Last Index)**。
    -   因為如果一段區間包含了字符 'a'，那麼這個區間 **至少** 要延伸到 'a' 最後一次出現的地方，否則 'a' 就會被切斷。
2.  遍歷字串：
    -   維護當前區間的 `start` 和 `end`。
    -   對於當前字符 `c`，更新 `end = max(end, last_index[c])`。
    -   如果當前索引 `i` 到達了 `end`，說明在這個點之前的所有字符，它們的最後一次出現位置都在 `i` 或之前。
    -   這意味著我們可以安全地在這裡切一刀。
    -   記錄長度 `i - start + 1`，並更新下一個區間起點 `start = i + 1`。

這是一種貪心策略：每遇到一個字符，就貪心地擴展當前邊界，直到不能擴展為止（也就是抵達了邊界）。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../partition_labels_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../partition_labels_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy + Last Index Map

```cpp
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        // Step 1: Record the last occurrence of each character
        // Since input is lowercase English letters, array of size 26 is enough
        int lastIndex[26] = {0};
        for (int i = 0; i < s.length(); i++) {
            lastIndex[s[i] - 'a'] = i;
        }

        vector<int> result;
        int size = 0;
        int end = 0;

        // Step 2: Iterate and update boundaries
        for (int i = 0; i < s.length(); i++) {
            size++;
            // Expand the end boundary to the last occurrence of current char
            end = max(end, lastIndex[s[i] - 'a']);

            // If we reached the end boundary, it means all characters in the current
            // segment have their last occurrence within this segment.
            if (i == end) {
                result.push_back(size);
                size = 0; // Reset length for next partition
            }
        }

        return result;
    }
};
```

### Python Reference

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = { c: i for i, c in enumerate(s) }

        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        // 1. 紀錄每個字母「最後一次出現」的索引位置
        // 使用大小 26 的陣列比 Map 更快
        int lastIndex[26] = {0};
        for (int i = 0; i < s.length(); i++) {
            lastIndex[s[i] - 'a'] = i;
        }

        vector<int> result;
        int size = 0; // 當前區間長度
        int end = 0;  // 當前區間必須延伸到的最遠位置

        for (int i = 0; i < s.length(); i++) {
            size++;

            // 對於遇到的每個字元，它要求區間至少要延伸到它的最後出現位置
            end = max(end, lastIndex[s[i] - 'a']);

            // 如果當前遍歷到的位置 i 正好等於目前要求的結束位置 end
            // 代表前面所有字元的最後出現位置都在 i 之內
            // 所以可以在這裡切斷
            if (i == end) {
                result.push_back(size);
                size = 0; // 重置長度，準備下一個區間
            }
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Scan string twice (once for map, once for loop).
-   **Space Complexity**: $O(1)$
    -   Array of size 26 is constant.
