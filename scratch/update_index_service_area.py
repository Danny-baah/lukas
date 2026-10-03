new_section = """    <!-- ==========================================================================
         EINSATZGEBIET SECTION (RHEIN-SELZ REGIONAL)
         Map-dominant editorial section matching visual specification
         ========================================================================== -->
    <section class="service-area-editorial-section" id="service-area" aria-labelledby="einsatzgebiet-heading">
      
      <div class="service-area-container">
        
        <div class="service-area-editorial-grid">
          
          <!-- Area 1: Intro (Eyebrow, Main Heading, Supporting Lead Text) -->
          <div class="sa-intro-block">
            
            <!-- Eyebrow with Lukas red accent bar -->
            <div class="sa-eyebrow service-area-anim" data-anim="fade-up">
              <span class="sa-red-bar" aria-hidden="true"></span>
              <span class="sa-eyebrow-text">EINSATZGEBIET</span>
            </div>

            <!-- Main Editorial Headline (Playfair Display) -->
            <h2 id="einsatzgebiet-heading" class="sa-heading service-area-anim" data-anim="fade-up" style="--anim-delay: 0.1s;">
              Rhein-Selz.<br>
              Wir sind in <span class="accent-red">Ihrer Nähe.</span>
            </h2>

            <!-- Supporting Copy -->
            <p class="sa-lead service-area-anim" data-anim="fade-up" style="--anim-delay: 0.2s;">
              Zuverlässiger Service für Privathaushalte und Unternehmen in Nierstein, Oppenheim und allen umliegenden Orten der Verbandsgemeinde Rhein-Selz. Schnell vor Ort, persönlich und zuverlässig.
            </p>

          </div>

          <!-- Area 2: Regional Information Row (3 understated points) -->
          <div class="sa-info-row service-area-anim" data-anim="fade-up" style="--anim-delay: 0.25s;">
            
            <!-- Point 01: 20 Orte in der Region -->
            <div class="sa-info-item">
              <div class="sa-info-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#e1252b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
              </div>
              <div class="sa-info-text">
                <span class="sa-info-num">20</span>
                <span class="sa-info-label">ORTE IN DER<br>REGION</span>
              </div>
            </div>

            <!-- Point 02: Rhein-Selz Landkreis Mainz-Bingen -->
            <div class="sa-info-item">
              <div class="sa-info-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#e1252b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
              </div>
              <div class="sa-info-text">
                <span class="sa-info-title">RHEIN-SELZ</span>
                <span class="sa-info-sub">LANDKREIS<br>MAINZ-BINGEN</span>
              </div>
            </div>

            <!-- Point 03: Schnell vor Ort -->
            <div class="sa-info-item">
              <div class="sa-info-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#e1252b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <polyline points="12 6 12 12 16 14"/>
                </svg>
              </div>
              <div class="sa-info-text">
                <span class="sa-info-title">SCHNELL</span>
                <span class="sa-info-sub">VOR ORT</span>
              </div>
            </div>

          </div>

          <!-- Area 3: Right Map Block (Centerpiece) -->
          <div class="sa-map-block service-area-anim" data-anim="fade-up" style="--anim-delay: 0.15s;">
            <div class="sa-map-wrapper">
              <img 
                src="/images/service-area-rhein-selz-map.jpg" 
                alt="Redaktionelle Karte des Einsatzgebietes Rhein-Selz mit Nierstein, Oppenheim und den umliegenden 20 Gemeinden" 
                class="sa-map-image"
                loading="lazy"
              />
            </div>
          </div>

          <!-- Area 4: Location List (Unsere Einsatzorte - 20 Locations in 4 Columns) -->
          <div class="sa-locations-block service-area-anim" data-anim="fade-up" style="--anim-delay: 0.3s;">
            
            <div class="sa-locations-header">
              <span class="sa-red-bar" aria-hidden="true"></span>
              <h3 class="sa-locations-title">UNSERE EINSATZORTE</h3>
            </div>

            <!-- 4-Column Town List with Thin Vertical Separators -->
            <div class="sa-towns-grid">
              <div class="sa-town-col">
                <span class="sa-town-name">Dalheim</span>
                <span class="sa-town-name">Dexheim</span>
                <span class="sa-town-name">Dienheim</span>
                <span class="sa-town-name">Dolgesheim</span>
                <span class="sa-town-name">Dorn-Dürkheim</span>
              </div>
              <div class="sa-town-col">
                <span class="sa-town-name">Eimsheim</span>
                <span class="sa-town-name">Friesenheim</span>
                <span class="sa-town-name">Guntersblum</span>
                <span class="sa-town-name">Hahnheim</span>
                <span class="sa-town-name">Hillesheim</span>
              </div>
              <div class="sa-town-col">
                <span class="sa-town-name">Köngernheim</span>
                <span class="sa-town-name">Ludwigshöhe</span>
                <span class="sa-town-name">Mommenheim</span>
                <span class="sa-town-name">Nierstein</span>
                <span class="sa-town-name">Oppenheim</span>
              </div>
              <div class="sa-town-col">
                <span class="sa-town-name">Selzen</span>
                <span class="sa-town-name">Uelversheim</span>
                <span class="sa-town-name">Undenheim</span>
                <span class="sa-town-name">Weinolsheim</span>
                <span class="sa-town-name">Wintersheim</span>
              </div>
            </div>

          </div>

          <!-- Area 5: Regional Closing Line -->
          <div class="sa-closing-block service-area-anim" data-anim="fade-up" style="--anim-delay: 0.35s;">
            <span class="sa-gold-bar" aria-hidden="true"></span>
            <p class="sa-closing-text">VON DALHEIM BIS WINTERSHEIM. FÜR IHRE SICHERHEIT VOR ORT.</p>
          </div>

        </div>

      </div>
    </section>"""

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = None
end_idx = None

for i, line in enumerate(lines):
    if '<section class="service-area-section" id="service-area">' in line:
        start_idx = i
    if start_idx is not None and '</section>' in line and i > start_idx:
        end_idx = i
        break

if start_idx is not None and end_idx is not None:
    print(f"Found section from line {start_idx+1} to {end_idx+1}")
    # Also include comment above if any
    if 'EINSATZGEBIET SECTION' in lines[start_idx-2]:
        start_idx = start_idx - 3
    new_lines = lines[:start_idx] + [new_section + '\n'] + lines[end_idx+1:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully updated index.html!")
else:
    print(f"Could not find indices: start={start_idx}, end={end_idx}")
