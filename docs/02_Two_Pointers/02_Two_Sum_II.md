# Two Sum II - Input Array Is Sorted (兩數之和 II - 輸入已排序)

## 1. 🧐 Problem Dissection (釐清問題)

這題是 "Two Sum" 的變種。
題目給一個 **已排序 (Sorted in non-decreasing order)** 的整數陣列 `numbers`，要找出兩個數字相加等於 `target`。
回傳這兩個數字的 **1-based index**。

-   **Input**: `numbers = [2,7,11,15], target = 9`
-   **Output**: `[1,2]` (解釋: 2 + 7 = 9)
-   **Constraints**:
    -   **$O(1)$ Extra Space**: 這是最關鍵的限制。這意味著我們 **不能使用 Hash Map**。
    -   只有唯一解。
    -   不可以重複使用同一個元素。
    -   $2 <= numbers.length <= 3 * 10^4$。

---

## 2. 🐢 Brute Force Approach (暴力解)

和一般 Two Sum 一樣，雙層迴圈。

-   `for i in 0..n`: `for j in i+1..n`: check sum.
-   **Time**: $O(n^2)$。
-   **Space**: $O(1)$。
-   **Result**: TLE。沒有利用到「已排序」這個性質。

---

## 3. 💡 The "Aha!" Moment (優化)

既然陣列是 **已排序** 的，我們可以利用這個性質來快速縮小搜尋範圍。

想像我們有兩個指標：

-   `Left` 指向最小的數 (開頭)。
-   `Right` 指向最大的數 (結尾)。

計算 `Sum = numbers[Left] + numbers[Right]`。

1.  如果 `Sum > Target`：
    -   我們需要讓總和 **變小**。
    -   `Left` 已經是最小了，動它只會變大。
    -   所以我們只能移動 `Right` (往左移，找次大的數)。
2.  如果 `Sum < Target`：
    -   我們需要讓總和 **變大**。
    -   `Right` 已經是最大了，動它只會變小。
    -   所以我們只能移動 `Left` (往右移，找次小的數)。
3.  如果 `Sum == Target`：
    -   找到了！

這就是標準的 **Two Pointers** 策略。

-   **為什麼這是對的？**
    -   每一次移動，我們都排除了一個「絕對不可能」的行或列 (如果我们把這想成一個 Matrix 搜尋)。
    -   這個邏輯保證我們不會錯過任何可能的組合。

---

## 4. 💻 Implementation (程式碼)

### Approach: Two Pointers

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right) {
            int currentSum = numbers[left] + numbers[right];

            if (currentSum > target) {
                // 總和太大，需要更小的數字 -> 右指標左移
                right--;
            } else if (currentSum < target) {
                // 總和太小，需要更大的數字 -> 左指標右移
                left++;
            } else {
                // 找到了！题目要求 1-based index
                return {left + 1, right + 1};
            }
        }

        return {}; // 理論上不會執行到這
    }
};
```

### Python Reference

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // 初始化雙指標
        int low = 0;
        int high = numbers.size() - 1;

        while (low < high) {
            // 注意：雖然題目 constraints 說數字範圍還好，
            // 但如果數字很大，相加可能會 Integer Overflow。
            // 這裡題目 constraints: -1000 <= numbers[i] <= 1000
            // 以及 target -1000 <= target <= 1000
            // 等等，LeetCode 最新 Constraints 其實是 -1000 <= numbers[i] <= 1000 (X)
            // 實際 Constraints 可能是 -10^9 到 10^9，相加可能導致 overflow。
            // 使用 long long 更保險 (如果是 C++，int 通常是 32-bit，範圍 2*10^9，勉強夠，但 long long 更好)
            // 不過此題 return 還是 int，我們先用 int。
            int sum = numbers[low] + numbers[high];

            if (sum == target) {
                return {low + 1, high + 1}; // 1-based index
            } else if (sum < target) {
                // sum 太小，我們需要大一點的值
                // 因為是 Sorted Array，只有移動 low 往右才能變大
                low++;
            } else {
                // sum 太大，我們需要小一點的值
                // 只有移動 high 往左才能變小
                high--;
            }
        }

        return {-1, -1};
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   `left` 只會 `++`，`right` 只會 `--`。
    -   在最糟情況下，兩個指標相遇，總共移動了 $n$ 步。
-   **Space Complexity**: $O(1)$
    -   只有 `left`, `right`, `sum` 幾個變數。沒有使用 Hash Map。

**Comparison w/ Two Sum I**:

-   Two Sum I: $O(n)$ Time, $O(n)$ Space (Hash Map).
-   Two Sum II: $O(n)$ Time, $O(1)$ Space (Two Pointers).
-   **關鍵差異**: II 的 Input 是 **Sorted** 的，這讓我們可以用空間換取了... 呃，其實這題同時省了空間跟時間常數，因為 Two Pointers 比 Hash Map 操作更快。
