#!/usr/bin/env python3
"""
批次為所有題解添加 YAML Front Matter (meta 描述和 tags)。
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

# 題目分類對應的標籤
CATEGORY_TAGS = {
    "01_Arrays_and_Hashing": ["Array", "Hash Table"],
    "02_Two_Pointers": ["Two Pointers", "Array"],
    "03_Sliding_Window": ["Sliding Window", "String"],
    "04_Stack": ["Stack", "Monotonic Stack"],
    "05_Binary_Search": ["Binary Search", "Array"],
    "06_Linked_List": ["Linked List"],
    "07_Trees": ["Tree", "Binary Tree", "DFS"],
    "08_Tries": ["Trie", "String"],
    "09_Heap": ["Heap", "Priority Queue"],
    "10_Backtracking": ["Backtracking", "Recursion"],
    "11_1D_DP": ["Dynamic Programming"],
    "12_2D_DP": ["Dynamic Programming", "2D DP"],
    "13_Greedy": ["Greedy"],
    "14_Intervals": ["Intervals", "Sorting"],
    "15_Graphs": ["Graph", "DFS", "BFS"],
    "16_Advanced_Graphs": ["Graph", "Dijkstra", "MST"],
    "17_Math_Geometry": ["Math", "Matrix"],
    "18_Bit_Manipulation": ["Bit Manipulation"],
}


def extract_difficulty(content: str) -> str:
    """從內容中提取難度"""
    if "🟢 Easy" in content or "Easy</span>" in content:
        return "Easy"
    elif "🔴 Hard" in content or "Hard</span>" in content:
        return "Hard"
    return "Medium"


def extract_title(content: str) -> str:
    """從內容中提取標題"""
    match = re.search(r'^#\s+(.+?)(?:\s*<span|$)', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "NeetCode 題解"


def add_front_matter(file_path: Path, category: str) -> bool:
    """為 .md 檔案添加 YAML Front Matter"""
    content = file_path.read_text(encoding="utf-8")
    
    # 檢查是否已有 Front Matter
    if content.startswith("---"):
        return False
    
    # 提取資訊
    title = extract_title(content)
    difficulty = extract_difficulty(content)
    tags = CATEGORY_TAGS.get(category, ["Algorithm"])
    tags_str = ", ".join(tags)
    
    # 生成描述 (前 160 字)
    desc_match = re.search(r'Problem Dissection.*?\n\n(.+?)(?:\n\n|---)', content, re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()[:150].replace('\n', ' ')
    else:
        desc = f"{title} - NeetCode 150 題解，{difficulty} 難度"
    
    # 建立 Front Matter
    front_matter = f"""---
title: "{title}"
description: "{desc}"
tags:
  - {chr(10) + '  - '.join(tags)}
difficulty: {difficulty}
---

"""
    
    new_content = front_matter + content
    file_path.write_text(new_content, encoding="utf-8")
    return True


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    
    print("=" * 60)
    print("📝 添加 YAML Front Matter (Meta + Tags)")
    print("=" * 60)
    
    updated = 0
    for category_dir in sorted(docs_dir.iterdir()):
        if not category_dir.is_dir() or not category_dir.name[0].isdigit():
            continue
        
        print(f"\n📁 {category_dir.name}:")
        
        for md_file in sorted(category_dir.glob("*.md")):
            if add_front_matter(md_file, category_dir.name):
                updated += 1
                print(f"  ✅ {md_file.name}")
            else:
                print(f"  ⏭️  已有 Front Matter: {md_file.name}")
    
    print(f"\n✅ 已更新 {updated} 個檔案")


if __name__ == "__main__":
    main()
