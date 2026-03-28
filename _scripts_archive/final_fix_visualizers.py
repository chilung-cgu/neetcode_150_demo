#!/usr/bin/env python3
"""
最終修復：為所有缺失圖例和複雜度的視覺化器添加這些元素。
採用更直接的方式：在 </div> 結束的 viz-card 區塊中添加。
"""
from __future__ import annotations

import re
from pathlib import Path

LEGEND_HTML = '''
                <div class="legend">
                    <div class="legend-item"><div class="legend-color normal"></div>一般</div>
                    <div class="legend-item"><div class="legend-color current"></div>目前處理</div>
                    <div class="legend-item"><div class="legend-color in-stack"></div>完成</div>
                </div>'''

COMPLEXITY_HTML = '''
                <div class="complexity-badge">
                    <span class="label">Time:</span> O(n)
                    <span class="label" style="margin-left: 12px;">Space:</span> O(n)
                </div>'''

# 缺少圖例的視覺化器列表
MISSING_FILES = [
    "docs/01_Arrays_and_Hashing/product_of_array_visualizer.html",
    "docs/04_Stack/daily_temperatures_visualizer.html",
    "docs/06_Linked_List/merge_k_lists_visualizer.html",
    "docs/07_Trees/construct_tree_visualizer.html",
    "docs/07_Trees/invert_tree_visualizer.html",
    "docs/07_Trees/level_order_visualizer.html",
    "docs/07_Trees/right_side_view_visualizer.html",
    "docs/08_Tries/word_dictionary_visualizer.html",
    "docs/09_Heap/twitter_visualizer.html",
    "docs/10_Backtracking/permutations_visualizer.html",
    "docs/15_Graphs/clone_graph_visualizer.html",
    "docs/15_Graphs/course_schedule_ii_visualizer.html",
    "docs/15_Graphs/redundant_connection_visualizer.html",
    "docs/15_Graphs/surrounded_regions_visualizer.html",
    "docs/15_Graphs/walls_gates_visualizer.html",
    "docs/16_Advanced_Graphs/alien_dictionary_visualizer.html",
    "docs/17_Math_Geometry/multiply_strings_visualizer.html",
    "docs/17_Math_Geometry/pow_visualizer.html",
    "docs/17_Math_Geometry/rotate_image_visualizer.html",
    "docs/18_Bit_Manipulation/counting_bits_visualizer.html",
    "docs/18_Bit_Manipulation/single_number_visualizer.html",
]


def fix_file(file_path: Path) -> bool:
    """修復單個視覺化器"""
    if not file_path.exists():
        print(f"  ⚠️ 檔案不存在: {file_path}")
        return False
    
    content = file_path.read_text(encoding="utf-8")
    modified = False
    
    # 添加圖例（在演算法說明 viz-card 前面）
    if "legend" not in content:
        # 找到 "viz-card">.*演算法說明 或 EXPLANATION 的位置
        pattern = r'(</div>\s*</div>\s*)(<div class="viz-card">.*?(?:演算法說明|EXPLANATION))'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            insert_pos = match.start(2)
            content = content[:insert_pos] + LEGEND_HTML + "\n            " + content[insert_pos:]
            modified = True
    
    # 添加複雜度（在控制區後面）
    if "complexity-badge" not in content:
        # 找到 controls 或 speed-control 結束後的位置
        pattern = r'(</select>\s*</div>\s*</div>\s*</div>)'
        match = re.search(pattern, content)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + COMPLEXITY_HTML + content[insert_pos:]
            modified = True
    
    if modified:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    project_root = Path(__file__).parent
    
    print("=" * 60)
    print("🔧 最終修復：添加圖例和複雜度")
    print("=" * 60)
    
    fixed = 0
    for file_path_str in MISSING_FILES:
        file_path = project_root / file_path_str
        if fix_file(file_path):
            fixed += 1
            print(f"  ✅ {file_path.name}")
        else:
            print(f"  ⏭️ 無需修改: {file_path.name}")
    
    print(f"\n✅ 已修復 {fixed} 個視覺化器")


if __name__ == "__main__":
    main()
