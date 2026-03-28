#!/usr/bin/env python3
"""
修復剩餘 18 個特殊結構的視覺化器，添加自動播放按鈕。
採用更通用的策略：在 </script> 之前插入播放按鈕相關程式碼。
"""
from __future__ import annotations

import re
from pathlib import Path

# 需要手動修復的 18 個視覺化器
SPECIAL_VISUALIZERS = [
    "docs/05_Binary_Search/median_arrays_visualizer.html",
    "docs/05_Binary_Search/time_map_visualizer.html",
    "docs/06_Linked_List/copy_random_visualizer.html",
    "docs/06_Linked_List/reorder_list_visualizer.html",
    "docs/07_Trees/serialize_tree_visualizer.html",
    "docs/08_Tries/word_search_ii_visualizer.html",
    "docs/10_Backtracking/palindrome_partition_visualizer.html",
    "docs/10_Backtracking/subsets_ii_visualizer.html",
    "docs/13_Greedy/partition_labels_visualizer.html",
    "docs/14_Intervals/min_interval_query_visualizer.html",
    "docs/16_Advanced_Graphs/reconstruct_itinerary_visualizer.html",
    "docs/17_Math_Geometry/plus_one_visualizer.html",
    "docs/17_Math_Geometry/set_matrix_zeroes_visualizer.html",
    "docs/18_Bit_Manipulation/reverse_integer_visualizer.html",
]


def add_play_button_to_controls(file_path: Path) -> bool:
    """添加播放按鈕和速度控制到 controls 區塊（通用策略）"""
    content = file_path.read_text(encoding="utf-8")
    
    # 檢查是否已有播放按鈕
    if 'id="playBtn"' in content:
        print(f"    ⏭️  已有播放按鈕: {file_path.name}")
        return False
    
    # 策略：找到 Reset/重置 按鈕行並在其後添加
    patterns = [
        r'(onclick="resetVisualization\(\)"[^>]*>[^<]*</button>)',  # 匹配重置按鈕
        r'(onclick="init\(\)"[^>]*>[^<]*</button>)',  # 有些用 init()
    ]
    
    play_button_code = '''
                    <button class="viz-btn play-btn" id="playBtn" onclick="viz.toggleAutoPlay()">▶ 自動播放</button>
                    <div class="speed-control">
                        <label>速度:</label>
                        <select id="speedSelect" onchange="viz.setSpeed(Number(this.value))">
                            <option value="2000">0.5x</option>
                            <option value="1500" selected>1x</option>
                            <option value="1000">1.5x</option>
                            <option value="500">2x</option>
                        </select>
                    </div>'''
    
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            new_content = re.sub(pattern, r'\1' + play_button_code, content, count=1, flags=re.IGNORECASE)
            if new_content != content:
                file_path.write_text(new_content, encoding="utf-8")
                print(f"    ✅ 已修復: {file_path.name}")
                return True
    
    # 備用策略：在 </div>.*?controls 後面的第一個 </div> 前插入
    # 尋找 class="controls" 區塊
    def add_before_div_close(match):
        return match.group(1) + play_button_code + '\n                </div>'
    
    controls_pattern = r'(class="controls"[^>]*>.*?<button[^>]*>[^<]*</button>.*?<button[^>]*>[^<]*</button>.*?<button[^>]*>[^<]*</button>)\s*</div>'
    new_content = re.sub(controls_pattern, add_before_div_close, content, count=1, flags=re.DOTALL)
    
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"    ✅ 已修復 (備用策略): {file_path.name}")
        return True
    
    print(f"    ⚠️  無法修復: {file_path.name}")
    return False


def main():
    project_root = Path(__file__).parent
    
    print("=" * 60)
    print("🔧 修復特殊結構視覺化器")
    print("=" * 60)
    
    fixed = 0
    for viz_path in SPECIAL_VISUALIZERS:
        file_path = project_root / viz_path
        if file_path.exists():
            if add_play_button_to_controls(file_path):
                fixed += 1
        else:
            print(f"    ❌ 檔案不存在: {viz_path}")
    
    print("\n" + "=" * 60)
    print(f"📈 修復了 {fixed}/{len(SPECIAL_VISUALIZERS)} 個特殊視覺化器")
    print("=" * 60)


if __name__ == "__main__":
    main()
