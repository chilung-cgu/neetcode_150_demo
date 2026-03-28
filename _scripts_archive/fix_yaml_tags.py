#!/usr/bin/env python3
"""
修復所有題解的 YAML Front Matter tags 格式問題。
"""
from __future__ import annotations

import re
from pathlib import Path


def fix_yaml_tags(file_path: Path) -> bool:
    """修復 YAML tags 格式"""
    content = file_path.read_text(encoding="utf-8")
    
    # 檢查是否有問題的格式
    # 錯誤格式: "tags:\n  - \nArray  - Hash Table"
    # 正確格式: "tags:\n  - Array\n  - Hash Table"
    
    pattern = r'tags:\n  - \n([^\n]+)'
    
    def fix_tags(match):
        tags_line = match.group(1)
        # 分割 tags（以 "  - " 分隔）
        tags = [t.strip() for t in re.split(r'\s+-\s+', tags_line) if t.strip()]
        if tags:
            return 'tags:\n' + '\n'.join([f'  - {tag}' for tag in tags])
        return match.group(0)
    
    new_content = re.sub(pattern, fix_tags, content)
    
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    
    print("=" * 60)
    print("🔧 修復 YAML Tags 格式")
    print("=" * 60)
    
    fixed = 0
    for category_dir in sorted(docs_dir.iterdir()):
        if not category_dir.is_dir() or not category_dir.name[0].isdigit():
            continue
        
        for md_file in sorted(category_dir.glob("*.md")):
            if fix_yaml_tags(md_file):
                fixed += 1
                print(f"  ✅ {md_file.name}")
    
    print(f"\n✅ 已修復 {fixed} 個檔案")


if __name__ == "__main__":
    main()
