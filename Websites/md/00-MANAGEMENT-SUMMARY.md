# Management Summary — Praxis-Websites auf Jamstack-Basis

> **Vorlage für:** Geschäftsführung engel&engel gmbh
> **Stand:** Oktober 2026
> **Grundlage:** 17 Kapitel Konzept in `Websites/md/` — dieses Dokument ist die Kurzfassung für die Vorlage.

## 1. Worum es geht

Arztpraxen leiden unter schwerfälligen, wartungsintensiven WordPress-Systemen: Plugin-Schwachstellen, DSGVO- und HWG-Abmahnfallen, langsame Ladezeiten auf dem Smartphone. Wir setzen stattdessen auf **statische Praxis-Websites**: schnell, rechtssicher, in Deutschland gehostet, zentral gebaut und von uns betreut.

## 2. Ausgangslage

| Problem der Praxis | Wirkung |
| --- | --- |
| WordPress mit Plugins und Updates | laufende Wartung, Sicherheitslücken, Ausfälle |
| Langsame Ladezeiten | schlechtere Google-Platzierung, unbrauchbare Mobilansicht |
| Impressum, Datenschutz, HWG, Barrierefreiheit | Abmahnrisiko, unklare Verantwortung |
| Agenturverträge | lange Wartezeiten, hohe Rechnungen, keine festen Reaktionszeiten |

## 3. Unser Ansatz

Statische Website (HTML/CSS/JS) ohne Redaktionssystem und ohne Datenbank, zentral gebaut über eine Pipeline und aus deutschem Rechenzentrum ausgeliefert. **Die Pflege liegt bei uns:** Die Praxis meldet Änderungen formlos, wir setzen sie um, prüfen sie (Sprechzeiten, HWG, Rechtstexte) und stellen sie live. Die Praxis braucht keinen Zugang zu Technik und keine Einarbeitung.

## 4. Was wir damit verkaufen

1. **Geschwindigkeit** — Ladezeiten im Bereich einer Sekunde statt mehrerer Sekunden; bessere lokale Sichtbarkeit.
2. **Sicherheit** — keine Plugins, kein Redaktionssystem, keine Datenbank: kaum Angriffsfläche.
3. **Rechtssicherheit** — Impressum mit Berufsangaben, Datenschutz, Barrierefreiheitserklärung und HWG-konforme Texte von Anfang an.
4. **Betreuung** — feste Ansprechpartner und zugesagte Reaktionszeiten statt Wartungsvertrag ohne Inhalt.

## 5. Die Umsetzung

| Baustein | Rolle |
| --- | --- |
| **GitLab** | Repositories und Pipeline: Theme und Praxis-Daten versioniert, Builds reproduzierbar, Änderungen rückholbar |
| **Neuer VPS** (Hetzner Cloud oder Terra Cloud, deutsches Rechenzentrum) | Rechenleistung für Build und Auslieferung, DSGVO-konform |
| **Domains und DNS** (Hetzner) | Registrierung über Hetzner; Zonen und Einträge kostenlos per API — damit wird jede neue Praxis automatisiert ausgerollt |
| **Coolify** | Deployment, Domains, SSL-Zertifikate, Container |

Eine Praxis ist damit kein eigenes Hosting-Paket mehr, sondern ein Repository plus Domain auf einer gemeinsamen, zentral betriebenen Plattform.

## 6. Kosten je 10 Praxen

> Grobe Schätzung, keine Angebote. Coolify, GitLab und Hugo sind Open Source — es gibt **keine Lizenzkosten**.

| Posten | Größenordnung |
| --- | --- |
| VPS (Terra Cloud) inkl. Backup | ca. 30–80 €/Monat |
| Domains (10 × ca. 12 €/Jahr, Hetzner; DNS kostenlos) | ca. 10 €/Monat |
| KI-Nutzung (Claude, für Texte und Pflege) | ca. 20–120 €/Monat |
| **Sachkosten gesamt** | **ca. 60–210 €/Monat** |
| Arbeitszeit laufend | 8–15 Stunden/Monat |
| Arbeitszeit einmalig (Aufbau plus Einrichtung) | ca. 25–45 Personentage |

Das sind **6–21 € Sachkosten pro Praxis und Monat**. Der eigentliche Kostentreiber ist die Arbeitszeit, nicht die Technik — deshalb zählt jede Minute, die die Routine je Praxis kürzer wird (Vorlagen, Standardisierung, KI-Unterstützung).

Auf der Erlösseite stehen bei 10 Praxen 490–990 €/Monat (49–99 € je Praxis) plus die einmalige Setup-Gebühr.

## 7. Fahrplan

| Phase | Ziel |
| --- | --- |
| **Pilot** | eine reale Praxis vollständig umsetzen, Prozess dokumentieren |
| **3–10 Praxen** | Wiederholbarkeit beweisen, Aufwand je Praxis senken |
| **10–25 Praxen** | Entscheidung für die Factory, zentrale Pipeline einführen |
| **25–50+ Praxen** | Betrieb industrialisieren: Monitoring, Reporting, klare Reaktionszeiten |

## 8. Was wir vorschlagen

1. **Infrastruktur aufsetzen:** VPS bei Terra Cloud, Coolify, GitLab Runner — einmaliger Aufwand, danach trägt sie alle Praxen.
2. **Theme als Hugo-Theme umsetzen** — Voraussetzung für jede weitere Praxis.
3. **Pilotpraxis starten** und den Ablauf vollständig dokumentieren.
4. **Preisstufen wie skizziert einführen** und die Zahlen nach dem Pilot mit echten Werten nachrechnen.
5. **Betriebsprozess schriftlich fixieren:** Reaktionszeiten, Änderungskontingent, Störungsweg.
6. **Vergleichscheck als Vertriebseinstieg** — kostenlose Prüfung bestehender Praxis-Websites auf Ladezeit, Recht und Sichtbarkeit.

## 9. Nächste Schritte

- VPS aufsetzen, Coolify installieren, GitLab Runner registrieren
- Theme als Hugo-Theme umsetzen und eine Test-Praxis deployen
- Pilotpraxis auswählen und Daten aufnehmen
- Angebotsunterlage mit den Preisstufen erstellen
- Betriebs- und Wartungsprozess festhalten
