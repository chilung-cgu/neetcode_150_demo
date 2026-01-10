# 📚 MkDocs 使用指南

## 本地預覽

```bash
# 安裝依賴（首次執行）
pip install mkdocs mkdocs-material

# 啟動本地伺服器
mkdocs serve
```

瀏覽器開啟：`http://localhost:8000`

---

## 自動生成難度索引

每次有新題目時，執行以下指令更新難度索引頁：

```bash
python3 scripts/generate_difficulty_index.py
```

---

## 部署到 GitHub Pages

### 手動部署

```bash
mkdocs gh-deploy
```

### 自動部署（推薦）

已設定 GitHub Actions，每次 push 到 `main` 分支會自動觸發部署。

**初次設定步驟**：
1. 前往 GitHub Repo: `Settings` → `Pages`
2. **Source** 選擇 `GitHub Actions`
3. Push 任何變更後，等待 Actions 完成即可

網站會發布在：`https://chilung-cgu.github.io/neetcode_150_demo/`

---

## 專案結構

```
neetcode_150_demo/
├── docs/                          # MkDocs 文件來源
│   ├── index.md                   # 首頁
│   ├── by-category/               # 按分類索引
│   ├── by-difficulty/             # 按難度索引（自動生成）
│   ├── 01_Arrays_and_Hashing/     # 題目檔案（複製自根目錄）
│   └── ...
├── scripts/
│   └── generate_difficulty_index.py  # 自動化腳本
├── mkdocs.yml                     # MkDocs 配置檔
└── .github/workflows/
    └── deploy-docs.yml            # GitHub Actions 設定
```

---

## 疑難排解

### Q: 修改題目檔案後，網站沒有更新？

A: 請記得同步更新 `docs/` 目錄下的對應檔案：
```bash
# 複製更新後的檔案
cp 01_Arrays_and_Hashing/*.md docs/01_Arrays_and_Hashing/
```

### Q: 如何新增分類索引頁？

A: 手動建立 `docs/by-category/XX-category-name.md`，並在 `mkdocs.yml` 的 `nav` 區塊加入連結。
