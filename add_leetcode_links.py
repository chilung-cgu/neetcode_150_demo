#!/usr/bin/env python3
"""
批次添加 LeetCode 題目連結到所有 150 個題解。
在每個題解的標題下方添加 LeetCode 題號和連結。
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Any


def load_leetcode_mapping(mapping_path: Path) -> Dict[str, Any]:
    """載入 LeetCode 對照表"""
    with open(mapping_path, "r", encoding="utf-8") as f:
        return json.load(f)


def add_leetcode_link(file_path: Path, leetcode_num: int, slug: str) -> bool:
    """
    為單個 .md 檔案添加 LeetCode 連結。
    在第一個 # 標題行的下方添加連結區塊。
    """
    content = file_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    # 檢查是否已有 LeetCode 連結
    if "📌 **LeetCode" in content:
        print(f"    ⏭️  已有連結，跳過: {file_path.name}")
        return False
    
    # 找到第一個 # 標題行
    title_line_idx = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title_line_idx = i
            break
    
    if title_line_idx is None:
        print(f"    ❌ 找不到標題: {file_path.name}")
        return False
    
    # 構建 LeetCode 連結區塊
    leetcode_url = f"https://leetcode.com/problems/{slug}/"
    link_block = f'\n> 📌 **LeetCode #{leetcode_num}** — [題目連結]({leetcode_url}) | [NeetCode 解說](https://neetcode.io/problems/{slug})\n'
    
    # 在標題行後插入連結區塊
    lines.insert(title_line_idx + 1, link_block)
    
    # 寫回檔案
    file_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"    ✅ #{leetcode_num} 已添加: {file_path.name}")
    return True


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    mapping_path = project_root / "leetcode_mapping.json"
    
    print("=" * 60)
    print("🔗 NeetCode 150 LeetCode 連結批次更新工具")
    print("=" * 60)
    
    # 1. 載入對照表
    print("\n📖 載入 leetcode_mapping.json...")
    mapping = load_leetcode_mapping(mapping_path)
    
    total_problems = sum(len(problems) for problems in mapping.values())
    print(f"找到 {total_problems} 個題目的對照資訊。")
    
    # 2. 批次更新每個檔案
    print("\n🔄 開始批次更新...")
    updated = 0
    skipped = 0
    failed = 0
    
    for category, problems in mapping.items():
        print(f"\n📁 {category}:")
        for problem_name, info in problems.items():
            file_path = docs_dir / category / f"{problem_name}.md"
            
            if not file_path.exists():
                print(f"    ⚠️  檔案不存在: {file_path}")
                failed += 1
                continue
            
            leetcode_num = info["leetcode_num"]
            slug = info["slug"]
            
            if add_leetcode_link(file_path, leetcode_num, slug):
                updated += 1
            else:
                skipped += 1
    
    # 3. 輸出統計
    print("\n" + "=" * 60)
    print("📈 更新統計")
    print("=" * 60)
    print(f"  ✅ 已更新: {updated} 個檔案")
    print(f"  ⏭️  已跳過: {skipped} 個檔案")
    print(f"  ❌ 失敗: {failed} 個檔案")
    print(f"  📊 總計: {updated + skipped + failed} / {total_problems}")
    print("=" * 60)
    
    # 驗證
    if updated + skipped == total_problems and failed == 0:
        print("\n✅ 驗證通過：150/150 檔案處理完成！")
        return 0
    else:
        print(f"\n⚠️  驗證失敗：預期 {total_problems}，實際 {updated + skipped + failed}")
        return 1


if __name__ == "__main__":
    exit(main())
