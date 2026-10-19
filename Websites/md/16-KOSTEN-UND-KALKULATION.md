# Kosten & Kalkulation

> **Hinweis:** Die Zahlen in diesem Kapitel sind **Annahmen und Rechenbeispiele**, keine Angebote. Vor dem Verkauf werden sie mit echten Preisen (Hosting, Infrastruktur, Arbeitszeit) gefüllt.

## 1. Kostenblöcke

| Block | Bestandteile | Charakter |
| --- | --- | --- |
| **Infrastruktur** | Webhosting je Praxis (Modell A) **oder** VPS + Runner (Modell B), Domain, SSL, Backup | monatlich, fix |
| **Einrichtung** | Datenerfassung, Konfiguration, Inhalte, Bilder, Rechtstexte, QA, Go-Live | einmalig, Arbeitszeit |
| **Betrieb** | Wartung, Änderungen, Monitoring, Formular-Tests, Reporting | monatlich, Arbeitszeit |
| **Vertrieb** | Akquise, Erstgespräch, Angebot, Nachfassen | einmalig, Arbeitszeit |
| **Werkzeuge** | Design-/Bildbearbeitung, Monitoring, Passwort-Manager | monatlich, fix (geteilt) |

## 2. Annahmen für das Rechenbeispiel

| Größe | Annahme |
| --- | --- |
| Einrichtungsaufwand je Praxis | 1,5–3 Personentage (ohne Fototermin) |
| Wartungsaufwand je Praxis | 30–60 Minuten pro Monat |
| Änderungsaufwand | 15–30 Minuten pro Meldung |
| Hosting je Praxis (Modell A) | ab ca. 10 €/Monat |
| Infrastruktur (Modell B) | ein VPS + Runner für alle Praxen, mit echten Angeboten zu kalkulieren |
| Domain | ca. 10–15 €/Jahr (oft inklusive) |

## 3. Rechenbeispiel je Praxis (Modell A, Managed Service)

| Posten | Betrag |
| --- | --- |
| Hosting-Tarif | ca. 10 €/Monat |
| Wartung (45 Min/Monat, interner Stundensatz) | abhängig vom Satz |
| Kleinänderungen (Annahme 1–2 pro Monat) | abhängig vom Satz |
| **Deckungsbeitrag** | Monatspauschale minus Infrastruktur minus Arbeitszeit |

Bei einer Pauschale von 49 €/Monat bleiben nach Abzug von ca. 10 € Hosting rund 39 € vor Arbeitszeit. Das ist die zentrale Kennzahl: **Die Pauschale muss den tatsächlichen Betreuungsaufwand decken** – deshalb ist die Wartungsroutine (Kapitel 14) so kurz wie möglich zu halten.

## 4. Preisstufen

| Stufe | Leistung | Preisspanne (Beispiel) |
| --- | --- | --- |
| **Basis** | Website, Hosting, Domain, SSL, Wartung, Änderungen im Monatskontingent | 49–69 €/Monat |
| **Komfort** | zusätzlich erweitertes Änderungskontingent, priorisierte Umsetzung, kürzere Reaktionszeit | 79–99 €/Monat |
| **Premium** | zusätzlich Redaktionsservice, SEO-Betreuung, Reporting, kürzere Reaktionszeit | ab 129 €/Monat |

Dazu eine **einmalige Setup-Gebühr** (Onboarding, Texte, Bilder, Rechtstexte, Go-Live), die den Einrichtungsaufwand aus Abschnitt 2 abbildet.

## 5. Skaleneffekte

- **Modell A skaliert linear:** jede Praxis bringt eigenen Hosting-Aufwand und eigene Wartungszeit mit.
- **Modell B skaliert unterproportional:** Theme-Änderungen und Pipeline-Optimierungen wirken für alle Praxen gleichzeitig. Fixkosten (VPS, Runner) verteilen sich auf immer mehr Kunden.
- **Der eigentliche Hebel ist die Wartungszeit**, nicht das Hosting: Wenn die Routine je Praxis von 60 auf 20 Minuten sinkt, verdoppelt sich der Deckungsbeitrag, ohne dass ein Kunde mehr zahlt.

## 6. Risiken

| Risiko | Wirkung | Gegenmaßnahme |
| --- | --- | --- |
| Baukasten-Anbieter (ab wenigen Euro/Monat) | Preisdruck nach unten | Nutzen argumentieren: Rechtssicherheit, Betreuung, Sichtbarkeit – nicht „nur eine Website" |
| Preisverfall durch KI-Websites | Einstiegsangebote werden billiger | Fokus auf Betreuung, Haftung und Beratung statt auf reine Erstellung |
| Zu niedrige Pauschale bei steigender Änderungsfrequenz | Marge kippt | Änderungskontingent vertraglich definieren, Mehrbedarf bepreisen |
| Klumpenrisiko (Modell B) | ein Ausfall trifft alle Praxen | Redundanz, zweites Auslieferungsziel, dokumentierter Notfallplan |
