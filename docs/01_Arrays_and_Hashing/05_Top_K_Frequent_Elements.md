# Top K Frequent Elements (前 K 個高頻元素) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #347** — [題目連結](https://leetcode.com/problems/top-k-frequent-elements/) | [NeetCode 解說](https://neetcode.io/problems/top-k-frequent-elements)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `nums` 和一個整數 `k`，要求回傳出現頻率最高的 `k` 個元素。

- **Input**: `nums = [1,1,1,2,2,3], k = 2`
- **Output**: `[1,2]`
- **Constraints**:
  - $k$ 在有效範圍內。
  - 題目要求時間複雜度 **優於** $O(n \log n)$。這是一個很大的提示！(這是否決 Sorting 解法的紅牌)。

---

## 2. 🐢 Brute Force Approach (暴力解)

1.  用 Hash Map 統計每個數字的頻率。
2.  將 Map 的內容轉成 `Pair<Number, Count>` 的列表。
3.  根據 Count 進行 Sorting (Descending)。
4.  取前 `k` 個。

- **Time Complexity**: $O(n \log n)$ (因為 Sorting)。
- **Result**: 雖然能解，但題目明確說要比這更快，所以這不是滿分答案。

---

## 3. 💡 The "Aha!" Moment (優化)

如何避開 $O(n \log n)$ 的全局排序？

**思路 1: Max Heap (Priority Queue)**

- 我們不需要對 _所有_ 元素排序，我們只需要前 `k` 個。
- 建立一個 Max Heap，把所有 `(Count, Number)` 丟進去。
- Pop `k` 次。
- **Cost**: Build Heap $O(N)$, Pop $k$ times $O(k \log n)$。總共 $O(N + k \log n)$。這比 Sort 好。

**思路 2: Bucket Sort (Linear Time)**

- 頻率的範圍是多少？一個數字最多出現 `n` 次 (陣列長度)。
- 我們可以建立一個陣列 `buckets`，大小為 `n + 1`。
- `buckets[i]` 存放「出現了 `i` 次的所有數字」。
- 例如：`nums = [1,1,1,2,2,3]`
  - 1 出現 3 次 -> `bucket[3].push(1)`
  - 2 出現 2 次 -> `bucket[2].push(2)`
  - 3 出現 1 次 -> `bucket[1].push(3)`
- 最後從 `bucket[n]` 往回走到 `bucket[1]`，收集 `k` 個數字。

**Decision**:
Bucket Sort 是 $O(n)$，這是真正的最佳解。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../top_k_frequent_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../top_k_frequent_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

---

## 4. 💻 Implementation (程式碼)

### Approach 1: Bucket Sort (O(n) - Best)

```cpp
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 1. Count frequencies
        unordered_map<int, int> countMap;
        for (int n : nums) {
            countMap[n]++;
        }

        // 2. Create buckets
        // Index i 代表出現頻率，Value 是出現 i 次的數字列表
        // 大小為 n + 1 因為頻率最大可能是 nums.size()
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& pair : countMap) {
            buckets[pair.second].push_back(pair.first);
        }

        // 3. Gather top k
        vector<int> result;
        // 從最高頻率往回找
        for (int i = buckets.size() - 1; i >= 0; i--) {
            if (buckets[i].empty()) continue;

            for (int n : buckets[i]) {
                result.push_back(n);
                if (result.size() == k) return result;
            }
        }

        return result;
    }
};
```

### Approach 2: Min Heap (O(n log k))

維護一個大小只有 `k` 的 Min Heap。如果新元素的頻率比 Heap Top 大，就 Pop Top 並 Push 新元素。這樣 Heap 裡永遠保留最大的 `k` 個。

```cpp
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> countMap;
        for (int n : nums) countMap[n]++;

        // Min Heap: pair<freq, num>
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        for (auto& pair : countMap) {
            pq.push({pair.second, pair.first});
            if (pq.size() > k) {
                pq.pop(); // 移除最小頻率的，保留大的
            }
        }

        vector<int> result;
        while (!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};
```

### Python Reference (Bucket Sort)

```python
class Solution:
    # Python 的型別提示 (Type Hint) 類似 C++ 的函數簽名，但僅供 IDE 參考，執行時不會強制檢查
    # List[int] 等同於 std::vector<int>
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1. 建立 Hash Map (C++: unordered_map<int, int>)
        count = {}

        # 2. 建立 Buckets (二維陣列)
        # 語法：List Comprehension (列表推導式)
        # 邏輯：生成 len(nums) + 1 個獨立的空 list
        # C++ 對照：vector<vector<int>> freq(nums.size() + 1);
        # 注意：不能寫 [[]] * N，那會導致所有 bucket 指向同一個記憶體位址 (Shallow Copy)
        freq = [[] for i in range(len(nums) + 1)]

        # 3. 統計頻率
        for n in nums:
            # .get(n, 0): 嘗試取值，若 key 不存在則回傳預設值 0
            # Python 的 dict[key] 若不存在會 crash，不像 C++ map[key] 會自動初始化為 0
            count[n] = count.get(n, 0) + 1

        # 4. 填入 Buckets
        # .items() 回傳 (key, value) 的 tuple 列表
        # n, c 對應 key, value (類似 C++17 的 Structured Binding: for (auto [n, c] : count))
        for n, c in count.items():
            freq[c].append(n) # append 等同於 push_back

        res = []

        # 5. 反向遍歷 Buckets 收集結果
        # range(start, stop, step) 是「左閉右開」區間 [start, stop)
        # start: len(freq) - 1 (最後一個 index，最高頻率)
        # stop: 0 (因為不包含 0，所以迴圈會執行到 index 1 結束)
        # step: -1 (每次遞減)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們來看 Bucket Sort 的 C++ 細節。

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: 建立 Hash Map 統計頻率
        // Space: O(N) 用於儲存 distinct elements
        unordered_map<int, int> counts;
        for (int n : nums) {
            counts[n]++;
        }

        // Step 2: 建立 Buckets
        // buckets[i] 是一個 list，存放所有出現次數為 i 的數字
        // 最大出現次數就是 nums.size() (全部都是同一個字時)
        // Space: O(N)
        vector<vector<int>> buckets(nums.size() + 1);

        for (auto const& [num, count] : counts) {
            buckets[count].push_back(num);
        }

        // Step 3: 從後往前遍歷 Buckets
        vector<int> result;
        // 小技巧：reserve k 可以稍微優化 performance
        result.reserve(k);

        for (int i = buckets.size() - 1; i > 0; i--) {
            // 如果這個頻率沒有數字，直接跳過
            if (buckets[i].empty()) continue;

            // 將這個頻率桶裡的所有數字加入結果
            for (int n : buckets[i]) {
                result.push_back(n);
                // 一旦收集滿 k 個，立刻回傳
                if (result.size() == k) {
                    return result;
                }
            }
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

### Bucket Sort

- **Time Complexity**: $O(n)$
  - 統計頻率：$O(n)$
  - 放入 Buckets：$O(n)$ (遍歷 map)
  - 讀取 Buckets：$O(n)$ (最差情況下 bucket 是空的，但我們還是要 iterate index。所有的數字加起來總數是 distinct elements，也小於 $n$)
  - 總合：$O(n)$ (Linear Time)
- **Space Complexity**: $O(n)$
  - Hash Map + Buckets 陣列。

### Min Heap Approach

- **Time Complexity**: $O(n \log k)$
  - 遍歷 Map (size $m \le n$)，每次 push/pop heap 是 $\log k$。
  - 所以是 $O(n \log k)$。當 $k$ 接近 $n$ 時，退化成 $O(n \log n)$。
- **Space Complexity**: $O(n)$ (Map) + $O(k)$ (Heap)。

**結論**: Bucket Sort 是理論最優解，展現了對數據特性的深刻理解 (頻率是有上限的)。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果 K 非常大怎麼辦？
- 能否做到 O(n) 時間？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有處理 K > unique elements 的情況
- ⚠️ 使用全排序導致效率低

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 知道 Bucket Sort 解法
- 💎 討論 Heap vs QuickSelect
