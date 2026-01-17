# Min Stack (最小堆疊)

## 1. 🧐 Problem Dissection (釐清問題)

題目要求設計一個 Stack，除了支援標準的 `push`, `pop`, `top` 之外，還額外支援 `getMin()`。
**Constraints**:

-   所有操作都必須是 **$O(1)$** Time Complexity。
-   $O(1)$ `getMin` 是最難的部分。如果遍歷 Stack 找最小值，那是 $O(n)$。

-   **Input**:
    -   `MinStack()`
    -   `push(-2)`
    -   `push(0)`
    -   `push(-3)`
    -   `getMin()` -> Returns -3
    -   `pop()` -> Removes -3
    -   `top()` -> Returns 0
    -   `getMin()` -> Returns -2

---

## 2. 🐢 Brute Force Approach (暴力解)

只需實現標準 Stack。`getMin()` 每次都遍歷 vector 找最小。

-   `getMin()`: $O(n)$。
-   其他: $O(1)$。
-   **Result**: 雖然功能正確，但不符合题目要求的 $O(1)$。

---

## 3. 💡 The "Aha!" Moment (優化)

我們需要在 push 每個元素的同時，**記住「當這個元素是 Top 時，目前的最小值是誰」**。

我們可以維護 **兩個 Stack**：

1.  **Main Stack (`s`)**: 存所有的數據。
2.  **Min Stack (`min_s`)**: 存「對應高度」時的最小值。

**邏輯**：

-   **Push(val)**:
    -   `s.push(val)`
    -   `min_s.push( min(val, min_s.top()) )`。
    -   這樣 `min_s.top()` 永遠就是當前的全局最小值。
-   **Pop()**:
    -   `s.pop()`
    -   `min_s.pop()`。因為這個元素被移除了，當前的最小值可能會變回之前的狀態。
-   **GetMin()**:
    -   `return min_s.top()`。

**Example**:
Push -2: `s: [-2]`, `min_s: [-2]`
Push 0:  `s: [-2, 0]`, `min_s: [-2, -2]` (因為 0 > -2，min 還是 -2)
Push -3: `s: [-2, 0, -3]`, `min_s: [-2, -2, -3]` (因為 -3 < -2，新 min 是 -3)

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../min_stack_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../min_stack_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Two Stacks

```cpp
#include <stack>
#include <algorithm> // for min

using namespace std;

class MinStack {
private:
    stack<int> s;
    stack<int> min_s;

public:
    MinStack() {

    }

    void push(int val) {
        s.push(val);
        // 如果 min_s 為空，或者 val 比當前最小值還小，push val
        // 否則，重複 push 當前的最小值 (保持同步)
        if (min_s.empty() || val < min_s.top()) {
            min_s.push(val);
        } else {
            min_s.push(min_s.top());
        }
    }

    void pop() {
        s.pop();
        min_s.pop();
    }

    int top() {
        return s.top();
    }

    int getMin() {
        return min_s.top();
    }
};
```

### Approach: Optimized Two Stacks (Save Space)

我們可以只在 `val <= min_s.top()` 時才 Push 進 `min_s`。
Pop 時，只有當 `s.top() == min_s.top()` 時才 Pop `min_s`。
這樣可以省一點空間，但如果有大量重複最小值，效果有限。
面試時寫第一種 (同步 Stack) 最不容易錯，且 Time Complexity 一樣。

### Approach: One Stack (Pair)

每個元素存 `pair<val, current_min>`。
```cpp
stack<pair<int, int>> s;
// push: s.push({val, min(val, s.top().second)})
```

### Python Reference

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class MinStack {
private:
    // 一般堆疊，存實際數據
    stack<int> stk;
    // 最小堆疊，存「當下」的最小值
    stack<int> minStk;

public:
    MinStack() {
        // Constructor, std::stack 自動初始化为空
    }

    void push(int val) {
        stk.push(val);

        // 決定 minStk 要存什麼
        if (minStk.empty()) {
            minStk.push(val);
        } else {
            // 取 val 與當前最小值 (minStk.top()) 的較小者
            // 這樣 minStk 的頂端永遠代表整個 stk 的最小值
            minStk.push(std::min(val, minStk.top()));
        }
    }

    void pop() {
        // 兩個一起 pop，保持高度一致
        stk.pop();
        minStk.pop();
    }

    int top() {
        return stk.top();
    }

    int getMin() {
        // O(1) 取得最小值
        return minStk.top();
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(1)$ for all operations.
    -   我們只用了基本的 stack operations (push/pop/top) 和 min comparison，這些都是常數時間。
-   **Space Complexity**: $O(n)$
    -   我們用了兩個 stack，總共存儲 $2n$ 個元素。依然是線性空間。
