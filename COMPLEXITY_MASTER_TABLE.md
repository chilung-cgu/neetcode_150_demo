# LeetCode 複雜度總表（完整速背版）

> 更新日期：2026-03-29（已用官方/權威來源交叉查證）  
> 目標：給你一份「先快背、再細看」的完整 Big-O 速查表。

---

## 0) 符號約定（先看這個）

| 符號 | 意義 |
|---|---|
| `n` | 陣列/字串/節點數量（一般資料量） |
| `m` | 邊數（Graph edges） |
| `V`, `E` | 圖的點數、邊數 |
| `k` | 額外參數（例如 top-k、字母表大小、桶數） |
| `L` | 字串長度（或單字長度） |
| `W` | 背包容量（weight/capacity） |
| `α(n)` | 反 Ackermann 函數（極慢成長，實務可視為接近常數） |

---

## 0.1 你剛問的重點：什麼是 amortized？

**一句話**：  
`amortized O(1)` 不是「每一次都 O(1)」，而是「做很多次後，平均每次成本是 O(1)」。

**用 C++ `vector::push_back` 直覺理解**：

- 平常尾插：直接放進去，成本 `O(1)`  
- 容量滿了：配置更大記憶體 + 搬移舊元素，這次可能 `O(n)`  
- 但擴容不會每次發生，只會偶爾發生  
- 所以連續做很多次 `push_back`，總成本是線性，平均下來每次是 `O(1)`（攤銷）

**小例子**（概念）：

- 連續做 8 次 `push_back`，可能只有第 1、2、4、8 次附近有擴容成本  
- 總成本雖然有幾次很貴，但分攤到 8 次操作後，平均仍是常數級

> [!TIP]
> 面試說法可以用這句：  
> “`push_back` is `O(1)` amortized, with occasional `O(n)` reallocation.”

---

## 0.2 static array vs dynamic array（C++ 版）

### A) Static Array（靜態陣列）

- **大小固定**，建立後不可改  
- 記憶體通常在 stack（區域變數）或靜態區（全域/`static`）  
- 存取 `arr[i]` 是 `O(1)`  
- 不需要擴容邏輯，常數因子小

```cpp
int a[100];               // compile-time fixed size
std::array<int, 100> b;   // fixed-size wrapper
```

### B) Dynamic Array（動態陣列）

- **大小可變**（可 grow/shrink）  
- 記憶體在 heap，容器要管理 `size` 與 `capacity`  
- 隨機存取仍是 `O(1)`  
- 尾插通常 `O(1)` amortized，擴容那次最壞 `O(n)`

```cpp
std::vector<int> v;
v.push_back(42);          // amortized O(1)
```

### C) 快速對照

| 比較項目 | Static Array | Dynamic Array (`vector`) |
|---|---|---|
| 大小是否可變 | 否 | 是 |
| 記憶體位置 | stack/靜態區（常見） | heap（由 allocator 管理） |
| random access | `O(1)` | `O(1)` |
| 尾端新增 | 不適用（固定大小） | `O(1)` amortized，偶爾 `O(n)` |
| 中間插入/刪除 | `O(n)` | `O(n)` |
| 使用情境 | 已知固定大小、追求簡單高效 | 大小不確定、需要彈性 |

---

## 1) 30 秒速背總表（面試前最後看）

| 類別 | 操作/演算法 | Average | Worst | 備註 |
|---|---|---:|---:|---|
| Dynamic Array | random access | `O(1)` | `O(1)` | `arr[i]` |
| Dynamic Array | append (尾插) | `O(1)` amortized | `O(n)` | 擴容時搬移 |
| Dynamic Array | insert/delete middle | `O(n)` | `O(n)` | 需位移 |
| Hash Table | search/insert/delete | `O(1)` | `O(n)` | 碰撞極端情況 |
| Balanced BST (`map/set`) | search/insert/delete | `O(log n)` | `O(log n)` | 紅黑樹等 |
| Heap | push / pop | `O(log n)` | `O(log n)` | top=`O(1)` |
| BFS / DFS | 圖遍歷 | `O(V+E)` | `O(V+E)` | adjacency list |
| Binary Search | 查找 | `O(log n)` | `O(log n)` | 已排序前提 |
| Merge Sort | 排序 | `O(n log n)` | `O(n log n)` | 穩定，額外 `O(n)` |
| Quick Sort | 排序 | `O(n log n)` | `O(n^2)` | pivot 選不好會退化 |
| Dijkstra (heap) | 最短路 | `O((V+E)logV)` | `O((V+E)logV)` | 邊權非負 |
| Bellman-Ford | 最短路 | `O(VE)` | `O(VE)` | 可處理負權 |
| Floyd-Warshall | 全點對最短路 | `O(V^3)` | `O(V^3)` | 小圖常用 |
| DSU (Union-Find) | find/union | `O(α(n))` amortized | 單次可到 `O(log n)` | 路徑壓縮+按秩合併 |

---

## 2) 資料結構操作複雜度（通用）

### 2.1 線性結構

| 資料結構 | 操作 | Average | Worst | 備註 |
|---|---|---:|---:|---|
| Array (static) | access by index | `O(1)` | `O(1)` | 連續記憶體 |
| Array (static) | search | `O(n)` | `O(n)` | 未排序 |
| Array (static) | insert/delete | `O(n)` | `O(n)` | 需搬移 |
| Dynamic Array | access by index | `O(1)` | `O(1)` | `vector/list` 類 |
| Dynamic Array | append | `O(1)` amortized | `O(n)` | reallocation |
| Dynamic Array | pop back | `O(1)` | `O(1)` | |
| Dynamic Array | insert/delete at i | `O(n)` | `O(n)` | 位移 |
| Singly Linked List | access by index | `O(n)` | `O(n)` | 無隨機存取 |
| Singly Linked List | search | `O(n)` | `O(n)` | |
| Singly Linked List | insert/delete head | `O(1)` | `O(1)` | |
| Singly Linked List | insert after known node | `O(1)` | `O(1)` | 已拿到節點指標 |
| Doubly Linked List | insert/delete head/tail | `O(1)` | `O(1)` | |
| Doubly Linked List | delete known node | `O(1)` | `O(1)` | |
| Stack | push/pop/top | `O(1)` | `O(1)` | |
| Queue | enqueue/dequeue/front | `O(1)` | `O(1)` | |
| Deque | push/pop both ends | `O(1)` | `O(1)` | |

### 2.2 雜湊、樹、優先佇列

| 資料結構 | 操作 | Average | Worst | 備註 |
|---|---|---:|---:|---|
| Hash Table | search/insert/delete | `O(1)` | `O(n)` | hash collision 退化 |
| Binary Search Tree (未平衡) | search/insert/delete | `O(log n)` | `O(n)` | skew tree 退化 |
| Balanced BST (AVL/RB) | search/insert/delete | `O(log n)` | `O(log n)` | |
| Heap (binary) | top | `O(1)` | `O(1)` | |
| Heap (binary) | push / pop | `O(log n)` | `O(log n)` | |
| Heap (binary) | build heap | `O(n)` | `O(n)` | |
| Trie | insert/search/delete | `O(L)` | `O(L)` | `L` 為 key 長度 |
| Union-Find (DSU) | find/union | `O(α(n))` amortized | 單次可到 `O(log n)` | 路徑壓縮 + union by rank/size |

### 2.3 區間資料結構（LeetCode 高頻）

| 結構 | 建構 | 查詢 | 更新 | 空間 |
|---|---:|---:|---:|---:|
| Prefix Sum | `O(n)` | `O(1)` 區間和 | 單點改值 `O(n)` | `O(n)` |
| Difference Array | `O(n)` | 回復原陣列 `O(n)` | 區間加值 `O(1)` | `O(n)` |
| Fenwick Tree (BIT) | `O(n)` | prefix/range `O(log n)` | `O(log n)` | `O(n)` |
| Segment Tree | `O(n)` | `O(log n)` | `O(log n)` | `O(n)`（常見實作約 `4n`） |
| Sparse Table | `O(n log n)` | `O(1)`（idempotent，如 min/max/gcd） | 不支援動態更新 | `O(n log n)` |

---

## 3) 語言容器速查（LeetCode 常用）

## 3.1 Python（CPython）

| 容器 | 操作 | Average | Worst | 備註 |
|---|---|---:|---:|---|
| `list` | `a[i]` 讀寫 | `O(1)` | `O(1)` | 動態陣列 |
| `list` | `append` | `O(1)` | 單次可 `O(n)` | 攤銷常數 |
| `list` | `pop()` (尾端) | `O(1)` | `O(1)` | |
| `list` | `insert(i,x)` / `pop(i)` | `O(n)` | `O(n)` | 位移 |
| `list` | `x in list` | `O(n)` | `O(n)` | 線性掃描 |
| `collections.deque` | `append/appendleft` | `O(1)` | `O(1)` | 雙端高效 |
| `collections.deque` | `pop/popleft` | `O(1)` | `O(1)` | |
| `collections.deque` | `remove(x)` | `O(n)` | `O(n)` | |
| `dict` | `get/set/del/in` | `O(1)` | `O(n)` | hash table |
| `set` | `add/remove/in` | `O(1)` | `O(n)` | hash table |
| `set` | union `s|t` | `O(len(s)+len(t))` | `O(len(s)+len(t))` | |
| `set` | intersection `s&t` | `O(min(len(s),len(t)))` | `O(len(s)*len(t))` | |

> 註：Python 官方 wiki 明確區分 average 與 worst；worst-case 多半來自碰撞或極端配置。

### 3.2 C++ STL（常見容器）

| 容器 | 操作 | Average | Worst | 備註 |
|---|---|---:|---:|---|
| `vector` | random access | `O(1)` | `O(1)` | |
| `vector` | `push_back` | `O(1)` amortized | `O(n)` | 擴容搬移 |
| `vector` | insert/erase middle | `O(n)` | `O(n)` | |
| `deque` | random access | `O(1)` | `O(1)` | |
| `deque` | push/pop front/back | `O(1)` | `O(1)` | |
| `deque` | insert/erase middle | `O(n)` | `O(n)` | |
| `list` | insert/erase known iterator | `O(1)` | `O(1)` | 雙向 linked list |
| `list` | random access / search | `O(n)` | `O(n)` | |
| `map` / `set` | search/insert/erase | `O(log n)` | `O(log n)` | 紅黑樹 |
| `unordered_map` / `unordered_set` | search/insert/erase | `O(1)` | `O(n)` | 平均常數、最壞線性 |
| `priority_queue` | `top` | `O(1)` | `O(1)` | heap top |
| `priority_queue` | `push/pop` | `O(log n)` | `O(log n)` | |

---

## 4) 排序 / 選擇 / 搜尋演算法

### 4.1 排序總表

| 演算法 | Best | Average | Worst | Extra Space | Stable | 備註 |
|---|---:|---:|---:|---:|---|---|
| Bubble Sort（優化版） | `O(n)` | `O(n^2)` | `O(n^2)` | `O(1)` | 是 | 幾乎不用於實戰 |
| Selection Sort | `O(n^2)` | `O(n^2)` | `O(n^2)` | `O(1)` | 否 | 交換次數少 |
| Insertion Sort | `O(n)` | `O(n^2)` | `O(n^2)` | `O(1)` | 是 | 小資料很實用 |
| Merge Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | 是 | 穩定 |
| Quick Sort | `O(n log n)` | `O(n log n)` | `O(n^2)` | `O(log n)` avg recursion | 否 | pivot 決定退化風險 |
| Heap Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` | 否 | 原地但不穩定 |
| Counting Sort | `O(n+k)` | `O(n+k)` | `O(n+k)` | `O(n+k)` | 可穩定 | `k` 為值域 |
| Radix Sort | `O(d(n+k))` | `O(d(n+k))` | `O(d(n+k))` | `O(n+k)` | 視底層排序 | `d` 位數 |
| Bucket Sort | `O(n+k)` | `O(n+k)`（分布佳） | `O(n^2)` | `O(n+k)` | 視實作 | 依資料分布 |
| Timsort（Python sort） | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | 是 | 真實工程常用 |

### 4.2 搜尋 / 選擇

| 演算法 | Average | Worst | 備註 |
|---|---:|---:|---|
| Linear Search | `O(n)` | `O(n)` | |
| Binary Search（已排序） | `O(log n)` | `O(log n)` | |
| Quickselect（第 k 小/大） | `O(n)` | `O(n^2)` | 隨機 pivot 可改善期望 |

---

## 5) 圖論演算法（LeetCode 高頻）

| 演算法 | 時間複雜度 | 空間複雜度 | 備註 |
|---|---:|---:|---|
| BFS | `O(V+E)` | `O(V)` | adjacency list |
| DFS | `O(V+E)` | `O(V)` | 遞迴棧最深可到 `V` |
| Topological Sort（Kahn/DFS） | `O(V+E)` | `O(V)` | DAG |
| Dijkstra（binary heap） | `O((V+E)logV)` | `O(V+E)` | 邊權需非負 |
| Dijkstra（dense/array） | `O(V^2)` | `O(V^2)` 或 `O(V+E)` | 稠密圖常見 |
| Bellman-Ford | `O(VE)` | `O(V)` | 可處理負權、可檢測負環 |
| Floyd-Warshall | `O(V^3)` | `O(V^2)` | 全點對最短路 |
| Kruskal (MST) | `O(E log E)`（≈`O(E log V)`） | `O(V)` | 排序邊 + DSU |
| Prim（binary heap） | `O(E log V)` | `O(V+E)` | |
| Prim（adj matrix） | `O(V^2)` | `O(V^2)` | |
| SCC（Tarjan/Kosaraju） | `O(V+E)` | `O(V)` | |
| Bridge / Articulation Point | `O(V+E)` | `O(V)` | low-link |
| Union-Find per op | `O(α(n))` amortized | `O(n)` | 連通分量題常用 |

---

## 6) DP / 回溯 / 字串 / 數學

### 6.1 動態規劃（經典）

| 問題/方法 | 時間 | 空間 | 備註 |
|---|---:|---:|---|
| Fibonacci / Climbing Stairs | `O(n)` | `O(1)` 可優化 | |
| 0/1 Knapsack | `O(nW)` | `O(W)`（壓縮後） | pseudo-polynomial |
| Coin Change | `O(n*amount)` | `O(amount)` | |
| LIS（binary search 解） | `O(n log n)` | `O(n)` | |
| LIS（DP 解） | `O(n^2)` | `O(n)` | |
| LCS | `O(nm)` | `O(nm)` | |
| Edit Distance | `O(nm)` | `O(nm)` | 可優化到 `O(min(n,m))` |
| Interval DP（常見） | `O(n^3)` | `O(n^2)` | 例：區間合併類 |

### 6.2 回溯 / 搜尋樹

| 類型 | 時間（常見上界） | 空間 | 備註 |
|---|---:|---:|---|
| Subsets | `O(2^n)` | `O(n)`（遞迴深度） | 輸出本身也是 `2^n` |
| Permutations | `O(n!)` | `O(n)` | |
| Combination（n 選 k） | `O(C(n,k) * k)` | `O(k)` | |
| N-Queens | 約 `O(n!)` | `O(n)` | 強烈依剪枝 |

### 6.3 字串演算法

| 演算法 | 時間 | 空間 | 備註 |
|---|---:|---:|---|
| KMP | `O(n+m)` | `O(m)` | `n` 文本、`m` pattern |
| Z-Algorithm | `O(n)` | `O(n)` | |
| Rabin-Karp | 平均 `O(n+m)` | 最壞 `O(nm)` | hash collision 退化 |
| Trie Search/Insert | `O(L)` | `O(total chars)` | |

### 6.4 數學與位元

| 方法 | 時間 | 空間 | 備註 |
|---|---:|---:|---|
| Fast Power（Binary Exponentiation） | `O(log n)` | `O(1)` 或 `O(log n)` 遞迴 | |
| Euclid GCD | `O(log min(a,b))` | `O(1)` | |
| Sieve of Eratosthenes | `O(n log log n)` | `O(n)` | |
| 位元計數（固定 32/64 位） | `O(1)` | `O(1)` | 若以 machine word 視角 |

---

## 7) LeetCode 高頻模板複雜度（超實用）

| 模板 | 時間 | 空間 | 關鍵備註 |
|---|---:|---:|---|
| Two Pointers（同向/對撞） | `O(n)` | `O(1)` | |
| Sliding Window | `O(n)` | `O(1)`~`O(k)` | 每元素進出窗口最多一次 |
| Monotonic Stack | `O(n)` amortized | `O(n)` | 每元素 push/pop 最多一次 |
| Monotonic Deque | `O(n)` amortized | `O(n)` | Sliding Window Maximum 經典 |
| Prefix Sum | build `O(n)`, query `O(1)` | `O(n)` | |
| Binary Search on Answer | `O(logR * check(n))` | 依 check | `R` 為答案範圍 |
| Meet in the Middle | `O(2^(n/2))` | `O(2^(n/2))` | 指數降半常用於 `n<=40` |

---

## 8) 最容易背錯的 10 件事（務必記住）

1. `unordered_map` / `dict` 是 **平均 `O(1)`**，不是保證最壞 `O(1)`。  
2. Dynamic Array 的 `append` 是 **攤銷 `O(1)`**，單次可能 `O(n)`。  
3. `list.pop(0)` 在 Python 是 `O(n)`，不是 `O(1)`。  
4. Quick Sort 不是永遠 `O(n log n)`；最壞 `O(n^2)`。  
5. BFS/DFS 的 `O(V+E)` 是在 adjacency list；若用 matrix 會變 `O(V^2)`。  
6. Dijkstra 不能處理負權邊。  
7. DSU 的 `O(α(n))` 是 **amortized**，不是每次嚴格常數。  
8. Heap 的 `top` 是 `O(1)`，但 `push/pop` 是 `O(log n)`。  
9. BST 若不平衡會退化到 `O(n)`。  
10. DP 的時間常常取決於狀態數 × 轉移數，先數這兩個再下結論。

---

## 9) 查證來源（本次整理實際檢查）

### 官方/權威容器複雜度

- C++ 參考（cppreference）  
  - `vector`：<https://en.cppreference.com/w/cpp/container/vector>  
  - `deque`：<https://en.cppreference.com/w/cpp/container/deque>  
  - `list`：<https://en.cppreference.com/w/cpp/container/list>  
  - `map`：<https://en.cppreference.com/w/cpp/container/map>  
  - `set`：<https://en.cppreference.com/w/cpp/container/set>  
  - `unordered_map`：<https://en.cppreference.com/w/cpp/container/unordered_map>  
  - `unordered_set`：<https://en.cppreference.com/w/cpp/container/unordered_set>  
  - `priority_queue`：<https://en.cppreference.com/w/cpp/container/priority_queue>  

- Python（CPython）時間複雜度參考（官方 wiki 封存頁）  
  - <https://wiki.python.org/moin/TimeComplexity>

### 演算法複雜度（cp-algorithms）

- BFS：<https://cp-algorithms.com/graph/breadth-first-search.html>  
- DFS：<https://cp-algorithms.com/graph/depth-first-search.html>  
- Dijkstra：<https://cp-algorithms.com/graph/dijkstra.html>  
- Bellman-Ford：<https://cp-algorithms.com/graph/bellman_ford.html>  
- Floyd-Warshall：<https://cp-algorithms.com/graph/all-pair-shortest-path-floyd-warshall.html>  
- DSU：<https://cp-algorithms.com/data_structures/disjoint_set_union.html>  
- Kruskal + DSU：<https://cp-algorithms.com/graph/mst_kruskal_with_dsu.html>

### 補充（排序總覽）

- Sorting algorithms（比較表與背景）：  
  <https://en.wikipedia.org/wiki/Sorting_algorithm>

---

## 10) 使用建議（背誦路線）

1. 先背「30 秒速背總表」。  
2. 再背「第 7 節高頻模板」。  
3. 最後補齊「第 4、5、6 節」細節（尤其圖論與 DP）。  
4. 每次刷題寫下：`time = ?`、`space = ?`、`why`，背得最快。
