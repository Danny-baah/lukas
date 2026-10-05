files = ['index.html', 'ueber-uns.html', 'leistungen.html', 'kontakt.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    c = c.replace('alt="Lukas Sicherheitstechnik Fachkraft im Einsatz"', 'alt="Schlüsselnotdienst Rhein-Selz Fachkraft im Einsatz"')
    c = c.replace('alt="Lukas Abraham – Inhaber Lukas Sicherheitstechnik"', 'alt="Lukas Abraham – Schlüsselnotdienst Rhein-Selz"')
    c = c.replace('alt="Lukas Sicherheitstechnik Einsatzfahrzeug"', 'alt="Schlüsselnotdienst Rhein-Selz Einsatzfahrzeug"')
    c = c.replace('alt="Lukas Sicherheitstechnik Servicefahrzeug"', 'alt="Schlüsselnotdienst Rhein-Selz Servicefahrzeug"')
    c = c.replace('alt="Lukas Sicherheitstechnik – Hauseingang und Einsatzfahrzeug vor Ort"', 'alt="Schlüsselnotdienst Rhein-Selz – Hauseingang und Einsatzfahrzeug vor Ort"')
    c = c.replace('Lukas Sicherheitstechnik steht für persönliche Betreuung', 'Schlüsselnotdienst Rhein-Selz steht für persönliche Betreuung')
    c = c.replace('aria-label="Kontakt aufnehmen zu Lukas Sicherheitstechnik"', 'aria-label="Kontakt aufnehmen zu Schlüsselnotdienst Rhein-Selz"')
    c = c.replace('aria-label="Lukas Sicherheitstechnik anrufen unter 0160 91885082"', 'aria-label="Schlüsselnotdienst Rhein-Selz anrufen unter 0160 91885082"')
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print('Updated copy to Schlüsselnotdienst Rhein-Selz!')
