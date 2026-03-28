#!/usr/bin/env python3
"""Add final 5 visualizer embeds."""

import os
import re

mappings = {
    "16_Advanced_Graphs/01_Reconstruct_Itinerary.md": "reconstruct_itinerary_visualizer.html",
    "16_Advanced_Graphs/05_Alien_Dictionary.md": "alien_dictionary_visualizer.html",
    "17_Math_Geometry/07_Multiply_Strings.md": "multiply_strings_visualizer.html",
    "17_Math_Geometry/08_Detect_Squares.md": "detect_squares_visualizer.html",
    "18_Bit_Manipulation/07_Reverse_Integer.md": "reverse_integer_visualizer.html",
}

def get_embed_html(visualizer_name):
    return f'''### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../{visualizer_name}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../{visualizer_name}" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation'''

base_dir = '/data/leo/chichi/neetcode_150_demo/docs'
for md_file, vis_file in mappings.items():
    full_path = os.path.join(base_dir, md_file)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'visualizer.html' not in content:
        pattern = r'---\s*\n\n## 4\. 💻 Implementation'
        if re.search(pattern, content):
            new_content = re.sub(pattern, get_embed_html(vis_file), content, count=1)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"OK: {md_file}")
        else:
            print(f"WARN: {md_file}")
    else:
        print(f"SKIP: {md_file}")
