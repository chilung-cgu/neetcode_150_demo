# Contains Duplicate (存在重複元素) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #217** — [題目連結](https://leetcode.com/problems/contains-duplicate/) | [NeetCode 解說](https://neetcode.io/problems/contains-duplicate)


## 1. 🧐 Problem Dissection (釐清問題)

作為面試者，在直接跳進程式碼之前，我們應該先與面試官確認題目的邊界條件。這展現了你的細心與對系統穩定性的考量。

- **Input Constraints**: 陣列長度範圍？(`1 <= nums.length <= 10^5`) 數值範圍？(`-10^9 <= nums[i] <= 10^9`)
  - _思考_：這意味著 $O(n^2)$ 的暴力解必定會 TLE (Time Limit Exceeded)，我們需要 $O(n)$ 或 $O(n \log n)$ 的解法。
- **Empty/Single Element**: 雖然題目說至少有一個元素，但確認一下總是好的。如果在只有一個元素的情況下，是否永遠回傳 `false`？
- **Memory Constraints**: 我們有多少記憶體可用？如果在嵌入式系統 (Embedded Systems) 中，記憶體受限，我們可能需要犧牲時間換空間。

**自問自答 (Mock Interview Question)**:

> "請問我們可以修改傳入的 Input Array 嗎？"
> (如果可以，Sort 解法會更有吸引力，因為可以達到 $O(1)$ Space。)

---

## 2. 🐢 Brute Force Approach (暴力解)

直觀的做法是拿每一個數字跟其他所有數字比對。

```cpp
bool containsDuplicate(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] == nums[j]) return true;
        }
    }
    return false;
}
```

- **Time Complexity**: $O(n^2)$。對於 $10^5$ 的數據量，$n^2 = 10^{10}$，這遠遠超過一般 OJ (Online Judge) 的 1秒限制 ($10^8$ operations)。
- **Space Complexity**: $O(1)$。
- **結論**: 這是一個好的起點，但顯然無法通過面試。

---

## 3. 💡 The "Aha!" Moment (優化)

如何加速搜尋？
在 Brute Force 中，我們為了找 `nums[i]` 是否已出現過，重複掃描了後面的陣列。這讓我們想到了 **Lookup Table** 的概念。

**思路引導 (Socratic Method)**:

1.  **Sorting**: 如果陣列是排序好的，重複的元素會在哪裡？
    - _答案_：相鄰。
    - _代價_：Sorting 需要 $O(n \log n)$。這比 $O(n^2)$ 好很多。
    - _優點_：Space Complexity 是 $O(1)$ (視 algo 而定)，適合記憶體極度受限的 Embedded 環境。

2.  **Hash Set**: 我們真的需要排序嗎？我們只想知道「這個數字之前有沒有看過」。
    - _資料結構_：Hash Set (在 C++ 中是 `std::unordered_set`) 提供平均 $O(1)$ 的查詢與插入。
    - _代價_：需要 $O(n)$ 的額外記憶體。
    - _優點_：Time Complexity 降到 $O(n)$，這是理論上的最佳解。

**Decision**:
除非面試官特別強調記憶體限制 (Constraints)，否則 **Hash Set** 通常是預設的最佳解 (Time-Space Tradeoff)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../contains_duplicate_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../contains_duplicate_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

---

## 4. 💻 Implementation (程式碼)

### approach 1: Hash Set (Time Optimized)

這是標準的 LeetCode 解法。

```cpp
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // 使用 unordered_set 來記錄看過的數字
        // Reserve 空間可以避免 rehash，對於效能有一點點幫助 (Embedded 思維)
        unordered_set<int> seen;
        seen.reserve(nums.size());

        for (int num : nums) {
            // find() 平均是 O(1)
            if (seen.find(num) != seen.end()) {
                return true; // 找到重複了
            }
            seen.insert(num);
        }
        return false;
    }
};
```

### Approach 2: Sorting (Space Optimized)

如果在 Embedded System (如 ARM Cortex-M0)，記憶體非常珍貴，我們可能會選擇這個。

```cpp
#include <vector>
#include <algorithm> // std::sort

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // std::sort 平均是 O(n log n)
        sort(nums.begin(), nums.end());

        // 檢查相鄰元素
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }
        return false;
    }
};
```

### Python Reference (Logic Check)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return true
            hashset.add(n)
        return false
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

讓我們專注於 Hash Set 的實作細節，這更能展示 C++ 能力。

```cpp
class Solution {
public:
    // Pass by reference (vector<int>&) 避免 copy 整個陣列，這是基本的效能習慣。
    bool containsDuplicate(vector<int>& nums) {
        // unordered_set 基於 Hash Table 實作。
        // Space overhead 比 vector 大，但查找速度快。
        unordered_set<int> seen;

        // 優化：如果我們知道大概會有多少元素，reserve 可以減少 memory allocation 的次數。
        // 在大量數據下，這會顯著減少 runtime overhead。
        seen.reserve(nums.size());

        // Range-based for loop (C++11)，語法更乾淨。
        for (const int& num : nums) { // 使用 const reference 雖然對 int 沒差，但對複雜物件是好習慣

            // count() return 1 if found, 0 otherwise.
            // 也可以用 seen.find(num) != seen.end()，兩者在這種情境下等價。
            if (seen.count(num)) {
                return true;
            }

            // 將數字加入集合
            seen.insert(num);
        }

        // 跑完迴圈都沒找到重複，回傳 false
        return false;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

### Hash Set Approach

- **Time Complexity**: $O(n)$
  - 我們遍歷陣列一次。Hash Set 的 `insert` 和 `find` 操作平均是 $O(1)$。
  - Worst case (Hash collision 極多) 會退化到 $O(n^2)$，但在現代 Hash 實作與正常測試資料下極少發生。
- **Space Complexity**: $O(n)$
  - 最糟情況下，沒有重複元素，我們需要將所有 $n$ 個數字存入 Hash Set。

### Sorting Approach

- **Time Complexity**: $O(n \log n)$
  - 主要消耗在 Sorting。
- **Space Complexity**: $O(1)$ (或是 $O(\log n)$ 取決於 sort 實作的 stack depth)
  - 如果不計算 Input Array 本身，我們只用了常數空間來做 iterator。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果陣列已排序怎麼辦？
- 如果只能用 O(1) 空間怎麼辦？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 忘記處理空陣列
- ⚠️ 使用 O(n²) 暴力解但未說明可優化

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 主動提到 Hash collision 最壞情況
- 💎 討論 Set vs Map 的選擇

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Valid Anagram (有效的易位構詞)](02_Valid_Anagram.md)
- [Longest Consecutive Sequence (最長連續序列)](09_Longest_Consecutive_Sequence.md)
