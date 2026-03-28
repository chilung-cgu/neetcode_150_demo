#!/usr/bin/env python3
"""
批次添加面試技巧區塊到所有 150 個題解。
在每個題解的「複雜度分析」章節後添加面試技巧區塊。
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Any, Optional


def load_interview_tips(tips_path: Path) -> Dict[str, Any]:
    """載入面試技巧資料庫"""
    if tips_path.exists():
        with open(tips_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def generate_tips_block(problem_name: str, tips_data: Optional[Dict]) -> str:
    """根據題目資料生成面試技巧區塊"""
    
    if tips_data:
        follow_ups = tips_data.get("follow_ups", [])
        red_flags = tips_data.get("red_flags", [])
        bonus_points = tips_data.get("bonus_points", [])
        high_freq = tips_data.get("high_freq", False)
    else:
        # 通用模板
        follow_ups = ["你會如何處理更大的輸入？", "有沒有更好的空間複雜度？"]
        red_flags = ["沒有考慮邊界條件", "未討論複雜度"]
        bonus_points = ["主動討論 trade-offs", "提供多種解法比較"]
        high_freq = False
    
    high_freq_badge = " ⭐ 高頻題" if high_freq else ""
    
    follow_ups_md = "\n".join([f"- {q}" for q in follow_ups])
    red_flags_md = "\n".join([f"- ⚠️ {r}" for r in red_flags])
    bonus_points_md = "\n".join([f"- 💎 {b}" for b in bonus_points])
    
    return f"""
---

## 7. 💼 Interview Tips (面試技巧){high_freq_badge}

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

{follow_ups_md}

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

{red_flags_md}

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

{bonus_points_md}
"""


def add_interview_tips(file_path: Path, tips_data: Optional[Dict]) -> bool:
    """為單個 .md 檔案添加面試技巧區塊"""
    content = file_path.read_text(encoding="utf-8")
    
    # 檢查是否已有面試技巧區塊
    if "Interview Tips" in content or "面試技巧" in content:
        print(f"    ⏭️  已有面試技巧: {file_path.name}")
        return False
    
    # 生成面試技巧區塊
    problem_name = file_path.stem
    tips_block = generate_tips_block(problem_name, tips_data)
    
    # 在檔案結尾添加
    new_content = content.rstrip() + "\n" + tips_block
    
    file_path.write_text(new_content, encoding="utf-8")
    print(f"    ✅ 已添加面試技巧: {file_path.name}")
    return True


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    tips_path = project_root / "interview_tips.json"
    
    print("=" * 60)
    print("💼 面試技巧區塊批次更新工具")
    print("=" * 60)
    
    # 1. 載入面試技巧資料庫
    print("\n📖 載入 interview_tips.json...")
    all_tips = load_interview_tips(tips_path)
    
    # 2. 找到所有題解
    updated = 0
    skipped = 0
    
    # 遍歷所有分類目錄
    for category_dir in sorted(docs_dir.iterdir()):
        if not category_dir.is_dir() or not category_dir.name[0].isdigit():
            continue
        
        category_name = category_dir.name
        category_tips = all_tips.get(category_name, {})
        
        print(f"\n📁 {category_name}:")
        
        # 遍歷分類中的所有題解
        for md_file in sorted(category_dir.glob("*.md")):
            problem_name = md_file.stem
            problem_tips = category_tips.get(problem_name, None)
            
            if add_interview_tips(md_file, problem_tips):
                updated += 1
            else:
                skipped += 1
    
    # 3. 輸出統計
    print("\n" + "=" * 60)
    print("📈 更新統計")
    print("=" * 60)
    print(f"  ✅ 已更新: {updated} 個檔案")
    print(f"  ⏭️  已跳過: {skipped} 個檔案")
    print(f"  📊 總計: {updated + skipped}")
    print("=" * 60)
    
    return 0 if updated + skipped >= 150 else 1


if __name__ == "__main__":
    exit(main())
