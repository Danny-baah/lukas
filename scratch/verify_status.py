import re

files = ['index.html', 'ueber-uns.html', 'leistungen.html', 'preise.html', 'kontakt.html', 'impressum.html', 'datenschutz.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    title = re.search(r'<title>(.*?)</title>', c)
    title_txt = title.group(1) if title else 'None'
    brand_main = re.search(r'class="brand-main">(.*?)</span>', c)
    brand_txt = brand_main.group(1) if brand_main else 'None'
    footer_main = re.search(r'class="footer-brand-main">(.*?)</span>', c)
    foot_txt = footer_main.group(1) if footer_main else 'None'
    active_nav = re.findall(r'class="nav-item active">(.*?)</a>', c)
    print(f'{f}: title="{title_txt}" | logo="{brand_txt}" | footer="{foot_txt}" | active={active_nav}')
