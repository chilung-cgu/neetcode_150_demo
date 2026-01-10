#!/usr/bin/env python3
"""
從 task.md 自動生成按難度分類的索引頁面
"""
import re
from pathlib import Path
from collections import defaultdict

def parse_task_md():
    """解析 task.md，提取題目資訊"""
    task_file = Path("task.md")
    if not task_file.exists():
        print("❌ 找不到 task.md")
        return {}
    
    content = task_file.read_text(encoding="utf-8")
    
    # 正則提取：- [x] [題目名稱](路徑.md) <!-- Difficulty -->
    # 範例：- [x] [Contains Duplicate](01_Arrays_and_Hashing/01_Contains_Duplicate.md) <!-- Easy -->
    pattern = r"- \[x\] \[([^\]]+)\]\(([^\)]+)\)\s*<!--\s*(\w+)"
    matches = re.findall(pattern, content)
    
    problems = {"Easy": [], "Medium": [], "Hard": []}
    
    for name, path, difficulty in matches:
        # 提取分類名稱（從路徑）
        parts = path.split("/")
        if len(parts) >= 2:
            category_raw = parts[0]
            # 將 "01_Arrays_and_Hashing" 轉為 "Arrays & Hashing"
            category = category_raw.split("_", 1)[1].replace("_", " ")
            
            problems[difficulty].append({
                "name": name,
                "path": path,
                "category": category
            })
    
    return problems

def generate_difficulty_pages(problems):
    """生成三個難度索引頁"""
    difficulty_info = {
        "Easy": {
            "icon": "📗",
            "desc": "建議先完成所有 Easy 題目，建立基礎並熟悉常見模式（如 Hash Map、Two Pointers、DFS/BFS）。"
        },
        "Medium": {
            "icon": "📙",
            "desc": "挑戰中等難度題目，深入理解演算法優化技巧與多種解法的取捨（Time-Space Tradeoff）。"
        },
        "Hard": {
            "icon": "📕",
            "desc": "攻克高難度題目，掌握進階技巧如動態規劃、圖論演算法、複雜的資料結構設計。"
        }
    }
    
    for diff, items in problems.items():
        output = Path(f"docs/by-difficulty/{diff.lower()}.md")
        output.parent.mkdir(parents=True, exist_ok=True)
        
        icon = difficulty_info[diff]["icon"]
        desc = difficulty_info[diff]["desc"]
        
        with open(output, "w", encoding="utf-8") as f:
            f.write(f"# {icon} {diff} 題目 (共 {len(items)} 題)\n\n")
            f.write(f"> **學習建議**：{desc}\n\n")
            f.write("---\n\n")
            
            # 按分類分組
            by_cat = defaultdict(list)
            for item in items:
                by_cat[item["category"]].append(item)
            
            # 按原始順序排序（保持 task.md 的順序）
            for cat in sorted(by_cat.keys()):
                probs = by_cat[cat]
                f.write(f"## {cat}\n\n")
                for p in probs:
                    # 生成相對路徑連結
                    rel_path = f"../{p['path']}"
                    f.write(f"- [{p['name']}]({rel_path})\n")
                f.write("\n")
        
        print(f"✅ 已生成：{output} ({len(items)} 題)")

def create_symlinks():
    """在 docs/solutions/ 建立符號連結（可選）"""
    # 這步驟可選，因為相對路徑已經可以直接連到原始檔案
    pass

if __name__ == "__main__":
    print("🔍 正在解析 task.md...")
    problems = parse_task_md()
    
    total = sum(len(items) for items in problems.values())
    print(f"📊 找到 {total} 道已完成題目：")
    for diff, items in problems.items():
        print(f"   - {diff}: {len(items)} 題")
    
    print("\n📝 生成難度索引頁...")
    generate_difficulty_pages(problems)
    
    print("\n✨ 完成！")
