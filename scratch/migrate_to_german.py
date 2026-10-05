import os
import re

def process_content(content, page_type):
    # 1. Update Brand Logo in Navbar
    logo_pattern = r'<a href="/" class="brand-logo" aria-label="[^"]*">\s*<img src="/images/mark\.png" alt="[^"]*" class="brand-mark-img" width="14" height="42" />\s*<div class="brand-logotype">\s*<div class="brand-title">\s*<span class="brand-main">[^<]*</span>\s*<span class="brand-accent">[^<]*</span>\s*</div>\s*<span class="brand-sub">[^<]*</span>\s*</div>\s*</a>'
    
    new_logo = '''<a href="/" class="brand-logo" aria-label="Schlüsselnotdienst Rhein-Selz Startseite">
            <img src="/images/mark.png" alt="Schlüsselnotdienst Rhein-Selz Logo" class="brand-mark-img" width="14" height="42" />
            <div class="brand-logotype">
              <div class="brand-title">
                <span class="brand-main">Schlüsselnotdienst</span>
                <span class="brand-accent">Rhein-Selz</span>
              </div>
              <span class="brand-sub">Alles was zugeht, machen wir auch wieder auf</span>
            </div>
          </a>'''
    content = re.sub(logo_pattern, new_logo, content)

    # 2. Update Footer Brand
    footer_brand_pattern = r'<a href="/" class="footer-brand" aria-label="[^"]*">\s*<div class="footer-brand-title">\s*<span class="footer-brand-main">[^<]*</span>\s*<span class="footer-brand-accent-line"[^>]*></span>\s*</div>\s*<div class="footer-brand-sub">\s*<span>[^<]*</span>\s*<span>[^<]*</span>\s*</div>\s*</a>'
    
    new_footer_brand = '''<a href="/" class="footer-brand" aria-label="Schlüsselnotdienst Rhein-Selz Startseite">
              <div class="footer-brand-title">
                <span class="footer-brand-main">SCHLÜSSELNOTDIENST</span>
                <span class="footer-brand-accent-line" aria-hidden="true"></span>
              </div>
              <div class="footer-brand-sub">
                <span>RHEIN-SELZ</span>
                <span>24/7 NOTDIENST &amp; SICHERHEIT</span>
              </div>
            </a>'''
    content = re.sub(footer_brand_pattern, new_footer_brand, content)

    # 3. Update Navigation Links (Desktop)
    nav_links_pattern = r'<div class="nav-links">[\s\S]*?</div>\s*<!-- Right Call Pill Button -->'
    
    # Active states per page
    act_home = ' active' if page_type == 'home' else ''
    act_about = ' active' if page_type == 'about' else ''
    act_services = ' active' if page_type == 'services' else ''
    act_pricing = ' active' if page_type == 'pricing' else ''
    act_contact = ' active' if page_type == 'contact' else ''

    new_nav_links = f'''<div class="nav-links">
            <a href="/" class="nav-item{act_home}">Startseite</a>
            <a href="/ueber-uns.html" class="nav-item{act_about}">Über uns</a>
            <a href="/leistungen.html" class="nav-item{act_services}">Leistungen</a>
            <a href="/preise.html" class="nav-item{act_pricing}">Preise &amp; Ablauf</a>
            <a href="/kontakt.html" class="nav-item{act_contact}">Einsatzgebiet &amp; Kontakt</a>
          </div>

          <!-- Right Call Pill Button -->'''
    content = re.sub(nav_links_pattern, new_nav_links, content)

    # 4. Update Mobile Menu Links
    mobile_menu_pattern = r'<div class="mobile-menu" id="mobileMenu">[\s\S]*?<div class="m-cta-wrap">'
    new_mobile_menu = f'''<div class="mobile-menu" id="mobileMenu">
          <a href="/" class="m-link{act_home}">Startseite</a>
          <a href="/ueber-uns.html" class="m-link{act_about}">Über uns</a>
          <a href="/leistungen.html" class="m-link{act_services}">Leistungen</a>
          <a href="/preise.html" class="m-link{act_pricing}">Preise &amp; Ablauf</a>
          <a href="/kontakt.html" class="m-link{act_contact}">Einsatzgebiet &amp; Kontakt</a>
          <div class="m-cta-wrap">'''
    content = re.sub(mobile_menu_pattern, new_mobile_menu, content)

    # 5. Update footer navigation links
    content = re.sub(r'<a href="/" class="footer-link">Home</a>', r'<a href="/" class="footer-link">Startseite</a>', content)
    content = re.sub(r'<a href="/about\.html" class="footer-link">Über Lukas</a>', r'<a href="/ueber-uns.html" class="footer-link">Über uns</a>', content)
    content = re.sub(r'<a href="/services\.html" class="footer-link">Leistungen</a>', r'<a href="/leistungen.html" class="footer-link">Leistungen</a>', content)
    content = re.sub(r'<a href="/pricing\.html" class="footer-link">Preise &amp; Ablauf</a>', r'<a href="/preise.html" class="footer-link">Preise &amp; Ablauf</a>', content)
    content = re.sub(r'<a href="/contact\.html" class="footer-link">Kontakt</a>', r'<a href="/kontakt.html" class="footer-link">Kontakt</a>', content)
    content = re.sub(r'<a href="/contact\.html" class="footer-link active">Kontakt</a>', r'<a href="/kontakt.html" class="footer-link active">Kontakt</a>', content)
    content = re.sub(r'<a href="/#service-area" class="footer-link">Einsatzgebiet</a>', r'<a href="/kontakt.html#einsatzgebiet" class="footer-link">Einsatzgebiet</a>', content)
    content = re.sub(r'<a href="/#service-area" class="footer-link">Kontakt</a>', r'<a href="/kontakt.html" class="footer-link">Kontakt</a>', content)

    # 6. Global URL replacements
    content = content.replace('href="/about.html"', 'href="/ueber-uns.html"')
    content = content.replace('href="/services.html"', 'href="/leistungen.html"')
    content = content.replace('href="/pricing.html"', 'href="/preise.html"')
    content = content.replace('href="/contact.html"', 'href="/kontakt.html"')
    content = content.replace('href="/services.html#', 'href="/leistungen.html#')
    content = content.replace('href="/contact.html#', 'href="/kontakt.html#')

    # Also replace any remaining "Über Lukas" nav links
    content = content.replace('>Über Lukas<', '>Über uns<')

    return content

# Read original files
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

with open('pricing.html', 'r', encoding='utf-8') as f:
    pricing_content = f.read()

with open('contact.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

with open('impressum.html', 'r', encoding='utf-8') as f:
    impressum_content = f.read()

with open('datenschutz.html', 'r', encoding='utf-8') as f:
    datenschutz_content = f.read()

# Process each
index_processed = process_content(index_content, 'home')
# Update title and meta description
index_processed = re.sub(r'<title>.*?</title>', '<title>Schlüsselnotdienst Rhein-Selz – Sicherheit, die bleibt.</title>', index_processed, count=1)
index_processed = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Schlüsselnotdienst Rhein-Selz – 24/7 Notdienst &amp; professionelle Sicherheitstechnik in Nierstein, Oppenheim und allen 20 Gemeinden der VG Rhein-Selz." />', index_processed, count=1)

about_processed = process_content(about_content, 'about')
about_processed = re.sub(r'<title>.*?</title>', '<title>Über uns – Schlüsselnotdienst Rhein-Selz</title>', about_processed, count=1)
about_processed = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Schlüsselnotdienst Rhein-Selz – Ihr verlässlicher regionaler Partner für Schloss &amp; Riegel in Rhein-Selz und Umgebung." />', about_processed, count=1)

services_processed = process_content(services_content, 'services')
services_processed = re.sub(r'<title>.*?</title>', '<title>Leistungen – Schlüsselnotdienst Rhein-Selz</title>', services_processed, count=1)
services_processed = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Unsere Leistungen: Notöffnungen, Schlosswechsel, Einbruchschutz &amp; Schließanlagen für Rhein-Selz und Umgebung." />', services_processed, count=1)

pricing_processed = process_content(pricing_content, 'pricing')
pricing_processed = re.sub(r'<title>.*?</title>', '<title>Preise &amp; Ablauf – Schlüsselnotdienst Rhein-Selz</title>', pricing_processed, count=1)
pricing_processed = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Transparente Festpreise und fairer Ablauf ohne versteckte Kosten beim Schlüsselnotdienst Rhein-Selz." />', pricing_processed, count=1)

contact_processed = process_content(contact_content, 'contact')
contact_processed = re.sub(r'<title>.*?</title>', '<title>Einsatzgebiet &amp; Kontakt – Schlüsselnotdienst Rhein-Selz</title>', contact_processed, count=1)
contact_processed = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Einsatzgebiet und Kontakt – Schlüsselnotdienst Rhein-Selz. 24/7 Notruf unter 0160 91885082." />', contact_processed, count=1)

impressum_processed = re.sub(r'<title>.*?</title>', '<title>Impressum – Schlüsselnotdienst Rhein-Selz</title>', impressum_content, count=1)
impressum_processed = impressum_processed.replace('href="/" class="legal-brand">Lukas Sicherheitstechnik<', 'href="/" class="legal-brand">Schlüsselnotdienst Rhein-Selz<')

datenschutz_processed = re.sub(r'<title>.*?</title>', '<title>Datenschutzerklärung – Schlüsselnotdienst Rhein-Selz</title>', datenschutz_content, count=1)
datenschutz_processed = datenschutz_processed.replace('href="/" class="legal-brand">Lukas Sicherheitstechnik<', 'href="/" class="legal-brand">Schlüsselnotdienst Rhein-Selz<')

# Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_processed)

# Write new German files
with open('ueber-uns.html', 'w', encoding='utf-8') as f:
    f.write(about_processed)

with open('leistungen.html', 'w', encoding='utf-8') as f:
    f.write(services_processed)

with open('preise.html', 'w', encoding='utf-8') as f:
    f.write(pricing_processed)

with open('kontakt.html', 'w', encoding='utf-8') as f:
    f.write(contact_processed)

with open('impressum.html', 'w', encoding='utf-8') as f:
    f.write(impressum_processed)

with open('datenschutz.html', 'w', encoding='utf-8') as f:
    f.write(datenschutz_processed)

# Also create redirect stubs for the old English files so no 404s ever occur
redirect_template = '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
  <title>Weiterleitung – Schlüsselnotdienst Rhein-Selz</title>
</head>
<body>
  <p>Sie werden weitergeleitet zu <a href="{target}">{target}</a>...</p>
</body>
</html>'''

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(redirect_template.format(target='/ueber-uns.html'))

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(redirect_template.format(target='/leistungen.html'))

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(redirect_template.format(target='/preise.html'))

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(redirect_template.format(target='/kontakt.html'))

print("Migration completed successfully!")
