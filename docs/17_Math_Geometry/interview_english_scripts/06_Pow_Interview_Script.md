# 06 Pow(x, n) — Interview English Script (C++)

> Source aligned with: `docs/17_Math_Geometry/06_Pow.md`

> Quick links: [Source Solution](../06_Pow.md) · [Chapter Script Index](index.md) · [Global Index](../../interview_english_scripts/index.md)

## 1) 30-second problem restatement script

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me restate Pow of x and n. | 我先重述 Pow(x,n)。 | Restatement |
| We must compute x raised to integer power n. | 要計算 x 的 n 次方。 | Restatement |
| N can be negative, so reciprocal handling is required. | n 可能是負數，所以要處理倒數。 | Restatement |
| A linear multiplication loop is too slow for large absolute n. | 線性相乘對大 |n| 太慢。 | Restatement |
| I will use fast exponentiation by squaring. | 我會用平方快速冪。 | Restatement |
| Key edge case is n equals INT_MIN, so I will store exponent in long long. | 重要邊界是 n=INT_MIN，因此指數要用 long long。 | Restatement |

## 2) Clarifying questions (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Should we assume n is 32-bit signed integer? | n 是否為 32 位有號整數？ | Clarify |
| For negative n, do we return exact double reciprocal behavior? | 負 n 是否照雙精度倒數行為回傳？ | Clarify |
| Is iterative binary exponentiation preferred over recursive? | 你偏好迭代還是遞迴快速冪？ | Clarify |
| Should we explicitly guard n equals INT_MIN overflow on negation? | 是否要明確處理 n=INT_MIN 取負溢位？ | Clarify |
| Are floating-point precision artifacts acceptable as usual? | 浮點誤差依一般規則可接受嗎？ | Clarify |

## 3) Approach discussion

### Brute force (3 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Brute force multiplies x by itself absolute n times. | 暴力法是把 x 連乘 |n| 次。 | Approach |
| That costs O(|n|) time, which is too slow for very large exponents. | 這是 O(|n|) 時間，指數大時太慢。 | Approach |
| We need logarithmic exponent reduction. | 我們需要對數級縮小指數。 | Approach |

### Optimized approach (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Convert exponent to long long N to avoid overflow when negating INT_MIN. | 先把指數轉 long long，避免 INT_MIN 取負溢位。 | Approach |
| If N is negative, set x to one over x and N to minus N. | 若 N<0，令 x=1/x，N=-N。 | Approach |
| Maintain answer as one and current_product as x. | 維護 answer=1、current_product=x。 | Approach |
| While N is positive, multiply answer when lowest bit is one, then square current_product and shift N right. | 當 N>0，低位為 1 就乘進答案，再平方底數並右移 N。 | Approach |
| This gives O(log |n|) time and O(1) extra space. | 這可達 O(log|n|) 時間與 O(1) 額外空間。 | Approach |

## 4) Coding-and-speaking script (line-by-line, in coding order)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I cast n to long long N first. | 我先把 n 轉成 long long N。 | Coding |
| If N is negative, I invert x and negate N. | 若 N 為負，我把 x 取倒數並把 N 取正。 | Coding |
| I initialize ans to one and curr to x. | 我初始化 ans=1、curr=x。 | Coding |
| While N is greater than zero, process binary bits. | 當 N>0 就依二進位位元處理。 | Coding |
| If N is odd, multiply ans by curr. | 若 N 為奇數，ans 乘上 curr。 | Coding |
| Square curr each round. | 每輪都把 curr 平方。 | Coding |
| Divide N by two using right shift or integer division. | 用右移或除以二縮小 N。 | Coding |
| After loop ends, return ans. | 迴圈結束後回傳 ans。 | Coding |

## 5) Dry-run script using one sample input

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me dry-run x equals two and n equals ten. | 我用 x=2、n=10 手跑。 | Dry-run |
| N is positive, so no reciprocal step. | N 為正，不做倒數步驟。 | Dry-run |
| Binary of ten is one-zero-one-zero. | 10 的二進位是 1010。 | Dry-run |
| Process bits from low to high: multiply ans only on one bits. | 從低位往高位處理，只有位元 1 才乘進 ans。 | Dry-run |
| Curr evolves as two, four, sixteen, two-fifty-six by squaring. | curr 透過平方依序變 2、4、16、256。 | Dry-run |
| Final ans becomes one thousand twenty-four. | 最終 ans 變成 1024。 | Dry-run |
| That matches expected output. | 這與預期輸出一致。 | Dry-run |

## 6) Edge/corner test script (at least 4 cases)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Case one: n equals zero should return one. | 案例一：n=0 應回 1。 | Edge test |
| Case two: negative exponent like n equals minus two. | 案例二：負指數如 n=-2。 | Edge test |
| Case three: n equals INT_MIN to verify overflow-safe conversion. | 案例三：n=INT_MIN 檢查取負安全性。 | Edge test |
| Case four: x equals one and x equals minus one. | 案例四：x=1 與 x=-1。 | Edge test |
| Case five: fractional base like two point one with small positive n. | 案例五：小數底數如 2.1 搭配小正指數。 | Edge test |

## 7) Complexity script

### Short version (2 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Time complexity is O(log absolute n). | 時間複雜度是 O(log|n|)。 | Complexity |
| Extra space complexity is O(1) for iterative method. | 迭代法額外空間複雜度是 O(1)。 | Complexity |

### Full version (4 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Each loop halves N, so iteration count is logarithmic. | 每輪都把 N 減半，故迭代次數是對數級。 | Complexity |
| Multiplications per loop are constant. | 每輪乘法次數是常數。 | Complexity |
| Therefore runtime is O(log absolute n). | 因此總時間為 O(log|n|)。 | Complexity |
| We keep only scalar variables ans, curr, and N, so extra memory is O(1). | 僅用 ans、curr、N 等純量，額外空間 O(1)。 | Complexity |

## 8) If stuck rescue lines (10 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Let me rewrite exponent using binary decomposition. | 我先把指數改寫成二進位分解。 | If stuck |
| If n is negative, convert to reciprocal base first. | 若 n 為負，先改成倒數底數。 | If stuck |
| Fast power means repeatedly squaring the base. | 快速冪就是重複平方底數。 | If stuck |
| A one bit means include current power in answer. | 位元為 1 代表把當前冪乘進答案。 | If stuck |
| A zero bit means skip multiply for that round. | 位元為 0 則該輪不乘。 | If stuck |
| Shift exponent right each iteration. | 每輪把指數右移。 | If stuck |
| I must use long long to safely negate INT_MIN. | 我必須用 long long 才能安全處理 INT_MIN。 | If stuck |
| Let me verify quickly with n equals minus two. | 我快速驗證 n=-2。 | If stuck |
| Then verify n equals ten for normal flow. | 再驗證 n=10 的一般流程。 | If stuck |
| Great, algorithm and edge handling now align. | 很好，演算法與邊界處理已一致。 | If stuck |

## 9) Final wrap-up lines (5 lines)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| I solved it using iterative exponentiation by squaring. | 我用迭代平方快速冪解題。 | Wrap-up |
| Negative exponents are handled via reciprocal conversion. | 負指數透過倒數轉換處理。 | Wrap-up |
| Casting n to long long handles INT_MIN safely. | 將 n 轉 long long 可安全處理 INT_MIN。 | Wrap-up |
| Complexity is O(log|n|) time and O(1) extra space. | 複雜度是 O(log|n|) 時間、O(1) 額外空間。 | Wrap-up |
| This is the standard interview-optimal power solution. | 這是面試中標準最佳的冪次解法。 | Wrap-up |

## 10) Ultra-short cheat sheet (20 lines total)

| English line | Traditional Chinese meaning (short) | Interview stage |
|---|---|---|
| Goal: compute x to the power n efficiently. | 目標：高效計算 x 的 n 次方。 | Cheat sheet |
| Avoid O(|n|) repeated multiplication. | 避免 O(|n|) 連乘。 | Cheat sheet |
| Use binary exponentiation. | 使用二進位快速冪。 | Cheat sheet |
| Store n in long long N. | 用 long long 存 N。 | Cheat sheet |
| If N < 0, x = 1/x and N = -N. | 若 N<0，x=1/x 且 N=-N。 | Cheat sheet |
| Initialize ans = 1 and curr = x. | 初始化 ans=1、curr=x。 | Cheat sheet |
| While N > 0 loop. | 當 N>0 時迴圈。 | Cheat sheet |
| If N is odd, ans *= curr. | 若 N 奇數，ans*=curr。 | Cheat sheet |
| curr *= curr every round. | 每輪 curr*=curr。 | Cheat sheet |
| N >>= 1 every round. | 每輪 N 右移一位。 | Cheat sheet |
| Return ans at end. | 最後回傳 ans。 | Cheat sheet |
| n = 0 => answer 1. | n=0 時答案為 1。 | Cheat sheet |
| n < 0 => reciprocal path. | n<0 走倒數路徑。 | Cheat sheet |
| INT_MIN requires long long handling. | INT_MIN 需 long long 處理。 | Cheat sheet |
| Time O(log|n|). | 時間 O(log|n|)。 | Cheat sheet |
| Extra space O(1). | 額外空間 O(1)。 | Cheat sheet |
| Common bug: negating int INT_MIN directly. | 常見錯誤：直接對 int 的 INT_MIN 取負。 | Cheat sheet |
| Common bug: forgetting odd-bit multiply. | 常見錯誤：忘記奇數位要乘。 | Cheat sheet |
| Verify with n=10 and n=-2. | 用 n=10 與 n=-2 驗證。 | Cheat sheet |
| Explain with bit contributions for clarity. | 用位元貢獻來說明最清楚。 | Cheat sheet |

## Quality check

- Consistency with source solution: ✅ Fast power (iterative) with negative handling.
- Constraint alignment: ✅ INT_MIN-safe exponent conversion.
- Language simplicity: ✅ Direct and interview-focused.
