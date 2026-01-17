# Longest Consecutive Sequence (最長連續序列)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個**未排序**的整數陣列 `nums`，找出其中數字最長的「連續序列」長度。
例如：`[100, 4, 200, 1, 3, 2]`
連續序列是 `[1, 2, 3, 4]`，長度為 4。

- **Constraints**:
  - 題目強制要求 **$O(n)$** Time Complexity。
  - 這直接封殺了 Sorting 解法 ($O(n \log n)$)。

---

## 2. 🐢 Brute Force (Sorting)

即使題目說不行，我們還是先想一下 Sorting。

1.  Sort array: `[1, 2, 3, 4, 100, 200]`
2.  Iterate: 如果 `nums[i] == nums[i-1] + 1`，長度 +1。
3.  **Cost**: $O(n \log n)$。

---

## 3. 💡 The "Aha!" Moment (優化)

要達到 $O(n)$，我們必須使用 **Hash Set** 來達成 $O(1)$ 的 lookup。

思路：

1.  把所有數字丟進 `unordered_set`。能快速知道某個數字存不存在。
2.  遍歷陣列中的每一個數字 `num`。
3.  **關鍵判斷**：我們怎麼知道 `num` 是不是一個序列的**開頭**？
    - 檢查 `num - 1` 是否存在於 Set 中。
    - 如果 `num - 1` **不存在**，那 `num` 肯定是序列的第一個數字 (e.g., 1 沒有 0，所以 1 是開頭)。
    - 如果 `num - 1` **存在**，那 `num` 就不是開頭，我們直接跳過 (因為之後處理 `num-1` 或更前面的數字時，自然會算到 `num`)。
4.  如果是開頭，就開始 `while` loop 往上數：`num + 1` 在不在？ `num + 2` 在不在？... 直到斷掉。

這樣每個數字最多被 access 兩次 (一次是 check start，一次是 being counted)，所以是嚴格的 $O(n)$。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../longest_consecutive_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../longest_consecutive_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hash Set

```cpp
#include <vector>
#include <unordered_set>
#include <algorithm> // max

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for (int n : numSet) { // 遍歷 Set 而不是 vector 可以自動去重
            // Check if 'n' is the start of a sequence
            if (numSet.find(n - 1) == numSet.end()) {
                int length = 0;
                while (numSet.find(n + length) != numSet.end()) {
                    length++;
                }
                longest = max(longest, length);
            }
        }

        return longest;
    }
};
```

### Python Reference

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // 1. 將所有數字放入 Hash Set，達到 O(1) 查詢
        // 同時去除重複數字，這對這題沒影響 (連續序列不需重複)
        unordered_set<int> elements(nums.begin(), nums.end());

        int maxLen = 0;

        for (int num : elements) {
            // 2. 只有當 num 是序列的「起點」時，才開始計算
            // 判斷方式：如果 num - 1 不在 set 裡，那 num 必然是起點
            if (elements.find(num - 1) == elements.end()) {
                int currentNum = num;
                int currentLen = 1;

                // 3. 往上尋找 consecutive elements
                // 這是一個 inner loop，但因為每個數字只會被執行 "計數" 一次
                // 所以整體還是 O(n)
                while (elements.find(currentNum + 1) != elements.end()) {
                    currentNum += 1;
                    currentLen += 1;
                }

                // 4. 更新最大長度
                if (currentLen > maxLen) {
                    maxLen = currentLen;
                }
            }
        }

        return maxLen;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - 建構 Set: $O(n)$。
  - 遍歷 Set: 雖然有一個 `while` 在 `for` 裡面，看起來像 $O(n^2)$，但實際上，只有當數字是 Sequence Start 時才會進入 `while`。
  - 舉例：`[1, 2, 3, 4]`。
    - `1`: 是 start. While loop 跑 4 次 (count 1,2,3,4)。
    - `2`: 不是 start (1 exists). Skip.
    - `3`: 不是 start. Skip.
    - `4`: 不是 start. Skip.
  - 總操作次數是 $n + n = 2n$，所以是線性時間。
- **Space Complexity**: $O(n)$
  - Hash Set 儲存所有 unique numbers。
