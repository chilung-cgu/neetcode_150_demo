# Two Sum (兩數之和)

## 1. 🧐 Problem Dissection (釐清問題)

這是 LeetCode 的第一題，經典中的經典。
題目給我一個整數陣列 `nums` 和一個目標值 `target`，要我找出兩個數字，相加等於 `target`，並回傳它們的 **index**。

-   **Constraints**:
    -   只會有 **唯一解** (Exactly one solution)。這簡化了很多事情。
    -   不可以重複使用同一個元素 (Can't use the same element twice)。
-   **Clarification**:
    -   陣列是排序好的嗎？(通常沒有)
    -   可能有負數嗎？(有)
    -   這題很重要，因為它不僅考你程式能力，還考你對 `Hash Map` 應用場景的直覺。

---

## 2. 🐢 Brute Force Approach (暴力解)

"對於每一個數字 `x`，我們去後面找有沒有一個數字 `y` 等於 `target - x`。"

```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }
    return {};
}
```

-   **Time Complexity**: $O(n^2)$。
-   **Space Complexity**: $O(1)$。
-   **問題**: 隨著 `n` 變大，效率急劇下降。

---

## 3. 💡 The "Aha!" Moment (優化)

我們在暴力解中，內層迴圈在做什麼？
-> "在陣列中尋找一個值 `target - nums[i]`"。

**這就是 Hash Map 最擅長的事：快速查找 (Look up)。**

我們可以迭代 `nums`，對於每個數字 `n`：

1.  計算我們需要的另一半：`diff = target - n`。
2.  問 Hash Map： "你裡面用過 `diff` 嗎？"
    -   如果有，太棒了！我們找到了答案 `{map[diff], current_index}`。
    -   如果沒有，把現在這個數字 `n` 和它的 `index` 存進 Hash Map，留給後面的人配對。

**這就是 One-pass Hash Map 策略。**

---

## 4. 💻 Implementation (程式碼)

### approach 1: One-pass Hash Map

```cpp
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Key: 數字的值 (number)
        // Value: 該數字的索引 (index)
        unordered_map<int, int> numMap;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            // 檢查 complement 是否已經在 map 中
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }

            // 將當前數字加入 map
            numMap[nums[i]] = i;
        }

        return {}; // 題目保證有解，這裡理論上跑不到
    }
};
```

### Python Reference

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 使用 unordered_map 達成 O(1) 查找
        // map<int, int> 雖然也可以，但它是 O(log n)，面試時 unordered_map 通常更好
        unordered_map<int, int> prevMap;

        for (int i = 0; i < nums.size(); i++) {
            int currentNum = nums[i];
            int needed = target - currentNum;

            // map.find() 回傳 iterator。如果不等於 end() 代表找到了。
            // 使用 find 比 count 好，因為我們需要那個 iterator 來取 value (index)。
            if (prevMap.find(needed) != prevMap.end()) {
                // 注意順序：先放原本在 map 裡的 (較小的 index)，再放現在的 (較大的 index)
                // 雖然題目沒要求順序，但這樣比較直觀
                return {prevMap[needed], i};
            }

            // 把當前數字存起來：Value maps to Index
            prevMap[currentNum] = i;
        }

        return {};
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

### Hash Map Approach
-   **Time Complexity**: $O(n)$
    -   我們只需遍歷陣列一次。每次 Hash Map 的查找與插入平均是 $O(1)$。
-   **Space Complexity**: $O(n)$
    -   Hash Map 最多儲存 `n` 個元素。

### Brute Force Approach
-   **Time Complexity**: $O(n^2)$
-   **Space Complexity**: $O(1)$

**Trade-off**:
我們用了 $O(n)$ 的空間，換取了從 $O(n^2)$ 到 $O(n)$ 的時間進步。這在現代軟體開發中通常是非常划算的交易。
