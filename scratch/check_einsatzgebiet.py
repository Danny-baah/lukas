import re

with open('index.html', 'r', encoding='utf-8') as f:
    c_index = f.read()
with open('contact.html', 'r', encoding='utf-8') as f:
    c_contact = f.read()

print('=== index.html sections ===')
for m in re.finditer(r'<section[^>]+id=["\']([^"\']+)["\']', c_index):
    print(f"  id: {m.group(1)}")

print('=== contact.html sections ===')
for m in re.finditer(r'<section[^>]+id=["\']([^"\']+)["\']', c_contact):
    print(f"  id: {m.group(1)}")
