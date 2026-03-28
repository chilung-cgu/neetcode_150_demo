#!/usr/bin/env python3
"""
批次添加相關題目導航區塊到所有 150 個題解。
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Any, List


def load_related_problems(json_path: Path) -> Dict[str, Any]:
    """載入相關題目資料"""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_related_section(
    current_category: str,
    current_problem: str,
    related_data: Dict,
    docs_dir: Path
) -> str:
    """生成相關題目區塊 HTML"""
    if not related_data:
        return ""
    
    internal_links = related_data.get("related", [])
    external_links = related_data.get("related_external", [])
    
    if not internal_links and not external_links:
        return ""
    
    lines = ["\n---\n", "\n## 📚 Related Problems (相關題目)\n", "\n### 站內相關\n"]
    
    # 內部連結
    for ref in internal_links:
        if "/" in ref:
            # 跨分類引用
            cat, prob = ref.split("/", 1)
            md_path = docs_dir / cat / f"{prob}.md"
            if md_path.exists():
                # 提取標題
                content = md_path.read_text(encoding="utf-8")
                title_match = re.search(r'^#\s+(.+?)(?:\s*<span|$)', content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else prob.replace("_", " ")
                lines.append(f"- [{title}](../{cat}/{prob}.md)\n")
        else:
            # 同分類引用
            md_path = docs_dir / current_category / f"{ref}.md"
            if md_path.exists():
                content = md_path.read_text(encoding="utf-8")
                title_match = re.search(r'^#\s+(.+?)(?:\s*<span|$)', content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else ref.replace("_", " ")
                lines.append(f"- [{title}]({ref}.md)\n")
    
    # 外部連結
    if external_links:
        lines.append("\n### 進階挑戰\n")
        for url in external_links:
            # 從 URL 提取題目名稱
            slug = url.rstrip("/").split("/")[-1]
            name = slug.replace("-", " ").title()
            lines.append(f"- [{name}]({url}) — LeetCode\n")
    
    return "".join(lines)


def add_related_problems(file_path: Path, related_data: Dict, docs_dir: Path) -> bool:
    """為單個 .md 檔案添加相關題目區塊"""
    content = file_path.read_text(encoding="utf-8")
    
    # 檢查是否已有相關題目區塊
    if "Related Problems" in content or "相關題目" in content:
        print(f"    ⏭️  已有相關題目: {file_path.name}")
        return False
    
    # 獲取分類和題目名稱
    category = file_path.parent.name
    problem = file_path.stem
    
    # 生成相關題目區塊
    category_data = related_data.get(category, {})
    problem_data = category_data.get(problem, {})
    
    related_section = generate_related_section(category, problem, problem_data, docs_dir)
    
    if not related_section:
        print(f"    ⏭️  無相關題目: {file_path.name}")
        return False
    
    # 在檔案結尾添加
    new_content = content.rstrip() + "\n" + related_section
    file_path.write_text(new_content, encoding="utf-8")
    print(f"    ✅ 已添加相關題目: {file_path.name}")
    return True


def main():
    project_root = Path(__file__).parent
    docs_dir = project_root / "docs"
    json_path = project_root / "related_problems.json"
    
    print("=" * 60)
    print("📚 相關題目導航批次更新工具")
    print("=" * 60)
    
    # 載入資料
    print("\n📖 載入 related_problems.json...")
    related_data = load_related_problems(json_path)
    
    # 批次更新
    updated = 0
    skipped = 0
    
    for category_dir in sorted(docs_dir.iterdir()):
        if not category_dir.is_dir() or not category_dir.name[0].isdigit():
            continue
        
        print(f"\n📁 {category_dir.name}:")
        
        for md_file in sorted(category_dir.glob("*.md")):
            if add_related_problems(md_file, related_data, docs_dir):
                updated += 1
            else:
                skipped += 1
    
    print("\n" + "=" * 60)
    print("📈 更新統計")
    print("=" * 60)
    print(f"  ✅ 已更新: {updated} 個檔案")
    print(f"  ⏭️  已跳過: {skipped} 個檔案")
    print(f"  📊 總計: {updated + skipped}")
    print("=" * 60)


if __name__ == "__main__":
    main()
