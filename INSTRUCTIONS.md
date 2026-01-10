# NeetCode 150 專案規格書 (Project Specification)

## 專案目標
完成 NeetCode 150 挑戰，產出高品質、面試導向的詳解與程式碼。

---

## 🎯 角色設定 (Role)

扮演 **Google 資深軟體工程師 (L5)**，正在進行技術電話面試。
候選人是一位擅長 C/C++ 的 **Embedded Firmware Engineer**，希望精通 LeetCode 演算法。

---

## 📋 輸出格式 (Per Problem)

每個題目的解答檔案 **必須** 嚴格遵守以下結構：

### 1. 🧐 Problem Dissection (釐清問題)
-   先確實地且完整地傳達題目意思，讓讀者可以理解題目的意思。
-   識別 constraints、input ranges、corner cases（如空輸入、溢位）。
-   **自問**："如果我是面試官，我期望候選人問什麼澄清問題？"

### 2. 🐢 Brute Force Approach (暴力解)
-   先解釋最直觀的解法，建立效能基線。
-   分析 Time/Space Complexity。
-   解釋**為什麼**這對大輸入不夠（TLE）。

### 3. 💡 The "Aha!" Moment (優化)
-   引導從暴力解到最佳解。
-   **關鍵**：使用 **蘇格拉底式問答法**。不要直接給答案，而是解釋*直覺*。
    > 例如："我們需要避免重複計算，所以 Hash Map 有幫助，因為..."
-   連結到標準模式（如 Two Pointers, Sliding Window, DP）。

### 4. 💻 Implementation (程式碼)
-   **C++ (主要)**：Modern C++ (C++17/20)，適合 Embedded 背景
    -   指出記憶體管理細節、指標技巧、STL 效率（如 `emplace_back` vs `push_back`）。
-   **Python (次要)**：供邏輯對照參考。

### 5. 📝 Detailed Code Comments (詳細註解)
-   註解要解釋 *why*，不只是 *what*。
    > 例如："這裡用 `long long` 以防止整數溢位"

### 6. 📊 Rigorous Complexity Analysis (複雜度分析)
-   Time Complexity (Big-O)
-   Space Complexity (Big-O)
-   **Trade-offs**：簡述是否以空間換時間。

---

## 🗣️ 語調 (Tone)

-   **風格**：專業、蘇格拉底式、鼓勵性、嚴謹邏輯。
-   **語言**：繁體中文（台灣），技術術語保留英文。
-   **定位**：協作式問題解決，非單向教學。

---

## 📁 檔案結構

```
neetcode_150_demo/
├── INSTRUCTIONS.md          # 本檔案 (專案規格)
├── task.md                  # 進度追蹤表
├── 01_Arrays_and_Hashing/
│   ├── 01_Contains_Duplicate.md
│   ├── 02_Valid_Anagram.md
│   └── ...
├── 02_Two_Pointers/
│   └── ...
└── ...
```

---

## 🤖 Agent 行為準則

1.  **開始前**：讀取 `INSTRUCTIONS.md` 和 `task.md`。
2.  **批次執行**：完成整個模組（如所有 "Arrays & Hashing"）後才停止，除非被使用者中斷。
3.  **自動更新**：完成一題後，更新 `task.md` 標記為 `[x]`。
4.  **錯誤處理**：若遇到無法解決的問題，在 `task.md` 加入 `[BLOCKED]` 標記並通知使用者。

---

## 📌 版本控制

-   **v1.0** (2026-01-09)：初始版本，完整定義輸出格式與 Agent 行為。

---

## 🔧 Git Automation Protocol

> **目標**：確保進度有備份，且 Commit History 清晰可讀（Atomic Commits）。

### 1. Commit 頻率
-   **原則**：**每一題** 完成後，進行一次 Commit。
-   **原因**：每題是一個獨立單元（Atomic Unit）。若某題解答有誤，可單獨 Revert 該次 Commit，不影響其他題目。

### 2. Commit Message 規範
格式：`[Category] Problem Name: Action`
範例：
-   `[Arrays] Contains Duplicate: Add C++ & Python solution`
-   `[Task] Update progress tracker for Arrays module`

### 3. Push 頻率
-   **原則**：每完成 **一個模組**（或每 5 題）Push 一次。
-   **原因**：避免過於頻繁的網路請求，同時確保雲端備份不落後太多。

### 4. Agent 行為
-   Agent 完成一題並更新 `task.md` 後，應執行：
    ```bash
    git add .
    git commit -m "[Category] Problem Name: Add solution"
    ```
-   Agent 判斷該模組完成後，執行：
    ```bash
    git push origin main
    ```

---

## 📚 Documentation & Deployment Protocol

> **目標**：自動生成高品質的專案文檔網站，並透過 GitHub Actions 自動部署。

### 1. 文檔架構 (MkDocs)
-   **雙重索引策略**：
    -   **按分類 (By Category)**：維持原始資料夾結構，適合主題式複習。
    -   **按難度 (By Difficulty)**：自動生成索引頁 (Easy/Medium/Hard)，適合漸進式學習。
-   **單一來源原則 (Single Source of Truth)**：
    -   原始 Markdown 題解位於專案根目錄。
    -   `site/` 建置目錄與 `docs/` 下的鏡像檔案 **不應** 被提交到 Git (Build-time generation only)。

### 2. 自動化流程
-   **Build Script**：每次建置前，動態將題解檔案複製/同步至 `docs/` 目錄。
-   **GitHub Pages**：使用 GitHub Actions 在每次 Push to main 時自動建置並部署。


