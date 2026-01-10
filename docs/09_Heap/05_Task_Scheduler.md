# Task Scheduler (任務調度器)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字元陣列 `tasks`，每個字元代表一種任務。
你需要安排這些任務的執行順序。
-   每個任務執行耗時 1 單位時間。
-   相同種類的任務之間必須有至少 `n` 單位時間的冷卻時間 (Interval)。
-   在此期間，CPU 可以執行其他不同的任務，或者 **Idle (待命)**。

計算完成所有任務所需的 **最少時間**。

-   **Input**: `tasks = ["A","A","A","B","B","B"], n = 2`
-   **Output**: 8
    -   A -> B -> idle -> A -> B -> idle -> A -> B
-   **Input**: `tasks = ["A","A","A","B","B","B"], n = 0`
-   **Output**: 6 (A->B->A->B->A->B)
-   **Constraints**:
    -   $1 <= tasks.length <= 10^4$
    -   `tasks[i]` is upper-case English letter.
    -   $0 <= n <= 100$

---

## 2. 🐢 Brute Force Approach (暴力解)

模擬 CPU 排程。
使用優先佇列 (Priority Queue) 存放任務頻率。
每次從 PQ 拿出 `n+1` 個頻率最高的任務來填滿「一輪」週期。
如果不夠 `n+1` 個，就填 Idle。
-   Simulation works, but complex to implement cleanly.

---

## 3. 💡 The "Aha!" Moment (優化)

不需要真正模擬，可以用 **數學/鴿籠原理** 計算。

關鍵在於 **頻率最高** 的任務。假設頻率最高的任務是 A，出現 `maxFreq` 次 (例如 3 次)。
我們必須把這 3 個 A 排開，中間隔 `n` 個空格：
`A _ _ A _ _ A`

1.  **框架大小**: 我們至少需要 `(maxFreq - 1)` 個大小為 `(n + 1)` 的塊。
    -   前面的 A 佔據了 `maxFreq - 1` 組。
    -   最後一個 A 不一定要後面跟著 Idle。
    -   Base Length = `(maxFreq - 1) * (n + 1)`

2.  **填補最後一塊**:
    -   最後一組只有那些「頻率等於 maxFreq」的任務會留下來。
    -   如果有 k 個任務頻率都是 maxFreq，最後一塊長度就是 k。
    -   Total Length = `(maxFreq - 1) * (n + 1) + k`

3.  **例外**:
    -   如果在填滿框架後，還有剩下的「低頻」任務插不進去（雖然其實空格很多，理論上一定插得進去）。
    -   更準確地說：如果任務非常多，多到填滿所有空格還不夠放，這時候因為沒有 Idle 了，CPU 一直在工作，所以總時間就是 `tasks.length`。

結論：**Result = max(tasks.length, calculated_slot_size)**

---

## 4. 💻 Implementation (程式碼)

### Approach: Math / Greedy

```cpp
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // Count frequencies
        unordered_map<char, int> counts;
        int maxFreq = 0;
        for (char t : tasks) {
            counts[t]++;
            maxFreq = max(maxFreq, counts[t]);
        }
        
        // Count how many tasks have the max frequency
        int maxFreqTasksCount = 0;
        for (auto& pair : counts) {
            if (pair.second == maxFreq) {
                maxFreqTasksCount++;
            }
        }
        
        // Calculate the minimum length based on maxFreq
        // (maxFreq - 1) groups of size (n + 1), plus the last chunk
        long result = (long)(maxFreq - 1) * (n + 1) + maxFreqTasksCount;
        
        // The answer cannot be less than the total number of tasks
        return max((int)result, (int)tasks.size());
    }
};
```

### Approach: Simulation with Max-Heap (More intuitive but slower)

```cpp
#include <vector>
#include <queue>

using namespace std;

class SolutionSimulation {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> counts;
        for (char t : tasks) counts[t]++;
        
        priority_queue<int> pq;
        for (auto& pair : counts) pq.push(pair.second);
        
        int time = 0;
        queue<pair<int, int>> waitQueue; // {count, readyTime}
        
        while (!pq.empty() || !waitQueue.empty()) {
            time++;
            
            if (!pq.empty()) {
                int count = pq.top();
                pq.pop();
                
                if (count - 1 > 0) {
                    waitQueue.push({count - 1, time + n});
                }
            }
            
            if (!waitQueue.empty() && waitQueue.front().second == time) {
                pq.push(waitQueue.front().first);
                waitQueue.pop();
            }
        }
        
        return time;
    }
};
```

### Python Reference

```python
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        maxFreq = max(count.values())
        maxFreqTasks = 0
        
        for c in count.values():
            if c == maxFreq:
                maxFreqTasks += 1
                
        res = (maxFreq - 1) * (n + 1) + maxFreqTasks
        
        return max(res, len(tasks))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // 1. 統計每個任務的頻率
        // 陣列通常比 HashMap 快 (只有 26 個字母)
        vector<int> freq(26, 0);
        int maxFreq = 0;
        for (char c : tasks) {
            freq[c - 'A']++;
            maxFreq = max(maxFreq, freq[c - 'A']);
        }
        
        // 2. 統計有幾個任務同為最大頻率 (Tie for max frequency)
        // 例如 A:3, B:3, n=2. maxFreq=3, count=2 (A, B)
        // 排列: A B _ A B _ A B
        int maxFreqCount = 0;
        for (int f : freq) {
            if (f == maxFreq) {
                maxFreqCount++;
            }
        }
        
        // 3. 計算公式
        // 我們把頻率最高的任務 A 視為 "骨架"
        // A _ _ A _ _ A
        // 這個骨架有 (maxFreq - 1) 個間隔
        // 每個間隔長度為 (n + 1) (包含 A 自己)
        // 所以基礎長度是 (maxFreq - 1) * (n + 1)
        // 最後，我們要把剩下那一次 A (以及其他也是 maxFreq 的任務)加回去
        // 即 + maxFreqCount
        int calcLen = (maxFreq - 1) * (n + 1) + maxFreqCount;
        
        // 4. 回傳
        // 如果任務種類很多，把空格都填滿了還有剩，那就不會有任何 Idle
        // 此時所需時間就是任務總數
        return max(calcLen, (int)tasks.size());
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Counting frequencies takes $O(N)$.
    -   Finding max takes $O(26) = O(1)$.
-   **Space Complexity**: $O(1)$
    -   Frequency array size 26.
