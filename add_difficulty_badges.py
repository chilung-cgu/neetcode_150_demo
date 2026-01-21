#!/usr/bin/env python3
"""
為 NeetCode 150 所有題目頁面添加難易度 Badge。
從 task.md 讀取難度資訊，批次更新每個 .md 檔案的標題。
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Dict

# 難度對應的 Badge 樣式
DIFFICULTY_BADGES = {
    "Easy": '<span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>',
    "Medium": '<span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>',
    "Hard": '<span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>',
}


def parse_task_md(task_md_path: Path) -> Dict[str, str]:
    """
    解析 task.md，提取每個題目的難度。
    返回 {檔案相對路徑: 難度} 的對應表。
    """
    content = task_md_path.read_text(encoding="utf-8")
    
    # 匹配格式: [題目名稱](路徑.md) <!-- Easy/Medium/Hard -->
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)\s*<!--\s*(Easy|Medium|Hard)(?:\s*⭐)?\s*-->'
    
    difficulty_map = {}
    for match in re.finditer(pattern, content):
        title = match.group(1)
        file_path = match.group(2)
        difficulty = match.group(3)
        difficulty_map[file_path] = difficulty
        print(f"  ✓ {file_path}: {difficulty}")
    
    return difficulty_map


def add_badge_to_file(file_path: Path, difficulty: str) -> bool:
    """
    為單個 .md 檔案添加難度 Badge。
    返回是否有進行修改。
    """
    content = file_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    if not lines:
        return False
    
    # 找到第一個 # 開頭的標題行
    for i, line in enumerate(lines):
        if line.startswith("# "):
            # 檢查是否已有 Badge
            if '<span style="background:' in line:
                print(f"    ⏭️ 已有 Badge，跳過: {file_path.name}")
                return False
            
            # 添加 Badge
            badge = DIFFICULTY_BADGES.get(difficulty, "")
            lines[i] = f"{line.rstrip()} {badge}"
            
            # 寫回檔案
            file_path.write_text("\n".join(lines), encoding="utf-8")
            print(f"    ✅ 已添加 {difficulty} Badge: {file_path.name}")
            return True
    
    print(f"    ❌ 找不到標題行: {file_path.name}")
    return False


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    task_md = project_root / "task.md"
    
    print("=" * 60)
    print("📊 NeetCode 150 難度 Badge 批次更新工具")
    print("=" * 60)
    
    # 1. 解析 task.md 獲取難度對應表
    print("\n📖 解析 task.md 中的難度資訊...")
    difficulty_map = parse_task_md(task_md)
    print(f"\n找到 {len(difficulty_map)} 個題目的難度資訊。")
    
    # 2. 批次更新每個檔案
    print("\n🔄 開始批次更新...")
    updated = 0
    skipped = 0
    failed = 0
    
    for rel_path, difficulty in difficulty_map.items():
        file_path = docs_dir / rel_path
        if not file_path.exists():
            print(f"    ⚠️ 檔案不存在: {file_path}")
            failed += 1
            continue
        
        if add_badge_to_file(file_path, difficulty):
            updated += 1
        else:
            skipped += 1
    
    # 3. 輸出統計
    print("\n" + "=" * 60)
    print("📈 更新統計")
    print("=" * 60)
    print(f"  ✅ 已更新: {updated} 個檔案")
    print(f"  ⏭️ 已跳過: {skipped} 個檔案")
    print(f"  ❌ 失敗: {failed} 個檔案")
    print("=" * 60)


if __name__ == "__main__":
    main()
