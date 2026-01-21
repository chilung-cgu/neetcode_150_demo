#!/usr/bin/env python3
"""
從所有 150 題解中提取複雜度資訊，生成複雜度速查表。
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple


def extract_complexity(file_path: Path) -> Tuple[str, str, str, str]:
    """從題解中提取時間和空間複雜度"""
    content = file_path.read_text(encoding="utf-8")
    
    # 提取標題
    title_match = re.search(r'^#\s+(.+?)(?:\s*<span|$)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else file_path.stem
    
    # 提取難度
    difficulty = "Medium"  # 預設
    if "🟢 Easy" in content or "Easy</span>" in content:
        difficulty = "Easy"
    elif "🔴 Hard" in content or "Hard</span>" in content:
        difficulty = "Hard"
    
    # 提取時間複雜度
    time_pattern = r'\*\*Time Complexity\*\*:\s*\$?\\?O?\(?([^$\n]+?)\)?\$?'
    time_match = re.search(time_pattern, content, re.IGNORECASE)
    time_complexity = time_match.group(1).strip() if time_match else "-"
    
    # 備用模式
    if time_complexity == "-":
        time_pattern2 = r'-\s+\*\*Time\*\*:\s*\$?(.+?)\$?\s*$'
        time_match2 = re.search(time_pattern2, content, re.MULTILINE)
        if time_match2:
            time_complexity = time_match2.group(1).strip()
    
    # 提取空間複雜度
    space_pattern = r'\*\*Space Complexity\*\*:\s*\$?\\?O?\(?([^$\n]+?)\)?\$?'
    space_match = re.search(space_pattern, content, re.IGNORECASE)
    space_complexity = space_match.group(1).strip() if space_match else "-"
    
    if space_complexity == "-":
        space_pattern2 = r'-\s+\*\*Space\*\*:\s*\$?(.+?)\$?\s*$'
        space_match2 = re.search(space_pattern2, content, re.MULTILINE)
        if space_match2:
            space_complexity = space_match2.group(1).strip()
    
    return title, difficulty, time_complexity, space_complexity


def generate_cheatsheet(docs_dir: Path) -> str:
    """生成完整的複雜度速查表"""
    output = """# 📊 複雜度速查表

本頁面匯總了 NeetCode 150 所有題目的時間和空間複雜度，方便快速查閱。

---

## 按分類查閱

"""
    
    # 按分類收集資料
    categories: Dict[str, List] = {}
    
    for category_dir in sorted(docs_dir.iterdir()):
        if not category_dir.is_dir() or not category_dir.name[0].isdigit():
            continue
        
        category_name = category_dir.name
        category_display = category_name.replace("_", " ")[3:]  # 移除編號前綴
        categories[category_display] = []
        
        for md_file in sorted(category_dir.glob("*.md")):
            title, difficulty, time_c, space_c = extract_complexity(md_file)
            
            # 生成相對連結
            link = f"[{title}]({category_name}/{md_file.name})"
            
            categories[category_display].append({
                "link": link,
                "difficulty": difficulty,
                "time": time_c,
                "space": space_c,
            })
    
    # 生成表格
    for category, problems in categories.items():
        output += f"### {category}\n\n"
        output += "| 題目 | 難度 | Time | Space |\n"
        output += "|------|------|------|-------|\n"
        
        for p in problems:
            diff_badge = "🟢" if p["difficulty"] == "Easy" else "🟡" if p["difficulty"] == "Medium" else "🔴"
            output += f"| {p['link']} | {diff_badge} {p['difficulty']} | {p['time']} | {p['space']} |\n"
        
        output += "\n---\n\n"
    
    # 添加複雜度總覽
    output += """## 常見複雜度解釋

| 複雜度 | 說明 | 常見場景 |
|--------|------|----------|
| O(1) | 常數時間 | Hash Table 查找 |
| O(log n) | 對數時間 | Binary Search |
| O(n) | 線性時間 | 遍歷陣列一次 |
| O(n log n) | 排序時間 | Merge Sort, Quick Sort |
| O(n²) | 平方時間 | 雙層迴圈、DP 表格 |
| O(2ⁿ) | 指數時間 | 暴力遞迴、Backtracking |
| O(n!) | 階乘時間 | 全排列 |

---

## 空間複雜度提示

- **O(1)**: 只用固定數量的變數
- **O(n)**: 需要額外陣列或 Hash Table
- **O(h)**: 遞迴棧深度，h 為樹高
- **O(m × n)**: 2D DP 表格
"""
    
    return output


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    output_path = docs_dir / "complexity_cheatsheet.md"
    
    print("=" * 60)
    print("📊 生成複雜度速查表")
    print("=" * 60)
    
    cheatsheet = generate_cheatsheet(docs_dir)
    output_path.write_text(cheatsheet, encoding="utf-8")
    
    print(f"✅ 已生成: {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
