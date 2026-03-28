#!/usr/bin/env python3
"""Script to add remaining visualizer embeds to markdown files."""

import os
import re

# Additional mappings for missing files
mappings = {
    # Linked List
    "06_Linked_List/06_Add_Two_Numbers.md": "add_two_numbers_visualizer.html",
    # Graphs
    "15_Graphs/11_Number_of_Connected_Components.md": "connected_components_visualizer.html",
    "15_Graphs/12_Graph_Valid_Tree.md": "valid_tree_visualizer.html",
    # Math
    "17_Math_Geometry/03_Set_Matrix_Zeroes.md": "set_matrix_zeroes_visualizer.html",
    "17_Math_Geometry/04_Happy_Number.md": "happy_number_visualizer.html",
    "17_Math_Geometry/05_Plus_One.md": "plus_one_visualizer.html",
    "17_Math_Geometry/06_Pow.md": "pow_visualizer.html",
    # Bit Manipulation
    "18_Bit_Manipulation/02_Number_of_1_Bits.md": "count_bits_visualizer.html",
    "18_Bit_Manipulation/04_Reverse_Bits.md": "reverse_bits_visualizer.html",
    "18_Bit_Manipulation/05_Missing_Number.md": "missing_number_visualizer.html",
    "18_Bit_Manipulation/06_Sum_of_Two_Integers.md": "sum_two_integers_visualizer.html",
}

def get_embed_html(visualizer_name):
    return f'''### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../{visualizer_name}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../{visualizer_name}" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation'''

def process_file(md_path, vis_name, base_dir):
    full_path = os.path.join(base_dir, md_path)
    if not os.path.exists(full_path):
        print(f"SKIP: {md_path} (file not found)")
        return False
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'visualizer.html' in content:
        print(f"SKIP: {md_path} (already has visualizer)")
        return False
    
    pattern = r'---\s*\n\n## 4\. 💻 Implementation'
    replacement = get_embed_html(vis_name)
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, replacement, content, count=1)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"OK: {md_path}")
        return True
    else:
        print(f"WARN: {md_path} (pattern not found)")
        return False

if __name__ == '__main__':
    base_dir = '/data/leo/chichi/neetcode_150_demo/docs'
    success = 0
    for md_file, vis_file in mappings.items():
        if process_file(md_file, vis_file, base_dir):
            success += 1
    print(f"\nProcessed {success} files successfully")
