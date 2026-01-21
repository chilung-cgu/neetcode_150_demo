# Best Time to Buy and Sell Stock (買賣股票的最佳時機) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #121** — [題目連結](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [NeetCode 解說](https://neetcode.io/problems/best-time-to-buy-and-sell-stock)


## 1. 🧐 Problem Dissection (釐清問題)

題目給我們一個陣列 `prices`，其中 `prices[i]` 代表第 `i` 天的股價。
我們只能選擇 **某一天** 買入，並在 **未來的某一天** 賣出。
請問我們最多能賺多少錢？
如果賺不到錢 (例如股價一路跌)，回傳 0。

- **Input**: `[7,1,5,3,6,4]`
- **Output**: `5` (Day 2 buy at 1, Day 5 sell at 6).
- **Wrong Example**: Buy at 1, Sell at 7? 不行，因為 7 在 1 之前 (時光不能倒流)。
- **Constraints**:
  - $1 <= prices.length <= 10^5$。
  - 只做一次交易 (One transaction)。

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一天 `i` (買入日)，我們去檢查它之後的每一天 `j` (賣出日)。
`Profit = prices[j] - prices[i]`。
找出所有組合中的最大值。

- **Time Complexity**: $O(n^2)$。
- **Result**: TLE。

---

## 3. 💡 The "Aha!" Moment (優化)

這題其實是一個 **Dynamic Sliding Window** (或者說是 greedy 狀態維護) 的問題。

想像我們正沿著時間線走。
當我們站在第 `i` 天時，如果要「今天賣出並獲利最大」，那我們需要在什麼時候買入？
答案是：**在過去 (`0` 到 `i-1`) 的最低點買入**。

所以我們只需要維護一個變數 `minPrice`，代表「過去最低的股價」。
然後對於每一天：

1.  計算 `todayProfit = currentPrice - minPrice`。
2.  更新 `maxProfit`。
3.  如果 `currentPrice < minPrice`，更新 `minPrice`。

這就是 $O(n)$ 一次遍歷。

**Why Sliding Window?**
這也可以看作是一個與「最高利潤」相關的窗口：
`Left` = 最低買點。
`Right` = 當前賣點。
如果 `prices[Right] < prices[Left]`，說明我們找到了一個更低的買點，直接把 `Left` 跳去 `Right` (重置窗口起點)。(因為更低的買點意味著未來潛在利潤更高)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../buy_sell_stock_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../buy_sell_stock_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Linear Scan (One Pass)

```cpp
#include <vector>
#include <algorithm>
#include <climits> // for INT_MAX

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            // 隨時更新歷史最低價
            if (price < minPrice) {
                minPrice = price;
            }
            // 如果沒破底，就算算看如果今天賣能賺多少，並更新最大利潤
            else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }

        return maxProfit;
    }
};
```

### Python Reference

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l=buy, r=sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # 發現更低的買點，直接跳過去
            r += 1

        return maxP
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 設定 minPrice 為最大整數，確保第一個價格一定會成為新的 minPrice
        int minPrice = INT_MAX;
        int maxP = 0;

        // 遍歷每一天的股價
        for (const int& p : prices) {
            // Step 1: 試圖更新最低買入點
            // 如果遇到比以前看過都還低的價格，那這絕對是新的「最佳買點候選人」
            // (雖然這可能發生在最後一天，導致無法賣出，但邏輯上更新它沒壞處)
            if (p < minPrice) {
                minPrice = p;
            }
            // Step 2: 如果今天價格比較高，嘗試計算利潤
            else {
                // 如果今天賣出的利潤比之前紀錄的還高，更新 maxP
                int currentProfit = p - minPrice;
                if (currentProfit > maxP) {
                    maxP = currentProfit;
                }
            }
        }

        return maxP;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - 只需要遍歷一次陣列。
- **Space Complexity**: $O(1)$
  - 只使用兩個變數 `minPrice` 和 `maxP`。

**延伸思考**:
這題是 "Kadane's Algorithm" (Maximum Subarray) 的一種變形。
如果我們把陣列轉換成 `diff` array (每日漲跌幅)，那這題就變成了「找出最大連續子陣列和」。
`prices = [1, 7, 4]` -> `diff = [6, -3]`.
`max sub = 6`。
但直接維護 `minPrice` 更直觀。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果可以多次買賣？
- 如果有交易手續費？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 嘗試 O(n²) 暴力解
- ⚠️ 沒有維護最小價格

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 一趟遍歷 O(n)
- 💎 解釋 Kadane 變形的概念

---

## 📚 Related Problems (相關題目)

### 站內相關

### 進階挑戰
- [Best Time To Buy And Sell Stock Ii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) — LeetCode
