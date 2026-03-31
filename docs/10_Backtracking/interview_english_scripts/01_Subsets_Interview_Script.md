# 01 Subsets — Interview English Script (C++)

> Source aligned with: `docs/10_Backtracking/01_Subsets.md`

> Quick links: [Source Solution](../01_Subsets.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate the subsets problem. | 我先重述 subsets 題目。 | Restatement |
| We are given an array of distinct integers. | 題目給一個元素互異的整數陣列。 | Restatement |
| We need to return all possible subsets. | 要回傳所有可能子集。 | Restatement |
| The empty subset must be included too. | 空集合也必須包含。 | Restatement |
| Output order does not matter in this problem. | 這題輸出順序不重要。 | Restatement |
| I will use DFS backtracking with include or exclude decisions. | 我會用 DFS 回溯做選或不選。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Can I assume all numbers are unique as stated? | 可依題意假設所有數字都不重複嗎？ | Clarify |
| Is any output ordering acceptable? | 輸出順序是否可任意？ | Clarify |
| Should the empty set be explicitly returned? | 是否一定要顯式回傳空集合？ | Clarify |
| Is recursive backtracking acceptable for this input size? | 這個輸入規模可接受遞迴回溯嗎？ | Clarify |
| Do you also want iterative or bitmask alternatives discussed? | 是否也希望我提迭代或 bitmask 替代法？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force can enumerate every bitmask from zero to two to the n minus one. | 暴力法可列舉 0 到 2^n-1 的 bitmask。 | Approach |
| Each bit tells whether the corresponding element is picked. | 每個位元表示該元素是否被選。 | Approach |
| This still takes O(n times two to the n). | 這仍需要 O(n*2^n)。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Use DFS where each index has two decisions. | 用 DFS，對每個索引做兩種決策。 | Approach |
| Decision one is exclude current number and move on. | 決策一是不選當前數字，往下走。 | Approach |
| Decision two is include it, recurse, then backtrack. | 決策二是選它、遞迴、再回溯。 | Approach |
| When index reaches n, current path is one valid subset. | 當索引到 n，當前路徑就是合法子集。 | Approach |
| This is clean, interview-friendly, and maps to the decision tree directly. | 這種寫法清楚且直接對應決策樹。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I define result list and current subset path. | 我先定義結果陣列與當前路徑。 | Coding |
| I write dfs function taking index and path state. | 我撰寫 dfs，參數是索引與路徑狀態。 | Coding |
| Base case is index equals nums size. | 基底條件是 index 等於陣列長度。 | Coding |
| At base case I append a copy of current path. | 在基底時加入路徑拷貝。 | Coding |
| First branch is exclude nums[index]. | 第一分支是不選 nums[index]。 | Coding |
| Second branch pushes nums[index], recurses, then pops. | 第二分支是 push、遞迴、再 pop。 | Coding |
| Backtracking pop restores state for sibling branch. | 回溯的 pop 會還原狀態給同層分支。 | Coding |
| Finally I return the full result collection. | 最後回傳完整結果集合。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run nums equals [1,2,3]. | 我手跑 nums=[1,2,3]。 | Dry-run |
| Start at index zero with empty path. | 從 index=0、空路徑開始。 | Dry-run |
| Exclude one branch eventually yields empty and [3], [2], [2,3]. | 不選 1 的分支會得到空集與 [3]、[2]、[2,3]。 | Dry-run |
| Include one branch yields [1], [1,3], [1,2], [1,2,3]. | 選 1 的分支會得到 [1]、[1,3]、[1,2]、[1,2,3]。 | Dry-run |
| Total subsets are eight, which equals two to the power three. | 總子集數為 8，等於 2^3。 | Dry-run |
| Every subset appears exactly once. | 每個子集都剛好出現一次。 | Dry-run |
| This matches expected output pattern. | 這與預期輸出型態一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: single element array should return two subsets. | 案例一：單元素陣列應回傳兩個子集。 | Edge test |
| Case two: negative values should work exactly the same. | 案例二：負數元素也應完全正常。 | Edge test |
| Case three: larger n should still produce two to the n subsets. | 案例三：較大 n 仍應產生 2^n 個子集。 | Edge test |
| Case four: verify no duplicate subsets when input is distinct. | 案例四：輸入互異時不應有重複子集。 | Edge test |
| Case five: check empty subset is present in output. | 案例五：確認輸出包含空集合。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(n times two to the n). | 時間複雜度是 O(n*2^n)。 | Complexity |
| Auxiliary space is O(n), excluding output storage. | 不含輸出時輔助空間為 O(n)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| There are two choices per element, so we have two to the n leaves. | 每元素兩種選擇，因此有 2^n 個葉節點。 | Complexity |
| Building or copying subset content contributes the factor n. | 建立或拷貝子集內容帶來 n 因子。 | Complexity |
| Recursion depth is at most n. | 遞迴深度最多是 n。 | Complexity |
| Output itself requires O(n times two to the n) memory. | 輸出本身記憶體是 O(n*2^n)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me reduce this to a binary decision per element. | 我先把它化成每元素二元決策。 | If stuck |
| Each number is either in or out of current subset. | 每個數字不是選就是不選。 | If stuck |
| That naturally forms a DFS tree. | 這自然形成 DFS 樹。 | If stuck |
| I should stop when index reaches array length. | 索引到陣列末端就該停止。 | If stuck |
| At that point I record one subset snapshot. | 那時就記錄一份子集快照。 | If stuck |
| If I forget pop, sibling branches will be polluted. | 若忘記 pop，同層分支會被污染。 | If stuck |
| Let me verify with [1,2] quickly. | 我快速用 [1,2] 驗證。 | If stuck |
| I get [], [2], [1], [1,2], which is correct. | 得到 []、[2]、[1]、[1,2]，正確。 | If stuck |
| So recursion and backtracking states are now consistent. | 遞迴與回溯狀態已一致。 | If stuck |
| Great, I can finalize complexity confidently. | 很好，我可有把握地收尾複雜度。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved subsets with DFS include or exclude branching. | 我用 DFS 選或不選分支解出 subsets。 | Wrap-up |
| The implementation is short and easy to reason about. | 這份實作精簡且容易推理。 | Wrap-up |
| It generates every subset exactly once. | 它會剛好生成每個子集一次。 | Wrap-up |
| Runtime is O(n times two to the n). | 時間是 O(n*2^n)。 | Wrap-up |
| I can also provide iterative and bitmask variants if needed. | 若需要我也可補充迭代與 bitmask 版本。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Problem type: power set generation. | 題型：冪集合生成。 | Cheat sheet |
| Input numbers are distinct. | 輸入數字互異。 | Cheat sheet |
| Include empty subset. | 必含空集合。 | Cheat sheet |
| Two choices per element. | 每元素兩種選擇。 | Cheat sheet |
| Use DFS backtracking. | 使用 DFS 回溯。 | Cheat sheet |
| State: current index and path. | 狀態：索引與路徑。 | Cheat sheet |
| Base: index equals n. | 基底：index==n。 | Cheat sheet |
| Record path copy at base. | 基底時記錄路徑拷貝。 | Cheat sheet |
| Branch one: exclude current. | 分支一：不選當前值。 | Cheat sheet |
| Branch two: include current. | 分支二：選當前值。 | Cheat sheet |
| Include branch needs push and pop. | 選取分支需 push 與 pop。 | Cheat sheet |
| Pop restores sibling state. | pop 還原同層狀態。 | Cheat sheet |
| Total subsets count is 2^n. | 子集總數是 2^n。 | Cheat sheet |
| Time complexity O(n*2^n). | 時間複雜度 O(n*2^n)。 | Cheat sheet |
| Aux space O(n). | 輔助空間 O(n)。 | Cheat sheet |
| Output space O(n*2^n). | 輸出空間 O(n*2^n)。 | Cheat sheet |
| Validate with [1,2,3]. | 用 [1,2,3] 驗證。 | Cheat sheet |
| Check empty subset exists. | 檢查空集合存在。 | Cheat sheet |
| Any output order is fine. | 任意輸出順序可接受。 | Cheat sheet |
| Alternative: bitmask enumeration. | 替代法：bitmask 列舉。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ DFS include/exclude logic is preserved.
- No hallucinated constraints: ✅ Follows distinct-input and power-set semantics.
- Language simplicity: ✅ Natural spoken lines for interview narration.
