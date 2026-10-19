# Recht & Compliance

Rechtliche Pflichten, Datenschutz und Barrierefreiheit einer Praxis-Website. **Kein Rechtsrat** – die Texte werden vor Go-Live von der Praxis geprüft und im Zweifel rechtlich finalisiert.

## 1. Relevante Gesetze

| Gesetz | Was es regelt | Relevanz |
| --- | --- | --- |
| **DSGVO** | Personenbezogene Daten, Informationspflichten (Art. 12–14), Betroffenenrechte, AV-Verträge (Art. 28) | Hoch – jede Website |
| **TTDSG § 25** | Cookies/Client-Speicherung: Einwilligung für nicht notwendige Zugriffe | Hoch – bei Tracking/Consent |
| **DDG § 5** (Nachfolger TMG) | Impressumspflicht (Anbieterkennzeichnung) | Hoch – Pflichtseite |
| **HWG** (Heilmittelwerbegesetz) | Werbegrenzen für Heilmittel und Behandlungen: § 3 irreführend, § 11 Nr. 7 Angstmache, § 11 Nr. 11 Äußerungen Dritter, § 12 Krankheitsliste (Anlage A); Bußgeld bis 50.000 € | Hoch – arztspezifisch |
| **MBO-Ä § 27** | Berufsrechtliches Werbeverbot: keine anpreisende, irreführende, vergleichende Werbung | Hoch – arztspezifisch |
| **UWG** | Unlauterer Wettbewerb (Abmahnungen) | Mittel |
| **BFSG** (seit 28.06.2025) | Barrierefreiheit von Dienstleistungen inkl. Websites (EN 301 549 / WCAG 2.1 AA), Barrierefreiheitserklärung | Hoch – Pflichtseite |
| **MStV § 18 Abs. 2** | Verantwortlichkeitsangabe im Impressum | Mittel |

## 2. Pflichtseiten (immer vorhanden)

1. **Impressum** – Name/Anschrift, Kontakt und die arztspezifischen Berufsangaben (Berufsbezeichnung, zuständige Ärztekammer, Kassenärztliche Vereinigung, Land der Approbation, geltende Berufsordnung). Fehlende Berufsangaben sind abmahnbar.
2. **Datenschutzerklärung** – Verantwortlicher, verarbeitete Daten, Rechtsgrundlagen, Betroffenenrechte, Hosting inkl. Auftragsverarbeitung (Art. 28 DSGVO).
3. **Barrierefreiheitserklärung** – nach BFSG Anlage 3 mit Feedback-Kontakt und Hinweis auf die Schlichtungsstelle.

## 3. HWG-Kernregeln

- **Informieren statt anpreisen** – keine Wirkversprechen („Heilung garantiert", „Erfolg sicher")
- **Keine Angstmacherei** (§ 11 Nr. 7) – „Ohne Vorsorge droht Krebs" ist unzulässig
- **Keine Krankengeschichten** in missbräuchlicher oder irreführender Weise (§ 11 Nr. 3), keine Vorher/Nachher-Darstellungen
- **§ 12 Anlage A:** Werbung zu bösartigen Neubildungen, Suchtkrankheiten, meldepflichtigen Infektionen und Schwangerschaftskomplikationen ist außerhalb der Fachkreise unzulässig → bei diesen Themen rein informativ bleiben
- **Äußerungen Dritter** (§ 11 Nr. 11): Patientenstimmen nur mit Einwilligung und nie anpreisend
- **Zuwendungen/Gewinnspiele** (§ 7): keine Verlosungen mit Arzneimittelbezug

## 4. Rechtstexte erstellen

Grundsatz: Die Texte im Template sind **Muster mit Platzhaltern** und werden je Praxis gefüllt und geprüft.

### Impressum (§ 5 DDG + Berufsrecht)

- Praxisname, Anschrift (Straße, PLZ, Ort), Telefon, E-Mail
- Berufsbezeichnung (Fachärztin/Facharzt für …)
- Zuständige Ärztekammer und Kassenärztliche Vereinigung
- Land der Approbation, Verweis auf die Berufsordnung
- Verantwortlich i. S. v. § 18 Abs. 2 MStV
- Optional: Umsatzsteuer-ID, Aufsichtsbehörde

> Kammer, KV und Approbationsland werden **bei der Praxis erfragt** – niemals aus Altbeständen übernommen oder geraten.

### Datenschutzerklärung

- Verantwortlicher (Name, Anschrift, Kontakt)
- Zugriffsdaten (IP, Datum/Uhrzeit, Seite, Browsertyp) – Rechtsgrundlage Art. 6 Abs. 1 lit. f DSGVO
- Kontaktformular: Zweck (Anfragebearbeitung, Art. 6 Abs. 1 lit. b), Speicherdauer, keine Weitergabe
- Cookies/Tracking: standardmäßig nur technisch notwendige Speicherung
- Hosting inkl. Auftragsverarbeitung (Art. 28 DSGVO) – Angabe des konkreten Hosters
- Rechte der Betroffenen (Art. 15–21) und Beschwerderecht bei der Aufsichtsbehörde
- Je Praxis ergänzen: Online-Terminbuchung, eingebundene Dienste, Fotoeinwilligungen

### Barrierefreiheitserklärung (BFSG Anlage 3)

- Stand der Vereinbarkeit mit EN 301 549 / WCAG 2.1 AA („weitgehend barrierefrei" + bekannte Einschränkungen)
- Feedback-Kontakt (E-Mail/Telefon der Praxis)
- Schlichtungsstelle: Bundesfachstelle für Barrierefreiheit
- Datum der Erstellung und letzten Überprüfung

## 5. Datenschutz-Default: keine externen Requests

Grundregel des Templates: **keine externen Requests, kein Tracking ohne Einwilligung** – damit entfällt ein Consent-Banner vollständig (TTDSG § 25).

| Baustein | Lösung | Warum |
| --- | --- | --- |
| Karten | OpenStreetMap-Link/-Embed oder statische Karte | Google Maps überträgt Daten an Google |
| Fonts | System-Stack oder selbst gehostete woff2 | Google Fonts = Request an Google |
| JS-Bibliotheken | lokal gehostet + SRI | kein CDN-Roundtrip, keine Fremdabhängigkeit |
| Analytics | keins (Default) | keine Einwilligung nötig, keine IP-Speicherung |
| Formular | `sende.php` (PHP-Mail) | keine Datenbank, kein Dritt-Anbieter |

**Falls Tracking gewünscht:** datensparsame, selbst gehostete Lösung bevorzugen (Plausible, Matomo mit IP-Anonymisierung), Consent-Layer einbinden, Datenschutzerklärung ergänzen (Zweck, Anbieter, Art. 6 Abs. 1 lit. a, Widerruf erreichbar halten).

Weitere Praxis-Fälle: Terminbuchung (Kapitel 07), Bewertungs-Widgets vermeiden und Portale nur sachlich verlinken, Newsletter nur mit Double-Opt-in (für Praxen meist unnötig), keine Social-Media-Buttons mit Tracking.

## 6. Barrierefreiheit (BFSG / WCAG 2.1 AA)

Seit 28.06.2025 gilt das BFSG auch für Praxis-Websites. Maßgeblich ist EN 301 549, Kern: WCAG 2.1 AA.

**Pflicht-Umsetzung im Template:**

- Kontraste ≥ 4,5:1 (Text), 3:1 (große Flächen/UI) – Markenfarben prüfen, dunklere Variante für Text
- Vollständige Tastaturbedienbarkeit, sichtbarer Fokus (`:focus-visible`)
- Semantisches HTML: eine H1 je Seite, `<nav>`, `<main>`, `<footer>`, `<time>`
- Alt-Texte für Bilder, dekorative Bilder `alt=""`, Icons `aria-hidden`
- Skip-Link „Zum Inhalt springen", `lang="de"`
- Formulare mit `label for`, verständlichen Fehlermeldungen, `aria-expanded` für Akkordeons

**Häufige Stolperfallen:** zu schwache Markenkontraste, „hier klicken"-Links, Nur-Hover-Interaktionen, Karussells ohne Pause, `div`-Spaghetti statt Semantik, PDF-Formulare ohne Textschicht.

**Prüfung:** axe DevTools, Lighthouse Accessibility ≥ 90, Tab-Navigation komplett, Zoom 200 % ohne horizontalen Scroll, Screenreader-Stichprobe (Startseite + Formular).

## 7. Checklisten

**Rechtstexte**
- [ ] Impressum mit Kammer, KV, Approbationsland und Verantwortlichem vollständig
- [ ] Datenschutzerklärung inkl. Hosting, Formular und Terminbuchung
- [ ] Barrierefreiheitserklärung mit Feedback-Kontakt und Schlichtungsstelle
- [ ] Praxis hat die Texte gegengelesen (OK dokumentiert), Stand-Datum geführt

**Datenschutz**
- [ ] Keine externen Ressourcen (DevTools → Network → keine Fremd-Domains)
- [ ] Kein Tracking ohne Consent-System
- [ ] Karte = OSM/statisch, Fonts lokal

**Barrierefreiheit**
- [ ] axe/Lighthouse ohne kritische Fehler
- [ ] Tab-Navigation und Fokus auf allen Seiten, Kontraste geprüft
- [ ] Zoom 200 % ohne Inhaltsverlust

## 8. Im Factory-Modell

- Rechtstexte sind **Praxis-Daten**: Impressum, Datenschutz und Barrierefreiheitserklärung liegen im Praxis-Repository und werden beim Onboarding strukturiert erfasst (Kammer, KV, Approbationsland, Ansprechpartner).
- Das zentrale Theme liefert die Muster und die Barrierefreiheits-Basis; Änderungen daran wirken über den Runner in alle Praxen.
- **Verantwortlichkeit bleibt bei der Praxis** (Inhalte und Rechtstexte), engel&engel betreut die Technik – das wird dokumentiert (Kapitel 12).
- Änderungen an Diensten (neue Terminbuchung, neues Tracking) erfordern immer ein Update der Datenschutzerklärung.
