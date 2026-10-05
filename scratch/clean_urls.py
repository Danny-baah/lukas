import glob
import re

files = ['index.html', 'ueber-uns.html', 'leistungen.html', 'preise.html', 'kontakt.html', 'impressum.html', 'datenschutz.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Replace .html in href links
    # Examples:
    # href="/ueber-uns.html" -> href="/ueber-uns"
    # href="/ueber-uns.html#section" -> href="/ueber-uns#section"
    # href="/kontakt.html#einsatzgebiet" -> href="/kontakt#einsatzgebiet"
    # href="/leistungen.html#notdienst" -> href="/leistungen#notdienst"
    # href="/datenschutz.html" -> href="/datenschutz"
    # href="/impressum.html" -> href="/impressum"
    
    c = c.replace('href="/ueber-uns.html"', 'href="/ueber-uns"')
    c = c.replace('href="/ueber-uns.html#', 'href="/ueber-uns#')
    c = c.replace('href="/leistungen.html"', 'href="/leistungen"')
    c = c.replace('href="/leistungen.html#', 'href="/leistungen#')
    c = c.replace('href="/preise.html"', 'href="/preise"')
    c = c.replace('href="/preise.html#', 'href="/preise#')
    c = c.replace('href="/kontakt.html"', 'href="/kontakt"')
    c = c.replace('href="/kontakt.html#', 'href="/kontakt#')
    c = c.replace('href="/impressum.html"', 'href="/impressum"')
    c = c.replace('href="/datenschutz.html"', 'href="/datenschutz"')
    c = c.replace('href="/about.html"', 'href="/ueber-uns"')
    c = c.replace('href="/services.html"', 'href="/leistungen"')
    c = c.replace('href="/pricing.html"', 'href="/preise"')
    c = c.replace('href="/contact.html"', 'href="/kontakt"')

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print("Updated all internal links to clean URLs without .html!")
