#!/usr/bin/env python3
"""
批次更新所有 150 個視覺化器 HTML，添加自動播放按鈕和速度控制。
"""
from __future__ import annotations

import re
from pathlib import Path


def update_visualizer_html(file_path: Path) -> bool:
    """
    為單個視覺化器 HTML 添加自動播放控制。
    在現有 controls div 中添加自動播放按鈕和速度控制。
    """
    content = file_path.read_text(encoding="utf-8")
    
    # 檢查是否已有自動播放按鈕
    if 'id="playBtn"' in content:
        print(f"    ⏭️  已有播放按鈕，跳過: {file_path.name}")
        return False
    
    # 策略 1: 找到重置按鈕並在其後添加
    # 尋找 ↻ 重置 或 ↻ 重置 按鈕
    reset_btn_pattern = r'(<button[^>]*onclick="resetVisualization\(\)"[^>]*>↻\s*重置</button>)'
    
    if re.search(reset_btn_pattern, content):
        # 添加自動播放按鈕和速度控制
        replacement = r'''\1
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
        
        new_content = re.sub(reset_btn_pattern, replacement, content)
        file_path.write_text(new_content, encoding="utf-8")
        print(f"    ✅ 已添加播放控制: {file_path.name}")
        return True
    
    # 策略 2: 尋找 controls div 結尾
    controls_end_pattern = r'(</div>\s*)(.*?<div class="state-grid">)'
    match = re.search(controls_end_pattern, content, re.DOTALL)
    
    if match:
        # 嘗試在 controls 結尾後添加第二行控制
        controls_row_2 = '''
                <div class="controls-row-2">
                    <button class="viz-btn play-btn" id="playBtn" onclick="viz.toggleAutoPlay()">▶ 自動播放</button>
                    <div class="speed-control">
                        <label>速度:</label>
                        <select id="speedSelect" onchange="viz.setSpeed(Number(this.value))">
                            <option value="2000">0.5x</option>
                            <option value="1500" selected>1x</option>
                            <option value="1000">1.5x</option>
                            <option value="500">2x</option>
                        </select>
                    </div>
                </div>
'''
        # 找到 controls div 結尾
        controls_pattern = r'(class="controls"[^>]*>.*?)(</div>)(\s*<div class="state-grid">)'
        
        def add_controls_row_2(m):
            return m.group(1) + m.group(2) + controls_row_2 + m.group(3)
        
        new_content = re.sub(controls_pattern, add_controls_row_2, content, flags=re.DOTALL)
        
        if new_content != content:
            file_path.write_text(new_content, encoding="utf-8")
            print(f"    ✅ 已添加第二行控制: {file_path.name}")
            return True
    
    print(f"    ⚠️  無法識別結構: {file_path.name}")
    return False


def find_all_visualizers(docs_dir: Path) -> list:
    """找到所有視覺化器 HTML 檔案"""
    visualizers = []
    for category_dir in docs_dir.iterdir():
        if category_dir.is_dir() and category_dir.name.startswith(("0", "1")):
            for html_file in category_dir.glob("*_visualizer.html"):
                visualizers.append(html_file)
            for html_file in category_dir.glob("*visualizer.html"):
                if html_file not in visualizers:
                    visualizers.append(html_file)
    return sorted(visualizers)


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    
    print("=" * 60)
    print("🎬 視覺化器自動播放功能批次更新工具")
    print("=" * 60)
    
    # 1. 找到所有視覺化器
    print("\n🔍 掃描視覺化器檔案...")
    visualizers = find_all_visualizers(docs_dir)
    print(f"找到 {len(visualizers)} 個視覺化器。")
    
    # 2. 批次更新
    print("\n🔄 開始批次更新...")
    updated = 0
    skipped = 0
    failed = 0
    
    for viz_file in visualizers:
        result = update_visualizer_html(viz_file)
        if result:
            updated += 1
        elif "已有" in str(result) or result is False:
            # 已跳過的情況
            skipped += 1
    
    # 重新計算 (因為有些可能是 failed)
    # 手動修正一下邏輯
    total = len(visualizers)
    failed = total - updated - skipped
    
    # 3. 輸出統計
    print("\n" + "=" * 60)
    print("📈 更新統計")
    print("=" * 60)
    print(f"  ✅ 已更新: {updated} 個檔案")
    print(f"  ⏭️  已跳過: {skipped} 個檔案")
    print(f"  ⚠️  需手動: {failed} 個檔案")
    print(f"  📊 總計: {total}")
    print("=" * 60)
    
    return 0


if __name__ == "__main__":
    exit(main())
