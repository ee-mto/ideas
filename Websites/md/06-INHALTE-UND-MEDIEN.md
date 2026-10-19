# Inhalte & Medien

Patientenzentrierte Inhalte, Bilder und Bewertungsmanagement für Praxis-Websites.

## 1. Leitprinzip: die 10-Sekunden-Regel

Ein Besucher muss in **unter 10 Sekunden** erkennen: Was ist das für eine Praxis, wie sind die **Sprechzeiten**, wie bekomme ich einen **Termin**, was gilt im **Notfall**. Alles andere ist sekundär – auch auf dem Smartphone, ohne Scrollen.

## 2. Seitenstruktur

| # | Seite | Kerninhalt |
| --- | --- | --- |
| 1 | Startseite | Hero (Fachbereich + Ort), Termin-CTA, Sprechzeiten-Kurzübersicht, Notfall-Banner, Kernleistungen |
| 2 | Leistungen | Kassen- und IGeL-Leistungen getrennt und verständlich |
| 3 | Team | Ärzt:innen mit Facharztbezeichnung, Foto (nur mit Einwilligung) |
| 4 | Sprechzeiten + Anfahrt | Tabelle, Parken, ÖPNV, Barrierefreiheit der Praxis |
| 5 | Termin | Telefonnummer groß, Online-Buchung, „Was mitbringen" |
| 6 | Notfall | 116117, 112, Akutsprechstunde, nächste Notaufnahme |
| 7 | Aktuelles | Urlaubsvertretung (der größte Anruf-Vermeider), Neuerungen |
| 8 | Patienteninfo | Formulare, Abläufe, Services |
| 9 | FAQ | echte Patientenfragen mit FAQ-Schema |
| 10 | Kontakt + Rechtliches | Impressum, Datenschutz, Barrierefreiheitserklärung |

## 3. Textregeln

- **Verständliche Sprache** – medizinische Begriffe erklären („DMP = strukturierte Betreuung bei chronischen Erkrankungen")
- **Sachlich, warm, persönlich** – „wir" statt institutionell; keine Superlative (HWG!)
- **Konkret statt generisch** – „Akutsprechstunde täglich 8–10 Uhr, ohne Termin" statt „gute Erreichbarkeit"
- **Handlungsorientiert** – CTAs wie „Termin vereinbaren", „Sprechzeiten ansehen"
- **Niedrige Hürden betonen** (Hausarzt) – „ohne Überweisung", „Hausbesuche möglich"
- **IGeL transparent** – Selbstzahler-Leistungen klar kennzeichnen und erklären

## 4. Schwerpunktseiten (Fachbereich-Spezialisierung)

Baukasten je Schwerpunktseite:

1. H1 fachlich + regional
2. Intro: für wen, warum wichtig (sachlich)
3. Anlässe als Aufzählung
4. Ablauf (Schritte, Dauer, Vorbereitung)
5. Leistungen im Detail (faktenbasiert)
6. FAQ (2–4 Fragen, FAQ-Schema)
7. CTA (Termin + Telefon)
8. Verwandte Themen (interne Links)

**HWG-Check:** informieren statt anpreisen – keine Heilungsversprechen, keine Angstmache, bei § 12-Krankheiten (Onkologie, Sucht …) rein informativ.

## 5. Bilder & Medien

### Rechtliches zuerst

| Motiv | Regel |
| --- | --- |
| Team-/Ärzt:innen-Fotos | schriftliche Einwilligung mit Zweck und Widerruf, DSGVO-konform aufbewahren |
| Patientenfotos | nur mit ausdrücklicher Einwilligung, nie im Werbekontext; bei Kindern zusätzlich Sorgeberechtigte |
| Vorher/Nachher | im medizinischen Werbekontext unzulässig (HWG § 11 Abs. 1 Nr. 3) |
| Stockfotos | Lizenz prüfen, keine Wasserzeichen, Lizenznachweis dokumentieren |
| Krankenhaus-/Gerätebilder | nur mit Einwilligung der Einrichtung, keine Logos ohne Freigabe |

### HWG-konforme Bildwahl

- seriös und menschenwürdig – keine schockierenden Krankheitsbilder, keine Leidens-Darstellungen
- keine Bilder, die Heilung oder Erfolg suggerieren
- keine Bilddarstellungen von Körperveränderungen in missbräuchlicher Weise (§ 11 Nr. 5)
- sachlich-informative Darstellungen von Behandlungen sind zulässig, anpreisende nicht

### Technische Anforderungen

- Formate: WebP/AVIF für Fotos, SVG für Logo und Icons
- Größe: Ziel < 200 KB pro Bild, Hero < 300 KB
- `width`/`height` immer setzen (kein Layout-Shift), `loading="lazy"` außer Hero, Hero mit `fetchpriority="high"`
- beschreibende Alt-Texte, dekorative Bilder `alt=""`
- Dateinamen klein, mit Bindestrich, ohne Umlaute (`dr-muster-sprechzimmer.webp`)

## 6. Bewertungen & Reputation

**Rechtlicher Rahmen:** HWG § 11 Nr. 11 – Äußerungen Dritter sind unzulässig, wenn sie missbräuchlich, abstoßend oder irreführend sind. Keine Fake-Bewertungen (UWG, Berufsrecht). Sachliche Verweise auf Jameda, Doctolib oder das Google-Business-Profil sind erlaubt.

**Empfohlene Praxis:**

1. Nicht zitieren, sondern verlinken – neutraler Linkblock („Bewertungen auf Jameda / Google"), keine Sterne-Widgets, die Fremddaten laden
2. Natürlich sammeln – die Praxis bittet nach dem Termin höflich um eine Bewertung, ohne Anreize
3. Portale pflegen – Jameda-, Doctolib- und GBP-Profil aktuell halten (Sprechzeiten, Fotos, Antworten)

**Umgang:** Positiv kurz und persönlich danken. Negativ zeitnah, sachlich und lösungsorientiert antworten – niemals öffentlich über medizinische Details (Schweigepflicht, § 203 StGB). Offensichtlich falsche Bewertungen bei der Plattform melden.

## 7. Checklisten

**Content**
- [ ] Sprechzeiten, Notfall und Termin-CTA in den ersten 10 Sekunden sichtbar (Desktop und Mobile)
- [ ] Texte in „Wir"-Form, verständlich, ohne Fachjargon-Wände
- [ ] Keine Heilsversprechen oder Anpreisungen (HWG-Review)
- [ ] Jede Schwerpunktseite folgt dem Baukasten
- [ ] Urlaubsvertretung aktuell gepflegt

**Bilder**
- [ ] Einwilligungen für alle Personenbilder liegen schriftlich vor
- [ ] Keine Vorher/Nachher- oder irreführenden Bilder
- [ ] Bilder als WebP/AVIF, < 200 KB, Dimensionen und Alt-Texte gesetzt
- [ ] Stock-Lizenzen dokumentiert

**Bewertungen**
- [ ] Keine ungenehmigten Patientenstimmen auf der Website
- [ ] Portale neutral verlinkt, keine Daten ladenden Widgets
- [ ] Antwort-Richtlinie für negative Bewertungen abgestimmt
- [ ] GBP-/Jameda-Daten konsistent mit der Website

## 8. Im Factory-Modell

- Inhalte liegen im **Praxis-Repository** (`/content`), Bilder als optimierte Assets daneben – dadurch bleibt das Theme für alle Praxen identisch.
- Der **Bild-Workflow** ist Teil des Onboardings: Bedarf klären, Einwilligungen einholen, konvertieren, Alt-Texte und Dimensionen hinterlegen.
- Die redaktionelle Pflege liegt zentral bei engel&engel – die Praxis meldet Änderungen formlos (Kapitel 03), die technische Betreuung steht in Kapitel 14.
