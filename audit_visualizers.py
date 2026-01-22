import os
import re

DOCS_DIR = '/data/leo/chichi/neetcode_150_demo/docs'
OUTPUT_FILE = 'visualizer_quality_report.md'

features_check = {
    'Interactive': [r'custom-input-section', r'runCustomInput', r'setExample', r'<input'],
    'Dynamic': [r'generateAlgorithmSteps', r'generateSteps', r'function generate'],
    'Complexity': [r'complexity-badge'],
    'Explanation': [r'explanation', r'id="explanation"'],
    'CoreJS': [r'core\.js'],
    'Controls': [r'prevBtn', r'nextBtn']
}

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {}
    for feature, patterns in features_check.items():
        results[feature] = any(re.search(p, content) for p in patterns)
    
    return results

def main():
    files = []
    for root, dirs, filenames in os.walk(DOCS_DIR):
        for f in filenames:
            if f.endswith('_visualizer.html'):
                files.append(os.path.join(root, f))
    
    files.sort()
    
    print(f"Checking {len(files)} files...")
    
    report_lines = []
    report_lines.append("# 視覺化器高標準逐一檢測報告")
    report_lines.append(f"\n檢測總數: {len(files)}\n")
    report_lines.append("| ID | 檔案 | 互動性 | 動態生成 | 複雜度 | 解說 | CoreJS | 狀態 |")
    report_lines.append("|---|---|---|---|---|---|---|---|")
    
    pass_count = 0
    
    for idx, filepath in enumerate(files, 1):
        rel_path = os.path.relpath(filepath, DOCS_DIR)
        name = os.path.basename(filepath)
        res = check_file(filepath)
        
        all_pass = all(res.values())
        status = "✅" if all_pass else "❌"
        if all_pass:
            pass_count += 1
            
        row = f"| {idx} | {name} | {'✅' if res['Interactive'] else '❌'} | {'✅' if res['Dynamic'] else '❌'} | {'✅' if res['Complexity'] else '❌'} | {'✅' if res['Explanation'] else '❌'} | {'✅' if res['CoreJS'] else '❌'} | {status} |"
        report_lines.append(row)

    report_lines.append(f"\n**合格統計**: {pass_count}/{len(files)}")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
        
    print(f"Report generated at {OUTPUT_FILE}")
    print(f"Pass rate: {pass_count}/{len(files)}")
    if pass_count != len(files):
        print("Some files failed the check.")

if __name__ == '__main__':
    main()
