# Trapping Rain Water (接雨水) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 array `height` 代表地形高度，每個寬度為 1。請問下雨後這個地形能接住多少水？

- **Input**: `[0,1,0,2,1,0,1,3,2,1,2,1]`
- **Output**: `6`
- **Core Concept**: 水能存多高，取決於該位置 **左邊最高的牆** 和 **右邊最高的牆** 中较矮的那一个，扣掉当前地板高度。
  - `Water[i] = max(0, min(LeftMax[i], RightMax[i]) - height[i])`

---

## 2. 🐢 Brute Force Approach (暴力解)

對每一個位置 `i`，我往左跑一遍找 `MaxL`，往右跑一遍找 `MaxR`。

- `Water[i] = min(MaxL, MaxR) - height[i]`
- **Time**: $O(n^2)$。對每個點都掃描兩邊。
- **Space**: $O(1)$。

---

## 3. 💡 The "Aha!" Moment (優化)

我們先優化 Brute Force 的重複計算。
我們可以預先計算兩個陣列：

- `leftMax[i]`：位置 `i` 左邊(含自己)最高的牆。
- `rightMax[i]`：位置 `i` 右邊(含自己)最高的牆。
  這叫做 **Dynamic Programming** thinking。

- **Time**: $O(n)$。 (3 passes)
- **Space**: $O(n)$。 (存兩個陣列)

**能否優化到 $O(1)$ Space (Two Pointers)?**

想像我們有 `Left` 和 `Right` 兩個指標，以及 `LeftMax` 和 `RightMax` 變數。

- 如果 `LeftMax < RightMax`：
  - 這意味著對於左邊的指針 `Left` 來說，瓶頸 **一定** 在左邊 (`LeftMax`)。
  - 為什麼？因為雖然右邊目前只看到 `RightMax`，但真正的右邊界可能更高 (在未掃描區域)，但絕對不會比 `RightMax` 矮。
  - 既然瓶頸已確定是 `LeftMax`，我們就可以直接計算 `Left` 位置的水量：`LeftMax - height[Left]`。
  - 移動 `Left`。
- 反之亦然：如果 `LeftMax >= RightMax`，瓶頸由右邊決定，計算 `Right` 位置的水量，移動 `Right`。

這就是 **Two Pointers** 的精隨：不需要知道對面確切多高，只要知道「對面比我高」，我的瓶頸就由我自己這邊決定。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../trapping_rain_water_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../trapping_rain_water_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Two Pointers (O(n) Time, O(1) Space)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) return 0;

        int left = 0;
        int right = height.size() - 1;

        int leftMax = height[left];
        int rightMax = height[right];

        int res = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                leftMax = max(leftMax, height[left]);
                res += leftMax - height[left];
            } else {
                right--;
                rightMax = max(rightMax, height[right]);
                res += rightMax - height[right];
            }
        }

        return res;
    }
};
```

### Python Reference

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        // 邊界檢查
        if (height.empty()) return 0;

        int l = 0;
        int r = height.size() - 1;

        // 記錄目前的左邊最高與右邊最高
        int leftMax = height[l];
        int rightMax = height[r];

        int water = 0;

        while (l < r) {
            // 關鍵判斷：哪邊是短板？
            // 如果 leftMax 比較小，那 index 'l' 能接多少水，完全取決於 leftMax。
            // 因為右邊至少有個 rightMax 擋著 (甚至更高)，所以水不會從右邊流掉，只會受限於左邊。
            if (leftMax < rightMax) {
                l++; // 移動到下一個位置

                // 更新 Left Max
                leftMax = max(leftMax, height[l]);

                // 計算水量。
                // 如果 height[l] 比 leftMax 小，就能裝水。
                // 如果 height[l] 就是新的 leftMax，那相減為 0，裝不了水。
                water += leftMax - height[l];

            } else {
                // 同理，如果 rightMax 比較小 (或相等)，瓶頸在右邊
                r--;
                rightMax = max(rightMax, height[r]);
                water += rightMax - height[r];
            }
        }

        return water;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - 每個位置只被訪問一次。
- **Space Complexity**: $O(1)$
  - 只用了常數變數。
  - 相較於 DP 解法 ($O(n)$ Space) 或 Stack 解法 ($O(n)$ Space)，這是最優解。
  - 這題在面試中如果能直接寫出 $O(1)$ Space，是 Strong Hire 的訊號。
