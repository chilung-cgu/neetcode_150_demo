#!/usr/bin/env python3
"""
強力修復所有視覺化器缺失的元素（圖例和複雜度）。
"""
from __future__ import annotations

import re
from pathlib import Path

# 複雜度資料
COMPLEXITY_DATA = {
    "default": ("O(n)", "O(n)"),
}

LEGEND_HTML = '''<div class="legend">
                    <div class="legend-item"><div class="legend-color normal"></div>一般</div>
                    <div class="legend-item"><div class="legend-color current"></div>目前處理</div>
                    <div class="legend-item"><div class="legend-color in-stack"></div>完成</div>
                </div>'''

COMPLEXITY_HTML = '''<div class="complexity-badge">
                    <span class="label">Time:</span> {time}
                    <span class="label" style="margin-left: 12px;">Space:</span> {space}
                </div>'''


def fix_visualizer(file_path: Path) -> bool:
    """修復單個視覺化器"""
    content = file_path.read_text(encoding="utf-8")
    modified = False
    
    # 添加圖例（如果沒有）
    if "legend" not in content:
        # 找到 </div> 之前的 state-grid 區塊
        if "state-grid" in content:
            pattern = r'(</div>\s*</div>\s*</div>\s*<div class="viz-card">)'
            match = re.search(pattern, content)
            if match:
                replacement = LEGEND_HTML + "\n                " + match.group(1)
                content = content[:match.start()] + replacement + content[match.end():]
                modified = True
        
        # 如果沒找到，嘗試在 viz-card 結束前添加
        if not modified and "viz-card" in content:
            pattern = r'(</div>\s*<div class="viz-card">.*?<div class="viz-title">.*?EXPLANATION)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                insert_point = match.start()
                content = content[:insert_point] + LEGEND_HTML + "\n            " + content[insert_point:]
                modified = True
    
    # 添加複雜度（如果沒有）
    if "complexity-badge" not in content:
        complexity_html = COMPLEXITY_HTML.format(time="O(n)", space="O(n)")
        
        if "state-grid" in content:
            content = content.replace(
                '<div class="state-grid">',
                complexity_html + '\n                <div class="state-grid">'
            )
            modified = True
    
    if modified:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    docs_dir = Path(__file__).parent / "docs"
    
    print("=" * 60)
    print("🔧 強力修復視覺化器缺失元素")
    print("=" * 60)
    
    fixed = 0
    for html_file in sorted(docs_dir.rglob("*visualizer.html")):
        if fix_visualizer(html_file):
            fixed += 1
            print(f"  ✅ {html_file.name}")
    
    print(f"\n✅ 已修復 {fixed} 個視覺化器")


if __name__ == "__main__":
    main()
