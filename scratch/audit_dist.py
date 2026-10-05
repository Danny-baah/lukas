import os
import glob
import re

print("=== DIST AUDIT ===")
html_files = glob.glob('dist/*.html')
print(f"Total HTML files in dist: {len(html_files)}")
for hf in sorted(html_files):
    name = os.path.basename(hf)
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    comments = re.findall(r'<!--[\s\S]*?-->', content)
    has_logo = 'Schlüsselnotdienst' in content
    print(f"  {name:18} | Size: {os.path.getsize(hf):6} B | Comments: {len(comments):2} | Has 'Schlüsselnotdienst': {has_logo}")

maps = glob.glob('dist/**/*.map', recursive=True)
print(f"Sourcemaps in dist: {len(maps)}")

htaccess_path = 'dist/.htaccess'
print(f".htaccess exists in dist: {os.path.exists(htaccess_path)}")
if os.path.exists(htaccess_path):
    print("  .htaccess size:", os.path.getsize(htaccess_path), "bytes")

print("=== AUDIT COMPLETE ===")
