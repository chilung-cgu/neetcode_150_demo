# Car Fleet (車隊) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目給我們終點 `target`，和兩個陣列 `position` 與 `speed`。
有 `n` 輛車在單行道上往 `target` 前進。

-   **No Overtaking**: 車子不能超車。如果後車追上前車，它必須減速，以跟前車一樣的速度行駛（形成一個 Fleet）。
-   **Fleet**: 只要兩輛車連在一起（位置相同，速度相同），就算一個 Fleet。一輛車自己也算一個 Fleet。
-   請問最後會有多少個 Fleet 到達終點？

-   **Input**: `target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]`
-   **Output**: `3`
    -   10 (spd 2) -> 需要 1s 到達。
    -   8 (spd 4) -> 需要 1s 到達。這兩量會撞在一起 (變成一個 fleet)。
    -   5 (spd 1) -> 需要 7s 到達。
    -   3 (spd 3) -> 需要 3s 到達。這會追上 5，變成一個 fleet (at 12)。
    -   0 (spd 1) -> 需要 12s 到達。
    -   Total: `[10,8]`, `[5,3]`, `[0]` -> 3 fleets.

---

## 2. 🐢 Brute Force Approach (暴力解)

模擬每一秒車子的移動，檢查 collision。

-   **Time**: 取決於 target 大小，若是 100 miles with 0.1 speed... 太慢。
-   重點不是模擬過程，而是「誰被誰擋住」。

---

## 3. 💡 The "Aha!" Moment (優化)

這題的核心在於 **到達終點所需的時間 (Time to Target)**。

`time = (target - position) / speed`

關鍵邏輯：

1.  **由後往前看 (Reverse Sort by Position)**：
    -   我們應該先看「離終點最近」的車子。為什麼？
    -   因為前面的車子永遠不會追上後面的車子（因為它已經在前面了）。
    -   只有**後面的車子**會追上**前面的車子**。
    -   所以，前面的車子是「路障」。

2.  **Monotonic Stack** (Conceptual)：
    -   假如車子 A 在車子 B 前面 (pos A > pos B)。
    -   如果 `time A < time B`：A 比較快到達。B 追不上 A。B 自己是一個 Fleet。
    -   如果 `time A >= time B`：B 比較快（或一樣），B 會追上 A。但因為不能超車，B 只能減速陪 A 走。所以 B 與 A 合併，所需時間變成 `time A`。B 不再是獨立的 Fleet。

**演算法**：

1.  將車子配對 `(position, speed)`。
2.  根據 `position` **降冪排序** (從離終點最近的開始看)。
3.  遍歷排序後的車子，計算 `time`。
4.  維護一個 Stack。
    -   如果 Stack 空，Push `time`。
    -   如果 `current_time > stack.top()`，代表這台車比前車慢，追不上，自己形成一個新 Fleet。Push `current_time`。
    -   如果 `current_time <= stack.top()`，代表這台車比前車快，會追上。合併進前車的 Fleet。此時 **不需要 Push** (因为它消失了，或者說它被併入了前車，而前車的時間還是瓶頸)。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../car_fleet_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../car_fleet_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Sorting + Linear Scan

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, double>> cars;

        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], (double)(target - position[i]) / speed[i]});
        }

        // 按照位置從大到小排序 (從終點往回看)
        sort(cars.rbegin(), cars.rend());

        int fleets = 0;
        double maxTime = 0.0; // 記錄當前 Fleet 中最慢的那台車的時間（也就是瓶頸時間）

        for (int i = 0; i < n; i++) {
            double currentTime = cars[i].second;

            // 如果這台車所需時間比前面的瓶頸時間還長
            // 代表它來不及追上前面的車隊，它自己會成為一個新的車隊（並且可能擋住後面的人）
            if (currentTime > maxTime) {
                maxTime = currentTime;
                fleets++;
            }
            // 如果 currentTime <= maxTime，代表它會追上前面的車，所以被合併，fleets 不變
        }

        return fleets;
    }
};
```

### Python Reference

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        # Sort by position (reverse) isn't strictly necessary if we pop from end,
        # but sorting normally and iterating reverse is cleaner.
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        // 儲存 Pair: {位置, 到達時間}
        // 注意時間要是 double，不然整數除法會丟失精度
        vector<pair<int, double>> cars;

        for (int i = 0; i < n; i++) {
            double time = (double)(target - position[i]) / speed[i];
            cars.push_back({position[i], time});
        }

        // 關鍵：將車子按照「位置」由大到小排序 (靠近終點的先處理)
        sort(cars.rbegin(), cars.rend());

        int fleetCount = 0;
        double prevEta = 0.0; // 前一台車(或前一個車隊)到達終點的時間

        for (const auto& car : cars) {
            double curEta = car.second;

            // 邏輯判斷：
            // 因為我們是從前車往後車看。
            // 1. 如果後車 (cur) 比前車 (prev) 快 (時間短, curEta <= prevEta)：
            //    後車會追上前車。因為不能超車，後車速度被迫降到跟前車一樣。
            //    所以後車「消失」併入前車 fleet。我們什麼都不用做 (也不用更新 prevEta)。

            // 2. 如果後車 (cur) 比前車 (prev) 慢 (時間長, curEta > prevEta)：
            //    後車永遠追不上前車。前車已經跑了。
            //    後車自己形成一個新的 fleet，並且成為更後面車子的新路障。
            if (curEta > prevEta) {
                fleetCount++;
                prevEta = curEta;
            }
        }

        return fleetCount;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n \log n)$
    -   排序是最耗時的操作。
    -   遍歷只需 $O(n)$。
-   **Space Complexity**: $O(n)$
    -   用來儲存 pairs。
