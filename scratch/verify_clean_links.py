import re

files = ['index.html', 'ueber-uns.html', 'leistungen.html', 'preise.html', 'kontakt.html', 'impressum.html', 'datenschutz.html']

total_found = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    links = re.findall(r'href=["\']([^"\']*\.html[^"\']*)["\']', c)
    if links:
        print(f"{f}: remaining .html links -> {links}")
        total_found += len(links)

if total_found == 0:
    print("ALL internal links across all pages now use clean URLs without .html!")
