# Product of Array Except Self (除自身以外陣列的乘積) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #238** — [題目連結](https://leetcode.com/problems/product-of-array-except-self/) | [NeetCode 解說](https://neetcode.io/problems/product-of-array-except-self)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `nums`，回傳一個陣列 `answer`，其中 `answer[i]` 等於 `nums` 中除了 `nums[i]` 之外所有元素的乘積。

- **Input**: `[1,2,3,4]`
- **Output**: `[24,12,8,6]`
  - 24 = 2*3*4
  - 12 = 1*3*4
  - 8 = 1*2*4
  - 6 = 1*2*3
- **Constraints**:
  - 時間複雜度必須是 $O(n)$。
  - **不能使用除法 (Division)**。
  - **Follow-up**: 能否達到 $O(1)$ Space Complexity? (Output array 不算空間)

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一個 `i`，跑一遍陣列把其他數字乘起來。

- **Time Complexity**: $O(n^2)$。
- **Result**: Time Limit Exceeded (TLE)。題目要求 $O(n)$。

### Approach 1.5: Division (Not Allowed)

算出所有數字的總乘積 `P`，然後 `answer[i] = P / nums[i]`。

- **問題 1**: 題目 **禁止使用除法**。
- **問題 2**: 如果陣列中有 **0**，你會遇到 Divide by Zero (除以零) 的錯誤。即便處理 0，邏輯也會變得很複雜 (如果有兩個 0，結果全為 0；如果有一個 0，除了那個 0 的位置是其他數乘積，其他位置都是 0)。

---

## 3. 💡 The "Aha!" Moment (優化)

既然不能用除法，我們怎麼湊出「左邊所有人的乘積」x「右邊所有人的乘積」？

**Prefix & Suffix Product (前綴與後綴乘積)**

對於任意位置 `i`，我們想要的結果其實是：
`answer[i] = (nums[0]...nums[i-1]) * (nums[i+1]...nums[n-1])`
也就是：`Left Product * Right Product`

我們可以分兩次遍歷計算：

1.  **第一次遍歷 (Left -> Right)**:
    - 計算所有 `i` 左邊的乘積，存入 `answer[i]`。
    - `answer[i] = nums[0] * ... * nums[i-1]`
2.  **第二次遍歷 (Right -> Left)**:
    - 計算所有 `i` 右邊的乘積，並 **乘** 到 `answer[i]` 上。
    - 我們不需要一個額外的陣列來存 Right Product，只需要一個變數 `postfix` 隨路累積即可。

這樣我們就達成了 $O(n)$ Time 和 $O(1)$ Extra Space。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../product_of_array_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../product_of_array_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Prefix & Postfix (Optimal)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);

        // Pass 1: 計算 Prefix Product (左邊的乘積)
        // res[i] 會包含 nums[0] * ... * nums[i-1]
        res[0] = 1; // 第一個元素左邊沒有數字，設為 identity 1
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }

        // Pass 2: 計算 Postfix Product 並乘上去
        // postfix 變數代表 nums[i+1] * ... * nums[n-1]
        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postfix; // 原本的 prefix * 現在的 postfix
            postfix *= nums[i]; // 更新 postfix 給下一個 (更左邊的) 用
        }

        return res;
    }
};
```

### Python Reference

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: 初始化結果陣列 (Allocation)
        # [1] * N 會產生一個長度為 N 的 list，裡面填滿 1
        # C++: vector<int> res(nums.size(), 1);
        res = [1] * (len(nums))

        prefix = 1
        # Step 2: Prefix Pass (由左往右)
        # 目的：算出每個位置「左邊所有數字」的乘積
        for i in range(len(nums)):
            res[i] = prefix   # 將目前的 prefix 存入 res[i] (此時 res[i] 只有左邊的乘積)
            prefix *= nums[i] # 更新 prefix，把當前數字乘進去，給下一個位置用

        postfix = 1
        # Step 3: Postfix Pass (由右往左)
        # 目的：算出每個位置「右邊所有數字」的乘積，並直接乘上原本 res[i] 內的左邊乘積
        # range(start, stop, step): 從最後一個 index (len-1) 倒數到 0 (stop=-1 不包含)
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # 關鍵：res[i] = (左邊乘積) * (右邊乘積)
            postfix *= nums[i] # 更新 postfix，給前一個位置用

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        // 初始化結果陣列。
        // 題目說 Output array 不算在 Space Complexity 中。
        // 我們先用 res 來存 Prefix Product。
        vector<int> res(n, 1); // 這裡可以直接由 1 開始，也可以像上面那樣手動設

        // 第一遍：Prefix
        // res[i] = nums[0] * nums[1] * ... * nums[i-1]
        // 注意：我們用一個變數 prefix 來追蹤累積乘積
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            res[i] = prefix; // 把「當前位置左邊的所有乘積」存入
            prefix *= nums[i]; // 把自己乘進去，給下一個人用
        }

        // 現在 res[i] 只有左邊的乘積。
        // 第二遍：Postfix
        // 從右邊開始掃回來，補上右邊的乘積
        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postfix; // 左邊乘積 * 右邊乘積 = 答案
            postfix *= nums[i]; // 把自己乘進去，給下一個人(左邊那位)用
        }

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

### Time Complexity

- **$O(n)$**:
  - 第一個迴圈遍歷一次 (Prefix)。
  - 第二個迴圈遍歷一次 (Postfix)。
  - 總共 $2n \approx O(n)$。

### Space Complexity

- **$O(1)$** (Extra Space):
  - 題目定義 output array 不算額外空間。
  - 我們只使用了 `prefix`, `postfix`, `n`, `i` 幾個變數。
  - 因此 Space Complexity 是 $O(1)$。
  - (如果不算 Output 優化，我們理論上需要兩個陣列 `prefix[]` 和 `suffix[]`，那樣就是 $O(n)$)。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果有 0 怎麼辦？
- 能否處理整數溢位？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 使用除法（題目禁止）
- ⚠️ 沒有處理多個 0 的情況

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 一趟遍歷完成
- 💎 討論前綴積與後綴積的概念

---

## 📚 Related Problems (相關題目)

### 站內相關

### 進階挑戰
- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) — LeetCode
