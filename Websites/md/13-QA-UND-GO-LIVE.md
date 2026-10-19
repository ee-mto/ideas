# QA & Go-Live

## 1. Abnahmekriterien

- [ ] Alle Pflichtseiten vorhanden und von jeder Seite erreichbar (Navigation vollständig)
- [ ] Sprechzeiten und Notfallhinweis auf der Startseite
- [ ] Impressum vollständig (inkl. Kammer, KV, Approbationsland), Datenschutzerklärung, Barrierefreiheitserklärung
- [ ] HWG-Check: keine Heilsversprechen, keine verbotenen Krankheitsbezüge, keine Fotos ohne Einwilligung
- [ ] Mobile-Ansicht geprüft, Ladezeit < 3 s
- [ ] SSL aktiv, HTTP→HTTPS-Umleitung, Security-Header gesetzt
- [ ] `sitemap.xml`, `robots.txt` und JSON-LD validiert
- [ ] Kontaktformular sendet an das Praxis-Postfach, DSGVO-Hinweis vorhanden

## 2. Automatische Prüfungen

```bash
# 1. Seite erreichbar + Statuscode
curl -sI https://www.domain.de/leistungen | head -1        # HTTP/2 200

# 2. Security-Header
curl -sI https://www.domain.de | grep -iE "strict-transport|x-frame|x-content|referrer|permissions"

# 3. JSON-LD vorhanden
curl -s https://www.domain.de/ | grep -o 'application/ld+json' | head -1

# 4. Verwaiste Links (Stichprobe): alle hrefs der Startseite crawlen
```

- **Lighthouse** (Desktop und Mobile): Performance, Accessibility, SEO, Best Practices jeweils ≥ 90
- **Rich Results Test** für JSON-LD, **W3C Nu Html Checker** für HTML
- **axe DevTools** für Barrierefreiheit
- **404-Test:** nicht existierende URL liefert die 404-Seite

## 3. Manuelle Tests

- **Formular:** echte Absendung an das Praxis-Postfach, Pflichtfelder, Honeypot (gefüllt), Fehlermeldung bei Versandfehler
- **Navigation:** jede Seite über das Menü erreichbar, aktiver Menüpunkt korrekt, Browser-Zurück funktioniert
- **Mobile:** iPhone- und Android-Stichprobe (Hamburger-Menü, Sprechzeiten-Tabelle, Termin-CTA ohne Scrollen sichtbar)
- **Zoom 200 %** ohne horizontales Scrollen, Tab-Navigation vollständig

## 4. Übergabe an die Praxis

- Kurzdokumentation: wie die Praxis online gefunden wird, wer der Ansprechpartner ist
- **Änderungsprozess:** Praxis meldet Änderungen (Sprechzeiten, Urlaub), der Dienstleister deployt – mit definierter Reaktionszeit
- Zugang zum Google Business Profile klären
- Erste Woche nach Go-Live: täglicher Kurzcheck (Formular, Verfügbarkeit, Analytics falls vorhanden)

## 5. Wartungsroutine (monatlich)

- [ ] Formularversand testen
- [ ] Sprechzeiten und Urlaubsvertretung aktuell?
- [ ] SSL gültig, Security-Header unverändert
- [ ] Uptime-Monitor ohne Alarme
- [ ] Abhängigkeiten und Build-Tools auf Sicherheitsupdates geprüft

## 6. Im neuen Stack

Die Prüfungen wandern in die Pipeline und werden damit für jede Praxis reproduzierbar:

| Prüfung | Umsetzung in der Pipeline |
| --- | --- |
| HTML-Validierung | Build schlägt fehl bei Validator-Fehlern |
| Links | Link-Check über alle generierten Seiten im CI-Job |
| Security-Header | Header-Check gegen die Staging-/Live-Domain |
| Performance | Lighthouse CI mit Budgets (LCP/CLS/INP, Bundle-Größe) |
| Barrierefreiheit | axe-CI im Build |
| Rechtstexte | Pflichtfeld-Prüfung: Impressum/Datenschutz/Barrierefreiheit vorhanden und gefüllt |

**Wichtig:** Automatische Prüfungen ersetzen die manuelle Abnahme nicht. Formularversand, Mobilansicht und die inhaltliche Freigabe durch die Praxis bleiben Handarbeit – sie sind der letzte Schritt vor dem Go-Live.
