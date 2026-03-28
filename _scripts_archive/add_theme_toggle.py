#!/usr/bin/env python3
"""
批次為所有視覺化器添加主題切換按鈕。
"""
from __future__ import annotations

import re
from pathlib import Path


def add_theme_toggle(file_path: Path) -> bool:
    """為視覺化器添加主題切換按鈕"""
    content = file_path.read_text(encoding="utf-8")
    
    if 'theme-toggle' in content:
        return False
    
    # 在 <body> 開頭添加主題切換按鈕
    theme_button = '''<body>
    <button class="theme-toggle" onclick="AlgorithmVisualizer.toggleTheme()" title="切換主題">🌓</button>'''
    
    new_content = content.replace('<body>', theme_button)
    
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    docs_dir = Path(__file__).parent / "docs"
    
    print("=" * 60)
    print("🌓 添加主題切換按鈕到視覺化器")
    print("=" * 60)
    
    updated = 0
    for category_dir in docs_dir.iterdir():
        if not category_dir.is_dir() or not category_dir.name[0].isdigit():
            continue
        for html_file in category_dir.glob("*visualizer.html"):
            if add_theme_toggle(html_file):
                updated += 1
                print(f"  ✅ {html_file.name}")
    
    print(f"\n✅ 已更新 {updated} 個視覺化器")


if __name__ == "__main__":
    main()
