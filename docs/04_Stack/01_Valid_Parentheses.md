# Valid Parentheses (有效的括號)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個只包含 `(`, `)`, `{`, `}`, `[`, `]` 的字串 `s`。
判斷這個字串是否有效。
有效條件：

1.  左括號必須由相同類型的右括號閉合。
2.  左括號必須以正確的順序閉合。
    -   `"()"` -> True
    -   `"()[]{}"` -> True
    -   `"(]"` -> False
    -   `"([)]"` -> False (順序錯了)
    -   `"{[]}"` -> True

-   **Input**: `s = "()"`
-   **Output**: `true`
-   **Constraints**:
    -   $1 <= s.length <= 10^4$.

---

## 2. 🐢 Brute Force Approach (暴力解)

不斷地尋找成對的 `()`, `[]`, `{}` 並把它們刪除，直到字串為空或無法刪除。

-   `replace("()", "")`, `replace("[]", "")`...
-   **Time**: $O(n^2)$。因為每次 delete/replace 都可能重組字串。
-   **Result**: 雖然可行，但在字串很長時效率差。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 **Stack (堆疊)** 的教科書範例。
Stack 的特性是 **LIFO (Last In, First Out)**，這完美契合括號匹配的「最近開啟的括號必須最先閉合」的規則。

**演算法**:

1.  遍歷字串中的每個字元 `c`。
2.  如果是 **左括號** (`(`, `[`, `{`)：
    -   把它 Push 進 Stack。因為我們期待在未來看到對應的右括號。
3.  如果是 **右括號** (`]`, `}`, `)`)：
    -   檢查 Stack 是否為空。如果不空，Pop 出頂端的元素 `top`。
    -   檢查 `top` 和 `c` 是否配對 (`(`配`)`, `[`配`]`, `{`配`}`)。
    -   如果 Stack 為空 **或者** 不配對，則無效 (`false`)。
4.  最後檢查 Stack 是否為空。如果還有殘留的左括號，則是無效 (`false`)。

---

## 4. 💻 Implementation (程式碼)

### Approach: Stack

```cpp
#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> openStack;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                openStack.push(c);
            } else {
                // 遇到右括號，但在這之前沒有左括號 -> Invalid
                if (openStack.empty()) return false;

                char top = openStack.top();
                if ((c == ')' && top == '(') ||
                    (c == ']' && top == '[') ||
                    (c == '}' && top == '{')) {
                    openStack.pop();
                } else {
                    return false; // Mismatch
                }
            }
        }

        return openStack.empty();
    }
};
```

### Python Reference

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isValid(string s) {
        // 使用 Stack 來儲存尚未閉合的左括號
        stack<char> stk;

        for (char c : s) {
            // Case 1: 左括號，直接入棧
            // 我們還不知道這是否有效，直到看到右括號
            if (c == '(' || c == '{' || c == '[') {
                stk.push(c);
            }
            // Case 2: 右括號，嘗試匹配
            else {
                // 如果棧是空的，代表沒有左括號來配對這個右括號
                // e.g., "())" 的最後一個 ')'
                if (stk.empty()) {
                    return false;
                }

                char open = stk.top();

                // 檢查是否匹配
                bool isMatch = (c == ')' && open == '(') ||
                               (c == '}' && open == '{') ||
                               (c == ']' && open == '[');

                if (isMatch) {
                    stk.pop(); // 匹配成功，消除這一對
                } else {
                    return false; // 類型不符 e.g., "(]"
                }
            }
        }

        // 如果最後棧不為空，代表有左括號沒被閉合 e.g., "(()"
        return stk.empty();
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   只需遍歷字串一次。每個字元 Push 一次，Pop 最多一次。
-   **Space Complexity**: $O(n)$
    -   在最壞情況下 (例如 `((((((((` )，Stack 的大小會等於字串長度。
