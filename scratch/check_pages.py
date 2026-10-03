import os
import re

for filename in ['index.html', 'about.html', 'services.html', 'pricing.html', 'contact.html']:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
            print(f"=== {filename} ===")
            for img in imgs[:8]:
                print(f"  {img}")
