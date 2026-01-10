# 📚 MkDocs 使用指南

## 本地預覽 (Local Preview)

由於我們採用 **Build-time Copy Strategy** 來保持 Repo 整潔，請使用提供的腳本來啟動預覽：

```bash
# 1. 執行建置腳本 (這會將題目複製到 docs/ 並生成索引)
./scripts/build_docs.sh

# 2. 啟動 MkDocs 伺服器
mkdocs serve
```

或者如果您只想要單次編譯：

```bash
./scripts/build_docs.sh
```

瀏覽器開啟：`http://localhost:8000`

---

## 部署到 GitHub Pages

### 自動部署（推薦）

我們已配置 GitHub Actions (`.github/workflows/deploy-docs.yml`)。
每次 **Push to main** 時，系統會自動：
1. Checkout 原始碼
2. 執行 `./scripts/build_docs.sh` (動態生成完整文檔結構)
3. 部署到 GitHub Pages

**初次設定**：
1. 確保 Repo 為 Public
2. Settings → Pages → Source 選擇 **GitHub Actions**

網站網址：`https://chilung-cgu.github.io/neetcode_150_demo/`

---

## 專案結構說明

- **`docs/`**：只包含靜態資源 (index.md, css, configured nav pages)。**不要**在此提交題目檔案。
- **`scripts/build_docs.sh`**：負責將 `01_Arrays...` 等模組複製進 `docs/`。
- **`.gitignore`**：已設定忽略 `docs/[0-9][0-9]_*/`，防止重複提交。

---

## 常見問題

### Q: 我修改了根目錄的題目，為什麼 `mkdocs serve` 沒變？
A: `mkdocs serve` 預設監聽 `docs/` 資料夾。因為我們是從根目錄複製進去的，您需要**重新執行** `./scripts/build_docs.sh` 來更新 `docs/` 中的副本。
