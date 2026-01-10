#!/usr/bin/env python3
"""
從 task.md 自動生成：
1. 按難度分類的索引頁 (by-difficulty/*.md)
2. 按類別分類的索引頁 (by-category/*.md)
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
    pattern = r"- \[x\] \[([^\]]+)\]\(([^\)]+)\)\s*<!--\s*(\w+)\s*\S*\s*-->"
    # Note: \s*\S*\s* handles optional "⭐" or other markers
    matches = re.findall(pattern, content)
    
    problems = {"Easy": [], "Medium": [], "Hard": []}
    by_category = defaultdict(list)
    
    for name, path, difficulty in matches:
        # 提取分類資料
        # path example: 01_Arrays_and_Hashing/01_Contains_Duplicate.md
        parts = path.split("/")
        if len(parts) >= 2:
            dir_name = parts[0] # 01_Arrays_and_Hashing
            
            # Category Name: "Arrays & Hashing"
            category_name = dir_name.split("_", 1)[1].replace("_", " ")
            
            # Filename for index: "01-arrays-hashing.md"
            slug = dir_name.lower().replace("_", "-")
            
            item = {
                "name": name,
                "path": path,
                "category": category_name,
                "dir_name": dir_name,
                "slug": slug,
                "difficulty": difficulty
            }
            
            problems[difficulty].append(item)
            by_category[slug].append(item)
            
    return problems, by_category

def generate_difficulty_pages(problems):
    """生成三個難度索引頁"""
    difficulty_info = {
        "Easy": {"icon": "📗", "desc": "建議先完成所有 Easy 題目，建立基礎並熟悉常見模式。"},
        "Medium": {"icon": "📙", "desc": "挑戰中等難度題目，深入理解演算法優化技巧。"},
        "Hard": {"icon": "📕", "desc": "攻克高難度題目，掌握進階技巧與複雜設計。"}
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
            
            # 按原始目錄順序排序
            # 我們需要一個 map: category_name -> dir_name 來排序
            cat_sort_key = {}
            for item in items:
                cat_sort_key[item["category"]] = item["dir_name"]

            for cat in sorted(by_cat.keys(), key=lambda x: cat_sort_key[x]):
                probs = by_cat[cat]
                f.write(f"## {cat}\n\n")
                for p in probs:
                    rel_path = f"../{p['path']}"
                    f.write(f"- [{p['name']}]({rel_path}) {{: .{p['difficulty'].lower()} }}\n")
                f.write("\n")
        
        print(f"✅ 難度索引：{output} ({len(items)} 題)")

def generate_category_pages(by_category):
    """生成類別索引頁"""
    
    # 手動維護順序（也可以從 task.md 解析，這裡簡單處理）
    # 實際上可以直接用 slug 排序，因為我們有 01, 02...
    
    sorted_slugs = sorted(by_category.keys())
    
    # 建立 Previous / Next 鏈結
    prev_map = {}
    next_map = {}
    for i in range(len(sorted_slugs)):
        curr = sorted_slugs[i]
        if i > 0:
            prev_map[curr] = sorted_slugs[i-1]
        if i < len(sorted_slugs) - 1:
            next_map[curr] = sorted_slugs[i+1]

    for slug, items in by_category.items():
        if not items:
            continue
            
        category_name = items[0]["category"]
        output = Path(f"docs/by-category/{slug}.md")
        output.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output, "w", encoding="utf-8") as f:
            f.write(f"# {category_name}\n\n")
            f.write(f"> 此模組共有 {len(items)} 道題目。\n\n")
            f.write("---\n\n")
            f.write("## 題目列表\n\n")
            
            for p in items:
                rel_path = f"../{p['path']}"
                diff_class = p['difficulty'].lower()
                
                f.write(f"### [{p['name']}]({rel_path}) {{: .{diff_class} }}\n")
                f.write(f"**難度**：{p['difficulty']}\n\n")
                f.write("---\n\n")
                
            # Navigation Footer
            f.write("## 導航\n\n")
            nav_links = []
            
            if slug in prev_map:
                p_slug = prev_map[slug]
                # 取得前一個分類名稱 (有點冗餘但為了顯示)
                p_name = by_category[p_slug][0]["category"]
                nav_links.append(f"⬅️ 上一章：[{p_name}]({p_slug}.md)")
            else:
                nav_links.append("⬅️ 上一章：無")
                
            if slug in next_map:
                n_slug = next_map[slug]
                n_name = by_category[n_slug][0]["category"]
                nav_links.append(f"下一章：[{n_name}]({n_slug}.md) ➡️")
            else:
                nav_links.append("下一章：無 ➡️")
                
            f.write(f"{' | '.join(nav_links)}\n")
            
        print(f"✅ 分類索引：{output} ({len(items)} 題)")

if __name__ == "__main__":
    print("🔍 正在解析 task.md...")
    problems, by_cat = parse_task_md()
    
    generate_difficulty_pages(problems)
    generate_category_pages(by_cat)
    
    print("\n✨ 所有索引頁生成完成！")
