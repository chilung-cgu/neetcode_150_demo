---
title: "Encode and Decode Strings (字串編碼與解碼)"
description: "題目要求我們設計兩個函式："
tags:
  - Array
  - Hash Table
difficulty: Medium
---

# Encode and Decode Strings (字串編碼與解碼) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #271** — [題目連結](https://leetcode.com/problems/encode-and-decode-strings/) | [NeetCode 解說](https://neetcode.io/problems/string-encode-and-decode)


## 1. 🧐 Problem Dissection (釐清問題)

題目要求我們設計兩個函式：

1.  `encode(vector<string>) -> string`
2.  `decode(string) -> vector<string>`
    確保 `decode(encode(strs)) == strs`。

- **Constraints**:
  - String 可以包含 **任何 256 個 ASCII 字元**。這意味著它可能包含 `#`, `:`, `/`, 甚至 `\0`。
  - 此題是設計題 (System Design 縮影)，重點在於「如何處理 Delimiter (分隔符) 的衝突」。

---

## 2. 🐢 Naive Approach (Delimiter)

最直覺的想法是用特殊符號把字串接起來。
例如：`["hello", "world"]` -> `"hello,world"`。

- **問題**：如果輸入是 `["hello,", "world"]`，解碼時會變成 `["hello", "", "world"]`。
- **修正**：那用特殊符號如 `π`? 還是會有衝突可能。
- **Escaping**: 也可以像 CSV 一樣用跳脫字元 (Escaping)，例如把 `,` 變成 `\,`。但這樣實作稍複雜 ( $O(n)$ 但常數較大)。

---

## 3. 💡 The "Aha!" Moment (優化)

如何徹底避免內容衝突？ **Length Prefixing (長度前綴)**。

這是網路通訊協定 (如 HTTP Header Content-Length) 常用的技巧。
我們在每個字串前面加上「它的長度」和一個「分隔符」。

**Format**: `length + "#" + content`

- Example: `["hello", "world"]`
- Encode: `5#hello` + `5#world` = `"5#hello5#world"`
- Decode 邏輯:
  1.  讀取數字，直到遇到 `#`。 -> 讀到 `5`。
  2.  讀到 `#`，知道接下來 `5` 個字元是內容。
  3.  讀取 `hello`。
  4.  指標移到下一個位置，重複。

**為什麼這不會衝突？**
因為我們只會把 `#` 當作分隔符號 **如果它前面緊接著數字** (在我們解析長度的時候)。一旦我們解析出長度 `L`，我們就直接讀取接下來 `L` 個 bytes，不管裡面有沒有 `#`，我們都不在乎。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../encode_decode_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../encode_decode_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Length Prefixing

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded = "";
        for (const string& s : strs) {
            encoded += to_string(s.length()) + "#" + s;
        }
        return encoded;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;
        while (i < s.length()) {
            // 尋找分隔符 '#' 的位置
            int j = i;
            while (s[j] != '#') {
                j++;
            }

            // 解析長度 length
            int length = stoi(s.substr(i, j - i));

            // 提取內容 string
            // 內容開始於 j + 1 (跳過 '#')
            string str = s.substr(j + 1, length);
            decoded.push_back(str);

            // 移動指針到下一個區塊的開始
            i = j + 1 + length;
        }
        return decoded;
    }
};
```

### Python Reference

```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    string encode(vector<string>& strs) {
        string res = "";
        for (const string& s : strs) {
            // to_string() 轉換 int -> string
            // 格式確保為：長度 + '#' + 內容
            res += to_string(s.size()) + '#' + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;

        while (i < s.size()) {
            // Step 1: 找到下一個 '#'，這之間的數字就是長度
            int j = i;
            while (s[j] != '#') {
                j++;
            }

            // Step 2: 解析長度
            // s.substr(start, length)
            int len = stoi(s.substr(i, j - i));

            // Step 3: 擷取實際字串
            // 字串起始點是 '#' 的下一位: j + 1
            // 長度是剛剛解出來的 len
            string str = s.substr(j + 1, len);
            res.push_back(str);

            // Step 4: 更新 i 到下一個 chunk 的開頭
            // 目前位置 j + 1 + len
            i = j + 1 + len;
        }

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(N)$
  - $N$ 是所有字串的總字元數。 Encode 遍歷每個字元一次，Decode 也遍歷每個字元一次。
- **Space Complexity**: $O(1)$
  - 如果不計算 Input/Output 所需的儲存空間，我們的 algo 只用了幾個整數變數 (`i`, `j`, `len`)。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果字串包含特殊字元怎麼辦？
- 如何做到流式處理？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 分隔符可能出現在字串內容中
- ⚠️ 整數解析錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 設計 Length-Prefix 編碼
- 💎 主動討論各種編碼方案的優缺點
